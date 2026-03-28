# Zenodo Release Checklist

## 1. Purpose

This document defines the practical checklist for preparing a project release for archival publication, including Zenodo-oriented packaging.

Its purpose is to ensure that the release is:

- coherent;
- reproducible;
- appropriately documented;
- free from obvious sensitive material leaks;
- suitable for long-term reference.

## 2. Scope

This checklist applies to the public or archival release package associated with the project.

It covers:

- repository release readiness;
- artifact selection;
- documentation alignment;
- metadata preparation;
- final archival review.

It does not replace internal operational runbooks or image publication policies, but it should be consistent with them.

## 3. Release Candidate Identification

Checklist:

- identify the intended repository tag or release boundary;
- verify that the selected commit represents a coherent project state;
- confirm that documentation corresponds to that exact state;
- confirm that the selected release is the one intended for external reference.

Acceptance condition:

- the release candidate is explicit and stable.

## 4. Documentation Readiness

Checklist:

- verify top-level README clarity;
- verify baseline documentation is present;
- verify stage documentation is present as needed;
- verify build or run instructions are present where appropriate;
- verify known limitations are documented honestly.

Acceptance condition:

- an external reader can understand what the project is and how the materials relate to each other.

## 5. Artifact Selection Readiness

Checklist:

- confirm which source directories are included;
- confirm which config files are included;
- confirm which scripts are included;
- confirm which results or figures are included;
- confirm which generated artifacts are intentionally excluded.

Acceptance condition:

- the archive contents are deliberate rather than accidental.

## 6. Sensitive Material Review

Checklist:

- verify that no secrets are committed;
- verify that no private keys are included;
- verify that no credentials are included;
- verify that no host-specific confidential material is included;
- verify that temporary local artifacts are excluded.

Acceptance condition:

- the archival package is safe for publication.

## 7. Reproducibility Review

Checklist:

- verify that essential experiment scripts are present;
- verify that important configs are present or represented by safe examples;
- verify that code and documentation point to the same workflow;
- verify that figures or result files are attributable to a documented process;
- verify that obvious reproducibility gaps are documented if they cannot yet be fully closed.

Acceptance condition:

- the release is meaningfully reproducible or honestly delimited.

## 8. Metadata Preparation

Checklist:

- prepare release title;
- prepare project description;
- prepare authorship information;
- prepare keywords where useful;
- prepare citation-oriented information;
- prepare date and version information.

Acceptance condition:

- the release can be understood and cited as an archival object.

## 9. GitHub Release Preparation

Checklist:

- prepare release notes;
- confirm the selected git tag;
- confirm repository state is pushed and visible;
- verify that release attachments, if any, are correct;
- ensure that the release narrative matches the actual archive contents.

Acceptance condition:

- the GitHub release can serve as the public anchor for the archival package.

## 10. Zenodo-Specific Preparation

Checklist:

- verify repository-release linkage if using GitHub-Zenodo integration;
- prepare a release description suitable for archival users;
- verify file naming clarity;
- verify that the archive contents are understandable without local machine assumptions;
- verify that the archive corresponds to the intended public record.

Acceptance condition:

- the release is suitable for DOI-linked archival deposition.

## 11. Optional but Recommended Additions

Recommended additions where appropriate:

- `CITATION.cff`
- release notes draft
- artifact inventory
- high-level architecture figure
- reproducibility notes
- manifest of included datasets, figures, and scripts

These are not always mandatory, but they strengthen the archival quality of the release.

## 12. Failure Conditions

The release should be considered not ready if any of the following remain true:

- repository documentation is inconsistent;
- critical artifacts are missing;
- sensitive material may still be present;
- the release boundary is unclear;
- the release cannot be explained coherently to an external reader;
- archive contents are accidental rather than curated.

## 13. Minimum Acceptance Checklist

The release should not be treated as publication-ready unless all of the following are true:

- release candidate is explicitly identified;
- repository documentation is coherent;
- selected artifacts are deliberate;
- sensitive material review is complete;
- reproducibility review is complete;
- metadata is prepared;
- release notes are prepared or drafted.

## 14. Evidence to Record

At release time, record at minimum:

- release tag;
- release date;
- repository commit;
- included artifact classes;
- any documented limitations;
- publication or archive URL once available.

## 15. Recommended Repository Outputs

At minimum, the repository should contain:

- `docs/publication/STAGE5_REPRODUCIBILITY_AND_PUBLICATION_PLAN.md`
- `docs/publication/ZENODO_RELEASE_CHECKLIST.md`

Later additions may include:

- `docs/publication/ARTIFACT_INVENTORY.md`
- `docs/publication/RELEASE_NOTES_DRAFT.md`
- `CITATION.cff`

## 16. Final Statement

This checklist exists to ensure that publication is a controlled and research-appropriate act rather than a last-minute file upload.

Once the checklist is satisfied, the project may proceed to release publication and archival deposition with much stronger confidence.
