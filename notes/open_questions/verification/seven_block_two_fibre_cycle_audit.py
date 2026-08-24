#!/usr/bin/env python3
"""Audit atom-selector pairs in the certified seven-block OML skeleton.

This is a finite incidence/state audit.  It classifies lattice-atom
automorphism orbits, propagation supports, joint point-state coherence with
q_0, and whether the resulting two interval fibres can occur in one block.
It does not assert an infinite sigma-complete inflation theorem.
"""

import argparse
from collections import Counter, defaultdict
import itertools
import json
from pathlib import Path


SCHEMA = "seven-block-two-fibre-cycle-v1"


def cover_graph(meet):
    size = len(meet)

    def le(left, right):
        return meet[left][right] == left

    successors = {node: set() for node in range(size)}
    predecessors = {node: set() for node in range(size)}
    for left in range(size):
        for right in range(size):
            if left == right or not le(left, right):
                continue
            if not any(
                middle not in (left, right)
                and le(left, middle)
                and le(middle, right)
                for middle in range(size)
            ):
                successors[left].add(right)
                predecessors[right].add(left)
    return successors, predecessors


def canonical_cycle(cycle):
    variants = []
    for oriented in (cycle, list(reversed(cycle))):
        for shift in range(len(cycle)):
            variants.append(tuple(oriented[shift:] + oriented[:shift]))
    return min(variants)


def cycles_containing(graph, required):
    cycles = set()
    nodes = sorted(graph)
    for length in range(3, len(nodes) + 1):
        for cycle in itertools.permutations(nodes, length):
            if cycle[0] != min(cycle) or not required <= set(cycle):
                continue
            if all(cycle[(i + 1) % length] in graph[cycle[i]]
                   for i in range(length)):
                cycles.add(canonical_cycle(list(cycle)))
    return sorted(cycles, key=lambda cycle: (len(cycle), cycle))


def atom_automorphisms(meet, atoms):
    """Enumerate atom permutations preserving the atomistic event family."""
    event_atom_masks = {
        sum(1 << index for index, atom in enumerate(atoms)
            if meet[atom][event] == atom)
        for event in range(len(meet))
    }
    assert len(event_atom_masks) == len(meet), "the skeleton must be atomistic"
    signatures = []
    for index in range(len(atoms)):
        signatures.append(tuple(sorted(Counter(
            mask.bit_count() for mask in event_atom_masks if mask >> index & 1
        ).items())))
    classes = defaultdict(list)
    for index, signature in enumerate(signatures):
        classes[signature].append(index)

    automorphisms = []
    permutation_families = [list(itertools.permutations(indices))
                            for indices in classes.values()]
    class_indices = list(classes.values())
    for choices in itertools.product(*permutation_families):
        permutation = list(range(len(atoms)))
        for indices, images in zip(class_indices, choices):
            for source, target in zip(indices, images):
                permutation[source] = target
        valid = True
        for mask in event_atom_masks:
            image = sum(1 << permutation[index]
                        for index in range(len(atoms)) if mask >> index & 1)
            if image not in event_atom_masks:
                valid = False
                break
        if valid:
            automorphisms.append(permutation)
    return automorphisms


def build(skeleton):
    meet = skeleton["meet"]
    masks = skeleton["event_masks"]
    successors, predecessors = cover_graph(meet)
    bottom = next(node for node in successors if not predecessors[node])
    atoms = sorted(successors[bottom])
    automorphisms = atom_automorphisms(meet, atoms)
    unseen = set(atoms)
    orbits = []
    while unseen:
        representative = min(unseen)
        representative_index = atoms.index(representative)
        orbit = sorted({atoms[auto[representative_index]]
                        for auto in automorphisms})
        orbits.append(orbit)
        unseen.difference_update(orbit)
    orbit_of = {
        atom: index for index, orbit in enumerate(orbits) for atom in orbit
    }

    blocks = {block["name"]: block for block in skeleton["blocks"]}
    support = {
        atom: sorted(
            name for name, block in blocks.items() if atom in block["atoms"]
        )
        for atom in atoms
    }
    incidence = {name: set() for name in blocks}
    for overlap in skeleton["pairwise_intersections"]:
        # Size two is the trivial {0,1} overlap and carries no selector data.
        if overlap["size"] > 2:
            incidence[overlap["left"]].add(overlap["right"])
            incidence[overlap["right"]].add(overlap["left"])

    q0 = skeleton["generators"]["B_atoms"][0]
    q_support = set(support[q0])
    selectors = []
    pairs = []
    for atom in atoms:
        selectors.append(
            {
                "event": atom,
                "mask": masks[atom],
                "automorphism_orbit": orbit_of[atom],
                "support": support[atom],
            }
        )
        if atom == q0:
            continue
        atom_support = set(support[atom])
        jointly_coherent = bool(masks[q0] & masks[atom])
        common_blocks = sorted(q_support & atom_support)
        if atom_support == q_support:
            relation = "identical"
        elif atom_support < q_support or q_support < atom_support:
            relation = "nested"
        elif not common_blocks:
            relation = "disjoint"
        else:
            relation = "crossed"
        required = q_support | atom_support
        cycles = cycles_containing(incidence, required)
        pairs.append(
            {
                "second_selector": atom,
                "second_mask": masks[atom],
                "jointly_coherent_with_q0": jointly_coherent,
                "support_relation": relation,
                "common_support_blocks": common_blocks,
                "one_block_sees_both_fibres": bool(common_blocks),
                "minimal_block_cycle": list(cycles[0]) if cycles else None,
                "minimal_block_cycle_length": len(cycles[0]) if cycles else None,
                "actual_overlap_relation": (
                    "none: no block contains both selector intervals"
                    if not common_blocks
                    else "requires a separate completed-inflation audit"
                ),
                "relation_factorizes_at_raw_atlas_level": not common_blocks,
                "priority": (
                    "reject-orthogonal"
                    if not jointly_coherent
                    else "control-disjoint-rectangular"
                    if not common_blocks
                    else "candidate"
                ),
            }
        )

    coherent = [pair for pair in pairs if pair["jointly_coherent_with_q0"]]
    return {
        "schema": SCHEMA,
        "scope": (
            "atom-interval substitutions in the certified finite skeleton; "
            "not an infinite sigma-completeness certificate"
        ),
        "q0": q0,
        "automorphism_count": len(automorphisms),
        "atom_orbits": orbits,
        "selectors": selectors,
        "pairs_with_q0": pairs,
        "checks": {
            "atom_count": len(atoms),
            "orbit_sizes": [len(orbit) for orbit in orbits],
            "q0_support": support[q0],
            "jointly_coherent_second_selectors": [
                pair["second_selector"] for pair in coherent
            ],
            "all_jointly_coherent_distinct_pairs_have_disjoint_support": all(
                pair["support_relation"] == "disjoint" for pair in coherent
            ),
            "no_jointly_coherent_distinct_pair_has_direct_fibre_overlap": all(
                not pair["one_block_sees_both_fibres"] for pair in coherent
            ),
            "all_jointly_coherent_raw_relations_factorize": all(
                pair["relation_factorizes_at_raw_atlas_level"]
                for pair in coherent
            ),
        },
        "verdict": (
            "No jointly coherent distinct atom pair has overlapping propagation "
            "support. Cycles in the block-incidence graph therefore carry no "
            "two-coordinate overlap equation, so the raw two-fibre relation is "
            "rectangular."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skeleton",
        type=Path,
        default=Path(__file__).with_name("seven_block_skeleton.json"),
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(json.loads(args.skeleton.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
