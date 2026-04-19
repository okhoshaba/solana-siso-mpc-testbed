# Documentation Overview

## Purpose

This file is the entry point for the repository documentation under `docs/`.

Its purpose is to make the documentation tree readable as a structured system rather than as a loose collection of markdown files.

## Primary Entry Documents

Start with these two files:

- `REPOSITORY_STATUS.md`
- `MASTER_ROADMAP.md`
- `DOCUMENT_INDEX.md`

These files provide:

- the formal archival status and successor-repository split;
- the full transition programme logic;
- the dependency order of the stages;
- the index of all major stage documents.

## Documentation Areas

## 1. Baseline

Path:

- `docs/baseline/`

Purpose:

- formalise the Project 1 baseline;
- record the runbook;
- define success criteria;
- define the component inventory.

Main files:

- `TECHNICAL_BASELINE.md`
- `RUNBOOK_PROJECT1.md`
- `SUCCESS_CRITERIA.md`
- `COMPONENT_INVENTORY.md`

## 2. Infrastructure

Path:

- `docs/infrastructure/`

Purpose:

- define the Stage 1 Kubernetes platform;
- define VM roles;
- define infrastructure execution and acceptance logic.

Main files:

- `STAGE1_KUBERNETES_PLAN.md`
- `VM_ROLE_MATRIX.md`
- `STAGE1_EXECUTION_CHECKLIST.md`
- `CLUSTER_ACCEPTANCE_CHECKLIST.md`

## 3. Repository Preparation

Path:

- `docs/repository/`

Purpose:

- define how the repository becomes buildable and ready for containerisation.

Main files:

- `STAGE2_REPOSITORY_PREPARATION_PLAN.md`
- `REPOSITORY_BUILDABILITY_CHECKLIST.md`

## 4. Images

Path:

- `docs/images/`

Purpose:

- define image strategy, registry usage, and publication policy.

Main files:

- `STAGE3_IMAGE_STRATEGY_AND_REGISTRY_PLAN.md`
- `IMAGE_TAGGING_AND_PUBLICATION_POLICY.md`

## 5. Deployment

Path:

- `docs/deployment/`

Purpose:

- define how Mode A should be deployed and validated inside Kubernetes.

Main files:

- `STAGE4_MODEA_K8S_DEPLOYMENT_PLAN.md`
- `MODEA_VALIDATION_CHECKLIST.md`

## 6. Publication

Path:

- `docs/publication/`

Purpose:

- define how the project should be prepared for release and archival packaging.

Main files:

- `STAGE5_REPRODUCIBILITY_AND_PUBLICATION_PLAN.md`
- `ZENODO_RELEASE_CHECKLIST.md`

## 7. Project 2

Path:

- `docs/project2/`

Purpose:

- define the Project 2 architecture and the transition path from Mode A to Mode B.

Main files:

- `STAGE6_PROJECT2_ARCHITECTURE_PLAN.md`
- `PROJECT2_TRANSITION_ROADMAP.md`

## Recommended Reading Order

Recommended reading order for a new reader:

1. `docs/MASTER_ROADMAP.md`
2. `docs/DOCUMENT_INDEX.md`
3. `docs/baseline/`
4. `docs/infrastructure/`
5. `docs/repository/`
6. `docs/images/`
7. `docs/deployment/`
8. `docs/publication/`
9. `docs/project2/`

## Recommended Use

Use the documentation in two different ways depending on the task.

### For understanding the whole programme

Read:

- `MASTER_ROADMAP.md`
- `DOCUMENT_INDEX.md`

### For running or implementing a specific stage

Go directly to the relevant stage directory and use its plan plus checklist documents.

## Maintenance Rule

Whenever a major new planning or execution document is added under `docs/`, update:

- `docs/DOCUMENT_INDEX.md`
- `docs/README.md`

This keeps the documentation navigable as the repository grows.

## Final Statement

The documentation under `docs/` is intended to function as the formal written framework for the transition from Project 1 to Project 2.

Use this file as the documentation entry point after the repository root `README.md`.
