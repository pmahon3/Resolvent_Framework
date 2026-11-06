#!/usr/bin/env python3
"""Poland innovations (DYNAMIC_CLOSURE.md): restricted VAR (own lag + 2 nearest sites' lags), then V_G, reach m=3,4, radius H(d)."""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np, networkx as nx
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m_ = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py"); hm = mod("hm", "hypergraph_method.py"); spz = mod("spz", "spearman_poland.py")


def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def main(csvp, wdir):
    rng = np.random.default_rng(25); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y0 = np.array([[S[s][0][y] for s in sites] for y in yrs]); k = len(sites)
    Dm = np.array([[m_.km(S[a][1], S[b][1]) for b in sites] for a in sites])
    nbr = [list(np.argsort(Dm[i])[1:3]) for i in range(k)]
    pairs = list(itertools.combinations(range(k), 2)); dists = sorted(Dm[i, j] for i, j in pairs)
    grid = [float(np.quantile(dists, q)) for q in np.arange(0.1, 1.0, 0.1)]

    def innov(X, idx):
        P0, P1 = X[:-1][idx], X[1:][idx]; E = np.empty_like(P1)
        for i in range(k):
            Z = np.column_stack([np.ones(len(idx)), P0[:, i], P0[:, nbr[i][0]], P0[:, nbr[i][1]]]); cc, *_ = np.linalg.lstsq(Z, P1[:, i], rcond=None); E[:, i] = P1[:, i] - Z @ cc
        return spear(E)

    hyps = {"pairs (V_G)": pairs, "reach<=3": list(itertools.combinations(range(k), 3)), "reach<=4": list(itertools.combinations(range(k), 4))}
    for d in grid:
        G = nx.Graph(); G.add_nodes_from(range(k)); G.add_edges_from((i, j) for i, j in pairs if Dm[i, j] <= d)
        hyps[f"radius {d:.0f} km"] = pairs + [tuple(sorted(q)) for q in nx.find_cliques(G) if len(q) >= 3]
    solvers = {name: hm.VH(H, k) for name, H in hyps.items()}
    rej = {name: 0 for name in hyps}; Ts = {name: [] for name in hyps}
    for draw in range(5):
        X = np.log1p(spz.jitter(Y0, rng)); n = len(X) - 1; full = np.arange(n); R = innov(X, full)
        b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, X))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
        Zs = []
        for _ in range(300):
            st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
            Z = math.sqrt(n) * (innov(X, idx) - R); np.fill_diagonal(Z, 0); Zs.append(Z)
        for name, f in solvers.items():
            T = math.sqrt(n) * f(R); crit = np.percentile([f(np.eye(k) + Z) + 1 for Z in Zs], 95)
            rej[name] += T > crit; Ts[name].append(T)
        print(f"draw {draw+1}/5 done (block {b})", flush=True)
    print(f"innovations: restricted VAR (own + 2 nearest sites), n = {len(Y0)-1}")
    for name in hyps:
        print(f"   {name:16s} T range [{min(Ts[name]):+.2f}, {max(Ts[name]):+.2f}]   rejected {rej[name]}/5")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
