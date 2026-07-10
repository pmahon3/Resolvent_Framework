"""P29 + P30: the swap-spectrum criterion and the mechanized fork hunt
(design session, 2026-07-08/09).

Theorem-let A (operational form): L unsafe(rho) <=> for some k in [2,|A|],
some all-distinct k-tuple t reaches shift(t) in exactly L steps inside the
all-distinct k-tuple dynamics (componentwise-legal steps, every intermediate
tuple all-distinct). k=2 = swap-reachability in the off-diagonal tensor
square. NO POLYTOPES ANYWHERE.

P29 (calibration gate): the criterion must reproduce every recorded profile:
  NAND: Safe = evens (L=3..10); rho13: {3} (3..9); rho20: 6Z (2..12);
  FULL2: none; implication: all; equality: all; NE3: none (3..7).
  Plus theorem-let B check: eventual periodicity of each unsafe set (L<=40).

P30 (the hunt): exhaustive scan, mod isomorphism, totality enforced
(out-deg>=1 AND in-deg>=1 every state), over transfer digraphs on <=4
states, plus the minimally-branching 5-state slice (functional + 1 extra
arc). Fork candidate: branching AND exists q<=6 with 3q,4q both SAFE
(criterion) and both variety-realized (closed walks exist). Survivors
classified by taming-mechanism filters (deterministic / base-period parity
/ graded-singleton-fiber). Empty list = the impossibility theorem's
experimental induction base at this scale.
"""
import sys
from math import gcd
from itertools import product, permutations, combinations

def tuple_digraph(arcs, A, k):
    """Nodes: all-distinct k-tuples; arcs componentwise. Returns (nodes, adj
    bitrows)."""
    nodes = [t for t in product(range(A), repeat=k) if len(set(t)) == k]
    idx = {t: i for i, t in enumerate(nodes)}
    out = {a: [b for b in range(A) if (a, b) in arcs] for a in range(A)}
    adj = [0] * len(nodes)
    for t in nodes:
        row = 0
        for tp in product(*[out[x] for x in t]):
            if len(set(tp)) == k:
                row |= 1 << idx[tp]
        adj[idx[t]] = row
    return nodes, idx, adj

def unsafe_set(arcs, A, Lmax):
    """Unsafe lengths in 1..Lmax via shift-reachability, all k in [2,A]."""
    unsafe = set()
    for k in range(2, A + 1):
        nodes, idx, adj = tuple_digraph(arcs, A, k)
        if not nodes:
            continue
        targets = []
        for t in nodes:
            s = t[1:] + (t[0],)
            targets.append(idx[s])
        # reach[i] = bitset of nodes reachable from i in exactly L steps
        reach = [1 << i for i in range(len(nodes))]
        for L in range(1, Lmax + 1):
            reach = [0 if r == 0 else
                     _mul_row(r, adj) for r in reach]
            for i in range(len(nodes)):
                if reach[i] >> targets[i] & 1:
                    unsafe.add(L)
                    break
    return unsafe

def _mul_row(r, adj):
    out = 0
    while r:
        b = r & -r
        out |= adj[b.bit_length() - 1]
        r ^= b
    return out

def base_walk_lengths(arcs, A, Lmax):
    """Lengths L with a closed base walk (variety nonempty on ring L)."""
    M = [[1 if (a, b) in arcs else 0 for b in range(A)] for a in range(A)]
    have = set()
    P = [[1 if i == j else 0 for j in range(A)] for i in range(A)]
    for L in range(1, Lmax + 1):
        P = [[1 if any(P[i][k2] and M[k2][j] for k2 in range(A)) else 0
              for j in range(A)] for i in range(A)]
        if any(P[i][i] for i in range(A)):
            have.add(L)
    return have

def eventual_period(unsafe, Lmax):
    for p in range(1, 13):
        for start in range(1, Lmax - 2 * p):
            if all((L in unsafe) == ((L + p) in unsafe)
                   for L in range(start, Lmax - p + 1)):
                return start, p
    return None, None

# ---------------- P29 ----------------
LANGS = {
 "NAND":    (frozenset({(0,0),(0,1),(1,0)}), 2),
 "rho13":   (frozenset({(0,0),(0,1),(1,2),(2,0)}), 3),
 "rho20":   (frozenset({(0,1),(1,0),(2,3),(3,4),(4,2)}), 5),
 "FULL2":   (frozenset({(0,0),(0,1),(1,0),(1,1)}), 2),
 "implication": (frozenset({(0,0),(0,1),(1,1)}), 2),
 "equality":    (frozenset({(0,0),(1,1)}), 2),
 "NE3":     (frozenset((a,b) for a in range(3) for b in range(3) if a != b), 3),
}
EXPECT = {   # recorded profiles on their tested ranges
 "NAND":    lambda L: L % 2 == 1,            # unsafe = odd,  range 3..10
 "rho13":   lambda L: L != 3,                # range 3..9
 "rho20":   lambda L: L % 6 != 0,            # range 2..12
 "FULL2":   lambda L: True,                  # range 3..8
 "implication": lambda L: False,             # all safe
 "equality":    lambda L: False,
 "NE3":     lambda L: True,                  # range 3..7
}
RANGES = {"NAND": range(3,11), "rho13": range(3,10), "rho20": range(2,13),
          "FULL2": range(3,9), "implication": range(3,9), "equality": range(3,9),
          "NE3": range(3,8)}
print("== P29: swap-spectrum criterion vs recorded profiles ==")
p29_ok = True
for name, (arcs, A) in LANGS.items():
    U = unsafe_set(arcs, A, 40)
    ok = all((L in U) == EXPECT[name](L) for L in RANGES[name])
    st, per = eventual_period(U, 40)
    print(f"  {name}: match on recorded range = {ok};"
          f" eventual period (from L={st}) = {per};"
          f" unsafe within 1..14 = {sorted(L for L in U if L <= 14)}")
    p29_ok = p29_ok and ok
print("  P29:", "HIT — criterion reproduces every profile, polytope-free"
      if p29_ok else "MISS — theorem-let A needs its bookkeeping revisited")
if not p29_ok:
    sys.exit(1)

# ---------------- P30 ----------------
print("== P30: exhaustive fork hunt ==")
QMAX = 6
def analyze_digraph(arcs, A):
    outdeg = [sum(1 for b in range(A) if (a,b) in arcs) for a in range(A)]
    indeg  = [sum(1 for a in range(A) if (a,b) in arcs) for b in range(A)]
    if min(outdeg) == 0 or min(indeg) == 0:
        return None                     # totality
    branching = max(outdeg) >= 2
    if not branching:
        return None                     # fork needs nondeterminism
    Lneed = 4 * QMAX
    U = unsafe_set(arcs, A, Lneed)
    W = base_walk_lengths(arcs, A, Lneed)
    for q in range(1, QMAX + 1):
        if (3*q not in U) and (4*q not in U) and (3*q in W) and (4*q in W):
            return ('CANDIDATE', q)
    return None

def classify_taming(arcs, A):
    outdeg = [sum(1 for b in range(A) if (a,b) in arcs) for a in range(A)]
    tags = []
    if max(outdeg) == 1: tags.append('deterministic')
    # base period (gcd of closed-walk lengths through each SCC)
    W = base_walk_lengths(arcs, A, 24)
    if W:
        g = 0
        for L in W: g = gcd(g, L)
        if g >= 2: tags.append(f'graded-d{g}')
    return tags or ['unclassified']

def canonical(mask, A):
    best = mask
    for perm in permutations(range(A)):
        m2 = 0
        for a in range(A):
            for b in range(A):
                if mask >> (a*A+b) & 1:
                    m2 |= 1 << (perm[a]*A + perm[b])
        if m2 < best: best = m2
    return best

found = []
tested = 0
for A in (2, 3, 4):
    for mask in range(1, 1 << (A*A)):
        if canonical(mask, A) != mask:
            continue
        arcs = frozenset((a,b) for a in range(A) for b in range(A)
                         if mask >> (a*A+b) & 1)
        r = analyze_digraph(arcs, A)
        tested += 1
        if r:
            found.append((A, sorted(arcs), r[1], classify_taming(arcs, A)))
    print(f"  |A|={A}: exhaustive (canonical, total, branching) done;"
          f" candidates so far: {len(found)}")
# 5-state minimally-branching slice: functional + 1 extra arc
slice_found = 0
seen5 = set()
for f5 in product(range(5), repeat=5):
    base = frozenset((a, f5[a]) for a in range(5))
    for extra in product(range(5), repeat=2):
        if extra in base: continue
        arcs = base | {extra}
        key = frozenset(arcs)
        if key in seen5: continue
        seen5.add(key)
        r = analyze_digraph(arcs, 5)
        if r:
            found.append((5, sorted(arcs), r[1], classify_taming(arcs, 5)))
            slice_found += 1
print(f"  |A|=5 minimally-branching slice (functional+1): done;"
      f" slice candidates: {slice_found}")
print(f"== P30 RESULT: {len(found)} fork candidates ==")
for (A, arcs, q, tags) in found[:20]:
    print(f"  |A|={A}, q={q}, tags={tags}, arcs={arcs}")
if not found:
    print("  CERTIFIED EMPTY at this scope: exhaustive <=4 states +"
          " minimally-branching 5-state slice — the impossibility theorem's"
          " experimental induction base.")
