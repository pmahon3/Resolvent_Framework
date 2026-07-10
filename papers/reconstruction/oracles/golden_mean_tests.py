"""P4-P6: the golden-mean / polymorphism-transfer predictions (design session,
2026-07-07; pre-registered, scale-sanity passed — all mechanisms fit at n<=8).

P4: golden-mean length-3 variety (no-11 words; n=5) with the three coordinate
    contexts -> COMMENSURABLE (min preserves NAND).
P5: same variety PLUS an XOR-derived context (k=4) -> INCOMMENSURABLE
    (XOR graph kills the symmetric polymorphism).
P6: full cube (n=8) with only monotone-derived (AND/OR) contexts, k=3 ->
    COMMENSURABLE (min preserves monotone graphs). Robustness: all 20 triples
    from the six 2-variable AND/OR compressions.
"""
import sys
sys.path.insert(0, '.')
from itertools import product, combinations
from commensurability_harness import analyze

def coord_ctx(pts, idx, f):
    """Bipartition of pts by boolean f, as cells of indices."""
    c0 = frozenset(idx[p] for p in pts if not f(p))
    c1 = frozenset(idx[p] for p in pts if f(p))
    assert c0 and c1
    return (c0, c1)

# ---------- P4 ----------
V = [p for p in product([0,1],repeat=3) if not any(p[i]==1==p[i+1] for i in range(2))]
assert len(V) == 5
idx = {p:i for i,p in enumerate(V)}
ctxs = [coord_ctx(V, idx, lambda p,a=a: p[a]==1) for a in range(3)]
r = analyze(5, 3, ctxs)
print("P4 golden-mean coord contexts:", r['verdict'],
      "-> PASS" if r['verdict']=='R_EQUALS_C' else "-> MISS")

# ---------- P5 ----------
for (i,j) in [(0,2),(0,1),(1,2)]:
    x = coord_ctx(V, idx, lambda p,i=i,j=j: (p[i]^p[j])==1)
    r = analyze(5, 4, ctxs + [x])
    verdict = r['verdict']
    outcome = "PASS (incommensurable)" if verdict != 'R_EQUALS_C' else "MISS (commensurable)"
    print(f"P5 golden-mean + XOR(x{i+1},x{j+1}): {verdict} -> {outcome}")

# ---------- P6 ----------
cube = list(product([0,1],repeat=3))
cidx = {p:i for i,p in enumerate(cube)}
mono = {}
for (i,j) in [(0,1),(1,2),(0,2)]:
    mono[f"AND(x{i+1},x{j+1})"] = lambda p,i=i,j=j: p[i] and p[j]
    mono[f"OR(x{i+1},x{j+1})"]  = lambda p,i=i,j=j: p[i] or p[j]
names = list(mono)
misses = 0
for trio in combinations(names, 3):
    cs = [coord_ctx(cube, cidx, mono[t]) for t in trio]
    # skip degenerate protocols with duplicate contexts
    if len({tuple(sorted(tuple(sorted(cell)) for cell in c)) for c in cs}) < 3: continue
    r = analyze(8, 3, cs)
    if r['verdict'] != 'R_EQUALS_C':
        misses += 1
        print("P6 MISS:", trio, "->", r['verdict'])
print(f"P6 monotone triples: {misses} misses out of all valid triples",
      "-> PASS" if misses==0 else "-> MISS(ES) above")
