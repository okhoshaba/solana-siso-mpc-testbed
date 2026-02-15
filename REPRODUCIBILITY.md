# Reproducibility

## Environments
- Controller host: Fedora (loadgen + dashboard + analysis)
- Plant VM: Solana validator + metrics exporter

## Required endpoints
- RPC (forwarded): http://127.0.0.1:8899
- Prometheus metrics (forwarded): http://127.0.0.1:9464/metrics
- Loadgen control: http://127.0.0.1:7070

## Sanity checks
Run:
```bash
bash scripts/sanity_check.sh
