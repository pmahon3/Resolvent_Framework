#!/usr/bin/env python3
"""Step 4: Poland spatial-reach test H(d) (HYPERGRAPH_METHOD.md)."""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np, networkx as nx
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m_ = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py"); hm = mod("hm", "hypergraph_method.py"); spz = mod("spz", "spearman_poland.py")


def main(csvp, wdir):
    rng = np.random.default_rng(21); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y0 = np.array([[S[s][0][y] for s in sites] for y in yrs]); k = len(sites)
    Dm = np.array([[m_.km(S[a][1], S[b][1]) for b in sites] for a in sites])
    dists = sorted(Dm[i, j] for i, j in itertools.combinations(range(k), 2)); grid = [float(np.quantile(dists, q)) for q in np.arange(0.1, 1.0, 0.1)]
    print(f"sites {k}, n = {len(yrs)}; inter-site distances {min(dists):.0f}-{max(dists):.0f} km; grid {[round(g) for g in grid]}")
    pairs = list(itertools.combinations(range(k), 2))
    for d in grid:
        G = nx.Graph(); G.add_nodes_from(range(k)); G.add_edges_from((i, j) for i, j in pairs if Dm[i, j] <= d)
        H = pairs + [tuple(sorted(q)) for q in nx.find_cliques(G) if len(q) >= 3]
        f = hm.VH(H, k); res = []
        for _ in range(5):
            Y = np.apply_along_axis(lambda col: col, 0, spz.jitter(Y0, rng))
            res.append(hm.test(Y, f, rng, NB=300) if True else None)
        R = hm.spear(spz.jitter(Y0, rng)); T = math.sqrt(len(yrs)) * f(R)
        maxc = max((len(q) for q in nx.find_cliques(G)), default=1)
        print(f"d = {d:6.0f} km: largest local centre {maxc} sites; T = {T:+.2f}; rejected in {sum(res)}/5 jitter draws", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
