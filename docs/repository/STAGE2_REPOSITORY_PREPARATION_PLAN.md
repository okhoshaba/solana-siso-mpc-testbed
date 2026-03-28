# Stage 2 Repository Preparation Plan

## 1. Purpose

This document defines the Stage 2 plan for preparing the existing repository for reproducible builds and later containerisation.

Stage 2 is the bridge between:

- infrastructure readiness established in Stage 1; and
- image-building and workload onboarding planned for later stages.

Its purpose is to move the project from a partially working, partly local, partly repository-based state to a repository structure that is suitable for disciplined engineering work.

## 2. Stage 2 Goal

The goal of Stage 2 is to make the repository **buildable, navigable, and containerisation-ready** without prematurely over-refactoring it.

At the end of Stage 2, the repository should:

- contain the real working code required for the current Project 1 baseline;
- have a clear structure by component;
- include reproducible build instructions;
- expose dependencies explicitly;
- support later Docker image creation with minimal additional repository surgery.

## 3. Scope of Stage 2

Stage 2 covers:

- identification of the real working codebase;
- synchronisation between local working code and GitHub repository state;
- structural cleanup of repository directories;
- separation of main components;
- addition of build instructions and dependency records;
- preparation for future Dockerfiles and image pipelines.

Stage 2 does **not** yet require:

- final publication-quality repository polish;
- final Zenodo packaging;
- complete Project 2 architecture material;
- full Kubernetes deployment of research workloads.

## 4. Repository Preparation Principle

Stage 2 should follow a pragmatic principle:

> first achieve reproducible buildability, then pursue structural elegance.

This means:

- do not wait for perfect repository beauty before making it usable;
- do not keep critical working code only on local machines;
- do not allow undocumented local patches to remain the real source of truth.

The repository must become the authoritative engineering baseline.

## 5. Current Problem Statement

At present, the project appears to have the following likely issues:

- some code exists in corrected local form but is not fully reflected in the public repository;
- runtime knowledge may be partly stored in operator memory or shell history;
- the component boundaries may be clearer operationally than structurally in the repository;
- build instructions may be implicit rather than formal;
- some future container targets may not yet have clearly separated source trees.

This is a typical pre-containerisation state and Stage 2 is specifically intended to resolve it.

## 6. Stage 2 Desired End State

The repository should reach the following condition.

### 6.1 Engineering clarity

The repository should make it obvious:

- what the components are;
- where their source code lives;
- how each component is built;
- how each component is configured;
- which components are baseline-critical.

### 6.2 Reproducible buildability

The repository should allow an operator or researcher to:

- identify the build target;
- install or resolve the dependencies;
- build the relevant binaries or applications;
- verify that the correct code is being built.

### 6.3 Containerisation readiness

The repository should be ready for later creation of:

- custom Docker images;
- runtime configuration packaging;
- repeatable build pipelines.

## 7. Stage 2 Component Targets

The following component groups should be treated as explicit repository targets.

### 7.1 Validator-related support assets

This may include:

- configs;
- helper scripts;
- baseline runtime notes;
- any supporting utilities required for the validator environment.

The validator binary itself may remain an upstream-provided component, but its repository-side supporting material must still be organised.

### 7.2 `solana-latency-research`

This is a critical Project 1 component and must be reconciled between:

- the corrected local working version; and
- the repository version.

Stage 2 must ensure that the repository contains the working private-network-relevant implementation or a documented, reproducible path to it.

### 7.3 Load generator

The source tree and build path for the load generator should be made explicit.

Stage 2 should clarify:

- exact source location;
- how the binary is produced;
- what runtime inputs are required;
- how the component will later become a container image.

### 7.4 Dashboard / controller components

The repository should clearly separate Python-based control and dashboard logic from other components.

Stage 2 should clarify:

- where dashboard code lives;
- where MPC-related control code lives;
- what Python dependencies are required;
- what entrypoints are used.

### 7.5 Scenario scripts

Scenario scripts should become clearly repository-managed operational assets.

Stage 2 should clarify:

- where the scripts live;
- how they are invoked;
- which environment variables they require;
- which components they expect to already be running.

## 8. Recommended Repository Structure Principle

Stage 2 should prefer a repository structure that reflects the real system structure.

Example principle:

- docs separated from code;
- components separated by runtime role;
- scripts kept explicit and discoverable;
- configuration files grouped in predictable locations.

The exact directory structure may vary, but the repository should no longer depend on operator intuition to be navigable.

## 9. Recommended Stage 2 Work Items

## 9.1 Identify authoritative working code

Tasks:

- determine which local code is the real working version;
- compare local working trees against the current repository state;
- identify missing commits, patches, or private corrections;
- decide what must be committed immediately.

## 9.2 Make component boundaries explicit

Tasks:

- separate load generator logic from dashboard logic;
- separate scenario scripts from application code;
- separate configuration assets from runtime binaries;
- define the main entrypoint for each component.

## 9.3 Record build instructions

Tasks:

- define build commands per component;
- define dependency files per component;
- define required toolchains;
- record these instructions in repository documentation.

## 9.4 Prepare for Dockerfiles

Tasks:

- ensure each future image target has a clean source root;
- ensure runtime config paths are clear;
- ensure secrets are not hardcoded into source;
- ensure the repository is ready for image-specific build contexts.

## 10. Recommended Documentation Outputs of Stage 2

Stage 2 should produce at least the following repository-facing artifacts:

- Stage 2 repository preparation plan;
- repository buildability checklist;
- component-level README files where needed;
- updated top-level README sections if the current repository structure is unclear.

Optional but useful artifacts:

- component dependency matrix;
- build command summary;
- container target mapping notes.

## 11. Recommended Technical Outputs of Stage 2

Stage 2 should aim to produce:

- corrected source code committed into the repository;
- explicit component directories;
- dependency files committed;
- repeatable local build commands;
- a repository state suitable for starting Dockerfile creation.

## 12. Acceptance Criteria for Stage 2

Stage 2 should be considered complete only if all of the following are true:

1. the repository contains the real working code required for the baseline;
2. the main components are structurally identifiable;
3. build commands are documented;
4. dependency information is documented or committed;
5. the repository is ready for Dockerfile creation;
6. critical local-only knowledge has been moved into version-controlled form.

## 13. Risks at Stage 2

The main risks are:

- incorrect local code remains outside the repository;
- too much time is spent on cosmetic refactoring;
- component boundaries remain ambiguous;
- hidden dependencies are not documented;
- future image creation is blocked by repository layout problems.

## 14. Risk Mitigation Strategy

Recommended mitigation actions:

- prioritise working code synchronisation over aesthetic refactoring;
- keep changes incremental and reviewable;
- preserve runability while restructuring;
- document build commands as soon as they are confirmed;
- avoid large uncontrolled repository rewrites.

## 15. Relation to Later Stages

Stage 2 directly enables:

- Stage 3 image creation and registry publication;
- Stage 4 Kubernetes workload onboarding;
- Stage 5 reproducibility and publication packaging.

If Stage 2 is weak, later stages will inherit unnecessary instability.

## 16. Stage 2 Completion Statement

Stage 2 is complete when the repository has become the authoritative, buildable, and containerisation-ready engineering source for the current Project 1 system.

At that point, the project can move with confidence into image-building work.
