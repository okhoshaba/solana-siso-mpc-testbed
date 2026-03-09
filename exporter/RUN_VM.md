# Run VM Baseline

## Status

The VM-side baseline workflow currently exists in working form, but parts of the bring-up process are still being systematised and automated.

## Purpose

This component supports the single-node private Solana baseline used for controlled benchmarking experiments.

## Current Project 1 objective

Project 1 focuses on:
- documenting the VM-side baseline workflow;
- reducing manual bring-up steps;
- introducing Ansible-based automation for the baseline deployment path.

## Planned usage path

1. prepare the VM environment;
2. apply baseline configuration;
3. start the private Solana baseline;
4. verify service readiness;
5. expose the environment for host-side benchmark execution.

## Note

The initial target is a reproducible single-node baseline rather than a full multi-node deployment framework.

