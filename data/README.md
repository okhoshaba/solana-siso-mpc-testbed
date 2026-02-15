
---

### `data/README.md`
```md
# Datasets

This folder contains raw experiment logs and processed datasets for identification.

## Raw CSV (`data/raw/`)
Produced by `scripts/step_test.sh` via `tee`.

Columns:
- `time` (HH:MM:SS) local time (Fedora)
- `lam_cmd` (tx/s): commanded lambda (u_cmd)
- `sent_per_sec_reported` (tx/s): loadgen reported throughput (may be noisy)
- `sent_total` (count): total sent transactions (monotonic counter)
- `u_ach(sent_calc)` (tx/s): achieved throughput computed as Δsent_total/Δt (preferred u_ach)
- `inflight` (count): outstanding txs in loadgen
- `err_per_sec` (1/s): error rate
- `lat_p99` (s): `solana_transaction_latency_seconds{quantile="0.99"}`

Notes:
- For identification, we recommend using `u_ach(sent_calc)` as plant input proxy, not `sent_per_sec_reported`.
- Missing values (`nan`) indicate a telemetry acquisition issue (tunnels down, bad JSON, etc).

## Processed datasets (`data/processed/`)
Prepared for ARX fitting. Typical columns:
- `t_sec`: time in seconds from start
- `u_cmd`
- `u_ach`
- `lat_p99`

Exact format is described in the corresponding dataset header.
