# Experimental Setup for HP3C 2026

## Overview

This document describes the experimental setup used to generate the data reported in the HP3C 2026 paper.

## Testbed Architecture

### Controller Host
- Role: experiment control and orchestration
- Operating system: [TO FILL]
- CPU: [TO FILL]
- RAM: [TO FILL]

### Plant / Validator Node
- Role: private blockchain node under test
- Environment: [bare metal / VM / containerized VM]
- Operating system: [TO FILL]
- CPU: [TO FILL]
- RAM: [TO FILL]

### Additional Components
- Load generator: [TO FILL]
- Metrics exporter: [TO FILL]
- RPC endpoint: [TO FILL]
- Metrics endpoint: [TO FILL]

## Software Versions

- Validator software: [TO FILL]
- Solana / Agave version: [TO FILL]
- Load generator version or commit: [TO FILL]
- Metrics exporter version or commit: [TO FILL]
- Analysis scripts version or commit: [TO FILL]

## Workload Definition

### Benchmark Type
Synthetic transaction workload executed against a private blockchain testbed.

### Load Control Variable
- Commanded load variable: `u_cmd` or equivalent
- Achieved throughput variable: `u_ach` or equivalent

### Workload Parameters
- transaction type: [TO FILL]
- account set size: [TO FILL]
- transaction generation mode: [TO FILL]
- rate sweep or step schedule: [TO FILL]

## Run Protocol

Each experimental run should be described by:

- run identifier
- start time
- duration
- warm-up interval
- steady-state interval
- cool-down interval
- sampling interval

### Proposed Template
- warm-up: [TO FILL]
- measurement window: [TO FILL]
- cool-down: [TO FILL]
- sampling interval: [TO FILL]

## Recorded Metrics

The paper-facing workflow uses the following observable metrics:

- commanded load
- achieved throughput
- end-to-end latency
- inflight or backlog proxy
- error rate or overload proxy

## Repetition Policy

- number of repeated runs per operating point: [TO FILL]
- aggregation method: [median / mean / quantiles]
- outlier handling: [TO FILL]

## Selected Runs for the Paper

The final paper should explicitly list the raw runs that are considered canonical for the reported figures and tables.

## Notes

This setup document should reflect only the experiments used in the paper, not all experiments ever performed in the repository.

