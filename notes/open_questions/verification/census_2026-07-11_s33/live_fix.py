#!/usr/bin/env python3
"""Corrected sigma-live computation (period-p, phase-consistent).

s24 any-position convention: local state s at phase r is sigma-live iff
it lies on SOME two-sided infinite chain path whose full target word has
EXACTLY ONE 1.  Decompose at s: a prefix ending at s and a suffix starting
at s; total ones = 1.  So s is live at r iff EITHER
  (A) letter(s)=1 and s begins an all-zero SUFFIX and s ends an all-zero
      PREFIX; OR
  (B) letter(s)=0 and [s begins a one-1 suffix and ends an all-zero prefix]
      OR [s begins an all-zero suffix and ends a one-1 prefix].
where:
  SUFFIX fixpoints (forward, phase r -> r+1):
    E0[r] = s: all-zero infinite forward path (greatest fp)  [have it]
    E1[r] = s: exactly-one-1 infinite forward path (least fp) [have it]
  PREFIX fixpoints (backward, phase r <- r-1); a bi-infinite path has no
    boundary, so the prefix is also infinite and we need:
    P0[r] = s: all-zero infinite BACKWARD path ending at s
    P1[r] = s: exactly-one-1 infinite BACKWARD path ending at s
These are the mirror fixpoints on the reversed transition relation.
Boundary-rooted (root-only) convention instead sets the prefix to 'starts
at cell 0 with an all-zero or one-1 finite prefix'.
"""
from relay_core import succ_masks, NS, LETTER, L0MASK, L1MASK


def pred_masks(succ, p):
    """pred[r][s] = states t at phase r-1 with s in succ[r-1][t]."""
    pred = [[0] * NS for _ in range(p)]
    for r in range(p):
        rprev = (r - 1) % p
        for t in range(NS):
            st = succ[rprev][t]
            for s in range(NS):
                if (st >> s) & 1:
                    pred[r][s] |= 1 << t
    return pred


def suffix_fixpoints(succ, p):
    E0 = [L0MASK] * p
    ch = True
    while ch:
        ch = False
        for r in range(p):
            nx = E0[(r + 1) % p]
            m = 0
            for s in range(NS):
                if (E0[r] >> s) & 1 and (succ[r][s] & nx):
                    m |= 1 << s
            if m != E0[r]:
                E0[r] = m; ch = True
    E1 = [0] * p
    ch = True
    while ch:
        ch = False
        for r in range(p):
            nE0, nE1 = E0[(r + 1) % p], E1[(r + 1) % p]
            m = E1[r]
            for s in range(NS):
                if (m >> s) & 1:
                    continue
                if LETTER[s]:
                    if succ[r][s] & nE0:
                        m |= 1 << s
                else:
                    if succ[r][s] & nE1:
                        m |= 1 << s
            if m != E1[r]:
                E1[r] = m; ch = True
    return E0, E1


def prefix_fixpoints(pred, p):
    """Mirror of suffix on reversed edges: P0[r]=all-zero infinite backward
    path ending at s (incl. s's letter); P1[r]=exactly-one-1 backward."""
    P0 = [L0MASK] * p
    ch = True
    while ch:
        ch = False
        for r in range(p):
            pv = P0[(r - 1) % p]
            m = 0
            for s in range(NS):
                if (P0[r] >> s) & 1 and (pred[r][s] & pv):
                    m |= 1 << s
            if m != P0[r]:
                P0[r] = m; ch = True
    P1 = [0] * p
    ch = True
    while ch:
        ch = False
        for r in range(p):
            pP0, pP1 = P0[(r - 1) % p], P1[(r - 1) % p]
            m = P1[r]
            for s in range(NS):
                if (m >> s) & 1:
                    continue
                if LETTER[s]:
                    if pred[r][s] & pP0:
                        m |= 1 << s
                else:
                    if pred[r][s] & pP1:
                        m |= 1 << s
            if m != P1[r]:
                P1[r] = m; ch = True
    return P0, P1


def live_any(succ, p):
    E0, E1 = suffix_fixpoints(succ, p)
    pred = pred_masks(succ, p)
    P0, P1 = prefix_fixpoints(pred, p)
    live = [0] * p
    for r in range(p):
        for s in range(NS):
            if LETTER[s]:
                ok = ((E0[r] >> s) & 1) and ((P0[r] >> s) & 1)
            else:
                ok = (((E1[r] >> s) & 1) and ((P0[r] >> s) & 1)) or \
                     (((E0[r] >> s) & 1) and ((P1[r] >> s) & 1))
            if ok:
                live[r] |= 1 << s
    return live, E0, E1, P0, P1


def live_root(succ, p):
    """Boundary-rooted: prefix starts at cell 0 (finite, phase-0 seeded)."""
    E0, E1 = suffix_fixpoints(succ, p)
    # reachable-from-cell-0 with ones-so-far-before-this-node in {0,1}
    # Rpre[r][k] = states reachable at phase r having emitted k ones STRICTLY
    # BEFORE entering this node.
    Rpre = [[0, 0] for _ in range(p)]
    Rpre[0][0] = (1 << NS) - 1                    # cell 0: nothing emitted yet
    ch = True
    while ch:
        ch = False
        for r in range(p):
            r2 = (r + 1) % p
            for k in (0, 1):
                src = Rpre[r][k]
                if not src:
                    continue
                for s in range(NS):
                    if not ((src >> s) & 1):
                        continue
                    kk = k + LETTER[s]            # ones emitted after leaving s
                    if kk > 1:
                        continue
                    nxt = succ[r][s]
                    add = nxt & ~Rpre[r2][kk]
                    if add:
                        Rpre[r2][kk] |= add
                        ch = True
    live = [0] * p
    for r in range(p):
        for s in range(NS):
            # rooted one-1 path through s: prefix ones k, suffix must make
            # total 1
            k0 = (Rpre[r][0] >> s) & 1
            k1 = (Rpre[r][1] >> s) & 1
            if LETTER[s]:
                ok = (k0 and ((E0[r] >> s) & 1))          # this s is the 1
            else:
                ok = (k1 and ((E0[r] >> s) & 1)) or \
                     (k0 and ((E1[r] >> s) & 1))
            if ok:
                live[r] |= 1 << s
    return live
