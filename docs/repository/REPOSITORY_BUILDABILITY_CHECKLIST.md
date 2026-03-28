# Repository Buildability Checklist

## 1. Purpose

This document defines the practical checklist for making the repository buildable and ready for later containerisation.

Its purpose is to turn Stage 2 from a conceptual cleanup effort into a concrete engineering process.

## 2. Buildability Principle

A repository should be considered buildable only if a technically competent operator can:

- find the relevant component;
- understand how it is built;
- resolve its dependencies;
- execute the build;
- confirm that the intended artifact was produced.

If any of those steps depend mainly on undocumented local knowledge, the repository is not yet sufficiently buildable.

## 3. Authoritative Source Check

Checklist:

- verify which local working tree contains the real corrected code;
- compare that code against the repository state;
- identify missing commits, patches, or configuration changes;
- move baseline-critical corrections into version control.

Acceptance condition:

- the repository, not a local ad hoc copy, becomes the authoritative source of the working implementation.

## 4. Component Discovery Check

Checklist:

- confirm that each major component has a clear source location;
- confirm that each component has a recognisable entrypoint;
- confirm that scripts, configs, and code are not mixed ambiguously;
- confirm that baseline-critical components are easy to locate.

Minimum components to identify clearly:

- `solana-latency-research`
- load generator
- dashboard
- MPC/control logic if separate
- scenario scripts
- configuration assets

Acceptance condition:

- a new operator can find the key components without guessing.

## 5. Dependency Clarity Check

Checklist:

- identify Go dependencies for Go-based components;
- identify Python dependencies for Python-based components;
- identify shell/runtime dependencies for scripts;
- identify any system packages needed for builds;
- record dependency files in the repository where appropriate.

Acceptance condition:

- dependencies are explicit enough to support repeatable builds.

## 6. Build Command Check

Checklist:

- define the build command for each Go component;
- define the run command for each Python component;
- define any virtual environment or interpreter expectations;
- define any script execution prerequisites;
- record all confirmed commands in documentation.

Acceptance condition:

- the build and run commands no longer depend on memory or shell history alone.

## 7. Configuration Check

Checklist:

- identify runtime config files per component;
- identify which configs belong in version control;
- identify which values are environment-specific;
- avoid hardcoded secrets in source files;
- add example config files where needed.

Acceptance condition:

- configuration is explicit and ready for later mapping to ConfigMaps, Secrets, or image runtime arguments.

## 8. Directory Structure Check

Checklist:

- confirm that source files are grouped logically;
- confirm that scripts are separated from generated binaries;
- confirm that docs are separated from code;
- confirm that config locations are predictable;
- reduce unnecessary structural ambiguity.

Acceptance condition:

- repository layout reflects system structure well enough for later Docker build contexts.

## 9. Artifact Verification Check

Checklist:

- build the Go binaries from the repository state;
- verify that produced binaries correspond to intended components;
- run the Python entrypoint in the documented way;
- verify that scripts can be found and executed from documented locations.

Acceptance condition:

- repository artifacts can be built or run using documented procedures.

## 10. Containerisation Readiness Check

Checklist:

- verify that each future image target has a clear source root;
- verify that each future image target has a clear entrypoint;
- verify that each target’s runtime inputs are understood;
- verify that build contexts can be defined cleanly;
- verify that no critical component depends on undocumented filesystem assumptions.

Acceptance condition:

- the repository can support Dockerfile creation without major structural uncertainty.

## 11. Documentation Check

Checklist:

- update top-level README if required;
- add component README files if required;
- commit Stage 2 documentation;
- document confirmed build commands;
- document known limitations and local-only gaps if any still remain.

Acceptance condition:

- repository documentation reflects actual engineering reality.

## 12. Failure Conditions

Stage 2 should be considered incomplete if any of the following remain true:

- working code still exists only outside the repository;
- component boundaries are unclear;
- build commands are undocumented;
- dependencies are hidden;
- configuration remains partly implicit;
- later Dockerfile creation would still require major detective work.

## 13. Minimum Acceptance Checklist

The repository should be accepted as Stage 2-complete only if all of the following are true:

- real working code is committed;
- major components are structurally clear;
- dependencies are explicit;
- build commands are documented;
- runtime configuration is identifiable;
- the repository is ready for Dockerfile work.

## 14. Recommended Repository Artifacts

The following documentation should exist after Stage 2:

- `docs/repository/STAGE2_REPOSITORY_PREPARATION_PLAN.md`
- `docs/repository/REPOSITORY_BUILDABILITY_CHECKLIST.md`

Optional but strongly recommended:

- top-level `README.md` improvements;
- per-component README files;
- dependency summaries.

## 15. Final Statement

This checklist should be used to determine whether the repository is ready to become the engineering foundation for image-building and later Kubernetes deployment.

Once this checklist is satisfied, the project may proceed to container image strategy and implementation.
