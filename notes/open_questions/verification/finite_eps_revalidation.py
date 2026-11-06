#!/usr/bin/env python3
"""Finite-eps Hong-Li with Politis-White blocks (FINITE_EPS_REVALIDATION.md)."""
import math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
sp = importlib.util.spec_from_file_location("nd", Path(__file__).with_name("vg_numdelta.py")); nd = importlib.util.module_from_spec(sp); sp.loader.exec_module(nd)


def rho(A): return float(np.max(np.abs(np.linalg.eigvalsh(A))))
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def test(Y, rng, NB=1000):
    n, k = Y.shape; I = np.eye(k); R = spear(Y); r0 = rho(np.abs(R - I)); T = math.sqrt(n) * (r0 - 1)
    b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, Y))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
    eps = {"sqrt(ln n/n)": math.sqrt(math.log(n) / n), "n^-1/6": n ** (-1/6)}; D = {e: [] for e in list(eps) + ["inf"]}
    for _ in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (spear(Y[idx]) - R); np.fill_diagonal(Z, 0)
        for name, e in eps.items(): D[name].append((rho(np.abs(R + e * Z - I)) - r0) / e)
        D["inf"].append(rho(np.abs(Z)))
    return {k_: T > np.percentile(v, 95) for k_, v in D.items()}


def main():
    rng = np.random.default_rng(22); names = ["sqrt(ln n/n)", "n^-1/6", "inf"]
    print(f"{'world':5s} {'n':>3s} {'phi':>5s} " + " ".join(f"{x:>13s}" for x in names))
    cells = [(w, n, phi) for w in ("W1", "W2", "W3", "WD") for n in (30, 53) for phi in (-0.5, 0.5)] + [(w, 53, phi) for w in ("P1", "P2") for phi in (-0.5, 0.5)]
    for w, n, phi in cells:
        res = [test(nd.world(w, n, phi, rng), rng) for _ in range(300)]
        print(f"{w:5s} {n:3d} {phi:+5.1f} " + " ".join(f"{np.mean([r[x] for r in res]):13.2f}" for x in names), flush=True)


if __name__ == "__main__":
    main()
