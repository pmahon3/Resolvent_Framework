"""
Probe for the missing lemma (M) of the lock-avoidance proof (session 5).

(M): in an all-odd union U, if pair (D,D') with |D|=p < q=|D'| is killed at
EVERY base at laps (1,1), then some ordered kill (u,v) has a SIMPLE hybrid
H1(u,v) = D[u->v] . D'[v->u]  (length m = (p+q)/2, hand-proved identity).

Consequences being tested alongside:
  P(a): a failing pair with delta = (q-p)/2 ODD never occurs in all-odd U
        (its simple hybrid would be an EVEN simple cycle, contradiction).
  P(b): a failing pair with delta EVEN has a simple hybrid = new ODD simple
        cycle of length m, giving the shared pair (D, H1) with gap delta
        < 2 delta  -->  the descent step.

Sweeps the same glued universe as lock_avoidance_lemma.py.
"""
import sys, os, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossed_cycle_master_lemma import simple_cycles, walk_works
from lock_avoidance_lemma import (build_glued, glued_graphs, odd_cycle_pairs,
                                  kill_edges_11)

def hybrid(Ci, Cj, u, v):
    """H1(u,v): Ci-segment u->v then Cj-segment v->u, as vertex list
    (closed, last == first). Returns (walk, simple?)."""
    p, q = len(Ci), len(Cj)
    ip = {x: i for i, x in enumerate(Ci)}
    jp = {x: j for j, x in enumerate(Cj)}
    segC = [Ci[(ip[u] + t) % p] for t in range(0, (ip[v] - ip[u]) % p)]
    segD = [Cj[(jp[v] + t) % q] for t in range(0, (jp[u] - jp[v]) % q)]
    W = segC + segD
    return W + [u], len(W) == len(set(W))

def main(smax=4):
    n_failing_pairs = 0
    n_delta_odd_failing = 0
    n_M_violations = 0
    m_len_checked = 0
    for p in (3, 5, 7):
        for q in range(p + 2, 14, 2):
            for ipos, jpos in glued_graphs(p, q, smax):
                rel, A = build_glued(p, q, ipos, jpos)
                cycles = simple_cycles(rel, A)
                if any(len(C) % 2 == 0 for C in cycles):
                    continue
                for Ci, Cj in odd_cycle_pairs(cycles):
                    kills = kill_edges_11(Ci, Cj)
                    if any(len(ks) == 0 for ks in kills.values()):
                        continue  # pair has a free base: not a failing pair
                    n_failing_pairs += 1
                    pp, qq = len(Ci), len(Cj)
                    delta = (qq - pp) // 2
                    m = (pp + qq) // 2
                    if delta % 2 == 1:
                        n_delta_odd_failing += 1
                        print("P(a) VIOLATION: delta odd failing pair "
                              "p=%d q=%d (glue p=%d q=%d %s %s)"
                              % (pp, qq, p, q, ipos, jpos))
                    found_simple = False
                    for u, ks in kills.items():
                        for v in ks:
                            W, simp = hybrid(Ci, Cj, u, v)
                            assert len(W) - 1 == m, "hybrid length != m: hand identity WRONG"
                            m_len_checked += 1
                            if simp:
                                found_simple = True
                    if not found_simple:
                        n_M_violations += 1
                        print("(M) VIOLATION: p=%d q=%d all-bases-killed, "
                              "no kill edge with simple hybrid "
                              "(glue p=%d q=%d ipos=%s jpos=%s)"
                              % (pp, qq, p, q, ipos, jpos))
    print("failing pairs: %d | delta-odd failing: %d | (M) violations: %d "
          "| hybrid-length identity checked %d times, 0 failures"
          % (n_failing_pairs, n_delta_odd_failing, n_M_violations,
             m_len_checked))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
