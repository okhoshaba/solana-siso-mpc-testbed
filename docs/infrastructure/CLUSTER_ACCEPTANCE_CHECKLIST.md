# Cluster Acceptance Checklist for Stage 1

## 1. Purpose

This document defines the acceptance checklist for the Kubernetes infrastructure created in Stage 1.

Its function is to determine whether the Stage 1 environment is ready to be treated as the official infrastructure baseline for later project stages.

## 2. Scope

This checklist applies to:

- the VM layer;
- the Kubernetes control plane;
- the worker node pool;
- the internal registry;
- the Prometheus-based observability baseline;
- the minimum operational documentation required for the cluster.

This checklist does not yet validate the deployment of Project 1 research workloads.

## 3. Acceptance Principle

The cluster should be accepted only if it is both:

- **operationally working**; and
- **documented sufficiently** for repeatable future use.

A partially working but undocumented cluster should not be treated as a completed Stage 1 result.

## 4. VM Layer Acceptance

The VM layer is accepted only if all of the following are true:

- `k8s-cp-01` exists and is reachable;
- `k8s-wrk-01` exists and is reachable;
- `k8s-wrk-02` exists and is reachable;
- `k8s-wrk-03` exists and is reachable;
- `k8s-ops-01` exists and is reachable;
- hostnames are configured correctly;
- IP addressing is documented;
- actual CPU, RAM, and disk allocations match the intended plan closely enough to be operationally valid.

## 5. Operating System Acceptance

The operating system layer is accepted only if:

- all required packages are installed;
- SSH administration works;
- time synchronisation is working;
- required OS updates are applied;
- the systems are stable after reboot;
- node-to-node connectivity functions as expected.

## 6. Kubernetes Control Plane Acceptance

The control plane is accepted only if:

- the API server is reachable;
- `kubectl` administration works from the intended operations path;
- the control plane remains stable after initialisation;
- control-plane services are healthy;
- no unresolved bootstrap error remains.

## 7. Worker Node Acceptance

The worker node layer is accepted only if:

- all intended workers have joined the cluster;
- all intended workers appear in `kubectl get nodes`;
- all intended workers report `Ready`;
- workloads can be scheduled to workers successfully.

## 8. Core Cluster Function Acceptance

The cluster core is accepted only if:

- cluster DNS works;
- a simple test pod can be deployed;
- the test pod reaches Running state;
- in-cluster networking works for the test workload;
- basic pod lifecycle behaviour appears normal.

## 9. Registry Acceptance

The internal registry layer is accepted only if:

- the registry service is running;
- registry storage is available;
- a test image can be pushed successfully;
- a test image can be pulled successfully;
- worker nodes can consume images through the intended path;
- the registry endpoint and usage method are documented.

## 10. Observability Acceptance

The observability layer is accepted only if:

- Prometheus is deployed;
- Prometheus is reachable through the intended access path;
- Prometheus has at least a minimal set of scrape targets;
- Prometheus returns usable data;
- Prometheus storage location is documented.

## 11. Documentation Acceptance

Documentation is accepted only if the following repository artifacts exist and reflect reality:

- `docs/infrastructure/STAGE1_KUBERNETES_PLAN.md`
- `docs/infrastructure/VM_ROLE_MATRIX.md`
- `docs/infrastructure/STAGE1_EXECUTION_CHECKLIST.md`
- `docs/infrastructure/CLUSTER_ACCEPTANCE_CHECKLIST.md`

The documentation must match the actual deployed state closely enough for later reuse.

## 12. Minimum Operational Commands

The Stage 1 cluster should not be accepted unless the operator can successfully perform the following minimum commands or their documented equivalents:

- inspect node state;
- inspect system pods;
- deploy a basic test workload;
- inspect the registry path;
- inspect the Prometheus deployment;
- confirm basic cluster health.

The exact commands may vary by installation method, but the operator must be able to demonstrate these functions reliably.

## 13. Failure Conditions

Stage 1 should be considered not accepted if any of the following remain unresolved:

- one or more required VMs are missing;
- one or more VMs are unstable or unreachable;
- the control plane is not stable;
- one or more worker nodes fail to join or remain NotReady;
- test workloads cannot be scheduled;
- internal registry is absent or unusable;
- Prometheus is absent or unusable;
- documentation does not reflect the real environment.

## 14. Conditional Acceptance Rule

Conditional acceptance is allowed only for minor issues that do not affect the structural readiness of the cluster.

Examples of issues that may still allow conditional acceptance:

- minor naming inconsistencies already documented for later cleanup;
- small non-critical documentation refinements still pending;
- Prometheus dashboard polish not yet complete, provided scraping is already operational.

Examples of issues that do **not** allow acceptance:

- worker nodes not ready;
- registry unavailable;
- control plane unstable;
- lack of documentation for core infrastructure;
- inability to run a test workload.

## 15. Evidence to Record at Acceptance Time

When Stage 1 is accepted, the following evidence should be recorded in the repository or operational notes:

- final VM list;
- final IP list;
- final resource allocations;
- Kubernetes version;
- container runtime used;
- registry endpoint;
- Prometheus endpoint;
- date of acceptance;
- operator notes on any accepted limitations.

## 16. Stage 1 Acceptance Statement

Stage 1 is accepted when the Kubernetes environment is:

- deployed;
- reachable;
- operational;
- minimally observable;
- able to run test workloads; and
- sufficiently documented for later research use.

At that point, the project may legitimately proceed to containerisation and workload onboarding stages.
