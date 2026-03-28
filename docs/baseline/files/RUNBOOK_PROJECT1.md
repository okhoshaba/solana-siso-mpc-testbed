# Runbook for Project 1 Baseline

## 1. Purpose

This runbook describes the operational procedure for starting, validating, using, and stopping the current Project 1 baseline environment.

It is intended to provide a repeatable operator-facing procedure for the Mode A baseline before migration to Kubernetes.

## 2. Scope

This runbook covers:

- validator startup;
- payer funding;
- latency framework startup;
- SSH tunnel creation;
- availability checks;
- load generator startup;
- scenario execution;
- dashboard startup;
- basic shutdown and troubleshooting guidance.

## 3. Preconditions

Before starting the environment, the following conditions must hold:

- the VM is available over SSH;
- the VM contains `solana-test-validator`;
- the VM contains the working private-network version of `solana-latency-research`;
- the host contains the `loadgen2_bin` binary;
- the host contains the dashboard Python environment;
- the host has access to the required benchmark scripts;
- the required payer keypair file exists;
- the required Geyser plugin configuration file exists;
- the operator knows the VM hostname used in the SSH tunnel command.

## 4. Startup Procedure

The startup procedure must be executed in the order given below.

## 4.1 Start `solana-test-validator` on the VM

Run:

```bash
solana-test-validator \
  --ledger ~/solana-localnet/ledger \
  --reset \
  --bind-address 127.0.0.1 \
  --rpc-port 8899 \
  --geyser-plugin-config ~/yellowstone-geyser.json
```

Expected result:

- the validator starts successfully;
- the ledger is created or reset;
- the RPC endpoint becomes available on `127.0.0.1:8899`;
- no immediate fatal startup error is printed.

Operational note:

- keep this process running in its shell session while the experiment environment is active.

## 4.2 Fund the payer wallet on the VM

Run:

```bash
PAYER="<payer_pubkey_from_stats>"
solana config set --url http://127.0.0.1:8899
solana balance "$PAYER"
solana airdrop 10000 "$PAYER"
solana balance "$PAYER"
```

Example:

```bash
PAYER=6avCzMrjUDebRYtSoQ6GPQENjoxDaD2Udik8JzRnKbtb
solana config set --url http://127.0.0.1:8899
solana balance "$PAYER"
solana airdrop 10000 "$PAYER"
solana balance "$PAYER"
```

Expected result:

- Solana CLI points to the local RPC endpoint;
- the payer balance is visible before and after the airdrop;
- the airdrop succeeds;
- the post-airdrop balance is increased as expected.

## 4.3 Start `solana-latency-research` on the VM

Run:

```bash
cd ~/solana-latency-research
go run . --config configs/config.local.yaml
```

Expected result:

- the process starts without immediate fatal error;
- the local private-network configuration is accepted;
- the framework remains running for the duration of the experiment.

Operational note:

- this process should be treated as part of the active baseline environment and should remain running until the experiment finishes.

## 4.4 Start the SSH tunnel on the host

Run:

```bash
ssh -N -o ExitOnForwardFailure=yes \
  -L 127.0.0.1:8899:127.0.0.1:8899 \
  -L 127.0.0.1:9464:127.0.0.1:9464 \
  -L 127.0.0.1:10000:127.0.0.1:10000 \
  s
```

Expected result:

- the SSH session remains active;
- port forwarding is established without failure;
- the host can access RPC and metrics through localhost.

Operational note:

- `s` is the hostname of the VM;
- this session must remain active while the experiment is running.

## 4.5 Verify service availability from the host

### 4.5.1 Check that forwarded ports are listening

Run:

```bash
ss -lntp | egrep '(:8899|:9464)\b' || true
```

Expected result:

- listening or forwarded state is visible for the relevant ports.

### 4.5.2 Check RPC health

Run:

```bash
curl -s http://127.0.0.1:8899 -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"getHealth"}'
```

Expected result:

- the RPC endpoint responds successfully;
- the response is not empty;
- the validator appears operational.

### 4.5.3 Check metrics availability

Run:

```bash
curl -sS --max-time 2 http://127.0.0.1:9464/metrics | head -n 2
```

Expected result:

- the metrics endpoint responds;
- the output is non-empty and resembles Prometheus-style text metrics.

## 4.6 Start the load generator on the host

Run:

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

Expected result:

- the load generator starts successfully;
- the configured listen address is bound;
- the process remains running and ready for scenario execution.

Operational note:

- verify that the payer keypair path is correct before startup.

## 4.7 Execute the experiment scenario on the host

Choose one of the supported scenarios.

### 4.7.1 Step test

Run:

```bash
RATE_KEY=lambda HOLD=60 SAMPLE=2 LEVELS_STR="50 150 300 450 600 800 1000 1200 1300 1450 1650 1850 1650 1450 1300 1200 1000 800 600 450 300 150 50" bash scripts/knee_step_test.sh
```

Expected result:

- the script starts normally;
- the load profile progresses through the configured levels;
- the script completes without an unexplained early abort.

### 4.7.2 Adaptive test

Run:

```bash
RATE_KEY=lambda SAMPLE=2 DUR=20 START=1300 MULT=1.4 MAX=4000 \
SAT_STOP=0.92 LAT_MULT=1.25 ERR_STOP=0.5 \
bash scripts/knee_probe_adaptive.sh
```

Expected result:

- the adaptive probing sequence starts;
- rate control parameters are accepted;
- the script runs until its stopping condition is reached or the configured boundary is met.

## 4.8 Start the dashboard on the host

Run:

```bash
cd ~/siso_controller
source venv/bin/activate
python3 ./mpc_dashboard_v2.py
```

Expected result:

- the dashboard process starts;
- the web interface becomes reachable from the host.

Dashboard URL:

```text
http://127.0.0.1:8050
```

## 5. Normal Operational Flow

A normal run follows this order:

1. start validator;
2. fund payer;
3. start latency framework;
4. start SSH forwarding;
5. validate connectivity and metrics;
6. start load generator;
7. run the selected scenario;
8. start or observe dashboard;
9. monitor the experiment.

## 6. Shutdown Procedure

The baseline environment is currently a manually controlled environment. The recommended shutdown method is to stop the long-running processes in the reverse order of startup.

Suggested sequence:

1. stop the scenario script if it is still active;
2. stop the dashboard process;
3. stop the load generator;
4. terminate the SSH tunnel session;
5. stop `solana-latency-research`;
6. stop `solana-test-validator`.

Recommended operational method:

- terminate each process cleanly in the shell where it is running, typically with `Ctrl+C`;
- use forceful process termination only if clean shutdown is not possible.

## 7. Logs and Diagnostics

At baseline, the environment is primarily terminal-driven.

Current practical log sources:

- terminal output of `solana-test-validator`;
- terminal output of `solana-latency-research`;
- terminal output of `loadgen2_bin`;
- terminal output of scenario scripts;
- terminal output of the dashboard process;
- Prometheus-compatible metrics endpoint on the forwarded metrics port.

If persistent log files are later introduced, the repository documentation should be updated accordingly.

## 8. Troubleshooting

## 8.1 RPC health check fails

Possible causes:

- validator is not running;
- validator is still starting;
- SSH tunnel is not active;
- forwarding to `127.0.0.1:8899` failed.

Checks:

- verify the validator process on the VM;
- verify the SSH forwarding session;
- rerun the health check manually.

## 8.2 Metrics endpoint is unavailable

Possible causes:

- metrics exporter is not active;
- forwarding to port `9464` is not established;
- the latency framework or related service is not running as expected.

Checks:

- verify the SSH tunnel;
- verify the VM-side service expected to expose metrics;
- rerun the metrics curl command.

## 8.3 Payer funding fails

Possible causes:

- incorrect payer public key;
- validator RPC is unavailable;
- Solana CLI is pointing at a different RPC endpoint.

Checks:

- rerun `solana config get`;
- verify `solana balance "$PAYER"` before airdrop;
- verify validator availability on `127.0.0.1:8899`.

## 8.4 Load generator does not start

Possible causes:

- invalid keypair path;
- RPC endpoint unavailable;
- port `7070` already in use.

Checks:

- verify the keypair file exists;
- rerun the RPC health check;
- inspect local port usage.

## 8.5 Dashboard does not open

Possible causes:

- dashboard process did not start successfully;
- Python virtual environment is not activated;
- port `8050` is already in use.

Checks:

- inspect dashboard terminal output;
- verify the virtual environment;
- inspect local port usage.

## 8.6 Scenario script exits early

Possible causes:

- missing environment variables;
- load generator not running;
- RPC instability;
- script logic reached a stop condition.

Checks:

- verify the required environment variables in the command line;
- confirm that the load generator remains active;
- confirm that RPC health remains available.

## 9. Operator Notes

The current baseline environment is intentionally kept close to the working Project 1 procedure. It is not yet designed as a self-healing or fully automated platform.

The purpose of this runbook is not to optimise the workflow, but to preserve the currently functioning research procedure in a stable, documented form.

## 10. Next Use of This Runbook

This runbook will later be used for:

- comparison with the Kubernetes-based Mode A implementation;
- identification of what should become Jobs, Deployments, Services, PVCs, ConfigMaps, and Secrets;
- validation that the migration preserves the scientific and operational logic of Project 1.
