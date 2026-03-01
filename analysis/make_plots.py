#!/usr/bin/env python3
# make_plots.py (stdlib + matplotlib)
#
# Input: CSV from scripts/collect_csv.py (or older variants).
# Saves plots into results/figures (default) and optionally copies to paper/figures.

import argparse
import csv
import gzip
import math
import os
import statistics
from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple

import matplotlib.pyplot as plt


ALIASES = {
    "t_sec": ["t_sec", "t", "time_sec"],
    "u_cmd": ["u_cmd", "lam_cmd", "lambda", "target_lambda", "rate"],
    "sent_total": ["sent_total", "sent", "total_sent", "sent_ok_total", "ok_total"],
    "u_ach": ["u_ach", "u_ach_from_total", "u_ach_reported", "sent_per_sec", "sent_per_sec_reported"],
    "lat_p99": ["lat_p99", "y_lat_p99_sec", "lat_p99_sec", "p99", "latency_p99"],
    "inflight": ["inflight", "in_flight"],
    "err_per_sec": ["err_per_sec", "errors_per_sec", "errRate"],
}

def pick_col(fieldnames: List[str], keys: List[str]) -> Optional[str]:
    exact = {h.strip(): h.strip() for h in fieldnames}
    for k in keys:
        if k in exact:
            return k
    lower = {h.strip().lower(): h.strip() for h in fieldnames}
    for k in keys:
        lk = k.lower()
        if lk in lower:
            return lower[lk]
    return None

def ffloat(x: str) -> Optional[float]:
    x = (x or "").strip()
    if not x:
        return None
    try:
        return float(x)
    except Exception:
        return None

def fint(x: str) -> Optional[int]:
    x = (x or "").strip()
    if not x:
        return None
    try:
        return int(float(x))
    except Exception:
        return None

def median(xs: List[float]) -> float:
    return statistics.median(xs) if xs else float("nan")

@dataclass
class Row:
    t_sec: float
    u_cmd: float
    sent_total: Optional[int]
    u_ach: Optional[float]
    lat_p99: Optional[float]
    inflight: Optional[float]
    err_per_sec: Optional[float]

def open_maybe_gz(path: str):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", newline="")
    return open(path, "r", newline="")

def compute_u_ach_from_sent(rows: List[Row]) -> None:
    prev_sent = None
    prev_t = None
    for r in rows:
        if r.u_ach is not None and r.u_ach > 0:
            if r.sent_total is not None:
                prev_sent = r.sent_total
                prev_t = r.t_sec
            continue

        if r.sent_total is None or prev_sent is None or prev_t is None:
            if r.sent_total is not None:
                prev_sent = r.sent_total
                prev_t = r.t_sec
            continue

        dt = r.t_sec - prev_t
        ds = r.sent_total - prev_sent
        if dt > 0 and ds >= 0:
            r.u_ach = ds / dt

        prev_sent = r.sent_total
        prev_t = r.t_sec

def detect_segments_by_u_cmd(rows: List[Row], min_seg_s: float = 8.0) -> List[List[Row]]:
    if not rows:
        return []
    segs: List[List[Row]] = []
    cur = [rows[0]]
    for r in rows[1:]:
        if abs(r.u_cmd - cur[-1].u_cmd) < 1e-9:
            cur.append(r)
        else:
            segs.append(cur)
            cur = [r]
    segs.append(cur)

    out = []
    for s in segs:
        dur = s[-1].t_sec - s[0].t_sec
        if dur >= min_seg_s and len(s) >= 3:
            out.append(s)
    return out

def safe_stem(path: str) -> str:
    base = os.path.basename(path)
    for suf in [".csv.gz", ".csv"]:
        if base.endswith(suf):
            base = base[: -len(suf)]
            break
    return base.replace(" ", "_")

def ensure_dir(d: str) -> None:
    os.makedirs(d, exist_ok=True)

def save_fig(fig, outpath: str, dpi: int = 150):
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)

def maybe_copy(outpath: str, paper_dir: Optional[str]):
    if not paper_dir:
        return
    ensure_dir(paper_dir)
    dst = os.path.join(paper_dir, os.path.basename(outpath))
    try:
        # simple copy (no shutil to keep it minimal)
        with open(outpath, "rb") as fsrc:
            with open(dst, "wb") as fdst:
                fdst.write(fsrc.read())
    except Exception:
        pass

def main():
    ap = argparse.ArgumentParser(description="Build standard figures from a run CSV (stdlib + matplotlib, no pandas).")
    ap.add_argument("csv_path")
    ap.add_argument("--outdir", default="results/figures")
    ap.add_argument("--paperdir", default="", help="If set, copy figures to this dir as well (e.g., paper/figures)")
    ap.add_argument("--prefix", default="", help="Filename prefix for plots (default: stem of csv)")
    ap.add_argument("--min-seg-s", type=float, default=8.0, help="Minimum segment duration for step medians.")
    ap.add_argument("--dpi", type=int, default=150)
    args = ap.parse_args()

    paperdir = args.paperdir.strip() or None
    ensure_dir(args.outdir)

    with open_maybe_gz(args.csv_path) as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            raise SystemExit("ERROR: no header found")

        col_t = pick_col(r.fieldnames, ALIASES["t_sec"])
        col_u = pick_col(r.fieldnames, ALIASES["u_cmd"])
        col_sent = pick_col(r.fieldnames, ALIASES["sent_total"])
        col_uach = pick_col(r.fieldnames, ALIASES["u_ach"])
        col_lat = pick_col(r.fieldnames, ALIASES["lat_p99"])
        col_infl = pick_col(r.fieldnames, ALIASES["inflight"])
        col_err = pick_col(r.fieldnames, ALIASES["err_per_sec"])

        if col_t is None or col_u is None:
            raise SystemExit("ERROR: need t_sec and u_cmd (or aliases)")

        rows: List[Row] = []
        for row in r:
            t = ffloat(row.get(col_t, ""))
            u = ffloat(row.get(col_u, ""))
            if t is None or u is None:
                continue

            sent = fint(row.get(col_sent, "")) if col_sent else None
            uach = ffloat(row.get(col_uach, "")) if col_uach else None
            lat = ffloat(row.get(col_lat, "")) if col_lat else None
            infl = ffloat(row.get(col_infl, "")) if col_infl else None
            err = ffloat(row.get(col_err, "")) if col_err else None

            rows.append(Row(t_sec=t, u_cmd=u, sent_total=sent, u_ach=uach, lat_p99=lat, inflight=infl, err_per_sec=err))

    if len(rows) < 5:
        raise SystemExit(f"ERROR: too few rows parsed: {len(rows)}")

    # sort by time
    rows.sort(key=lambda x: x.t_sec)

    # fill missing u_ach from sent_total if possible
    compute_u_ach_from_sent(rows)

    prefix = args.prefix.strip() or safe_stem(args.csv_path)

    # ---------- Plot 1: throughput timeseries ----------
    t = [x.t_sec for x in rows]
    u_cmd = [x.u_cmd for x in rows]
    u_ach = [x.u_ach if (x.u_ach is not None and x.u_ach > 0) else float("nan") for x in rows]

    fig = plt.figure(figsize=(10, 4))
    ax = fig.add_subplot(111)
    ax.plot(t, u_cmd, label="u_cmd")
    ax.plot(t, u_ach, label="u_ach")
    ax.set_xlabel("time, s")
    ax.set_ylabel("tx/s")
    ax.set_title("Throughput tracking (u_cmd vs u_ach)")
    ax.legend()
    out1 = os.path.join(args.outdir, f"{prefix}__throughput_timeseries.png")
    save_fig(fig, out1, dpi=args.dpi)
    maybe_copy(out1, paperdir)

    # ---------- Plot 2: latency p99 timeseries ----------
    lat = [x.lat_p99 if (x.lat_p99 is not None and x.lat_p99 > 0) else float("nan") for x in rows]
    fig = plt.figure(figsize=(10, 4))
    ax = fig.add_subplot(111)
    ax.plot(t, lat, label="lat_p99")
    ax.set_xlabel("time, s")
    ax.set_ylabel("seconds")
    ax.set_title("Confirmation latency p99 (observed)")
    ax.legend()
    out2 = os.path.join(args.outdir, f"{prefix}__lat_p99_timeseries.png")
    save_fig(fig, out2, dpi=args.dpi)
    maybe_copy(out2, paperdir)

    # ---------- Step-level medians (for knee/scatter plots) ----------
    segs = detect_segments_by_u_cmd(rows, min_seg_s=args.min_seg_s)
    # If not step-like, treat as one segment
    if not segs:
        segs = [rows]

    lvl_u = []
    lvl_uach = []
    lvl_sat = []
    lvl_lat = []

    for s in segs:
        u = s[0].u_cmd
        uachs = [x.u_ach for x in s if x.u_ach is not None and x.u_ach > 0]
        lats = [x.lat_p99 for x in s if x.lat_p99 is not None and x.lat_p99 > 0]

        uach_med = median(uachs)
        lat_med = median(lats)

        sat_med = float("nan")
        if not math.isnan(uach_med) and u > 0:
            sat_med = uach_med / u

        lvl_u.append(u)
        lvl_uach.append(uach_med)
        lvl_sat.append(sat_med)
        lvl_lat.append(lat_med)

    # ---------- Plot 3: u_cmd vs u_ach (segment medians) ----------
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111)
    ax.scatter(lvl_u, lvl_uach)
    ax.set_xlabel("u_cmd, tx/s")
    ax.set_ylabel("median u_ach, tx/s")
    ax.set_title("u_cmd vs u_ach (segment medians)")
    out3 = os.path.join(args.outdir, f"{prefix}__u_cmd_vs_u_ach.png")
    save_fig(fig, out3, dpi=args.dpi)
    maybe_copy(out3, paperdir)

    # ---------- Plot 4: saturation vs u_cmd (segment medians) ----------
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111)
    ax.scatter(lvl_u, lvl_sat)
    ax.set_xlabel("u_cmd, tx/s")
    ax.set_ylabel("median saturation (u_ach/u_cmd)")
    ax.set_title("Saturation vs u_cmd (segment medians)")
    out4 = os.path.join(args.outdir, f"{prefix}__saturation_vs_u_cmd.png")
    save_fig(fig, out4, dpi=args.dpi)
    maybe_copy(out4, paperdir)

    # Optional: also output latency vs u_cmd for paper diagnostics (small & useful)
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111)
    ax.scatter(lvl_u, lvl_lat)
    ax.set_xlabel("u_cmd, tx/s")
    ax.set_ylabel("median lat_p99, s")
    ax.set_title("lat_p99 vs u_cmd (segment medians)")
    out5 = os.path.join(args.outdir, f"{prefix}__lat_p99_vs_u_cmd.png")
    save_fig(fig, out5, dpi=args.dpi)
    maybe_copy(out5, paperdir)

    print("Wrote figures:")
    for p in [out1, out2, out3, out4, out5]:
        print("  " + p)
    if paperdir:
        print(f"Also copied to paperdir: {paperdir}")

if __name__ == "__main__":
    main()
