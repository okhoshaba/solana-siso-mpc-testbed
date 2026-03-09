# Architecture

## Overview

The baseline testbed is organised around a private single-node Solana environment and a host-side experimental workflow used for load generation, result collection, analysis, and visualisation.

## Main Components

### 1. Host Machine
The host machine is responsible for:
- running experiment orchestration scripts;
- running host-side load generation logic;
- collecting and organising outputs;
- processing data and generating figures;
- supporting dashboard-related baseline functions.

### 2. Virtual Machine
The VM is responsible for:
- hosting the private single-node Solana baseline;
- running VM-side baseline infrastructure components;
- supporting exporter and measurement-side functionality;
- exposing the experimental environment to host-side tools.

### 3. Benchmark Workflow
The benchmark workflow connects:
- baseline bring-up;
- load generation;
- metric collection;
- data storage;
- analysis and plotting.

### 4. Results and Publication Layer
The publication layer includes:
- figures;
- result tables;
- datasets;
- GitHub release materials;
- Zenodo archival release materials.

## Current State

The architecture exists in working baseline form, but some steps remain manual and some components remain only partially systematised in the public repository.

## Project 1 Architectural Objective

Project 1 does not redesign the architecture. It improves its public usability by:
- systematising repository structure;
- documenting host/VM responsibilities;
- reducing manual bring-up steps;
- introducing Ansible-based automation for the single-node baseline.

## Later Phases

Later phases may extend this architecture to:
- multi-node private Solana clusters;
- richer observability flows;
- adaptive load-control layers.

