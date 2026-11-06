#!/usr/bin/env python3
"""Finite-sample size of the eps=inf reach test at m=3 (REACH_TEST_VALIDITY.md)."""
import math, importlib.util
from pathlib import Path
import numpy as np
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
sr = mod("sr", "source_reach_poland.py"); pv = sr.pv


def boundary_R(k=10, m=3, rng=np.random.default_rng(0)):
    L = np.zeros((k, k))
    for j in range(k):
        for d in range(m): L[(j + d) % k, j] = rng.uniform(0.5, 1.0)
    C = L @ L.T; dd = np.sqrt(np.diag(C)); R = C / np.outer(dd, dd)
    sol = sr.VmSolver(k, m); lo, hi = 0.0, 5.0                     # V_m(I+s(R-I)) increasing in s for s >= 0
    for _ in range(40):
        s = (lo + hi) / 2; v = sol(np.eye(k) + s * (R - np.eye(k)))
        lo, hi = (s, hi) if v < 0 else (lo, s)
    Rs = np.eye(k) + lo * (R - np.eye(k)); return Rs, sol(Rs)


def sim(Rs, n, phi, rng):
    k = len(Rs); Lc = np.linalg.cholesky(Rs + 1e-10 * np.eye(k)); eps = rng.standard_normal((n + 50, k)) @ Lc.T
    X = np.empty_like(eps); X[0] = eps[0]
    for t in range(1, n + 50): X[t] = phi * X[t-1] + math.sqrt(1 - phi**2) * eps[t]
    return X[50:]


def main():
    rng = np.random.default_rng(12); Rs, v = boundary_R(); k = len(Rs); print(f"boundary world: V_3 = {v:+.2e}, V_2 = {sr.VmSolver(k,2)(Rs):+.3f}")
    sol = sr.VmSolver(k, 3); I = np.eye(k); n = 53; t = np.arange(n, dtype=float); b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b)
    for phi in (0.0, 0.5):
        rej = 0
        for s in range(100):
            Y = sim(Rs, n, phi, rng); R = np.corrcoef(pv.prep(Y, [t]).T); T = math.sqrt(n) * sol(R); D = []
            for _ in range(300):
                st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
                Z = math.sqrt(n) * (np.corrcoef(pv.prep(Y[idx], [t[idx]]).T) - R); D.append(sol(I + Z - np.diag(np.diag(Z))) + 1)
            rej += T > np.percentile(D, 95)
        print(f"phi={phi}: size of H0(3) test = {rej/100:.2f}", flush=True)


if __name__ == "__main__":
    main()
