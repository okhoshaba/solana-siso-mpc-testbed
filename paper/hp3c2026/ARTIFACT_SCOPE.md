# Artifact Scope for HP3C 2026

## Objective

This document defines the exact scope of the repository materials that support the HP3C 2026 paper.

## In-Scope Materials

The following materials are considered part of the paper artifact:

1. Synthetic-load experiments executed on the private blockchain testbed.
2. End-to-end measurements used for throughput, latency, saturation, and backlog analysis.
3. Processed tables and figures selected for the paper.
4. Scripts required to reproduce the selected processed results and figures.
5. Documentation required to understand the mapping from measurements to model variables.

## Out-of-Scope Materials

The following materials are not claimed as part of the paper contribution:

1. Full repository history and exploratory intermediate outputs.
2. Control-oriented extensions not directly used in the paper narrative.
3. Full internal reconstruction of the Solana validator pipeline.
4. Any claim requiring stage-level telemetry that is not present in the selected dataset.
5. Any future MIMO/MPC extensions not validated in this paper.

## Canonical Evidence Path

The paper should rely on a single canonical path from raw data to final figures:

- selected raw runs
- selected processed tables
- selected figure-generation scripts
- final figures used in the manuscript

Only these selected items should be cited in the paper-facing workflow.

## Permitted Claims

The artifact supports the following types of claims:

- bottleneck onset detection from end-to-end measurements
- identification of near-linear, knee, and saturation regimes
- throughput-latency degradation under synthetic load
- practical gray-box performance modeling in a controlled testbed

## Non-Permitted Claims

The artifact does not support the following claims unless new evidence is added:

- exact identification of internal Solana pipeline bottlenecks
- strict causal claims about account-lock contention
- strict causal claims about fee-priority scheduling
- complete white-box queueing reconstruction of the validator internals

## Canonical Dataset Rule

Before the paper is written, one and only one selected dataset path must be marked as canonical for:

- main plots
- main result table
- bottleneck onset analysis
- saturation discussion

Any alternative result files may remain in the repository, but they must not be part of the paper-facing path unless explicitly justified.
Only one canonical dataset path will be used in the paper.

## Freeze Rule

This document must be updated before the archival release is created.

