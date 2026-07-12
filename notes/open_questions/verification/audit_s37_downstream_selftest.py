#!/usr/bin/env python3
"""Anchors for the independent s37 downstream oracle."""
from audit_s37_downstream_oracle import NS, audit


def main():
    assert NS == 29
    # The two s36 period-one candidates must reproduce their independently
    # banked adjacent false order.  Keep period one: rooted any-position
    # semantics intentionally does not permit phasewise period collapse.
    candidates = (
        ((0,11),(3,5),(6,9),(13,3)),
        ((1,7),(5,9),(11,11),(12,3)),
    )
    for port in candidates:
        r = audit([port], 1, 2)
        # The newer mandatory fixed-root restriction is stronger than the
        # s36 any-position screen; these candidates fail it as well.
        assert r['root_local_false_orders'] > 0
        adjacent = next(x for x in r['cross_cell'] if x['i'] == 0 and x['j'] == 1)
        assert adjacent['false_count'] > 0
        assert any(x == ('a', 1) and y == ('c', 1)
                   for x, y in adjacent['first_false'])
    # Period-two width-one anchors from the exhaustive s36 zero census.
    # Each must fail at least one operative local condition.
    anchors = (
        ((((0,0),), ((0,0),)), 1),
        ((((0,1),), ((1,0),)), 2),
        ((((3,11),), ((11,3),)), 4),
    )
    for maps, target in anchors:
        r = audit(maps, target, 8)
        operative = (all(r['phase_face_free_tested']) and
                     all(r['phase_face_nonlive_tested']) and
                     not any(r['phase_local_false_orders_tested']))
        assert not operative
    print('s37 downstream self-test passed: s36 candidates and p2-k1 anchors')


if __name__ == '__main__': main()
