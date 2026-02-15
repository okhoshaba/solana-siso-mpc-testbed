#!/usr/bin/env bash
set -euo pipefail

: "${VM_HOST:?Set VM_HOST (e.g. user@1.2.3.4)}"
: "${VM_SSH_PORT:=22}"

# Local forwards
RPC_L=8899
PROM_L=9464

# Remote ports on VM
RPC_R=8899
PROM_R=9464

echo "[tunnels] Forwarding localhost:${RPC_L}->${RPC_R}, localhost:${PROM_L}->${PROM_R} via ${VM_HOST}:${VM_SSH_PORT}"
ssh -N -L ${RPC_L}:127.0.0.1:${RPC_R} -L ${PROM_L}:127.0.0.1:${PROM_R} -p ${VM_SSH_PORT} "${VM_HOST}"
