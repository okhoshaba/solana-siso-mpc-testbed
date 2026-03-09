# Baseline Workflow

## Purpose

This document summarises the baseline workflow for the private single-node Solana benchmarking environment.

## Workflow Stages

### Stage 1 — Environment Preparation
Prepare the host and VM environment, verify versions, and confirm that baseline dependencies are available.

Relevant files:
- `env/fedora_versions.txt`
- `env/vm_versions.txt`
- `env/requirements.txt`

### Stage 2 — Baseline Bring-Up
Bring up the single-node private Solana environment on the VM and prepare the host-side connection workflow.

Current state:
- partially manual;
- planned to be reduced through Ansible automation under Project 1.

### Stage 3 — Benchmark Execution
Execute baseline scenarios using the host-side operational scripts and load-generation logic.

Relevant materials:
- `scripts/`
- `loadgen/`
- `exporter/`

### Stage 4 — Data Collection
Collect baseline outputs and organise them into raw and derived data structures.

Relevant materials:
- `data/raw/`
- `data/processed/`
- `experiments/`
- `results/`

### Stage 5 — Analysis and Plotting
Run processing, quality-control, and plotting scripts to obtain structured baseline results.

Relevant materials:
- `analysis/`
- `results/figures/`
- `paper/figures/`

### Stage 6 — Packaging and Release
Prepare a coherent public baseline release for:
- GitHub publication;
- Zenodo archival release.

## Project 1 Improvement Target

Project 1 improves this workflow by:
- documenting it in a consistent form;
- reducing manual infrastructure steps;
- improving release readiness;
- packaging baseline artefacts for public review and citation.

