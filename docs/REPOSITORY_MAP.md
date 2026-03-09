# Repository Map

## Purpose

This document explains the purpose of each major directory in the repository.

## Top-Level Layout

### `analysis/`
Processing, quality-control, modelling, and plotting scripts for turning raw experiment outputs into structured results and figures.

### `dashboard/`
Baseline dashboard-related materials for local observability. This area is being systematised as part of Project 1.

### `data/`
Raw and processed data assets, together with data documentation and schema notes.

### `env/`
Environment notes and version files describing host-side and VM-side software context.

### `experiments/`
Campaign-level experiment structure, metadata, and experiment outputs grouped by run or campaign.

### `exporter/`
VM-side or measurement-side baseline materials related to data export and experimental support tooling.

### `.git/`
Git metadata. Not relevant to the public technical baseline itself.

### `loadgen/`
Host-side load generation baseline materials, including Go-related structure and execution notes.

### `paper/`
Paper-oriented figures and preprint assets used to support technical write-up.

### `results/`
Derived results, figure outputs, summaries, and fitted artefacts generated from baseline experiments.

### `scripts/`
Operational shell and Python scripts used to execute and collect baseline experiment runs.

### `automation/ansible/`
Deployment automation for the single-node private Solana baseline environment.

### `release/`
Release notes and publication packaging for GitHub and Zenodo releases.

## Reading Order for New Reviewers

Recommended reading order:

1. `README.md`
2. `PROJECT_STATUS.md`
3. `ROADMAP.md`
4. `docs/BASELINE_WORKFLOW.md`
5. `docs/VM_HOST_SETUP.md`
6. `docs/ANSIBLE_PLAN.md`
7. component-level README files

