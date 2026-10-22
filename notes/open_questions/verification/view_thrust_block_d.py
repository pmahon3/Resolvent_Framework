"""Block D self-check (2026-10-20; outcomes pre-registered in view_thrust_scouting_plan.md).
For a graph, alphabet n, a family of pair laws (consistent marginals) and a 'relation' function per edge:
  S = relata only (single-variable events), R = relations only (events of the relation value per edge),
  J = Dynkin closure of R u S, F = full carrier (all pair events).
Report min forced value on each (negative = twist visible to that algebra). Forced value via least squares on
the cell span after checking the functional kills the null space.
"""
import itertools, sys
import numpy as np
def run(name, V, E, n, law, rel):
    pts = list(itertools.product(range(n), repeat=V)); N = len(pts); full = (1 << N) - 1
    def mask(pred): return sum(1 << t for t, p in enumerate(pts) if pred(p))
    def closure(gens):
        D = set(gens) | {0, full}; fr = list(D)
        while fr:
            new = set(); L = list(D)
            for a in fr:
                if full ^ a not in D: new.add(full ^ a)
                for b in L:
                    if a & b == 0 and (a | b) not in D: new.add(a | b)
            D |= new; fr = list(new)
        return D
    S = closure({mask(lambda p, i=i, v=v: p[i] == v) for i in range(V) for v in range(n)})
    rvals = sorted({rel(a, b) for a in range(n) for b in range(n)})
    R = closure({mask(lambda p, e=e, r=r: rel(p[e[0]], p[e[1]]) == r) for e in E for r in rvals})
    J = closure(R | S)
    cells = [(k, a, b) for k in range(len(E)) for a in range(n) for b in range(n)]
    M = np.array([[1.0 if (p[E[k][0]] == a and p[E[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])
    mu = np.array([law(k, a, b) for (k, a, b) in cells])
    _, s, Vt = np.linalg.svd(M); null = Vt[np.sum(s > 1e-9):]
    assert np.allclose(null @ mu, 0), "functional not well defined"
    def val(m):
        f = np.array([(m >> t) & 1 for t in range(N)], float)
        c = np.linalg.lstsq(M, f, rcond=None)[0]; assert np.allclose(M @ c, f); return float(c @ mu)
    Fgens = {mask(lambda p, e=e, a=a, b=b: p[e[0]] == a and p[e[1]] == b) for e in E for a in range(n) for b in range(n)}
    F = closure(Fgens) if n ** V <= 27 else None
    out = []
    for nm, A in [("R", R), ("S", S), ("J", J), ("F", F)]:
        if A is None: out.append(f"{nm}: skipped"); continue
        out.append(f"{nm}:{len(A)} min {min(val(m) for m in A):+.3f}")
    print(f"{name:42s} | " + " | ".join(out), flush=True)
tri = [(0, 1), (1, 2), (2, 0)]
rot = lambda n, st: (lambda k, a, b: 1.0 / n if b == (a + st[k]) % n else 0.0)
diff = lambda n: (lambda a, b: (b - a) % n)
cmp_ = lambda a, b: (a > b) - (a < b)
eq = lambda a, b: int(a == b)
run("clock core, n=2, relation=difference", 3, tri, 2, rot(2, (0, 0, 1)), diff(2))
run("clock core, n=3, relation=difference", 3, tri, 3, rot(3, (0, 0, 1)), diff(3))
run("Condorcet scores mod 3 (+1,+1,+1), rel=compare", 3, tri, 3, rot(3, (1, 1, 1)), cmp_)
run("Condorcet scores mod 3 (+1,+1,+1), rel=difference", 3, tri, 3, rot(3, (1, 1, 1)), diff(3))
spec = lambda k, a, b: 0.5 if a != b else 0.0
run("Specker all-differ n=2 (non-gauge), rel=equality", 3, tri, 2, spec, eq)
noisy = lambda k, a, b: (0.45 if a != b else 0.05)
run("noisy Specker (0.9 differ) n=2, rel=equality", 3, tri, 2, noisy, eq)
C4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
par = lambda k, a, b: 0.5 if ((a != b) if k != 2 else (a == b)) else 0.0
run("C4 parity (diff,diff,same,diff) n=2, rel=equality", 4, C4, 2, par, eq)
# mod 3 with steps (1,1,1) has holonomy 3 = 0 mod 3: a world exists (control, F min 0 as expected).
# Real Condorcet test: mod 4, holonomy 3 != 0. F (64 points) skipped; visible via mod-2 transport (odd holonomy).
run("Condorcet scores mod 4 (+1,+1,+1), rel=compare", 3, tri, 4, rot(4, (1, 1, 1)), cmp_)
run("Condorcet scores mod 4 (+1,+1,+1), rel=difference", 3, tri, 4, rot(4, (1, 1, 1)), diff(4))
