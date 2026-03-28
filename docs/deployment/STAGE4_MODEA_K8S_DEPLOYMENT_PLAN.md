# Stage 4 Mode A Kubernetes Deployment Plan

## 1. Purpose

This document defines the Stage 4 plan for reproducing the Project 1 baseline inside Kubernetes while preserving the scientific and operational logic of Mode A.

Stage 4 is the first stage in which the documented baseline begins to move into the Kubernetes environment created earlier.

Its purpose is not to redesign the object of study, but to reproduce the existing single-node research workflow in a controlled containerised form.

## 2. Stage 4 Goal

The goal of Stage 4 is to deploy the Mode A baseline inside Kubernetes in a way that preserves:

- the single-node nature of the environment;
- the logical order of operations established in Project 1;
- the current roles of validator, funding step, latency framework, load generator, scenario execution, dashboard, and metrics;
- the ability to compare baseline behaviour outside Kubernetes with baseline behaviour inside Kubernetes.

At the end of Stage 4, the project should have a working Kubernetes-based Mode A reproduction.

## 3. Scope of Stage 4

Stage 4 covers:

- workload mapping from the baseline to Kubernetes objects;
- deployment of Mode A components into the cluster;
- internal service connectivity for the reproduced baseline;
- execution of baseline-compatible scenarios;
- validation of functional equivalence relative to Project 1.

Stage 4 does **not** yet include:

- transition to multi-node Agave/Solana;
- validator set scaling;
- RPC layer redesign for Project 2;
- MIMO scaling of load generators;
- final publication packaging.

## 4. Stage 4 Principle

The main principle of Stage 4 is:

> reproduce first, optimise later.

This means:

- keep the environment as close as practical to the documented baseline;
- avoid redesigning component roles during the first migration;
- treat scientific comparability as more important than architectural elegance.

## 5. Mode A Restatement

Mode A remains defined as:

- a single-node Solana research environment;
- based on `solana-test-validator`;
- intended to preserve continuity with Project 1;
- used as the authoritative pre-Project-2 baseline.

The Kubernetes version of Mode A must still remain Mode A. It must not silently evolve into a different research object.

## 6. Workload Mapping Strategy

The current baseline components should be mapped into Kubernetes according to operational role.

## 6.1 Validator workload

Component:

- `solana-test-validator`

Recommended Kubernetes mapping:

- a stateful workload, or other carefully controlled pod-level deployment preserving local state expectations;
- persistent storage for the ledger path;
- explicit port exposure inside the cluster;
- external operator access only where needed.

Reasoning:

- the validator is the core stateful element of Mode A;
- the ledger path and restart behaviour must remain controlled.

## 6.2 Funding step

Component:

- payer funding procedure

Recommended Kubernetes mapping:

- one-shot Job

Reasoning:

- funding is an operational preparation step rather than a long-running service;
- Jobs reflect the current baseline logic more accurately than a permanently running container.

## 6.3 Latency framework workload

Component:

- `solana-latency-research`

Recommended Kubernetes mapping:

- Deployment or equivalent long-running managed workload

Reasoning:

- the framework behaves like an active service process during the experiment window;
- it is not the primary stateful blockchain workload, but it is part of the live experiment path.

## 6.4 Load generator workload

Component:

- `loadgen`

Recommended Kubernetes mapping:

- Deployment

Reasoning:

- Mode A currently uses a single load generator process;
- Stage 4 should preserve that single-generator assumption.

## 6.5 Scenario execution workload

Component:

- scenario scripts

Recommended Kubernetes mapping:

- one-shot Job or controlled operator-invoked job template

Reasoning:

- scenario execution is episodic;
- script execution is operationally closer to a batch job than to a service.

## 6.6 Dashboard workload

Component:

- dashboard / monitoring UI

Recommended Kubernetes mapping:

- Deployment plus controlled Service exposure

Reasoning:

- the dashboard is long-running while the experiment is active;
- it should be accessible to the operator in a controlled way.

## 6.7 Metrics and observability

Components:

- Prometheus
- metrics endpoints associated with the experiment

Recommended Kubernetes mapping:

- existing Stage 1 observability layer extended to include Mode A targets

Reasoning:

- observability must remain available during migration;
- metrics continuity is part of baseline validation.

## 7. Proposed Stage 4 Workload Set

The initial Mode A reproduction should aim for the following workload set:

- validator workload;
- funding Job;
- latency framework Deployment;
- load generator Deployment;
- scenario Job;
- dashboard Deployment;
- Prometheus scrape integration.

This is the minimum set needed to preserve the baseline logic inside Kubernetes.

## 8. Service and Connectivity Model

Inside Kubernetes, Stage 4 should replace the old VM-host SSH forwarding model with internal cluster communication.

Recommended connectivity principle:

- workloads communicate through cluster networking and Services;
- operator access is provided only where operationally required;
- local manual tunnelling should not remain the core inter-component communication mechanism.

Expected effects:

- validator RPC becomes an internal service endpoint;
- load generator and latency framework consume that endpoint inside the cluster;
- dashboard exposure is controlled and documented;
- metrics paths become part of the cluster observability model.

## 9. Configuration Management Principle

Stage 4 should separate image contents from runtime configuration.

Recommended direction:

- static configuration files placed in ConfigMaps where appropriate;
- secrets handled outside images;
- command-line arguments documented and controlled;
- environment-specific values clearly separated from code.

This matters because Stage 4 is the first point where runtime assumptions should begin transitioning from shell memory to declarative infrastructure.

## 10. Storage Principle

The validator’s state must remain deliberate and visible.

Recommended direction:

- explicit persistent storage for validator ledger state;
- clear documentation of where baseline data is stored;
- no accidental loss of state through ad hoc pod replacement unless that reset is intended.

Because Mode A often uses reset semantics, the storage policy must distinguish between:

- persistent operational storage; and
- deliberate clean-start experiment resets.

## 11. Operator Access Principle

Stage 4 should remain console-first and operationally disciplined.

Recommended operator access pattern:

- cluster administration through the designated operations path;
- dashboard access via controlled forwarding or service exposure;
- no unnecessary broad external exposure of experimental services.

This preserves the current administration model while adapting it to Kubernetes.

## 12. Stage 4 Deployment Sequence

Recommended high-level deployment order:

1. deploy validator workload;
2. verify validator startup and internal RPC availability;
3. execute funding Job;
4. deploy latency framework;
5. verify metrics and service communication;
6. deploy load generator;
7. deploy dashboard;
8. execute scenario Job;
9. validate observability and output behaviour;
10. compare outcomes against the documented baseline.

## 13. Functional Equivalence Targets

Stage 4 should preserve the following functional targets:

- validator starts successfully;
- payer funding succeeds;
- latency framework runs;
- load generator runs;
- scenario execution works;
- dashboard is reachable;
- metrics are available;
- experiment outputs are recognisable and comparable to the Project 1 baseline.

## 14. Stage 4 Acceptance Criteria

Stage 4 should be considered complete only if all of the following are true:

1. all Mode A baseline-critical components can be deployed inside Kubernetes;
2. the deployment sequence works in a repeatable way;
3. operator-visible services are reachable in the intended manner;
4. at least one baseline scenario completes successfully;
5. metrics are available during the run;
6. behaviour is close enough to the original baseline to support meaningful comparison.

## 15. Main Risks at Stage 4

The main risks are:

- accidentally changing the scientific object while migrating;
- introducing infrastructure complexity that breaks comparability;
- mismapping baseline steps into unsuitable workload types;
- losing visibility into metrics during migration;
- coupling runtime configuration too tightly to images.

## 16. Risk Mitigation Strategy

Recommended mitigation actions:

- preserve single-node logic;
- keep workload roles close to the documented baseline;
- validate each component independently before full-chain tests;
- compare Kubernetes behaviour with the original runbook;
- treat equivalence testing as mandatory rather than optional.

## 17. Recommended Repository Outputs

After Stage 4 planning, the repository should contain at least:

- `docs/deployment/STAGE4_MODEA_K8S_DEPLOYMENT_PLAN.md`
- `docs/deployment/MODEA_VALIDATION_CHECKLIST.md`

Optional but useful later:

- workload mapping notes;
- manifest inventory notes;
- deployment runbook.

## 18. Relation to Later Stages

Stage 4 is the first operational proof that the documented baseline can survive infrastructure migration.

It directly supports:

- Stage 5 publication-grade reproducibility;
- Stage 6 transition planning toward Project 2.

If Stage 4 fails to preserve comparability, later stages lose much of their scientific grounding.

## 19. Stage 4 Completion Statement

Stage 4 is complete when Mode A has been successfully reproduced inside Kubernetes in a repeatable, observable, and baseline-comparable form.

At that point, the project will have crossed the key transition from documentation and preparation into infrastructure-backed execution.
