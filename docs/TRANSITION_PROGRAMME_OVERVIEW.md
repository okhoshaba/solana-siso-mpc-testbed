# Solana Transition Platform: From Project 1 to Project 2

## Overview

This repository contains the engineering and research transition programme for moving from the current Project 1 Solana research stand toward a more structured, containerised, Kubernetes-backed platform and, later, toward the multi-node Project 2 architecture.

The repository is designed to preserve scientific continuity while gradually improving:

- documentation quality;
- infrastructure discipline;
- repository buildability;
- image lifecycle management;
- Kubernetes deployment readiness;
- reproducibility and publication readiness.

In other words, this repository is not only a codebase. It is also the formal transition framework from a working single-node experimental environment to a more advanced research platform.

## Current High-Level Objective

The current high-level objective is to preserve the working Project 1 baseline and then move through a staged transition process that leads to:

- a reproducible Kubernetes-backed Mode A baseline;
- controlled image and deployment workflows;
- a later, clearly defined multi-node Mode B architecture for Project 2.

## Research Modes

The repository distinguishes between two research modes.

### Mode A

Mode A is the continuity mode inherited from Project 1.

It is:

- single-node;
- based on `solana-test-validator`;
- the main comparison baseline;
- intended to preserve the operational and scientific logic of Project 1.

### Mode B

Mode B is the target mode for Project 2.

It is:

- multi-node;
- based on Agave/Solana architecture;
- intended for richer scaling experiments;
- intended for future validator/RPC/load/controller separation and expansion.

These two modes must not be confused with each other. Mode B is not merely a larger Mode A. It is a different research architecture.

## Repository Purpose

This repository exists to support the following programme:

1. formalise the baseline;
2. prepare the infrastructure;
3. prepare the repository for reproducible builds;
4. define image discipline;
5. reproduce Mode A in Kubernetes;
6. prepare the project for release and publication;
7. define the architectural direction of Project 2.

## Documentation Entry Points

The main documentation entry points are:

- `docs/MASTER_ROADMAP.md`
- `docs/DOCUMENT_INDEX.md`

Recommended reading order:

1. `docs/MASTER_ROADMAP.md`
2. `docs/baseline/`
3. `docs/infrastructure/`
4. `docs/repository/`
5. `docs/images/`
6. `docs/deployment/`
7. `docs/publication/`
8. `docs/project2/`

## Repository Documentation Structure

The repository documentation is organised into the following major areas:

- `docs/baseline/` — Project 1 baseline, runbook, success criteria, component inventory
- `docs/infrastructure/` — Stage 1 Kubernetes infrastructure planning and acceptance materials
- `docs/repository/` — Stage 2 repository preparation and buildability materials
- `docs/images/` — Stage 3 image strategy and publication policy
- `docs/deployment/` — Stage 4 Mode A deployment and validation materials
- `docs/publication/` — Stage 5 reproducibility and publication materials
- `docs/project2/` — Stage 6 Project 2 architecture and transition roadmap

## Stage Overview

### Stage 0 — Baseline formalisation

Defines the current Project 1 environment in formal, version-controlled form.

### Stage 1 — Infrastructure preparation

Defines the Kubernetes infrastructure foundation and VM planning.

### Stage 2 — Repository preparation

Defines the steps needed to make the repository buildable and containerisation-ready.

### Stage 3 — Image strategy

Defines the image taxonomy, registry model, and publication rules for images.

### Stage 4 — Mode A reproduction in Kubernetes

Defines how the baseline should be reproduced in Kubernetes without changing the research object.

### Stage 5 — Reproducibility and publication

Defines how the project should be packaged for release, archival, and reuse.

### Stage 6 — Project 2 architecture

Defines the target multi-node architecture and the transition roadmap to that future state.

## Operational Interpretation

At this stage, the repository contains the planning and documentation framework for the full transition programme.

This means that the repository already defines:

- what the baseline is;
- what infrastructure is needed;
- how the repository should be prepared;
- how images should be handled;
- how the baseline should later be deployed into Kubernetes;
- how the project should later be packaged and published;
- how the target Project 2 architecture should be understood.

However, planning documents do not replace implementation. Practical execution still requires:

- real infrastructure deployment;
- real repository reconciliation;
- real image builds;
- real Kubernetes manifests;
- real validation runs;
- real release packaging.

## Suggested Immediate Next Steps

The most practical next steps for the project are:

1. maintain the baseline documents as authoritative references;
2. execute or validate the Stage 1 infrastructure setup;
3. reconcile the local working code with the repository;
4. begin preparing Docker build targets for the main custom components;
5. later move into Kubernetes-based Mode A execution.

## Intended Audience

This repository is written for:

- the primary researcher;
- collaborators;
- supervisors;
- technical reviewers;
- future maintainers;
- later external readers of release or archival packages.

## Documentation Philosophy

The repository follows a simple documentation philosophy:

- preserve working knowledge;
- convert operator memory into version-controlled artifacts;
- make engineering decisions explicit;
- preserve scientific comparability;
- separate baseline preservation from future architecture growth.

## Final Statement

This repository is the structured transition path from a working Project 1 Solana research stand to a more disciplined, containerised, reproducible, and extensible Project 2-oriented research platform.

For the full programme view, start with:

- `docs/MASTER_ROADMAP.md`
- `docs/DOCUMENT_INDEX.md`
