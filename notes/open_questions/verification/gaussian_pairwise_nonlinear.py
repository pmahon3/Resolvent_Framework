#!/usr/bin/env python3
"""Step 2: can nonlinear PAIRWISE-ONLY worlds exceed the linear-Gaussian ceiling? (population, n = 1e6, 3 sites)"""
import importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import norm, rankdata
sp = importlib.util.spec_from_file_location("g", Path(__file__).with_name("gaussian_pairwise.py")); g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
rng = np.random.default_rng(0); N = 1_000_000
Z = rng.standard_normal((N, 3))             # pair sources AB, BC, CA
AB, BC, CA = Z.T
q = norm.ppf(1 - 2**-0.5)
worlds = {
    "additive (linear)": lambda f: (f(AB) + f(CA), f(AB) + f(BC), f(BC) + f(CA)),
    "min (AND-like)": lambda f: (np.minimum(AB, CA), np.minimum(AB, BC), np.minimum(BC, CA)),
    "max": lambda f: (np.maximum(AB, CA), np.maximum(AB, BC), np.maximum(BC, CA)),
    "product": lambda f: (AB * CA, AB * BC, BC * CA),
    "AND indicator q=1/sqrt2": lambda f: ((AB > q) & (CA > q), (AB > q) & (BC > q), (BC > q) & (CA > q)),
    "heavy tail exp(2S) sum": lambda f: (np.exp(2*AB) + np.exp(2*CA), np.exp(2*AB) + np.exp(2*BC), np.exp(2*BC) + np.exp(2*CA)),
    "heavy tail max exp(3S)": lambda f: (np.maximum(np.exp(3*AB), np.exp(3*CA)), np.maximum(np.exp(3*AB), np.exp(3*BC)), np.maximum(np.exp(3*BC), np.exp(3*CA))),
    "rare-event spikes": lambda f: ((AB > 2.5) * 10 + (CA > 2.5) * 10, (AB > 2.5) * 10 + (BC > 2.5) * 10, (BC > 2.5) * 10 + (CA > 2.5) * 10),
}
print(f"{'world':26s} {'pearson r (AB,BC,CA)':>26s} {'V_G raw':>8s} {'V_G log1p':>9s} {'V_G normal-scores':>17s}")
for name, w in worlds.items():
    Y = np.column_stack([np.asarray(v, float) for v in w(lambda s: s)])
    out = []
    for tf in ("raw", "log", "ns"):
        X = Y.copy()
        if tf == "log": X = np.log1p(X - X.min(0))
        if tf == "ns": X = norm.ppf((np.apply_along_axis(rankdata, 0, X) - 0.5) / N)
        R = np.corrcoef(X.T); out.append((R, g.VG(R)))
    R0 = out[0][0]
    print(f"{name:26s} {str([round(R0[0,1],3), round(R0[1,2],3), round(R0[0,2],3)]):>26s} {out[0][1]:+8.3f} {out[1][1]:+9.3f} {out[2][1]:+17.3f}", flush=True)
