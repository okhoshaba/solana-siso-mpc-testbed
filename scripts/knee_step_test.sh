#!/usr/bin/env bash
set -euo pipefail

# Defaults
HOLD="${HOLD:-60}"
SAMPLE="${SAMPLE:-2}"
WARMUP="${WARMUP:-0}"

# IMPORTANT: your loadgen expects {"lambda": ...}
RATE_KEY="${RATE_KEY:-lambda}"

LOADGEN_URL="${LOADGEN_URL:-http://127.0.0.1:7070}"
PROM_URL="${PROM_URL:-http://127.0.0.1:9464}"

LAT_METRIC="${LAT_METRIC:-solana_transaction_latency_seconds}"
LAT_QUANTILE="${LAT_QUANTILE:-0.99}"

LEVELS_STR="${LEVELS_STR:-50 150 300 450 600 800 1000 1200 1300 1450 1650 1850 1650 1450 1300 1200 1000 800 600 450 300 150 50}"

OUT="${OUT:-data/raw/knee_step_$(date +%F_%H%M%S).csv}"
mkdir -p "$(dirname "$OUT")"

echo "[knee_step_test] OUT=${OUT}"
echo "[knee_step_test] RATE_KEY=${RATE_KEY} HOLD=${HOLD}s SAMPLE=${SAMPLE}s WARMUP=${WARMUP}s"
echo "[knee_step_test] LEVELS_STR=${LEVELS_STR}"

python3 scripts/collect_csv.py \
  --loadgen-url "${LOADGEN_URL}" \
  --prom-url "${PROM_URL}" \
  --lat-metric "${LAT_METRIC}" \
  --lat-quantile "${LAT_QUANTILE}" \
  --rate-key "${RATE_KEY}" \
  --sample "${SAMPLE}" \
  step \
    --levels "${LEVELS_STR}" \
    --hold "${HOLD}" \
    --warmup "${WARMUP}" \
  | tee "${OUT}"

echo "[knee_step_test] Wrote ${OUT}"
