# Stage 5 Reproducibility and Publication Plan

## 1. Purpose

This document defines the Stage 5 plan for reproducibility packaging, repository finalisation, release preparation, and research publication support.

Stage 5 begins after:

- the Project 1 baseline has been documented;
- Stage 1 infrastructure has been defined and prepared;
- Stage 2 repository buildability has been established;
- Stage 3 image strategy has been defined;
- Stage 4 Mode A migration and validation have been planned or executed.

Its purpose is to convert the accumulated engineering and research outputs into a publication-ready, reproducible, and externally understandable package.

## 2. Stage 5 Goal

The goal of Stage 5 is to make the project suitable for:

- internal technical review;
- external scientific review;
- archival publication;
- later reuse by other researchers;
- future continuation into Project 2.

At the end of Stage 5, the project should have:

- a coherent and finalised repository structure;
- a documented release state;
- a reproducibility-oriented artifact set;
- a publication-ready package for archival deposit, including Zenodo if desired.

## 3. Scope of Stage 5

Stage 5 covers:

- final repository documentation improvements;
- release-oriented cleanup and alignment;
- preparation of figures, scripts, configs, and metadata;
- definition of what belongs in the public reproducibility package;
- preparation for GitHub release creation;
- preparation for Zenodo deposition.

Stage 5 does **not** yet require:

- implementation of Project 2 multi-node architecture;
- scaling studies for validator sets or RPC layers;
- MIMO runtime expansion;
- final Project 2 infrastructure design execution.

## 4. Why Stage 5 Matters

Without Stage 5, the project may remain technically useful to the original operator but still be weak in terms of:

- scientific reproducibility;
- external readability;
- archival quality;
- citation readiness;
- research continuity.

Stage 5 exists to prevent that outcome.

## 5. Stage 5 Principle

The main principle of Stage 5 is:

> package the project as evidence, not merely as code.

This means the repository and release materials must show not only what was built, but also:

- what was studied;
- how it was run;
- which results belong to which configuration;
- which artifacts support the scientific claims.

## 6. Stage 5 Desired End State

The project should reach the following condition.

### 6.1 Repository clarity

A third party should be able to understand:

- what the project is;
- what the baseline environment was;
- how the transition work was staged;
- what code, scripts, and configurations were used;
- what outputs correspond to what experiments.

### 6.2 Reproducibility packaging

A technically competent reader should be able to identify:

- source code;
- configuration files;
- build instructions;
- deployment instructions;
- experiment scripts;
- figure-generation or result-generation artifacts.

### 6.3 Publication readiness

The project should be suitable for:

- release tagging;
- GitHub release notes;
- archival packaging;
- DOI-linked deposit through Zenodo if desired.

## 7. Core Stage 5 Work Items

## 7.1 Final repository review

Tasks:

- verify repository structure is coherent;
- remove obsolete or misleading files if appropriate;
- ensure key docs are visible and up to date;
- ensure the repository reflects the real engineering state.

## 7.2 Reproducibility artifact selection

Tasks:

- identify which source trees belong in the release;
- identify which configs belong in the release;
- identify which scripts belong in the release;
- identify which figures and results belong in the release;
- identify which artifacts are essential and which are optional.

## 7.3 Documentation alignment

Tasks:

- align top-level README with the real repository structure;
- ensure stage documents are easy to navigate;
- ensure baseline, infrastructure, image, and deployment docs are mutually consistent;
- ensure operator-facing and publication-facing documentation do not contradict each other.

## 7.4 Release preparation

Tasks:

- define the release boundary;
- define the release tag;
- prepare release notes;
- record important image references if applicable;
- verify the release corresponds to a known repository state.

## 7.5 Zenodo packaging preparation

Tasks:

- determine the exact archive contents;
- prepare descriptive metadata;
- prepare title, authorship, and description;
- prepare citation-oriented fields;
- ensure the archive is understandable independently of local operator context.

## 8. Recommended Artifact Classes for Stage 5

The Stage 5 package should usually draw from the following classes of material.

### 8.1 Source artifacts

Examples:

- Go source code;
- Python source code;
- shell scripts;
- supporting utilities.

### 8.2 Configuration artifacts

Examples:

- baseline configs;
- local example configs;
- deployment-related configs;
- Prometheus or observability configs where appropriate;
- non-secret runtime examples.

### 8.3 Documentation artifacts

Examples:

- baseline documents;
- stage plans;
- runbooks;
- validation checklists;
- README files.

### 8.4 Result artifacts

Examples:

- experiment outputs;
- derived result files;
- figures used in reporting;
- summary tables where appropriate.

### 8.5 Metadata artifacts

Examples:

- release notes;
- citation metadata;
- provenance notes;
- version notes;
- archive manifest.

## 9. Exclusion Principle

Stage 5 should also decide what **not** to publish.

Examples of items that should not be included directly in public archival packages:

- secrets;
- private keys;
- machine-specific credentials;
- accidental local junk files;
- transient build artifacts with no reproducibility value;
- operator-specific environment residues.

## 10. Repository Documentation Expectations

By the end of Stage 5, the repository should ideally contain:

- a clear top-level README;
- documentation of the baseline;
- documentation of Stage 1 through Stage 4 planning or execution;
- clear entry points into code and experiment assets;
- clear notes on reproducibility limitations where they still exist.

## 11. Release Boundary Principle

A release should correspond to a coherent state of the project, not to an arbitrary snapshot.

This means a Stage 5 release should ideally include:

- a known repository commit or tag;
- coherent documentation;
- consistent code/config/results relationships;
- a stable explanation of what the release represents.

## 12. Zenodo Preparation Principle

A Zenodo archive should be understandable as a self-contained research record.

This means the archival package should make sense to someone who sees:

- the title;
- the authorship;
- the description;
- the files;
- the repository release linkage.

It should not depend heavily on hidden operator context.

## 13. Stage 5 Deliverables

Stage 5 should produce:

- a Stage 5 reproducibility and publication plan;
- a Zenodo or release checklist;
- a final repository review outcome;
- release notes or release draft text;
- a publication-ready artifact inventory.

## 14. Stage 5 Acceptance Criteria

Stage 5 should be considered complete only if all of the following are true:

1. the repository is coherent enough for external readers;
2. release-relevant artifacts have been selected deliberately;
3. documentation is aligned with the actual project state;
4. a clear release boundary exists;
5. the project can be archived in a reproducibility-oriented form;
6. obvious publication blockers have been removed.

## 15. Risks at Stage 5

The main risks are:

- publishing an inconsistent repository state;
- omitting critical reproducibility artifacts;
- including sensitive or machine-specific material accidentally;
- leaving the archive too dependent on undocumented context;
- confusing engineering notes with publication-facing narrative.

## 16. Risk Mitigation Strategy

Recommended mitigation actions:

- perform a release-oriented review before publication;
- maintain an explicit inclusion/exclusion list;
- verify that sensitive material is excluded;
- tie release artifacts to a known commit/tag;
- ensure that public-facing documentation explains the project clearly enough for non-local readers.

## 17. Relation to Later Stages

Stage 5 strengthens the scientific value of all prior work and directly supports:

- defensible publication;
- later reuse of the project;
- structured handover into Project 2 planning and implementation.

Without Stage 5, the project risks being technically rich but archival-weak.

## 18. Recommended Repository Outputs

After Stage 5 planning, the repository should contain at least:

- `docs/publication/STAGE5_REPRODUCIBILITY_AND_PUBLICATION_PLAN.md`
- `docs/publication/ZENODO_RELEASE_CHECKLIST.md`

Optional but useful later:

- `docs/publication/ARTIFACT_INVENTORY.md`
- `docs/publication/RELEASE_NOTES_DRAFT.md`
- `CITATION.cff`

## 19. Stage 5 Completion Statement

Stage 5 is complete when the project has been transformed from an internal engineering/research workspace into a coherent, reviewable, reproducibility-oriented release candidate suitable for GitHub release publication and archival deposit.
