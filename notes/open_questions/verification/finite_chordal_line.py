"""gate.finite_chordal_line (ii), 2026-10-18. Pair windows on 4 slots over {0,1}. Graphs: C4 (non-chordal),
the diamond (two triangles sharing an edge) and K4 (both chordal). D = the Dynkin closure of the window
events, computed directly (not assumed equal to the 0/1 span). Board polytope = consistent window cell
probabilities mu with forced value Lambda_mu(E) >= 0 for all E in D. Joint = mixtures of points.
Test: sample board vertices with random objectives; check each for being a mixture (LP). A non-mixture is
a rigorous witness; none found is evidence that board = joint.
Lambda_mu(E) is defined only if E lies in the span V; D is inside V, which is checked.
"""
import itertools, sys
import numpy as np
from scipy.optimize import linprog
A = 2; V = 4
GRAPHS = {'C4': [(0, 1), (1, 2), (2, 3), (3, 0)],
          'diamond': [(0, 1), (1, 2), (0, 2), (2, 3), (3, 0)],
          'K4': [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]}
pts = list(itertools.product(range(A), repeat=V)); n = len(pts); full = (1 << n) - 1
for name, E in GRAPHS.items():
    cells = [(k, a, b) for k in range(len(E)) for a in range(A) for b in range(A)]
    G = np.array([[1.0 if (p[E[k][0]] == a and p[E[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])
    gens = set()
    for k, (i, j) in enumerate(E):
        for S in range(1 << (A * A)):
            m = 0
            for t, p in enumerate(pts):
                if S >> (p[i] * A + p[j]) & 1: m |= 1 << t
            gens.add(m)
    D = set(gens) | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    Dv = [np.array([(m >> t) & 1 for t in range(n)], dtype=float) for m in D]
    Gp = np.linalg.pinv(G)
    Y = np.array([Gp @ f for f in Dv])
    inV = max(np.abs(G @ y - f).max() for y, f in zip(Y, Dv)) < 1e-9
    # constraints: windows sum to 1; shared-slot marginals agree
    Aeq = []; beq = []
    for k in range(len(E)):
        Aeq.append([1.0 if c[0] == k else 0.0 for c in cells]); beq.append(1.0)
    def marg(k, slot, val):
        i, j = E[k]
        return np.array([1.0 if (c[0] == k and ((i == slot and c[1] == val) or (j == slot and c[2] == val))) else 0.0 for c in cells])
    for slot in range(V):
        ks = [k for k, (i, j) in enumerate(E) if slot in (i, j)]
        for k2 in ks[1:]:
            for val in range(A):
                Aeq.append(list(marg(ks[0], slot, val) - marg(k2, slot, val))); beq.append(0.0)
    Aeq = np.array(Aeq); beq = np.array(beq)
    def is_mixture(mu):
        r = linprog(np.zeros(n), A_eq=np.vstack([G.T, np.ones((1, n))]), b_eq=np.concatenate([mu, [1.0]]),
                    bounds=(0, None), method='highs')
        return r.status == 0
    rng = np.random.default_rng(1); witness = None; tried = 0
    for t in range(300):
        c = rng.normal(size=len(cells))
        res = linprog(-c, A_ub=-Y, b_ub=np.zeros(len(Y)), A_eq=Aeq, b_eq=beq, bounds=(0, 1), method='highs')
        if res.status != 0: continue
        tried += 1
        if not is_mixture(res.x): witness = res.x; break
    print(f"{name}: |D| = {len(D)} (inside span: {inV}); sampled {tried} board vertices; "
          f"non-mixture board state found: {witness is not None}", flush=True)
    if witness is not None:
        print("   witness cells:", {cells[i]: round(v, 3) for i, v in enumerate(witness) if v > 1e-6})
