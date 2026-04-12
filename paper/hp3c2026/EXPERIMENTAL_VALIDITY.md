# Experimental Validity and Threats to Validity

## Purpose

This document records the main threats to validity affecting the HP3C 2026 paper artifact and explains how they are handled.

## Main Threats to Validity

### 1. Background Server Load

Observed differences across measurement runs may be partially explained by non-identical background load on the host or validator environment at different times.

This factor is treated as an uncontrolled confounder unless explicitly logged and quantified for a given run.

### 2. Environment Drift

If software versions, runtime configuration, or infrastructure conditions changed between runs, the measured operating points may not be fully comparable.

### 3. End-to-End Observability Limit

The current paper-facing dataset is based primarily on end-to-end measurements. Therefore, internal stage-level bottlenecks inside the validator pipeline cannot be directly identified unless additional telemetry is added.

### 4. Synthetic Workload Bias

The workload is synthetic and controlled. This improves repeatability, but it may not reflect all real-world transaction mixes or contention patterns.

## Consequences for Interpretation

Because of the above limitations, the paper should interpret its findings as follows:

- the model identifies effective bottleneck onset
- the model characterizes saturation behavior
- the model does not prove exact internal micro-bottlenecks without stage-level observability
- cross-run discrepancies must be interpreted cautiously

## Mitigation Measures

The following measures are recommended or already used:

- repeated runs at the same operating point
- summary statistics across runs
- explicit selection of canonical runs
- run documentation and environment notes
- sanity checks before experiment execution
- stable software versions during the selected paper runs

## Recommended Additional Controls

If feasible before submission, add:

- host CPU utilization logs
- host memory utilization logs
- disk and network activity logs
- background process snapshots
- validator health snapshots before each run

## What the Paper Can Safely Claim

The paper can safely claim:

- end-to-end bottleneck onset detection
- saturation regime identification
- throughput-latency degradation trends under synthetic load
- usefulness of a queueing-inspired gray-box model

## What the Paper Should Not Claim

The paper should not claim:

- exact internal stage attribution
- strict causal attribution to account-lock contention
- strict causal attribution to fee scheduling
- exact white-box reconstruction of the validator pipeline

## Update Policy

This document should be revised whenever new telemetry or environment-control evidence is added.

