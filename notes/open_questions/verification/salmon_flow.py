#!/usr/bin/env python3
"""Whole flow on sockeye salmon (SALMON_FLOW.md). Usage: python3 salmon_flow.py <sr.csv> <coords.csv>"""
import csv, sys, math, itertools, collections, importlib.util
from pathlib import Path
import numpy as np, networkx as nx
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
hm = mod("hm", "hypergraph_method.py"); m_ = mod("m", "mast_ceiling_gate.py")
F1 = [("Bristol Bay", s) for s in ["Alagnak River", "Egegik River", "Igushik River", "Kvichak River", "Naknek River", "Nushagak River", "Togiak River", "Ugashik River", "Wood River"]]
F2 = [("Bristol Bay", "Kvichak River"), ("Black Lake", "Chignik River Watershed"), ("Upper Cook Inlet", "Kenai River"), ("PWS", "Copper River"),
      ("KodiakMgmtArea", "Frazer Lake"), ("BC North Coast", "Skeena"), ("Fraser", "Chilko")]
DFO = {("BC North Coast", "Skeena"), ("Fraser", "Chilko")}


def rho(A): return float(np.max(np.abs(np.linalg.eigvalsh(A))))
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def load(srp, cop):
    co = {r["locationCode"]: (float(r["lat"]), float(r["lon"])) for r in csv.DictReader(open(cop))}
    d = collections.defaultdict(dict); loc = {}
    for r in csv.DictReader(open(srp)):
        if r["species"] != "sockeye" or r["spawners"] in ("", "NA") or r["recruits"] in ("", "NA"): continue
        S, Rr = float(r["spawners"]), float(r["recruits"])
        if S > 0 and Rr > 0: d[(r["region"], r["stock"])][int(float(r["BY"]))] = (S, Rr); loc[(r["region"], r["stock"])] = co.get(r["locationCode"])
    return d, loc


def ricker_resid(series):
    yrs = sorted(series); S = np.array([series[y][0] for y in yrs]); R = np.array([series[y][1] for y in yrs])
    z = np.log(R / S); X = np.column_stack([np.ones_like(S), S]); b, *_ = np.linalg.lstsq(X, z, rcond=None)
    return dict(zip(yrs, z - X @ b))


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2; return 12742 * math.asin(math.sqrt(h))


def block(Y): return int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, Y))['circular'].max()), 2), len(Y) // 3))


def run_test(R_of, n, f, rng, NB, base):
    R = R_of(np.arange(n)); T = math.sqrt(n) * f(R); b = block(base); nbl = math.ceil(n / b); D = []
    for _ in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); D.append(f(np.eye(len(R)) + Z) + 1)
    return T, float(np.percentile(D, 95))


def family(name, stocks, d, loc, rng, radius=True):
    res = {s: ricker_resid(d[s]) for s in stocks}
    yrs = sorted(set.intersection(*[set(res[s]) for s in stocks])); Y = np.array([[res[s][y] for s in stocks] for y in yrs]); n, k = Y.shape
    t = np.array(yrs, float); pairs = list(itertools.combinations(range(k), 2)); I = np.eye(k)
    vgf = lambda R: rho(np.abs(R - np.eye(len(R)))) - 1
    print(f"\n== {name}: {k} stocks, brood years {yrs[0]}-{yrs[-1]} (n = {n}); mean |r| = {np.mean([abs(spear(Y)[i,j]) for i,j in pairs]):.2f}", flush=True)
    def resid_on(cols): 
        def f_(idx):
            X = np.column_stack([np.ones(len(idx))] + [c_[idx] for c_ in cols]); bb, *_ = np.linalg.lstsq(X, Y[idx], rcond=None); return spear(Y[idx] - X @ bb)
        return f_
    for lab, R_of in (("raw", lambda idx: spear(Y[idx])), ("detrended", resid_on([t])), ("step-1977 removed", resid_on([(t >= 1977).astype(float)]))):
        T, crit = run_test(R_of, n, vgf, rng, 1000, Y); print(f"   1 V_G {lab:18s}: T = {T:+.2f} vs {crit:.2f} {'REJECT' if T > crit else ''}", flush=True)
    hyps = {f"reach<={m}": list(itertools.combinations(range(k), m)) for m in (3, 4, 5) if m < k}
    if radius:
        Dm = np.array([[km(loc[a], loc[b]) for b in stocks] for a in stocks]); dd = sorted(Dm[i, j] for i, j in pairs)
        for q in np.arange(0.1, 1.0, 0.2):
            dq = float(np.quantile(dd, q)); G = nx.Graph(); G.add_nodes_from(range(k)); G.add_edges_from((i, j) for i, j in pairs if Dm[i, j] <= dq)
            hyps[f"radius<={dq:.0f}km"] = pairs + [tuple(sorted(c)) for c in nx.find_cliques(G) if len(c) >= 3]
        nbr = [list(np.argsort(Dm[i])[1:3]) for i in range(k)]
    else:
        nbr = [[(i + 1) % k, (i - 1) % k] for i in range(k)]
    def innov(idx):
        P0, P1 = Y[:-1][idx], Y[1:][idx]; E = np.empty_like(P1)
        for i in range(k):
            X = np.column_stack([np.ones(len(idx)), P0[:, i], P0[:, nbr[i][0]], P0[:, nbr[i][1]]]); cc, *_ = np.linalg.lstsq(X, P1[:, i], rcond=None); E[:, i] = P1[:, i] - X @ cc
        return spear(E)
    for hname, H in hyps.items():
        f = hm.VH(H, k); T, crit = run_test(lambda idx: spear(Y[idx]), n, f, rng, 300, Y)
        Ti, criti = run_test(innov, n - 1, f, rng, 300, Y)
        print(f"   {hname:18s} levels T = {T:+.2f} vs {crit:.2f} {'REJECT' if T > crit else '      '} | innovations T = {Ti:+.2f} vs {criti:.2f} {'REJECT' if Ti > criti else ''}", flush=True)
    Ti, criti = run_test(innov, n - 1, vgf, rng, 1000, Y); print(f"   4 V_G innovations    : T = {Ti:+.2f} vs {criti:.2f} {'REJECT' if Ti > criti else ''}", flush=True)
    return Y, stocks


def main(srp, cop):
    rng = np.random.default_rng(26); d, loc = load(srp, cop)
    family("F1 Bristol Bay", F1, d, loc, rng)
    Y, stocks = family("F2 North Pacific cross-agency", F2, d, loc, rng)
    trip = [t for t in itertools.combinations(range(len(stocks)), 3) if any(stocks[i] in DFO for i in t) and any(stocks[i] not in DFO for i in t)]
    ps = []
    for t in trip:
        Yt = Y[:, list(t)]; R0 = spear(Yt); T = math.sqrt(len(Yt)) * (rho(np.abs(R0 - np.eye(3))) - 1)
        b = block(Yt); nbl = math.ceil(len(Yt) / b); D = []
        for _ in range(4000):
            st = rng.integers(0, len(Yt) - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:len(Yt)]
            Z = math.sqrt(len(Yt)) * (spear(Yt[idx]) - R0); np.fill_diagonal(Z, 0); D.append(rho(np.abs(Z)))
        ps.append(max(np.mean(np.array(D) >= T), 1 / 4000))
    rej = m_.holm(np.array(ps))
    print(f"\n== F3 protocol-free triples (ADF&G + DFO): {len(trip)} triples; Holm-significant {int(rej.sum())}; min p {min(ps):.4f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
