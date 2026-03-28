# Success Criteria for Project 1 Baseline

## 1. Purpose

This document defines the formal success criteria for the Project 1 baseline environment.

It is intended to serve two purposes:

- to determine whether the current baseline environment is functioning correctly;
- to provide a reference for later comparison with the Kubernetes-based implementation.

## 2. Scope

The criteria in this document apply to Mode A only:

- single-node `solana-test-validator`;
- VM-host split architecture;
- manual but repeatable Project 1 workflow;
- baseline experiment execution using the existing benchmark components.

## 3. Baseline Environment Startup Success

The Project 1 baseline environment is considered successfully started only if all of the following conditions are satisfied.

### 3.1 Validator startup success

Success conditions:

- `solana-test-validator` starts without immediate fatal error;
- the validator remains running;
- RPC becomes reachable on `127.0.0.1:8899`.

### 3.2 Payer funding success

Success conditions:

- Solana CLI is configured to use `http://127.0.0.1:8899`;
- the payer public key is valid;
- `solana airdrop` completes successfully;
- the payer balance increases as expected after funding.

### 3.3 Latency framework startup success

Success conditions:

- `solana-latency-research` starts without immediate fatal error;
- the intended local configuration is accepted;
- the process remains active during the experiment.

### 3.4 SSH forwarding success

Success conditions:

- the SSH forwarding session starts successfully;
- no `ExitOnForwardFailure` error occurs;
- forwarded RPC and metrics ports are reachable from the host.

### 3.5 Metrics availability success

Success conditions:

- the metrics endpoint responds on the forwarded metrics port;
- the response is non-empty;
- the metrics output is suitable for Prometheus-style scraping.

### 3.6 Load generator startup success

Success conditions:

- the load generator starts without immediate fatal error;
- it can connect to the configured RPC endpoint;
- it can bind to its configured listen address;
- it remains available for scenario execution.

### 3.7 Dashboard startup success

Success conditions:

- the dashboard process starts successfully;
- the web interface becomes reachable on `http://127.0.0.1:8050`;
- the dashboard remains available during the experiment.

## 4. Experiment Execution Success

An experiment run is considered successful only if all of the following conditions are satisfied.

### 4.1 Scenario execution success

Success conditions:

- the selected scenario script starts correctly;
- the script accepts the intended parameters;
- the script runs through its logical sequence;
- the script completes normally or reaches its defined stop condition.

### 4.2 Load path continuity success

Success conditions:

- the load generator remains active during scenario execution;
- the validator remains reachable while load is applied;
- the RPC endpoint remains responsive throughout the meaningful part of the run.

### 4.3 Metrics continuity success

Success conditions:

- metrics remain reachable during the run;
- no unexplained loss of metrics occurs during the main experiment phase.

### 4.4 Monitoring continuity success

Success conditions:

- the dashboard remains available during the run;
- the operator can observe the benchmark process while it is active.

### 4.5 Output generation success

Success conditions:

- the experiment produces the expected runtime outputs;
- the run can be identified as completed rather than aborted;
- the operator can distinguish a valid run from a failed run based on command output and monitoring state.

## 5. Minimum Baseline Acceptance Criteria

The baseline environment is accepted as operational only if the following checklist is fully satisfied:

- validator starts;
- RPC health responds;
- payer funding succeeds;
- latency framework starts;
- SSH forwarding works;
- metrics endpoint is reachable;
- load generator starts;
- at least one scenario can be executed;
- dashboard is reachable.

## 6. Failure Conditions

The baseline environment is considered failed if any of the following occurs:

- validator does not start;
- RPC is unavailable when expected;
- payer funding fails in a previously working environment;
- latency framework exits unexpectedly;
- SSH forwarding cannot be established;
- metrics endpoint is unavailable without explanation;
- load generator does not start or immediately exits;
- scenario scripts fail before meaningful execution;
- dashboard does not become reachable.

## 7. Regression Indicators

The following are considered regressions relative to the Project 1 baseline:

- previously documented commands no longer work;
- the order of operations becomes insufficient for a working run without documented reason;
- funding or RPC behaviour becomes unstable;
- metrics availability degrades;
- dashboard availability degrades;
- experimental runs become less reproducible;
- a future Kubernetes-based reproduction differs materially without explanation.

## 8. Comparison Criteria for Future Kubernetes Migration

When Mode A is later reproduced in Kubernetes, the following comparison criteria must be applied.

### 8.1 Functional equivalence

The Kubernetes-based version must preserve:

- single-node logical structure;
- validator role;
- payer funding role;
- latency framework role;
- load generation role;
- scenario execution role;
- dashboard role;
- metrics visibility.

### 8.2 Operational equivalence

The Kubernetes-based version must preserve:

- the ability to start the full environment;
- the ability to run at least one step test and one adaptive test;
- the ability to observe RPC, metrics, and dashboard behaviour.

### 8.3 Scientific equivalence

The Kubernetes-based version must remain close enough to the baseline that comparison of results is meaningful.

This means:

- any architectural differences must be documented;
- any changed runtime assumptions must be documented;
- any materially different behaviour must be justified rather than ignored.

## 9. Interpretation Rules

The baseline should be interpreted conservatively.

This means:

- a partial startup is not a successful startup;
- a run that starts but cannot sustain the experiment is not a successful run;
- an unavailable metrics path is a failure for research purposes, even if the validator itself is still alive;
- any missing component that breaks observability or experiment control counts as a baseline failure.

## 10. Baseline Success Statement

The Project 1 baseline is considered valid and ready for use as a migration reference if:

- the full startup sequence can be executed in the documented order;
- the validator, funding, latency framework, SSH forwarding, metrics, load generator, and dashboard all function together;
- at least one benchmark scenario executes successfully;
- the resulting environment is stable enough to be used as the authoritative pre-Kubernetes reference point.
