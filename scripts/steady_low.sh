#!/usr/bin/env bash
set -euo pipefail

SAMPLE="${SAMPLE:-2}"
DURATION="${DURATION:-600}"     # 10 минут
RATE="${RATE:-150}"             # стартовое значение (можно менять)

OUT="${OUT:-data/raw/steady_$(date +%F_%H%M%S)_low.csv}"

python3 scripts/collect_csv.py steady \
  --sample "${SAMPLE}" \
  --rate "${RATE}" \
  --duration "${DURATION}" \
  | tee "${OUT}"

echo "[ok] wrote ${OUT}"
