#!/usr/bin/env python3
import argparse, csv, math, statistics, sys
from typing import Dict, List, Optional, Tuple

ALIASES = {
    "u_cmd": ["u_cmd", "lam_cmd", "lambda", "rate"],
    "t_sec": ["t_sec", "t", "time_sec"],
    "sent_total": ["sent_total", "sent", "total_sent"],
    "u_ach": ["u_ach", "u_ach(sent_calc)", "ach", "throughput"],
    "lat_p99": ["lat_p99", "p99", "latency_p99", "tx_lat_p99"],
}

def pick_col(header: List[str], keys: List[str]) -> Optional[str]:
    hset = {h.strip(): h.strip() for h in header}
    for k in keys:
        if k in hset:
            return k
    # case-insensitive match
    lower = {h.strip().lower(): h.strip() for h in header}
    for k in keys:
        if k.lower() in lower:
            return lower[k.lower()]
    return None

def ffloat(x: str) -> Optional[float]:
    x = (x or "").strip()
    if not x:
        return None
    try:
        return float(x)
    except:
        return None

def fint(x: str) -> Optional[int]:
    x = (x or "").strip()
    if not x:
        return None
    try:
        return int(float(x))
    except:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw_csv")
    args = ap.parse_args()

    with open(args.raw_csv, "r", newline="") as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            print("ERROR: no header", file=sys.stderr)
            sys.exit(2)

        col_t = pick_col(r.fieldnames, ALIASES["t_sec"])
        col_u = pick_col(r.fieldnames, ALIASES["u_cmd"])
        col_sent = pick_col(r.fieldnames, ALIASES["sent_total"])
        col_uach = pick_col(r.fieldnames, ALIASES["u_ach"])
        col_lat = pick_col(r.fieldnames, ALIASES["lat_p99"])

        print("Detected columns:")
        print(f"  t_sec:      {col_t}")
        print(f"  u_cmd:      {col_u}")
        print(f"  sent_total: {col_sent}")
        print(f"  u_ach:      {col_uach}")
        print(f"  lat_p99:    {col_lat}")
        print()

        if col_t is None or col_u is None or col_sent is None:
            print("ERROR: raw must contain at least t_sec, u_cmd, sent_total (or aliases).", file=sys.stderr)
            sys.exit(2)

        t: List[float] = []
        u: List[float] = []
        sent: List[int] = []
        uach: List[Optional[float]] = []
        lat: List[Optional[float]] = []

        for row in r:
            tv = ffloat(row.get(col_t, ""))
            uv = ffloat(row.get(col_u, ""))
            sv = fint(row.get(col_sent, ""))
            if tv is None or uv is None or sv is None:
                continue
            t.append(tv); u.append(uv); sent.append(sv)
            uach.append(ffloat(row.get(col_uach, "")) if col_uach else None)
            lat.append(ffloat(row.get(col_lat, "")) if col_lat else None)

        n = len(t)
        print(f"Rows parsed: {n}")
        if n < 5:
            print("ERROR: too few rows", file=sys.stderr)
            sys.exit(2)

        # dt stats
        dts = [t[i]-t[i-1] for i in range(1, n) if t[i] > t[i-1]]
        if dts:
            print(f"dt median: {statistics.median(dts):.3f}s, mean: {statistics.mean(dts):.3f}s, min: {min(dts):.3f}s, max: {max(dts):.3f}s")
        else:
            print("dt: cannot compute (non-increasing t_sec?)")

        # monotonic sent_total
        bad = sum(1 for i in range(1, n) if sent[i] < sent[i-1])
        print(f"sent_total monotonic violations: {bad}")

        # missing stats
        miss_uach = sum(1 for x in uach if x is None)
        miss_lat = sum(1 for x in lat if x is None)
        print(f"missing u_ach: {miss_uach}/{n}")
        print(f"missing lat_p99: {miss_lat}/{n}")

        # ranges
        print(f"u_cmd range: {min(u):.3f} .. {max(u):.3f} tx/s")
        # compute u_ach if available
        uach_vals = [x for x in uach if x is not None]
        if uach_vals:
            print(f"u_ach range (reported): {min(uach_vals):.3f} .. {max(uach_vals):.3f} tx/s")
            # saturation
            sat = [ (uach[i]/u[i]) for i in range(n) if uach[i] is not None and u[i] > 0 ]
            if sat:
                print(f"saturation u_ach/u_cmd: median={statistics.median(sat):.3f}, min={min(sat):.3f}, max={max(sat):.3f}")
        lat_vals = [x for x in lat if x is not None]
        if lat_vals:
            print(f"lat_p99 range: {min(lat_vals):.6f} .. {max(lat_vals):.6f} s")
        print("\nQC done.")

if __name__ == "__main__":
    main()
