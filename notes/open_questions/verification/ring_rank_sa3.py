"""Ring detection rank (2026-10-20; prediction P1 pre-registered in definitions_draft.md section 15).
A state on D_3 restricts to a probability on every 3-subset algebra, agreeing on shared pairs and with the
given edge laws (Sherali-Adams level 3). If that LP is infeasible, the twist is visible at rank <= 3.
Pair views (D_2) are blind on rings (known), so infeasible => rank exactly 3. A = 2.
"""
import itertools
import numpy as np
from scipy.optimize import linprog
def sa3(name, V, edges, law):
    triples = list(itertools.combinations(range(V), 3)); vals = list(itertools.product((0, 1), repeat=3))
    nv = len(triples) * 8; idx = lambda t, v: t * 8 + vals.index(v)
    Aeq, beq = [], []
    for t, T in enumerate(triples):
        Aeq.append([1.0 if k // 8 == t else 0.0 for k in range(nv)]); beq.append(1.0)
    pairs = list(itertools.combinations(range(V), 2))
    for (i, j) in pairs:
        ts = [t for t, T in enumerate(triples) if i in T and j in T]
        for a, b in itertools.product((0, 1), repeat=2):
            def row(t):
                T = triples[t]; r = [0.0] * nv
                for v in vals:
                    if v[T.index(i)] == a and v[T.index(j)] == b: r[idx(t, v)] = 1.0
                return r
            if (i, j) in edges or (j, i) in edges:
                e = edges.index((i, j)) if (i, j) in edges else edges.index((j, i))
                pa, pb = (a, b) if (i, j) in edges else (b, a)
                for t in ts: Aeq.append(row(t)); beq.append(law(e, pa, pb))
            for t1, t2 in zip(ts, ts[1:]):
                r1, r2 = row(t1), row(t2); Aeq.append([x - y for x, y in zip(r1, r2)]); beq.append(0.0)
    res = linprog(np.zeros(nv), A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * nv, method="highs")
    print(f"{name:34s} SA3 feasible: {res.status == 0}  -> {'rank > 3 or needs more' if res.status == 0 else 'visible at rank 3'}")
par = lambda e, a, b: 0.5 if ((a != b) if e != 2 else (a == b)) else 0.0
sa3("C4 parity (diff,diff,same,diff)", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], par)
spec = lambda e, a, b: 0.5 if a != b else 0.0
sa3("C5 all-differ", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], spec)
for p in (0.9, 0.75, 0.6):
    noisy = lambda e, a, b, p=p: (p / 2 if a != b else (1 - p) / 2)
    sa3(f"C5 noisy all-differ P(differ)={p}", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], noisy)
    sa3(f"C4 noisy parity P={p}", 4, [(0, 1), (1, 2), (2, 3), (3, 0)],
        lambda e, a, b, p=p: ((p / 2 if a != b else (1 - p) / 2) if e != 2 else (p / 2 if a == b else (1 - p) / 2)))
