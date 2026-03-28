# Image Tagging and Publication Policy

## 1. Purpose

This document defines the policy for image naming, tagging, digest recording, and publication.

Its purpose is to ensure that image handling across the project remains:

- reproducible;
- understandable;
- operationally safe;
- suitable for later scientific review.

## 2. Policy Principle

The core policy is:

> every deployment-relevant image must be identifiable by both human-readable tag and immutable content reference.

This means:

- tags are required for operator workflow;
- digests are required for reproducibility and deployment control.

## 3. Registry Separation Policy

Images should be separated by operational intent.

Recommended categories:

- **internal** — images intended for datacentre cluster use;
- **public** — images intended for broader external availability;
- **experimental** — images intended for temporary or exploratory use.

This separation may be implemented:

- by namespace;
- by repository path;
- or by a documented combination of both.

## 4. Component Naming Policy

Component names should be explicit and stable.

Recommended examples:

- `loadgen`
- `dashboard`
- `controller`
- `scenario-runner`
- `solana-tools`

Component names should not be renamed casually once manifests or publications begin to depend on them.

## 5. Tagging Policy

## 5.1 General rule

Do not use `latest` as the normal deployment tag.

`latest` may exist for convenience in local development if desired, but it must not be treated as the authoritative deployment reference.

## 5.2 Recommended tag types

Useful tag families may include:

- semantic release tags, for example `v0.1.0`;
- date-based tags, for example `2026-03-28`;
- commit-derived tags, for example `git-abc1234`;
- release-candidate tags, for example `v0.1.0-rc1`.

One consistent scheme should be selected and used deliberately.

## 5.3 Minimum requirement

Every image intended for shared use should have:

- one clear tag;
- one recorded digest;
- one known source state in the repository.

## 6. Digest Recording Policy

For every deployment-grade image, record:

- image name;
- tag;
- digest;
- source commit or release reference;
- build date;
- intended registry target.

This information may be stored in:

- release notes;
- image matrix documentation;
- deployment notes;
- repository documentation.

## 7. Publication Workflow Policy

The publication workflow should follow this order:

1. confirm repository state;
2. build image;
3. verify image behaviour;
4. assign final tag;
5. push image to registry;
6. capture digest;
7. update documentation or release notes.

Publication should not be treated as complete until the digest has been captured.

## 8. Build Provenance Policy

Every custom image should be traceable back to:

- source directory;
- build file;
- build command;
- repository commit or release state.

If that traceability is missing, the image should not be treated as a deployment-grade artifact.

## 9. Configuration Policy

Images should remain as environment-agnostic as practical.

This means:

- use runtime configuration rather than rebuilds where feasible;
- keep environment-specific values outside the image where sensible;
- use example configuration files rather than hardcoded secrets or host-specific values.

## 10. Secret Handling Policy

The following must not be baked into images:

- private keys;
- production credentials;
- registry passwords;
- environment-specific secrets;
- operator-specific secrets.

Secrets must be injected later by controlled runtime mechanisms.

## 11. Experimental Image Policy

Experimental images are allowed, but must be clearly distinguishable from stable images.

Recommended practice:

- use a distinct namespace or tag suffix;
- avoid reusing stable tags for experimental builds;
- do not deploy experimental images into baseline validation without explicit notation.

## 12. Stable Image Policy

A stable image should satisfy the following conditions:

- built from known repository state;
- tagged consistently;
- digest captured;
- intended use documented;
- suitable for repeat deployment.

Stable images are the ones that should later appear in Kubernetes manifests tied to research runs.

## 13. Documentation Policy

At minimum, the project should maintain a documented image record including:

- component name;
- registry path;
- tag;
- digest;
- source reference;
- notes on purpose and intended usage.

This may later become an image matrix document if needed.

## 14. Failure Conditions

The image policy should be considered violated if any of the following occur:

- a deployment uses an untracked image;
- an image tag is used without knowing its source state;
- a custom image is published without digest capture;
- a stable deployment relies on `latest`;
- secrets are baked into an image;
- public and internal image purposes are mixed without documentation.

## 15. Minimum Acceptance Checklist

The image workflow should be treated as policy-compliant only if:

- image names are structured clearly;
- tags follow a documented rule;
- digests are recorded;
- source provenance is known;
- publication steps are repeatable;
- image purpose is documented.

## 16. Suggested Repository Artifacts

After Stage 3, the repository should ideally contain:

- `docs/images/STAGE3_IMAGE_STRATEGY_AND_REGISTRY_PLAN.md`
- `docs/images/IMAGE_TAGGING_AND_PUBLICATION_POLICY.md`

Optional but recommended later:

- `docs/images/IMAGE_MATRIX.md`
- `docs/images/BUILD_AND_PUSH_RUNBOOK.md`

## 17. Final Statement

This policy exists to ensure that image handling supports both operational deployment and research reproducibility.

Once the policy is applied consistently, the project can proceed to image building and later Kubernetes deployment with substantially lower ambiguity.
