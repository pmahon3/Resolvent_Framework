#!/usr/bin/env python3
"""Producer: per-column fibre-trace closure of the rotating small-piece
candidate (oml_rotating_small_piece_candidate.md, Gate N column core).

Universe: the 6-cell fibre partition {g, h, W, Vi, Vj, R} at a type-k
column. Generators of the column trace: r_k={g,h}, r_i={g,W,Vi},
r_j={h,W,Vj}, {g}, {h}. Ops: relative complement and disjoint union
(comparable difference derivable). Exhaustive over the 64 subsets.

Claims certified:
  C1 closure size and membership list (canonical, sorted);
  C2 no nonempty event below W;  C3 r_i cap r_j = {W} not in closure;
  C4 the sigma-kill events {g},{h},r_k present with r_k = {g}⊍{h};
  C5 exactly the cells g,h are isolated.
Scope: column-LOCAL trace only; global closure coincidences are not
covered by this certificate.
"""
import json, sys
FULL = frozenset(range(6))
NAMES = {0: 'g', 1: 'h', 2: 'W', 3: 'Vi', 4: 'Vj', 5: 'R'}
def closure_of(gens):
    cl = set(gens) | {frozenset(), FULL}
    changed = True
    while changed:
        changed = False
        for X in list(cl):
            c = FULL - X
            if c not in cl:
                cl.add(c); changed = True
        items = list(cl)
        for i, X in enumerate(items):
            for Y in items[i + 1:]:
                if not (X & Y) and (X | Y) not in cl:
                    cl.add(X | Y); changed = True
    return cl
def name(X):
    return ','.join(NAMES[i] for i in sorted(X)) if X else 'empty'
def main():
    gens = [frozenset(s) for s in ([0, 1], [0, 2, 3], [1, 2, 4], [0], [1])]
    cl = closure_of(gens)
    rij = frozenset([0, 2, 3]) & frozenset([1, 2, 4])
    cert = {
        'universe_cells': list(NAMES.values()),
        'generators': sorted(name(g) for g in gens),
        'closure_size': len(cl),
        'closure': sorted(name(X) for X in cl),
        'nonempty_below_W': sorted(name(X) for X in cl if X and X <= frozenset([2])),
        'rij_equals_W': sorted(NAMES[i] for i in rij) == ['W'],
        'rij_in_closure': rij in cl,
        'nonempty_below_rij': sorted(name(X) for X in cl if X and X <= rij),
        'isolated_cells': sorted(NAMES[c] for c in range(6) if frozenset([c]) in cl),
        'rk_splits': frozenset([0]) in cl and frozenset([1]) in cl and frozenset([0, 1]) in cl,
    }
    out = sys.argv[sys.argv.index('--output') + 1] if '--output' in sys.argv else \
        'column_trace_schema.json'
    with open(out, 'w') as f:
        json.dump(cert, f, indent=1, sort_keys=True)
    print(f"closure size {cert['closure_size']}; below-W {cert['nonempty_below_W'] or 'NONE'}; "
          f"rij in closure {cert['rij_in_closure']}; isolated {cert['isolated_cells']}; "
          f"rk splits {cert['rk_splits']}")
    assert cert['nonempty_below_W'] == [] and not cert['rij_in_closure']
    assert cert['nonempty_below_rij'] == [] and cert['isolated_cells'] == ['g', 'h']
    assert cert['rk_splits'] and cert['rij_equals_W']
    print('all producer assertions PASS')
if __name__ == '__main__':
    main()
