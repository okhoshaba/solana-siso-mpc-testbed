# Repository Status

## Formal Status

This repository is archived / sunset.

It is no longer under active development and is no longer the primary location for ongoing project work.

## Why Development Was Stopped Here

Development in this repository was stopped because the original codebase had accumulated several distinct responsibilities within one monolithic repository, including:

- synthetic benchmarking and load generation;
- MPC and controller-related implementation work;
- latency research for private Solana network experiments;
- infrastructure and private testbed bring-up.

These areas now have different maintenance, release, and documentation needs. Splitting them into focused successor repositories provides clearer ownership, more explicit repository boundaries, and more maintainable development workflows.

## What This Repository Still Remains Useful For

This repository is preserved for:

- historical context on earlier phases of the project;
- reproducibility of previously documented experiments and baseline artefacts;
- citation of prior repository and release states;
- inspection of the original integrated repository structure and workflow assumptions.

## Changes No Longer Expected Here

The following kinds of changes are no longer expected in this repository:

- new features;
- new subsystem development;
- major refactors;
- expansion of operational infrastructure;
- ongoing dashboard, controller, or load-generation feature work;
- continued development of private-network bring-up logic as the main line of progress.

Only limited documentation, archival, citation, or reproducibility-related maintenance should occur here if strictly necessary.

## Successor Repositories

Active development is being continued in the following successor repositories.

### `solana-siso-loadgen-go`

Scope:

- synthetic benchmark in Go;
- CLI;
- load scenarios;
- release binaries;
- run documentation.

### `solana-siso-mpc-controller`

Scope:

- MPC-related codebase;
- `core/`;
- `dashboard/`;
- `batch/`;
- `configs/`;
- `scripts/`;
- `docs/`;
- `tests/`.

### `solana-latency-research-private`

Scope:

- adapted latency research framework for private Solana network experiments.

### `solana-siso-testbed`

Scope:

- infrastructure for the research testbed;
- Dockerfiles;
- compose files;
- provisioning scripts;
- network configs;
- image build pipeline;
- startup checks;
- healthchecks;
- private Solana environment bring-up.

## Maintenance Posture

This repository should be treated as a preserved historical and reproducibility artefact rather than as a destination for future feature delivery.
