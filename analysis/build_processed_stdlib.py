#!/usr/bin/env python3
import argparse, csv, sys
from typing import Dict, List, Optional

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
    ap.add_argument("out_csv")
    ap.add_argument("--drop-missing-lat", action="store_true", help="drop rows where lat_p99 is missing")
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

        if col_t is None or col_u is None or col_sent is None:
            print("ERROR: need t_sec, u_cmd, sent_total (or aliases) in raw", file=sys.stderr)
            sys.exit(2)

        rows_out: List[Dict[str, str]] = []
        prev_t: Optional[float] = None
        prev_sent: Optional[int] = None

        for row in r:
            t = ffloat(row.get(col_t, ""))
            u_cmd = ffloat(row.get(col_u, ""))
            sent_total = fint(row.get(col_sent, ""))

            if t is None or u_cmd is None or sent_total is None:
                continue

            lat = ffloat(row.get(col_lat, "")) if col_lat else None
            if args.drop_missing_lat and lat is None:
                # allow skip if you want strict KPI availability
                continue

            u_ach = ffloat(row.get(col_uach, "")) if col_uach else None
            if u_ach is None and prev_t is not None and prev_sent is not None:
                dt = t - prev_t
                ds = sent_total - prev_sent
                if dt > 0 and ds >= 0:
                    u_ach = ds / dt

            # strict processed requires all four
            if u_ach is None or lat is None:
                prev_t, prev_sent = t, sent_total
                continue

            rows_out.append({
                "t_sec": f"{t:.6f}",
                "u_cmd": f"{u_cmd:.6f}",
                "u_ach": f"{u_ach:.6f}",
                "lat_p99": f"{lat:.9f}",
            })

            prev_t, prev_sent = t, sent_total

    with open(args.out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["t_sec", "u_cmd", "u_ach", "lat_p99"])
        w.writeheader()
        for row in rows_out:
            w.writerow(row)

    print(f"Wrote processed rows: {len(rows_out)} -> {args.out_csv}")

if __name__ == "__main__":
    main()
