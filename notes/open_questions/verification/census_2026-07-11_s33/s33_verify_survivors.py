#!/usr/bin/env python3
"""Adversarial verification of the four k=3 two-cell survivors of the
corrected screen.  Independent liveness cross-check via explicit lassos
(never a bounded-unroll heuristic); global periodic girth; master-cycle
girth.  A survivor is a genuine T4 counterexample candidate only if it
passes ALL of: screen (already), global girth over the periodic chain,
and master-cycle girth >= 5 with a single complete master block.
"""
from relay_core import (two_cell_maps, window_girth_ok, succ_masks, analyze,
                        false_nonorders, master_gap_dists, S_STAR, NS, STATES,
                        SYMS, IMG, ALL, LETTER, L0MASK)

SURV = [((1, 7), (3, 1), (7, 5)),
        ((1, 7), (5, 5), (9, 1)),
        ((1, 9), (5, 5), (9, 3)),
        ((3, 5), (7, 9), (9, 3))]


def lasso_live(m, s):
    """Independent liveness check for local state s (period-1 chain): does
    some infinite path from cell 0 through s have target word with exactly
    one 1?  A period-1 chain's reachable configuration graph is finite
    (nodes = states), so an infinite one-1 path exists iff there is a lasso:
    a finite path prefix p (from any admissible cell-0 state, passing s at
    some position) with exactly one letter-1 among all nodes, whose final
    node lies on a cycle of all letter-0 nodes.  We compute:
      - Z = states that begin an all-zero infinite path (on a 0-cycle basin);
      - for each state t, can we reach an all-zero infinite continuation
        after emitting exactly one 1 (with s visited)?
    Realized as reachability with a 2-state ones counter and a 'visited s'
    flag, terminating in the all-zero basin Z."""
    succ = succ_masks(m)
    # all-zero infinite basin: greatest set closed under a 0-successor
    Z = (1 << NS) - 1
    Z &= L0MASK
    changed = True
    while changed:
        changed = False
        newZ = 0
        for x in range(NS):
            if (Z >> x) & 1 and (succ[x] & Z):
                newZ |= 1 << x
        if newZ != Z:
            Z = newZ
            changed = True
    # forward search over (state, ones in {0,1}, saw_s bool); start cell 0
    # any state admissible in cell 0.  Node accepted if ones==1 and it lies
    # in Z (all-zero continuation) OR is a 1-letter state entering Z.
    from collections import deque
    start = [(x, LETTER[x], x == s) for x in range(NS)]
    seen = set()
    dq = deque()
    for st in start:
        if st[1] <= 1:
            seen.add(st)
            dq.append(st)
    while dq:
        x, ones, saw = dq.popleft()
        # acceptance: this node is in the all-zero basin, ones==1, saw s
        if ones == 1 and saw and ((Z >> x) & 1):
            return True
        for y in range(NS):
            if (succ[x] >> y) & 1:
                no = ones + LETTER[y]
                if no > 1:
                    continue
                ns = (x == s) or saw or (y == s)
                st = (y, no, ns)
                if st not in seen:
                    seen.add(st)
                    dq.append(st)
    return False


def global_girth(m, upto=12):
    """First window size (<=upto) at which the periodic chain fails girth,
    or None if all pass (evidence of global girth; period-1 chain is
    eventually periodic so a stable pass is conclusive)."""
    for n in range(2, upto + 1):
        if not window_girth_ok([m], n):
            return n
    return None


for m in SURV:
    print('=== survivor', m, '===')
    a = analyze([m])
    live = [s for s in range(NS) if (a['live'][0] >> s) & 1]
    # independent lasso cross-check on all 11 states
    lasso = [s for s in range(NS) if lasso_live(m, s)]
    agree = set(live) == set(lasso)
    print('  automaton live set:', live)
    print('  lasso   live set:', lasso, '  AGREE:', agree)
    print('  s_* lasso-live?', S_STAR in lasso, '(must be False)')
    fno = false_nonorders(sum(1 << s for s in lasso))
    print('  false non-orders on lasso-live set:', fno, '(0 = order-determining)')
    gg = global_girth(m)
    print('  global girth: first failing window =', gg,
          '(None = passes to window 12)')
    print('  master gaps:', master_gap_dists([m]),
          ' shortest master cycle =',
          (min(v for v in master_gap_dists([m]).values() if v) + 1))
    verdict = 'CANDIDATE' if (agree and S_STAR not in lasso and fno == 0
                              and gg is None
                              and min(master_gap_dists([m]).values()) + 1 >= 5) \
        else 'KILLED'
    print('  VERDICT:', verdict)
