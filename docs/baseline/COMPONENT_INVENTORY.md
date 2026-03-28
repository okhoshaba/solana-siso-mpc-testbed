# Component Inventory for Project 1 Baseline

## 1. Purpose

This document provides a structured inventory of the technical components that make up the current Project 1 baseline.

It is intended to support:

- baseline documentation;
- later containerisation work;
- mapping of current components to future Kubernetes workloads;
- clarification of ownership, runtime location, and operational role.

## 2. Inventory Summary

| Component | Role | Current Runtime Location | Technology | Main Config / Input | Main Ports | Current Operational State |
|----------|------|--------------------------|------------|---------------------|------------|---------------------------|
| `solana-test-validator` | Single-node blockchain test environment | VM | Solana binary | `~/yellowstone-geyser.json`, local ledger | `8899`, `9464` | Active baseline component |
| Payer funding step | Wallet preparation for traffic generation | VM | Solana CLI | payer public key, RPC URL | uses `8899` | Active baseline component |
| `solana-latency-research` | Latency research framework | VM | Go | `configs/config.local.yaml` | uses local RPC/metrics path | Active baseline component |
| SSH tunnel | Expose VM-local services to host | Host | OpenSSH | VM hostname, local port mappings | `8899`, `9464`, `10000` | Active baseline component |
| `loadgen2_bin` | Synthetic transaction load generator | Host | Go binary | keypair path, CLI flags | `7070`, uses `8899` | Active baseline component |
| Scenario scripts | Benchmark orchestration | Host | Bash | environment variables and script parameters | none | Active baseline component |
| `mpc_dashboard_v2.py` | Dashboard and visual monitoring | Host | Python | Python virtual environment, script inputs | `8050` | Active baseline component |
| Prometheus | Metrics collection | Intended environment component | Prometheus | scrape configuration | expected metrics path via `9464` | Present conceptually, not yet fully formalised in repo |

## 3. Detailed Component Records

## 3.1 `solana-test-validator`

**Component name**  
`solana-test-validator`

**Role**  
Single-node Solana blockchain node used as the current baseline network.

**Current runtime location**  
VM

**Technology**  
Solana command-line validator binary

**Main command**

```bash
solana-test-validator \
  --ledger ~/solana-localnet/ledger \
  --reset \
  --bind-address 127.0.0.1 \
  --rpc-port 8899 \
  --geyser-plugin-config ~/yellowstone-geyser.json
```

**Inputs / dependencies**

- local ledger path;
- local Geyser plugin configuration;
- Solana runtime installed on the VM.

**Ports**

- `8899` — RPC
- `9464` — metrics, as used in the current operational checks

**Future Kubernetes mapping**

- likely stateful workload;
- baseline candidate for Mode A containerised reproduction.

## 3.2 Payer funding step

**Component name**  
Payer funding step

**Role**  
Prepare the payer wallet before benchmark traffic generation.

**Current runtime location**  
VM

**Technology**  
Solana CLI

**Main commands**

```bash
PAYER="<payer_pubkey_from_stats>"
solana config set --url http://127.0.0.1:8899
solana balance "$PAYER"
solana airdrop 10000 "$PAYER"
solana balance "$PAYER"
```

**Inputs / dependencies**

- valid payer public key;
- reachable local validator RPC;
- Solana CLI configured on the VM.

**Ports**

- uses `8899`

**Future Kubernetes mapping**

- best represented as a one-shot Job or controlled init step.

## 3.3 `solana-latency-research`

**Component name**  
`solana-latency-research`

**Role**  
Run the latency research logic in the private single-node environment.

**Current runtime location**  
VM

**Technology**  
Go

**Main command**

```bash
cd ~/solana-latency-research
go run . --config configs/config.local.yaml
```

**Inputs / dependencies**

- repository checkout or working tree on the VM;
- local configuration file;
- local validator endpoint;
- corrected private-network code path.

**Ports**

- no standalone operator-facing port formally fixed here;
- participates in the metrics path used by the environment.

**Operational note**

The working VM version is adapted beyond the original public placeholder implementation and must later be reconciled with the GitHub repository.

**Future Kubernetes mapping**

- likely Deployment in Mode A containerised baseline.

## 3.4 SSH tunnel

**Component name**  
SSH forwarding tunnel

**Role**  
Transport access from the host to VM-local services.

**Current runtime location**  
Host

**Technology**  
OpenSSH

**Main command**

```bash
ssh -N -o ExitOnForwardFailure=yes \
  -L 127.0.0.1:8899:127.0.0.1:8899 \
  -L 127.0.0.1:9464:127.0.0.1:9464 \
  -L 127.0.0.1:10000:127.0.0.1:10000 \
  s
```

**Inputs / dependencies**

- SSH reachability to the VM;
- known VM hostname;
- local host ports available.

**Ports**

- local `8899`
- local `9464`
- local `10000`

**Future Kubernetes mapping**

- not expected to remain a core architectural element after migration;
- to be replaced by cluster networking, Services, and controlled port-forwarding.

## 3.5 `loadgen2_bin`

**Component name**  
`loadgen2_bin`

**Role**  
Generate controlled synthetic transaction load.

**Current runtime location**  
Host

**Technology**  
Go binary

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

**Inputs / dependencies**

- reachable RPC endpoint;
- payer keypair file;
- available local listen port;
- operator-selected traffic parameters.

**Ports**

- listens on `7070`
- uses RPC on `8899`

**Future Kubernetes mapping**

- likely Deployment for baseline reproduction;
- may later evolve into a scaled traffic generation layer for Project 2.

## 3.6 Scenario scripts

**Component name**  
Scenario scripts

**Role**  
Run benchmark scenarios and shape the traffic profile.

**Current runtime location**  
Host

**Technology**  
Bash

**Main commands**

Step test:

```bash
RATE_KEY=lambda HOLD=60 SAMPLE=2 LEVELS_STR="50 150 300 450 600 800 1000 1200 1300 1450 1650 1850 1650 1450 1300 1200 1000 800 600 450 300 150 50" bash scripts/knee_step_test.sh
```

Adaptive test:

```bash
RATE_KEY=lambda SAMPLE=2 DUR=20 START=1300 MULT=1.4 MAX=4000 \
SAT_STOP=0.92 LAT_MULT=1.25 ERR_STOP=0.5 \
bash scripts/knee_probe_adaptive.sh
```

**Inputs / dependencies**

- scenario scripts present in the repository or working directory;
- active load generator;
- active validator RPC;
- active supporting services.

**Ports**

- no dedicated listening port

**Future Kubernetes mapping**

- likely Job-based execution model.

## 3.7 `mpc_dashboard_v2.py`

**Component name**  
`mpc_dashboard_v2.py`

**Role**  
Provide visual monitoring for the benchmark process.

**Current runtime location**  
Host

**Technology**  
Python

**Main commands**

```bash
cd ~/siso_controller
source venv/bin/activate
python3 ./mpc_dashboard_v2.py
```

**Inputs / dependencies**

- Python virtual environment;
- dashboard script;
- required Python packages;
- active benchmark environment.

**Ports**

- `8050`

**Future Kubernetes mapping**

- likely Deployment with a Service and controlled local access.

## 3.8 Prometheus

**Component name**  
Prometheus

**Role**  
Metrics collection and scrape orchestration.

**Current runtime location**  
Not yet fully formalised in repository-managed baseline form

**Technology**  
Prometheus

**Inputs / dependencies**

- reachable metrics endpoint;
- scrape configuration.

**Ports**

- expected to consume metrics from `9464`

**Operational note**

Prometheus is conceptually part of the baseline environment, but its exact installation and repository-controlled configuration need to be made explicit in a later revision.

**Future Kubernetes mapping**

- dedicated observability workload.

## 4. Runtime Split Summary

The current runtime split is:

### VM-side

- `solana-test-validator`
- payer funding step
- `solana-latency-research`

### Host-side

- SSH tunnel
- `loadgen2_bin`
- scenario scripts
- dashboard

### Cross-cutting observability

- metrics endpoint
- Prometheus-compatible scraping model

## 5. Current Gaps Relevant to Future Migration

The following inventory-level issues should be kept in mind:

- some working code exists in corrected local form and is not yet fully aligned with the repository;
- Prometheus is not yet fully documented as a repository-managed component;
- exact persistent data paths beyond the validator ledger are not yet fully formalised in documentation;
- the current architecture uses a manual split between VM and host, which will later need to be mapped into Kubernetes workloads.

## 6. Use of This Inventory in Later Stages

This inventory will be used for:

- deciding which components become container images first;
- mapping current components to Kubernetes workload types;
- defining which components are stateful and which are stateless;
- identifying which inputs should later become ConfigMaps, Secrets, PVCs, or CLI arguments;
- checking that the Kubernetes-based Mode A reproduction still contains all baseline-critical roles.
