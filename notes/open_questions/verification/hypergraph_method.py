#!/usr/bin/env python3
"""Step 3 validation (HYPERGRAPH_METHOD.md): V_H test on H(2) = pairs + consecutive ring triples."""
import math, itertools, sys
import numpy as np
import cvxpy as cp
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
K = 10


class VH:
    def __init__(self, H, k=K):
        self.P = cp.Parameter((k, k), symmetric=True); X = cp.Variable((k, k), symmetric=True)
        cons = [cp.trace(X) == 1] + [cp.diag(X) >= 0] + [X[np.ix_(list(S), list(S))] >> 0 for S in H if len(S) > 1]
        self.prob = cp.Problem(cp.Maximize(-cp.trace(X @ self.P)), cons)
    def __call__(self, R):
        self.P.value = (R + R.T) / 2; self.prob.solve(solver="CLARABEL"); return float(self.prob.value)


PAIRS = list(itertools.combinations(range(K), 2))
TRIPLES = [tuple(sorted({i, (i + 1) % K, (i + 2) % K})) for i in range(K)]
H2 = PAIRS + TRIPLES


def triple_R(rng, noise=0.0):
    L = np.zeros((K, K))
    for j, S in enumerate(TRIPLES):
        for i in S: L[i, j] = rng.uniform(0.5, 1.0)
    C = L @ L.T + noise * np.eye(K); d = np.sqrt(np.diag(C)); return C / np.outer(d, d)


def scale_to(R, f, target=0.0):
    lo, hi = 0.0, 1.0
    if f(np.eye(K) + hi * (R - np.eye(K))) < target:
        while f(np.eye(K) + hi * (R - np.eye(K))) < target and hi < 5: hi *= 1.5
    for _ in range(35):
        s = (lo + hi) / 2; v = f(np.eye(K) + s * (R - np.eye(K))); lo, hi = (s, hi) if v < target else (lo, s)
    return np.eye(K) + lo * (R - np.eye(K))


def simulate(R, n, rng): return rng.standard_normal((n, K)) @ np.linalg.cholesky(R + 1e-10 * np.eye(K)).T
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def test(Y, f, rng, NB=200):
    n = len(Y); R = spear(Y); T = math.sqrt(n) * f(R)
    b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, Y))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
    D = []
    for _ in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (spear(Y[idx]) - R); np.fill_diagonal(Z, 0); D.append(f(np.eye(K) + Z) + 1)
    return T > np.percentile(D, 95)


def main():
    rng = np.random.default_rng(20); f2 = VH(H2); fp = VH(PAIRS)
    Rbase = triple_R(np.random.default_rng(0))
    Rb = scale_to(Rbase, f2); print(f"size world: V_H2 = {f2(Rb):+.2e}, V_2 = {fp(Rb):+.3f}")
    Rpoly = scale_to(Rbase, f2, target=-0.15); vpoly2 = fp(Rpoly)
    # mono: one factor on all sites, lam2 chosen so V_2 matches Poly
    def mono(l2): M = l2 * np.ones((K, K)) + (1 - l2) * np.eye(K); return M
    lo, hi = 0.0, 0.99
    for _ in range(40):
        mid = (lo + hi) / 2; lo, hi = (mid, hi) if fp(mono(mid)) < vpoly2 else (lo, mid)
    Rmono = mono(lo)
    print(f"Poly: V_2 = {vpoly2:+.3f}, V_H2 = {f2(Rpoly):+.3f} | Mono: V_2 = {fp(Rmono):+.3f}, V_H2 = {f2(Rmono):+.3f}, lambda2 = {lo:.3f}", flush=True)
    for name, R in (("size (H2 boundary)", Rb), ("Poly", Rpoly), ("Mono", Rmono)):
        r = np.mean([test(simulate(R, 53, rng), f2, rng) for _ in range(50)])
        print(f"{name}: rejection of H(2) = {r:.2f}", flush=True)


if __name__ == "__main__":
    main()
