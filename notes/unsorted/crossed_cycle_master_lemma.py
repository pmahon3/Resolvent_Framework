"""
MASTER-LEMMA oracle for the crossed-cycle exclusion (2026-07-10, session 4).

HAND-DERIVED CLAIMS UNDER TEST (independent re-impl throughout; advisor down):

  MASTER LEMMA (token-riding): if G has a closed walk W of even length 2m with
  W(t) != W(t+m) for all t in [0,m], then the pair (W(0), W(m)) reaches
  (W(m), W(0)) in the off-diagonal pair digraph D: token1 rides W(t),
  token2 rides W(t+m), t = 0..m. Each step is a D-arc; the antipodal
  condition is exactly off-diagonality. => crossed cycle.

  COR 1: even simple cycle => crossed (antipodal tokens).
  COR L: a loop (1-cycle) in a strongly connected G with n>=2 => crossed
         (loop + shortest cycle >=2 through its vertex: even => Cor 1;
          odd q>=3 => W = loop . C, shares exactly one vertex, 1 != q).
  COR 2: two odd simple cycles, lengths p != q, sharing exactly one vertex,
         based there: W = C1 . C2 works (only clash channel is an
         "index-locked" shared vertex C1(t) = C2(t + (q-p)/2), absent here).

  PREDICTIONS on every NO-CROSS language (falsifiers for the hand proof):
    P1: no loops.
    P2: all simple cycles have ODD length.
    P3: no "working walk" exists in the candidate family (soundness:
        working walk => crossed; a working walk in a no-cross lang = BUG).

  COVERAGE question (guides the remaining case analysis): among PRIMITIVE
  langs, what fraction are explained by the candidate family
  (single even cycle / two cycles at a shared base / two disjoint cycles
  joined by shortest paths, small lap counts)? Residuals printed.

Conventions match crossed_cycle_exclusion.py: rel = set of ordered pairs.
"""
import itertools, sys, random
from math import gcd
from collections import deque

# ---------- basic graph utils (fresh implementations) ----------

def adj_out(rel, A):
    return {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}

def is_total(rel, A):
    return ({a for a, b in rel} == set(range(A))
            and {b for a, b in rel} == set(range(A)))

def strongly_conn(rel, A):
    out = adj_out(rel, A)
    inn = {a: [b for b in range(A) if (b, a) in rel] for a in range(A)}
    def reach(g):
        seen = {0}; dq = deque([0])
        while dq:
            x = dq.popleft()
            for y in g[x]:
                if y not in seen:
                    seen.add(y); dq.append(y)
        return seen
    return reach(out) == set(range(A)) and reach(inn) == set(range(A))

def period(rel, A):
    out = adj_out(rel, A)
    lvl = {0: 0}; dq = deque([0])
    while dq:
        x = dq.popleft()
        for y in out[x]:
            if y not in lvl:
                lvl[y] = lvl[x] + 1; dq.append(y)
    g = 0
    for a in range(A):
        for b in out[a]:
            g = gcd(g, abs(lvl[a] + 1 - lvl[b]))
    return g if g > 0 else 1

# ---------- independent crossed-cycle oracle (fresh BFS) ----------

def has_crossed_cycle(rel, A):
    for a in range(A):
        for b in range(a + 1, A):
            seen = {(a, b)}; dq = deque([(a, b)])
            hit = False
            while dq and not hit:
                x, y = dq.popleft()
                for c in range(A):
                    if (x, c) not in rel:
                        continue
                    for d in range(A):
                        if c != d and (y, d) in rel:
                            if (c, d) == (b, a):
                                hit = True; break
                            if (c, d) not in seen:
                                seen.add((c, d)); dq.append((c, d))
                    if hit:
                        break
            if hit:
                return True
    return False

# ---------- simple cycle enumeration (min-vertex canonical) ----------

def simple_cycles(rel, A):
    """All simple directed cycles, as vertex lists [v0..v_{p-1}] (arcs vi->vi+1,
    last->first). Loops appear as [v]."""
    out = adj_out(rel, A)
    cycles = []
    for s in range(A):
        stack = [(s, [s], {s})]
        while stack:
            v, path, seen = stack.pop()
            for w in out[v]:
                if w == s:
                    cycles.append(path[:])
                elif w > s and w not in seen:
                    stack.append((w, path + [w], seen | {w}))
    return cycles

# ---------- Master Lemma machinery ----------

def walk_arcs_ok(W, rel):
    return all((W[i], W[i + 1]) in rel for i in range(len(W) - 1))

def walk_works(W):
    """W = closed walk as vertex list with W[0]==W[-1]; length L=len(W)-1.
    True iff L even and W[t] != W[t+m] for all t in [0,m]."""
    L = len(W) - 1
    if L % 2 != 0 or L == 0:
        return False
    m = L // 2
    return all(W[t] != W[t + m] for t in range(m + 1))

def verify_swap_path(W, rel, A):
    """Machine-check of the Master Lemma on a working walk: the explicit
    token path is a D-path from (W0,Wm) to (Wm,W0). Returns True or raises."""
    L = len(W) - 1; m = L // 2
    pairs = [(W[t], W[t + m]) for t in range(m + 1)]
    assert pairs[0] == (W[0], W[m]) and pairs[-1] == (W[m], W[0])
    for (x, y) in pairs:
        assert x != y, "token collision - Master Lemma proof is WRONG"
    for (x, y), (c, d) in zip(pairs, pairs[1:]):
        assert (x, c) in rel and (y, d) in rel, "not a D-arc - proof WRONG"
    return True

def rotate(C, x):
    i = C.index(x)
    return C[i:] + C[:i]

def shortest_path(rel, A, srcs, dsts):
    """Shortest path (vertex list) from any of srcs to any of dsts; interior
    avoids nothing in particular (BFS). None if unreachable."""
    out = adj_out(rel, A)
    dq = deque((s, [s]) for s in srcs)
    seen = set(srcs)
    while dq:
        v, path = dq.popleft()
        if v in dsts:
            return path
        for w in out[v]:
            if w not in seen:
                seen.add(w); dq.append((w, path + [w]))
    return None

def candidate_walks(rel, A, max_laps=3):
    """Yield candidate closed walks: single cycles (even), two cycles at each
    shared basepoint with lap counts, and disjoint cycle pairs joined by
    shortest paths."""
    cycles = simple_cycles(rel, A)
    for C in cycles:
        if len(C) % 2 == 0:
            yield C + [C[0]]
    for Ci, Cj in itertools.permutations(cycles, 2):
        p, q = len(Ci), len(Cj)
        shared = set(Ci) & set(Cj)
        if shared:
            for x in shared:
                Ri, Rj = rotate(Ci, x), rotate(Cj, x)
                for a in range(1, max_laps + 1):
                    for b in range(1, max_laps + 1):
                        if (a * p + b * q) % 2 == 0:
                            yield Ri * a + Rj * b + [x]
        else:
            P1 = shortest_path(rel, A, set(Ci), set(Cj))
            if P1 is None:
                continue
            u, v = P1[0], P1[-1]
            P2 = shortest_path(rel, A, {v}, {u})
            if P2 is None:
                continue
            Ru, Rv = rotate(Ci, u), rotate(Cj, v)
            s = (len(P1) - 1) + (len(P2) - 1)
            for a in range(1, max_laps + 1):
                for b in range(1, max_laps + 1):
                    if (a * p + b * q + s) % 2 == 0:
                        # u ... (laps of Ci) ... u -P1-> v ... (laps of Cj) ... v -P2-> u
                        yield Ru * a + P1 + (Rv * b)[1:] + P2

def explained(rel, A, max_laps=3):
    """Return a working candidate walk (Master-Lemma certificate), or None."""
    for W in candidate_walks(rel, A, max_laps):
        assert walk_arcs_ok(W, rel), "candidate walk broken (bug in generator)"
        if walk_works(W):
            verify_swap_path(W, rel, A)
            return W
    return None

# ---------- the EQUIVALENCE (converse direction) ----------

def crossed_pair_walk(rel, A):
    """If crossed, return the pair walk (x_0,y_0)..(x_m,y_m) with x_0=a,y_0=b,
    x_m=b,y_m=a via BFS parents; else None."""
    for a in range(A):
        for b in range(a + 1, A):
            par = {(a, b): None}; dq = deque([(a, b)])
            while dq:
                x, y = dq.popleft()
                for c in range(A):
                    if (x, c) not in rel:
                        continue
                    for d in range(A):
                        if c != d and (y, d) in rel and (c, d) not in par:
                            par[(c, d)] = (x, y)
                            if (c, d) == (b, a):
                                path = [(b, a)]
                                while par[path[-1]] is not None:
                                    path.append(par[path[-1]])
                                return path[::-1]
                            dq.append((c, d))
    return None

def check_equivalence(rel, A):
    """crossed  <=>  exists antipodal-free even closed walk. Forward: build W
    from the D-path and assert walk_works (converse-direction machine check).
    Backward is the Master Lemma (checked via verify_swap_path elsewhere)."""
    pw = crossed_pair_walk(rel, A)
    if pw is None:
        return False  # no-cross; Master Lemma direction checked by explained()==None
    W = [x for x, y in pw] + [y for x, y in pw][1:]
    # W = x_0..x_m then y_1..y_m; y_m = a = x_0, so closed, even length 2m
    assert walk_arcs_ok(W, rel), "converse construction broken: not a walk"
    assert walk_works(W), "converse construction broken: antipodal coincidence"
    return True

def sweep_equivalence(A, limit=None):
    n = 0
    for rel in all_sc_langs(A):
        cc = has_crossed_cycle(rel, A)
        assert check_equivalence(rel, A) == cc
        n += 1
        if limit and n >= limit:
            break
    print(f"A={A}: equivalence crossed <=> antipodal-free even closed walk "
          f"machine-checked on {n} langs")

# ---------- sweeps ----------

def all_sc_langs(A):
    allp = [(a, b) for a in range(A) for b in range(A)]
    for m in range(A, len(allp) + 1):
        for combo in itertools.combinations(allp, m):
            rel = frozenset(combo)
            if is_total(rel, A) and strongly_conn(rel, A):
                yield rel

def sweep_full(A):
    n = prim = prim_expl = 0
    nocross = []
    residual = []
    for rel in all_sc_langs(A):
        n += 1
        cc = has_crossed_cycle(rel, A)
        if not cc:
            nocross.append(rel)
            # P3 soundness: a working walk here = contradiction = bug
            W = explained(rel, A)
            assert W is None, f"WORKING WALK IN NO-CROSS LANG (BUG): {sorted(rel)} {W}"
            continue
        if period(rel, A) == 1:
            prim += 1
            if explained(rel, A) is not None:
                prim_expl += 1
            else:
                residual.append(rel)
    print(f"A={A}: {n} s.c. total langs, {len(nocross)} no-cross, "
          f"{prim} primitive, explained {prim_expl}/{prim}, "
          f"residual {len(residual)}")
    # P1/P2 on no-cross
    bad = 0
    for rel in nocross:
        cyc = simple_cycles(rel, A)
        loops = [C for C in cyc if len(C) == 1]
        evens = [C for C in cyc if len(C) % 2 == 0]
        if loops or evens:
            bad += 1
            print(f"  PREDICTION FAILED (no-cross with loop/even cycle): "
                  f"{sorted(rel)} loops={loops} evens={evens}")
    print(f"  no-cross predictions P1+P2: {'ALL HOLD' if bad == 0 else f'{bad} FAIL'}")
    for rel in residual[:6]:
        cyc = sorted(len(C) for C in simple_cycles(rel, A))
        print(f"  RESIDUAL primitive unexplained: cycles={cyc} rel={sorted(rel)}")
    return residual

def sample_langs(A, trials, rng):
    allp = [(a, b) for a in range(A) for b in range(A)]
    seen = set()
    for _ in range(trials):
        k = rng.randint(A, min(len(allp), 3 * A))
        rel = frozenset(rng.sample(allp, k))
        if rel in seen or not is_total(rel, A) or not strongly_conn(rel, A):
            continue
        seen.add(rel)
        yield rel

def sweep_sample(A, trials=40000, seed=7):
    rng = random.Random(seed)
    n = prim = prim_expl = 0
    nocross = []
    residual = []
    for rel in sample_langs(A, trials, rng):
        n += 1
        cc = has_crossed_cycle(rel, A)
        if not cc:
            nocross.append(rel)
            W = explained(rel, A)
            assert W is None, f"WORKING WALK IN NO-CROSS LANG (BUG): {sorted(rel)} {W}"
            continue
        if period(rel, A) == 1:
            prim += 1
            if explained(rel, A) is not None:
                prim_expl += 1
            else:
                residual.append(rel)
    print(f"A={A} SAMPLE: {n} distinct s.c. langs, {len(nocross)} no-cross, "
          f"{prim} primitive, explained {prim_expl}/{prim}, residual {len(residual)}")
    bad = 0
    for rel in nocross:
        cyc = simple_cycles(rel, A)
        if any(len(C) == 1 for C in cyc) or any(len(C) % 2 == 0 for C in cyc):
            bad += 1
            print(f"  PREDICTION FAILED on no-cross: {sorted(rel)}")
    print(f"  no-cross predictions P1+P2 ({len(nocross)} langs): "
          f"{'ALL HOLD' if bad == 0 else f'{bad} FAIL'}")
    for rel in residual[:6]:
        cyc = sorted(len(C) for C in simple_cycles(rel, A))
        print(f"  RESIDUAL primitive unexplained: cycles={cyc} rel={sorted(rel)}")
    return residual

def sweep_period3_n6(trials=30000, seed=11):
    """Hunt no-cross langs at n=6 via period-3-graded random graphs; test the
    even-cycle prediction where it first has teeth (a 6-cycle fits)."""
    rng = random.Random(seed)
    A = 6
    found = 0; bad = 0; with_even = 0
    seen = set()
    sizes_list = [(2, 2, 2), (3, 2, 1), (4, 1, 1), (2, 3, 1), (1, 2, 3)]
    for _ in range(trials):
        sizes = rng.choice(sizes_list)
        classes = []
        i = 0
        for s in sizes:
            classes.append(list(range(i, i + s))); i += s
        rel = set()
        for k in range(3):
            src, dst = classes[k], classes[(k + 1) % 3]
            for a in src:
                for b in rng.sample(dst, rng.randint(1, len(dst))):
                    rel.add((a, b))
        rel = frozenset(rel)
        if rel in seen or not is_total(rel, A) or not strongly_conn(rel, A):
            continue
        seen.add(rel)
        if has_crossed_cycle(rel, A):
            continue
        found += 1
        cyc = simple_cycles(rel, A)
        evens = [C for C in cyc if len(C) % 2 == 0]
        loops = [C for C in cyc if len(C) == 1]
        if evens:
            with_even += 1
        if evens or loops:
            bad += 1
            print(f"  n=6 PREDICTION FAILED: no-cross with evens={evens} "
                  f"loops={loops} rel={sorted(rel)}")
        W = explained(rel, A)
        assert W is None, f"WORKING WALK IN NO-CROSS LANG (BUG): {sorted(rel)}"
    print(f"n=6 period-3 hunt: {len(seen)} distinct graphs, {found} no-cross, "
          f"predictions {'ALL HOLD' if bad == 0 else f'{bad} FAIL'} "
          f"(no-cross with an even simple cycle: {with_even})")

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "3"):
        sweep_full(3)
    if which in ("all", "4"):
        sweep_full(4)
    if which in ("all", "5"):
        sweep_sample(5)
    if which in ("all", "6"):
        sweep_period3_n6()
    if which in ("all", "eq"):
        sweep_equivalence(3)
        sweep_equivalence(4, limit=4000)
    print("DONE")
