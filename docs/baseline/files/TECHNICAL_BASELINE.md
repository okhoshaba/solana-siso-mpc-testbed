# Technical Baseline for Project 1

## 1. Purpose

This document defines the technical baseline of Project 1 before migration to a Kubernetes-based research platform.

The purpose of this baseline is:

- to formally record the currently working research workflow;
- to identify the exact software components, commands, ports, and dependencies;
- to preserve continuity with the existing Project 1 environment;
- to establish a reference point for later comparison with the Kubernetes-based implementation.

This baseline corresponds to the currently operational single-node Solana research stand used for latency and synthetic benchmark experiments.

## 2. Scope

This document covers:

- the current single-node Solana environment;
- the current split between the VM-side and host-side responsibilities;
- the operational workflow used to run the benchmark process;
- the current interaction between validator, funding, latency framework, load generator, dashboard, and metrics.

This document does not yet define the multi-node Agave/Solana architecture planned for Project 2.

## 3. Research Mode

**Mode A** is the baseline operational mode for Project 1.

Mode A is defined as:

- a **single-node** Solana test environment;
- based on `solana-test-validator`;
- used as the current experimental baseline;
- preserved specifically for continuity with Project 1 and for future comparison against the Kubernetes-based implementation.

## 4. Current Infrastructure

### 4.1 VM-side environment

A virtual machine is used to run the blockchain node and the latency research framework.

Current responsibilities of the VM:

- run `solana-test-validator`;
- store and reset the validator ledger;
- expose the Solana RPC endpoint;
- use the Geyser plugin configuration;
- run the adapted `solana-latency-research` framework.

### 4.2 Host-side environment

A host machine is used to run the traffic generation and visual monitoring components.

Current responsibilities of the host:

- create SSH tunnels to the VM;
- verify RPC and metrics availability;
- run the synthetic transaction load generator;
- execute experiment scenario scripts;
- run the dashboard for monitoring.

## 5. System Architecture Overview

The current Project 1 baseline uses a two-level split:

1. **VM level**
   - blockchain node;
   - latency framework.

2. **Host level**
   - SSH forwarding;
   - load generation;
   - experiment orchestration;
   - dashboard.

This means that the current baseline is operationally functional, but still partially manual and distributed across two execution environments.

## 6. Main Components

### 6.1 `solana-test-validator`

**Role**

A single-node local Solana test network used as the current blockchain object of study in Project 1.

**Responsibilities**

- create the local ledger;
- expose RPC on localhost;
- provide a controllable test environment;
- support the Geyser plugin;
- act as the transaction target for synthetic benchmarks.

**Main command**

```bash
solana-test-validator \
  --ledger ~/solana-localnet/ledger \
  --reset \
  --bind-address 127.0.0.1 \
  --rpc-port 8899 \
  --geyser-plugin-config ~/yellowstone-geyser.json
```

**Notes**

- `--reset` recreates the environment for a clean run.
- the validator is bound to `127.0.0.1`;
- external access is currently achieved via SSH forwarding from the host.

### 6.2 Payer funding step

**Role**

Preparation step required before running transaction load.

**Responsibilities**

- set the RPC URL;
- check payer balance;
- fund the payer account by airdrop;
- verify the balance after funding.

**Main commands**

```bash
PAYER="<payer_pubkey_from_stats>"
solana config set --url http://127.0.0.1:8899
solana balance "$PAYER"
solana airdrop 10000 "$PAYER"
solana balance "$PAYER"
```

**Example**

```bash
PAYER=6avCzMrjUDebRYtSoQ6GPQENjoxDaD2Udik8JzRnKbtb
solana config set --url http://127.0.0.1:8899
solana balance "$PAYER"
solana airdrop 10000 "$PAYER"
solana balance "$PAYER"
```

### 6.3 `solana-latency-research`

**Role**

A latency research framework adapted for the private single-node Solana environment used in Project 1.

**Responsibilities**

- connect to the local/private validator;
- run the latency analysis logic required by the experiments;
- expose or support metric collection for the study.

**Main command**

```bash
cd ~/solana-latency-research
go run . --config configs/config.local.yaml
```

**Notes**

- the original public repository version contained placeholders and logic for public Solana testnet/devnet usage;
- the VM currently contains a corrected and tested version adapted for the private test environment;
- this corrected state must later be reconciled with the GitHub repository.

### 6.4 SSH forwarding

**Role**

Expose VM-local services to the host machine.

**Responsibilities**

- forward the Solana RPC endpoint;
- forward the metrics endpoint;
- forward any additional service required for the experiment.

**Main command**

```bash
ssh -N -o ExitOnForwardFailure=yes \
  -L 127.0.0.1:8899:127.0.0.1:8899 \
  -L 127.0.0.1:9464:127.0.0.1:9464 \
  -L 127.0.0.1:10000:127.0.0.1:10000 \
  s
```

**Notes**

- `s` is the hostname of the VM;
- this tunnel is a critical current dependency of the baseline architecture;
- in the future Kubernetes architecture, this mechanism is expected to be replaced by internal cluster networking and controlled port forwarding.

### 6.5 Load generator

**Role**

Generate synthetic transaction traffic against the validator RPC endpoint.

**Responsibilities**

- issue transactions at controlled rates;
- use configurable concurrency and inflight parameters;
- provide load for step tests and adaptive tests.

**Main command**

```bash
~/siso_controller/loadgen2_bin \
  -rpc http://127.0.0.1:8899 \
  -keypair /home/khoshaba/siso_controller/payer.json \
  -listen 127.0.0.1:7070 \
  -workers 16 \
  -burst 1 \
  -inflight 128 \
  -lambda 20
```

**Current baseline runtime parameters**

- RPC endpoint: `http://127.0.0.1:8899`
- keypair file: `/home/khoshaba/siso_controller/payer.json`
- listen address: `127.0.0.1:7070`
- workers: `16`
- burst: `1`
- inflight: `128`
- lambda: `20`

### 6.6 Experiment scenarios

**Role**

Run controlled transaction load profiles.

**Responsibilities**

- execute a step-profile load test;
- execute an adaptive search or probing procedure;
- drive the traffic generation process under reproducible parameter sets.

**Step test command**

```bash
RATE_KEY=lambda HOLD=60 SAMPLE=2 LEVELS_STR="50 150 300 450 600 800 1000 1200 1300 1450 1650 1850 1650 1450 1300 1200 1000 800 600 450 300 150 50" bash scripts/knee_step_test.sh
```

**Adaptive test command**

```bash
RATE_KEY=lambda SAMPLE=2 DUR=20 START=1300 MULT=1.4 MAX=4000 \
SAT_STOP=0.92 LAT_MULT=1.25 ERR_STOP=0.5 \
bash scripts/knee_probe_adaptive.sh
```

### 6.7 Dashboard

**Role**

Provide visual monitoring of the benchmark process.

**Responsibilities**

- show the current benchmark state;
- support analysis of the synthetic load process;
- provide a browser-accessible interface on the host.

**Main commands**

```bash
cd ~/siso_controller
source venv/bin/activate
python3 ./mpc_dashboard_v2.py
```

**Dashboard URL**

```text
http://127.0.0.1:8050
```

### 6.8 Prometheus

**Role**

Collect experiment-related metrics.

**Current status**

- Prometheus is part of the intended baseline operational environment;
- however, its installation and exact baseline configuration are not yet fully formalised in the current manual workflow.

**Baseline interpretation**

Prometheus must be treated as a required metrics component of the environment, but its exact installation and scrape configuration still need to be fixed explicitly in the repository during the next documentation revision.

## 7. Port Map

| Port | Location | Purpose |
|------|----------|---------|
| 8899 | VM, forwarded to host | Solana RPC |
| 9464 | VM, forwarded to host | Metrics endpoint |
| 10000 | VM, forwarded to host | Additional forwarded service |
| 7070 | Host | Load generator listen endpoint |
| 8050 | Host | Dashboard web interface |

## 8. End-to-End Workflow

The current Project 1 baseline workflow is as follows:

1. Start `solana-test-validator` on the VM.
2. Fund the payer wallet on the VM.
3. Start `solana-latency-research` on the VM.
4. Start SSH forwarding from the host to the VM.
5. Verify port forwarding, RPC health, and metrics availability from the host.
6. Start the load generator on the host.
7. Execute the chosen benchmark scenario script on the host.
8. Start the dashboard on the host.
9. Observe the dashboard and collect metrics.

## 9. Baseline Operational Assumptions

The following assumptions are currently true for Project 1:

- the validator is local to the VM and bound to localhost;
- the host accesses validator services via SSH forwarding;
- the payer must be funded before meaningful traffic generation begins;
- the load generator depends on a valid payer keypair and RPC availability;
- the dashboard runs separately from the validator;
- the setup is manual but reproducible if the correct order of operations is followed.

## 10. Current Limitations

The current baseline has the following limitations:

- the workflow is partly manual;
- the environment is split across VM and host;
- service communication depends on SSH tunnelling;
- Prometheus is not yet fully formalised as a repository-managed component;
- some corrected or production-relevant code still exists primarily in local working form rather than fully synchronised repository form;
- the current setup is a single-node environment and does not yet represent a multi-node Agave/Solana architecture.

## 11. Why This Baseline Matters

This baseline is the formal reference point for all subsequent work.

It will be used for:

- containerisation of existing components;
- migration of Mode A into Kubernetes;
- comparison between baseline and Kubernetes execution;
- evaluation of whether orchestration changes influence experimental results;
- later architectural transition to Project 2.

## 12. Baseline Invariants for Future Comparison

The following properties should be preserved when reproducing this baseline in Kubernetes:

- single-node experimental mode;
- same logical order of operations;
- same functional role of each component;
- equivalent RPC availability;
- equivalent payer funding step;
- equivalent load generation logic;
- equivalent scenario execution logic;
- equivalent dashboard and metrics visibility.

Any deviation from these invariants must be explicitly documented and justified.
