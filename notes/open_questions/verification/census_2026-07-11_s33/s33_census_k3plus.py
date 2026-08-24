#!/usr/bin/env python3
"""s33 census: corrected three-condition screen on two-pentagon gluings
with k >= 3 atom identifications (HANDOFF s32 Priority 1(a)).

Filter order (stop at first failure):
  1. incidence validity / two-cell girth >= 5;
  2. s_* free path (general fixed-or-basin: all-zero infinite path
     through s_*; fixed-point subcount reported);
  3. s_* non-sigma-live (any-position convention; root-only diagnostic);
  4. sigma-live states order-determine the pentagon (0 false non-orders).
Survivors (if any) then face 3-cell window girth, cross-cell separation,
master geometry.

Scope facts proved by hand (pigeonhole, verified here by the k=5 port
check): any 6 pentagon atoms contain a co-block pair, and a co-block old
pair (bo=1) would need its images at block distance >= 4 > 3 = pentagon
diameter bound; hence k >= 6 has NO girth-valid map, and k = 5 forces
old ports = new ports = the odd atoms.
"""
import sys
from collections import Counter
from relay_core import (two_cell_maps, window_girth_ok, succ_masks, analyze,
                        false_nonorders, master_gap_dists, S_STAR,
                        pair_prefilter_ok, BODIST)

for k in (3, 4, 5):
    total = 0
    pre = 0
    valid = []
    for m in two_cell_maps(k):
        total += 1
        if not pair_prefilter_ok(m):
            continue
        pre += 1
        if window_girth_ok([m], 2):
            valid.append(m)
    print(f'--- k={k} ---')
    print('maps:', total, ' pair-prefilter pass:', pre, ' valid (girth>=5):', len(valid))
    if k == 5:
        odd = frozenset({1, 3, 5, 7, 9})
        assert all(frozenset(i for i, j in m) == odd and
                   frozenset(j for i, j in m) == odd for m in valid), \
            'k=5 ports must be the odd atoms'
        print('k=5 port check: all valid maps use odd->odd ports (as proved)')

    free = []
    fixed = 0
    for m in valid:
        a = analyze([m])
        if (a['free'][0] >> S_STAR) & 1:
            free.append((m, a))
            if (a['succ'][0][S_STAR] >> S_STAR) & 1:
                fixed += 1
    print('s_* free basin path:', len(free), f'(of which fixed point: {fixed})')

    nonlive = [(m, a) for m, a in free if not ((a['live'][0] >> S_STAR) & 1)]
    print('s_* non-sigma-live:', len(nonlive))

    sizes = Counter()
    fnos = Counter()
    surv = []
    for m, a in nonlive:
        L = a['live'][0]
        f = false_nonorders(L)
        sizes[bin(L).count('1')] += 1
        fnos[f] += 1
        if f == 0:
            surv.append((m, a))
    print('live-size dist:', dict(sorted(sizes.items())))
    print('false-nonorder dist:', dict(sorted(fnos.items())))
    print('order-determining survivors:', len(surv))
    for m, a in surv:
        print('  SURVIVOR:', m, 'live mask:', bin(a["live"][0]),
              '3-cell girth:', window_girth_ok([m], 3),
              '6-cell girth:', window_girth_ok([m], 6),
              'master gaps:', master_gap_dists([m]))
    # root-only diagnostic on the free set
    rn = 0
    rs = 0
    for m, a in free:
        L = a['E1'][0]
        if not ((L >> S_STAR) & 1):
            rn += 1
            if false_nonorders(L) == 0:
                rs += 1
    print('root-only convention: non-live', rn, '; survivors', rs)
    sys.stdout.flush()
