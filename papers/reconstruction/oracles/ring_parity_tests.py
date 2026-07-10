"""Ring-parity verification round (design session handoff, 2026-07-07).

Golden-mean world (NAND on adjacent coordinates), SCOPE contexts (full edge-
window partitions of the variety). Structure = ring C_L; variety = independent
sets of C_L.

- P4' (instance of the free theorem): PATH of length 3 (acyclic structure),
  scope contexts {x1x2},{x2x3} -> commensurable (R = C).
- C3, C5 (odd rings): INcommensurable — machine-confirm the hand proofs, plus
  exact certificates for the half-model (mass 1/2 on (0,1) and (1,0) per edge):
  scope-coherent, unrealisable. C3 counting: legal configs have <= 1 one, model
  forces E[#1s] = 3/2. C5: model support needs a proper 2-coloring of an odd
  cycle. [Design paste said '>= 2 on triangle-legal'; correct bound is <= 1 —
  conclusion unchanged.]
- P7 (pre-registered, OPEN): C4 commensurable — all local-polytope vertices
  realisable (R = C).
- P8 (pre-registered): C6 commensurable; if it holds the parity-theorem proof
  attempt is warranted.
"""
import sys, time
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product
from commensurability_harness import analyze

def ring_variety(L):
    return [p for p in product([0,1],repeat=L)
            if not any(p[i]==1==p[(i+1)%L] for i in range(L))]

def path_variety(L):
    return [p for p in product([0,1],repeat=L)
            if not any(p[i]==1==p[i+1] for i in range(L-1))]

def scope_contexts(V, scopes):
    idx = {p:i for i,p in enumerate(V)}
    ctxs = []
    for S in scopes:
        cells = {}
        for p in V:
            key = tuple(p[i] for i in S)
            cells.setdefault(key, set()).add(idx[p])
        ctxs.append(tuple(frozenset(c) for c in cells.values()))
    return ctxs

# ---------- P4': path, acyclic ----------
V = path_variety(3)
r = analyze(len(V), 2, scope_contexts(V, [(0,1),(1,2)]))
print(f"P4' path-3 scope contexts: {r['verdict']} ->",
      "PASS (free theorem instance)" if r['verdict']=='R_EQUALS_C' else "MISS")

# ---------- odd rings: C3, C5 ----------
for L in (3, 5):
    V = ring_variety(L)
    scopes = [(i,(i+1)%L) for i in range(L)]
    r = analyze(len(V), L, scope_contexts(V, scopes))
    ok = r['verdict'] != 'R_EQUALS_C'
    print(f"C{L} (odd, n={len(V)}): {r['verdict']} ->",
          "CONFIRMED incommensurable" if ok else "REFUTES hand proof (!)")
    # direct certificate for the half-model: E[#1s] under any realising measure
    # legal configs on odd ring have <= floor(L/2) ones; model forces sum of
    # vertex marginals = L/2 > floor(L/2).
    max_ones = max(sum(p) for p in V)
    assert max_ones == L//2
    print(f"   certificate: model E[#1s] = {L}/2 > alpha(C{L}) = {L//2} on legal configs")

# ---------- P7: C4 ----------
V = ring_variety(4)
t0 = time.time()
r = analyze(len(V), 4, scope_contexts(V, [(i,(i+1)%4) for i in range(4)]))
print(f"P7 C4 (n={len(V)}): {r['verdict']} ({time.time()-t0:.0f}s) ->",
      "PASS (commensurable)" if r['verdict']=='R_EQUALS_C' else "MISS: " + r['verdict'])

if len(sys.argv) > 1 and sys.argv[1] == 'small':
    sys.exit(0)
# ---------- P8: C6 ----------
V = ring_variety(6)
t0 = time.time()
r = analyze(len(V), 6, scope_contexts(V, [(i,(i+1)%6) for i in range(6)]))
print(f"P8 C6 (n={len(V)}): {r['verdict']} ({time.time()-t0:.0f}s) ->",
      "PASS (commensurable)" if r['verdict']=='R_EQUALS_C' else "MISS: " + r['verdict'])
