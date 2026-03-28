# Master Roadmap for Transition from Project 1 to Project 2

## 1. Purpose

This document provides the master roadmap for the full transition programme from Project 1 to Project 2.

Its purpose is to unify all previously defined stages into one coherent planning document that can be used as the top-level navigation and governance artifact for the repository.

It should be read together with the stage-specific documents, but it is intended to answer the high-level question:

> What is the overall plan, in what order should work proceed, and what does successful completion of the transition programme look like?

## 2. Programme Objective

The overall objective of the programme is to move from:

- a working but partly manual Project 1 research stand based on a single-node `solana-test-validator`;

toward:

- a structured, containerised, Kubernetes-backed transition platform;
- a reproducible engineering and publication workflow;
- a later multi-node Agave/Solana-based Project 2 architecture.

This transition must preserve scientific continuity while also increasing engineering maturity.

## 3. Programme Principle

The central principle of the programme is:

> preserve the baseline, formalise the infrastructure, stabilise the engineering workflow, then expand the research architecture.

This principle prevents premature architectural change from destroying the comparability and interpretability of the existing research results.

## 4. Global Stage Overview

The programme is divided into the following stages.

### Stage 0
Formalise the Project 1 baseline and success criteria.

### Stage 1
Define and prepare the Kubernetes infrastructure foundation.

### Stage 2
Prepare the repository for reproducible builds and later containerisation.

### Stage 3
Define image strategy, registry usage, and publication discipline for images.

### Stage 4
Reproduce Mode A inside Kubernetes while preserving baseline comparability.

### Stage 5
Prepare the project for reproducibility-oriented release and publication.

### Stage 6
Define the Project 2 target architecture and the transition roadmap from Mode A to Mode B.

## 5. Stage Dependency Logic

The stages are not independent. Their dependency structure is intentional.

### 5.1 Stage 0 -> all later stages

Without a documented baseline, later migration cannot be evaluated scientifically.

### 5.2 Stage 1 -> Stage 4

Without infrastructure, Kubernetes-based reproduction cannot occur.

### 5.3 Stage 2 -> Stage 3 and Stage 4

Without a buildable repository, image creation and clean deployment are unstable.

### 5.4 Stage 3 -> Stage 4 and Stage 5

Without image discipline, Kubernetes deployment and release reproducibility both become weak.

### 5.5 Stage 4 -> Stage 5 and Stage 6

Without a valid Kubernetes-based Mode A reproduction, later publication and architectural transition lose their baseline anchor.

### 5.6 Stage 5 and Stage 6

These stages have different purposes:

- Stage 5 packages and stabilises what has been done;
- Stage 6 defines what comes next architecturally.

They are related, but they are not interchangeable.

## 6. Stage-by-Stage Summary

## 6.1 Stage 0 — Baseline Formalisation

Purpose:

- make Project 1 explicit and version-controlled.

Main outputs:

- technical baseline;
- runbook;
- success criteria;
- component inventory.

Why it matters:

- creates the authoritative pre-migration reference.

Completion meaning:

- the project baseline exists as documentation rather than memory.

## 6.2 Stage 1 — Infrastructure Foundation

Purpose:

- establish the Kubernetes-capable execution environment.

Main outputs:

- Stage 1 infrastructure plan;
- VM role matrix;
- execution checklist;
- cluster acceptance checklist.

Why it matters:

- creates the controlled environment in which migration can later happen.

Completion meaning:

- the infrastructure platform exists and is ready for workload onboarding.

## 6.3 Stage 2 — Repository Preparation

Purpose:

- make the repository the authoritative buildable source.

Main outputs:

- repository preparation plan;
- buildability checklist;
- repository restructuring and dependency clarification.

Why it matters:

- removes the gap between local working code and version-controlled engineering truth.

Completion meaning:

- the repository is buildable and ready for image work.

## 6.4 Stage 3 — Image Strategy

Purpose:

- define how runtime artifacts will be built, named, published, and reproduced.

Main outputs:

- image strategy and registry plan;
- image tagging and publication policy.

Why it matters:

- prevents image drift and deployment ambiguity.

Completion meaning:

- the project has a controlled image workflow.

## 6.5 Stage 4 — Mode A Reproduction in Kubernetes

Purpose:

- move the baseline into Kubernetes without changing the scientific object.

Main outputs:

- Mode A deployment plan;
- Mode A validation checklist;
- later, manifests and deployment runbooks.

Why it matters:

- proves that the baseline can survive infrastructure migration.

Completion meaning:

- a valid Kubernetes-based Mode A exists and remains comparable to the original baseline.

## 6.6 Stage 5 — Reproducibility and Publication

Purpose:

- transform the project from an internal engineering effort into a release-grade research package.

Main outputs:

- Stage 5 reproducibility and publication plan;
- Zenodo release checklist;
- later, artifact inventory and release notes.

Why it matters:

- increases archival value, reviewability, and research continuity.

Completion meaning:

- the project can be released and archived as a coherent reproducibility package.

## 6.7 Stage 6 — Project 2 Architecture

Purpose:

- define the next-generation research architecture.

Main outputs:

- Project 2 architecture plan;
- transition roadmap from Mode A to Mode B.

Why it matters:

- prevents Project 2 from becoming an undocumented mutation of Project 1.

Completion meaning:

- the target multi-node architecture is defined as a distinct research environment.

## 7. Mode Logic Across the Programme

The programme distinguishes between two modes.

## 7.1 Mode A

Mode A is the Project 1 continuity mode.

It is:

- single-node;
- based on `solana-test-validator`;
- the scientific comparison baseline.

It appears most strongly in:

- Stage 0;
- Stage 4;
- Stage 5.

## 7.2 Mode B

Mode B is the Project 2 target mode.

It is:

- multi-node;
- based on Agave/Solana architecture;
- a distinct research object.

It appears most strongly in:

- Stage 6.

## 7.3 Why the distinction matters

This distinction ensures that:

- infrastructure migration is not confused with research-object change;
- scaling is interpreted as experiment design, not merely as operations;
- Project 2 claims can still be traced back to a meaningful baseline.

## 8. Recommended Programme Execution Order

The recommended execution order is:

1. complete Stage 0 documentation;
2. establish or validate Stage 1 infrastructure;
3. complete Stage 2 repository preparation;
4. implement Stage 3 image discipline;
5. execute Stage 4 Mode A reproduction and validation;
6. package the stable state through Stage 5;
7. begin Stage 6 implementation planning for Project 2.

This is the preferred sequence because it preserves both engineering and scientific discipline.

## 9. Current Practical Interpretation

At the current planning level, the project can be interpreted as follows:

- Stage 0 has produced the formal baseline documentation.
- Stage 1 has produced the infrastructure planning and acceptance framework.
- Stage 2 has produced the repository-preparation framework.
- Stage 3 has produced the image discipline framework.
- Stage 4 has produced the deployment and validation planning framework.
- Stage 5 has produced the reproducibility and publication planning framework.
- Stage 6 has produced the architectural transition framework for Project 2.

This means the repository now contains a strong planning skeleton for the entire transition programme.

## 10. What Remains Beyond Documentation

Even with all stage documents in place, the programme still requires practical execution in the following categories:

- real infrastructure deployment;
- real repository reconciliation and restructuring;
- real image builds and pushes;
- real Kubernetes manifests and workload deployment;
- real validation runs;
- real release packaging;
- real Project 2 implementation.

The documents define the programme. They do not replace the implementation work.

## 11. Recommended Repository Structure

A practical high-level documentation structure is:

- `docs/baseline/`
- `docs/infrastructure/`
- `docs/repository/`
- `docs/images/`
- `docs/deployment/`
- `docs/publication/`
- `docs/project2/`

This master roadmap should live at a visible top-level documentation entry point such as:

- `docs/MASTER_ROADMAP.md`

or, if preferred:

- `docs/overview/MASTER_ROADMAP.md`

## 12. Governance Use

This document can be used as:

- a top-level planning reference;
- a supervisor-facing summary;
- a review aid;
- a project governance artifact;
- a bridge between engineering work and dissertation-oriented structure.

## 13. Programme Success Criteria

The transition programme should be considered successful only if all of the following become true over time:

1. the Project 1 baseline remains documented and comparable;
2. the infrastructure is real, not merely planned;
3. the repository becomes the authoritative engineering source;
4. images become controlled and reproducible artifacts;
5. Mode A is successfully reproduced inside Kubernetes;
6. the project becomes release- and archive-ready;
7. Project 2 architecture becomes explicit and implementable.

## 14. Final Programme Statement

This roadmap defines the full structured path from a working but partly manual Project 1 research stand to a disciplined, containerised, reproducible, and architecturally extensible Project 2 transition platform.

It exists to ensure that the project develops in a way that is:

- scientifically interpretable;
- operationally disciplined;
- documentable;
- reproducible;
- extensible.
