# Stage 3 Image Strategy and Registry Plan

## 1. Purpose

This document defines the Stage 3 plan for container images, registry usage, and image lifecycle management.

Stage 3 begins after:

- the baseline has been documented;
- the Stage 1 Kubernetes infrastructure has been defined;
- the repository has been prepared for reproducible builds in Stage 2.

Its purpose is to turn the repository and infrastructure preparation into a disciplined image strategy suitable for later deployment of Mode A workloads and, eventually, Project 2 workloads.

## 2. Stage 3 Goal

The goal of Stage 3 is to establish a controlled and reproducible image workflow that supports:

- upstream image usage where appropriate;
- creation of custom images for project-specific components;
- publication of images to the selected registry path;
- later Kubernetes deployment without ambiguity about image provenance.

At the end of Stage 3, the project should have:

- a documented image taxonomy;
- a documented registry strategy;
- documented tagging and versioning rules;
- buildable image targets for the main custom components;
- a repeatable publication workflow.

## 3. Scope of Stage 3

Stage 3 covers:

- classification of images into categories;
- registry strategy definition;
- naming and tagging rules;
- build and publication discipline;
- digest-based reproducibility;
- preparation of project-specific images.

Stage 3 does **not** yet require:

- full workload deployment in Kubernetes;
- final performance validation of containerised Mode A;
- final publication packaging for Zenodo;
- final Project 2 runtime scaling implementation.

## 4. Why Stage 3 Matters

The project will rely on a mixture of:

- standard upstream images;
- derived images based on standard images;
- fully custom images built from repository code.

Without a clear image strategy, later stages risk:

- version drift;
- unclear provenance;
- failed deployment reproducibility;
- confusion between public and internal artifacts;
- unstable Kubernetes manifests.

Stage 3 exists to prevent those problems.

## 5. Image Strategy Principle

The central principle of Stage 3 is:

> use the most trustworthy and simplest image source that still preserves reproducibility and operational control.

In practice, this means:

- use upstream images where provenance is clear and the image is suitable;
- derive images where small project-specific additions are needed;
- build custom images where project-specific code is the true runtime source.

## 6. Image Categories

Stage 3 defines three primary image classes.

## 6.1 Upstream standard images

These are images obtained from a trusted upstream source and used without rebuilding.

Typical examples:

- Prometheus;
- registry image;
- selected utility images used for support functions.

Use conditions:

- provenance is clear;
- image origin is trustworthy;
- version is explicitly pinned;
- image is compatible with the intended runtime environment.

## 6.2 Derived images

These are images based on a trusted upstream image, with controlled project-specific additions.

Typical examples:

- upstream base plus config files;
- upstream base plus entrypoint wrapper;
- upstream base plus helper scripts.

Use conditions:

- the derived layer is small and intentional;
- the relationship to the upstream base is documented;
- the resulting image is versioned under the project namespace.

## 6.3 Custom images

These are images built from project-owned code and controlled by the repository.

Typical examples:

- load generator;
- dashboard;
- MPC/controller component;
- scenario-runner;
- helper tools image.

Use conditions:

- the repository contains the authoritative source;
- the build process is documented;
- the image is versioned and published in a controlled way.

## 7. Expected Image Targets

The following targets should be considered the likely Stage 3 image candidates.

### 7.1 Support-service images

These may include:

- internal registry service;
- Prometheus;
- lightweight administration or helper images.

### 7.2 Project-specific runtime images

These are the highest-priority custom targets:

- `loadgen`
- `dashboard`
- `controller`
- `scenario-runner`

### 7.3 Tools images

These may later include:

- Solana CLI tools image;
- utility image for payer or funding jobs;
- debugging or maintenance tool images.

## 8. Registry Strategy

The registry strategy should support both discipline and flexibility.

## 8.1 Internal registry role

The internal registry should provide:

- controlled image storage;
- fast local access from the cluster;
- reduced dependence on external availability;
- a predictable path for later deployments.

## 8.2 Public registry role

A public registry may be used for:

- publication of project-specific images intended for broader reuse;
- distribution of reproducible images associated with the research output;
- public availability where appropriate.

## 8.3 Recommended dual-path model

A practical model is:

- **internal registry** for operational use in the datacentre cluster;
- **public registry namespace** for externally shareable project images.

This supports both operational reproducibility and broader dissemination.

## 9. Naming Convention

Image names should be explicit and role-oriented.

Recommended pattern:

- `<registry>/<namespace>/<component>:<tag>`

Examples:

- `registry.local/research/loadgen:<tag>`
- `registry.local/research/dashboard:<tag>`
- `registry.local/research/controller:<tag>`
- `registry.local/research/scenario-runner:<tag>`

If a public namespace is later used, the same component naming should be preserved there.

Naming goals:

- make role clear;
- keep image purpose obvious;
- make later manifest maintenance simpler.

## 10. Versioning and Tagging Principle

Tags must support reproducibility.

Recommended practice:

- avoid `latest` as an operational deployment default;
- use meaningful, explicit tags;
- record digests for deployment-grade use;
- tie tags to repository state or release logic.

Useful tag styles may include:

- semantic versions;
- date-based tags;
- commit-derived tags;
- release candidate tags.

The exact scheme may be chosen later, but it must be consistent.

## 11. Digest Pinning Principle

For deployment and scientific reproducibility, digests should be treated as the strongest image identity.

This means:

- tags are useful for human workflow;
- digests are preferred for manifest-level reproducibility;
- published release notes should record both where practical.

## 12. Build Discipline

Every custom image should have:

- a defined build context;
- a defined Dockerfile or equivalent build file;
- a defined entrypoint;
- a defined runtime configuration model;
- a defined publication target.

Builds should be traceable to repository state.

This means that for each custom image it should be possible to answer:

- which source code was used;
- which Dockerfile was used;
- which tag was produced;
- which digest was published.

## 13. Publication Discipline

Image publication should follow a controlled process.

Recommended high-level workflow:

1. confirm repository state is correct;
2. build the image;
3. test the image locally or in a controlled path;
4. tag the image according to policy;
5. push to the intended registry;
6. record the resulting image reference and digest.

The publication workflow should be predictable enough that the same image lineage can be reconstructed later.

## 14. Security and Secret Handling Principle

Images must not embed secrets.

This means:

- no private keys baked into images;
- no registry secrets committed to source control;
- no environment-specific secrets hardcoded in Dockerfiles;
- runtime secret handling should later be delegated to environment configuration and Kubernetes mechanisms.

## 15. Stage 3 Deliverables

Stage 3 should produce:

- image strategy and registry plan;
- image tagging and publication policy;
- initial image target list;
- initial custom image builds for the main project components;
- recorded registry paths and digests.

## 16. Stage 3 Acceptance Criteria

Stage 3 should be considered complete only if all of the following are true:

1. the image classes are defined clearly;
2. the registry path strategy is defined;
3. naming and tagging rules are documented;
4. at least the main custom image targets are prepared for build;
5. the project can build and publish images in a repeatable way;
6. image provenance is clear enough for later deployment and scientific reuse.

## 17. Risks at Stage 3

The main risks are:

- using unverified or stale upstream images without scrutiny;
- allowing tags to drift without digest tracking;
- mixing experimental and deployment-grade images without distinction;
- embedding environment-specific assumptions into images;
- producing images whose source provenance cannot later be reconstructed.

## 18. Risk Mitigation Strategy

Recommended mitigation actions:

- pin upstream versions explicitly;
- record digests for every deployment-grade image;
- separate public, internal, and experimental image paths;
- document every custom image target;
- treat image publication as part of the research reproducibility chain.

## 19. Relation to Later Stages

Stage 3 enables:

- Stage 4 Kubernetes deployment of Mode A components;
- Stage 5 reproducibility packaging and external publication;
- Stage 6 architectural scaling toward Project 2.

Without a strong Stage 3, later deployment work becomes fragile and difficult to reproduce.

## 20. Stage 3 Completion Statement

Stage 3 is complete when the project has a controlled, documented, and repeatable image workflow that can supply the Kubernetes platform with trustworthy and reproducible images for later stages.
