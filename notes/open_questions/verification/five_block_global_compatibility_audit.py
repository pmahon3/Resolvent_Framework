#!/usr/bin/env python3
"""Audit global compatible families in the arbitrary-base q0 inflation.

The audit works with the finite set of event forms.  A nonconstant inflated
event is represented by its outside-q0 part and one Boolean coefficient.
For a finite family, the coefficient algebra is partitioned by the truth
vectors of those coefficients.  Pairwise compatibility can therefore be
tested on the corresponding specializations in the 44-event skeleton.

This is an exact finite-pattern audit of the normal-form argument.  It is not
a Lean certificate and does not by itself prove sigma-completeness.
"""

import argparse
import itertools
import json
from pathlib import Path

from exhaustive_boundary_properness_audit import (
    OMEGA,
    UNIV,
    atom_list,
    labelled_blocks,
    maximal_cliques,
    unique_extreme,
)


SCHEMA = "five-block-global-compatibility-v1"
CHOSEN = ("A00", "A01", "C01", "A10", "A11")
INFLATED = CHOSEN[:3]


def skeleton_data():
    blocks = labelled_blocks()
    blocks = {name: blocks[name] for name in CHOSEN}
    carrier = set().union(*blocks.values())
    meet = {(x, y): unique_extreme(carrier, x, y, False)
            for x in carrier for y in carrier}
    join = {(x, y): unique_extreme(carrier, x, y, True)
            for x in carrier for y in carrier}

    def compatible(x, y):
        return join[meet[x, y], meet[x, UNIV - y]] == x

    return blocks, carrier, compatible


def event_forms(blocks, carrier):
    q0 = frozenset(point for point in OMEGA if point[0] == 0)
    templates = {}
    for name in INFLATED:
        atoms = atom_list(blocks[name])
        assert q0 in atoms
        outside_atoms = [atom for atom in atoms if atom != q0]
        for mask in range(1 << len(outside_atoms)):
            outside = frozenset().union(*(
                outside_atoms[i] for i in range(len(outside_atoms))
                if mask >> i & 1
            ))
            templates[outside] = {
                "kind": "parameter",
                "zero": outside,
                "one": outside | q0,
            }

    forms = []
    for event in sorted(carrier, key=lambda x: (len(x), sorted(x))):
        forms.append({
            "kind": "constant",
            "zero": event,
            "one": event,
            "blocks": tuple(name for name in CHOSEN if event in blocks[name]),
        })
    for outside, form in sorted(templates.items(), key=lambda item: sorted(item[0])):
        form["blocks"] = tuple(
            name for name in INFLATED
            if form["zero"] in blocks[name] and form["one"] in blocks[name]
        )
        forms.append(form)
    return forms


def feasible_truth_vectors(family, compatible):
    parameters = [i for i, form in enumerate(family)
                  if form["kind"] == "parameter"]
    position = {index: j for j, index in enumerate(parameters)}
    feasible = []
    for bits in itertools.product((0, 1), repeat=len(parameters)):
        events = []
        for i, form in enumerate(family):
            bit = bits[position[i]] if i in position else 0
            events.append(form["one"] if bit else form["zero"])
        if all(compatible(events[i], events[j])
               for i in range(len(events)) for j in range(i + 1, len(events))):
            feasible.append(bits)
    nonconstant = all(
        {bits[j] for bits in feasible} == {0, 1}
        for j in range(len(parameters))
    )
    return feasible, nonconstant


def four_region_crosscheck(forms, blocks, compatible):
    """Compare the truth-vector rule with the concrete P(4) block cover.

    Four atoms realize the four possible truth regions of two coefficients.
    The previously certified P(4) approximant has exactly the five named
    maximal blocks, so two concrete events are compatible exactly when their
    named-block membership sets intersect.
    """
    assignments = tuple(itertools.product((0, 1), repeat=4))

    def coefficient_values(form):
        return range(16) if form["kind"] == "parameter" else (0,)

    def actual_membership(form, coefficient):
        if form["kind"] == "constant":
            return frozenset(form["blocks"])
        membership = set()
        for name in CHOSEN:
            if name not in INFLATED:
                continue
            # An inflated block contains the event iff every fibre-atom
            # specialization belongs to its skeleton block with the same
            # outside form.
            if all((form["one"] if coefficient >> atom & 1 else form["zero"])
                   in blocks[name] for atom in range(4)):
                membership.add(name)
        # Degenerate coefficients are skeleton events and may also lie in
        # either unchanged finite block.
        if coefficient in (0, 15):
            event = form["one"] if coefficient == 15 else form["zero"]
            membership.update(name for name in CHOSEN if event in blocks[name])
        return frozenset(membership)

    comparisons = 0
    for i, left in enumerate(forms):
        for right in forms[i:]:
            for a in coefficient_values(left):
                for b in coefficient_values(right):
                    pointwise = all(compatible(
                        left["one"] if a >> atom & 1 else left["zero"],
                        right["one"] if b >> atom & 1 else right["zero"],
                    ) for atom in range(4))
                    concrete = bool(actual_membership(left, a) &
                                    actual_membership(right, b))
                    assert pointwise == concrete
                    comparisons += 1
    return {
        "coefficient_truth_assignments": len(assignments),
        "form_instance_pair_comparisons": comparisons,
        "pointwise_equals_concrete_compatibility": True,
    }


def find_obstruction(forms, compatible):
    """Find a minimal compatible family not contained in a named block."""
    full_names = frozenset(CHOSEN)
    for size in range(2, len(CHOSEN) + 1):
        for indices in itertools.combinations(range(len(forms)), size):
            family = [forms[i] for i in indices]
            common = full_names.intersection(*(form["blocks"] for form in family))
            if common:
                continue
            # Minimality removes redundant signature repetitions and sharply
            # bounds the exhaustive search.
            if any(full_names.intersection(*(
                    family[j]["blocks"] for j in range(size) if j != i
                    )) == frozenset()
                   for i in range(size)):
                continue
            feasible, nonconstant = feasible_truth_vectors(family, compatible)
            if feasible and nonconstant:
                return {
                    "size": size,
                    "indices": list(indices),
                    "truth_vectors": [list(bits) for bits in feasible],
                    "required_fibre_atoms": len(feasible),
                    "block_signatures": [list(form["blocks"]) for form in family],
                }
    return None


def build():
    blocks, carrier, compatible = skeleton_data()
    forms = event_forms(blocks, carrier)
    obstruction = find_obstruction(forms, compatible)
    crosscheck = four_region_crosscheck(forms, blocks, compatible)
    signatures = {}
    for form in forms:
        key = "/".join(form["blocks"])
        signatures[key] = signatures.get(key, 0) + 1
    return {
        "schema": SCHEMA,
        "scope": (
            "all finite pairwise-compatible families of arbitrary-base q0 "
            "normal forms; sigma-completeness and the main conjecture excluded"
        ),
        "counts": {
            "skeleton_events": len(carrier),
            "constant_forms": sum(form["kind"] == "constant" for form in forms),
            "parameter_forms": sum(form["kind"] == "parameter" for form in forms),
            "block_signature_counts": signatures,
        },
        "checks": {
            "skeleton_maximal_compatible_families": len(maximal_cliques(
                carrier, lambda x, y: x != y and compatible(x, y)
            )),
            "minimal_obstruction_search_bound": len(CHOSEN),
            "compatible_family_without_common_named_block": obstruction,
            "global_five_block_cover": obstruction is None,
            "four_region_crosscheck": crosscheck,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build()
    assert result["checks"]["skeleton_maximal_compatible_families"] == 5
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
