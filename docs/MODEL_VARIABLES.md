# Model Variables Mapping

## Purpose

This document maps repository metrics to the variables used in the HP3C 2026 paper model.

The goal is not to claim a full internal reconstruction of the validator pipeline, but to define a clear gray-box mapping from observed measurements to analytical variables.

## Variable Mapping

| Repository Metric | Paper Symbol | Meaning | Role in Model | Units |
|---|---|---|---|---|
| `u_cmd` or `lam_cmd` | `\lambda_{cmd}` | commanded input load | exogenous input rate | tx/s |
| `u_ach` | `\lambda_{ach}` | achieved throughput | effective output rate | tx/s |
| `lat_p99` or selected latency metric | `L` | end-to-end delay proxy | congestion indicator | ms |
| `inflight` | `B` | backlog proxy | queue growth indicator | count |
| `err_per_sec` | `E` | overload/error proxy | failure or stress indicator | 1/s |
| `u_ach / u_cmd` | `S` | saturation ratio | operating regime indicator | dimensionless |

## Modeling Interpretation

The paper uses a queueing-inspired gray-box interpretation:

- `\lambda_{cmd}` represents the imposed arrival pressure
- `\lambda_{ach}` represents the effective service/output behavior
- `L` captures end-to-end delay growth under congestion
- `B` captures backlog accumulation
- `S` helps distinguish near-linear, knee, and saturation regimes

## Effective Bottleneck Onset

The paper defines effective bottleneck onset as the transition region where one or more of the following become visible:

1. saturation ratio begins to decline materially
2. latency growth accelerates
3. backlog proxy begins sustained growth
4. achieved throughput no longer tracks commanded load approximately linearly

## Important Limitation

These variables support a gray-box performance model. They do not directly identify internal validator stages unless additional internal telemetry is introduced.

## Recommended Notation Consistency

The paper should use one notation consistently throughout:

- `\lambda_{cmd}` for commanded load
- `\lambda_{ach}` for achieved throughput
- `L` for delay proxy
- `B` for backlog proxy
- `S` for saturation ratio

Do not alternate between multiple symbol systems unless strictly necessary.

## To Be Finalized

Before manuscript drafting, this document should be updated with:

- the final chosen latency metric
- the final chosen backlog proxy
- the final formula for the saturation ratio
- any run-aggregation notation used in tables and figures

