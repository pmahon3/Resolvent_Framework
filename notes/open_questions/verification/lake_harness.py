#!/usr/bin/env python3
"""Pre-registered lake calibration harness (notes/open_questions/views_across_records/LAKE_HARNESS.md).
Usage: python3 -I lake_harness.py <path to ntl37_v15.csv>"""
import csv, sys, itertools, collections
import numpy as np
from scipy.optimize import linprog
from scipy.stats import spearmanr

LAKES = ["AL", "BM", "CR", "SP", "TR"]
G = ["D", "C", "R"]                       # Daphnia, copepods, rotifers


def group_of(code, name):                 # fixed 2026-11-05 from the code/name list only
    if 51100 <= code <= 51199: return "D"
    if (20000 <= code <= 20999 and code != 29900) or 30000 <= code <= 30999: return "C"
    if 60000 <= code <= 63999 or "ROTIFER" in name.upper(): return "R"
    return None


def load(path):
    st = collections.defaultdict(lambda: dict(D=0.0, C=0.0, R=0.0))   # (lake,date,station) -> sums
    for r in csv.DictReader(open(path)):
        if r["lakeid"] not in LAKES: continue
        key = (r["lakeid"], r["sample_date"], r["station"])
        g = group_of(int(r["species_code"]), r["species_name"])
        st[key]                                   # sampled date, even if no taxon of a group
        if g and r["density"] not in ("", "NA"):
            st[key][g] += float(r["density"])
    by = collections.defaultdict(list)
    for (lk, dt, s), v in st.items(): by[(lk, dt)].append(v)
    data = {lk: [] for lk in LAKES}
    for (lk, dt), vs in sorted(by.items()):
        data[lk].append((int(dt[:4]), [np.log10(np.mean([v[g] for v in vs]) + 1) for g in G]))
    return data


def binarise(rows):
    X = np.array([x for _, x in rows]); yrs = np.array([y for y, _ in rows])
    return yrs, X > np.median(X, axis=0)


def joint(B):                              # empirical law on {0,1}^3, index 4a+2b+c
    idx = B[:, 0] * 4 + B[:, 1] * 2 + B[:, 2]
    return np.bincount(idx.astype(int), minlength=8) / len(B)


def dis(B, i, j): return float(np.mean(B[:, i] != B[:, j]))


def V_of(dDC, dCR, dRD):
    return max(0.0, dRD - dDC - dCR, dDC - dCR - dRD, dCR - dDC - dRD, dDC + dCR + dRD - 2)


def delta_full(Ps):                        # min_Q max_k TV(Q,P_k): vars q(8), u_k(8) per k, t
    K = len(Ps); n = 8 + 8 * K + 1
    c = np.zeros(n); c[-1] = 1
    A, b = [], []
    for k, P in enumerate(Ps):
        for s in range(8):
            for sg in (1, -1):             # sg*(q_s - P_s) <= u_ks
                row = np.zeros(n); row[s] = sg; row[8 + 8 * k + s] = -1; A.append(row); b.append(sg * P[s])
        row = np.zeros(n); row[8 + 8 * k:8 + 8 * k + 8] = 0.5; row[-1] = -1; A.append(row); b.append(0)
    Aeq = np.zeros((1, n)); Aeq[0, :8] = 1
    return linprog(c, A_ub=np.array(A), b_ub=b, A_eq=Aeq, b_eq=[1], bounds=(0, None)).fun


def main(path):
    data = load(path)
    Bs, Ps, years = {}, {}, {}
    for lk in LAKES:
        years[lk], Bs[lk] = binarise(data[lk]); Ps[lk] = joint(Bs[lk])
        d = (dis(Bs[lk], 0, 1), dis(Bs[lk], 1, 2), dis(Bs[lk], 2, 0))
        print(f"{lk}: n_dates={len(Bs[lk])}  years {years[lk].min()}-{years[lk].max()}  d(DC,CR,RD)={tuple(round(x,3) for x in d)}  same-lake V={V_of(*d):.2e}")
    split, truth = [], []
    for a, b, c in itertools.permutations(LAKES, 3):
        e = V_of(dis(Bs[a], 0, 1), dis(Bs[b], 1, 2), dis(Bs[c], 2, 0)) / 3
        split.append(e); truth.append(delta_full([Ps[a], Ps[b], Ps[c]]))
    split, truth = np.array(split), np.array(truth)
    assert np.all(split <= truth + 1e-9), "bound eps_split <= delta_full violated"
    null, nulltruth = [], []
    for lk in LAKES:
        sets = [Bs[lk][years[lk] % 3 == m] for m in range(3)]
        Pset = [joint(S) for S in sets]
        for a, b, c in itertools.permutations(range(3), 3):
            null.append(V_of(dis(sets[a], 0, 1), dis(sets[b], 1, 2), dis(sets[c], 2, 0)) / 3)
            nulltruth.append(delta_full([Pset[a], Pset[b], Pset[c]]))
    null, nulltruth = np.array(null), np.array(nulltruth)
    q95 = np.percentile(null, 95); rho = spearmanr(split, truth).correlation
    print(f"\nreal designs (60): eps_split median {np.median(split):.4f}, max {split.max():.4f}, frac>0 {np.mean(split>0):.2f}")
    print(f"                   delta_full median {np.median(truth):.4f}, max {truth.max():.4f}")
    print(f"pseudo-lake null (30): eps_null median {np.median(null):.4f}, 95th {q95:.4f}, max {null.max():.4f}, frac>0 {np.mean(null>0):.2f}")
    print(f"                       delta_full(null) median {np.median(nulltruth):.4f}, 95th {np.percentile(nulltruth,95):.4f}")
    print(f"Spearman(eps_split, delta_full) = {rho:.3f}")
    if np.median(split) <= q95: v = "TOOTHLESS"
    elif rho > 0.5: v = "INFORMATIVE"
    else: v = "LOOSE"
    print("VERDICT:", v)


if __name__ == "__main__":
    main(sys.argv[1])
