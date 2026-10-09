"""Census for the open half of L-B (bar-D aperiodicity), per strongly connected
component of bar-D.

bar-D: vertices = unordered pairs {a,b}, a != b; arc {a,b} -> {c,d} for every
ordered arc (a,b) -> (c,d) of D = (rho (x) rho) off the diagonal; monodromy m = 0
if the arc keeps the sheet (ascending frame), 1 if it flips it.  For each SCC H
that carries a closed walk we compute
  period(H)     = gcd of closed-walk lengths in H,
  G_H           = image of closed walks in Z2 x Z2 under (length, monodromy).
The aperiodic half of L-B asks: primitive rho  =>  no H with a crossed closed walk
(odd monodromy) is periodic.  Hand claim under test (2026-10-09): if bar-D is
strongly connected then it is aperiodic (chase walks on simple cycles of length
c >= 2 give length c; a loop at v plus a simple cycle through v of length c >= 3
gives a delay walk of length c + 1; c = 2 gives a length-1 swap).
See notes/joint2_wielandt_finding.md (section of 2026-10-09)."""
import itertools, sys
from math import gcd

def primitive(rel, A):
    M = [[1 if (a, b) in rel else 0 for b in range(A)] for a in range(A)]
    P = [row[:] for row in M]
    for _ in range((A - 1) ** 2 + 1):          # Wielandt bound
        if all(all(r) for r in P): return True
        P = [[1 if any(P[i][k] and M[k][j] for k in range(A)) else 0 for j in range(A)] for i in range(A)]
    return all(all(r) for r in P)

def barD(rel, A):
    V = [frozenset(p) for p in itertools.combinations(range(A), 2)]
    asc = lambda P: tuple(sorted(P))
    arcs = []
    for a in range(A):
        for b in range(A):
            if a == b: continue
            for c in range(A):
                if (a, c) not in rel: continue
                for d in range(A):
                    if c == d or (b, d) not in rel: continue
                    P, Q = frozenset((a, b)), frozenset((c, d))
                    m = (0 if (a, b) == asc(P) else 1) ^ (0 if (c, d) == asc(Q) else 1)
                    arcs.append((P, Q, m))
    return V, arcs

def sccs(V, arcs):
    out = {v: [] for v in V}; inn = {v: [] for v in V}
    for P, Q, _ in arcs: out[P].append(Q); inn[Q].append(P)
    def reach(s, g):
        seen = {s}; st = [s]
        while st:
            x = st.pop()
            for y in g[x]:
                if y not in seen: seen.add(y); st.append(y)
        return seen
    comps, done = [], set()
    for v in V:
        if v in done: continue
        C = reach(v, out) & reach(v, inn); done |= C; comps.append(C)
    return comps

def comp_invariants(C, arcs):
    """period and G for an SCC via a (length, monodromy) potential."""
    inner = [(P, Q, m) for P, Q, m in arcs if P in C and Q in C]
    if not inner: return None
    root = next(iter(C)); pot = {root: (0, 0)}; st = [root]
    out = {}
    for P, Q, m in inner: out.setdefault(P, []).append((Q, m))
    while st:
        x = st.pop()
        for y, m in out.get(x, []):
            if y not in pot: pot[y] = (pot[x][0] + 1, pot[x][1] ^ m); st.append(y)
    g, gens = 0, set()
    for P, Q, m in inner:                       # each arc closes a cycle element
        dl = pot[P][0] + 1 - pot[Q][0]; g = gcd(g, abs(dl))
        gens.add((dl % 2, pot[P][1] ^ m ^ pot[Q][1]))
    G = {(0, 0)}
    for _ in range(3):
        G |= {((x[0] + y[0]) % 2, x[1] ^ y[1]) for x in G for y in gens | G}
    return g, frozenset(G)

def simple_cycles(rel, A):
    """All simple directed cycles of rho, as vertex lists (rotation-canonical)."""
    out = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    cyc = []
    def dfs(start, cur, path, seen):
        for nx in out[cur]:
            if nx == start: cyc.append(path[:])
            elif nx > start and nx not in seen:
                seen.add(nx); path.append(nx); dfs(start, nx, path, seen); path.pop(); seen.discard(nx)
    for s0 in range(A): dfs(s0, s0, [s0], {s0})
    return cyc

def check_walk(rel, w1, w2):
    """Two synchronous token walks: valid rho-steps, never colliding, closing in D
    (same ordered pair) or crossing (swapped pair). Returns (length, closes_in_bar_D)."""
    assert len(w1) == len(w2)
    for t in range(len(w1) - 1):
        assert (w1[t], w1[t + 1]) in rel and (w2[t], w2[t + 1]) in rel, "illegal step"
    assert all(x != y for x, y in zip(w1, w2)), "touches the diagonal"
    assert {w1[-1], w2[-1]} == {w1[0], w2[0]}, "not closed in bar-D"
    return len(w1) - 1

def argument_walks(rel, A):
    """The hand argument's walks: (start pair, length) for each construction."""
    walks = []
    cycles = simple_cycles(rel, A)
    for C in cycles:
        c = len(C)
        if c < 2: continue
        for j in range(1, c):                                  # chase walk, length c
            w1 = [C[t % c] for t in range(c + 1)]; w2 = [C[(j + t) % c] for t in range(c + 1)]
            walks.append((frozenset((C[0], C[j])), check_walk(rel, w1, w2), 'chase'))
        if c == 2:                                             # swap, length 1
            walks.append((frozenset(C), check_walk(rel, [C[0], C[1]], [C[1], C[0]]), 'swap'))
    loops = [v for v in range(A) if (v, v) in rel]
    for v in loops:
        for C in cycles:
            if len(C) < 3 or v not in C: continue
            k = C.index(v); C = C[k:] + C[:k]; c = len(C)
            for j in range(1, c - 1):                          # delay walk, length c + 1
                w1 = [C[0], C[0]] + [C[t % c] for t in range(1, c + 1)]   # waits at v first
                w2 = [C[j]]; pos = j; waited = False
                for _ in range(c + 1):
                    if pos % c == 0 and not waited and len(w2) > 1: waited = True
                    else: pos += 1
                    w2.append(C[pos % c])
                walks.append((frozenset((C[0], C[j])), check_walk(rel, w1, w2), 'delay'))
    return walks

def census(A, exhaustive=True):
    allp = [(a, b) for a in range(A) for b in range(A)]
    stats = dict(prim=0, sc=0, sc_aperiodic=0, disc=0, bad=0, one_cyc_scc=0, diag=0, full=0, odd_no_cross_multi=0)
    bad_examples = []
    for mask in range(1 << len(allp)):
        rel = frozenset(p for i, p in enumerate(allp) if mask >> i & 1)
        if not primitive(rel, A): continue
        stats['prim'] += 1
        V, arcs = barD(rel, A)
        comps = [C for C in sccs(V, arcs) if comp_invariants(C, arcs)]
        if len(comps) == 1 and len(comps[0]) == len(V):
            stats['sc'] += 1
            per, G = comp_invariants(comps[0], arcs)
            stats['sc_aperiodic'] += (per == 1)
        else:
            stats['disc'] += 1
        # the argument's own walks: valid, diagonal-free, closed (asserted), and their
        # lengths have gcd 1 inside a single SCC whenever only one SCC carries cycles
        W = argument_walks(rel, A)
        if len(comps) == 1:
            stats['one_cyc_scc'] += 1
            g = 0
            for P, L, _ in W:
                assert P in comps[0]; g = gcd(g, L)
            assert g == 1, (sorted(rel), W)
            per, G = comp_invariants(comps[0], arcs)
            stats['diag'] += G == frozenset({(0, 0), (1, 1)}); stats['full'] += len(G) == 4
        for C in comps:
            per, G = comp_invariants(C, arcs)
            if not any(x[1] == 1 for x in G) and any(x[0] == 1 for x in G) and len(comps) > 1:
                stats['odd_no_cross_multi'] += 1
            crossed = any(x[1] == 1 for x in G)
            if crossed and per != 1:
                stats['bad'] += 1
                if len(bad_examples) < 5: bad_examples.append((sorted(rel), sorted(map(sorted, C)), per, sorted(G)))
    return stats, bad_examples

def main():
  for A in (2, 3, 4):
    s, ex = census(A)
    print(f"A={A}: primitive={s['prim']}  bar-D s.c.={s['sc']} (aperiodic {s['sc_aperiodic']})  "
          f"bar-D not s.c.={s['disc']}  periodic SCC carrying a crossed walk={s['bad']}")
    print(f"      one cycle-carrying SCC={s['one_cyc_scc']} (argument walks asserted, gcd 1; "
          f"G diagonal {s['diag']}, full {s['full']})  "
          f"multi-SCC with an odd-no-crossed SCC={s['odd_no_cross_multi']}")
    for e in ex: print("   example:", e)

# --- A = 5: random sample (2^25 relations is too many to enumerate) ---
import random
def sample(A, n, seed=11):
    random.seed(seed); allp = [(a, b) for a in range(A) for b in range(A)]
    seen = cnt = multi = bad = 0
    while cnt < n:
        rel = frozenset(p for p in allp if random.random() < random.choice((0.2, 0.3, 0.45)))
        if not primitive(rel, A): continue
        cnt += 1
        V, arcs = barD(rel, A)
        comps = [C for C in sccs(V, arcs) if comp_invariants(C, arcs)]
        multi += len(comps) > 1
        for C in comps:
            per, G = comp_invariants(C, arcs)
            bad += any(x[1] == 1 for x in G) and per != 1
        if len(comps) == 1:
            g = 0
            for P, L, _ in argument_walks(rel, A):
                assert P in comps[0]; g = gcd(g, L)
            assert g == 1
    print(f"A={A} sample: primitive={cnt}  >1 cycle-carrying SCC={multi}  periodic crossed SCC={bad}")

# --- Cycle lemma (2026-10-09): chases on ONE simple cycle C form one aperiodic SCC ---
# Moves: a token on C takes an excursion e (walk x_i -> x_i' whose interior avoids C;
# loops and chords included) while the other token stays on C.  Interior vertices
# avoid C, so the only possible collision is at the landing vertex.  Offset
# j = pos2 - pos1 (mod c) changes by +defect (token 1 moves) or -defect (token 2),
# defect = len(e) - ((i' - i) mod c).  Claim: the defects generate Z_c, so the
# offsets Z_c minus {0} are connected (2-connectivity of connected Cayley graphs of
# degree >= 2), and the closed walks so obtained have gcd-1 lengths.
def excursions(rel, A, C, bound):
    onC = set(C); idx = {v: i for i, v in enumerate(C)}; c = len(C)
    out = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    ex = []
    for x in C:
        frontier = [[x]]
        for _ in range(bound):
            nxt = []
            for w in frontier:
                for y in out[w[-1]]:
                    if y in onC:
                        if not (len(w) == 1 and idx[y] == (idx[x] + 1) % c):   # skip C's own arc
                            ex.append(w + [y])
                    else:
                        nxt.append(w + [y])
            frontier = nxt
    return ex

def apply_move(rel, C, j, e, mover):
    """Build the token walks for one excursion move from chase offset j; assert legality
    and no collision; return the new offset (or None if it would land on the other token)."""
    c = len(C); idx = {v: i for i, v in enumerate(C)}
    i0, i1, L = idx[e[0]], idx[e[-1]], len(e) - 1
    # mover sits at x_{i0} at time 0; the other token sits at offset +j (mover=1) or -j
    other0 = (i0 + j) % c if mover == 1 else (i0 - j) % c
    other = [C[(other0 + t) % c] for t in range(L + 1)]
    if other[-1] == e[-1]: return None
    for t in range(L):
        assert (e[t], e[t + 1]) in rel and (other[t], other[t + 1]) in rel
    assert all(a != b for a, b in zip(e, other))
    land = idx[other[-1]] - i1
    return land % c if mover == 1 else (-land) % c

def cycle_lemma_check():
    from math import gcd
    for A in (2, 3, 4):
        allp = [(a, b) for a in range(A) for b in range(A)]
        n_cyc = 0
        for mask in range(1 << len(allp)):
            rel = frozenset(p for i, p in enumerate(allp) if mask >> i & 1)
            if not primitive(rel, A): continue
            for C in simple_cycles(rel, A):
                c = len(C)
                if c < 2: continue
                n_cyc += 1
                ex = excursions(rel, A, C, bound=2 * A)
                defects = {(len(e) - 1 - ((C.index(e[-1]) - C.index(e[0])) % c)) % c for e in ex}
                g = c
                for d in defects: g = gcd(g, d)
                assert g == 1, (sorted(rel), C, defects)           # defects generate Z_c
                # offset graph built from actual constructed moves
                adj = {j: set() for j in range(1, c)}
                for j in range(1, c):
                    for e in ex:
                        for mover in (1, 2):
                            k = apply_move(rel, C, j, e, mover)
                            if k is not None:
                                assert k != 0; adj[j].add(k)
                seen = {1}; st = [1]
                while st:
                    x = st.pop()
                    for y in adj[x]:
                        if y not in seen: seen.add(y); st.append(y)
                assert seen == set(range(1, c)), (sorted(rel), C, adj)  # offsets connected
        print(f"A={A}: {n_cyc} (language, simple cycle) pairs: defects generate Z_c and "
              "constructed moves connect every offset")

if __name__ == "__main__":
    if '--sample5' in sys.argv: sample(5, 4000)
    elif '--cycle-lemma' in sys.argv: cycle_lemma_check()
    else: main()
