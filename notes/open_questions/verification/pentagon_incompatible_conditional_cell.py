#!/usr/bin/env python3
"""Exact finite certificate for the incompatible conditional cell.

The five blocks are the 5-loop Greechie diagram
  {2i, 2i+1, 2i+2 mod 10}, i < 5.
Its concrete representation uses all two-valued block states as points.
The designated coordinates are the five odd atoms
  (a1,a2,a3,q,r) = (1,3,5,7,9).

The checker independently enumerates all block states, builds the concrete
22-element event family, and exhaustively checks unique binary extrema,
orthocomplementation, the orthomodular law, point-state order separation,
pairwise incompatibility of the five designated atoms, and the requested
truth table.  No external package is used.
"""

from itertools import combinations, product
import json


BLOCKS = tuple((2*i, 2*i+1, (2*i+2) % 10) for i in range(5))
COORDS = (1, 3, 5, 7, 9)


def block_states():
    out = set()
    for choices in product(*BLOCKS):
        chosen = frozenset(choices)
        if all(len(chosen.intersection(block)) == 1 for block in BLOCKS):
            out.add(chosen)
    return tuple(sorted(out, key=lambda s: tuple(sorted(s))))


def extrema(events, x, y, lower):
    if lower:
        candidates = [z for z in events if z <= x and z <= y]
        extrema_ = [z for z in candidates
                    if not any(z < w for w in candidates)]
    else:
        candidates = [z for z in events if x <= z and y <= z]
        extrema_ = [z for z in candidates
                    if not any(w < z for w in candidates)]
    return extrema_


def main():
    states = block_states()
    omega = frozenset(range(len(states)))
    atoms = {
        a: frozenset(i for i, state in enumerate(states) if a in state)
        for a in range(10)
    }
    events = {frozenset(), omega}
    for event in atoms.values():
        events.add(event)
        events.add(omega - event)
    assert len(events) == 22

    meets, joins = {}, {}
    for x in events:
        for y in events:
            glb = extrema(events, x, y, True)
            lub = extrema(events, x, y, False)
            assert len(glb) == len(lub) == 1
            meets[x, y], joins[x, y] = glb[0], lub[0]

    assert all(omega - x in events for x in events)
    assert all((x | y) in events for x in events for y in events if not x & y)
    assert all(meets[x, omega-x] == frozenset() and
               joins[x, omega-x] == omega for x in events)
    for x in events:
        for y in events:
            if x <= y:
                rhs = joins[x, meets[y, omega-x]]
                assert rhs == y

    # Every strict nonorder is witnessed by a carrier point, hence the point
    # states order-separate this concrete finite OML.
    assert all(any(i in x and i not in y for i in omega)
               for x in events for y in events if not x <= y)

    # In a concrete OML, compatibility is the Boolean decomposition identity.
    def compatible(x, y):
        return joins[meets[x, y], meets[x, omega-y]] == x

    centre = {x for x in events if all(compatible(x, y) for y in events)}
    assert centre == {frozenset(), omega}
    atom_partitions = {
        tuple(sorted(t)) for t in combinations(range(10), 3)
        if not (atoms[t[0]] & atoms[t[1]])
        and not (atoms[t[0]] & atoms[t[2]])
        and not (atoms[t[1]] & atoms[t[2]])
        and (atoms[t[0]] | atoms[t[1]] | atoms[t[2]]) == omega
    }
    assert atom_partitions == {tuple(sorted(b)) for b in BLOCKS}

    designated = [atoms[a] for a in COORDS]
    assert all(not compatible(designated[i], designated[j])
               for i in range(5) for j in range(i+1, 5))

    profiles = sorted({tuple(int(a in state) for a in COORDS)
                       for state in states})
    activation_support = frozenset(
        i for i, state in enumerate(states)
        if all(a in state for a in COORDS[:3]))
    assert activation_support not in events
    off_activation_points = omega - activation_support
    assert all(x & off_activation_points for x in events if x)
    required = {(1,1,1,0,0), (1,1,1,1,1)}
    forbidden = {(1,1,1,0,1), (1,1,1,1,0)}
    assert required <= set(profiles)
    assert not forbidden.intersection(profiles)
    off_profiles = {p[3:] for p in profiles if p[:3] != (1,1,1)}
    assert off_profiles == {(0,0), (0,1), (1,0), (1,1)}

    off_points = {i for i, state in enumerate(states)
                  if tuple(int(a in state) for a in COORDS[:3]) != (1,1,1)}
    missed_nonorders = [(x, y) for x in events for y in events
                        if not x <= y and not ((x-y) & off_points)]
    assert len(missed_nonorders) == 4

    # Exhaust every designation by atom/coatom events.  There are 780 choices
    # with the exact implication and all four off-cylinder output profiles,
    # but none whose off-cylinder states alone order-determine the pentagon.
    symbols = tuple((kind, a) for kind in ("atom", "coatom")
                    for a in range(10))

    def value(symbol, state):
        kind, a = symbol
        return int((a in state) == (kind == "atom"))

    def sym_compatible(x, y):
        if x[1] == y[1]:
            return True
        return any(x[1] in block and y[1] in block for block in BLOCKS)

    strong_designations = 0
    off_order_determining = 0
    for activation in combinations(symbols, 3):
        if not all(not sym_compatible(x, y)
                   for x, y in combinations(activation, 2)):
            continue
        for qsym, rsym in product(symbols, repeat=2):
            rows = [tuple(value(x, state)
                          for x in (*activation, qsym, rsym))
                    for state in states]
            rowset = set(rows)
            if not required <= rowset or forbidden & rowset:
                continue
            if {row[3:] for row in rowset if row[:3] != (1,1,1)} != {
                    (0,0), (0,1), (1,0), (1,1)}:
                continue
            strong_designations += 1
            off = {i for i, row in enumerate(rows)
                   if row[:3] != (1,1,1)}
            if all(not x <= y and bool((x-y) & off) or x <= y
                   for x in events for y in events):
                off_order_determining += 1
    assert strong_designations == 780
    assert off_order_determining == 0

    result = {
        "schema": "pentagon-incompatible-conditional-cell-v1",
        "blocks": [list(b) for b in BLOCKS],
        "designated_atoms": {"a1": 1, "a2": 3, "a3": 5,
                             "q": 7, "r": 9},
        "carrier_points_and_profiles": [
            {"chosen_atoms": sorted(state),
             "profile": "".join(str(int(a in state)) for a in COORDS)}
            for state in states
        ],
        "event_count": len(events),
        "state_count": len(states),
        "all_designated_pairs_incompatible": True,
        "activation_support_is_not_event": True,
        "unique_binary_extrema": True,
        "orthomodular": True,
        "point_states_order_separate": True,
        "centre_size": len(centre),
        "essentially_irreducible": True,
        "maximal_boolean_blocks": [list(b) for b in BLOCKS],
        "disjoint_union_closed": True,
        "every_nonzero_event_has_off_activation_point_state": True,
        "activated_profiles": ["11100", "11111"],
        "off_activation_output_profiles": ["00", "01", "10", "11"],
        "off_activation_states_order_separate": False,
        "missed_ordered_nonrelations_for_displayed_designation": 4,
        "all_atom_coatom_designations_with_truth_table": strong_designations,
        "such_designations_with_off_activation_order_separation": 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
