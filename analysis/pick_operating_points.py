#!/usr/bin/env python3
import argparse, csv, math, statistics
from typing import List, Optional, Dict

ALIASES = {
    "u_cmd": ["u_cmd", "lam_cmd", "lambda", "rate"],
    "t_sec": ["t_sec", "t", "time_sec"],
    "sent_total": ["sent_total", "sent", "total_sent"],
    "u_ach": ["u_ach", "u_ach(sent_calc)", "ach", "throughput"],
    "lat_p99": ["lat_p99", "p99", "latency_p99", "tx_lat_p99"],
}

def pick_col(header: List[str], keys: List[str]) -> Optional[str]:
    exact = {h.strip(): h.strip() for h in header}
    for k in keys:
        if k in exact:
            return k
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
    ap.add_argument("--sat-low", type=float, default=0.95, help="saturation threshold for LOW region")
    ap.add_argument("--sat-high", type=float, default=0.80, help="saturation threshold for HIGH region")
    ap.add_argument("--min-lat", type=float, default=1e-6, help="ignore lat_p99 below this (missing/zero)")
    args = ap.parse_args()

    with open(args.raw_csv, "r", newline="") as f:
        r = csv.DictReader(f)
        if r.fieldnames is None:
            raise SystemExit("No header")

        col_u = pick_col(r.fieldnames, ALIASES["u_cmd"])
        col_sent = pick_col(r.fieldnames, ALIASES["sent_total"])
        col_uach = pick_col(r.fieldnames, ALIASES["u_ach"])
        col_lat = pick_col(r.fieldnames, ALIASES["lat_p99"])

        if col_u is None or (col_uach is None and col_sent is None):
            raise SystemExit("Need u_cmd and (u_ach or sent_total) in raw CSV.")
        if col_lat is None:
            raise SystemExit("Need lat_p99 in raw CSV (or alias).")

        rows = []
        prev_sent = None
        prev_t = None

        # We try to compute u_ach from sent_total if u_ach missing
        col_t = pick_col(r.fieldnames, ALIASES["t_sec"])

        for row in r:
            u = ffloat(row.get(col_u, ""))
            lat = ffloat(row.get(col_lat, ""))
            if u is None or lat is None or lat < args.min_lat:
                continue

            u_ach = ffloat(row.get(col_uach, "")) if col_uach else None

            if u_ach is None and col_sent and col_t:
                t = ffloat(row.get(col_t, ""))
                sent = fint(row.get(col_sent, ""))
                if t is not None and sent is not None and prev_sent is not None and prev_t is not None:
                    dt = t - prev_t
                    ds = sent - prev_sent
                    if dt > 0 and ds >= 0:
                        u_ach = ds / dt
                if t is not None and sent is not None:
                    prev_t, prev_sent = t, sent

            if u_ach is None or u <= 0:
                continue

            sat = u_ach / u
            rows.append((u, u_ach, sat, lat))

        if len(rows) < 10:
            raise SystemExit(f"Too few valid rows after filtering: {len(rows)}")

        # Aggregate by u_cmd level (median per level)
        by_u: Dict[float, List[tuple]] = {}
        for u, uach, sat, lat in rows:
            by_u.setdefault(u, []).append((uach, sat, lat))

        levels = sorted(by_u.keys())
        agg = []
        for u in levels:
            uachs = [x[0] for x in by_u[u]]
            sats  = [x[1] for x in by_u[u]]
            lats  = [x[2] for x in by_u[u]]
            agg.append((u, statistics.median(uachs), statistics.median(sats), statistics.median(lats)))

        # LOW: highest u where sat >= sat_low
        low_candidates = [a for a in agg if a[2] >= args.sat_low]
        low = max(low_candidates, key=lambda x: x[0], default=None)

        # HIGH: lowest u where sat <= sat_high
        high_candidates = [a for a in agg if a[2] <= args.sat_high]
        high = min(high_candidates, key=lambda x: x[0], default=None)

        # Knee estimate (simple): first u where sat drops below 0.95 (or median sat drops fastest)
        knee = None
        for a in agg:
            if a[2] < args.sat_low:
                knee = a
                break

        print("Operating point suggestions (from knee CSV):")
        if knee:
            print(f"  knee_estimate: u_cmd≈{knee[0]:.3f}  sat≈{knee[2]:.3f}  lat_p99≈{knee[3]:.6f}s")
        else:
            print("  knee_estimate: not found (saturation never dropped below sat_low)")

        if low:
            print(f"  steady_low:    u_cmd={low[0]:.3f}  sat≈{low[2]:.3f}  lat_p99≈{low[3]:.6f}s")
        else:
            print("  steady_low:    not found (no levels with saturation >= sat_low)")

        if high:
            print(f"  steady_high:   u_cmd={high[0]:.3f}  sat≈{high[2]:.3f}  lat_p99≈{high[3]:.6f}s")
        else:
            print("  steady_high:   not found (no levels with saturation <= sat_high)")

if __name__ == "__main__":
    main()
