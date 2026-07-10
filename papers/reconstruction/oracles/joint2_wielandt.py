"""
Joint 2 of universal impossibility, retargeted per advisor.

Claim to test: grading (taming 4 = transfer digraph fibered over Z_d) IS
Perron-Frobenius imprimitivity (period d = gcd of cycle lengths of a strongly
connected digraph). If so, step (2) "residue-structured unsafe => grading" is
classical, and the difficulty relocates to step (1):

  REAL PROBE (Wielandt shape): does a PRIMITIVE (period-1) strongly connected
  non-symmetric transfer digraph exist that is SAFE at a RICH length set?
  Per Wielandt / Perron-Frobenius it should NOT: a primitive digraph has, past the
  Wielandt index, walks of EVERY length between any pair => it should force
  frustration (winding-2 simple cycles) at cofinitely many L => NOT rich-safe.

  A HIT (primitive + rich-safe) refutes the conjecture.
  A MISS (every primitive strongly-connected non-symmetric lang is unsafe
  cofinitely) is the proof shape: safe-at-rich => imprimitive => graded.

We use LISC2 (raw simple winding-2 cycle) as the unsafe oracle (ground truth),
restricted to the residence class.
"""
import itertools
from math import gcd
from functools import reduce

# ---------- digraph period (Perron-Frobenius) ----------
def digraph_period(rel, A):
    """Period of a strongly connected digraph = gcd of all cycle lengths.
    Compute via BFS distances: gcd of (d[u]+1 - d[v]) over edges u->v from a root,
    standard. Returns 0 if not strongly connected (undefined period)."""
    out = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    # strong-connectivity check
    def reach(start, graph):
        seen = {start}; st = [start]
        while st:
            x = st.pop()
            for y in graph[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        return seen
    inn = {a: [b for b in range(A) if (b, a) in rel] for a in range(A)}
    if reach(0, out) != set(range(A)) or reach(0, inn) != set(range(A)):
        return 0  # not strongly connected
    # BFS levels from 0; period = gcd over edges of (level[u]+1-level[v])
    level = {0: 0}; st = [0]; g = 0
    # do a full BFS assigning levels (first-seen), then scan all edges
    from collections import deque
    dq = deque([0])
    while dq:
        x = dq.popleft()
        for y in out[x]:
            if y not in level:
                level[y] = level[x] + 1; dq.append(y)
    for a in range(A):
        for b in out[a]:
            g = gcd(g, abs(level[a] + 1 - level[b]))
    return g if g > 0 else 1  # g=0 means acyclic-ish; strongly conn => at least 1


def is_graded(rel, A, d):
    """Fibered over Z_d: exists labelling phi: states -> Z_d with every arc a->b
    having phi(b) = phi(a)+1 mod d. Test by BFS consistency."""
    if d < 2:
        return False
    out = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    phi = {}
    for s in range(A):
        if s in phi:
            continue
        phi[s] = 0
        st = [s]
        while st:
            x = st.pop()
            for y in out[x]:
                want = (phi[x] + 1) % d
                if y in phi:
                    if phi[y] != want:
                        return False
                else:
                    phi[y] = want; st.append(y)
    return True


# ---------- unsafe oracle ----------
def lisc2_raw(rel, A, L):
    adj = {(i, s): [((i + 1) % L, t) for t in range(A) if (s, t) in rel]
           for i in range(L) for s in range(A)}
    lc = [0] * L
    import sys; sys.setrecursionlimit(10**7)
    def dfs(start, cur, steps, vis):
        if steps == 2 * L: return cur == start
        for nx in adj[cur]:
            ni, ns = nx
            if nx == start and steps + 1 == 2 * L: return True
            if nx not in vis and lc[ni] < 2:
                vis.add(nx); lc[ni] += 1
                if dfs(start, nx, steps + 1, vis): lc[ni] -= 1; vis.discard(nx); return True
                lc[ni] -= 1; vis.discard(nx)
        return False
    for s0 in range(A):
        lc[0] = 1
        if dfs((0, s0), (0, s0), 0, {(0, s0)}): lc[0] = 0; return True
        lc[0] = 0
    return False


def is_symmetric(rel):
    return all((b, a) in rel for (a, b) in rel)

def is_strongly_connected(rel, A):
    return digraph_period(rel, A) != 0

def is_total(rel, A):
    """every state has an out-arc and an in-arc (recurrent-branching-ish floor)"""
    outs = {a for (a, b) in rel}; ins = {b for (a, b) in rel}
    return outs == set(range(A)) and ins == set(range(A))


# ---------- (I) verify grading == imprimitivity on examples ----------
print("=== (I) grading (fibered Z_d) == PF period d ? ===")
examples = {
    "graded-d2 (rho13 base)": {(0,1),(0,2),(1,0),(2,0)},
    "pure 3-cycle": {(0,1),(1,2),(2,0)},
    "2-cycle": {(0,1),(1,0)},
    "primitive (loop+cycle)": {(0,0),(0,1),(1,0)},  # golden-mean: period 1 (has loop)
    "full2": {(0,0),(0,1),(1,0),(1,1)},
}
for name, rel in examples.items():
    rel = frozenset(rel); A = 1 + max(max(a,b) for (a,b) in rel)
    p = digraph_period(rel, A)
    graded_at_p = is_graded(rel, A, p) if p >= 2 else False
    # also: is it graded at ANY d>=2?
    graded_any = any(is_graded(rel, A, d) for d in range(2, A+1))
    print(f"  {name:26} period={p}  graded@period={graded_at_p}  graded@any-d={graded_any}")

# ---------- (II) the Wielandt probe: primitive + rich-safe ? ----------
print("\n=== (II) PRIMITIVE strongly-connected non-symmetric langs: safe at rich set? ===")
print("    (rich = safe at >=3 lengths in [3..Lmax]; a HIT would refute the conjecture)")
Lmax = 9
richness_thresh = 3
hits = []
count_primitive = 0
for A in [2, 3]:
    all_pairs = [(a, b) for a in range(A) for b in range(A)]
    # enumerate relations (nonempty), filter to residence class
    for r in range(1, 1 << len(all_pairs)):
        rel = frozenset(all_pairs[i] for i in range(len(all_pairs)) if r >> i & 1)
        if not is_total(rel, A): continue
        if is_symmetric(rel): continue
        p = digraph_period(rel, A)
        if p != 1: continue  # want PRIMITIVE (period 1), strongly connected
        count_primitive += 1
        safe_lengths = [L for L in range(3, Lmax+1) if not lisc2_raw(rel, A, L)]
        if len(safe_lengths) >= richness_thresh:
            hits.append((A, sorted(rel), safe_lengths))
print(f"    scanned {count_primitive} primitive strongly-conn non-symmetric total langs (A<=3)")
if hits:
    print(f"    ⚠ {len(hits)} PRIMITIVE-BUT-RICH-SAFE candidates (potential fork!):")
    for A, rel, safe in hits[:12]:
        print(f"      A={A} rel={rel} safe@{safe}")
else:
    print("    MISS: every primitive strongly-conn non-symmetric lang is unsafe at "
          f">= {Lmax-2-richness_thresh+1} of L=3..{Lmax} — consistent with Wielandt/proof shape")
