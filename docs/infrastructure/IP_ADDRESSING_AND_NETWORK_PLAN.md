# IP Addressing and Network Plan

## 1. Purpose

This document defines the network and IP addressing plan for the Stage 1 Kubernetes environment.

Its purpose is to convert the general infrastructure plan into a real, operator-usable network definition.

This document should describe the actual network state used for:

- the KVM host;
- the Kubernetes control plane;
- the worker nodes;
- the operations VM;
- any optional future expansion nodes.

## 2. Scope

This plan covers:

- addressing scheme;
- hostnames;
- subnet definition;
- gateway and DNS assumptions;
- VM-to-VM connectivity requirements;
- operator access requirements;
- service exposure rules relevant to Stage 1.

This plan does **not** yet define the full internal service mesh of future workloads, but it must be strong enough to support Stage 1 cluster bootstrap and later Stage 4 onboarding.

## 3. Network Design Principle

The network design should prioritise:

- simplicity;
- explicitness;
- stable addressing;
- ease of console-first administration;
- later compatibility with Kubernetes cluster communication.

Where possible, use predictable addressing rather than ad hoc assignments.

## 4. Physical Host Network Context

| Field | Value |
|------|-------|
| KVM host name | `<HOST_SERVER_NAME>` |
| Host management IP | `<HOST_MGMT_IP>` |
| Bridge interface | `<BRIDGE_INTERFACE_NAME>` |
| Upstream network / VLAN | `<NETWORK_OR_VLAN>` |
| Gateway | `<GATEWAY_IP>` |
| Primary DNS | `<DNS_PRIMARY>` |
| Secondary DNS | `<DNS_SECONDARY>` |
| Time/NTP source | `<NTP_SOURCE>` |
| Notes | `<NOTES>` |

## 5. Stage 1 VM Addressing Table

| VM Name | Hostname | Role | Planned IP | Netmask / CIDR | Gateway | DNS | Notes |
|--------|----------|------|------------|----------------|---------|-----|------|
| `k8s-cp-01` | `k8s-cp-01` | Control Plane | `<IP_CP_01>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Control-plane API host |
| `k8s-wrk-01` | `k8s-wrk-01` | Worker Node | `<IP_WRK_01>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Worker node |
| `k8s-wrk-02` | `k8s-wrk-02` | Worker Node | `<IP_WRK_02>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Worker node |
| `k8s-wrk-03` | `k8s-wrk-03` | Worker Node | `<IP_WRK_03>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Worker node |
| `k8s-ops-01` | `k8s-ops-01` | Ops / Registry / Observability | `<IP_OPS_01>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Ops and support services |

## 6. Optional Expansion Addressing Table

Use only when expansion nodes become real.

| VM Name | Hostname | Role | Planned IP | Netmask / CIDR | Gateway | DNS | Notes |
|--------|----------|------|------------|----------------|---------|-----|------|
| `k8s-wrk-04` | `k8s-wrk-04` | Worker Node | `<IP_WRK_04>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Optional expansion worker |
| `k8s-wrk-05` | `k8s-wrk-05` | Worker Node | `<IP_WRK_05>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Optional expansion worker |
| `ref-ubuntu-01` | `ref-ubuntu-01` | External reference VM | `<IP_REF_01>` | `<CIDR>` | `<GATEWAY_IP>` | `<DNS_PRIMARY>` | Optional non-K8s comparison node |

## 7. Suggested Addressing Rules

Recommended operational rules:

- one IP per VM;
- stable hostnames matching inventory names;
- do not reuse IPs casually between roles;
- document all changes immediately in the repository;
- prefer static assignment or stable DHCP reservation.

## 8. Required Connectivity Matrix

### 8.1 Control Plane Requirements

`k8s-cp-01` must be reachable from:

- all worker nodes;
- `k8s-ops-01`;
- the operator administration path.

It must also be able to reach:

- all worker nodes;
- DNS;
- package repositories if needed during installation.

### 8.2 Worker Node Requirements

Each worker node must be able to reach:

- `k8s-cp-01`;
- other worker nodes as required by Kubernetes;
- `k8s-ops-01` for registry and observability use;
- DNS and package sources as needed.

### 8.3 Ops VM Requirements

`k8s-ops-01` must be able to reach:

- `k8s-cp-01`;
- all worker nodes;
- registry clients or cluster consumers;
- Prometheus scrape targets where appropriate;
- operator administration path.

## 9. Operator Access Model

The operator should be able to access at minimum:

- the physical KVM host;
- `k8s-cp-01`;
- `k8s-ops-01`;
- worker nodes by SSH if required.

Operational principle:

- keep access controlled and explicit;
- do not rely on accidental open access;
- keep the administration path documented.

Document the main operator entrypoint here:

| Field | Value |
|------|-------|
| Primary operator entry path | `<OPERATOR_ENTRYPOINT>` |
| Primary operator workstation or jump host | `<JUMP_HOST_IF_ANY>` |
| SSH key model | `<SSH_KEY_MODEL>` |
| Notes | `<NOTES>` |

## 10. Kubernetes-Relevant Network Notes

Stage 1 networking must be sufficient for:

- control plane bootstrap;
- worker join operations;
- internal pod networking after cluster setup;
- registry access from nodes;
- observability scraping paths.

Record the chosen Kubernetes-related network assumptions:

| Field | Value |
|------|-------|
| Bootstrap method | `kubeadm` |
| CNI plugin (planned) | `<CNI_PLUGIN>` |
| Pod CIDR | `<POD_CIDR>` |
| Service CIDR | `<SERVICE_CIDR>` |
| Cluster DNS domain | `<CLUSTER_DNS_DOMAIN>` |
| API endpoint strategy | `<API_ENDPOINT_STRATEGY>` |

## 11. Firewall and Port Planning

This section should record the real firewall policy used for Stage 1.

### 11.1 Minimum documentation rule

Document at least:

- which ports are allowed between cluster nodes;
- which ports are allowed from the operator path;
- which ports are allowed for registry use;
- which ports are allowed for Prometheus access.

### 11.2 Stage 1 service exposure notes

Record intended exposure here:

| Service | Host / VM | Access Scope | Port / Endpoint | Notes |
|--------|-----------|--------------|-----------------|------|
| Kubernetes API | `k8s-cp-01` | Operator + nodes | `<API_PORT>` | Control plane access |
| Registry | `k8s-ops-01` | Cluster nodes + operator if needed | `<REGISTRY_PORT>` | Internal registry |
| Prometheus | `k8s-ops-01` | Operator path | `<PROMETHEUS_PORT>` | Observability |
| SSH | all VMs | Operator path | `22` | Administrative access |

## 12. DNS and Hostname Policy

Recommended rules:

- every VM should have a hostname matching the node inventory;
- forward and reverse expectations should be documented where relevant;
- avoid ambiguous short-lived hostnames;
- keep VM names stable once cluster bootstrap has begun.

## 13. Validation Checklist for This Plan

This network plan should be considered operationally ready only if:

- every mandatory VM has a real IP address;
- gateway and DNS values are fixed;
- operator access path is fixed;
- the CNI, pod CIDR, and service CIDR assumptions are fixed;
- required node-to-node connectivity is verified or ready to verify.

## 14. Final Statement

This document is the authoritative Stage 1 network and addressing plan.

It should be kept aligned with reality and used as the reference for cluster bootstrap, troubleshooting, and later workload onboarding.
