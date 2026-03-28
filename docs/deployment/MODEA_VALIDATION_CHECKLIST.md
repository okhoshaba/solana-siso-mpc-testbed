# Mode A Validation Checklist

## 1. Purpose

This document defines the validation checklist for the Kubernetes-based reproduction of Mode A.

Its purpose is to determine whether the migrated Kubernetes deployment still behaves like the documented Project 1 baseline.

## 2. Validation Principle

Mode A in Kubernetes should be accepted only if it is:

- operationally working;
- observably working; and
- scientifically comparable to the original baseline.

A deployment that runs containers but no longer preserves the meaningful structure of the baseline should not be accepted as a valid Mode A reproduction.

## 3. Scope

This checklist applies to the Kubernetes-based Mode A environment only.

It covers:

- validator behaviour;
- funding step behaviour;
- latency framework behaviour;
- load generator behaviour;
- scenario execution behaviour;
- dashboard reachability;
- metrics continuity;
- baseline comparability.

## 4. Validator Validation

The validator portion of Mode A should be accepted only if:

- the validator workload starts successfully;
- the validator remains running;
- the internal RPC endpoint becomes reachable;
- the workload behaves consistently with baseline expectations;
- reset behaviour, if used, is deliberate and understood.

Failure examples:

- validator pod crash loop;
- RPC unavailable;
- ledger handling inconsistent with intended baseline behaviour.

## 5. Funding Job Validation

The funding step should be accepted only if:

- the funding Job executes successfully;
- the payer receives the intended funds;
- the Job can reach the validator RPC endpoint;
- the Job behaves as the Kubernetes equivalent of the baseline funding step.

Failure examples:

- Job cannot reach RPC;
- airdrop fails unexpectedly;
- payer balance is not updated as expected.

## 6. Latency Framework Validation

The latency framework should be accepted only if:

- its workload starts successfully;
- it connects to the intended internal RPC path;
- it remains active during the experiment window;
- it participates in the migrated baseline in the same functional role as before.

Failure examples:

- startup error due to hidden local assumptions;
- incorrect configuration;
- inability to communicate with the validator.

## 7. Load Generator Validation

The load generator should be accepted only if:

- it starts successfully;
- it connects to the intended RPC service;
- it preserves the single-generator assumption of Mode A;
- it remains stable during the scenario run.

Failure examples:

- the load generator cannot resolve or reach RPC;
- workload restarts unexpectedly;
- runtime parameters differ materially without documentation.

## 8. Scenario Execution Validation

Scenario execution should be accepted only if:

- the scenario Job starts correctly;
- the expected parameters are applied;
- the run completes or stops under a defined condition;
- the scenario remains functionally equivalent to the baseline script behaviour.

Failure examples:

- missing runtime inputs;
- premature Job failure;
- script logic depends on a filesystem layout not preserved in Kubernetes.

## 9. Dashboard Validation

The dashboard should be accepted only if:

- the dashboard workload starts successfully;
- the intended access path works;
- the operator can reach the interface;
- the dashboard remains usable during the run.

Failure examples:

- the dashboard is running but unreachable;
- required runtime dependencies were not carried into the image or deployment;
- service exposure is misconfigured.

## 10. Metrics Validation

Metrics continuity should be accepted only if:

- the expected metrics path is available;
- Prometheus can scrape the intended targets;
- metrics remain available throughout the experiment;
- observability remains sufficient to judge experiment correctness.

Failure examples:

- metrics disappear during the run;
- Prometheus cannot discover or scrape the relevant target;
- the migrated environment is operational but not observable.

## 11. End-to-End Validation

The Kubernetes-based Mode A reproduction should be accepted end-to-end only if all of the following are true:

- validator runs;
- funding succeeds;
- latency framework runs;
- load generator runs;
- dashboard is reachable;
- scenario execution succeeds;
- metrics are available;
- the overall run is recognisably equivalent to the original baseline.

## 12. Baseline Comparison Validation

The migrated Mode A environment should also be checked against the documented baseline.

Questions that must be answered positively:

- does the component role mapping remain faithful to the baseline?
- does the order of operations remain logically equivalent?
- are any behaviour changes documented?
- can at least one step test be reproduced meaningfully?
- can at least one adaptive test be reproduced meaningfully?

If major behavioural differences exist without documentation, validation should fail.

## 13. Minimum Acceptance Checklist

The Kubernetes-based Mode A reproduction should not be accepted unless all of the following are true:

- validator startup is successful;
- internal RPC is reachable;
- funding Job succeeds;
- latency framework starts and remains active;
- load generator starts and remains active;
- dashboard is reachable;
- at least one scenario executes successfully;
- Prometheus or equivalent observability remains functional;
- the run is comparable to the original baseline.

## 14. Failure Conditions

Mode A validation should fail if any of the following occur:

- core baseline components cannot be deployed;
- component roles are changed in an undocumented way;
- scenario execution is broken;
- metrics are unavailable;
- the migrated environment is operationally alive but scientifically incomparable.

## 15. Evidence to Record

When a Mode A Kubernetes validation run is accepted, the following evidence should be recorded:

- image references used;
- relevant manifest versions or repository state;
- validator startup evidence;
- funding success evidence;
- scenario execution record;
- dashboard access record;
- metrics availability record;
- notes on any accepted differences from the original baseline.

## 16. Recommended Repository Outputs

At minimum, the repository should contain:

- `docs/deployment/STAGE4_MODEA_K8S_DEPLOYMENT_PLAN.md`
- `docs/deployment/MODEA_VALIDATION_CHECKLIST.md`

Later it may also contain:

- manifest inventory;
- deployment runbook;
- comparison notes between bare baseline and Kubernetes baseline.

## 17. Final Statement

Mode A in Kubernetes should be treated as valid only when it preserves the documented baseline in a way that remains operationally sound and scientifically meaningful.

This checklist exists to prevent an infrastructure migration from being mistaken for a successful research-preserving reproduction when it is not.
