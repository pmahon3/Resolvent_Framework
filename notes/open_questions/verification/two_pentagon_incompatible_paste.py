#!/usr/bin/env python3
"""Exhaustive two-cell paste of the incompatible pentagon conditional cell.

By default two canonical 11-point pentagon cells are pasted by identifying
exactly q (and q-complement); ``--shared qr`` is the negative control that
also identifies r.  The concrete carrier is the corresponding state-space
fibre product.
The raw event family is the union of the two pulled-back 22-event families.
We then compute the least complement/disjoint-union closed concrete family and
audit latticehood, orthomodularity, centre, maximal Boolean blocks, all
two-valued states, both activated relations, and off-pattern escape.
"""

from itertools import combinations, product
import argparse
import json
from pathlib import Path


BLOCKS = tuple((2*i, 2*i+1, (2*i+2) % 10) for i in range(5))
COORDS = (1, 3, 5, 7, 9)


def local_states():
    out = set()
    for choices in product(*BLOCKS):
        chosen = frozenset(choices)
        if all(len(chosen & frozenset(block)) == 1 for block in BLOCKS):
            out.add(chosen)
    return tuple(sorted(out, key=lambda x: tuple(sorted(x))))


def extrema(events, x, y, lower):
    if lower:
        candidates = [z for z in events if z <= x and z <= y]
        return [z for z in candidates if not any(z < w for w in candidates)]
    candidates = [z for z in events if x <= z and y <= z]
    return [z for z in candidates if not any(w < z for w in candidates)]


def close_orthogonally(seed, omega):
    events = set(seed)
    rounds = []
    while True:
        old = len(events)
        events |= {omega - x for x in events}
        snapshot = tuple(events)
        events |= {x | y for i, x in enumerate(snapshot)
                   for y in snapshot[i:] if not x & y}
        rounds.append(len(events) - old)
        if len(events) == old:
            return frozenset(events), rounds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shared", choices=("q", "qr"), default="q")
    parser.add_argument("--verify", help="JSON receipt which must equal the result")
    parser.add_argument("--output", type=Path, help="write the exact JSON receipt")
    args = parser.parse_args()
    states = local_states()
    carrier = tuple((i, j) for i, s in enumerate(states)
                    for j, t in enumerate(states)
                    if ((7 in s),) == ((7 in t),)
                    and (args.shared != "qr" or (9 in s) == (9 in t)))
    omega = frozenset(range(len(carrier)))
    left_atoms = {a: frozenset(k for k, (i, _) in enumerate(carrier)
                               if a in states[i]) for a in range(10)}
    right_atoms = {a: frozenset(k for k, (_, j) in enumerate(carrier)
                                if a in states[j]) for a in range(10)}
    assert left_atoms[7] == right_atoms[7]
    if args.shared == "qr":
        assert left_atoms[9] == right_atoms[9]

    def cell_events(atoms):
        ans = {frozenset(), omega}
        for x in atoms.values():
            ans |= {x, omega-x}
        return ans

    left_events, right_events = cell_events(left_atoms), cell_events(right_atoms)
    expected_intersection = {frozenset(), omega, left_atoms[7], omega-left_atoms[7]}
    if args.shared == "qr":
        expected_intersection |= {left_atoms[9], omega-left_atoms[9]}
    assert left_events & right_events == expected_intersection
    raw = left_events | right_events
    events, rounds = close_orthogonally(raw, omega)

    meet, join = {}, {}
    failures = []
    for x in events:
        for y in events:
            glb, lub = extrema(events, x, y, True), extrema(events, x, y, False)
            if len(glb) != 1 or len(lub) != 1:
                failures.append((x, y, len(glb), len(lub)))
            else:
                meet[x, y], join[x, y] = glb[0], lub[0]
    lattice = not failures
    orthomodular = False
    centre = set()
    maximal_blocks = []
    if lattice:
        orthomodular = all(
            join[x, meet[y, omega-x]] == y
            for x in events for y in events if x <= y)

        def compatible(x, y):
            return join[meet[x, y], meet[x, omega-y]] == x

        centre = {x for x in events if all(compatible(x, y) for y in events)}
        # Maximal blocks are maximal compatibility cliques; enumerate with a
        # Bron--Kerbosch recursion over event indices, then retain Boolean
        # subalgebras.  Complement pairs make the graph modest in this model.
        ev = tuple(events)
        neigh = {i: {j for j in range(len(ev)) if j != i and compatible(ev[i], ev[j])}
                 for i in range(len(ev))}
        cliques = []
        def bk(r, p, x):
            if not p and not x:
                cliques.append(frozenset(r)); return
            pivot = next(iter(p | x), None)
            todo = set(p if pivot is None else p - neigh[pivot])
            for v in todo:
                bk(r | {v}, p & neigh[v], x & neigh[v])
                p.remove(v); x.add(v)
        bk(set(), set(range(len(ev))), set())
        for c in cliques:
            family = {ev[i] for i in c} | {frozenset(), omega}
            if all(omega-a in family for a in family) and all(a|b in family for a in family for b in family):
                maximal_blocks.append(family)
        assert len(maximal_blocks) == len(cliques)

    # Enumerate all two-valued finitely additive states by selecting exactly one
    # atom in every maximal Boolean block, implemented directly as 0/1 equations
    # over events and backtracking.  For the finite OML these are sigma-states.
    all_states = []
    if lattice and maximal_blocks:
        ev = tuple(events); idx = {x:i for i,x in enumerate(ev)}
        # It suffices and is faster to test carrier point profiles plus detect
        # non-point profiles through exhaustive truth assignments constrained by
        # complement and orthogonal joins.
        constraints = []
        for x in ev:
            constraints.append(("comp", idx[x], idx[omega-x]))
        for x in ev:
            for y in ev:
                if not x & y:
                    constraints.append(("sum", idx[x], idx[y], idx[x|y]))
        order = sorted(range(len(ev)), key=lambda i: -sum(i in c[1:] for c in constraints))
        vals = {idx[frozenset()]:0, idx[omega]:1}
        def consistent():
            for c in constraints:
                if c[0] == "comp" and c[1] in vals and c[2] in vals and vals[c[1]]+vals[c[2]] != 1:
                    return False
                if c[0] == "sum" and all(i in vals for i in c[1:]) and vals[c[1]]+vals[c[2]] != vals[c[3]]:
                    return False
            return True
        def bt(pos):
            while pos < len(order) and order[pos] in vals: pos += 1
            if pos == len(order):
                all_states.append(tuple(vals[i] for i in range(len(ev)))); return
            i = order[pos]
            for v in (0,1):
                vals[i]=v
                if consistent(): bt(pos+1)
            del vals[i]
        bt(0)

    def profile(point, atoms):
        return tuple(int(point in atoms[a]) for a in COORDS)
    left_profiles = {profile(k, left_atoms) for k in omega}
    right_profiles = {profile(k, right_atoms) for k in omega}
    both_activated = {tuple((*profile(k,left_atoms), *profile(k,right_atoms)[:3]))
                      for k in omega
                      if profile(k,left_atoms)[:3] == (1,1,1)
                      and profile(k,right_atoms)[:3] == (1,1,1)}
    left_activation = frozenset(k for k in omega if profile(k,left_atoms)[:3] == (1,1,1))
    right_activation = frozenset(k for k in omega if profile(k,right_atoms)[:3] == (1,1,1))
    union_activation = left_activation | right_activation
    off_both = omega - union_activation
    joint_outputs = {
        (int(k in left_atoms[7]), int(k in left_atoms[9]),
         int(k in right_atoms[9]))
        for k in left_activation & right_activation
    }
    point_state_profiles = {
        tuple(int(k in x) for x in ev) for k in omega
    } if lattice else set()

    result = {
        "schema": "two-pentagon-incompatible-paste-v1",
        "shared_boundary": args.shared,
        "exact_shared_event_count": len(left_events & right_events),
        "carrier_points": len(carrier),
        "raw_events": len(raw),
        "completed_events": len(events),
        "closure_round_increments": rounds,
        "lattice": lattice,
        "orthomodular": orthomodular,
        "complement_closed": all(omega-x in events for x in events),
        "disjoint_union_closed": all(x|y in events for x in events for y in events if not x&y),
        "point_states_order_separate": all(any(k in x and k not in y for k in omega)
                                             for x in events for y in events if not x <= y),
        "binary_extrema_failures": len(failures),
        "centre_size": len(centre),
        "maximal_block_count": len(maximal_blocks),
        "maximal_compatibility_clique_count": len(cliques) if lattice else 0,
        "maximal_block_sizes": sorted(len(b) for b in maximal_blocks),
        "two_valued_state_count": len(all_states),
        "carrier_point_state_count": len(carrier),
        "all_states_are_point_profiles": lattice and set(all_states) == point_state_profiles,
        "left_relation_preserved": sorted(''.join(map(str,p)) for p in left_profiles if p[:3] == (1,1,1)) == ["11100","11111"],
        "right_relation_preserved": sorted(''.join(map(str,p)) for p in right_profiles if p[:3] == (1,1,1)) == ["11100","11111"],
        "both_activation_point_count": len(left_activation & right_activation),
        "both_activated_profiles": sorted(''.join(map(str,p)) for p in both_activated),
        "both_activated_q_rleft_rright_profiles": sorted(''.join(map(str,p)) for p in joint_outputs),
        "left_activation_is_event": left_activation in events,
        "right_activation_is_event": right_activation in events,
        "union_activation_is_event": union_activation in events,
        "every_nonzero_event_has_point_off_both_activations": all(x & off_both for x in events if x),
        "first_extrema_failure": None if not failures else {
            "x": sorted(failures[0][0]), "y": sorted(failures[0][1]),
            "maximal_lower_bounds": failures[0][2], "minimal_upper_bounds": failures[0][3]},
    }
    if args.verify:
        with open(args.verify, encoding="utf-8") as handle:
            expected = json.load(handle)
        assert result == expected
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
