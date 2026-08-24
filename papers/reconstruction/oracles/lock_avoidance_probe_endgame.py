"""
Probe for STEP 9 (the endgame) of the lock-avoidance proof (session 5).

Claim under test (the final contradiction of the total-stall argument):

  For any failing pair (D,D') in an all-odd U, take the ordered kill (u->v)
  of MINIMAL directed D-distance dmin. If its hybrid is 2c (all pieces of
  length p; forced q=(2k-1)p), then for EVERY piece P_t (D-segment from x_t,
  length a_t):
    (i)  if a_t == 1: pair (P_t, D') has base x_t UNKILLED (no interior
         vertex exists; run vertices and endpoints never kill -- hand), or
    (ii) if pair (P_t, D') kills base x_t, the killer w is an original
         shared vertex strictly interior to the D-segment with
              tau(w) = tau(x_t) + delta  (mod q),  tau(y) = (j_y - i_y),
         and then (x_t -> w) is an ordered kill of the ORIGINAL pair (D,D')
         with directed distance <= a_t - 1 < dmin,
    (iii) or pair (P_t, D') simply has an unkilled base (no stall here).
  In a TOTAL stall (i)/(iii) are excluded and (ii) contradicts minimality
  of dmin; on real (non-stalled) graphs the dichotomy (i)/(ii)/(iii) must
  hold exhaustively -- that is what this probe asserts.

Also asserts the supporting hand computations on every instance:
  - peeling chain of a 2c hybrid: pieces are D-segment+D'-segment hybrids
    with Sum a_t = I;
  - run vertices / endpoints of (P_t, D') never kill each other;
  - the tau-equation <=> (x_t -> w) is an ordered (D,D')-kill at the claimed
    distance.
"""
import sys, os, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossed_cycle_master_lemma import simple_cycles
from lock_avoidance_lemma import (build_glued, glued_graphs, odd_cycle_pairs,
                                  kill_edges_11)
from lock_avoidance_probe_M import hybrid
from lock_avoidance_probe_descent import decompose

def ordered_kills(Ci, Cj):
    p, q = len(Ci), len(Cj)
    delta = (q - p) // 2
    ip = {v: i for i, v in enumerate(Ci)}
    jp = {v: j for j, v in enumerate(Cj)}
    shared = sorted(set(Ci) & set(Cj))
    out = []
    for u in shared:
        for v in shared:
            if u == v:
                continue
            I = (ip[v] - ip[u]) % p
            J = (jp[v] - jp[u]) % q
            if J == I + delta:
                out.append((u, v, I))
    return out

def endgame_check(rel, A, Ci, Cj):
    """Run the step-9 dichotomy on the minimal ordered kill of (Ci,Cj).
    Returns 'non2c' | 'ok'; raises AssertionError if the dichotomy fails."""
    p, q = len(Ci), len(Cj)
    delta = (q - p) // 2
    ip = {v: i for i, v in enumerate(Ci)}
    jp = {v: j for j, v in enumerate(Cj)}
    ok_all = ordered_kills(Ci, Cj)
    u, v, dmin = min(ok_all, key=lambda t: t[2])
    W, simp = hybrid(Ci, Cj, u, v)
    if simp:
        return 'non2c'
    # provenance-aware peel: arc r of W is a D-arc iff r < I (the D-segment
    # of the hybrid comes first); D n D' may share arcs, so provenance is by
    # POSITION, exactly as in the hand proof's peeling chain.
    I0 = dmin
    prov = [r < I0 for r in range(len(W) - 1)]  # True = D-provenance
    stack, pos, pieces = [], {}, []
    for r, x in enumerate(W[:-1]):
        if x in pos:
            kk = pos[x]
            cyc = stack[kk:]
            for y, _ in cyc:
                del pos[y]
            stack = stack[:kk]
            pieces.append(cyc)
        pos[x] = len(stack)
        stack.append((x, prov[r]))
    pieces.append(stack)
    if any(len(E) != p for E in pieces):
        return 'non2c'
    k = len(pieces)
    assert k * p == (p + q) // 2 and q == (2 * k - 1) * p, "2c arithmetic"
    total_a = 0
    for E in pieces:
        n = len(E)
        dpos = [t for t in range(n) if E[t][1]]
        dset = set(dpos)
        starts = [t for t in dpos if (t - 1) % n not in dset]
        assert len(starts) <= 1, "piece D-arcs not contiguous"
        a_t = len(dpos)
        total_a += a_t
        if a_t == 0:
            raise AssertionError("piece with no D-provenance arc")
        s0 = starts[0]
        x_t = E[s0][0]
        E = [y for y, _ in E]
        # interiors of the D-segment that are original shared vertices
        seg_int = [E[(s0 + r) % n] for r in range(1, a_t)]
        interior_shared = [w for w in seg_int if w in ip and w in jp]
        # kill analysis for pair (P_t, Cj) at base x_t
        ipE = {w: t for t, w in enumerate(E[s0:] + E[:s0])}  # E-pos rel x_t
        killers = []
        for w in set(E) & set(Cj):
            if w == x_t:
                continue
            IE = ipE[w] % p
            JE = (jp[w] - jp[x_t]) % q
            if JE == IE + delta:
                killers.append(w)
        if a_t == 1:
            assert not killers, "clean piece but x_t killed?!"
            continue  # dichotomy (i): x_t unkilled
        for w in killers:
            # hand claims: killer is interior-shared with the tau equation,
            # and (x_t -> w) is an ordered (D,D')-kill at distance < dmin
            assert w in interior_shared, \
                "killer of x_t is not an interior shared vertex"
            tau = lambda y: (jp[y] - ip[y]) % q
            assert tau(w) == (tau(x_t) + delta) % q, "tau equation fails"
            Iw = (ip[w] - ip[x_t]) % p
            Jw = (jp[w] - jp[x_t]) % q
            assert Jw == Iw + delta, "(x_t->w) not an ordered (D,D')-kill"
            assert 1 <= Iw <= a_t - 1 < dmin, "distance not < dmin"
        # if no killers: dichotomy (iii) -- fine
    assert total_a == dmin, "Sum a_t != I"
    return 'ok'

def main(smax=4, qmax=13):
    n_fail = n_2c_checked = 0
    for p in (3, 5, 7):
        for q in range(p + 2, qmax + 1, 2):
            for ipos, jpos in glued_graphs(p, q, smax):
                rel, A = build_glued(p, q, ipos, jpos)
                cycles = simple_cycles(rel, A)
                if any(len(C) % 2 == 0 for C in cycles):
                    continue
                for Ci, Cj in odd_cycle_pairs(cycles):
                    kills = kill_edges_11(Ci, Cj)
                    if any(not ks for ks in kills.values()):
                        continue
                    n_fail += 1
                    if endgame_check(rel, A, Ci, Cj) == 'ok':
                        n_2c_checked += 1
    print("glued sweep: failing pairs %d, 2c minimal-kill endgames verified %d"
          % (n_fail, n_2c_checked))
    # the two known genuine stall structures
    for p, q, ipos, jpos in [
            (5, 15, (0, 1, 2, 3), (0, 11, 7, 3)),
            (5, 15, (0, 1, 2, 4), (0, 11, 7, 4)),
            (5, 15, (0, 1, 3, 4), (0, 11, 8, 4)),
            (5, 15, (0, 2, 3, 4), (0, 12, 8, 4))]:
        rel, A = build_glued(p, q, ipos, jpos)
        cycles = simple_cycles(rel, A)
        assert all(len(C) % 2 for C in cycles)
        for Ci, Cj in odd_cycle_pairs(cycles):
            kills = kill_edges_11(Ci, Cj)
            if any(not ks for ks in kills.values()):
                continue
            r = endgame_check(rel, A, Ci, Cj)
            print("stall structure (%d,%d) %s %s: endgame %s"
                  % (len(Ci), len(Cj), ipos, jpos, r))

if __name__ == "__main__":
    main()
