# Dataset schema (v1)

## Raw log CSV (data/raw/*.csv)
Raw is an experiment log sampled every `SAMPLE` seconds.

**Required columns (preferred canonical names):**
- `t_sec` (float): seconds from experiment start
- `u_cmd` (float): commanded tx rate, tx/s
- `sent_total` (int): total sent transactions (monotonic counter)
- `u_ach` (float): achieved tx rate, tx/s (if not present, computed from Δsent_total/Δt)
- `lat_p99` (float): confirmation latency p99, seconds (may be empty if telemetry failed)

**Optional columns:**
- `inflight` (int)
- `err_per_sec` (float)

**Allowed aliases (accepted by converters):**
- `lam_cmd` -> `u_cmd`
- `sent_per_sec_reported` -> ignored (not used for identification)

## Processed dataset CSV (data/processed/*.csv)
Strict input for identification & plotting.

**Required columns:**
- `t_sec` (float)
- `u_cmd` (float)
- `u_ach` (float)
- `lat_p99` (float)

Rules:
- No missing values in required columns.
- Sampling is approximately constant (tolerance ±25%).
- `sent_total` monotonicity is checked in raw.
