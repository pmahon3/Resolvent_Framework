#!/usr/bin/env python3
"""Reproduce the s32 two-port pentagon-relay census (attack note S26)
to validate relay_core semantics before the new s33 censuses.

Expected: 4050 maps -> 1000 valid -> 275 s_* self-loop -> 45 non-live
-> 0 order-determining; live-size dist {0:5,4:2,5:4,6:30,9:4};
false-nonorder dist {4:4,55:30,65:2,71:2,102:2,350:5}; 7 of the 45 meet
master-cycle girth; root-only convention also 0 survivors.
"""
from collections import Counter
from relay_core import (two_cell_maps, window_girth_ok, succ_masks, analyze,
                        false_nonorders, master_gap_dists, S_STAR, NS,
                        pair_prefilter_ok)

maps = list(two_cell_maps(2))
print('total oriented two-atom maps:', len(maps))

valid = [m for m in maps if window_girth_ok([m], 2)]
print('valid (two-cell girth >= 5):', len(valid))
pf = [m for m in maps if pair_prefilter_ok(m)]
print('  (pair-prefilter count, diagnostic):', len(pf))

selfloop = []
for m in valid:
    succ = succ_masks(m)
    if (succ[S_STAR] >> S_STAR) & 1:
        selfloop.append(m)
print('s_* free zero self-loop:', len(selfloop))

# also the general basin count, diagnostic
basin = []
for m in valid:
    a = analyze([m])
    if (a['free'][0] >> S_STAR) & 1:
        basin.append((m, a))
print('  (general free-basin count, diagnostic):', len(basin))

nonlive = []
for m in selfloop:
    a = analyze([m])
    if not ((a['live'][0] >> S_STAR) & 1):
        nonlive.append((m, a))
print('s_* non-sigma-live (any-position):', len(nonlive))

sizes = Counter()
fnos = Counter()
pairs = Counter()
survivors = []
for m, a in nonlive:
    L = a['live'][0]
    n = bin(L).count('1')
    f = false_nonorders(L)
    sizes[n] += 1
    fnos[f] += 1
    pairs[(n, f)] += 1
    if f == 0:
        survivors.append(m)
print('live-size dist:', dict(sorted(sizes.items())))
print('false-nonorder dist:', dict(sorted(fnos.items())))
print('(size, fno) pairs:', dict(sorted(pairs.items())))
print('order-determining survivors:', len(survivors), survivors)

# master-cycle girth diagnostic on the 45
mg = 0
for m, a in nonlive:
    d = master_gap_dists([m])
    if all(v is not None and v >= 4 for v in d.values()):
        mg += 1
print('of the 45, meeting master-cycle girth (min d_g >= 4):', mg)

# root-only convention
root_nonlive = 0
root_surv = 0
for m in selfloop:
    a = analyze([m])
    L = a['E1'][0]                     # root-only live set
    if not ((L >> S_STAR) & 1):
        root_nonlive += 1
        if false_nonorders(L) == 0:
            root_surv += 1
print('root-only: non-live', root_nonlive, '; survivors', root_surv)

# sanity: M* map {1->5, 7->3} present with expected gap distances
mstar = ((1, 5), (7, 3))
print('M* valid:', window_girth_ok([mstar], 2))
succ = succ_masks(mstar)
print('M* s_* self-loop:', bool((succ[S_STAR] >> S_STAR) & 1))
print('M* gap dists (expect 4,5,8,9,12,13 for g=1..6):', master_gap_dists([mstar]))
