"""P25-P27: the K4-minor experiment + lifting-lemma controls (2026-07-08).

P25: even-subdivided K4 (every edge subdivided once; every circuit even),
     NAND beads. Circuit Localization -> SAFE; minor-theoretic line asks
     whether K4-minor facets survive NAND's restricted supports.
     Pre-stated mechanism note (this side): for NAND, evenizing circuits =
     bipartitizing the graph, so gate + classical bipartite FSTAB-integrality
     would tame the minor; the OPEN part at this structure is the gate.
P26: theta(3,3,2) NAND -> UNSAFE by inheritance through the two 5-circuits,
     gap 1/2 (lifting lemma in the path-sharing regime).
P27: totality necessity — matched lollipop pair (triangle C3-NAND + tail
     edge at vertex 0): (a) tail relation {(1,1)} (state 0 dead-ends at the
     tail): the unsafe triangle CANNOT lift -> G safe, intersection formula
     violated without totality; (b) tail relation equality {(0,0),(1,1)}
     (total): inheritance restored -> G unsafe. Controls the lemma's
     hypothesis in both directions.
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import simplex_max
from ring_commensurability import commensurable
from junction_tests import graph_protocol, junction_gate, fstab_verdict

print("== P25: even-subdivided K4, NAND ==")
# K4 vertices 0..3; midpoints 4..9 for edges (01),(02),(03),(12),(13),(23)
mid = {(0,1):4,(0,2):5,(0,3):6,(1,2):7,(1,3):8,(2,3):9}
EK4 = []
for (u,v),m in mid.items():
    EK4 += [(u,m),(m,v)]
# sanity: bipartite (originals vs midpoints)
side = [0,0,0,0,1,1,1,1,1,1]
assert all(side[x] != side[y] for (x,y) in EK4)
print("  structure sanity: subdivided K4 is bipartite (K4 minor retained)")
ok, V = junction_gate(10, EK4, "subdiv-K4")
if ok:
    safe = fstab_verdict(10, EK4, V, "subdiv-K4")
    print("  P25:", ("HIT — SAFE: the language refinement TAMES the minor "
                     "obstruction (mechanism: even circuits = bipartite for NAND "
                     "+ gate => FSTAB integral regardless of minors)") if safe
          else "UNSAFE — minor-type third mechanism EXISTS")

print("== P26: theta(3,3,2) NAND — predicted UNSAFE, inherited, gap 1/2 ==")
# hubs 0,1; paths 0-2-3-1, 0-4-5-1, 0-6-1
ET = [(0,2),(2,3),(3,1),(0,4),(4,5),(5,1),(0,6),(6,1)]
ok, V = junction_gate(7, ET, "theta(3,3,2)")
if ok:
    safe = fstab_verdict(7, ET, V, "theta(3,3,2)", gap_face=None)
    # gap of the 5-circuit odd-cycle inequality: vertices {0,2,3,1,6}, sum u <= 2
    five = {0,2,3,1,6}
    c = [F(1) if j in five else F(0) for j in range(7)]
    A_ub = [[1 if j in (x,y) else 0 for j in range(7)] for (x,y) in ET]
    st, val, _ = simplex_max(c, [], [], A_ub, [F(1)]*len(ET))
    print(f"    5-circuit inequality: max_C sum u = {val} vs STAB bound 2 -> gap {val-2}")
    print("  P26:", "HIT" if (not safe and val - 2 == F(1,2)) else "MISS")

print("== P27: totality necessity — matched lollipop pair ==")
# vertices: triangle 0,1,2 + tail vertex 3 attached at 0
TRI = [(0,1),(1,2),(0,2)]
def lollipop_protocol(tail_rel):
    """Mixed language: NAND on triangle edges, tail_rel on edge (0,3)."""
    V = [p for p in product([0,1], repeat=4)
         if not any(p[x]==1==p[y] for (x,y) in TRI)
         and (p[0],p[3]) in tail_rel]
    idx = {p:i for i,p in enumerate(V)}
    ctxs = []
    for (x,y) in TRI + [(0,3)]:
        cells = {}
        for p in V:
            cells.setdefault((p[x],p[y]), set()).add(idx[p])
        ctxs.append(tuple(frozenset(c) for c in cells.values()))
    return V, ctxs

# standalone triangle: unsafe (known: half-model, gap 1/2) — re-verified
Vt, ctxs_t = graph_protocol(3, TRI)
ok_t, _ = commensurable(len(Vt), ctxs_t, "  standalone C3-NAND (n=%d)" % len(Vt))
print("  standalone triangle unsafe:", not ok_t)

# (a) dead-end tail {(1,1)}: state 0 has no tail continuation
Va, ctxs_a = lollipop_protocol({(1,1)})
ok_a, _ = commensurable(len(Va), ctxs_a, f"  lollipop dead-end tail (n={len(Va)})")
# (b) total tail (equality)
Vb, ctxs_b = lollipop_protocol({(0,0),(1,1)})
ok_b, _ = commensurable(len(Vb), ctxs_b, f"  lollipop equality tail (n={len(Vb)})")
hit = ok_a and (not ok_b) and (not ok_t)
print("  P27:", "HIT — without totality the unsafe circuit cannot lift (G safe,"
      " intersection formula fails); with totality inheritance returns" if hit else "MISS")
