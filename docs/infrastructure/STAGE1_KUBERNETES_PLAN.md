# Stage 1 Kubernetes Plan for Project 1 Transition Platform

## 1. Purpose

This document defines the Stage 1 infrastructure plan for building the initial Kubernetes-based research platform that will support the transition from Project 1 to Project 2.

The immediate purpose of Stage 1 is not to build the final multi-node Agave/Solana architecture, but to establish a controlled, reproducible, and operationally manageable Kubernetes environment that can later host the Mode A baseline.

## 2. Scope of Stage 1

Stage 1 covers:

- preparation of the virtual infrastructure on the existing datacentre server;
- creation of the Kubernetes cluster baseline;
- assignment of VM roles;
- selection of operating systems by role;
- preparation of observability and registry services;
- preparation of the environment required for later containerised experiments.

Stage 1 does **not** yet include:

- migration of the existing Project 1 workload into Kubernetes;
- replacement of `solana-test-validator` with a multi-node Agave/Solana testnet;
- implementation of Project 2 scaling profiles;
- full experimental execution in Kubernetes.

Those activities belong to later stages.

## 3. Stage 1 Goal

The goal of Stage 1 is to produce a working Kubernetes infrastructure that is ready to host Project 1 baseline workloads in a later stage.

At the end of Stage 1, the environment should include:

- a functioning Kubernetes control plane;
- a functioning worker pool;
- internal cluster networking;
- an internal image registry;
- a basic observability layer;
- documented VM roles and resource assignments;
- a stable operational basis for later deployment of Mode A components.

## 4. Infrastructure Context

The current physical infrastructure is assumed to be:

- one datacentre server;
- dual-processor Xeon platform;
- 192 GB RAM;
- KVM-based virtualisation;
- console-oriented administration with no dependency on graphical tools.

This is sufficient for the initial Stage 1 layout, provided that resources are assigned conservatively and the cluster is kept architecturally simple.

## 5. Architectural Principle

Because the environment is currently hosted on a single physical server, Stage 1 should prioritise:

- simplicity;
- determinism;
- resource visibility;
- reproducibility;
- low operational overhead.

Stage 1 should **not** attempt to emulate high availability in a way that adds complexity without delivering real fault isolation. In particular, a multi-control-plane design is not justified on a single physical server at this stage.

## 6. Target Stage 1 Topology

The recommended initial topology is:

- **1 VM — Control Plane**
- **3 VM — Worker Nodes**
- **1 VM — Ops / Observability / Registry / Build Runner**

This gives the cluster enough separation for management, workload placement, and support services while keeping the design compact and realistic for the available hardware.

If future experiments require more validator-, RPC-, or loadgen-related capacity, the worker pool may be expanded by adding:

- **+1 VM**
- or **+2 VM**

to the Worker Node set.

## 7. Role Definitions

## 7.1 Control Plane VM

Purpose:

- host the Kubernetes control plane;
- manage scheduling, cluster state, and API operations;
- act as the administrative coordination point of the cluster.

Operational principles:

- reserve this VM for Kubernetes control-plane duties;
- avoid placing experimental Solana workloads here unless absolutely necessary;
- keep this node operationally stable and predictable.

## 7.2 Worker Node VMs

Purpose:

- run future research workloads;
- host stateful or stateless experiment components in later stages;
- provide the execution layer for validators, RPC nodes, load generators, dashboards, scenario jobs, and related services.

Operational principles:

- keep workers relatively uniform where possible;
- use resource labelling or taints later if specific placement becomes necessary;
- treat the worker set as the main experimental compute pool.

## 7.3 Ops / Observability / Registry / Build Runner VM

Purpose:

- host internal registry services;
- host observability services;
- host build-related utilities and administration tooling;
- provide an operational support layer for the cluster.

Typical responsibilities:

- internal image registry or Harbor;
- Prometheus;
- build runner utilities;
- cluster operations scripts;
- optional bastion-style administration role.

Operational principles:

- keep support services separate from the main control plane;
- reduce interference between monitoring/build tasks and research workloads;
- use this VM as the anchor point for repeatable cluster operations.

## 8. Recommended Operating Systems

## 8.1 Hypervisor

Recommended OS:

- **CentOS Stream 9**

Reasoning:

- stable choice for the KVM host;
- aligned with the intended datacentre/server administration model;
- suitable for console-first operations.

## 8.2 Kubernetes VMs

Recommended OS:

- **CentOS Stream 9**

Reasoning:

- operational consistency across the cluster;
- simplified administration;
- reduced cross-platform variance during early infrastructure work;
- better alignment with a single disciplined server-side operating model.

## 8.3 Separate Ubuntu 24.04 Reference VM

Recommended only if needed later.

Purpose:

- run a comparison baseline outside Kubernetes;
- support a reference validator environment when direct comparison with a non-containerised path is required;
- provide a controlled external baseline for later scientific comparison.

Important note:

- this Ubuntu VM is **not required** for Stage 1 completion;
- it becomes useful later if comparative bare-VM versus Kubernetes tests are required.

## 9. Mode Assumption for Stage 1

Stage 1 remains aligned with **Mode A** only.

Mode A means:

- the research baseline remains single-node;
- the object of study remains the existing `solana-test-validator` workflow;
- no architectural shift to a multi-node Agave/Solana topology is made yet.

This is important because Stage 1 is an infrastructure preparation stage, not yet a change of scientific object.

## 10. Stage 1 Deliverables

Stage 1 should produce the following concrete outputs.

### 10.1 Virtual infrastructure deliverables

- created VM set;
- documented VM names;
- documented IP addresses;
- documented role assignments;
- documented resource allocations.

### 10.2 Kubernetes deliverables

- initialised cluster;
- accessible API server;
- joined worker nodes;
- working `kubectl` administration path;
- basic namespace strategy.

### 10.3 Support service deliverables

- internal image registry or Harbor instance;
- basic Prometheus deployment;
- documented storage decisions for support services;
- documented access procedure for operators.

### 10.4 Documentation deliverables

- Stage 1 infrastructure plan;
- VM role matrix;
- cluster runbook or installation notes;
- baseline cluster acceptance checklist.

## 11. Storage Considerations

At Stage 1, storage planning should remain pragmatic.

Recommended initial approach:

- local VM disks for cluster bootstrap;
- explicit documentation of disk sizes per VM;
- persistent storage planning sufficient for registry and Prometheus;
- no premature attempt to build a complex distributed storage platform.

The goal is not yet to solve full production-grade persistence, but to create a stable, documented, and adequate infrastructure baseline.

## 12. Networking Considerations

Stage 1 networking must provide:

- stable VM-to-VM connectivity;
- predictable internal addressing;
- reliable control-plane to worker communication;
- operator access to cluster management endpoints;
- clear connectivity from workers to internal registry and observability services.

Networking documentation should include:

- VM names;
- IP addresses;
- subnet information;
- any firewall allowances required for KVM and Kubernetes communication.

## 13. Registry Strategy for Stage 1

Stage 1 should include an internal image distribution path.

Recommended approach:

- start with an internal registry service;
- optionally evolve to Harbor later if policy, organisation, or lifecycle management requires it;
- use this service to support later deployment of custom images.

Why this matters:

- Project 1 and Project 2 will require a mix of upstream and custom images;
- internal control over images improves reproducibility;
- dependence on external registry access should be reduced wherever practical.

## 14. Observability Strategy for Stage 1

Stage 1 should include a basic observability layer from the outset.

Recommended initial component:

- Prometheus

Purpose:

- collect cluster-level metrics;
- prepare the environment for later workload metrics;
- establish observability as a first-class infrastructure concern rather than an afterthought.

The observability layer at this stage does not need to be complex. It needs to be present, documented, and operational.

## 15. Stage 1 Acceptance Criteria

Stage 1 should be considered complete only if all of the following conditions are satisfied:

1. the required VMs are created and reachable;
2. the Kubernetes control plane is operational;
3. the worker nodes have joined the cluster successfully;
4. the internal registry is reachable from the cluster;
5. the observability VM is operational;
6. Prometheus is running in a basic usable form;
7. the role and resource allocation of all VMs is documented;
8. cluster administration can be performed repeatably from the designated operations path.

## 16. Stage 1 Risks

The main risks at Stage 1 are:

- overcomplicating the architecture too early;
- poor VM resource allocation;
- unclear separation between support services and experiment workloads;
- network misconfiguration between VMs;
- treating a single-physical-server environment as if it were true multi-fault-domain infrastructure.

## 17. Risk Mitigation Strategy

Recommended mitigation actions:

- keep the topology simple;
- use one control plane only;
- separate support services from worker workloads;
- document resource allocation explicitly;
- verify networking early with cluster smoke tests;
- avoid introducing Stage 2 or Stage 6 concerns into Stage 1 execution.

## 18. Relation to Later Stages

Stage 1 is the infrastructure foundation for all later work.

It directly enables:

- Stage 2: repository preparation for buildability and containerisation;
- Stage 3: image building and publication;
- Stage 4: Kubernetes-based reproduction of Mode A;
- Stage 6: later transition toward Project 2 and multi-node architecture.

Without a disciplined Stage 1, later experimental migration risks becoming inconsistent, fragile, and difficult to evaluate scientifically.

## 19. Stage 1 Completion Statement

Stage 1 is complete when the Kubernetes infrastructure exists as a stable, documented, and operational platform that is ready to accept the containerised Project 1 baseline in a later stage.

In other words, Stage 1 is successful when infrastructure preparation is complete, even though the Project 1 workloads themselves may not yet have been deployed inside Kubernetes.
