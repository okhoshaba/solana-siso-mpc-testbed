# Stage 6 Project 2 Architecture Plan

## 1. Purpose

This document defines the Stage 6 architectural plan for Project 2.

Stage 6 is the point at which the project moves beyond:

- documentation of the Project 1 baseline;
- Kubernetes infrastructure preparation;
- repository buildability work;
- image strategy definition;
- Mode A reproduction planning;
- publication-oriented packaging.

Its purpose is to define the next research architecture: a multi-node Agave/Solana-based environment suitable for controlled, scalable, and instrumented experiments.

## 2. Stage 6 Goal

The goal of Stage 6 is to define a formally structured target architecture for Project 2 that is:

- scientifically meaningful;
- operationally manageable;
- scalable in a controlled way;
- clearly separated from the Project 1 baseline;
- suitable for later implementation inside the Kubernetes platform.

At the end of Stage 6, the project should have:

- a defined target object of study for Project 2;
- a clear separation between Mode A and the new target mode;
- a documented role model for validators, RPC nodes, load generators, controllers, jobs, observability, and registry services;
- a staged architectural direction for future execution work.

## 3. Why Stage 6 Matters

Project 2 is not simply a larger copy of Project 1.

The transition from:

- single-node `solana-test-validator`;

to:

- a multi-node Agave/Solana research environment

changes the object of study itself.

This means the project must not treat Stage 6 as a routine scale-up. It is a controlled architectural transition into a different class of system.

## 4. Stage 6 Principle

The main principle of Stage 6 is:

> separate baseline preservation from next-generation architecture.

This means:

- Mode A remains the reference baseline;
- Project 2 becomes a new research environment rather than an implicit mutation of Mode A;
- architectural growth must be documented as a change in the experimental object, not hidden as a mere infrastructure upgrade.

## 5. Target Research Mode

Stage 6 introduces the target mode for Project 2.

This target mode is defined as:

- a multi-node Agave/Solana-based research environment;
- capable of supporting controlled scaling experiments;
- designed for richer validator/RPC/load interaction than Mode A;
- suitable for future MIMO-oriented control and synthetic benchmark management.

For clarity, this document refers to that target as **Mode B**.

## 6. Relationship Between Mode A and Mode B

## 6.1 Mode A

Mode A remains:

- single-node;
- based on `solana-test-validator`;
- continuity-preserving for Project 1;
- the main comparison baseline.

## 6.2 Mode B

Mode B is:

- multi-node;
- intended for Project 2;
- architecturally distinct from Mode A;
- suitable for distributed and scalable experiments.

## 6.3 Why the separation is essential

The separation is necessary because changes in:

- validator topology;
- number of nodes;
- RPC separation;
- load generation architecture;
- orchestration model

may materially affect observed behaviour.

Therefore, any comparison between Mode A and Mode B must be treated as a comparison between distinct research environments.

## 7. Core Architectural Layers of Project 2

The target architecture for Project 2 should be described as a set of interacting layers.

## 7.1 Consensus layer

This layer contains the validator set.

Primary role:

- represent the blockchain network under study;
- process transactions;
- maintain the evolving distributed state of the research environment.

Recommended Kubernetes interpretation:

- validator workloads represented as stateful workloads;
- each validator instance treated as a distinct node identity rather than a fungible replica.

Key principle:

- scaling validators changes the experimental topology and therefore must be treated as a controlled research action.

## 7.2 RPC layer

This layer contains nodes that expose RPC services and may be separated from the consensus workload.

Primary role:

- serve RPC requests;
- isolate user or benchmark access from consensus-critical roles where appropriate;
- support observation and traffic routing in a more controlled way.

Recommended Kubernetes interpretation:

- separate workload class from the validator set;
- implemented as one or more dedicated RPC-oriented workloads.

Key principle:

- do not assume that all externally relevant traffic should be served directly by consensus validators.

## 7.3 Load generation layer

This layer contains synthetic benchmark generators.

Primary role:

- produce controlled transaction traffic;
- support configurable workload patterns;
- later enable multi-channel or MIMO-style experimental control.

Recommended Kubernetes interpretation:

- initially a deployment-based workload model;
- later expandable to multiple coordinated generators where required.

Key principle:

- scaling this layer should be deliberate and measurable, not accidental.

## 7.4 Control layer

This layer contains control logic and automation components.

Primary role:

- orchestrate scenarios;
- execute policy or controller logic;
- support adaptive workload control;
- later support MIMO research paths if required.

Recommended Kubernetes interpretation:

- controller-like workloads;
- job-triggering logic;
- configuration-driven experiment management.

## 7.5 Scenario execution layer

This layer contains the batch-style scenario runs.

Primary role:

- run discrete experimental procedures;
- apply specific parameter schedules;
- support step tests, adaptive tests, and future scenario families.

Recommended Kubernetes interpretation:

- Job-oriented execution model.

## 7.6 Observability layer

This layer contains Prometheus and associated monitoring functionality.

Primary role:

- monitor infrastructure;
- monitor experiment runtime;
- preserve metrics continuity;
- provide evidence for experiment correctness and later analysis.

Recommended Kubernetes interpretation:

- dedicated observability services with persistent storage where appropriate.

## 7.7 Artifact and image layer

This layer contains image registry and related artifact management.

Primary role:

- store custom and derived images;
- support reproducible deployments;
- preserve image provenance.

Recommended Kubernetes or infrastructure interpretation:

- internal registry or Harbor-backed model integrated with the cluster workflow.

## 8. Baseline Target Architecture for Project 2

The recommended baseline target architecture for Project 2 is:

- `validator-set` — stateful validator layer, starting from 3 instances;
- `rpc-set` — dedicated RPC layer, initially 1 to 2 instances;
- `faucet` or `payer-tools` — job-based preparation utilities;
- `latency-research` or equivalent controller-side services — managed service workload;
- `loadgen` — initially single instance, later expandable;
- `scenario-runner` — job-based experiment execution;
- `dashboard` — operator-facing monitoring service;
- `prometheus` — observability service with persistent data handling;
- `registry` or `harbor` — artifact/image support service.

This is the conceptual baseline for Project 2, not yet the final tuned production profile.

## 9. Validator Set Interpretation

The validator set must not be treated as a standard stateless replica group.

Important interpretation rule:

- each validator instance is an experimental node with identity, storage, and network role;
- increasing validator count changes the structure of the object under study;
- validator scaling therefore belongs to the experimental design, not only to infrastructure operations.

This has two consequences:

1. validator count should be selected by scenario or topology profile;
2. validator scaling should not be treated as a casual horizontal autoscaling event during core research runs.

## 10. RPC Layer Interpretation

The RPC layer should be designed as a distinct layer when possible.

Reasons:

- reduce overloading of validators with mixed roles;
- allow more controlled traffic exposure;
- support more realistic architectural experiments;
- create room for future routing and traffic-management logic.

The RPC layer is one of the major architectural differences between Project 1 and Project 2.

## 11. Load Generator Interpretation

The load generation layer should evolve in stages.

### Initial Project 2 form

- one load generator instance;
- controlled continuation of Project 1 logic;
- useful for architectural shakeout and early comparability.

### Later Project 2 expansion

- multiple coordinated generators;
- possible channel separation;
- support for MIMO-oriented control research.

This staged approach reduces risk while preserving future scalability.

## 12. Control and MPC Interpretation

The controller layer is expected to become more important in Project 2 than in Project 1.

Possible roles include:

- rate adaptation;
- scenario orchestration;
- workload balancing;
- coordinated multi-generator control;
- later MIMO policy execution.

The precise control architecture may evolve, but Stage 6 should already reserve a distinct conceptual layer for it.

## 13. Storage Interpretation

Project 2 requires more deliberate storage planning than Mode A.

Storage concerns include:

- validator state;
- ledger state;
- observability data;
- registry storage;
- experiment outputs.

Key principle:

- stateful experimental data paths must be made explicit rather than left as incidental side effects of pod execution.

## 14. Network Interpretation

Project 2 will depend more heavily on clear internal communication than Project 1.

Important network concerns include:

- validator-to-validator communication;
- RPC accessibility;
- generator-to-RPC paths;
- observability scraping paths;
- operator access boundaries.

The network must support distributed behaviour without turning the architecture into an uncontrolled exposure surface.

## 15. Scaling Interpretation

Project 2 scaling should be profile-driven.

This means the project should define explicit profiles such as:

- 3-validator profile;
- 5-validator profile;
- 1-RPC profile;
- 2-RPC profile;
- 1-loadgen profile;
- 2-loadgen or 4-loadgen profile for later experiments.

Scaling should be a declared property of a test design, not merely a convenience action.

## 16. Stage 6 Deliverables

Stage 6 should produce:

- a Project 2 architecture plan;
- a transition roadmap from Mode A to Mode B;
- a layer model for the target environment;
- an initial topology profile concept;
- a documented interpretation of scaling and node roles.

## 17. Stage 6 Acceptance Criteria

Stage 6 should be considered complete only if all of the following are true:

1. Mode B is clearly defined as distinct from Mode A;
2. the major architectural layers are identified;
3. validator, RPC, load, control, scenario, observability, and artifact roles are defined;
4. scaling is interpreted as part of experimental design;
5. the architecture is suitable for later implementation planning.

## 18. Risks at Stage 6

The main risks are:

- blurring the distinction between Project 1 baseline and Project 2 target;
- treating validator replicas as ordinary service replicas;
- scaling infrastructure before the research topology is well defined;
- overcomplicating the design prematurely;
- failing to document architectural assumptions clearly.

## 19. Risk Mitigation Strategy

Recommended mitigation actions:

- preserve Mode A explicitly;
- define Mode B as a new target architecture;
- treat scaling as a research parameter;
- use staged topology profiles rather than uncontrolled growth;
- document role boundaries before implementation.

## 20. Relation to Future Work

Stage 6 is the architectural bridge from the current transition platform to the future experimental platform.

It prepares the ground for:

- implementation of Mode B workloads;
- scaling-aware experiment design;
- more sophisticated controller research;
- richer publication material for Project 2.

## 21. Stage 6 Completion Statement

Stage 6 is complete when Project 2 has been defined as a clear, multi-layer, multi-node research architecture that is distinct from the Project 1 baseline and ready for later implementation planning.
