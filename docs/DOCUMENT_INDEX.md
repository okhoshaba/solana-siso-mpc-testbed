# Documentation Index

## 1. Purpose

This document provides an index of the major documentation artifacts created for the transition programme from Project 1 to Project 2.

Its purpose is to make the repository easy to navigate and to show how the stage documents relate to each other.

## 2. Recommended Top-Level Documentation Structure

Recommended structure:

- `docs/baseline/`
- `docs/infrastructure/`
- `docs/repository/`
- `docs/images/`
- `docs/deployment/`
- `docs/publication/`
- `docs/project2/`

Recommended top-level navigation files:

- `docs/REPOSITORY_STATUS.md`
- `docs/MASTER_ROADMAP.md`
- `docs/DOCUMENT_INDEX.md`

### `docs/REPOSITORY_STATUS.md`
Purpose:

- records the formal archival / sunset status of the repository;
- explains the repository split into successor codebases.

## 3. Baseline Documentation

### `docs/baseline/TECHNICAL_BASELINE.md`
Purpose:

- defines the formal technical baseline for Project 1.

### `docs/baseline/RUNBOOK_PROJECT1.md`
Purpose:

- provides the operational procedure for running the baseline environment.

### `docs/baseline/SUCCESS_CRITERIA.md`
Purpose:

- defines the formal success criteria for the baseline.

### `docs/baseline/COMPONENT_INVENTORY.md`
Purpose:

- lists and explains the baseline components and their roles.

## 4. Infrastructure Documentation

### `docs/infrastructure/STAGE1_KUBERNETES_PLAN.md`
Purpose:

- defines the Stage 1 infrastructure plan.

### `docs/infrastructure/VM_ROLE_MATRIX.md`
Purpose:

- defines the VM role and resource allocation model.

### `docs/infrastructure/STAGE1_EXECUTION_CHECKLIST.md`
Purpose:

- provides the operational execution checklist for Stage 1.

### `docs/infrastructure/CLUSTER_ACCEPTANCE_CHECKLIST.md`
Purpose:

- defines the acceptance criteria for the Stage 1 cluster.

## 5. Repository Documentation

### `docs/repository/STAGE2_REPOSITORY_PREPARATION_PLAN.md`
Purpose:

- defines the repository preparation plan for Stage 2.

### `docs/repository/REPOSITORY_BUILDABILITY_CHECKLIST.md`
Purpose:

- provides the practical buildability checklist for the repository.

## 6. Image Documentation

### `docs/images/STAGE3_IMAGE_STRATEGY_AND_REGISTRY_PLAN.md`
Purpose:

- defines the Stage 3 image and registry strategy.

### `docs/images/IMAGE_TAGGING_AND_PUBLICATION_POLICY.md`
Purpose:

- defines the image naming, tagging, digest, and publication policy.

## 7. Deployment Documentation

### `docs/deployment/STAGE4_MODEA_K8S_DEPLOYMENT_PLAN.md`
Purpose:

- defines the plan for reproducing Mode A in Kubernetes.

### `docs/deployment/MODEA_VALIDATION_CHECKLIST.md`
Purpose:

- defines the validation checklist for the Kubernetes-based Mode A.

## 8. Publication Documentation

### `docs/publication/STAGE5_REPRODUCIBILITY_AND_PUBLICATION_PLAN.md`
Purpose:

- defines the Stage 5 publication and reproducibility plan.

### `docs/publication/ZENODO_RELEASE_CHECKLIST.md`
Purpose:

- defines the practical archival and Zenodo-oriented release checklist.

## 9. Project 2 Documentation

### `docs/project2/STAGE6_PROJECT2_ARCHITECTURE_PLAN.md`
Purpose:

- defines the target architecture for Project 2.

### `docs/project2/PROJECT2_TRANSITION_ROADMAP.md`
Purpose:

- defines the roadmap from Mode A to Mode B.

## 10. Navigation Logic

The recommended reading order is:

1. `docs/MASTER_ROADMAP.md`
2. baseline documents
3. infrastructure documents
4. repository documents
5. image documents
6. deployment documents
7. publication documents
8. Project 2 documents

This order follows the actual dependency logic of the programme.

## 11. Use Cases for This Index

This document can be used by:

- the primary researcher;
- collaborators;
- supervisors;
- reviewers;
- future users of the repository.

It is particularly useful when the repository becomes large enough that stage documents are no longer obvious from directory names alone.

## 12. Maintenance Rule

Whenever a new major planning or execution document is added to the repository, this index should be updated so that the documentation remains navigable as a coherent system.

## 13. Final Statement

This index exists to keep the repository understandable as a structured research and engineering programme rather than a loose collection of isolated markdown files.
