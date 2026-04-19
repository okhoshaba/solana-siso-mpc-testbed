# Solana SISO MPC Testbed

> [!IMPORTANT]
> This repository is archived / sunset and is no longer under active development.
> Ongoing work has been split into four focused successor repositories:
> `solana-siso-loadgen-go`, `solana-siso-mpc-controller`, `solana-latency-research-private`, and `solana-siso-testbed`.
> No new features should be added here.

A systematised and reproducible baseline package for controlled benchmarking in a private Solana environment.

## Overview

This repository contains the baseline research and engineering assets for a private Solana benchmarking environment oriented towards controlled load experiments, observability, and adaptive transaction-load control studies.

It is preserved as a historical repository for earlier stages of the project and for reproducibility, citation, and technical reference. Active development has moved to successor repositories with narrower and more explicit scope boundaries.

The project is not starting from zero. It already includes:
- analysis scripts;
- raw and derived data assets;
- experimental scripts;
- figures and result artefacts;
- reproducibility metadata;
- release metadata for archival publication;
- early paper-related materials.

At the same time, several operational components are still being systematised and prepared for full public release. In particular, parts of the host-side load generation logic, dashboard-related code, and VM-side deployment workflow are being consolidated and documented as part of the baseline release effort.

## Archival Status

This repository is no longer the main development location for the project.

Development was stopped here because the original monolithic repository had grown to cover several distinct concerns:
- synthetic load generation;
- MPC and controller-oriented logic;
- latency research for private Solana environments;
- infrastructure and bring-up for the private testbed.

These concerns are now being maintained in separate repositories so that each codebase can evolve with clearer ownership, structure, and release boundaries.

This repository remains valuable for:
- historical context on earlier project stages;
- reproducibility of prior experiments and benchmark artefacts;
- citation of earlier repository and release states;
- inspection of the original integrated baseline layout.

## Successor Repository Mapping

The previous monolithic scope is being superseded as follows:

- `loadgen/` and host-side synthetic benchmarking concerns move to `solana-siso-loadgen-go`
- MPC-related logic, controller structure, dashboard work, batch workflows, configs, scripts, docs, and tests move to `solana-siso-mpc-controller`
- latency research adapted for private Solana experiments moves to `solana-latency-research-private`
- infrastructure, Dockerfiles, compose files, provisioning, network configuration, image build pipeline, startup checks, healthchecks, and private Solana environment bring-up move to `solana-siso-testbed`

This repository should not receive new feature development. Only limited archival, citation, or reproducibility-oriented maintenance should be expected if strictly necessary.

## Historical Project 1 Scope

The current baseline release effort is focused on:

1. repository systematisation;
2. documentation of the existing workflow;
3. consolidation of baseline host-side and VM-side components;
4. Ansible-based automation for single-node baseline deployment;
5. GitHub publication and Zenodo archival release.

This phase is intentionally limited in scope. It does **not** aim to deliver:
- the full multi-node private cluster framework;
- a mature production-grade dashboard;
- the full MIMO adaptive-control phase.

Those items belong to a later follow-on phase.

## Repository Status

This repository contains the analytical and data side of the baseline work together with earlier integrated implementation materials. It is now retained as an archival baseline artefact rather than an active development repository.

See also:
- [`docs/REPOSITORY_STATUS.md`](docs/REPOSITORY_STATUS.md)

See:
- [`PROJECT_STATUS.md`](PROJECT_STATUS.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)
- [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md)
- [`docs/BASELINE_WORKFLOW.md`](docs/BASELINE_WORKFLOW.md)

## Repository Structure

- `analysis/` — data processing, quality control, operating-point selection, plotting, and summary scripts
- `data/` — raw and processed datasets, plus data documentation
- `results/` — derived result artefacts, segment tables, summary outputs, and figures
- `experiments/` — campaign-level experiment metadata and exported tables
- `scripts/` — operational experiment scripts and collection utilities
- `dashboard/` — dashboard-related baseline materials
- `loadgen/` — host-side load generation baseline materials
- `exporter/` — VM-side exporter and related baseline components
- `automation/ansible/` — deployment automation for the single-node baseline
- `paper/` — paper-related figures and preprint materials
- `release/` — release notes and publication packaging materials

## Baseline Workflow

At a high level, the baseline workflow is:

1. prepare the host and VM environment;
2. bring up the single-node private Solana baseline;
3. run baseline benchmark scenarios;
4. collect and organise raw outputs;
5. process results and generate figures;
6. package artefacts for GitHub and Zenodo release.

See [`docs/BASELINE_WORKFLOW.md`](docs/BASELINE_WORKFLOW.md) for details.

## Reproducibility

This repository is being prepared as a reproducible baseline release. Reproducibility currently covers:
- project metadata;
- data packaging;
- figures;
- experiment naming conventions;
- release artefacts.

The next step is to reduce manual infrastructure bring-up through Ansible-based automation for the single-node baseline environment.

See:
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)
- [`docs/VM_HOST_SETUP.md`](docs/VM_HOST_SETUP.md)
- [`docs/ANSIBLE_PLAN.md`](docs/ANSIBLE_PLAN.md)

## Public Release Plan

The project uses two publication channels:

- **GitHub** for repository hosting, documentation, code history, and release notes associated with earlier project stages;
- **Zenodo** for archival releases of reproducibility artefacts, datasets, figures, and release metadata suitable for citation.

## HP3C 2026 Paper Artifact

This repository also contains a paper-specific artifact subset for the HP3C 2026 submission.

See:

- `paper/hp3c2026/README.md` — paper-facing artifact overview
- `paper/hp3c2026/ARTIFACT_SCOPE.md` — scope of materials included in the paper
- `paper/hp3c2026/EXPERIMENT_SETUP.md` — experiment setup used for the paper
- `paper/hp3c2026/EXPERIMENTAL_VALIDITY.md` — threats to validity and confounding factors
- `docs/MODEL_VARIABLES.md` — mapping from repository metrics to paper model variables

## Citation

If you use this repository or its release artefacts, please consult [`CITATION.cff`](CITATION.cff) and the Zenodo release metadata. The archival status of the repository does not change its citation value for earlier project stages or released artefacts.

## Licence

This repository is distributed under the terms of the licence included in [`LICENSE`](LICENSE).

## Potential acknowledgement

If this baseline release receives grant support, the following acknowledgement text may be added to the repository and release materials:

> This work was supported by the Solana Foundation Ukraine Grants programme administered by Superteam Ukraine.
