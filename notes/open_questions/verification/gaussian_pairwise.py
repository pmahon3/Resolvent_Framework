#!/usr/bin/env python3
"""Linear-Gaussian pairwise ceiling V_G (notes/open_questions/views_across_records/GAUSSIAN_PAIRWISE_MODEL.md)."""
import itertools
import numpy as np
from scipy.optimize import minimize


def VG(R):
    k = len(R); pairs = list(itertools.combinations(range(k), 2)); a = np.array([abs(R[i, j]) for i, j in pairs]) + 1e-12
    def loads(w):
        L = np.zeros(k)
        for (i, j), ap, wp in zip(pairs, a, w):
            L[i] += ap * np.exp(wp); L[j] += ap * np.exp(-wp)
        return L
    # minimise a smooth max (log-sum-exp with large beta), then report the true max
    best = None
    for beta in (20, 80, 300):
        f = lambda w: np.log(np.sum(np.exp(beta * (loads(w) - 1)))) / beta
        x0 = np.zeros(len(pairs)) if best is None else best.x
        best = minimize(f, x0, method="L-BFGS-B")
    return float(np.max(loads(best.x)) - 1)


if __name__ == "__main__":
    for r in (0.4, 0.5, 0.6):
        R = np.full((3, 3), r); np.fill_diagonal(R, 1); print(f"equal triangle r={r}: V_G={VG(R):+.4f}")
    R = np.array([[1, .8, .1], [.8, 1, .1], [.1, .1, 1]]); print("one strong pair (.8,.1,.1):", round(VG(R), 4))
    rng = np.random.default_rng(0); k = 6; B = np.zeros((k, k))
    # random linear pairwise model -> must be feasible (V_G <= 0)
    worst = -9
    for _ in range(200):
        b = rng.normal(size=(k, k)); np.fill_diagonal(b, 0)
        tot = (b**2).sum(1, keepdims=True); b = b / np.sqrt(tot * rng.uniform(1.0, 1.5, (k, 1)))
        Rm = b * b.T; np.fill_diagonal(Rm, 1); worst = max(worst, VG(Rm))
    print("max V_G over 200 random linear pairwise models (should be <= 0):", round(worst, 4))
