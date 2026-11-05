#!/usr/bin/env python3
"""Size/power of the V_G bootstrap test (notes/open_questions/views_across_records/VG_TEST_VALIDATION.md)."""
import math, itertools, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import norm, rankdata
sp = importlib.util.spec_from_file_location("gp", Path(__file__).with_name("gaussian_poland.py")); gp = importlib.util.module_from_spec(sp); sp.loader.exec_module(gp)


def ar1(n, phi, rng, m=1):
    x = np.empty((n, m)); x[0] = rng.standard_normal(m)
    for t in range(1, n): x[t] = phi*x[t-1] + math.sqrt(1-phi**2)*rng.standard_normal(m)
    return x


def world(name, n, phi, rng):
    if name in ("W1", "W4", "W4ns"):
        S = ar1(n, phi, rng, 3); AB, BC, CA = S.T
        if name == "W1": return np.column_stack([AB+CA, AB+BC, BC+CA]) / math.sqrt(2)
        sp_ = lambda s: 10.0*(s > 2.5)
        Y = np.column_stack([sp_(AB)+sp_(CA), sp_(AB)+sp_(BC), sp_(BC)+sp_(CA)]) + 1e-6*rng.standard_normal((n, 3))
        if name == "W4ns": Y = norm.ppf((np.apply_along_axis(rankdata, 0, Y) - 0.5)/n)
        return Y
    k = 10
    if name == "W3":
        S = ar1(n, phi, rng, k)          # S[:, i] = source between i and i+1
        return np.column_stack([(S[:, (i-1) % k] + S[:, i]) / math.sqrt(2) for i in range(k)])
    pairs = list(itertools.combinations(range(k), 2)); S = ar1(n, phi, rng, len(pairs)); Y = np.zeros((n, k))
    for p, (i, j) in enumerate(pairs): Y[:, i] += S[:, p]; Y[:, j] += S[:, p]
    Y /= 3.0
    if name.startswith("P"):
        lam2 = {"P1": 0.05, "P2": 0.10}[name]; F = ar1(n, phi, rng, 1)
        Y = math.sqrt(1-lam2)*Y + math.sqrt(lam2)*F
    return Y


def detrend(Y):
    t = np.arange(len(Y), dtype=float); A = np.column_stack([np.ones_like(t), t])
    b, *_ = np.linalg.lstsq(A, Y, rcond=None); return Y - A @ b


def reject(Y, nb, vg, rng):
    E = detrend(Y); n = len(E); b = 3; nbl = math.ceil(n/b); vals = []
    for _ in range(nb):
        st = rng.integers(0, n-b+1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        vals.append(vg(np.corrcoef(E[idx].T)))
    return np.percentile(vals, 5) > 0


def main():
    rng = np.random.default_rng(5)
    print(f"{'world':6s} {'n':>3s} {'phi':>5s} {'rate':>6s}")
    for name in ("W1", "W4", "W4ns", "W2", "W3", "P1", "P2"):
        k = 3 if name in ("W1", "W4", "W4ns") else 10
        nsim, nb = (300, 1000) if k == 3 else (100, 300)
        vg = gp.FastVG(k)
        for n in (30, 53):
            for phi in (-0.5, 0.5):
                r = np.mean([reject(world(name, n, phi, rng), nb, vg, rng) for _ in range(nsim)])
                print(f"{name:6s} {n:3d} {phi:+5.1f} {r:6.2f}", flush=True)


if __name__ == "__main__":
    main()
