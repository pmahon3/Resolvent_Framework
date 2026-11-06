#!/usr/bin/env python3
"""V2 (REACH_TEST_SPEARMAN.md): finite-sample size of the Spearman eps=inf test, no detrending. m=2 grid + m=3 ring-of-triples."""
import math, sys, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import rankdata
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
nd = mod("nd", "vg_numdelta.py"); r3 = mod("r3", "reach_m3_validation.py")


def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def test(Y, stat, rng, NB):
    n = len(Y); R = spear(Y); T = math.sqrt(n) * stat(R)
    b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b); D = np.empty(NB)
    for s in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (spear(Y[idx]) - R); np.fill_diagonal(Z, 0); D[s] = stat(np.eye(len(R)) + Z) + 1
    return T > np.percentile(D, 95)


def main(part):
    rng = np.random.default_rng(14)
    if part == "m2":
        stat = lambda R: nd.rho(np.abs(R - np.eye(len(R)))) - 1
        for w in ("W1", "W4", "W2", "W3", "WD"):
            for n in (30, 53):
                for phi in (-0.5, 0.5):
                    r = np.mean([test(nd.world(w, n, phi, rng), stat, rng, 1000) for _ in range(300)])
                    print(f"m=2 {w:3s} n={n} phi={phi:+.1f} size={r:.2f}", flush=True)
    else:
        Rs, v = r3.boundary_R(); sol = r3.sr.VmSolver(len(Rs), 3)
        for phi in (0.0, 0.5):
            r = np.mean([test(r3.sim(Rs, 53, phi, rng), sol, rng, 300) for _ in range(100)])
            print(f"m=3 ring-of-triples n=53 phi={phi} size={r:.2f}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
