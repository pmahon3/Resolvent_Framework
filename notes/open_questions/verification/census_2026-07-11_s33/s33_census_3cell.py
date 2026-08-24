#!/usr/bin/env python3
"""s33 census: corrected three-condition screen on three-pentagon period-3
relays (HANDOFF s32 Priority 1(b)).  CORRECTED per s33 advisor:

- ONE-PORT relays are censused UNCONDITIONALLY: the full product of all
  100 valid 1-port interfaces, 100^3 = 1,000,000 triples, NO s_*-self-map
  pre-cut.  A zero result is therefore an unconditional 1-port no-go.
- TWO-PORT relays (1000^3 = 10^9 infeasible) are censused within the
  s32 removable-state DESIGN CLASS only: interfaces preserving s_* (the
  free non-live all-odd cluster state must survive undisturbed).  A zero
  result is a no-go WITHIN that design class, explicitly scoped.

Screen conditions per phase r (period-3 automaton, relay_core.analyze):
  1. s_* free (all-zero infinite path) at phase r;
  2. s_* NOT sigma-live at phase r;
  3. sigma-live states order-determine the pentagon at phase r.
The main loop screens phase 0 (conservative: fewer conditions admit MORE,
so a zero survivor count is still conclusive).  Any phase-0 survivor is
then re-screened at ALL three phases before being believed.
"""
import sys
from itertools import product
from collections import Counter
from relay_core import (two_cell_maps, window_girth_ok, pair_prefilter_ok,
                        succ_masks, analyze, false_nonorders, master_gap_dists,
                        S_STAR, NS)


def valid_ports(k):
    return [m for m in two_cell_maps(k)
            if pair_prefilter_ok(m) and window_girth_ok([m], 2)]


def s_star_selfmap(m):
    return bool((succ_masks(m)[S_STAR] >> S_STAR) & 1)


def phase0_survivor(triple):
    """True iff triple passes screen at phase 0 (s_* free, non-live, live
    set order-determines).  Returns (ok, live_mask)."""
    a = analyze(list(triple))
    if not ((a['free'][0] >> S_STAR) & 1):
        return False, 0
    if (a['live'][0] >> S_STAR) & 1:
        return False, 0
    L = a['live'][0]
    return (false_nonorders(L) == 0), L


def all_phase_check(triple):
    a = analyze(list(triple))
    ok = True
    for r in range(3):
        if not ((a['free'][r] >> S_STAR) & 1):
            ok = False
        if (a['live'][r] >> S_STAR) & 1:
            ok = False
        if false_nonorders(a['live'][r]) != 0:
            ok = False
    return ok, a


def run(ports, label):
    n = len(ports)
    print(f'--- {label}: {n} ports, product {n**3} triples ---')
    survivors = []
    checked = 0
    for triple in product(ports, repeat=3):
        checked += 1
        ok, L = phase0_survivor(triple)
        if ok:
            survivors.append(triple)
    print(f'  triples screened: {checked}; phase-0 survivors: {len(survivors)}')
    confirmed = []
    for triple in survivors:
        ok, a = all_phase_check(triple)
        if ok:
            gg = all(window_girth_ok(list(triple), w) for w in range(2, 10))
            mg = master_gap_dists(list(triple))
            confirmed.append((triple, gg, mg))
    print(f'  all-phase-confirmed survivors: {len(confirmed)}')
    for triple, gg, mg in confirmed[:20]:
        print('    SURVIVOR', triple, 'global-girth<=9', gg, 'master gaps', mg)
    sys.stdout.flush()
    return confirmed


if __name__ == '__main__':
    p1 = valid_ports(1)
    print('1-port valid interfaces:', len(p1))
    run(p1, 'one-port UNCONDITIONAL')

    p2 = valid_ports(2)
    p2self = [m for m in p2 if s_star_selfmap(m)]
    print('\n2-port valid interfaces:', len(p2),
          '; s_*-preserving (design class):', len(p2self))
    run(p2self, 'two-port DESIGN-CLASS (s_*-preserving)')
