# VM Role Matrix for Stage 1

## 1. Purpose

This document defines the proposed VM role matrix for Stage 1 of the Kubernetes transition platform.

The purpose of the matrix is:

- to make the virtual infrastructure explicit;
- to identify the role of each VM;
- to provide an initial resource allocation model;
- to support disciplined deployment on the available physical server.

The values below are recommended starting allocations. They may be refined after real resource measurements.

## 2. Recommended Stage 1 VM Set

| VM Name | Role | Recommended OS | Initial vCPU | Initial RAM | Initial Disk | Purpose |
|--------|------|----------------|--------------|-------------|--------------|---------|
| `k8s-cp-01` | Kubernetes Control Plane | CentOS Stream 9 | 8 | 16 GB | 120 GB | Cluster control plane and API management |
| `k8s-wrk-01` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | Future research workloads |
| `k8s-wrk-02` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | Future research workloads |
| `k8s-wrk-03` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | Future research workloads |
| `k8s-ops-01` | Ops / Observability / Registry / Build Runner | CentOS Stream 9 | 8 | 24 GB | 250 GB | Registry, Prometheus, build and admin tooling |

## 3. Why This Allocation Is Recommended

The proposed allocation tries to balance four constraints:

1. preserve enough memory for multiple worker nodes;
2. keep support services off the control plane;
3. leave headroom on the physical host for the hypervisor and operational overhead;
4. start with a conservative but usable research cluster rather than an oversized design.

Using the table above, the total initial allocation is:

- **vCPU**: 64
- **RAM**: 136 GB
- **Disk**: 970 GB virtual allocation

This leaves useful RAM headroom on a 192 GB host for:

- the hypervisor;
- system overhead;
- storage/cache effects;
- later tuning or VM resizing.

## 4. VM-by-VM Notes

## 4.1 `k8s-cp-01`

**Role**

Primary Kubernetes control plane node.

**Recommended use**

- Kubernetes API server;
- scheduler;
- controller manager;
- cluster administration anchor.

**Do not use for**

- primary Solana workload execution;
- build-heavy tasks;
- ad hoc experiment processes.

**Why 8 vCPU / 16 GB RAM**

This is usually sufficient for a compact research cluster with a single control plane and moderate management load.

## 4.2 `k8s-wrk-01`

**Role**

General-purpose worker node.

**Recommended future use**

- validator-related workload experiments;
- RPC-related services;
- stateless research services;
- controlled benchmarking components.

**Why 16 vCPU / 32 GB RAM**

This gives enough room for meaningful experimental placement without exhausting host resources too early.

## 4.3 `k8s-wrk-02`

**Role**

General-purpose worker node.

**Recommended future use**

- separation of workloads from `k8s-wrk-01`;
- later support for validator/RPC/loadgen placement policies;
- additional capacity for Jobs and observability-adjacent workloads.

**Why same size as `k8s-wrk-01`**

Worker symmetry simplifies early operations, scheduling, and troubleshooting.

## 4.4 `k8s-wrk-03`

**Role**

General-purpose worker node.

**Recommended future use**

- third placement target for future research workloads;
- capacity reserve for later growth;
- support for experiments requiring isolation across workers.

**Why same size as other workers**

A uniform initial worker set is easier to administer and better suited to controlled experiments.

## 4.5 `k8s-ops-01`

**Role**

Support-services VM.

**Recommended use**

- internal image registry or Harbor;
- Prometheus;
- build scripts and runners;
- bastion-style administration utilities;
- future operational runbooks and tooling.

**Why 8 vCPU / 24 GB RAM**

This VM should be strong enough to host registry and observability functions without competing for resources with experimental worker workloads.

**Why 250 GB disk**

Registry storage and observability data can grow quickly, so this VM should start with a larger disk allocation than the control plane.

## 5. Optional Expansion VMs

If Stage 1 evolves and the worker pool needs more capacity, the following optional pattern is recommended.

| VM Name | Role | Recommended OS | Initial vCPU | Initial RAM | Initial Disk | Purpose |
|--------|------|----------------|--------------|-------------|--------------|---------|
| `k8s-wrk-04` | Worker Node | CentOS Stream 9 | 16 | 24-32 GB | 200 GB | Additional future research capacity |
| `k8s-wrk-05` | Worker Node | CentOS Stream 9 | 16 | 24-32 GB | 200 GB | Additional future research capacity |

Expansion principle:

- add worker VMs only when measured demand justifies them;
- do not expand the cluster merely for architectural appearance;
- preserve symmetry if possible.

## 6. Optional Reference VM Outside Kubernetes

A separate non-Kubernetes reference VM may be useful later for scientific comparison.

| VM Name | Role | Recommended OS | Initial vCPU | Initial RAM | Initial Disk | Purpose |
|--------|------|----------------|--------------|-------------|--------------|---------|
| `ref-ubuntu-01` | External reference baseline VM | Ubuntu 24.04 LTS | 8-16 | 16-32 GB | 150-200 GB | Bare-VM baseline comparison outside Kubernetes |

This VM is **optional** and is **not required** for Stage 1 completion.

Recommended later use:

- compare baseline Mode A outside Kubernetes versus inside Kubernetes;
- evaluate any containerisation or orchestration overhead;
- preserve a clean scientific reference point.

## 7. Resource Allocation Principles

The following principles should govern VM sizing.

### 7.1 Prefer measured refinement over theoretical perfection

The initial values are starting values. They should be tuned later based on:

- actual worker pressure;
- registry storage growth;
- Prometheus storage behaviour;
- experiment-driven CPU and memory demand.

### 7.2 Preserve host headroom

Do not allocate all physical RAM to VMs immediately.

The physical host must retain room for:

- the hypervisor;
- page cache;
- operational stability;
- unexpected demand spikes.

### 7.3 Keep the control plane protected

The control plane VM should remain operationally stable and should not be overloaded with research jobs.

### 7.4 Keep support services off worker nodes where practical

Separating support services from worker nodes reduces interference with future experiments.

## 8. Suggested Naming Convention

Recommended initial naming convention:

- `k8s-cp-01` — control plane
- `k8s-wrk-01` .. `k8s-wrk-03` — workers
- `k8s-ops-01` — support services
- `ref-ubuntu-01` — optional external reference VM

This naming scheme is:

- explicit;
- easy to extend;
- suitable for console-first administration;
- suitable for infrastructure documentation and scripts.

## 9. Stage 1 Minimum VM Acceptance Criteria

The VM layer for Stage 1 should be considered ready only if:

1. all required Stage 1 VMs exist;
2. each VM boots reliably;
3. network reachability is verified between the relevant VMs;
4. the assigned operating systems are installed and usable;
5. the documented CPU, RAM, and disk allocations match the actual VM configuration;
6. the role of each VM is unambiguous and documented.

## 10. Summary

The recommended Stage 1 VM matrix is intentionally conservative, structured, and suitable for a single-server research cluster.

Its main goals are:

- make the infrastructure explicit;
- keep roles clearly separated;
- preserve room for later scaling;
- support repeatable transition from the baseline Project 1 environment toward Kubernetes-based execution.
