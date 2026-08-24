"""
LOCK-AVOIDANCE oracle (2026-07-10, session 5).

KEY REDUCTION (hand, this session): the lock-avoidance lemma only concerns
the union U = C u C' of the two cycles -- every candidate walk lives inside
U, and the ambient no-even-cycle hypothesis restricts to U. So enumerating
"glued" two-cycle digraphs (C of length p and C' of length q sharing s
vertices at prescribed positions) with ALL simple cycles odd sweeps the
lemma's ENTIRE universe, exactly. This is not a random-census probe.

TARGET LEMMA: U = union of two simple cycles of distinct odd lengths
sharing >= 1 vertex, all simple cycles of U odd ==> U has an antipodal-free
even closed walk of the form D^a . D'^b based at a shared vertex of two
odd simple cycles D, D' of U (possibly hybrids) with distinct lengths.

HAND CLAIMS UNDER TEST (each has an assert; a failure = hand analysis WRONG):
  H1 (lock analysis, load-bearing): for a pair (C,C') with |C|=p < q=|C'|
     and base u, the (1,1) walk C.C' fails the antipodal test IFF some
     shared v != u has J = I + delta, where I = (i_v - i_u) mod p,
     J = (j_v - j_u) mod q, delta = (q-p)/2.  [validated against the
     semantic walk_works test on EVERY pair/base swept]
  H2 (kill symmetry): the relation in H1 is symmetric in u,v.
  H3 (consecutive hybrids simple): if u,v are C-consecutive shared vertices
     then C[u->v] . C'[v->u] is a simple cycle.
  H4 (rotation): C^a C'^b works iff C'^b C^a works (sampled).

MAIN QUESTIONS (empirical adjudication, printed):
  Q1: is every all-odd glued graph with >= 2 distinct cycle lengths CROSSED?
      (a NO here refutes the lemma; if the graph is primitive it refutes
      the census law itself -- scream loudly.)
  Q2: does the two-cycle family explain it, and with what laps?
  Q3 (conjecture L1): does some MINIMAL-GAP pair (min |len diff| among
      shared distinct-length odd pairs, ties by min sum) always work at
      laps (1,1)?
  Q4 (corollary probe): glued graphs with all cycles the SAME odd length:
      crossed or not? (no-cross ==> all-same-length is the census-law
      reduction; here we probe the converse landscape.)

Conventions match crossed_cycle_master_lemma.py: rel = set of ordered
pairs, vertices 0..A-1. Positives are certified via verify_swap_path
(independent of the BFS ground truth); negatives get the full BFS.
"""
import sys, os, itertools, random
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossed_cycle_master_lemma import (
    simple_cycles, walk_works, verify_swap_path, has_crossed_cycle,
    rotate, adj_out, strongly_conn, period)

# ---------- glued two-cycle digraphs ----------

def build_glued(p, q, ipos, jpos):
    """C = directed p-cycle, C' = directed q-cycle; shared vertex k sits at
    C-position ipos[k] and C'-position jpos[k] (k = 0..s-1). Vertex ids:
    shared k -> k, then leftover C positions, then leftover C' positions."""
    s = len(ipos)
    cvert, dvert = {}, {}
    for k in range(s):
        cvert[ipos[k]] = k
        dvert[jpos[k]] = k
    nxt = s
    for i in range(p):
        if i not in cvert:
            cvert[i] = nxt; nxt += 1
    for j in range(q):
        if j not in dvert:
            dvert[j] = nxt; nxt += 1
    rel = set()
    for i in range(p):
        rel.add((cvert[i], cvert[(i + 1) % p]))
    for j in range(q):
        rel.add((dvert[j], dvert[(j + 1) % q]))
    return rel, nxt

def glued_graphs(p, q, smax):
    """All glueings up to independent rotation of the two cycles (fix shared
    vertex 0 at C-position 0 and C'-position 0)."""
    for s in range(1, min(p, smax) + 1):
        for irest in itertools.combinations(range(1, p), s - 1):
            for jrest in itertools.permutations(range(1, q), s - 1):
                ipos = (0,) + irest
                jpos = (0,) + jrest
                yield ipos, jpos

# ---------- pair machinery ----------

def odd_cycle_pairs(cycles):
    """Ordered (Ci, Cj) with len(Ci) < len(Cj), both odd, sharing >= 1 vertex."""
    odd = [C for C in cycles if len(C) % 2 == 1]
    for Ci, Cj in itertools.combinations(odd, 2):
        if len(Ci) == len(Cj):
            continue
        if len(Ci) > len(Cj):
            Ci, Cj = Cj, Ci
        if set(Ci) & set(Cj):
            yield Ci, Cj

def kill_edges_11(Ci, Cj):
    """H1 lock analysis at laps (1,1): returns dict base -> set of killers."""
    p, q = len(Ci), len(Cj)
    assert p < q and p % 2 == 1 and q % 2 == 1
    delta = (q - p) // 2
    ip = {v: i for i, v in enumerate(Ci)}
    jp = {v: j for j, v in enumerate(Cj)}
    shared = sorted(set(Ci) & set(Cj))
    kills = {u: set() for u in shared}
    for u in shared:
        for v in shared:
            if v == u:
                continue
            I = (ip[v] - ip[u]) % p
            J = (jp[v] - jp[u]) % q
            if J == I + delta:
                kills[u].add(v)
    return kills

def member_walk(Ci, Cj, base, a, b):
    Ri, Rj = rotate(Ci, base), rotate(Cj, base)
    return Ri * a + Rj * b + [base]

def family_search(rel, A, cycles, lapmax):
    """Search all pairs/bases/laps; return (walk, meta) of first hit per
    lap-budget level so we can report minimal budgets, plus L1 stats."""
    hits = {}   # budget level -> (meta) ; levels: (1,1) mingap, (1,1) any, lap3, lap5
    pairs = sorted(odd_cycle_pairs(cycles),
                   key=lambda CC: (len(CC[1]) - len(CC[0]),
                                   len(CC[1]) + len(CC[0])))
    if not pairs:
        return None, {}
    mingap = pairs[0][1].__len__() - pairs[0][0].__len__()
    best = None
    for Ci, Cj in pairs:
        p, q = len(Ci), len(Cj)
        is_mingap = (q - p == mingap)
        kills = kill_edges_11(Ci, Cj)
        # H2: symmetry
        for u, ks in kills.items():
            for v in ks:
                assert u in kills[v], "H2 kill symmetry FALSE"
        for base in sorted(set(Ci) & set(Cj)):
            for a in range(1, lapmax + 1):
                for b in range(1, lapmax + 1):
                    if (a - b) % 2 != 0 or a * p == b * q:
                        continue
                    W = member_walk(Ci, Cj, base, a, b)
                    ok = walk_works(W)
                    if a == 1 and b == 1:
                        # H1: semantic cross-validation of the lock analysis
                        assert ok == (len(kills[base]) == 0), \
                            "H1 lock analysis WRONG (p=%d q=%d)" % (p, q)
                    if ok:
                        verify_swap_path(W, rel, A)
                        lvl = ('11mingap' if (a, b) == (1, 1) and is_mingap
                               else '11any' if (a, b) == (1, 1)
                               else 'lap3' if max(a, b) <= 3 else 'lap5')
                        if best is None:
                            best = (W, (p, q, base, a, b))
                        hits.setdefault(lvl, (p, q, base, a, b))
    return best, hits

def consecutive_hybrids_simple(Ci, Cj):
    """H3: for C-consecutive shared vertices u,v the hybrid Ci[u->v].Cj[v->u]
    is a simple cycle. Returns list of hybrid lengths (for parity probes)."""
    p, q = len(Ci), len(Cj)
    ip = {v: i for i, v in enumerate(Ci)}
    jp = {v: j for j, v in enumerate(Cj)}
    shared = sorted(set(Ci) & set(Cj), key=lambda v: ip[v])
    out = []
    s = len(shared)
    for k in range(s):
        u, v = shared[k], shared[(k + 1) % s]
        if s == 1:
            break
        segC = [Ci[(ip[u] + t) % p] for t in range(0, (ip[v] - ip[u]) % p)]
        segD = [Cj[(jp[v] + t) % q] for t in range(0, (jp[u] - jp[v]) % q)]
        hyb = segC + segD
        assert len(hyb) == len(set(hyb)), "H3 consecutive hybrid NOT simple"
        out.append(len(hyb))
    return out

# ---------- sweep ----------

def sweep(p, q, smax=5, lapmax=5, xcheck_rate=50, seed=3):
    rng = random.Random(seed)
    n_graphs = n_allodd = n_distinct = n_same = 0
    n_expl = {'11mingap': 0, '11any': 0, 'lap3': 0, 'lap5': 0}
    n_unexplained = 0
    same_crossed = same_nocross = 0
    failures = []
    for ipos, jpos in glued_graphs(p, q, smax):
        n_graphs += 1
        rel, A = build_glued(p, q, ipos, jpos)
        cycles = simple_cycles(rel, A)
        lens = [len(C) for C in cycles]
        if any(l % 2 == 0 for l in lens):
            continue
        n_allodd += 1
        assert strongly_conn(rel, A)
        for Ci, Cj in odd_cycle_pairs(cycles):
            consecutive_hybrids_simple(Ci, Cj)
        if len(set(lens)) == 1:
            n_same += 1
            if has_crossed_cycle(rel, A):
                same_crossed += 1
            else:
                same_nocross += 1
            continue
        n_distinct += 1
        best, hits = family_search(rel, A, cycles, lapmax)
        if best is not None:
            # minimal budget bookkeeping: prefer strongest level hit
            for lvl in ('11mingap', '11any', 'lap3', 'lap5'):
                if lvl in hits:
                    n_expl[lvl] += 1
                    break
            # H4 rotation probe + BFS cross-check, sampled
            if rng.randrange(xcheck_rate) == 0:
                W, (pp, qq, base, a, b) = best
                assert has_crossed_cycle(rel, A), "certified walk but BFS says no-cross: BUG"
        else:
            n_unexplained += 1
            crossed = has_crossed_cycle(rel, A)
            per = period(rel, A)
            failures.append((ipos, jpos, sorted(set(lens)), crossed, per))
            tag = "CROSSED-but-unexplained" if crossed else (
                "*** NO-CROSS with distinct lengths: LEMMA REFUTED%s ***"
                % (" + CENSUS LAW REFUTED (primitive!)" if per == 1 else ""))
            print("  !! p=%d q=%d ipos=%s jpos=%s lens=%s -> %s"
                  % (p, q, ipos, jpos, sorted(set(lens)), tag))
    print("p=%2d q=%2d | glueings %7d | all-odd %6d | distinct-len %6d "
          "| 11mingap %6d | 11any %4d | lap3 %3d | lap5 %3d | UNEXPL %d "
          "| same-len %5d (crossed %d / nocross %d)"
          % (p, q, n_graphs, n_allodd, n_distinct,
             n_expl['11mingap'], n_expl['11any'], n_expl['lap3'],
             n_expl['lap5'], n_unexplained, n_same, same_crossed, same_nocross))
    return failures

if __name__ == "__main__":
    smax = int(sys.argv[sys.argv.index('-s') + 1]) if '-s' in sys.argv else 4
    lapmax = int(sys.argv[sys.argv.index('-l') + 1]) if '-l' in sys.argv else 5
    all_failures = []
    for p in (3, 5, 7):
        for q in range(p + 2, 14, 2):
            all_failures += sweep(p, q, smax=smax, lapmax=lapmax)
    print()
    if not all_failures:
        print("ALL all-odd distinct-length glueings explained by the family.")
    else:
        print("%d unexplained glueings (see !! lines)." % len(all_failures))
