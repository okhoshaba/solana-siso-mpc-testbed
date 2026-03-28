# Kubernetes Bootstrap Method

## 1. Purpose

This document defines the chosen Kubernetes bootstrap method for Stage 1.

Its purpose is to answer the operational question:

> How exactly will the Stage 1 Kubernetes cluster be created?

This document should be treated as the methodological basis for the later installation runbook.

## 2. Chosen Method

The chosen bootstrap method for Stage 1 is:

- **kubeadm**
- with a **single control plane**
- using **containerd** as the default container runtime

## 3. Why This Method Is Chosen

This method is chosen because it provides:

- a standard and transparent Kubernetes installation path;
- a well-understood control-plane / worker model;
- good suitability for a console-first datacentre environment;
- explicit administrative control over the cluster structure;
- less abstraction than lightweight shortcut distributions.

For this project, that is useful because the cluster is not only an operational tool but also part of a research platform whose structure should remain explainable and reviewable.

## 4. Why Not Treat This as a Lightweight Distribution Task

Other distributions may be easier in some cases, but the current project benefits from a more explicit setup because:

- Stage 1 needs a clearly understandable classic Kubernetes model;
- later dissertation or technical reporting may need architectural transparency;
- the project should avoid hiding important operational assumptions inside a simplified installer.

This does not mean other methods are bad. It means `kubeadm` is the most appropriate default for this specific transition platform.

## 5. Chosen Runtime

The default runtime chosen here is:

- **containerd**

Reasoning:

- widely used;
- appropriate for Kubernetes environments;
- straightforward for a classical kubeadm-based cluster;
- a good default choice for a console-first server environment.

If later operational evidence suggests CRI-O is preferable for this environment, that change should be made deliberately and documented explicitly rather than silently substituted.

## 6. Chosen Control Plane Shape

The chosen control plane shape is:

- **one control-plane VM only**

Rationale:

- the entire Stage 1 environment is hosted on a single physical server;
- pseudo-high-availability would add complexity without providing real fault-domain separation;
- Stage 1 should prioritise clarity and stability rather than appearance of redundancy.

## 7. Chosen Node Model

The node model is:

- `k8s-cp-01` — control plane
- `k8s-wrk-01` — worker
- `k8s-wrk-02` — worker
- `k8s-wrk-03` — worker
- `k8s-ops-01` — support-services VM, not necessarily a worker unless deliberately chosen

Important note:

`k8s-ops-01` may be kept outside normal workload scheduling depending on the final operational decision. That choice should be documented before install-time execution.

## 8. Bootstrap Scope

This bootstrap method covers:

- operating-system preparation assumptions;
- runtime selection;
- control-plane initialisation logic;
- worker join logic;
- administrative access assumptions;
- post-bootstrap validation direction.

This document does not yet contain all commands. Those belong in the install runbook.

## 9. Required Preconditions

Before bootstrap begins, the following must already be true:

- all mandatory VMs exist;
- hostnames are fixed;
- IP addresses are fixed;
- DNS and gateway assumptions are known;
- inter-VM reachability is available;
- time synchronisation is functioning;
- Stage 1 role allocation is no longer theoretical.

## 10. High-Level Bootstrap Sequence

The bootstrap sequence should follow this order:

1. prepare all VMs at the OS level;
2. install containerd on Kubernetes nodes;
3. install kubeadm, kubelet, and kubectl where appropriate;
4. prepare required kernel and networking settings;
5. initialise the control plane on `k8s-cp-01`;
6. configure administrative access to the cluster;
7. join worker nodes;
8. validate node readiness;
9. install the selected CNI plugin;
10. validate basic scheduling and networking;
11. proceed to support service onboarding.

## 11. Planned Administrative Model

Administrative control should be exercised through a single clear path.

Recommended pattern:

- bootstrap initiated from `k8s-cp-01` and/or designated operator path;
- admin kubeconfig stored in a controlled and documented location;
- `kubectl` use performed from the chosen administration node or operator environment.

Document the exact chosen admin path here:

| Field | Value |
|------|-------|
| Admin execution host | `<ADMIN_EXECUTION_HOST>` |
| kubeconfig path | `<KUBECONFIG_PATH>` |
| Primary kubectl operator | `<PRIMARY_OPERATOR>` |
| Notes | `<NOTES>` |

## 12. Planned Networking Assumptions

The following network assumptions must be fixed before execution:

| Field | Value |
|------|-------|
| Node subnet | `<NODE_SUBNET>` |
| Pod CIDR | `<POD_CIDR>` |
| Service CIDR | `<SERVICE_CIDR>` |
| Cluster DNS domain | `<CLUSTER_DNS_DOMAIN>` |
| Planned CNI plugin | `<CNI_PLUGIN>` |
| API endpoint address | `<API_ENDPOINT>` |

These values must later match the installation runbook and actual cluster state.

## 13. Planned Support-Service Direction

After bootstrap, the cluster or support environment should be ready for:

- internal registry deployment;
- Prometheus deployment;
- later Mode A workload onboarding.

This is why Stage 1 bootstrap should be treated as infrastructure preparation, not as the final scientific deployment step.

## 14. Acceptance Criteria for This Method Choice

This bootstrap method should be treated as final for Stage 1 only if the following statements remain acceptable:

1. the project prefers a standard Kubernetes installation path;
2. the project accepts one control plane for Stage 1;
3. the project accepts containerd as the initial runtime choice;
4. the project intends to keep the install path transparent and well documented.

If any of those assumptions change, this document should be revised before install execution begins.

## 15. What Must Be Written Next

Once this method choice is accepted, the next concrete document should be:

- `docs/infrastructure/K8S_INSTALL_RUNBOOK.md`

That runbook should convert this method into:

- exact package choices;
- exact preparation steps;
- exact control-plane init sequence;
- exact worker join sequence;
- exact validation commands.

## 16. Final Statement

The Stage 1 Kubernetes bootstrap method is defined as a `kubeadm`-based, single-control-plane cluster using containerd as the initial runtime choice.

This method is selected because it best matches the project’s need for clarity, discipline, reviewability, and controlled later growth.
