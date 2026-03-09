# Ansible Plan

## Purpose

This document outlines the planned use of Ansible to reduce manual deployment effort and improve reproducibility of the single-node private Solana baseline.

## Why Ansible Is Needed

The current baseline environment is functional, but parts of the infrastructure bring-up process are still performed manually. This creates friction for:
- reproducibility;
- technical review;
- release packaging;
- later reuse by external researchers or builders.

Project 1 therefore introduces Ansible-based automation for the baseline deployment path.

## Project 1 Automation Scope

The Ansible work in Project 1 is limited to the single-node baseline.

Planned coverage includes:
- baseline VM preparation;
- installation or preparation of required supporting tools;
- baseline host-side preparation where appropriate;
- configuration templating;
- verification steps for bring-up readiness.

## Planned Layout

The intended structure is:

- `automation/ansible/inventory/`
- `automation/ansible/group_vars/`
- `automation/ansible/playbooks/`
- `automation/ansible/roles/`

## Planned Playbooks

### `baseline_vm.yml`
Prepare the VM-side baseline environment.

### `baseline_host.yml`
Prepare the host-side baseline support environment where needed.

### `verify.yml`
Run basic verification steps for the baseline deployment path.

## Out of Scope

Project 1 does not attempt to provide:
- full multi-node orchestration;
- production-grade infrastructure automation;
- complete later-stage cluster lifecycle management.

## Intended Outcome

By the end of Project 1, the single-node private Solana baseline should have a documented and partially automated deployment path that significantly reduces manual setup effort.

