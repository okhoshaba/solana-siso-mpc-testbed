#!/usr/bin/env bash
set -euo pipefail

SAMPLE="${SAMPLE:-2}"
HOLD="${HOLD:-60}"
WARMUP="${WARMUP:-2}"

LEVELS_STR="${LEVELS_STR:-50 150 300 450 600 800 1000 800 600 450 300 150 50}"

OUT="${OUT:-data/raw/step_test_$(date +%F_%H%M%S)_knee.csv}"

python3 scripts/collect_csv.py step \
  --sample "${SAMPLE}" \
  --levels "${LEVELS_STR}" \
  --hold "${HOLD}" \
  --warmup "${WARMUP}" \
  | tee "${OUT}"

echo "[ok] wrote ${OUT}"
