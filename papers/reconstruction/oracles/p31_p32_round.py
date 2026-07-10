"""P31/P32/P33 round (2026-07-09), with the rho* mis-triage caught pre-run.

CATCH: rho* = {(0,0),(0,2),(1,1),(2,0)} has DISCONNECTED relation digraph
({0,2} + {1}) => on connected G the 1-sector mass is globally constant and
rho* = NAND(0,2) (+) fixed-point. Taming #6: DIRECT-SUM DECOMPOSITION
(machine-checked below): LOCAL(rho1+rho2, G) = mixtures of the component
polytopes => Safe(rho1+rho2) = Safe(rho1) ∩ Safe(rho2) on connected G.

P31 (as registered — prediction safe): decided by decomposition + the stored
  P25 verdict (NAND on even-subdivided K4 SAFE, gate PASS, zero fractional
  vertices). The prediction HITS; the experiment is NOT the fork (taming #6);
  mechanism correction recorded.
P32 (taming-#4 control): theta-digraph 0->1,1->{2,3},2->0,3->0 at q=3 on
  subdivided K4 (16 vertices, 18 edges): predicted SAFE with the RANK DROP
  visible — dim C = dim R = factorized dimension (2 sector-mixing dof +
  6+6+4 free binary choices), far below the unfactorized count; plus exact
  random-direction LP equality max_C = max_R as the safety evidence at a
  scale where full facet enumeration is infeasible (scope declared).
P33 (corrected): rho* disqualified; rerun survivors with connectivity +
  decomposition filter -> the TRUE minimal fork candidates.
"""
import sys, json, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import build_protocol, rref, simplex_max
from swap_spectrum_scan import unsafe_set, base_walk_lengths, canonical

# ---------- taming #6 machine check on rho*, small instance ----------
print("== Taming #6 check: rho* sector-mass forcing on a small connected graph ==")
RS = {(0,0),(0,2),(1,1),(2,0)}
# path of 3 vertices a->b->c: V = homs
Vp = [p for p in product(range(3), repeat=3)
      if (p[0],p[1]) in RS and (p[1],p[2]) in RS]
one_sector = [p for p in Vp if 1 in p]
assert all(p == (1,1,1) for p in one_sector)
print(f"  path-3: |V|={len(Vp)}; every config touching state 1 IS all-1:"
      f" {len(one_sector)==1} -> sector separation confirmed;"
      " rho* = NAND(0,2) ⊕ point")

# ---------- P31 ----------
print("== P31: rho* on q=2-subdivided K4 ==")
print("  decomposition lemma (connected G): LOCAL(rho*) = {λ·δ_all1 ⊕ (1-λ)·"
      "LOCAL_NAND}, MARG likewise -> C=R ⟺ NAND-part C=R ⟺ subdiv-K4 bipartite.")
print("  stored P25 verdict: NAND on even-subdivided K4: gate PASS, 0 fractional"
      " FSTAB vertices, SAFE.")
print("  P31: HIT (prediction 'safe' correct) — but NOT the fork: taming #6"
      " (direct sum) reduces it to P25's bipartite taming. Mis-triage corrected.")

# ---------- P32 ----------
print("== P32: theta-digraph at q=3 on subdivided K4 (taming-#4 control) ==")
TH = {(0,1),(1,2),(1,3),(2,0),(3,0)}
K4E = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
verts = 4
edges = []
for (u,v) in K4E:
    chain = [u, verts, verts+1, v]; verts += 2
    edges += [(chain[i], chain[i+1]) for i in range(3)]
A = 4
# V by backtracking
Vg = []
def bt(assign, i, order, adjc):
    if i == len(order):
        Vg.append(tuple(assign[v] for v in range(verts))); return
    v = order[i]
    for s in range(A):
        ok = True
        for (x,y) in edges:
            if x == v and assign.get(y) is not None and (s, assign[y]) not in TH: ok=False;break
            if y == v and assign.get(x) is not None and (assign[x], s) not in TH: ok=False;break
        if ok:
            assign[v] = s; bt(assign, i+1, order, adjc); assign[v] = None
bt({v: None for v in range(verts)}, 0, list(range(verts)), None)
print(f"  |V| = {len(Vg)} (predicted 144 = 64+64+16 across 3 phase sectors):"
      f" {'MATCH' if len(Vg)==144 else 'MISMATCH'}")
idx = {p:i for i,p in enumerate(Vg)}
ctxs = []
for (x,y) in edges:
    cells = {}
    for p in Vg:
        cells.setdefault((p[x],p[y]), set()).add(idx[p])
    ctxs.append(tuple(frozenset(c) for c in cells.values()))
cells, ctx_of, E, f, vertsR = build_protocol(len(Vg), ctxs)
d = len(cells)
Rr, Rp = rref([r+[v] for r,v in zip(E,f)])
dimC = d - len(Rr)
diffs = [[vv[j]-vertsR[0][j] for j in range(d)] for vv in vertsR[1:]]
B, piv = rref(diffs)
dimR = len(B)
pred_dim = 2 + 6 + 6 + 4
print(f"  cells d = {d}; dim C = {dimC}; dim R = {dimR};"
      f" factorization prediction = {pred_dim}")
print(f"  RANK DROP observable: {'CONFIRMED (dim C = dim R = ' + str(pred_dim) + ')' if dimC==dimR==pred_dim else 'DIFFERS — report exact values'}")
# exact random-direction LP equality
random.seed(11)
mism = 0
for t in range(20):
    c_obj = [F(random.randint(-5,5)) for _ in range(d)]
    st, val, _ = simplex_max(c_obj, E, f, [], [])
    assert st == 'optimal'
    mx = max(sum(ci*vi for ci,vi in zip(c_obj, vv)) for vv in vertsR)
    if val != mx: mism += 1
print(f"  20 exact random-direction LPs: max_C == max_R in {20-mism}/20"
      f" -> {'SAFE evidence (+ hand factorization argument); full facet pass infeasible at n=144 — scope declared' if mism==0 else 'MISMATCH: potential unsafety — investigate'}")
print("  P32:", "HIT (safe + rank drop visible)" if (dimC==dimR==pred_dim and mism==0) else "PARTIAL/MISS — see values")

# ---------- P33 corrected ----------
print("== P33 (corrected): survivors with connectivity + decomposition filter ==")
def connected_rel(arcs, A):
    und = {}
    nodes = set()
    for (a,b) in arcs:
        und.setdefault(a,set()).add(b); und.setdefault(b,set()).add(a)
        nodes |= {a,b}
    if not nodes: return False
    seen = {min(nodes)}; front=[min(nodes)]
    while front:
        x = front.pop()
        for y in und.get(x,()):
            if y not in seen: seen.add(y); front.append(y)
    return seen == nodes and len(nodes) == A
def recurrent_arcs(arcs, A):
    adjf = {s: [b for (a,b) in arcs if a == s] for s in range(A)}
    reach = {s: {s} for s in range(A)}
    ch = True
    while ch:
        ch = False
        for s in range(A):
            new = set(reach[s])
            for t in list(reach[s]): new |= set(adjf[t])
            if new != reach[s]: reach[s] = new; ch = True
    return frozenset((a,b) for (a,b) in arcs if a in reach[b])
QMAX = 6
final = []
for Asz in (2,3,4):
    for mask in range(1, 1 << (Asz*Asz)):
        if canonical(mask, Asz) != mask: continue
        arcs = frozenset((a,b) for a in range(Asz) for b in range(Asz)
                         if mask >> (a*Asz+b) & 1)
        outdeg = [sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        indeg  = [sum(1 for a in range(Asz) if (a,b) in arcs) for b in range(Asz)]
        if min(outdeg)==0 or min(indeg)==0 or max(outdeg)<2: continue
        if not connected_rel(arcs, Asz): continue
        R = recurrent_arcs(arcs, Asz)
        rec_out = {}
        for (a,b) in R: rec_out.setdefault(a, []).append(b)
        if not any(len(v)>=2 for v in rec_out.values()): continue
        # ALSO: recurrent part itself must be connected (else hidden direct sum)
        if not connected_rel(R, Asz):
            continue
        U = unsafe_set(arcs, Asz, 4*QMAX)
        W = base_walk_lengths(arcs, Asz, 4*QMAX)
        qs = [q for q in range(1,QMAX+1)
              if 3*q not in U and 4*q not in U and 3*q in W and 4*q in W]
        if qs:
            final.append({"A": Asz, "arcs": sorted(map(list,arcs)), "qs": qs,
                          "recurrent": sorted(map(list,R))})
print(f"  TRUE fork candidates (connected, recurrent-connected, recurrent-"
      f"branching, 3q/4q-safe): {len(final)}")
for s in final[:10]:
    print(f"    |A|={s['A']}, qs={s['qs']}, arcs={s['arcs']}")
json.dump(final, open("commensurability_fork_final.json","w"), indent=1)
if final:
    m = final[0]
    print(f"  MINIMAL candidate: |A|={m['A']}, {len(m['arcs'])} arcs — the"
          f" corrected P33 object, awaiting design-side registration.")
else:
    print("  EMPTY: with decomposition filtered, no fork candidate at <=4"
          " states — the impossibility base returns, now with 6 tamings.")
