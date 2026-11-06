#!/usr/bin/env python3
"""Assumption breakers (ASSUMPTION_BREAKERS.md)."""
import math
import numpy as np
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
K = 10


def rho(M): return float(np.max(np.abs(np.linalg.eigvalsh(M))))
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def ar1(n, phi, rng, m):
    x = np.empty((n, m)); x[0] = rng.standard_normal(m)
    for t in range(1, n): x[t] = phi * x[t-1] + math.sqrt(1 - phi**2) * rng.standard_normal(m)
    return x


def world(name, n, phi, rng):
    S = ar1(n, phi, rng, K); tt = np.arange(n) / n           # S[:, e] = source on edge (e, e+1)
    if name == "T": S = S + rng.normal(0, 2, K) * tt[:, None]
    if name == "S": S = S + rng.normal(0, 2, K) * (np.arange(n) > n / 2)[:, None]
    if name == "N": return np.column_stack([np.minimum(S[:, (i - 1) % K], S[:, i]) for i in range(K)])
    return np.column_stack([(S[:, (i - 1) % K] + S[:, i]) / math.sqrt(2) for i in range(K)])


def jit(Y, rng):
    J = Y.astype(float).copy()
    for j in range(Y.shape[1]):
        u = np.unique(Y[:, j]); gap = np.min(np.diff(u)) if len(u) > 1 else 1.0; J[:, j] += rng.normal(0, 1e-3 * gap, len(Y))
    return J


def detrend(Y):
    t = np.arange(len(Y), dtype=float); X = np.column_stack([np.ones_like(t), t]); b, *_ = np.linalg.lstsq(X, Y, rcond=None); return Y - X @ b


def test(Y, det, rng, NB=500):
    n = len(Y); t = np.arange(n, dtype=float)
    prep = (lambda idx: spear(detrend_on(Y[idx], t[idx]))) if det else (lambda idx: spear(Y[idx]))
    R = prep(np.arange(n)); T = math.sqrt(n) * (rho(np.abs(R - np.eye(K))) - 1)
    b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, Y))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
    D = np.empty(NB)
    for s in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (prep(idx) - R); np.fill_diagonal(Z, 0); D[s] = rho(np.abs(Z))
    return T > np.percentile(D, 95)


def detrend_on(Y, t):
    X = np.column_stack([np.ones_like(t), t]); b, *_ = np.linalg.lstsq(X, Y, rcond=None); return Y - X @ b


def main():
    rng = np.random.default_rng(17)
    for name, phis in (("C", (0.5,)), ("T", (0.5,)), ("S", (0.5,)), ("N", (-0.5, 0.5))):
        for phi in phis:
            for det in (False, True):
                r = np.mean([test(jit(world(name, 53, phi, rng), rng), det, rng) for _ in range(100)])
                print(f"world {name} phi={phi:+.1f} {'detrended' if det else 'raw      '}: rejection {r:.2f}", flush=True)


if __name__ == "__main__":
    main()
