"""Harness v2 calibration anchors (design session, 2026-07-07):
(c) full-support k=3 coordinate protocol (2x2x2 cube, n=8) must come back
    commensurable (product-measure theorem);
(d) punctured-cube instances (cube minus 2 points, n=6, coordinate contexts)
    — facet weight spectrum via gauge-reduced LP lower bound; design-side
    prediction: some punctured instance reaches weight >= 3 at reachable scale.
Also: the gauge weight of the n=5 fourth-mechanism facet.

Weight LB: for a facet with tight vertex set T and strict set S, any INTEGER
representative (lambda, mu) has lambda.v = mu on T and lambda.v <= mu - 1 on S
(integrality of 0/1 vertices). LP relaxation: minimize ||lambda||_inf under
those constraints -> valid lower bound on the gauge-reduced integer weight;
ceil to integer.
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import (analyze, build_protocol, r_hull_and_facets,
                                      simplex_max)

def facet_weight_LB(cells_d, verts, facet):
    a, b = facet
    d = len(a)
    T = [v for v in verts if sum(x*y for x, y in zip(a, v)) == b]
    S = [v for v in verts if sum(x*y for x, y in zip(a, v)) < b]
    # vars: lam = lp - ln (2d), mu = mp - mn (2), t (1); minimize t
    nv = 2*d + 3
    A_eq, b_eq, A_ub, b_ub = [], [], [], []
    def lamrow(v, sign):
        row = [F(0)]*nv
        for j in range(d):
            row[j] = sign*F(v[j]); row[d+j] = -sign*F(v[j])
        row[2*d] = -sign*F(1); row[2*d+1] = sign*F(1)
        return row
    for v in T:
        A_eq.append(lamrow(v, 1)); b_eq.append(F(0))          # lam.v - mu = 0
    for v in S:
        A_ub.append(lamrow(v, 1)); b_ub.append(F(-1))         # lam.v - mu <= -1
    for j in range(d):                                        # |lam_j| <= t
        r1 = [F(0)]*nv; r1[j] = F(1); r1[d+j] = F(-1); r1[2*d+2] = F(-1)
        A_ub.append(r1); b_ub.append(F(0))
        r2 = [F(0)]*nv; r2[j] = F(-1); r2[d+j] = F(1); r2[2*d+2] = F(-1)
        A_ub.append(r2); b_ub.append(F(0))
    cobj = [F(0)]*nv; cobj[2*d+2] = F(-1)                     # maximize -t
    st, val, x = simplex_max(cobj, A_eq, b_eq, A_ub, b_ub)
    assert st == 'optimal', st
    lb = -val
    import math
    return lb, math.ceil(lb) if lb == int(lb) else math.ceil(lb)

# ---------- anchor (c): 2x2x2 cube, coordinate contexts ----------
pts = list(product([0,1],repeat=3))
idx = {p:i for i,p in enumerate(pts)}
coords = []
for axis in range(3):
    c0 = frozenset(idx[p] for p in pts if p[axis]==0)
    c1 = frozenset(idx[p] for p in pts if p[axis]==1)
    coords.append((c0,c1))
res = analyze(8, 3, coords)
print("(c) 2x2x2 coordinate protocol:", res['verdict'],
      "-> PASS" if res['verdict']=='R_EQUALS_C' else "-> FAIL")
assert res['verdict']=='R_EQUALS_C'

# ---------- weight of the n=5 fourth-mechanism facet ----------
P1 = (frozenset({0}), frozenset({1}), frozenset({2,3,4}))
P2 = (frozenset({0}), frozenset({1,2}), frozenset({3,4}))
P3 = (frozenset({0}), frozenset({1,3}), frozenset({2,4}))
cells, ctx_of, E, f, verts = build_protocol(5, [P1,P2,P3])
hull_eqs, facets = r_hull_and_facets(verts)
wmax = 0
for fac in facets:
    lb, w = facet_weight_LB(cells, verts, fac)
    wmax = max(wmax, w)
print(f"n=5 fourth-mechanism protocol: {len(facets)} facets, weight spectrum max = {wmax}")

# ---------- anchor (d): punctured cubes (n=6) ----------
print("(d) punctured cubes (cube minus 2 points), coordinate contexts:")
seen_classes = {}
for pair in combinations(pts, 2):
    dist = sum(a!=b for a,b in zip(*pair))
    if dist in seen_classes: continue
    seen_classes[dist] = pair
for dist, pair in sorted(seen_classes.items()):
    keep = [p for p in pts if p not in pair]
    kidx = {p:i for i,p in enumerate(keep)}
    ctxs = []
    ok = True
    for axis in range(3):
        c0 = frozenset(kidx[p] for p in keep if p[axis]==0)
        c1 = frozenset(kidx[p] for p in keep if p[axis]==1)
        if not c0 or not c1: ok = False; break
        ctxs.append((c0,c1))
    if not ok: continue
    res = analyze(6, 3, ctxs)
    cells, ctx_of, E, f, verts = build_protocol(6, ctxs)
    hull_eqs, facets = r_hull_and_facets(verts)
    wmax, witness_fac = 0, None
    for fac in facets:
        lb, w = facet_weight_LB(cells, verts, fac)
        if w > wmax: wmax, witness_fac = w, fac
    print(f"  puncture Hamming-dist {dist}: verdict={res['verdict']},"
          f" facets={len(facets)}, max gauge-weight LB = {wmax}")
    if wmax >= 3:
        print("    weight>=3 facet:", [str(t) for t in witness_fac[0]], "<=", str(witness_fac[1]))
