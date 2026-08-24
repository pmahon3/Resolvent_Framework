"""P21-P24: junctions round (design session, 2026-07-08).

P21: figure-eight (4,4) NAND -> SAFE.
P22: figure-eight (3,4) NAND -> UNSAFE, inherited, gap 1/2.
P24: theta(2,2,2) NAND (= K_{2,3}; path-sharing stress test) -> SAFE.
P23: the bifurcation-reduction identity Safe_closure(rho,L) = Safe(rho|_V(L), L)
     on rho20, L=2..12.

Method for P21/22/24: (a) junction rank gate (P11-style: rank(EA) = #cells -
#graph-vertices AND the NAND edge-affine lift q(u) satisfies EA identically)
— failure mode (b) is exactly a gate miss, so the gate result is reported
per structure; (b) given the gate, C = FSTAB(G), R = STAB(G): exact FSTAB
vertex enumeration in marginal coordinates + exact hull membership for
fractional vertices; (c) full-harness protocol-level cross-check where n is
small (fig8(3,4) n=17, theta n=11; fig8(4,4) n=29 relies on gate+FSTAB).
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import build_protocol, rref, simplex_max
from ring_commensurability import commensurable
from winding_invariant_tests import (variety_A, in_hull, realized_arcs,
                                     simple_cycles, winding)
RHO20 = frozenset({(0,1),(1,0),(2,3),(3,4),(4,2)})

def circ_level_safe(L, rel, A):
    arcs = realized_arcs(L, [rel]*L, A)
    if not arcs:
        return None
    cyc = simple_cycles(L, arcs, A)
    secs = [c for c in cyc if winding(c, L) == 1]
    fracs = [c for c in cyc if winding(c, L) >= 2]
    if not secs:
        return 'degenerate-unsafe' if fracs else 'empty'
    arc_index = {a: j for j, a in enumerate(sorted(arcs))}
    sec_pts = []
    for s in secs:
        pt = [F(0)]*len(arc_index)
        for a in s: pt[arc_index[a]] = F(1)
        sec_pts.append(pt)
    for c in fracs:
        k = winding(c, L)
        pt = [F(0)]*len(arc_index)
        for a in c: pt[arc_index[a]] = F(1, k)
        if not in_hull(pt, sec_pts):
            return False
    return True

def graph_protocol(nverts, edges):
    """NAND on each edge of a graph: V = independent sets; contexts = edge
    scopes (V-induced cells)."""
    V = [p for p in product([0,1], repeat=nverts)
         if not any(p[x]==1==p[y] for (x,y) in edges)]
    idx = {p:i for i,p in enumerate(V)}
    ctxs = []
    for (x,y) in edges:
        cells = {}
        for p in V:
            cells.setdefault((p[x],p[y]), set()).add(idx[p])
        ctxs.append(tuple(frozenset(c) for c in cells.values()))
    return V, ctxs

def junction_gate(nverts, edges, label):
    V, ctxs = graph_protocol(nverts, edges)
    cells, ctx_of, E, f, verts = build_protocol(len(V), ctxs)
    Rr, Rp = rref([r+[v] for r,v in zip(E,f)])
    rank, d = len(Rr), len(cells)
    expect = d - nverts
    # affine lift: cell (a,b) of edge (x,y): (1,0)->u_x, (0,1)->u_y, (0,0)->1-u_x-u_y
    keys = []
    for j, cell in enumerate(cells):
        (x, y) = edges[ctx_of[j]]
        p0 = V[min(cell)]
        keys.append((x, y, p0[x], p0[y]))
    def q_of_u(u):
        q = []
        for (x,y,a,b) in keys:
            q.append({(1,0):u[x], (0,1):u[y], (0,0):1-u[x]-u[y]}[(a,b)])
        return q
    lift_ok = True
    pts = [[F(0)]*nverts] + [[F(1) if j==i else F(0) for j in range(nverts)]
                             for i in range(nverts)]
    for u in pts:
        q = q_of_u(u)
        for row, rhs in zip(E, f):
            if sum(r*x for r,x in zip(row,q)) != rhs:
                lift_ok = False
    ok = (rank == expect) and lift_ok
    print(f"  gate[{label}]: rank = {rank} (expect {expect}), lift identical = {lift_ok}"
          f" -> {'PASS: C = FSTAB(G)' if ok else 'FAIL — junction gate-analogue breaks'}")
    return ok, V

def fstab_verdict(nverts, edges, V, label, gap_face=None):
    """FSTAB(G) vertices; fractional ones tested against STAB = conv(ind sets)."""
    rows = [[(-1 if j==i else 0) for j in range(nverts)] for i in range(nverts)]
    rhs = [F(0)]*nverts
    for (x,y) in edges:
        rows.append([1 if j in (x,y) else 0 for j in range(nverts)])
        rhs.append(F(1))
    stab_pts = [[F(p[j]) for j in range(nverts)] for p in V]
    frac, bad = 0, 0
    seen = set()
    for S in combinations(range(len(rows)), nverts):
        M = [list(map(F, rows[s])) + [rhs[s]] for s in S]
        R2, P2 = rref(M)
        if len(R2) < nverts or any(pc == nverts for pc in P2):
            continue
        u = [F(0)]*nverts
        for row, pc in zip(R2, P2):
            u[pc] = row[-1]
        tu = tuple(u)
        if tu in seen: continue
        seen.add(tu)
        if any(x < 0 for x in u) or any(u[x]+u[y] > 1 for (x,y) in edges):
            continue
        if any(x not in (F(0),F(1)) for x in u):
            frac += 1
            if not in_hull(list(u), stab_pts):
                bad += 1
    safe = (bad == 0)
    print(f"  {label}: FSTAB fractional vertices = {frac}, outside STAB = {bad}"
          f" -> {'SAFE' if safe else 'UNSAFE'}")
    if gap_face is not None and not safe:
        # gap of the inherited odd-cycle facet: max over FSTAB of sum u_i - 1
        c = [F(1) if j in gap_face else F(0) for j in range(nverts)]
        A_ub = [[1 if j in (x,y) else 0 for j in range(nverts)] for (x,y) in edges]
        b_ub = [F(1)]*len(edges)
        st, val, _ = simplex_max(c, [], [], A_ub, b_ub)
        print(f"    inherited facet gap: max_C sum_triangle u - 1 = {val - 1}")
    return safe

print("== P21: figure-eight (4,4) NAND — predicted SAFE ==")
# vertices: 0 = junction; ring A: 0-1-2-3-0; ring B: 0-4-5-6-0
E44 = [(0,1),(1,2),(2,3),(0,3),(0,4),(4,5),(5,6),(0,6)]
ok, V = junction_gate(7, E44, "fig8(4,4)")
if ok:
    safe = fstab_verdict(7, E44, V, "fig8(4,4)")
    print("  P21:", "HIT" if safe else "MISS")

print("== P22: figure-eight (3,4) NAND — predicted UNSAFE, gap 1/2 ==")
# 0 = junction; ring A (C3): 0-1-2-0; ring B (C4): 0-3-4-5-0
E34 = [(0,1),(1,2),(0,2),(0,3),(3,4),(4,5),(0,5)]
ok, V = junction_gate(6, E34, "fig8(3,4)")
if ok:
    safe = fstab_verdict(6, E34, V, "fig8(3,4)", gap_face={0,1,2})
    print("  P22:", "HIT" if not safe else "MISS")
# harness cross-check (n small)
Vx, ctxs = graph_protocol(6, E34)
okh, _ = commensurable(len(Vx), ctxs, "  cross-check harness fig8(3,4)")
print("  cross-check agrees:", okh == False)

print("== P24: theta(2,2,2) NAND (K_{2,3}) — predicted SAFE ==")
# hubs 0, 1 (non-adjacent); middles 2,3,4; edges hub-middle
ETH = [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
ok, V = junction_gate(5, ETH, "theta(2,2,2)")
if ok:
    safe = fstab_verdict(5, ETH, V, "theta(2,2,2)")
    print("  P24:", "HIT" if safe else "MISS")
Vx, ctxs = graph_protocol(5, ETH)
okh, _ = commensurable(len(Vx), ctxs, "  cross-check harness theta(2,2,2)")
print("  cross-check agrees:", okh == True)

print("== P23: Safe_closure(rho20, L) = Safe(rho20|_V(L), L), L=2..12 ==")
from ring_commensurability import scope_contexts
for L in range(2, 13):
    V = variety_A(L, [RHO20]*L, 5)
    if not V:
        print(f"  L={L}: variety empty — both sides degenerate (identity trivially holds)")
        continue
    # LHS: closure-level = EA-on-V protocol verdict
    lhs, _ = commensurable(len(V), scope_contexts(V, [(i,(i+1)%L) for i in range(L)]),
                           f"  L={L} closure-level (n={len(V)})")
    # RHS: winding theorem on the V-restricted language (uniform by rotation)
    used = {(p[0], p[1]) for p in V}
    rhs_verdict = circ_level_safe(L, frozenset(used), 5)
    match = (lhs == (rhs_verdict is True))
    print(f"    restricted language {sorted(used)} -> theorem verdict {rhs_verdict}"
          f" | identity: {'HOLDS' if match else 'VIOLATED'}")
