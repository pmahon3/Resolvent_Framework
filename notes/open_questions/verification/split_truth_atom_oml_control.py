#!/usr/bin/env python3
"""Deterministic exhaustive audit of the split-truth-atom OML control.

This is a generic finite control, not an actual adjacent-assembly realization.
The old six-event MO2 is included as an ordered, complemented event family,
but its incompatible join A \/ B is deliberately not preserved.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "split_truth_atom_oml_control.json"
SCHEMA = "split-truth-atom-oml-control-v1"
OMEGA = frozenset(range(8))


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest(value):
    return sha256_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    )


def mask(event):
    return sum(1 << point for point in event)


def close_family(seeds):
    family = {frozenset(event) for event in seeds}
    rounds = []
    while True:
        before = len(family)
        snapshot = tuple(family)
        family.update(OMEGA - event for event in snapshot)
        snapshot = tuple(family)
        for left, right in itertools.combinations(snapshot, 2):
            if left.isdisjoint(right):
                family.add(left | right)
        added = len(family) - before
        rounds.append(added)
        if added == 0:
            return family, rounds


def extrema(family, left, right, upper):
    if upper:
        bounds = [event for event in family if left <= event and right <= event]
        return [
            event
            for event in bounds
            if not any(other < event for other in bounds)
        ]
    bounds = [event for event in family if event <= left and event <= right]
    return [
        event
        for event in bounds
        if not any(event < other for other in bounds)
    ]


def payload():
    p00 = frozenset({0, 1})
    p01 = frozenset({2, 3})
    p10 = frozenset({4, 5})
    p11 = frozenset({6, 7})
    a = p10 | p11
    b = p01 | p11
    literal_union = a | b
    h = literal_union | {0}
    old = {frozenset(), OMEGA, a, OMEGA - a, b, OMEGA - b}
    family, rounds = close_family(old | {h, OMEGA - h})
    ordered = sorted(family, key=lambda event: (len(event), mask(event)))

    complement_closed = all(OMEGA - event in family for event in family)
    disjoint_union_closed = all(
        left | right in family
        for left, right in itertools.combinations(family, 2)
        if left.isdisjoint(right)
    )

    joins = {}
    meets = {}
    lattice_failures = []
    for left in family:
        for right in family:
            lubs = extrema(family, left, right, True)
            glbs = extrema(family, left, right, False)
            if len(lubs) != 1 or len(glbs) != 1:
                lattice_failures.append(
                    {"left": mask(left), "right": mask(right),
                     "lub_count": len(lubs), "glb_count": len(glbs)}
                )
            else:
                joins[(left, right)] = lubs[0]
                meets[(left, right)] = glbs[0]

    orthomodular_failures = []
    if not lattice_failures:
        for left in family:
            for right in family:
                if left <= right:
                    rhs = joins[(left, meets[(right, OMEGA - left)])]
                    if rhs != right:
                        orthomodular_failures.append(
                            {"left": mask(left), "right": mask(right)}
                        )

    def commutes(left, right):
        rhs = joins[
            (meets[(left, right)], meets[(left, OMEGA - right)])
        ]
        return rhs == left

    centre = [
        event for event in family
        if all(commutes(event, other) for other in family)
    ]

    order_separation_failures = []
    for left in family:
        for right in family:
            if not left <= right and not any(
                point in left and point not in right for point in OMEGA
            ):
                order_separation_failures.append(
                    {"left": mask(left), "right": mask(right)}
                )

    point_state_additivity_failures = []
    for point in OMEGA:
        for left in family:
            for right in family:
                if left <= OMEGA - right:
                    join = joins[(left, right)]
                    if int(point in join) != int(point in left) + int(point in right):
                        point_state_additivity_failures.append(
                            {"point": point, "left": mask(left), "right": mask(right)}
                        )

    old_truth_profiles = {}
    old_ordered = sorted(old, key=mask)
    for point in OMEGA:
        profile = "".join("1" if point in event else "0" for event in old_ordered)
        old_truth_profiles.setdefault(profile, []).append(point)
    old_truth_atoms = sorted(old_truth_profiles.values())
    split_atoms = [
        atom for atom in old_truth_atoms
        if set(atom) & set(h) and not set(atom) <= set(h)
    ]

    a_join_b = joins[(a, b)] if not lattice_failures else frozenset()
    result = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "scope": (
            "Generic 8-point finite concrete OML control. It is not an actual "
            "two-copy assembly, ARR realization, or join-preserving embedding "
            "of the old MO2."
        ),
        "carrier_size": len(OMEGA),
        "event_count": len(family),
        "closure_round_addition_counts": rounds,
        "event_masks_hex": [hex(mask(event)) for event in ordered],
        "old_event_masks_hex": [hex(mask(event)) for event in old_ordered],
        "old_truth_atoms": old_truth_atoms,
        "complement_closed": complement_closed,
        "disjoint_union_closed": disjoint_union_closed,
        "all_pair_lattice_checked": True,
        "lattice_failure_count": len(lattice_failures),
        "orthomodular_comparable_pair_count": sum(
            left <= right for left in family for right in family
        ),
        "orthomodular_failure_count": len(orthomodular_failures),
        "centre_masks_hex": [hex(mask(event)) for event in sorted(centre, key=mask)],
        "centre_is_trivial": set(centre) == {frozenset(), OMEGA},
        "a_mask_hex": hex(mask(a)),
        "b_mask_hex": hex(mask(b)),
        "h_mask_hex": hex(mask(h)),
        "a_join_b_mask_hex": hex(mask(a_join_b)),
        "a_join_b_equals_h": a_join_b == h,
        "literal_union_mask_hex": hex(mask(literal_union)),
        "literal_union_absent": literal_union not in family,
        "split_old_truth_atoms": split_atoms,
        "split_old_truth_atom_count": len(split_atoms),
        "point_state_count": len(OMEGA),
        "point_state_additivity_failure_count": len(point_state_additivity_failures),
        "point_states_order_separate": not order_separation_failures,
        "order_separation_failure_count": len(order_separation_failures),
        "old_inclusion_and_complement_preserved": old <= family,
        "old_incompatible_join_not_preserved": a_join_b != OMEGA,
        "evidence_class": "Executable verified exhaustive finite evidence",
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "split_truth_atom_oml_control.py --verify"
        ),
        "producer_sha256": sha256_bytes(Path(__file__).read_bytes()),
    }
    assert len(family) == 12
    assert complement_closed and disjoint_union_closed
    assert not lattice_failures and not orthomodular_failures
    assert {mask(event) for event in centre} == {0x00, 0x02, 0xFD, 0xFF}
    assert a_join_b == h and literal_union not in family
    assert split_atoms == [[0, 1]]
    assert not point_state_additivity_failures and not order_separation_failures
    result["payload_sha256"] = digest(result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = payload()
    if args.emit:
        RECEIPT.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    if args.verify or not args.emit:
        assert RECEIPT.exists(), "receipt missing; run --emit first"
        assert json.loads(RECEIPT.read_text()) == result
    print(json.dumps({"status": "PASS", "payload_sha256": result["payload_sha256"]}))


if __name__ == "__main__":
    main()
