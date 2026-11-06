#!/usr/bin/env python3
"""Frustration in zooplankton communities (FRUSTRATION_ZOOPLANKTON.md). Usage: python3 frustration_zooplankton.py <ntl37_v15.csv>"""
import csv, sys, math, itertools, collections
import numpy as np
from scipy.stats import rankdata
from arch.bootstrap import optimal_block_length
LAKES = ["AL", "BM", "CR", "SP", "TR"]; SUMMER = {6, 7, 8}


def rho(A): return float(np.max(np.abs(np.linalg.eigvalsh(A))))
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def jit(Y, rng):
    J = Y.astype(float).copy()
    for j in range(Y.shape[1]):
        u = np.unique(Y[:, j]); gap = np.min(np.diff(u)) if len(u) > 1 else 1.0; J[:, j] += rng.normal(0, 1e-3 * gap, len(Y))
    return J


def detr(Y):
    t = np.arange(len(Y), dtype=float); X = np.column_stack([np.ones_like(t), t]); b, *_ = np.linalg.lstsq(X, Y, rcond=None); return Y - X @ b


def vg_test(Y, rng, det, NB=1000):
    n, k = Y.shape; t = np.arange(n, dtype=float)
    def R_of(idx):
        A = Y[idx]
        if det:
            X = np.column_stack([np.ones(len(idx)), t[idx]]); b, *_ = np.linalg.lstsq(X, A, rcond=None); A = A - X @ b
        return spear(A)
    R = R_of(np.arange(n)); T = math.sqrt(n) * (rho(np.abs(R - np.eye(k))) - 1)
    b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, Y))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
    D = []
    for _ in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); D.append(rho(np.abs(Z)))
    return T, float(np.percentile(D, 95)), R


def main(path):
    rng = np.random.default_rng(23)
    dens = collections.defaultdict(lambda: collections.defaultdict(list))   # lake -> (year, code) -> densities (per date avg later)
    names = {}
    for r in csv.DictReader(open(path)):
        if r["lakeid"] not in LAKES or int(r["sample_date"][5:7]) not in SUMMER: continue
        code = int(r["species_code"]); nm = r["species_name"]
        if code % 100 == 0 or code == 10000 or "UNKNOWN" in nm.upper() or not nm.strip() or r["density"] in ("", "NA"): continue
        names[code] = nm; dens[r["lakeid"]][(int(r["sample_date"][:4]), code)].append(float(r["density"]))
    for lk in LAKES:
        D = dens[lk]; years = sorted({y for y, _ in D}); codes = sorted({c for _, c in D})
        pres = {c: np.mean([np.mean(D.get((y, c), [0])) > 0 for y in years]) for c in codes}
        cand = [c for c in codes if pres[c] >= 0.8]
        meanv = {c: np.mean([np.mean(D.get((y, c), [0])) for y in years]) for c in cand}
        top = sorted(cand, key=lambda c: -meanv[c])[:8]
        yrs = [y for y in years if all((y, c) in D for c in top)]
        Y = np.array([[math.log10(np.mean(D[(y, c)]) + 1) for c in top] for y in yrs])
        R = spear(Y); k = len(top); prs = list(itertools.combinations(range(k), 2))
        neg = np.mean([R[i, j] < 0 for i, j in prs])
        tris = list(itertools.combinations(range(k), 3))
        fr = [t for t in tris if np.sign(R[t[0], t[1]] * R[t[1], t[2]] * R[t[0], t[2]]) > 0]
        v_fr = [rho(np.abs(R[np.ix_(t, t)] - np.eye(3))) - 1 for t in fr]
        v_ab = [rho(np.abs(R[np.ix_(t, t)] - np.eye(3))) - 1 for t in tris if t not in fr]
        out = [f"\n== {lk}: {k} species, n = {len(yrs)} years; negative pairs {neg:.2f}; frustrated triangles {len(fr)}/{len(tris)} "
               f"(antibalanced {1 - len(fr)/len(tris):.2f}); max triangle V2: frustrated {max(v_fr, default=float('nan')):+.3f}, antibalanced {max(v_ab, default=float('nan')):+.3f}"]
        for det in (False, True):
            T, crit, _ = vg_test(jit(Y, rng), rng, det)
            out.append(f"   whole-set V_G test ({'detrended' if det else 'raw'}): T = {T:+.2f} vs crit {crit:.2f} -> {'REJECT (common cause of >=3 species)' if T > crit else 'no rejection'}")
        print("\n".join(out), flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
