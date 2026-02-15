#!/usr/bin/env bash
set -euo pipefail

# ===== User-tunable knobs =====
SAMPLE="${SAMPLE:-2}"          # sampling period (s)
DUR="${DUR:-30}"               # duration per probe rate (s)  (quick scouting)
START="${START:-200}"          # starting rate (tx/s)
MULT="${MULT:-1.5}"            # geometric growth factor
MAX="${MAX:-8000}"             # safety cap (tx/s)

# Stop criteria (conservative defaults)
SAT_STOP="${SAT_STOP:-0.92}"   # stop if median(u_ach/u_cmd) <= this
LAT_MULT="${LAT_MULT:-1.25}"   # stop if median(lat) >= LAT_MULT * baseline_lat
ERR_STOP="${ERR_STOP:-0.5}"    # stop if median(err_per_sec) >= this (if available)

OUT="${OUT:-data/raw/knee_probe_$(date +%F_%H%M%S).csv}"

# URLs (must match your setup)
LOADGEN_URL="${LOADGEN_URL:-http://127.0.0.1:7070}"
PROM_URL="${PROM_URL:-http://127.0.0.1:9464}"

# ===== Helpers =====
median_py='
import csv,sys,statistics,math
path=sys.argv[1]
u_cmd=float(sys.argv[2])
lat=[]; sat=[]; err=[]
with open(path,"r",newline="") as f:
  r=csv.DictReader(f)
  for row in r:
    try:
      uach=row.get("u_ach","").strip()
      l=row.get("lat_p99","").strip()
      e=row.get("err_per_sec","").strip()
      if uach and float(uach)>0 and u_cmd>0:
        sat.append(float(uach)/u_cmd)
      if l and float(l)>0:
        lat.append(float(l))
      if e:
        err.append(float(e))
    except: pass
def med(xs):
  return statistics.median(xs) if xs else float("nan")
print(f"{med(sat)} {med(lat)} {med(err)}")
'

ceil_py='
import math,sys
x=float(sys.argv[1]); mult=float(sys.argv[2])
print(int(math.ceil(x*mult)))
'

echo "[probe] writing cumulative CSV -> ${OUT}"
echo "t_iso,t_sec,u_cmd,sent_total,u_ach,lat_p99,inflight,err_per_sec" > "${OUT}"

baseline_lat=""

rate="${START}"
prev_rate=""
trigger_rate=""
while (( rate <= MAX )); do
  echo "[probe] rate=${rate} tx/s for ${DUR}s (sample=${SAMPLE}s)"

  tmp="$(mktemp)"
  # Collect a short steady segment
  python3 scripts/collect_csv.py steady \
    --loadgen-url "${LOADGEN_URL}" \
    --prom-url "${PROM_URL}" \
    --sample "${SAMPLE}" \
    --rate "${rate}" \
    --duration "${DUR}" \
    > "${tmp}"

  # Append (skip header)
  tail -n +2 "${tmp}" >> "${OUT}"

  # Compute medians for this segment
  read sat_med lat_med err_med < <(python3 -c "$median_py" "${tmp}" "${rate}")

  # Establish baseline latency from first segment with valid lat
  if [[ -z "${baseline_lat}" ]]; then
    if python3 - <<PY >/dev/null
import math
x=float("${lat_med}")
print(0 if (math.isnan(x) or x<=0) else 1)
PY
    then :; else
      baseline_lat="${lat_med}"
      echo "[probe] baseline lat_p99 (median) = ${baseline_lat} s"
    fi
  fi

  echo "[probe] medians: sat=${sat_med}  lat=${lat_med}s  err=${err_med}"

  # If baseline not available yet, continue probing
  if [[ -z "${baseline_lat}" ]]; then
    prev_rate="${rate}"
    rate="$(python3 -c "$ceil_py" "${rate}" "${MULT}")"
    rm -f "${tmp}"
    continue
  fi

  # Stop checks
  stop=0
  # sat check
  python3 - <<PY >/dev/null || stop=1
import math
sat=float("${sat_med}")
thr=float("${SAT_STOP}")
# If sat is NaN -> don't stop based on sat
if not math.isnan(sat) and sat <= thr:
  raise SystemExit(1)
PY

  # latency check
  python3 - <<PY >/dev/null || stop=1
import math
lat=float("${lat_med}"); base=float("${baseline_lat}"); k=float("${LAT_MULT}")
# If lat is NaN -> don't stop based on latency
if not math.isnan(lat) and lat >= k*base:
  raise SystemExit(1)
PY

  # error check (only if err not NaN)
  python3 - <<PY >/dev/null || stop=1
import math
e=float("${err_med}"); thr=float("${ERR_STOP}")
if not math.isnan(e) and e >= thr:
  raise SystemExit(1)
PY

  if (( stop == 1 )); then
    trigger_rate="${rate}"
    break
  fi

  prev_rate="${rate}"
  rate="$(python3 -c "$ceil_py" "${rate}" "${MULT}")"
  rm -f "${tmp}"
done

echo
echo "[probe] DONE. Cumulative log: ${OUT}"

if [[ -z "${trigger_rate}" ]]; then
  echo "[probe] No saturation/latency trigger up to MAX=${MAX}. Consider increasing MAX or MULT."
  echo "[probe] Suggested knee refinement: use the top tested rate as upper knee bound."
  exit 0
fi

echo "[probe] Trigger detected at rate=${trigger_rate}. Previous rate=${prev_rate:-unknown}."
echo

# ===== Suggest a refined LEVELS_STR around the bracket [prev_rate, trigger_rate] =====
# We build a symmetric sequence: low baseline -> ramp to bracket -> a few points around knee -> ramp down.
# Use factors around knee:
# 0.6k, 0.75k, 0.9k, 1.0k, 1.1k, 1.25k, 1.4k
python3 - <<PY
import math
prev = ${prev_rate if prev_rate else 'None'}
trig = ${trigger_rate}
k = trig
f = [0.6,0.75,0.9,1.0,1.1,1.25,1.4]
levels = [max(50,int(round(k*x/50)*50)) for x in f]  # round to nearest 50
# Ensure monotonic unique increasing
levels = sorted(set(levels))
# Add a small warm-up ladder before knee
pre = [50,150,300,450,600,800,1000]
# keep only those below first knee-level
pre = [x for x in pre if x < levels[0]]
up = pre + levels
down = list(reversed(pre + levels[:-1]))
seq = up + down
print("Suggested LEVELS_STR:")
print(" ".join(str(x) for x in seq))
print()
print("Suggested command (final knee step):")
print(f'HOLD=60 SAMPLE=2 LEVELS_STR="{ " ".join(str(x) for x in seq) }" bash scripts/knee_step_test.sh')
PY
