# Project Status

## Summary

This project already exists in working baseline form. It is not being initiated from scratch.

The current repository contains:
- analysis scripts;
- experimental scripts;
- raw and derived data assets;
- figures and result artefacts;
- paper-related materials;
- reproducibility and release metadata.

At the same time, several operational components are still being systematised and are not yet fully represented in the public repository in a polished release-ready form.

## Already Present in the Repository

### Analysis and processing
- `analysis/build_processed_stdlib.py`
- `analysis/make_plots.py`
- `analysis/pick_operating_points.py`
- `analysis/qc_raw_stdlib.py`
- `analysis/summarise_run.py` or equivalent summary logic

### Data and metadata
- raw data under `data/raw/`
- data documentation in `data/README.md` and `data/SCHEMA.md`
- release metadata via `.zenodo.json`, checksums, and archive files

### Results and figures
- charts and experiment figures under `results/figures/`
- paper figures under `paper/figures/`
- segment and summary-related result files under `results/`

### Experiment scripts
- scenario scripts in `scripts/`
- campaign structure under `experiments/`

## Exists in Working Form but Still Needs Systematisation

The following baseline components exist conceptually or operationally, but still require structured public packaging, documentation, or clean-up:

- host-side load generation code;
- dashboard-related baseline code;
- VM-side operational workflow for environment bring-up;
- deployment logic currently executed manually;
- cleaner release notes and component-level status documentation.

## Planned Under Project 1

Project 1 focuses on:

1. repository systematisation;
2. component status documentation;
3. baseline release packaging;
4. Ansible-based automation for the single-node environment;
5. GitHub and Zenodo release preparation.

## Explicitly Out of Scope for Project 1

The following items are not part of the current microgrant scope:

- full multi-node private cluster support;
- a complete mature dashboard product;
- the full adaptive MIMO research phase;
- later-stage scale-up of the experimental framework.

## Intended Outcome

By the end of Project 1, the repository should function as a coherent and reviewable public baseline package rather than only as a private working research tree.

