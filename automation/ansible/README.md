# Ansible Automation

## Purpose

This directory contains the baseline deployment automation for the single-node private Solana benchmarking environment.

## Objective

The objective of this automation layer is to reduce manual setup effort and improve reproducibility of the baseline environment.

## Project 1 Scope

Project 1 introduces Ansible-based automation for:
- preparing the VM-side baseline environment;
- preparing relevant host-side baseline support steps;
- templating and documenting configuration paths;
- verifying baseline deployment readiness.

## Planned Structure

- `inventory/` — example inventory files
- `group_vars/` — shared variables for the baseline environment
- `playbooks/` — baseline playbooks
- `roles/` — reusable automation roles

## Intended Outcome

The intended outcome is a reproducible single-node baseline deployment path suitable for public release and later technical extension.

