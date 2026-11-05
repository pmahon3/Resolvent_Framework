#!/usr/bin/env python3
"""Run 4: Hong-Li numerical delta test for V_G (VG_TEST_VALIDATION.md; recipe VG_INFERENCE_METHODS.md)."""
import math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import norm, rankdata
sp = importlib.util.spec_from_file_location("v", Path(__file__).with_name("vg_test_validation.py")); v = importlib.util.module_from_spec(sp); sp.loader.exec_module(v)


def rho(A): return float(np.max(np.abs(np.linalg.eigvalsh(A))))


def prep(Y, t):
    n = len(Y); Z = norm.ppf((np.apply_along_axis(rankdata, 0, Y) - 0.5) / n)
    X = np.column_stack([np.ones(n), t]); b, *_ = np.linalg.lstsq(X, Z, rcond=None); return Z - X @ b


def numdelta(Y, rng, NB=1000):
    n, k = Y.shape; t = np.arange(n, dtype=float); I = np.eye(k)
    R = np.corrcoef(prep(Y, t).T); r0 = rho(np.abs(R - I)); T = math.sqrt(n) * (r0 - 1)
    b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b)
    eps = {"1/sqrt n": 1/math.sqrt(n), "sqrt(ln n/n)": math.sqrt(math.log(n)/n), "n^-1/6": n ** (-1/6)}
    D = {e: [] for e in list(eps) + ["inf"]}
    for _ in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Rs = np.corrcoef(prep(Y[idx], t[idx]).T); Z = math.sqrt(n) * (Rs - R)
        for name, e in eps.items(): D[name].append((rho(np.abs(R + e*Z - I)) - r0) / e)
        D["inf"].append(rho(np.abs(Z - np.diag(np.diag(Z)))))
    return {name: T > np.percentile(vals, 95) for name, vals in D.items()}


def world(name, n, phi, rng):
    if name == "W0": return v.ar1(n, phi, rng, 10)
    if name == "WD":
        S = v.ar1(n, phi, rng, 10); cols = []
        for base in (0, 5):
            for i in range(5): cols.append((S[:, base + (i-1) % 5] + S[:, base + i]) / math.sqrt(2))
        return np.column_stack(cols)
    return v.world(name, n, phi, rng)


def main():
    rng = np.random.default_rng(7); names = ["1/sqrt n", "sqrt(ln n/n)", "n^-1/6", "inf"]
    print(f"{'world':6s} {'n':>3s} {'phi':>5s} " + " ".join(f"{x:>13s}" for x in names))
    for w in ("W1", "W4", "W2", "W3", "WD", "W0", "P1", "P2"):
        for n in (30, 53):
            for phi in (-0.5, 0.5):
                res = [numdelta(world(w, n, phi, rng), rng) for _ in range(300)]
                print(f"{w:6s} {n:3d} {phi:+5.1f} " + " ".join(f"{np.mean([r[x] for r in res]):13.2f}" for x in names), flush=True)


if __name__ == "__main__":
    main()
