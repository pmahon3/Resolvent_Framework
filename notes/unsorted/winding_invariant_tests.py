"""P13-P16: the winding/circulation invariant round (design session, 2026-07-07).

Framework under test: for edge-scope ring protocols passing the RANK GATE
(EA system == circulation/conservation system on realized arcs), C = the
normalized circulation polytope of the layered ring, whose vertices are
(1/k)*chi_cycle over simple directed cycles (flow decomposition; winding k),
and R = conv(sections) = conv(winding-1 cycles). Commensurable <=> every
winding->=2 vertex lies in conv(sections).

P13 (decisive): ternary rho = 3-cycle {01,12,20} + loop {00}. Predicted
     Safe = 3Z exactly (mod-3, not parity => invariant is period structure).
P14: NAND stays safe at L=8,10 (TU sanity at scale).
P15: (a) exhaustive necklace search over NAND: NONE at even L=4,6,8;
     positive control: necklaces exist at odd L (XOR beads). (b) the rank
     gate run per language/L used anywhere in this round.
P16: separation hunt — a winding->=2 vertex OUTSIDE conv(sections) whose
     support still carries a section (incommensurable w/o strong
     contextuality). Exhaustive over uniform ternary relations, L=3,4.
     Hit => forward half of the necklace conjecture breaks; miss => proof
     attempt licensed.

Cross-checks: circulation-level verdicts vs full-harness separation test at
small L (P13 at L=3,4,5; must agree).
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product
from commensurability_harness import build_protocol, rref, simplex_max
from ring_commensurability import commensurable, scope_contexts

# ---------------- layered-ring machinery ----------------

def variety(L, rels):
    return [p for p in product(range(max(max(a,b) for r in rels for (a,b) in r)+1
                                     if rels[0] else 0), repeat=L)
            if all((p[i], p[(i+1)%L]) in rels[i] for i in range(L))]

def variety_A(L, rels, A):
    return [p for p in product(range(A), repeat=L)
            if all((p[i], p[(i+1)%L]) in rels[i] for i in range(L))]

def realized_arcs(L, rels, A):
    """Arcs on directed cycles of the layered ring = arcs realized by V."""
    arcs = {(i,a,b) for i in range(L) for (a,b) in rels[i] if a < A and b < A}
    # arc on a cycle iff some closed walk uses it; equivalent: keep arcs whose
    # endpoints stay in the recurrent part. Iterative prune of dead vertices.
    while True:
        outs = {}
        ins = {}
        for (i,a,b) in arcs:
            outs.setdefault((i,a), []).append((i,a,b))
            ins.setdefault(((i+1)%L, b), []).append((i,a,b))
        dead = set()
        verts = set(outs) | set(ins)
        for v in verts:
            if v not in outs or v not in ins:
                dead.add(v)
        if not dead:
            return arcs
        arcs = {(i,a,b) for (i,a,b) in arcs
                if (i,a) not in dead and ((i+1)%L, b) not in dead}

def simple_cycles(L, arcs, A):
    """All simple directed cycles of the layered ring, as frozensets of arcs."""
    adj = {}
    for (i,a,b) in arcs:
        adj.setdefault((i,a), []).append(((i+1)%L, b, (i,a,b)))
    found = set()
    def dfs(start, v, path, visited):
        for (w0, w1, arc) in adj.get(v, []):
            w = (w0, w1)
            if w == start:
                found.add(frozenset(path + [arc]))
            elif w not in visited:
                dfs(start, w, path + [arc], visited | {w})
    for a0 in range(A):
        s = (0, a0)
        if s in adj:
            dfs(s, s, [], {s})
    return found

def winding(cycle, L):
    return len(cycle) // L

def cycle_vertex(cycle, L, arc_index):
    k = winding(cycle, L)
    v = [F(0)] * len(arc_index)
    for arc in cycle:
        v[arc_index[arc]] = F(1, k)
    return v

def in_hull(point, hull_pts):
    if not hull_pts:
        return False
    m, d = len(hull_pts), len(point)
    A_eq = [[F(hull_pts[i][j]) for i in range(m)] for j in range(d)]
    b_eq = [F(x) for x in point]
    A_eq.append([F(1)] * m)
    b_eq.append(F(1))
    st, _, _ = simplex_max([F(0)] * m, A_eq, b_eq, [], [])
    return st == 'optimal'

def circulation_analysis(L, rels, A):
    """Returns (commensurable?, #sections, #frac_vertices, list of bad
    (outside-hull) fractional vertices with their cycles)."""
    arcs = realized_arcs(L, rels, A)
    if not arcs:
        return None  # degenerate: empty variety
    arc_index = {arc: j for j, arc in enumerate(sorted(arcs))}
    cyc = simple_cycles(L, arcs, A)
    sections = [c for c in cyc if winding(c, L) == 1]
    fracs = [c for c in cyc if winding(c, L) >= 2]
    sec_pts = [cycle_vertex(c, L, arc_index) for c in sections]
    bad = []
    for c in fracs:
        if not in_hull(cycle_vertex(c, L, arc_index), sec_pts):
            bad.append(c)
    return (len(bad) == 0, len(sections), len(fracs), bad, arc_index)

# ---------------- rank gate ----------------

def rank_gate(L, rels, A, label):
    """EA rowspace == conservation rowspace (on realized-arc coordinates)."""
    V = variety_A(L, rels, A)
    ctxs = scope_contexts(V, [(i, (i+1)%L) for i in range(L)])
    cells, ctx_of, E, f, verts = build_protocol(len(V), ctxs)
    # identify each cell with its realized arc (edge index + scope key)
    idxV = {p: i for i, p in enumerate(V)}
    cell_arc = []
    for j, cell in enumerate(cells):
        i = ctx_of[j]
        p0 = V[min(cell)]
        cell_arc.append((i, p0[i], p0[(i+1)%L]))
    arcs = realized_arcs(L, rels, A)
    assert set(cell_arc) == arcs, "realized arcs != EA cells"
    d = len(cells)
    # conservation system in cell coordinates + one normalization
    rows, rhs = [], []
    verts_l = {(i,a) for (i,a,b) in arcs} | {((i+1)%L, b) for (i,a,b) in arcs}
    for (i, a) in verts_l:
        row = [F(0)] * d
        for j, (e, x, y) in enumerate(cell_arc):
            if e == i and x == a: row[j] += 1            # outflow of (i,a)
            if (e+1) % L == i and y == a: row[j] -= 1    # inflow to (i,a)
        rows.append(row); rhs.append(F(0))
    row = [F(0)] * d
    for j, (e, x, y) in enumerate(cell_arc):
        if e == 0: row[j] = F(1)
    rows.append(row); rhs.append(F(1))
    A1 = [r + [v] for r, v in zip(E, f)]
    A2 = [r + [v] for r, v in zip(rows, rhs)]
    R1, P1 = rref(A1)
    R2, P2 = rref(A2)
    R12, _ = rref(A1 + A2)
    same = (len(R1) == len(R2) == len(R12))
    print(f"   gate[{label}]: rank EA = {len(R1)}, rank circ = {len(R2)},"
          f" joint = {len(R12)} -> {'PASS (identical rowspaces)' if same else 'MISS'}")
    return same

# ---------------- P13 ----------------
print("== P13: ternary 3-cycle + loop-at-0; predicted Safe = 3Z ==")
RHO13 = {(0,0),(0,1),(1,2),(2,0)}
A3 = 3
for L in range(3, 10):
    rels = [RHO13]*L
    res = circulation_analysis(L, rels, A3)
    comm, nsec, nfrac, bad, _ = res
    pred = (L % 3 == 0)
    ok = (comm == pred)
    print(f" L={L}: sections={nsec}, frac vertices={nfrac}, "
          f"commensurable={comm} (predicted {pred}) -> {'HIT' if ok else 'MISS'}")
    if L <= 6:
        rank_gate(L, rels, A3, f"P13 L={L}")
# cross-check with full harness at L=3,4,5
for L in (3, 4, 5):
    V = variety_A(L, [RHO13]*L, A3)
    ctxs = scope_contexts(V, [(i,(i+1)%L) for i in range(L)])
    ok, _ = commensurable(len(V), ctxs, f"   cross-check harness P13 L={L} (n={len(V)})")
    assert ok == (L % 3 == 0), "circulation-level and harness verdicts DISAGREE"

# ---------------- P14 ----------------
print("== P14: NAND safe at L=8,10 ==")
NAND = {(0,0),(0,1),(1,0)}
for L in (8, 10):
    res = circulation_analysis(L, [NAND]*L, 2)
    comm, nsec, nfrac, bad, _ = res
    print(f" L={L}: sections={nsec}, frac vertices={nfrac}, commensurable={comm}"
          f" -> {'HIT' if comm else 'MISS'}")
    rank_gate(L, [NAND]*L, 2, f"P14 L={L}")

# ---------------- P15 ----------------
print("== P15: exhaustive necklace search over NAND ==")
def boolmul(P, Q, A):
    return tuple(tuple(1 if any(P[i][k] and Q[k][j] for k in range(A)) else 0
                       for j in range(A)) for i in range(A))
def has_necklace(L, choices, A):
    """choices: per-edge nonempty sub-relations. Necklace iff layered graph
    has a cycle but no winding-1 cycle: tr(P)=0 and tr(P^k)>0 some k<=A."""
    mats = []
    for rel in choices:
        M = tuple(tuple(1 if (a,b) in rel else 0 for b in range(A)) for a in range(A))
        mats.append(M)
    P = mats[0]
    for M in mats[1:]:
        P = boolmul(P, M, A)
    if any(P[i][i] for i in range(A)):
        return False              # winding-1 exists
    Q = P
    for k in range(2, A+1):
        Q = boolmul(Q, P, A)
        if any(Q[i][i] for i in range(A)):
            return True           # cycle of winding k, none of winding 1
    return False

from itertools import combinations
nand_subs = []
pairs = sorted(NAND)
for mask in range(1, 8):
    nand_subs.append(frozenset(pairs[t] for t in range(3) if mask >> t & 1))
for L in (4, 6, 8):
    found = 0
    for choice in product(nand_subs, repeat=L):
        if has_necklace(L, choice, 2):
            found += 1
    print(f" even L={L}: {found} necklaces over {7**L} assignments ->",
          "HIT (none)" if found == 0 else "MISS")
for L in (3, 5):
    found = any(has_necklace(L, choice, 2) for choice in product(nand_subs, repeat=L))
    print(f" odd L={L} positive control: necklace exists = {found} ->",
          "OK" if found else "CONTROL FAILED")

# ---------------- P16 ----------------
print("== P16: separation hunt (uniform ternary relations, L=3,4) ==")
all_pairs = [(a,b) for a in range(3) for b in range(3)]
hits, tested = [], 0
for mask in range(1, 512):
    rel = frozenset(all_pairs[t] for t in range(9) if mask >> t & 1)
    for L in (3, 4):
        res = circulation_analysis(L, [rel]*L, 3)
        if res is None:
            continue
        tested += 1
        comm, nsec, nfrac, bad, arc_index = res
        if comm or nsec == 0:
            continue   # commensurable, or strongly-contextual-only regime trivially
        # incommensurable with sections present: check whether some BAD vertex's
        # support carries a section (winding-1 cycle inside its own arcs)
        for c in bad:
            sub = c  # arc set of the bad cycle
            sec_inside = any(winding(s, L) == 1
                             for s in simple_cycles(L, set(sub), 3))
            if sec_inside:
                hits.append((rel, L, sorted(sub)))
print(f" {tested} (relation, L) instances analyzed;"
      f" P16 hits (bad vertex w/ section-carrying support): {len(hits)}")
if hits:
    rel, L, sub = hits[0]
    print("  FIRST HIT: L =", L, " rel =", sorted(rel))
    print("  bad cycle arcs:", sub)
else:
    print(" -> MISS at exhaustive uniform scale: forward proof attempt LICENSED")
