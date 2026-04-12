# HP3C 2026 Paper Artifact

This directory contains the paper-oriented artifact subset for the HP3C 2026 submission.

## Purpose

The goal of this subset is to provide a clean, article-facing view of the repository that supports the conference paper on bottleneck onset and saturation modeling in a private Solana blockchain testbed.

This subset is intentionally narrower than the full repository. It includes only the materials relevant to the paper's claims, figures, experimental setup, and reproducibility path.

## Paper Scope

Working paper title:

**Modeling Bottleneck Onset in a Private Solana Blockchain Testbed**

Working claim:

> A queueing-inspired gray-box model, identified from end-to-end measurements, can detect effective bottleneck onset and explain saturation behavior under synthetic load in a private Solana testbed.

## Contents

- `ARTIFACT_SCOPE.md` — what is included in the paper and what is excluded
- `EXPERIMENT_SETUP.md` — experimental setup used for the paper
- `EXPERIMENTAL_VALIDITY.md` — threats to validity and confounding factors
- `../..//docs/MODEL_VARIABLES.md` — mapping from observed metrics to modeling variables
- `data/` — selected raw and processed datasets used in the paper
- `results/` — selected result tables used in the paper
- `figures/` — final figures used in the paper

## Directory Status

The following directories have been created for the paper-facing workflow:

- `data/`
- `results/`
- `figures/`

They will be populated only with the canonical materials selected for the HP3C 2026 submission.

## Important Note

This directory does not attempt to represent the entire repository history or all exploratory analyses. It only captures the frozen subset relevant to the HP3C 2026 paper.

## Intended Use

This artifact subset is intended for:

- paper review support
- reproducibility support
- figure and table traceability
- model-to-data traceability

## Status

This subset is under active preparation and will be frozen before archival release.

