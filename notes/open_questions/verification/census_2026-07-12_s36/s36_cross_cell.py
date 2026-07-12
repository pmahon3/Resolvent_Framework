#!/usr/bin/env python3
"""Exact rooted finite-position cross-cell separation for the two k=4 candidates.

For cells i<j this enumerates every compatible state word through j that
extends to an infinite word with exactly one target 1, then compares its
(state_i,state_j) projections against the actual quotient-symbol order.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S35 = HERE.parent / 'census_2026-07-12_s35'
sys.path.insert(0, str(S35))
import relay7_core as rc  # noqa: E402


def actual_leq(dsu, i, x, j, y):
    """Order of atom/complement symbols in a loop-Greechie quotient."""
    kx, ax = x
    ky, ay = y
    qx = dsu.find(14*i + ax)
    qy = dsu.find(14*j + ay)
    if kx == ky:
        return qx == qy
    if kx == 'c':
        return False
    # atom ax <= ay^perp exactly when distinct quotient atoms share a block.
    return qx != qy and any(qx in B and qy in B for B in CURRENT_BLOCKS)


CURRENT_BLOCKS = ()


def extendable_pairs(port, target, i, j):
    out = rc.analyze([port], target)
    succ, e0, e1 = out['succ'][0], out['E0'][0], out['E1'][0]
    letter = out['letter']
    # tuples (last_state, ones, state_at_i), starting at the free root.
    layer = {(s, letter[s], s if i == 0 else None) for s in range(rc.NS)}
    for n in range(j):
        nxt = set()
        for s, ones, si in layer:
            mask = succ[s]
            for t in range(rc.NS):
                one2 = ones + letter[t]
                if mask >> t & 1 and one2 <= 1:
                    nxt.add((t, one2, t if n+1 == i else si))
        layer = nxt
    pairs = set()
    for sj, ones, si in layer:
        suffix = e1 if ones == 0 else e0
        if succ[sj] & suffix:
            pairs.add((si, sj))
    return pairs


def failures(port, target, i, j):
    global CURRENT_BLOCKS
    CURRENT_BLOCKS, dsu = rc.quotient_blocks([port], j+1)
    pairs = extendable_pairs(port, target, i, j)
    fails = []
    for x in rc.SYMS:
        for y in rc.SYMS:
            if actual_leq(dsu, i, x, j, y):
                continue
            witnessed = any(bool(rc.IMG[x] >> si & 1) and
                              not bool(rc.IMG[y] >> sj & 1)
                              for si, sj in pairs)
            if not witnessed:
                fails.append((x, y))
    return pairs, fails


def main():
    downstream = json.loads((HERE/'s36_downstream_results.json').read_text())
    candidates = [r for r in downstream['rows']
                  if r['passes_adjacent_master_distance']]
    report = []
    for candidate in candidates:
        port = tuple(map(tuple, candidate['port']))
        checks = []
        for j in range(1, 13):
            for i in range(j):
                pairs, fail = failures(port, candidate['target'], i, j)
                checks.append({'i': i, 'j': j, 'realisable_state_pairs': len(pairs),
                               'false_orders': [[list(x), list(y)] for x, y in fail]})
        report.append({'target': candidate['target'], 'port': candidate['port'],
                       'checks': checks,
                       'passes_all_offsets_through_12': not any(
                           c['false_orders'] for c in checks)})
    dest = HERE/'s36_cross_cell_results.json'
    dest.write_text(json.dumps({'candidates': report}, indent=2, sort_keys=True)+'\n')
    for r in report:
        bad = [c for c in r['checks'] if c['false_orders']]
        print(r['port'], 'bad_checks=', len(bad),
              'first=', bad[0] if bad else None)


if __name__ == '__main__':
    main()
