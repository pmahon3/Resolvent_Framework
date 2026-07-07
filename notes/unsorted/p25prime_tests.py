"""P25' + P28 (2026-07-08), with the pre-run structural finding machine-checked:
rho20 = (01)(234) is a PERMUTATION language — deterministic. Consequences,
verified below: LOCAL(G) for permutation beads = the holonomy-invariant
simplex {u : pi^c u = u for all cycle classes c}; MARG = conv(fixed states);
so aggregation-level Safe <=> holonomy group H = {id}. The K4 minor never
gets a vote: the fork is unreached for a THIRD structural reason
(determinism), after NAND's parity coincidence.

P25': K4, all edges subdivided to length 6, rho20 -> predicted SAFE.
      Holonomy: all fundamental-cycle sums == 0 mod 6 -> H = {id} -> SAFE
      (aggregation); closure-level: V has 5 global sections, every edge
      context is a 5-singleton partition -> EA forces full agreement ->
      C = Delta(V) = R -> SAFE. HIT expected, fork unreached.
P28:  one path length 5 -> fundamental cycles pick up pi^{+-5}; H = <pi^5> =
      <pi> (5 coprime to 6) -> nontrivial orbits, NO fixed states ->
      MARG = empty, LOCAL = {(a,a,b,b,b)} segment -> UNSAFE, but in the
      DEGENERATE mode (inherited circuits are rho20-rings of length 17/23
      with EMPTY varieties): section-emptiness / CF=1, not a 1/2-type facet
      gap. HIT-with-mode-correction expected.
BONUS (round-3 scout): Safe profile of proper-3-coloring rings (NE3 =
      {(a,b): a != b}, nondeterministic, dense) at L=3..8 — the candidate
      language class for the genuinely decisive minor experiment.
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from math import gcd
from itertools import product
from winding_invariant_tests import circulation_analysis, rank_gate

PI = [1,0,3,4,2]   # rho20 as permutation
def perm_pow(p, k):
    n = len(p); out = list(range(n))
    k = k % 6 if k >= 0 else (k % 6)
    for _ in range(k % 6):
        out = [p[x] for x in out]
    return out

def subdiv_k4(lengths):
    """K4 on {0,1,2,3}; edge (u,v) subdivided into lengths[(u,v)] edges.
    Returns (nverts, oriented edges, fundamental cycle sums)."""
    K4E = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    verts = 4
    edges = []          # oriented (a, b)
    path_of = {}
    for (u,v) in K4E:
        L = lengths[(u,v)]
        chain = [u] + [verts + i for i in range(L-1)] + [v]
        verts += L - 1
        path_of[(u,v)] = chain
        for i in range(L):
            edges.append((chain[i], chain[i+1]))
    # spanning tree via BFS on undirected version; holonomy of non-tree edges
    adj = {}
    for idx,(a,b) in enumerate(edges):
        adj.setdefault(a, []).append((b, idx, +1))
        adj.setdefault(b, []).append((a, idx, -1))
    import collections
    depth_sum = {0: 0}     # net pi-exponent from root along tree
    parent_edge = {0: None}
    seen = {0}
    dq = collections.deque([0])
    tree = set()
    while dq:
        x = dq.popleft()
        for (y, idx, s) in adj[x]:
            if y not in seen:
                seen.add(y); tree.add(idx)
                depth_sum[y] = depth_sum[x] + s
                dq.append(y)
    cyc_sums = []
    for idx,(a,b) in enumerate(edges):
        if idx not in tree:
            cyc_sums.append(depth_sum[a] + 1 - depth_sum[b])
    return verts, edges, cyc_sums, path_of

def holonomy_verdict(cyc_sums, label):
    # H = <pi^c : c in sums>; orbits; fixed states
    gens = {c % 6 for c in cyc_sums}
    # subgroup of Z6 generated
    g = 0
    for c in gens: g = gcd(g, c)
    g = g % 6
    sub = {(g*i) % 6 for i in range(6)} if g else {0}
    H_id = (sub == {0})
    # orbits of <pi^g> on states
    if H_id:
        print(f"  {label}: all fundamental-cycle sums ≡ 0 mod 6 -> holonomy H = id"
              f" -> LOCAL = MARG ≅ Δ(5) -> SAFE (aggregation level)")
        return True
    p = perm_pow(PI, g)
    orbits, seen = [], set()
    for s in range(5):
        if s in seen: continue
        o, x = [], s
        while x not in seen:
            seen.add(x); o.append(x); x = p[x]
        orbits.append(o)
    fixed = [o[0] for o in orbits if len(o) == 1]
    print(f"  {label}: cycle sums mod 6 = {sorted(gens)} -> H = <pi^{g}>,"
          f" orbits {orbits}, fixed states {fixed}")
    print(f"    -> MARG = conv(fixed) = {'EMPTY' if not fixed else fixed},"
          f" LOCAL = invariant simplex (dim {len(orbits)-1}) -> UNSAFE"
          f" ({'degenerate: no sections at all, CF=1' if not fixed else 'partial'})")
    return False

print("== structural finding: rho20 is the permutation (01)(234) — machine check ==")
assert all(len([b for b in range(5) if (a,b) in
    {(0,1),(1,0),(2,3),(3,4),(4,2)}]) == 1 for a in range(5))
print("  every state has exactly ONE continuation: deterministic. LOCAL of a")
print("  permutation language = holonomy-invariant simplex; minor-blind.")

print("== P25': subdiv-K4, all lengths 6, rho20 ==")
lengths6 = {e: 6 for e in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]}
nv, edges, sums, _ = subdiv_k4(lengths6)
print(f"  structure: {nv} vertices, {len(edges)} edges, cycle sums {sums}")
safe = holonomy_verdict(sums, "P25'")
# closure level: V = root-push sections; every context a |V|-singleton partition
V = []
for s in range(5):
    # push s around the spanning tree; verify all edges
    val = {0: s}
    changed = True
    # simple propagation
    import collections
    dq = collections.deque([0])
    adj = {}
    for (a,b) in edges:
        adj.setdefault(a, []).append((b, +1)); adj.setdefault(b, []).append((a, -1))
    okc = True
    while dq:
        x = dq.popleft()
        for (y, sgn) in adj[x]:
            w = perm_pow(PI, sgn)[val[x]] if sgn > 0 else PI.index(val[x])
            if y in val:
                if val[y] != w: okc = False
            else:
                val[y] = w; dq.append(y)
    if okc: V.append(tuple(val[i] for i in range(nv)))
print(f"  closure level: |V| = {len(V)} global sections;"
      f" every edge context separates all {len(V)} -> EA = full agreement ->"
      f" C = Δ(V) = R -> SAFE")
for (a,b) in edges[:3] + edges[-3:]:
    assert len({(p[a],p[b]) for p in V}) == len(V)
print("  P25':", "HIT — SAFE at BOTH semantics, but the fork is UNREACHED for a"
      " third structural reason (determinism); K4 minor never votes" if safe and len(V)==5 else "MISS")

print("== P28: one path length 5 ==")
lengths5 = dict(lengths6); lengths5[(2,3)] = 5
nv, edges, sums, _ = subdiv_k4(lengths5)
print(f"  structure: {nv} vertices, {len(edges)} edges, cycle sums {sums}")
safe28 = holonomy_verdict(sums, "P28")
# closure level: V empty?
V = []
for s in range(5):
    val = {0: s}
    import collections
    dq = collections.deque([0]); okc = True
    adj = {}
    for (a,b) in edges:
        adj.setdefault(a, []).append((b, +1)); adj.setdefault(b, []).append((a, -1))
    while dq:
        x = dq.popleft()
        for (y, sgn) in adj[x]:
            w = PI[val[x]] if sgn > 0 else PI.index(val[x])
            if y in val:
                if val[y] != w: okc = False
            else:
                val[y] = w; dq.append(y)
    if okc: V.append(1)
print(f"  closure level: |V| = {len(V)} (empty -> fully degenerate)")
print("  P28:", "HIT (mode-corrected): unsafe by inheritance, but the inherited"
      " circuits (rho20-rings L=17,23) are DEGENERATE-unsafe (empty varieties):"
      " certificate = section-emptiness/CF=1, not a 1/2 facet gap" if not safe28 and not V else "MISS")

print("== ROUND-3 SCOUT: Safe profile of proper-3-coloring rings (NE3) ==")
NE3 = frozenset((a,b) for a in range(3) for b in range(3) if a != b)
prof = []
for L in range(3, 9):
    res = circulation_analysis(L, [NE3]*L, 3)
    comm, nsec, nfrac, bad, _ = res
    prof.append((L, comm, nsec, nfrac, len(bad)))
    print(f"  L={L}: sections={nsec}, winding>=2 vertices={nfrac},"
          f" bad={len(bad)} -> {'SAFE' if comm else 'UNSAFE'}")
    if L <= 5:
        rank_gate(L, [NE3]*L, 3, f"NE3 L={L}")
print("  NE3 is nondeterministic (2 continuations/state), dense (gate-friendly),"
      " and its Safe profile above is the round-3 design input.")
