"""gate.finite_staircase_carrier, buildability check (2026-10-18).
The window family F_A (x_{k+1} = x_k + 1 mod A) is invariant under the diagonal shift x -> x + (1,1,1).
The window events that depend only on a difference x_j - x_i are shift-invariant. Their Dynkin closure
D_inv (complements and disjoint unions) consists of genuinely buildable questions (D_inv is inside D)
and lives on the A^2 shift-orbits. We compute D_inv exactly and the minimum of Lambda over it.
Lambda of an invariant set = sum over its points of the forced weights lambda (from finite_staircase_carrier).
"""
import itertools, sys
import numpy as np
sys.path.insert(0, '.')
from finite_staircase_carrier import run as _run
def lam_vector(A):
    pts = list(itertools.product(range(A), repeat=3)); ix = {p: i for i, p in enumerate(pts)}; n = len(pts)
    W = [(0, 1), (1, 2), (2, 0)]
    rows = []; rhs = []
    for k, (i, j) in enumerate(W):
        for a in range(A):
            for b in range(A):
                r = np.zeros(n)
                for p in pts:
                    if p[i] == a and p[j] == b: r[ix[p]] = 1
                rows.append(r); rhs.append(1.0 / A if b == (a + 1) % A else 0.0)
    lam = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0]
    return pts, lam
for A in range(3, int(sys.argv[1]) + 1):
    pts, lam = lam_vector(A)
    orb = {}; 
    for p in pts:
        key = ((p[1] - p[0]) % A, (p[2] - p[0]) % A)    # orbit label = (d01, d02)
        orb.setdefault(key, []).append(p)
    keys = sorted(orb); kidx = {k: i for i, k in enumerate(keys)}; m = len(keys)
    ix = {p: i for i, p in enumerate(pts)}
    w = [sum(lam[ix[p]] for p in orb[k]) for k in keys]
    full = (1 << m) - 1
    gens = set()
    # invariant window events: window (0,1) depends on d01; (1,2) on d12 = d02 - d01; (2,0) on d20 = -d02
    funcs = [lambda k: k[0], lambda k: (k[1] - k[0]) % A, lambda k: (-k[1]) % A]
    for f in funcs:
        for R in range(1 << A):
            mask = 0
            for k in keys:
                if R >> f(k) & 1: mask |= 1 << kidx[k]
            gens.add(mask)
    D = set(gens) | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            c = full ^ a
            if c not in D: new.add(c)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    val = lambda mask: sum(w[i] for i in range(m) if mask >> i & 1)
    best = min(D, key=val)
    print(f"A={A}: |D_inv|={len(D)} of 2^{m}; min Lambda over D_inv = {val(best):.4f}; max = {max(val(x) for x in D):.4f}", flush=True)
    if val(best) < -1e-9:
        print("   minimising buildable set, as orbits (d01, d02):", [keys[i] for i in range(m) if best >> i & 1])
