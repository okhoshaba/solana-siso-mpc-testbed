# Solana SISO MPC Testbed (private cluster)

This repository contains a reproducible testbed for studying a private Solana cluster as a controlled dynamical system.
Current stage: **SISO identification** and baseline **ARX** model for the channel **u_cmd → u_ach**.

## What is implemented
- Private Solana cluster on a VM (validator + RPC).
- Metrics exporter (Prometheus exposition) from `solana-latency-research`.
- Go-based transaction load generator (Fedora side) with HTTP control plane:
  - `POST /rate` (set lambda)
  - `GET /stats` (telemetry)
- Dashboard (Dash/Plotly) for live monitoring and interactive control.
- Step-test campaign scripts + dataset preparation for ARX identification.

## Architecture (high-level)
Fedora (controller host):
- loadgen (HTTP :7070)
- dashboard (HTTP :8050)
- analysis scripts

VM (Solana plant):
- solana-test-validator (RPC :8899)
- exporter (Prometheus /metrics :9464)

Connectivity:
- SSH tunnels from Fedora to VM forward ports 8899 and 9464.

## Signals
- **u_cmd(t)**: commanded transaction rate (lambda), set via `POST /rate`.
- **u_ach(t)**: achieved rate, computed from `Δsent_total/Δt` (preferred) and/or `sent_per_sec`.
- **y_lat(t)**: transaction confirmation latency `lat_p99` from Prometheus metric:
  `solana_transaction_latency_seconds{quantile="0.99"}`.
- **sat(t)**: saturation ratio `u_ach/u_cmd`.

## Quick start (Fedora)
1) Start SSH tunnels:
```bash
bash scripts/ssh_tunnels.sh

Start loadgen:

# see loadgen/RUN_LOADGEN.md

Sanity check endpoints:
bash scripts/sanity_check.sh

Run a step-test campaign:
HOLD=60 SAMPLE=2 LEVELS_STR="50 150 300 450 600 800 1000 800 600 450 300 150 50" \
bash scripts/step_test.sh | tee data/raw/step_test_$(date +%F_%H%M%S)_knee.csv

Build ARX dataset and fit model:
python3 analysis/fit_arx_stdlib.py data/processed/arx_dataset_knee.csv --na 2 --nb 2 --nk 1

Reproducibility
See REPRODUCIBILITY.md for exact versions, commands, and expected outputs.

License

Code: Apache-2.0
Data: CC-BY-4.0

How to cite
See CITATION.cff.

