#!/usr/bin/env bash
set -euo pipefail

# ===== User-tunable knobs =====
SAMPLE="${SAMPLE:-2}"          # sampling period (s)
DUR="${DUR:-30}"               # duration per probe rate (s)
START="${START:-200}"          # starting rate (tx/s)
MULT="${MULT:-1.5}"            # geometric growth factor
MAX="${MAX:-8000}"             # safety cap (tx/s)

# Loadgen control payload key for POST /rate
# If your loadgen expects {"lambda": ...}, run with: RATE_KEY=lambda
RATE_KEY="${RATE_KEY:-rate}"

# Stop criteria (conservative defaults)
SAT_STOP="${SAT_STOP:-0.92}"   # stop if median(u_ach/u_cmd) <= this
LAT_MULT="${LAT_MULT:-1.25}"   # stop if median(lat) >= LAT_MULT * baseline_lat
ERR_STOP="${ERR_STOP:-0.5}"    # stop if median(err_per_sec) >= this (if available)

# Minimum number of valid samples to trust medians
MIN_SAT_N="${MIN_SAT_N:-3}"
MIN_LAT_N="${MIN_LAT_N:-3}"
MIN_ERR_N="${MIN_ERR_N:-3}"

OUT="${OUT:-data/raw/knee_probe_$(date +%F_%H%M%S).csv}"

# URLs (must match your setup)
LOADGEN_URL="${LOADGEN_URL:-http://127.0.0.1:7070}"
PROM_URL="${PROM_URL:-http://127.0.0.1:9464}"

# ===== Helpers =====
median_py='
import csv,sys,statistics,math
path=sys.argv[1]
u_cmd=float(sys.argv[2])

sat=[]; lat=[]; err=[]
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
      if e != "":
        err.append(float(e))
    except:
      pass

def med(xs):
  return statistics.median(xs) if xs else float("nan")

# print: sat_med lat_med err_med sat_n lat_n err_n
print(f"{med(sat)} {med(lat)} {med(err)} {len(sat)} {len(lat)} {len(err)}")
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
level_idx=0

while (( rate <= MAX )); do
  level_idx=$((level_idx + 1))
  echo "[probe] rate=${rate} tx/s for ${DUR}s (sample=${SAMPLE}s, rate_key=${RATE_KEY})"

  tmp="$(mktemp)"

  # IMPORTANT: global options MUST come before subcommand "steady"
  python3 scripts/collect_csv.py \
    --loadgen-url "${LOADGEN_URL}" \
    --prom-url "${PROM_URL}" \
    --sample "${SAMPLE}" \
    --rate-key "${RATE_KEY}" \
    steady \
      --rate "${rate}" \
      --duration "${DUR}" \
    > "${tmp}"

  # Append (skip header)
  tail -n +2 "${tmp}" >> "${OUT}"

  # Compute medians + counts for this segment
  read sat_med lat_med err_med sat_n lat_n err_n < <(python3 -c "$median_py" "${tmp}" "${rate}")

  # Establish baseline latency from first segment with enough valid latency samples
  if [[ -z "${baseline_lat}" ]]; then
    if (( lat_n >= MIN_LAT_N )); then
      baseline_lat="${lat_med}"
      echo "[probe] baseline lat_p99 (median) = ${baseline_lat} s (lat_n=${lat_n})"
    fi
  fi

  echo "[probe] medians: sat=${sat_med} (n=${sat_n})  lat=${lat_med}s (n=${lat_n})  err=${err_med} (n=${err_n})"

  # Always skip stop checks on the first level (we need a bracket)
  if (( level_idx == 1 )); then
    prev_rate="${rate}"
    rate="$(python3 -c "$ceil_py" "${rate}" "${MULT}")"
    rm -f "${tmp}"
    continue
  fi

  # If baseline not available yet, keep probing
  if [[ -z "${baseline_lat}" ]]; then
    prev_rate="${rate}"
    rate="$(python3 -c "$ceil_py" "${rate}" "${MULT}")"
    rm -f "${tmp}"
    continue
  fi

  stop=0

  # sat check (only if we have enough sat samples and sat is not NaN)
  if (( sat_n >= MIN_SAT_N )); then
    python3 - <<PY >/dev/null || stop=1
import math
sat=float("${sat_med}")
thr=float("${SAT_STOP}")
if (not math.isnan(sat)) and sat <= thr:
  raise SystemExit(1)
PY
  fi

  # latency check (only if enough latency samples)
  if (( lat_n >= MIN_LAT_N )); then
    python3 - <<PY >/dev/null || stop=1
import math
lat=float("${lat_med}"); base=float("${baseline_lat}"); k=float("${LAT_MULT}")
if (not math.isnan(lat)) and lat >= k*base:
  raise SystemExit(1)
PY
  fi

  # error check (only if enough err samples and err is not NaN)
  if (( err_n >= MIN_ERR_N )); then
    python3 - <<PY >/dev/null || stop=1
import math
e=float("${err_med}"); thr=float("${ERR_STOP}")
if (not math.isnan(e)) and e >= thr:
  raise SystemExit(1)
PY
  fi

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
  echo "[probe] No saturation/latency trigger up to MAX=${MAX}."
  echo "[probe] Consider increasing MAX, or lowering thresholds, or verify RATE_KEY."
  exit 0
fi

echo "[probe] Trigger detected at rate=${trigger_rate}. Previous rate=${prev_rate:-unknown}."
echo

# ===== Suggest a refined LEVELS_STR around the knee neighborhood =====
export PREV_RATE="${prev_rate:-}"
export TRIG_RATE="${trigger_rate}"

python3 - <<'PY'
import os, statistics

prev_s = os.environ.get("PREV_RATE","").strip()
prev = float(prev_s) if prev_s else None
trig = float(os.environ["TRIG_RATE"])

k = trig
f = [0.6, 0.75, 0.9, 1.0, 1.1, 1.25, 1.4]

# round to nearest 50
levels = [max(50, int(round(k*x/50)*50)) for x in f]
levels = sorted(set(levels))

pre = [50,150,300,450,600,800,1000]
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
