#!/usr/bin/env python3
"""Finite truth-region kernel for outsider extremality (OE).

For every P(k) x P(l), 1 <= k,l <= 4, certify that the five blockwise
greatest subsets of an input intersection have a greatest member, and dually
that the five blockwise least supersets of an input union have a least member.
The blockwise candidates are computed from Boolean block atoms, not by
assuming that set intersection is an event.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

from five_block_two_selector_inflation_audit import NAMES, inflate

SCHEMA = "five-block-two-atom-oe-kernel-v1"


def encode_model(k, ell):
    universe, subset_blocks = inflate(k, ell)
    points = sorted(universe)
    index = {point: i for i, point in enumerate(points)}
    encode = lambda event: sum(1 << index[p] for p in event)
    full = (1 << len(points)) - 1
    blocks = {name: {encode(event) for event in block}
              for name, block in subset_blocks.items()}
    carrier = set().union(*blocks.values())
    atoms = {}
    for name, block in blocks.items():
        atoms[name] = sorted(x for x in block if x and not any(
            y and y != x and y & ~x == 0 for y in block))
    return full, carrier, blocks, atoms


def audit_model(k, ell):
    full, carrier, blocks, atoms = encode_model(k, ell)
    events = sorted(carrier)
    cuts = {x & y for i, x in enumerate(events) for y in events[i:]}
    meet = {}
    join = {}
    winner_pairs = 0
    for i, x in enumerate(events):
        for y in events[i:]:
            cut = x & y
            span = x | y
            lowers = [sum(atom for atom in atoms[name]
                          if atom & ~cut == 0) for name in NAMES]
            uppers = [sum(atom for atom in atoms[name]
                          if atom & span) for name in NAMES]
            greatest = [z for z in lowers if all(w & ~z == 0 for w in lowers)]
            least = [z for z in uppers if all(z & ~w == 0 for w in uppers)]
            assert len(set(greatest)) == 1, (k, ell, hex(x), hex(y), "meet")
            assert len(set(least)) == 1, (k, ell, hex(x), hex(y), "join")
            lo, hi = greatest[0], least[0]
            assert lo in carrier and hi in carrier
            meet[x, y] = meet[y, x] = lo
            join[x, y] = join[y, x] = hi
            winner_pairs += 1
    complement = all(full ^ x in carrier for x in events)
    disjoint_union = all((x | y) in carrier for x in events for y in events
                         if not x & y)
    orthomodular = all(join[x, meet[y, full ^ x]] == y
                       for x in events for y in events if x & ~y == 0)
    encoded = "\n".join(map(hex, events))
    return {
        "fibre_atoms": [k, ell],
        "points": full.bit_count(),
        "events": len(events),
        "unordered_input_pairs": winner_pairs,
        "distinct_intersection_cuts": len(cuts),
        "event_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "checks": {
            "winner_formula_certified": True,
            "complement_closed": complement,
            "binary_disjoint_union_closed": disjoint_union,
            "unique_binary_extrema": True,
            "orthomodular": orthomodular,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    models = [audit_model(k, ell)
              for k, ell in itertools.product(range(1, 5), repeat=2)]
    assert all(all(model["checks"].values()) for model in models)
    result = {"schema": SCHEMA, "models": models}
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
