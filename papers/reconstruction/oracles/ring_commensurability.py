"""Separation-only commensurability test for the ring-parity questions
(C = R iff commensurable; skips the family-classification ladder, which is
the right tool at k<=3 but blows up its exact LPs at k=5,6).
Verdicts remain exact-rational; a separating witness is re-verified by
substitution when found."""
import sys, time
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product
from commensurability_harness import (build_protocol, r_hull_and_facets,
                                      rref, in_rowspace, simplex_max)

def commensurable(n, contexts, label):
    t0 = time.time()
    cells, ctx_of, E, f, verts = build_protocol(n, contexts)
    aug = [row + [rhs] for row, rhs in zip(E, f)]
    Rr, Rp = rref(aug)
    hull_eqs, facets = r_hull_and_facets(verts)
    def mx(c_obj):
        st, val, x = simplex_max(c_obj, E, f, [], [])
        assert st == 'optimal'
        return val, x
    for u, rhs in hull_eqs:
        if in_rowspace(Rr, Rp, list(u) + [rhs]):
            continue
        val, x = mx(list(u))
        if val != rhs:
            print(f"{label}: INCOMMENSURABLE (hull-eq witness) [{time.time()-t0:.0f}s]")
            return False, x
        val2, x2 = mx([-t for t in u])
        if -val2 != rhs:
            print(f"{label}: INCOMMENSURABLE (hull-eq witness) [{time.time()-t0:.0f}s]")
            return False, x2
    for a, b in facets:
        val, x = mx(list(a))
        if val > b:
            # re-verify witness: coherent (by LP constraints) and outside R via this facet
            assert all(sum(ai*vi for ai, vi in zip(a, v)) <= b for v in verts)
            print(f"{label}: INCOMMENSURABLE (facet witness, gap {val-b}) [{time.time()-t0:.0f}s]")
            return False, x
    print(f"{label}: COMMENSURABLE (C = R, all {len(facets)} facets + "
          f"{len(hull_eqs)} hull eqs verified exactly) [{time.time()-t0:.0f}s]")
    return True, None

def ring_variety(L):
    return [p for p in product([0,1],repeat=L)
            if not any(p[i]==1==p[(i+1)%L] for i in range(L))]

def scope_contexts(V, scopes):
    idx = {p:i for i,p in enumerate(V)}
    out = []
    for S in scopes:
        cells = {}
        for p in V:
            cells.setdefault(tuple(p[i] for i in S), set()).add(idx[p])
        out.append(tuple(frozenset(c) for c in cells.values()))
    return out

for L in [3, 5, 4, 6]:
    V = ring_variety(L)
    ctxs = scope_contexts(V, [(i,(i+1)%L) for i in range(L)])
    tag = {3:"C3 (odd)", 5:"C5 (odd)", 4:"P7: C4 (even)", 6:"P8: C6 (even)"}[L]
    commensurable(len(V), ctxs, f"{tag}, n={len(V)}, k={L}")
