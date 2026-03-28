# Project 2 Transition Roadmap

## 1. Purpose

This document defines the roadmap for transitioning from the current Project 1 baseline environment to the Project 2 target architecture.

Its purpose is to make the change from Mode A to Mode B explicit, staged, and scientifically defensible.

## 2. Roadmap Principle

The main principle is:

> transition by controlled architectural steps, not by a single uncontrolled leap.

This means the project should preserve intermediate checkpoints so that:

- comparability is retained;
- regressions can be identified;
- architectural changes can be attributed to specific transitions.

## 3. Starting Point

The starting point for this roadmap is:

- documented Project 1 baseline;
- Stage 1 infrastructure planning;
- Stage 2 repository preparation;
- Stage 3 image strategy;
- Stage 4 Mode A deployment and validation path;
- Stage 5 reproducibility and publication preparation.

This means the roadmap assumes that Mode A has been preserved as the authoritative reference path.

## 4. Target Point

The target point is:

- a multi-node Agave/Solana-based research environment;
- validator, RPC, load generation, control, and observability layers separated conceptually and operationally;
- suitability for controlled scaling and later MIMO-related research.

## 5. Transition Logic

The transition should proceed through clearly separated phases.

## 5.1 Phase 0 — Preserve Mode A

Objective:

- keep the existing single-node baseline valid and documented.

Reason:

- this is the reference path needed for scientific comparison.

Completion condition:

- Mode A remains reproducible, documented, and operationally testable.

## 5.2 Phase 1 — Reproduce Mode A inside Kubernetes

Objective:

- ensure that the baseline survives infrastructure migration.

Reason:

- without this step, later differences may be caused by Kubernetes migration rather than by architectural evolution.

Completion condition:

- Mode A is validated inside Kubernetes and remains comparable to the original baseline.

## 5.3 Phase 2 — Prepare reusable images and manifests

Objective:

- make the runtime stack portable and repeatable.

Reason:

- later architecture work depends on controlled image and deployment discipline.

Completion condition:

- the major runtime components are image-backed and deployment-oriented.

## 5.4 Phase 3 — Introduce topology-aware design

Objective:

- separate the architecture into validator, RPC, load, control, scenario, and observability roles.

Reason:

- Mode B requires explicit role separation and cannot rely on Mode A’s simpler assumptions.

Completion condition:

- the role model is documented and accepted.

## 5.5 Phase 4 — Introduce initial multi-node validator profile

Objective:

- move from single-node to a first controlled validator topology.

Recommended initial target:

- 3-validator profile

Reason:

- this is the smallest meaningful architectural shift into distributed-node behaviour.

Completion condition:

- the 3-validator profile is defined, deployed, and understood as a distinct experimental mode.

## 5.6 Phase 5 — Introduce separated RPC layer

Objective:

- move benchmark-facing or operator-facing RPC responsibilities away from direct validator-only assumptions.

Recommended initial target:

- 1-RPC or 2-RPC profile

Reason:

- this supports cleaner role separation and richer traffic experiments.

Completion condition:

- validator and RPC roles are no longer conflated by default.

## 5.7 Phase 6 — Introduce scalable load generation profiles

Objective:

- evolve from single-generator assumptions toward a multi-generator model where needed.

Recommended sequence:

- 1-loadgen profile
- 2-loadgen profile
- later 4-loadgen profile if justified

Reason:

- multi-generator logic should be introduced gradually and measured carefully.

Completion condition:

- generator scaling is profile-driven and documented.

## 5.8 Phase 7 — Introduce richer control logic

Objective:

- extend controller logic beyond simple single-generator assumptions.

Possible future direction:

- coordinated rate control;
- policy-driven orchestration;
- MIMO-related control research.

Completion condition:

- controller architecture becomes a distinct experimental layer rather than a helper script bundle.

## 5.9 Phase 8 — Expand topology profiles cautiously

Objective:

- move beyond the initial 3-validator profile only when justified.

Recommended later target:

- 5-validator profile

Reason:

- larger topologies should be introduced only after smaller ones are understood operationally and scientifically.

Completion condition:

- expanded topology is supported by resources, documentation, and experiment design.

## 6. Transition Rules

The following rules should govern the roadmap.

### 6.1 Do not discard Mode A

Mode A should remain available for comparison as long as Project 2 interpretation depends on the historical baseline.

### 6.2 One major architectural change at a time

Avoid introducing:

- multi-node validators;
- separated RPC;
- multi-generator scaling;
- controller redesign

all at once.

That would make attribution of behavioural changes difficult.

### 6.3 Treat topology as a research parameter

Validator count, RPC count, and loadgen count should be selected deliberately per profile.

### 6.4 Document every transition boundary

At each phase, record:

- what changed;
- why it changed;
- what remained constant;
- how the new phase differs from the baseline.

## 7. Recommended Topology Profiles

The following profiles are recommended as a controlled roadmap.

### Profile A0

- Mode A
- single-node validator
- single load generator
- baseline dashboard and metrics

Purpose:

- preserve Project 1 baseline.

### Profile B1

- 3 validators
- 1 RPC
- 1 load generator
- observability retained

Purpose:

- first distributed Mode B profile.

### Profile B2

- 3 validators
- 2 RPC
- 1 load generator
- controller layer more explicit

Purpose:

- introduce cleaner client-facing architecture.

### Profile B3

- 3 validators
- 2 RPC
- 2 load generators

Purpose:

- first controlled move toward multi-channel traffic generation.

### Profile B4

- 5 validators
- 2 RPC
- 2 or more load generators

Purpose:

- richer distributed environment once smaller profiles are stable.

## 8. Evidence Requirements During Transition

At each transition phase, the project should record:

- manifests or deployment state;
- image references;
- topology profile used;
- workload roles;
- metrics availability;
- operator notes on behaviour changes.

This is necessary for later analysis and publication.

## 9. Main Risks During Transition

The main risks are:

- losing comparability by changing too much at once;
- overinterpreting infrastructure changes as scientific effects;
- underdocumenting role changes;
- exhausting server resources before topology discipline is established;
- allowing the target architecture to drift without a formal roadmap.

## 10. Risk Mitigation Strategy

Recommended mitigation actions:

- keep phases explicit;
- scale gradually;
- preserve a reference baseline;
- record each topology profile carefully;
- validate each phase before moving to the next.

## 11. Recommended Repository Outputs

After Stage 6 planning, the repository should contain at minimum:

- `docs/project2/STAGE6_PROJECT2_ARCHITECTURE_PLAN.md`
- `docs/project2/PROJECT2_TRANSITION_ROADMAP.md`

Optional but useful later:

- topology profile matrix;
- role mapping notes;
- Project 2 implementation backlog.

## 12. Transition Completion Statement

The transition roadmap is complete when the project has a disciplined path from the documented single-node baseline to a controlled, multi-layer, multi-node Project 2 architecture.

This roadmap does not itself complete Project 2, but it makes Project 2 implementation possible in a traceable and scientifically coherent way.
