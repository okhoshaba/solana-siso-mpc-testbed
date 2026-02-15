#!/usr/bin/env bash
set -euo pipefail

LOADGEN_URL="${LOADGEN_URL:-http://127.0.0.1:7070}"
PROM_URL="${PROM_URL:-http://127.0.0.1:9464}"

HOLD="${HOLD:-60}"       # seconds per level
SAMPLE="${SAMPLE:-2}"    # seconds between samples
LEVELS_STR="${LEVELS_STR:-50 150 300 450 600 800 1000 800 600 450 300 150 50}"

echo "t_sec,u_cmd,sent_total,u_ach,lat_p99"

t0=$(date +%s)
prev_sent=""
prev_t=""

for u in ${LEVELS_STR}; do
  # set rate
  curl -sS -X POST "${LOADGEN_URL}/rate" -H 'Content-Type: application/json' \
    --data "{\"rate\": ${u}}" >/dev/null

  level_start=$(date +%s)
  while true; do
    now=$(date +%s)
    elapsed=$((now - level_start))
    if (( elapsed >= HOLD )); then
      break
    fi

    # pull stats from loadgen
    stats=$(curl -sS "${LOADGEN_URL}/stats")
    sent_total=$(echo "$stats" | sed -n 's/.*"sent_total":[ ]*\([0-9]*\).*/\1/p')
    if [[ -z "${sent_total}" ]]; then sent_total=""; fi

    # compute u_ach from sent_total
    t_sec=$((now - t0))
    u_ach=""
    if [[ -n "${prev_sent}" && -n "${sent_total}" && -n "${prev_t}" ]]; then
      dt=$((t_sec - prev_t))
      ds=$((sent_total - prev_sent))
      if (( dt > 0 )); then
        u_ach=$(python3 - <<PY
ds=${ds}; dt=${dt}
print(ds/dt)
PY
)
      fi
    fi

    # pull latency p99 from /metrics (very rough grep)
    lat_p99=$(curl -sS "${PROM_URL}/metrics" | awk '/solana_transaction_latency_seconds.*quantile="0.99"/ {print $2; exit}')

    echo "${t_sec},${u},${sent_total},${u_ach},${lat_p99}"

    prev_sent="${sent_total}"
    prev_t="${t_sec}"

    sleep "${SAMPLE}"
  done
done
