#!/usr/bin/env bash
set -euo pipefail

RPC_URL="${RPC_URL:-http://127.0.0.1:8899}"
PROM_URL="${PROM_URL:-http://127.0.0.1:9464/metrics}"
LOADGEN_URL="${LOADGEN_URL:-http://127.0.0.1:7070}"

echo "[check] RPC health: ${RPC_URL}"
curl -sS "${RPC_URL}" \
  -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"getHealth"}' | head -c 300 || true
echo
echo "[check] Prometheus metrics: ${PROM_URL}"
curl -sS "${PROM_URL}" | head -n 5
echo
echo "[check] Loadgen stats: ${LOADGEN_URL}/stats"
curl -sS "${LOADGEN_URL}/stats" | head -c 300 || true
echo
echo "[ok] sanity checks executed"
