# HP3C 2026 Archival Release Notes

## Purpose

This archival release prepares a stable public artifact package for the HP3C 2026 paper-facing analysis of bottleneck onset and saturation behavior in a private Solana testbed.

## Included Materials

The release includes the curated paper-facing dataset and figure set under the canonical path:

`raw_selected -> processed -> results -> figures`

Main included directories:

- `paper/hp3c2026/data/raw_selected/`
- `paper/hp3c2026/data/processed/`
- `paper/hp3c2026/results/`
- `paper/hp3c2026/figures/`

## Synthesis Outputs

- `bottleneck_onset_summary.csv` provides a compact regime-level summary of representative operating points for low, mid, knee, and high load regions. Its knee entry uses a transparent bottleneck-onset heuristic based on the first ascending knee point with `sat_med < 0.99`.
- `operating_regimes_summary.csv` maps each paper-facing regime to its corresponding raw file, processed file, core figure, and brief confounder note.

## Scope Notes

This release is limited to the selected public artifact for HP3C 2026. Excluded or secondary artifacts remain outside the canonical paper-facing path and are not part of the main archival narrative.

## Reproducibility Note

The archive is intended to support transparent inspection and paper-facing reproducibility of the selected synthetic-load experiments, summary tables, and figures. It does not claim turnkey reproduction of every local operational detail of the private testbed environment.

## Citation Note

Use the repository citation metadata for pre-release reference. Once the Zenodo DOI is minted, the Zenodo DOI should be preferred for archival citation.
