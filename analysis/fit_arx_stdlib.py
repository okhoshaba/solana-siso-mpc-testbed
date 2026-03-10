#!/usr/bin/env python3
"""
fit_arx_stdlib.py — ARX identification WITHOUT pandas/numpy.

- Reads a CSV produced by arx_dataset_* (or any CSV with numeric columns for u and y).
- Fits an ARX(na, nb, nk) model via least squares using normal equations + Gaussian elimination.

Model:
  y[k] + a1 y[k-1] + ... + a_na y[k-na] = b1 u[k-nk] + ... + b_nb u[k-nk-nb+1] + e[k]

It writes a JSON model file (default: arx_model.json).

Usage examples:
  python3 fit_arx_stdlib.py arx_dataset_knee_2026-02-01.csv --na 2 --nb 2 --nk 1
  python3 fit_arx_stdlib.py arx_dataset_knee_2026-02-01.csv --u_col u_ach_from_total --y_col y_lat_p99_sec
"""

from __future__ import annotations
import argparse
import csv
import json
import math
from typing import List, Tuple, Optional


def is_nan(x: float) -> bool:
    return isinstance(x, float) and math.isnan(x)


def parse_float(s: str) -> float:
    s = (s or "").strip()
    if s == "" or s.lower() == "nan":
        return float("nan")
    try:
        return float(s)
    except Exception:
        return float("nan")


def read_xy(csv_path: str, u_col: str, y_col: str) -> Tuple[List[float], List[float]]:
    with open(csv_path, "r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise SystemExit("CSV has no header row. Expected header with column names.")
        missing = [c for c in (u_col, y_col) if c not in reader.fieldnames]
        if missing:
            raise SystemExit(f"CSV missing columns: {missing}. Available: {reader.fieldnames}")

        u: List[float] = []
        y: List[float] = []
        for row in reader:
            uu = parse_float(row.get(u_col, ""))
            yy = parse_float(row.get(y_col, ""))
            if is_nan(uu) or is_nan(yy) or math.isinf(uu) or math.isinf(yy):
                continue
            u.append(uu)
            y.append(yy)

    if len(u) != len(y) or len(u) == 0:
        raise SystemExit("No valid (u,y) samples after cleaning.")
    return u, y


def mat_zero(n: int, m: int) -> List[List[float]]:
    return [[0.0 for _ in range(m)] for _ in range(n)]


def solve_linear(A: List[List[float]], b: List[float], ridge: float = 0.0) -> List[float]:
    """
    Solve A x = b via Gaussian elimination with partial pivoting.
    A is modified in-place.
    """
    n = len(A)
    # optional ridge to stabilize
    if ridge and ridge > 0.0:
        for i in range(n):
            A[i][i] += ridge

    # Build augmented matrix
    aug = [A[i][:] + [b[i]] for i in range(n)]

    # Forward elimination
    for col in range(n):
        # Pivot
        pivot_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot_row][col]) < 1e-18:
            raise SystemExit("Singular/ill-conditioned normal equations. Try --ridge 1e-8 or reduce orders.")
        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        # Normalize pivot row
        piv = aug[col][col]
        inv = 1.0 / piv
        for j in range(col, n + 1):
            aug[col][j] *= inv

        # Eliminate below
        for r in range(col + 1, n):
            factor = aug[r][col]
            if factor == 0.0:
                continue
            for j in range(col, n + 1):
                aug[r][j] -= factor * aug[col][j]

    # Back substitution
    x = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        s = aug[i][n]  # RHS
        for j in range(i + 1, n):
            s -= aug[i][j] * x[j]
        x[i] = s  # pivot is 1.0 after normalization
    return x


def fit_arx(u: List[float], y: List[float], na: int, nb: int, nk: int, ridge: float = 1e-10):
    if nb < 1:
        raise SystemExit("nb must be >= 1")
    if na < 0 or nb < 0 or nk < 0:
        raise SystemExit("na, nb, nk must be >= 0")

    N = len(y)
    maxlag = max(na, nk + nb - 1)
    if N <= maxlag + 5:
        raise SystemExit(f"Not enough samples: N={N}, need > {maxlag+5}")

    m = na + nb  # number of regressors
    # Normal equations: (X^T X) theta = X^T Y
    XtX = mat_zero(m, m)
    XtY = [0.0 for _ in range(m)]

    used = 0
    se = 0.0

    for k in range(maxlag, N):
        phi: List[float] = []
        for i in range(1, na + 1):
            phi.append(-y[k - i])
        for j in range(nb):
            phi.append(u[k - nk - j])
        Yk = y[k]

        # accumulate normal equations
        for i in range(m):
            XtY[i] += phi[i] * Yk
            for j in range(m):
                XtX[i][j] += phi[i] * phi[j]
        used += 1

    theta = solve_linear(XtX, XtY, ridge=ridge)

    # compute RMSE on same data (in-sample)
    for k in range(maxlag, N):
        phi = []
        for i in range(1, na + 1):
            phi.append(-y[k - i])
        for j in range(nb):
            phi.append(u[k - nk - j])
        yhat = sum(phi[i] * theta[i] for i in range(m))
        err = y[k] - yhat
        se += err * err

    rmse = math.sqrt(se / max(1, used))
    a = theta[:na]
    b = theta[na:]
    return a, b, rmse, used, maxlag


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", help="input dataset csv (must have header row)")
    ap.add_argument("--na", type=int, default=2)
    ap.add_argument("--nb", type=int, default=2)
    ap.add_argument("--nk", type=int, default=1)
    ap.add_argument("--u_col", default="sent_per_sec_reported", help="input column name (u)")
    ap.add_argument("--y_col", default="y_lat_p99_sec", help="output column name (y)")
    ap.add_argument("--ridge", type=float, default=1e-10, help="ridge added to normal equations diagonal")
    ap.add_argument("--out_model", default="arx_model.json", help="output JSON model path")
    args = ap.parse_args()

    u, y = read_xy(args.csv, args.u_col, args.y_col)
    a, b, rmse, used, maxlag = fit_arx(u=u, y=y, na=args.na, nb=args.nb, nk=args.nk, ridge=args.ridge)

    model = {
        "na": args.na,
        "nb": args.nb,
        "nk": args.nk,
        "u_col": args.u_col,
        "y_col": args.y_col,
        "ridge": args.ridge,
        "rmse_sec": rmse,
        "a": a,
        "b": b,
        "n_used": used,
        "maxlag": maxlag,
    }

    print("ARX fit OK (stdlib)")
    print(f"  N_used = {used}")
    print(f"  na={args.na} nb={args.nb} nk={args.nk}")
    print(f"  RMSE = {rmse:.6f} s")
    print("  a =", a)
    print("  b =", b)

    with open(args.out_model, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2)
    print(f"Saved model -> {args.out_model}")


if __name__ == "__main__":
    main()
