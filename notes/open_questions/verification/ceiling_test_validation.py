#!/usr/bin/env python3
"""Size/power simulation for the ceiling test (notes/open_questions/views_across_records/CEILING_TEST_VALIDATION.md)."""
import importlib.util, math
from pathlib import Path
import numpy as np
from scipy.stats import norm
sp = importlib.util.spec_from_file_location("m", Path(__file__).with_name("mast_ceiling_gate.py"))
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
NSIM, NB = 400, 1000


def ar1(n, phi, rng):
    x = np.empty(n); x[0] = rng.standard_normal()
    for t in range(1, n): x[t] = phi * x[t-1] + math.sqrt(1 - phi**2) * rng.standard_normal()
    return x


def world(n, phi, probs, rho, rng):
    S = [ar1(n, phi, rng) > norm.ppf(1 - p) for p in probs]          # AB, BC, CA good-years
    A = S[0] & S[2]; B = S[0] & S[1]; C = S[1] & S[2]
    X = np.column_stack([A, B, C]).astype(float) + 1e-6 * rng.standard_normal((n, 3))   # break median ties
    if rho > 0:
        cm = rng.random(n) < rho; coin = (rng.random(n) < 0.5).astype(float)
        X[cm] = coin[cm, None] + 1e-6 * rng.standard_normal((cm.sum(), 3))
    return X


def reject(X, b, rng):
    n = len(X); nb = math.ceil(n / b)
    starts = rng.integers(0, n - b + 1, (NB, nb))                        # no wrap-around
    idx = (starts[:, :, None] + np.arange(b)).reshape(NB, -1)[:, :n]
    Vb, _ = m.V16(X[idx])
    return np.percentile(Vb, 5) > 0


def main():
    rng = np.random.default_rng(1)
    sym = (2**-0.5,) * 3; asym = (0.62, 0.71, 0.80)
    print("rejection rates (400 sims each); size worlds should be <= 0.05")
    print(f"{'world':22s} {'n':>3s} {'phi':>5s} " + " ".join(f"b={b}" for b in (1, 3, 5)))
    cells = [("size: AND symmetric", sym, 0), ("size: asymmetric", asym, 0)] + [(f"power: rho={r}", sym, r) for r in (0.1, 0.2, 0.3, 0.5)]
    for name, probs, rho in cells:
        for n in (45, 72):
            for phi in (-0.5, 0.0, 0.5):
                rates = []
                for b in (1, 3, 5):
                    rates.append(np.mean([reject(world(n, phi, probs, rho, rng), b, rng) for _ in range(NSIM)]))
                print(f"{name:22s} {n:3d} {phi:+5.1f} " + " ".join(f"{r:4.2f}" for r in rates), flush=True)


if __name__ == "__main__":
    main()
