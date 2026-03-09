# VM and Host Set-Up

## Purpose

This document clarifies the current separation of responsibilities between the host machine and the VM in the baseline testbed.

## Host Responsibilities

The host machine is currently used for:
- orchestrating experiment execution;
- running host-side load generation logic;
- collecting and organising outputs;
- data processing and plotting;
- supporting dashboard-related baseline functions.

## VM Responsibilities

The VM is currently used for:
- running the single-node private Solana baseline;
- hosting VM-side infrastructure required for the benchmark environment;
- supporting exporter and measurement-side functionality;
- serving as the experimental execution target for host-side tools.

## Current Manual Steps

At present, some infrastructure bring-up steps are still performed manually, including:
- parts of VM preparation;
- parts of baseline Solana bring-up;
- parts of host/VM co-ordination;
- some operational sequencing of experiment support components.

## Project 1 Objective

Project 1 aims to reduce manual effort by:
- documenting the current host/VM workflow clearly;
- formalising the minimum reproducible baseline path;
- introducing Ansible-based automation for the single-node baseline environment.

## Intended Outcome

The intended outcome is not a fully general infrastructure framework, but a reproducible and well-documented baseline deployment path suitable for public release and technical review.

