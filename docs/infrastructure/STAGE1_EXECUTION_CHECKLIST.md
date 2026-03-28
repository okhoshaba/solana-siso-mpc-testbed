# Stage 1 Execution Checklist

## 1. Purpose

This document defines the practical execution checklist for Stage 1 of the Kubernetes transition platform.

Its purpose is to convert the architectural Stage 1 plan into a concrete sequence of implementation actions.

This checklist is operational in nature. It should be used while building the environment on the datacentre server.

## 2. Stage 1 Objective

The objective of Stage 1 is to build a working Kubernetes infrastructure that is ready to host the future containerised Mode A baseline.

At the end of this checklist, the operator should have:

- a created VM set;
- a functioning Kubernetes control plane;
- joined worker nodes;
- a reachable operations VM;
- an internal image registry;
- a basic Prometheus deployment;
- documented infrastructure state.

## 3. Preconditions

Before starting Stage 1 execution, the following should already be available:

- physical server installed and operational;
- KVM available on the host;
- console access to the server;
- selected VM naming convention;
- selected IP addressing approach;
- selected storage allocation per VM;
- baseline Stage 1 documentation committed to the repository.

## 4. Execution Sequence Overview

The recommended order of execution is:

1. prepare the physical host;
2. create VM inventory and addressing plan;
3. create the VMs;
4. install operating systems on the VMs;
5. perform base OS hardening and administration setup;
6. install Kubernetes prerequisites;
7. initialise the control plane;
8. join worker nodes;
9. validate core cluster operation;
10. deploy registry;
11. deploy Prometheus;
12. document the final state.

## 5. Physical Host Preparation

Checklist:

- verify CentOS Stream 9 host is operational;
- verify KVM/libvirt stack is installed and functioning;
- verify sufficient free CPU, RAM, and storage remain available;
- verify bridge or virtual networking plan for VMs;
- verify console-based administration path;
- verify time synchronisation on the host.

Completion criteria:

- host is stable;
- virtualisation works correctly;
- there is enough remaining capacity for the full Stage 1 VM set.

## 6. VM Inventory and IP Planning

Checklist:

- assign names to all Stage 1 VMs;
- assign roles to all Stage 1 VMs;
- assign IP addresses or DHCP reservations;
- record subnet, gateway, and DNS settings;
- record expected SSH access method;
- record target vCPU, RAM, and disk for each VM.

Required VM set:

- `k8s-cp-01`
- `k8s-wrk-01`
- `k8s-wrk-02`
- `k8s-wrk-03`
- `k8s-ops-01`

Completion criteria:

- no ambiguity remains about naming, addressing, or role assignment.

## 7. VM Creation

Checklist:

- create control plane VM;
- create three worker VMs;
- create operations VM;
- allocate CPU, RAM, and disk according to the VM role matrix;
- attach network interfaces correctly;
- verify all VMs boot successfully.

Completion criteria:

- all Stage 1 VMs exist and boot reliably.

## 8. Base Operating System Installation

Checklist for each VM:

- install CentOS Stream 9;
- set hostname correctly;
- configure static IP or reserved DHCP as planned;
- configure DNS resolution;
- configure time synchronisation;
- create or verify the administrative user;
- verify SSH access;
- apply available package updates.

Completion criteria:

- all VMs are reachable and administratively usable.

## 9. Base OS Preparation

Checklist for each VM:

- verify hostnames resolve correctly;
- disable swap if required by chosen Kubernetes bootstrap method;
- configure required kernel/network settings;
- configure firewall rules as needed;
- install required administration tools;
- verify inter-VM connectivity using ping and SSH where appropriate.

Completion criteria:

- operating systems are prepared for Kubernetes installation.

## 10. Kubernetes Prerequisites

Checklist:

- install container runtime on all Kubernetes VMs;
- install kubeadm, kubelet, and kubectl where appropriate;
- enable and start required services;
- verify version consistency across the nodes;
- confirm that prerequisites are satisfied on control plane and worker nodes.

Completion criteria:

- Kubernetes prerequisites are installed and active on all cluster VMs.

## 11. Control Plane Initialisation

Checklist:

- initialise the Kubernetes control plane on `k8s-cp-01`;
- capture the join command for worker nodes;
- configure admin kubeconfig for the operations path;
- verify API server availability;
- verify control plane status.

Completion criteria:

- the control plane is initialised;
- cluster administration is possible through `kubectl`.

## 12. Worker Node Join Procedure

Checklist:

- join `k8s-wrk-01` to the cluster;
- join `k8s-wrk-02` to the cluster;
- join `k8s-wrk-03` to the cluster;
- verify all workers appear in the node list;
- verify worker nodes become Ready.

Completion criteria:

- all planned worker nodes have joined successfully and report Ready.

## 13. Core Cluster Validation

Checklist:

- run `kubectl get nodes`;
- run `kubectl get pods -A`;
- verify node readiness;
- verify core system pods are healthy;
- deploy a simple test pod;
- verify the test pod schedules to a worker;
- verify DNS and networking from inside the cluster.

Completion criteria:

- the cluster is functioning as a usable Kubernetes environment.

## 14. Registry Deployment

Checklist:

- deploy internal image registry on `k8s-ops-01` or through the cluster according to the chosen design;
- define registry storage location;
- verify registry reachability;
- verify that a test image can be pushed and pulled;
- document registry address and access procedure.

Completion criteria:

- internal registry is operational and usable by the cluster.

## 15. Prometheus Deployment

Checklist:

- deploy a basic Prometheus instance;
- define Prometheus storage location;
- verify Prometheus is running;
- verify Prometheus can scrape at least basic cluster or node-level targets;
- document the Prometheus access path.

Completion criteria:

- Prometheus is active in a basic usable state.

## 16. Documentation and Recording

Checklist:

- record final VM hostnames;
- record final IP addresses;
- record actual VM resource allocations;
- record actual Kubernetes version;
- record actual container runtime choice;
- record registry endpoint;
- record Prometheus endpoint;
- commit updated infrastructure notes into the repository.

Completion criteria:

- the environment is documented well enough to be rebuilt or reviewed later.

## 17. Stage 1 Completion Checklist

Stage 1 should be marked complete only if all items below are true:

- all planned VMs exist;
- all VMs are reachable;
- Kubernetes control plane is running;
- all worker nodes are joined and Ready;
- a test workload can be scheduled;
- internal registry works;
- Prometheus works;
- infrastructure state is documented.

## 18. Recommended Repository Outputs

After execution, the following repository artifacts should exist or be updated:

- `docs/infrastructure/STAGE1_KUBERNETES_PLAN.md`
- `docs/infrastructure/VM_ROLE_MATRIX.md`
- `docs/infrastructure/STAGE1_EXECUTION_CHECKLIST.md`
- `docs/infrastructure/CLUSTER_ACCEPTANCE_CHECKLIST.md`
- optional installation notes or host-specific runbooks

## 19. Notes on Discipline

Stage 1 should remain an infrastructure stage.

Avoid the following at this point:

- mixing in Stage 4 experiment deployment;
- prematurely designing the full Project 2 topology;
- installing research workloads before the cluster is stable;
- letting undocumented ad hoc changes replace the written plan.

## 20. Final Statement

This checklist should be used as the operational guide for building the Stage 1 environment.

Once completed, the project can move from infrastructure preparation to containerisation and workload onboarding.
