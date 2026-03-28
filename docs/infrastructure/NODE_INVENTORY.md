# Node Inventory

## 1. Purpose

This document records the real infrastructure inventory for Stage 1 of the Kubernetes transition platform.

Its purpose is to move Stage 1 from abstract planning to infrastructure-specific execution.

This document should be updated whenever:

- the physical host characteristics are revised;
- VM names or roles change;
- VM resource allocations are changed;
- additional worker nodes are introduced.

## 2. Inventory Scope

This inventory covers:

- the physical host;
- the Stage 1 Kubernetes VMs;
- the optional reference VM outside Kubernetes, if later introduced.

## 3. Physical Host Inventory

| Field | Value |
|------|-------|
| Host server name | `<HOST_SERVER_NAME>` |
| Datacentre / rack / location | `<DATACENTRE_OR_LOCATION>` |
| Host role | KVM hypervisor for the research cluster |
| Host OS | CentOS Stream 9 |
| CPU platform | Dual Xeon |
| Total CPU cores / threads | `<CPU_CORES_THREADS>` |
| Total RAM | 192 GB |
| Primary storage layout | `<STORAGE_LAYOUT>` |
| Hypervisor stack | KVM / libvirt |
| Administration model | Console-first, no GUI dependency |
| Time sync method | `<TIME_SYNC_METHOD>` |
| Operator notes | `<NOTES>` |

## 4. Stage 1 VM Inventory

### 4.1 Mandatory VM Set

| VM Name | Role | OS | vCPU | RAM | Disk | Hostname | Planned IP | Current Status | Notes |
|--------|------|----|------|-----|------|----------|------------|----------------|------|
| `k8s-cp-01` | Kubernetes Control Plane | CentOS Stream 9 | 8 | 16 GB | 120 GB | `k8s-cp-01` | `<IP_CP_01>` | `<STATUS>` | Cluster control plane |
| `k8s-wrk-01` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | `k8s-wrk-01` | `<IP_WRK_01>` | `<STATUS>` | Future workload host |
| `k8s-wrk-02` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | `k8s-wrk-02` | `<IP_WRK_02>` | `<STATUS>` | Future workload host |
| `k8s-wrk-03` | Worker Node | CentOS Stream 9 | 16 | 32 GB | 200 GB | `k8s-wrk-03` | `<IP_WRK_03>` | `<STATUS>` | Future workload host |
| `k8s-ops-01` | Ops / Registry / Observability / Build Runner | CentOS Stream 9 | 8 | 24 GB | 250 GB | `k8s-ops-01` | `<IP_OPS_01>` | `<STATUS>` | Prometheus, registry, ops tooling |

### 4.2 Optional Expansion VM Set

Use this section only when worker expansion becomes real rather than hypothetical.

| VM Name | Role | OS | vCPU | RAM | Disk | Hostname | Planned IP | Current Status | Notes |
|--------|------|----|------|-----|------|----------|------------|----------------|------|
| `k8s-wrk-04` | Worker Node | CentOS Stream 9 | 16 | 24-32 GB | 200 GB | `k8s-wrk-04` | `<IP_WRK_04>` | `<STATUS>` | Optional expansion node |
| `k8s-wrk-05` | Worker Node | CentOS Stream 9 | 16 | 24-32 GB | 200 GB | `k8s-wrk-05` | `<IP_WRK_05>` | `<STATUS>` | Optional expansion node |

### 4.3 Optional External Reference VM

This VM is not required for Stage 1 completion, but may later be useful for comparison against a non-Kubernetes baseline.

| VM Name | Role | OS | vCPU | RAM | Disk | Hostname | Planned IP | Current Status | Notes |
|--------|------|----|------|-----|------|----------|------------|----------------|------|
| `ref-ubuntu-01` | External reference baseline VM | Ubuntu 24.04 LTS | 8-16 | 16-32 GB | 150-200 GB | `ref-ubuntu-01` | `<IP_REF_01>` | `<STATUS>` | Optional bare-VM comparison path |

## 5. Resource Summary

### 5.1 Mandatory Stage 1 Allocation

| Resource | Total Allocated |
|---------|------------------|
| vCPU | 64 |
| RAM | 136 GB |
| Virtual disk | 970 GB |

### 5.2 Host Headroom Check

| Resource | Host Total | Planned Allocation | Remaining Headroom | Notes |
|---------|------------|--------------------|--------------------|------|
| RAM | 192 GB | 136 GB | 56 GB | Reserve for hypervisor, cache, overhead |
| CPU | `<HOST_CPU_TOTAL>` | 64 vCPU | `<CPU_HEADROOM>` | Fill with actual host count |
| Disk | `<HOST_DISK_TOTAL>` | 970 GB virtual | `<DISK_HEADROOM>` | Depends on real storage layout |

## 6. Role Notes

### 6.1 `k8s-cp-01`
Use for:

- Kubernetes control plane;
- cluster API management;
- scheduling and control services.

Do not use for:

- primary Solana experiment workloads;
- ad hoc build-heavy tasks;
- dashboard or registry co-location unless forced by constraints.

### 6.2 `k8s-wrk-01` .. `k8s-wrk-03`
Use for:

- future validator-related workloads;
- loadgen workloads;
- dashboard and controller workloads if needed later;
- experiment Jobs.

Operational principle:

- keep workers relatively symmetric in Stage 1;
- specialise later only when workload evidence justifies it.

### 6.3 `k8s-ops-01`
Use for:

- internal image registry;
- Prometheus;
- administration tooling;
- build or packaging support tasks.

Operational principle:

- separate support services from experiment workers;
- keep this VM documented and stable.

## 7. Current Status Tracking

Use the following status vocabulary consistently:

- `planned`
- `created`
- `installed`
- `reachable`
- `cluster-joined`
- `operational`
- `retired`

Suggested interpretation:

- `planned` — exists only in documentation
- `created` — VM created but OS not yet fully prepared
- `installed` — OS installed and basic setup done
- `reachable` — SSH and network access verified
- `cluster-joined` — node joined to Kubernetes if applicable
- `operational` — ready for intended Stage 1 use
- `retired` — no longer part of the active plan

## 8. Inventory Update Rules

This inventory should be updated whenever:

- VM names change;
- IP addresses change;
- resource allocations are resized;
- a new worker node is added;
- the optional reference VM is introduced;
- a VM is removed from the active design.

## 9. Acceptance Condition for This Document

This document should be treated as complete for Stage 1 operational use only when:

- all mandatory VMs have real hostnames;
- all mandatory VMs have real IP assignments;
- all mandatory VMs have real resource assignments;
- the physical host details are no longer placeholder values.

## 10. Final Statement

This document is the authoritative infrastructure inventory for the Stage 1 environment.

It should be kept aligned with the actual server and VM state rather than with purely notional plans.
