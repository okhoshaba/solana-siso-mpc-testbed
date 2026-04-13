# Canonical Dataset for HP3C 2026

## Canonical Paper Path

The canonical paper-facing path for HP3C 2026 is:

`raw_selected -> processed -> figures`

Processed paper files are staged in `paper/hp3c2026/data/processed`.

`paper/hp3c2026/results` is reserved for future synthesis outputs and is intentionally empty at this stage.

## Raw Files

Files staged in `paper/hp3c2026/data/raw_selected`:

- `steady_low_2026-02-28_133431.csv`
- `steady_mid_2026-02-28_183006.csv`
- `steady_high_3550_2026-02-28_195846.csv`
- `knee_step_2026-02-28_191122.csv`

Source paths:

- `data/raw/steady_low_2026-02-28_133431.csv`
- `data/raw/steady_mid_2026-02-28_183006.csv`
- `data/raw/steady_high_3550_2026-02-28_195846.csv`
- `data/raw/knee_step_2026-02-28_191122.csv`

## Processed Files

Files staged in `paper/hp3c2026/data/processed`:

- `segments_steady_low.csv`
- `segments_mid.csv`
- `segments_high_3550.csv`
- `segments_knee_final.csv`

Source paths:

- `results/segments_steady_low.csv`
- `results/segments_mid.csv`
- `results/segments_high_3550.csv`
- `results/segments_knee_final.csv`

## Figure Files

Files staged in `paper/hp3c2026/figures`:

- `knee_step_2026-02-28_191122__u_cmd_vs_u_ach.png`
- `knee_step_2026-02-28_191122__lat_p99_vs_u_cmd.png`
- `knee_step_2026-02-28_191122__saturation_vs_u_cmd.png`
- `steady_high_3550_2026-02-28_195846__throughput_timeseries.png`
- `steady_low_2026-02-28_133431__lat_p99_vs_u_cmd.png`
- `steady_mid_2026-02-28_183006__lat_p99_vs_u_cmd.png`
- `steady_high_3550_2026-02-28_195846__lat_p99_vs_u_cmd.png`

Source paths:

- `results/figures/knee_step_2026-02-28_191122__u_cmd_vs_u_ach.png`
- `results/figures/knee_step_2026-02-28_191122__lat_p99_vs_u_cmd.png`
- `results/figures/knee_step_2026-02-28_191122__saturation_vs_u_cmd.png`
- `results/figures/steady_high_3550_2026-02-28_195846__throughput_timeseries.png`
- `results/figures/steady_low_2026-02-28_133431__lat_p99_vs_u_cmd.png`
- `results/figures/steady_mid_2026-02-28_183006__lat_p99_vs_u_cmd.png`
- `results/figures/steady_high_3550_2026-02-28_195846__lat_p99_vs_u_cmd.png`

## Excluded or Secondary Files

Do not include in the canonical paper path:

- `data/raw/knee_probe_2026-02-28_180332.csv`
- `data/raw/knee_step_2026-02-16_172027.csv`
- `data/raw/steady_high_2026-02-28_135022.csv`
- `data/raw/steady_high_sat_2026-02-28_185023.csv`
- `results/segments_high.csv`
- `results/segments_steady_high.csv`
- `results/segments_knee_2026-02-28.csv`
- `results/segments_knee_final_sat095.csv`
- `results/arx_model.json`
- `results/figures/steady_low_2026-02-28_133431__lat_p99_timeseries.png`
- `results/figures/steady_low_2026-02-28_133431__saturation_vs_u_cmd.png`
- `results/figures/steady_low_2026-02-28_133431__throughput_timeseries.png`
- `results/figures/steady_low_2026-02-28_133431__u_cmd_vs_u_ach.png`
- `results/figures/steady_mid_2026-02-28_183006__lat_p99_timeseries.png`
- `results/figures/steady_mid_2026-02-28_183006__saturation_vs_u_cmd.png`
- `results/figures/steady_mid_2026-02-28_183006__throughput_timeseries.png`
- `results/figures/steady_mid_2026-02-28_183006__u_cmd_vs_u_ach.png`
- `results/figures/knee_step_2026-02-28_191122__lat_p99_timeseries.png`
- `results/figures/knee_step_2026-02-28_191122__throughput_timeseries.png`
- `results/figures/steady_high_3550_2026-02-28_195846__lat_p99_timeseries.png`
- `results/figures/steady_high_3550_2026-02-28_195846__saturation_vs_u_cmd.png`
- `results/figures/steady_high_3550_2026-02-28_195846__u_cmd_vs_u_ach.png`
