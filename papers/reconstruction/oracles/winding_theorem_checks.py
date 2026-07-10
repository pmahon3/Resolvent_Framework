"""P17-P20: corroboration round for the winding characterization theorem
(design session, 2026-07-08).

P17: exact vertex enumeration of the EA polytope C (cell coordinates, zero-set
     method) = exactly the normalized simple layered cycles (Lemma 1 + gate),
     on gate-passing instances: NAND L=5, rho13 L=4, full-binary L=3, XOR L=4.
P18: Safe(rho13) recomputed PURELY from the primitive-orbit criterion
     (period q, winding k = q/gcd(q,L) >= 2, injective wrap: the k states each
     layer receives are distinct) reproduces {3} across L=3..9.
P19: full-language L=4 winding-2 simple cycles are exactly the anti-periodic
     words w_{i+4} = 1 - w_i, and all are C\\R witnesses.
P20 (fresh forward test): rho20 = 2-cycle on {0,1} + 3-cycle on {2,3,4}
     (disjoint). Predicted Safe = 6Z at the relation/circulation level.
     ALSO: the honesty-ledger caveat's first concrete exhibit — the transfer
     digraph is DISCONNECTED, so on clocks one component's period does not
     divide, that component's arcs are V-unrealized: the rank gate FAILS and
     the observed EA-on-V protocol diverges from the circulation object.
     Both levels reported.
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from math import gcd
from itertools import product, combinations
from commensurability_harness import build_protocol, rref, simplex_max
from ring_commensurability import commensurable, scope_contexts
from winding_invariant_tests import (variety_A, realized_arcs, simple_cycles,
                                     winding, in_hull, RHO13)

NAND = frozenset({(0,0),(0,1),(1,0)})
FULL2 = frozenset({(0,0),(0,1),(1,0),(1,1)})
XOR = frozenset({(0,1),(1,0)})
RHO20 = frozenset({(0,1),(1,0),(2,3),(3,4),(4,2)})

# ---------------- P17 ----------------

def ea_vertices(L, rels, A):
    """Exact vertex enumeration of C in cell coordinates (zero-set method)."""
    V = variety_A(L, rels, A)
    ctxs = scope_contexts(V, [(i,(i+1)%L) for i in range(L)])
    cells, ctx_of, E, f, verts = build_protocol(len(V), ctxs)
    d = len(cells)
    Rr, Rp = rref([r + [v] for r, v in zip(E, f)])
    dim = d - len(Rr)
    vertices = set()
    for Z in combinations(range(d), dim):
        rows = [r + [v] for r, v in zip(E, f)]
        for z in Z:
            rows.append([F(1) if j == z else F(0) for j in range(d)] + [F(0)])
        RR, PP = rref(rows)
        piv = [pc for pc in PP if pc < d]
        if len(RR) < d or len(piv) < d:
            continue
        if any(pc == d for pc in PP):
            continue  # inconsistent
        q = [F(0)] * d
        ok = True
        for row, pc in zip(RR, PP):
            if pc < d:
                q[pc] = row[-1]
        if all(x >= 0 for x in q):
            vertices.add(tuple(q))
    # predicted: normalized simple cycles on realized arcs, in cell coords
    idxV = {p: i for i, p in enumerate(V)}
    cell_arc = []
    for j, cell in enumerate(cells):
        i = ctx_of[j]
        p0 = V[min(cell)]
        cell_arc.append((i, p0[i], p0[(i+1)%L]))
    arc_pos = {arc: j for j, arc in enumerate(cell_arc)}
    arcs = set(cell_arc)
    predicted = set()
    for c in simple_cycles(L, arcs, A):
        k = winding(c, L)
        v = [F(0)] * d
        for arc in c:
            v[arc_pos[arc]] = F(1, k)
        predicted.add(tuple(v))
    return vertices, predicted

print("== P17: EA-polytope vertices == normalized simple cycles ==")
for (label, L, rels, A) in [("NAND L=5", 5, [NAND]*5, 2),
                            ("rho13 L=4", 4, [RHO13]*4, 3),
                            ("full-binary L=3", 3, [FULL2]*3, 2),
                            ("XOR L=4", 4, [XOR]*4, 2)]:
    vs, pred = ea_vertices(L, rels, A)
    ok = (vs == pred)
    print(f" {label}: |vertices| = {len(vs)}, |predicted| = {len(pred)} ->",
          "HIT (sets identical)" if ok else "MISS")
    assert ok

# ---------------- P18 ----------------

def primitive_orbits(rel, A, qmax):
    """Primitive cyclic words (up to rotation) legal for rel, period <= qmax."""
    adj = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    orbits = []
    for q in range(1, qmax + 1):
        seen = set()
        def walks(start, v, word):
            if len(word) == q:
                if start in adj[v]:
                    rots = {tuple(word[r:] + word[:r]) for r in range(q)}
                    if not rots & seen:
                        seen.add(tuple(word))
                        # primitive?
                        prim = all(q % p != 0 or
                                   any(word[i] != word[i % p] for i in range(q))
                                   for p in range(1, q))
                        if prim:
                            orbits.append(tuple(word))
                return
            for b in adj[v]:
                walks(start, b, word + [b])
        for a in range(A):
            walks(a, a, [a])
    return orbits

def orbit_unsafe(L, rel, A):
    """Unsafe(L) per the orbit criterion: some primitive orbit wraps
    injectively with winding >= 2."""
    for w in primitive_orbits(rel, A, A * L):
        q = len(w)
        k = q // gcd(q, L)
        if k < 2 or k > A:
            continue
        if all(len({w[(i + j * L) % q] for j in range(k)}) == k for i in range(L)):
            return True, w
    return False, None

print("== P18: Safe(rho13) from the orbit criterion alone ==")
safe = []
for L in range(3, 10):
    unsafe, w = orbit_unsafe(L, RHO13, 3)
    if not unsafe:
        safe.append(L)
    print(f" L={L}: orbit-criterion unsafe = {unsafe}"
          + (f" (witness orbit {w})" if w else ""))
print(f" Safe(rho13) by orbit criterion = {safe} ->",
      "HIT (= {3})" if safe == [3] else "MISS")
assert safe == [3]

# ---------------- P19 ----------------
print("== P19: full-language L=4 winding-2 cycles are anti-periodic ==")
arcs = realized_arcs(4, [FULL2]*4, 2)
w2 = [c for c in simple_cycles(4, arcs, 2) if winding(c, 4) == 2]
antip, bad_struct = 0, 0
V4 = variety_A(4, [FULL2]*4, 2)
ctxs4 = scope_contexts(V4, [(i,(i+1)%4) for i in range(4)])
for c in w2:
    # reconstruct the length-8 word by walking the cycle from its min layer-0 arc
    nxt = {}
    for (i,a,b) in c:
        nxt[(i,a)] = b
    start = min((a for (i,a,b) in c if i == 0))
    word, v = [], (0, start)
    for t in range(8):
        b = nxt[v]
        word.append(v[1])
        v = ((v[0]+1) % 4, b)
    if all(word[(i+4) % 8] == 1 - word[i] for i in range(8)):
        antip += 1
print(f" winding-2 simple cycles: {len(w2)}; anti-periodic: {antip} ->",
      "HIT" if antip == len(w2) and len(w2) > 0 else "MISS")
assert antip == len(w2) > 0

# ---------------- P20 ----------------
print("== P20: rho20 = 2-cycle + 3-cycle (disjoint); predicted Safe_circ = 6Z ==")
def circ_level_safe(L, rel, A):
    """Relation/circulation level: layered graph on ALL cycle-supported arcs
    (no V-pruning beyond dead-arc removal)."""
    arcs = realized_arcs(L, [rel]*L, A)   # prunes non-cycle arcs only
    if not arcs:
        return None
    cyc = simple_cycles(L, arcs, A)
    secs = [c for c in cyc if winding(c, L) == 1]
    fracs = [c for c in cyc if winding(c, L) >= 2]
    if not secs:
        return 'degenerate-unsafe' if fracs else 'empty'
    arc_index = {a: j for j, a in enumerate(sorted(arcs))}
    sec_pts = [[F(0)]*len(arc_index) for _ in secs]
    for s, pt in zip(secs, sec_pts):
        for a in s: pt[arc_index[a]] = F(1)
    for c in fracs:
        k = winding(c, L)
        pt = [F(0)]*len(arc_index)
        for a in c: pt[arc_index[a]] = F(1, k)
        if not in_hull(pt, sec_pts):
            return False
    return True

circ_safe = []
for L in range(2, 13):
    r = circ_level_safe(L, RHO20, 5)
    if r is True:
        circ_safe.append(L)
    print(f" L={L}: circulation-level -> {r}")
pred = [L for L in range(2, 13) if L % 6 == 0]
print(f" Safe_circ(rho20) = {circ_safe} (predicted 6Z = {pred}) ->",
      "HIT" if circ_safe == pred else "MISS")

print("-- P20b: the honesty-ledger caveat, exhibited (V-level divergence) --")
from winding_invariant_tests import rank_gate
for L in (2, 3, 4, 6):
    V = variety_A(L, [RHO20]*L, 5)
    try:
        g = rank_gate(L, [RHO20]*L, 5, f"rho20 L={L}")
    except AssertionError as e:
        print(f"   gate[rho20 L={L}]: FAIL — {e} (component arcs V-unrealized)")
        g = False
    if V:
        ok, _ = commensurable(len(V), scope_contexts(V, [(i,(i+1)%L) for i in range(L)]),
                              f"   EA-on-V harness rho20 L={L} (n={len(V)})")
