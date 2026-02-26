#!/usr/bin/env python3
# summarize_run.py (stdlib only)
#
# Summarizes a run CSV produced by scripts/collect_csv.py:
# t_iso,t_sec,u_cmd,sent_total,u_ach,lat_p99,inflight,err_per_sec
#
# Output:
# - overall stats (rows, dt stats, ranges)
# - segment stats (detect u_cmd steps and compute medians)
# - knee estimate (first segment where sat drops or latency grows)
# - suggested steady_low / steady_high
# - optionally writes a per-segment CSV summary

import argparse
import csv
import math
import statistics
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


ALIASES = {
    "t_sec": ["t_sec", "t", "time_sec"],
    "u_cmd": ["u_cmd", "lam_cmd", "lambda", "target_lambda", "rate"],
    "sent_total": ["sent_total", "sent", "total_sent", "sent_ok_total", "ok_total"],
    "u_ach": ["u_ach", "u_ach_from_total", "u_ach_reported", "sent_per_sec", "sent_per_sec_reported"],
    "lat_p99": ["lat_p99", "y_lat_p99_sec", "lat_p99_sec", "p99", "latency_p99"],
    "inflight": ["inflight", "in_flight"],
    "err_per_sec": ["err_per_sec", "err_per_sec_reported", "errors_per_sec"],
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

def pctl(xs: List[float], q: float) -> float:
    if not xs:
        return float("nan")
    xs2 = sorted(xs)
    if len(xs2) == 1:
        return xs2[0]
    # linear interpolation
    pos = (len(xs2) - 1) * q
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return xs2[lo]
    w = pos - lo
    return xs2[lo] * (1 - w) + xs2[hi] * w

@dataclass
class Row:
    t_sec: float
    u_cmd: float
    sent_total: Optional[int]
    u_ach: Optional[float]
    lat_p99: Optional[float]
    inflight: Optional[float]
    err_per_sec: Optional[float]

@dataclass
class Segment:
    idx: int
    u_cmd: float
    t_start: float
    t_end: float
    n: int
    u_ach_med: float
    sat_med: float
    lat_med: float
    lat_p95: float
    err_med: float
    inflight_max: float

def compute_u_ach_from_sent(rows: List[Row]) -> None:
    """Fill missing u_ach using Δsent_total/Δt when possible."""
    prev_sent = None
    prev_t = None
    for r in rows:
        if r.u_ach is not None:
            prev_sent = r.sent_total if r.sent_total is not None else prev_sent
            prev_t = r.t_sec
            continue
        if r.sent_total is None or prev_sent is None or prev_t is None:
            prev_sent = r.sent_total if r.sent_total is not None else prev_sent
            prev_t = r.t_sec
            continue
        dt = r.t_sec - prev_t
        ds = r.sent_total - prev_sent
        if dt > 0 and ds >= 0:
            r.u_ach = ds / dt
        prev_sent = r.sent_total
        prev_t = r.t_sec

def segment_by_u_cmd(rows: List[Row], min_seg_s: float = 8.0) -> List[List[Row]]:
    """Split into segments when u_cmd changes. Filters out too-short segments."""
    if not rows:
        return []
    segs: List[List[Row]] = []
    cur: List[Row] = [rows[0]]
    for r in rows[1:]:
        if abs(r.u_cmd - cur[-1].u_cmd) < 1e-9:
            cur.append(r)
        else:
            segs.append(cur)
            cur = [r]
    segs.append(cur)

    # drop segments that are too short (warmups/transients)
    out = []
    for s in segs:
        dur = s[-1].t_sec - s[0].t_sec
        if dur >= min_seg_s and len(s) >= 3:
            out.append(s)
    return out

def summarize_segment(seg_rows: List[Row], idx: int) -> Segment:
    u_cmd = seg_rows[0].u_cmd
    t_start = seg_rows[0].t_sec
    t_end = seg_rows[-1].t_sec
    n = len(seg_rows)

    uachs = [r.u_ach for r in seg_rows if r.u_ach is not None and r.u_ach > 0]
    lats  = [r.lat_p99 for r in seg_rows if r.lat_p99 is not None and r.lat_p99 > 0]
    errs  = [r.err_per_sec for r in seg_rows if r.err_per_sec is not None]
    infls = [r.inflight for r in seg_rows if r.inflight is not None]

    u_ach_med = median(uachs) if uachs else float("nan")
    sat_med = (u_ach_med / u_cmd) if (not math.isnan(u_ach_med) and u_cmd > 0) else float("nan")
    lat_med = median(lats) if lats else float("nan")
    lat_p95 = pctl(lats, 0.95) if lats else float("nan")
    err_med = median(errs) if errs else float("nan")
    infl_max = max(infls) if infls else float("nan")

    return Segment(
        idx=idx, u_cmd=u_cmd, t_start=t_start, t_end=t_end, n=n,
        u_ach_med=u_ach_med, sat_med=sat_med, lat_med=lat_med, lat_p95=lat_p95,
        err_med=err_med, inflight_max=infl_max
    )

def fmt(x: float, nd: int = 3) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "nan"
    return f"{x:.{nd}f}"

def main():
    ap = argparse.ArgumentParser(description="Summarize a run CSV (step/steady) into segment stats and knee estimate.")
    ap.add_argument("csv_path")
    ap.add_argument("--min-seg-s", type=float, default=8.0, help="Minimum segment duration to keep (seconds).")
    ap.add_argument("--sat-knee", type=float, default=0.92, help="Saturation threshold for knee detection.")
    ap.add_argument("--lat-mult-knee", type=float, default=1.25, help="Latency multiplier vs baseline for knee detection.")
    ap.add_argument("--sat-low", type=float, default=0.98, help="Saturation threshold for steady_low suggestion.")
    ap.add_argument("--lat-mult-low", type=float, default=1.10, help="Latency multiplier vs baseline for steady_low suggestion.")
    ap.add_argument("--out-segments-csv", default="", help="If set, write per-segment summary CSV here.")
    args = ap.parse_args()

    with open(args.csv_path, "r", newline="") as f:
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

    # compute dt stats
    dts = [rows[i].t_sec - rows[i-1].t_sec for i in range(1, len(rows)) if rows[i].t_sec > rows[i-1].t_sec]
    dt_med = median(dts)
    dt_min = min(dts) if dts else float("nan")
    dt_max = max(dts) if dts else float("nan")

    # fill missing u_ach
    compute_u_ach_from_sent(rows)

    # overall ranges
    u_cmds = [x.u_cmd for x in rows]
    uachs = [x.u_ach for x in rows if x.u_ach is not None and x.u_ach > 0]
    lats = [x.lat_p99 for x in rows if x.lat_p99 is not None and x.lat_p99 > 0]

    print("=== Run summary ===")
    print(f"file: {args.csv_path}")
    print(f"rows: {len(rows)}")
    print(f"t: {fmt(rows[0].t_sec)} .. {fmt(rows[-1].t_sec)} (sec)")
    print(f"dt median/min/max: {fmt(dt_med)} / {fmt(dt_min)} / {fmt(dt_max)} (sec)")
    print(f"u_cmd range: {fmt(min(u_cmds))} .. {fmt(max(u_cmds))}")
    if uachs:
        print(f"u_ach range: {fmt(min(uachs))} .. {fmt(max(uachs))}")
    else:
        print("u_ach: no valid samples (check /stats parsing or sent_total).")
    if lats:
        print(f"lat_p99 median/p95/max: {fmt(median(lats),4)} / {fmt(pctl(lats,0.95),4)} / {fmt(max(lats),4)} (s)")
    else:
        print("lat_p99: no valid samples (check /metrics).")
    print()

    # segments
    segs_raw = segment_by_u_cmd(rows, min_seg_s=args.min_seg_s)
    if not segs_raw:
        print("No step segments detected (likely steady run). Creating a single segment.")
        segs_raw = [rows]

    segs: List[Segment] = []
    for i, s in enumerate(segs_raw, 1):
        segs.append(summarize_segment(s, idx=i))

    # baseline latency: take first segment with valid lat_med
    baseline_lat = float("nan")
    for s in segs:
        if not math.isnan(s.lat_med) and s.lat_med > 0:
            baseline_lat = s.lat_med
            break

    print("=== Segment table (by detected u_cmd steps) ===")
    print("idx  u_cmd  dur_s  n   u_ach_med  sat_med  lat_med(s)  lat_p95(s)  err_med  infl_max")
    for s in segs:
        dur = s.t_end - s.t_start
        print(
            f"{s.idx:>3d}  {fmt(s.u_cmd,0):>5}  {fmt(dur,1):>5}  {s.n:>3d}  "
            f"{fmt(s.u_ach_med,1):>8}  {fmt(s.sat_med,3):>7}  "
            f"{fmt(s.lat_med,4):>9}  {fmt(s.lat_p95,4):>10}  "
            f"{fmt(s.err_med,3):>7}  {fmt(s.inflight_max,0):>8}"
        )
    print()

    # knee detection
    knee = None
    if not math.isnan(baseline_lat):
        for s in segs:
            sat_bad = (not math.isnan(s.sat_med)) and (s.sat_med <= args.sat_knee)
            lat_bad = (not math.isnan(s.lat_med)) and (s.lat_med >= args.lat_mult_knee * baseline_lat)
            if sat_bad or lat_bad:
                knee = s
                break

    print("=== Knee estimate ===")
    if math.isnan(baseline_lat):
        print("baseline_lat: nan (no latency samples) -> cannot compute latency-based knee")
    else:
        print(f"baseline lat_p99 (median): {fmt(baseline_lat,4)} s")
    if knee is None:
        print("knee: not detected under current thresholds.")
    else:
        print(
            f"knee first trigger at u_cmd≈{fmt(knee.u_cmd,0)} "
            f"(sat_med={fmt(knee.sat_med,3)}, lat_med={fmt(knee.lat_med,4)}s)"
        )
    print()

    # suggest steady_low / steady_high
    steady_low = None
    steady_high = None
    if not math.isnan(baseline_lat):
        # low: highest u_cmd that still has sat>=sat_low AND lat <= lat_mult_low*baseline
        low_cands = []
        for s in segs:
            ok_sat = (not math.isnan(s.sat_med)) and (s.sat_med >= args.sat_low)
            ok_lat = (math.isnan(s.lat_med)) or (s.lat_med <= args.lat_mult_low * baseline_lat)
            if ok_sat and ok_lat:
                low_cands.append(s)
        if low_cands:
            steady_low = max(low_cands, key=lambda x: x.u_cmd)

        # high: lowest u_cmd where sat<=sat_knee OR lat>=lat_mult_knee*baseline
        high_cands = []
        for s in segs:
            sat_bad = (not math.isnan(s.sat_med)) and (s.sat_med <= args.sat_knee)
            lat_bad = (not math.isnan(s.lat_med)) and (s.lat_med >= args.lat_mult_knee * baseline_lat)
            if sat_bad or lat_bad:
                high_cands.append(s)
        if high_cands:
            steady_high = min(high_cands, key=lambda x: x.u_cmd)

    print("=== Suggested operating points ===")
    if steady_low:
        print(f"steady_low:  u_cmd={fmt(steady_low.u_cmd,0)}  sat={fmt(steady_low.sat_med,3)}  lat={fmt(steady_low.lat_med,4)}s")
    else:
        print("steady_low:  not found (try lowering sat-low or check data quality)")
    if steady_high:
        print(f"steady_high: u_cmd={fmt(steady_high.u_cmd,0)}  sat={fmt(steady_high.sat_med,3)}  lat={fmt(steady_high.lat_med,4)}s")
    else:
        print("steady_high: not found (try increasing run range or lowering thresholds)")
    print()

    # optionally write per-segment csv
    if args.out_segments_csv:
        with open(args.out_segments_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["idx","u_cmd","dur_s","n","u_ach_med","sat_med","lat_med_s","lat_p95_s","err_med","inflight_max"])
            for s in segs:
                dur = s.t_end - s.t_start
                w.writerow([
                    s.idx, int(round(s.u_cmd)), f"{dur:.3f}", s.n,
                    f"{s.u_ach_med:.6f}" if not math.isnan(s.u_ach_med) else "",
                    f"{s.sat_med:.6f}" if not math.isnan(s.sat_med) else "",
                    f"{s.lat_med:.9f}" if not math.isnan(s.lat_med) else "",
                    f"{s.lat_p95:.9f}" if not math.isnan(s.lat_p95) else "",
                    f"{s.err_med:.6f}" if not math.isnan(s.err_med) else "",
                    f"{s.inflight_max:.3f}" if not math.isnan(s.inflight_max) else "",
                ])
        print(f"Wrote segment summary CSV: {args.out_segments_csv}")

if __name__ == "__main__":
    main()
