"""
Probe for the SUM-DESCENT step of the lock-avoidance proof (session 5).

Claim under test (replaces the refuted gap-descent (M)/P(a)):

  DESCENT: in an all-odd union U, if pair (D,D') (p < q) is killed at every
  base at (1,1), then U contains a shared distinct-length odd pair with
  p'+q' < p+q, obtained from ANY kill-edge hybrid H (closed walk, length
  m=(p+q)/2) as follows:
    case 1  H simple: m odd forced (m even would be an even simple cycle);
            pair (D, H), sum p+m < p+q.
    case 2a H non-simple, decomposition has cycles of >= 2 distinct lengths:
            some two cycles with distinct lengths share a vertex
            (decomposition intersection graph is connected).
    case 2b all decomposition cycles same length e != p: some cycle E covers
            a D-arc of H, so (E, D) is a shared pair, sum e+p < p+q.
    case 2c all same length e == p: THE POTENTIAL STALL (forces
            q = (2k-1)p). Does it ever occur? If yes, is there still a
            smaller-sum shared pair in U?

Machine-checks on every failing pair in the glued universe: hybrid length
identity, decomposition validity (each piece a simple cycle of rel, all
odd), and existence of the descent pair. Prints any 2c hits and any
DESCENT failures loudly.
"""
import sys, os, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossed_cycle_master_lemma import simple_cycles
from lock_avoidance_lemma import (build_glued, glued_graphs, odd_cycle_pairs,
                                  kill_edges_11)
from lock_avoidance_probe_M import hybrid

def decompose(W, rel):
    """Peel a closed walk (W[0]==W[-1]) into simple cycles covering its
    arc multiset. Returns list of vertex lists."""
    stack, pos, cycles = [], {}, []
    for v in W[:-1]:
        if v in pos:
            k = pos[v]
            cyc = stack[k:]
            for x in cyc:
                del pos[x]
            stack = stack[:k]
            cycles.append(cyc)
        pos[v] = len(stack)
        stack.append(v)
    cycles.append(stack)
    for cyc in cycles:
        assert len(cyc) == len(set(cyc)) and len(cyc) >= 2, "bad piece"
        for i in range(len(cyc)):
            assert (cyc[i], cyc[(i + 1) % len(cyc)]) in rel, "piece not in rel"
    return cycles

def main(smax=4):
    n_failing = n_case1 = n_case2a = n_case2b = n_case2c = 0
    n_descent_fail = 0
    for p in (3, 5, 7):
        for q in range(p + 2, 14, 2):
            for ipos, jpos in glued_graphs(p, q, smax):
                rel, A = build_glued(p, q, ipos, jpos)
                cycles = simple_cycles(rel, A)
                if any(len(C) % 2 == 0 for C in cycles):
                    continue
                for Ci, Cj in odd_cycle_pairs(cycles):
                    kills = kill_edges_11(Ci, Cj)
                    if any(not ks for ks in kills.values()):
                        continue
                    n_failing += 1
                    pp, qq = len(Ci), len(Cj)
                    m = (pp + qq) // 2
                    descent_found_somewhere = False
                    for u in sorted(kills):
                        for v in sorted(kills[u]):
                            W, simp = hybrid(Ci, Cj, u, v)
                            assert len(W) - 1 == m
                            if simp:
                                assert m % 2 == 1, "even simple cycle in all-odd U!"
                                n_case1 += 1
                                descent_found_somewhere = True
                                continue
                            pieces = decompose(W, rel)
                            lens = [len(E) for E in pieces]
                            assert all(l % 2 == 1 for l in lens), \
                                "even piece in all-odd U (impossible)"
                            assert sum(lens) == m and len(pieces) >= 2
                            if len(set(lens)) > 1:
                                n_case2a += 1
                                ok = any(
                                    len(E1) != len(E2) and set(E1) & set(E2)
                                    for E1, E2 in
                                    itertools.combinations(pieces, 2))
                                if not ok:
                                    print("2a: no adjacent distinct pair "
                                          "INSIDE decomposition; checking D/D'")
                                    ok = any(len(E) != pp and set(E) & set(Ci)
                                             for E in pieces) or \
                                         any(len(E) != qq and set(E) & set(Cj)
                                             for E in pieces)
                                assert ok, "case 2a descent pair MISSING"
                                descent_found_somewhere = True
                            else:
                                e = lens[0]
                                if e != pp:
                                    n_case2b += 1
                                    assert any(set(E) & set(Ci) for E in pieces), \
                                        "case 2b: no piece shares with D"
                                    descent_found_somewhere = True
                                else:
                                    n_case2c += 1
                                    print("case 2c HIT: p=%d q=%d glue "
                                          "p=%d q=%d ipos=%s jpos=%s "
                                          "(q=(2k-1)p, k=%d)"
                                          % (pp, qq, p, q, ipos, jpos,
                                             m // e))
                    if not descent_found_somewhere:
                        n_descent_fail += 1
                        print("DESCENT FAIL: p=%d q=%d glue p=%d q=%d "
                              "ipos=%s jpos=%s" % (pp, qq, p, q, ipos, jpos))
    print("failing pairs %d | case1(simple,m odd) %d | 2a %d | 2b %d "
          "| 2c(STALL) %d | descent failures %d"
          % (n_failing, n_case1, n_case2a, n_case2b, n_case2c,
             n_descent_fail))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
