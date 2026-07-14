#!/usr/bin/env python3
"""Independent verifier: recomputes the column-trace closure by a
different method (BFS over bitmasks, ops applied in a different order,
no shared code with the producer) and checks every certificate field."""
import json, sys
FULL = 0b111111
NAMES = ['g', 'h', 'W', 'Vi', 'Vj', 'R']
def bfs_closure(gen_masks):
    seen = set(gen_masks) | {0, FULL}
    frontier = list(seen)
    while frontier:
        nxt = []
        for x in frontier:
            cands = [x ^ FULL]
            cands += [x | y for y in list(seen) if (x & y) == 0]
            for c in cands:
                if c not in seen:
                    seen.add(c); nxt.append(c)
        frontier = nxt
    return seen
def mask_name(m):
    return ','.join(NAMES[i] for i in range(6) if m >> i & 1) if m else 'empty'
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'column_trace_schema.json'
    cert = json.load(open(path))
    gens = [0b000011, 0b001101, 0b010110, 0b000001, 0b000010]
    cl = bfs_closure(gens)
    assert len(cl) == cert['closure_size'], 'size mismatch'
    assert sorted(mask_name(m) for m in cl) == cert['closure'], 'membership mismatch'
    W = 0b000100
    assert [m for m in cl if m and (m | W) == W] == [], 'event below W found'
    rij = 0b001101 & 0b010110
    assert rij == W and (rij in cl) == cert['rij_in_closure'] and not cert['rij_in_closure']
    iso = sorted(NAMES[i] for i in range(6) if (1 << i) in cl)
    assert iso == cert['isolated_cells'] == ['g', 'h'], 'isolation mismatch'
    assert (0b000001 in cl) and (0b000010 in cl) and (0b000011 in cl)
    print(f'verifier: closure {len(cl)} events; ALL CHECKS PASS')
if __name__ == '__main__':
    main()
