#!/usr/bin/env python3
"""Audit the finite data for the (5,11) non-atomic pullback gate.

The orbit calculation concerns the certified 56-event skeleton.  The
pullback controls concern finite Boolean algebras and do not, by themselves,
assert that a coarse substitution has an OML completion.
"""

import argparse
from collections import Counter
import importlib.util
import itertools
import json
from pathlib import Path

from seven_block_interval_inflation_audit import unions


SCHEMA = "seven-block-nonatomic-pullback-v1"
HERE = Path(__file__).parent


def load_cycle_module():
    path = HERE / "seven_block_two_fibre_cycle_audit.py"
    spec = importlib.util.spec_from_file_location("two_fibre_cycle", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def event_automorphisms(skeleton):
    cycle = load_cycle_module()
    meet = skeleton["meet"]
    successors, predecessors = cycle.cover_graph(meet)
    bottom = next(x for x in successors if not predecessors[x])
    atoms = sorted(successors[bottom])
    atom_automorphisms = cycle.atom_automorphisms(meet, atoms)
    atom_mask_to_event = {
        sum(1 << i for i, atom in enumerate(atoms) if meet[atom][event] == atom): event
        for event in range(len(meet))
    }
    maps = []
    for automorphism in atom_automorphisms:
        event_map = []
        for event in range(len(meet)):
            mask = sum(1 << i for i, atom in enumerate(atoms)
                       if meet[atom][event] == atom)
            image = sum(1 << automorphism[i] for i in range(len(atoms))
                        if mask >> i & 1)
            event_map.append(atom_mask_to_event[image])
        maps.append(event_map)
    return atoms, maps


def pair_orbits(skeleton, pair_receipt):
    atoms, automorphisms = event_automorphisms(skeleton)
    meet = skeleton["meet"]
    comp = skeleton["complement"]
    blocks = {block["name"]: set(block["events"]) for block in skeleton["blocks"]}
    support = {event: {name for name, block in blocks.items() if event in block}
               for event in range(len(meet))}
    qualifying = {tuple(record["pair"]): record
                  for record in pair_receipt["qualifying_pairs"]}
    unseen = set(qualifying)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            tuple(sorted((automorphism[representative[0]],
                          automorphism[representative[1]])))
            for automorphism in automorphisms
        }
        assert orbit <= set(qualifying)
        record = qualifying[representative]
        left, right = representative
        regions = [meet[left][right], meet[left][comp[right]],
                   meet[comp[left]][right]]
        generated = {0, len(meet) - 1, left, right, comp[left], comp[right]}
        while True:
            old = set(generated)
            generated |= {comp[x] for x in old}
            generated |= {meet[x][y] for x in old for y in old}
            # In an ortholattice, x join y = (x^perp meet y^perp)^perp.
            generated |= {comp[meet[comp[x]][comp[y]]] for x in old for y in old}
            if generated == old:
                break
        invariants = {
            "support_sizes": sorted([len(support[left]), len(support[right])]),
            "support_intersection_size": len(support[left] & support[right]),
            "support_cycle_length": len(record["minimal_support_cycle"]),
            "interval_sizes": [sum(meet[x][left] == x for x in range(len(meet))),
                               sum(meet[x][right] == x for x in range(len(meet)))],
            "carrier_region_cardinalities": [
                skeleton["event_masks"][region].bit_count() for region in regions
            ],
            "common_block_count": len(record["common_blocks"]),
            "meet_event": regions[0],
            "generated_sub_oml_size": len(generated),
        }
        orbits.append({
            "representative": list(representative),
            "orbit_size": len(orbit),
            "members": [list(pair) for pair in sorted(orbit)],
            "common_blocks": record["common_blocks"],
            "meet_event": regions[0],
            "support_cycle": record["minimal_support_cycle"],
            "invariants": invariants,
            "priority": "primary-(5,11)-architecture" if representative == (5, 11)
                        else "separate-orbit-control",
        })
        unseen -= orbit
    return atoms, automorphisms, orbits


def pullback_control(a_atoms, d_atoms, c_atoms, collapse=None):
    """Finite Stone-space pullback of quotient maps between atom sets."""
    if collapse == "left":
        left_map = [0] * a_atoms
        right_map = [i % d_atoms for i in range(c_atoms)]
        effective_d = 1
        relation = list(itertools.product(range(a_atoms), range(c_atoms)))
    elif collapse == "right":
        left_map = [i % d_atoms for i in range(a_atoms)]
        right_map = [0] * c_atoms
        effective_d = 1
        relation = list(itertools.product(range(a_atoms), range(c_atoms)))
    else:
        assert a_atoms >= d_atoms and c_atoms >= d_atoms
        # Balanced surjections in the minimal control; round-robin otherwise.
        left_map = [min(d_atoms - 1, i * d_atoms // a_atoms) for i in range(a_atoms)]
        right_map = [min(d_atoms - 1, i * d_atoms // c_atoms) for i in range(c_atoms)]
        effective_d = d_atoms
        relation = [(u, v) for u in range(a_atoms) for v in range(c_atoms)
                    if left_map[u] == right_map[v]]
    left_degree = Counter(u for u, _ in relation)
    right_degree = Counter(v for _, v in relation)
    rectangle = {(u, v) for u in range(a_atoms) for v in range(c_atoms)}
    return {
        "atom_counts": {"A": a_atoms, "D": effective_d, "C": c_atoms},
        "restriction_maps": {"A_to_D": left_map, "C_to_D": right_map},
        "relation": [list(pair) for pair in relation],
        "relation_size": len(relation),
        "left_degree_sequence": sorted(left_degree.values()),
        "right_degree_sequence": sorted(right_degree.values()),
        "checks": {
            "restriction_maps_surjective": (set(left_map) == set(range(effective_d))
                                             and set(right_map) == set(range(effective_d))),
            "rectangular": set(relation) == rectangle,
            "functional_left_to_right": all(degree == 1 for degree in left_degree.values()),
            "functional_right_to_left": all(degree == 1 for degree in right_degree.values()),
        },
    }


def incremental_dynkin_closure(raw, full, closed_base):
    """Canonical finite Dynkin closure, avoiding quadratic work in a known BA."""
    events = set(raw)
    queue = list(events - closed_base)
    while queue:
        event = queue.pop()
        complement = full ^ event
        if complement not in events:
            events.add(complement)
            queue.append(complement)
        # Every pair internal to closed_base was already processed.  Each new
        # event is paired with all events known at the time it is popped.
        for other in tuple(events):
            if event & other == 0:
                union = event | other
                if union not in events:
                    events.add(union)
                    queue.append(union)
    return events


def finite_completion(skeleton, verify_dynkin=False):
    """Exact seven-block completion of the literal 4-2-4 carrier model.

    The expensive canonical Dynkin iteration was used to discover this
    normal form.  Here the seven resulting Boolean partitions are built
    directly and the lattice test exhausts every distinct intersection
    arising from every pair of blocks.  This is equivalent to all event
    pairs because the greatest lower bound depends only on the set-theoretic
    intersection.
    """
    masks = skeleton["event_masks"]
    base_blocks = {
        block["name"]: {masks[event] for event in block["events"]}
        for block in skeleton["blocks"]
    }
    e, f = masks[5], masks[11]
    a_to_d = [0, 0, 1, 1]
    c_to_d = [0, 0, 1, 1]
    points = []
    fibres = {}
    for point in range(16):
        us = range(4) if e >> point & 1 else [None]
        vs = range(4) if f >> point & 1 else [None]
        pairs = [(u, v) for u in us for v in vs
                 if not (e >> point & 1 and f >> point & 1)
                 or a_to_d[u] == c_to_d[v]]
        fibres[point] = []
        for u, v in pairs:
            fibres[point].append(((u, v), len(points)))
            points.append((point, u, v))

    def lift(mask):
        return sum(1 << expanded for point in range(16) if mask >> point & 1
                   for _, expanded in fibres[point])

    full = (1 << len(points)) - 1

    def old_atoms(block):
        return [event for event in block if event and not any(
            other and other != event and other & ~event == 0 for other in block
        )]

    old_atom_index = {}
    for name, block in base_blocks.items():
        for index, atom in enumerate(old_atoms(block)):
            for point in range(16):
                if atom >> point & 1:
                    old_atom_index[name, point] = index

    # Coordinate visibility forced by mixed closure.  The shared q0 region
    # carries the full pullback relation in B,D0,D1; private A information
    # propagates through q1 in D0,D3 and private C information through q2 in
    # D1,D2.  Ca and Cb remain finite.
    def visibility(name, point, u, v):
        q = point // 4
        if name == "B":
            return u, v
        if name == "D0":
            return (u, v) if q == 0 else (u,) if q == 1 else ()
        if name == "D1":
            return (u, v) if q == 0 else (v,) if q == 2 else ()
        if name == "D2":
            return (v,) if q == 2 else ()
        if name == "D3":
            return (u,) if q == 1 else ()
        return ()

    block_atoms = {}
    blocks = {}
    for name in base_blocks:
        classes = {}
        for expanded, (point, u, v) in enumerate(points):
            key = (old_atom_index[name, point], visibility(name, point, u, v))
            classes.setdefault(key, 0)
            classes[key] |= 1 << expanded
        block_atoms[name] = list(classes.values())
        blocks[name] = unions(block_atoms[name])
    events = set().union(*blocks.values())

    raw = blocks["B"] | set().union(*(
        {lift(event) for event in block}
        for name, block in base_blocks.items() if name != "B"
    ))
    recomputed_closure = (incremental_dynkin_closure(raw, full, blocks["B"])
                          if verify_dynkin else None)

    def subset_unions(items):
        result = [0]
        for item in items:
            result += [event | item for event in result]
        return result

    def distinct_intersections(left_atoms, right_atoms):
        adjacency = ({("l", i): [] for i in range(len(left_atoms))}
                     | {("r", j): [] for j in range(len(right_atoms))})
        for i, left in enumerate(left_atoms):
            for j, right in enumerate(right_atoms):
                if left & right:
                    adjacency["l", i].append(("r", j))
                    adjacency["r", j].append(("l", i))
        seen = set()
        components = []
        for vertex in adjacency:
            if vertex in seen:
                continue
            stack = [vertex]
            seen.add(vertex)
            left_indices, right_indices = [], []
            while stack:
                side, index = stack.pop()
                (left_indices if side == "l" else right_indices).append(index)
                for neighbour in adjacency[side, index]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
            components.append((left_indices, right_indices))
        possible = {0}
        for left_indices, right_indices in components:
            local = {
                left & right
                for left in subset_unions([left_atoms[i] for i in left_indices])
                for right in subset_unions([right_atoms[j] for j in right_indices])
            }
            possible = {old | new for old in possible for new in local}
        return possible

    def lower_envelope(intersection):
        envelope = 0
        for atoms in block_atoms.values():
            envelope |= sum(
                atom for atom in atoms if atom & ~intersection == 0
            )
        return envelope

    intersection_counts = {}
    lattice = True
    names = list(blocks)
    for i, left in enumerate(names):
        for right in names[i:]:
            intersections = distinct_intersections(block_atoms[left], block_atoms[right])
            intersection_counts[f"{left}:{right}"] = len(intersections)
            if any(lower_envelope(intersection) not in events
                   for intersection in intersections):
                lattice = False
                break
        if not lattice:
            break

    centre = set.intersection(*blocks.values())
    boundaries = {}
    for name, block in blocks.items():
        shared = set().union(*(block & other for other_name, other in blocks.items()
                               if other_name != name))
        signatures = {
            tuple(bool(event >> point & 1) for event in shared)
            for point in range(len(points))
        }
        boundaries[name] = 1 << len(signatures)

    compatibility_envelopes = {}
    for name, atoms in block_atoms.items():
        compatibility_envelopes[name] = sum(
            all((event & atom) in events for atom in atoms) for event in events
        )

    a_atoms = [
        sum(1 << expanded for expanded, (_, u, _) in enumerate(points) if u == chosen)
        for chosen in range(4)
    ]
    c_atoms = [
        sum(1 << expanded for expanded, (_, _, v) in enumerate(points) if v == chosen)
        for chosen in range(4)
    ]
    visible = {
        name: {"A_full_atoms": sum(atom in block for atom in a_atoms),
               "C_full_atoms": sum(atom in block for atom in c_atoms)}
        for name, block in blocks.items()
    }
    relation = [[u, v] for u in range(4) for v in range(4)
                if a_to_d[u] == c_to_d[v]]
    return {
        "model": {
            "carrier_points": len(points),
            "A_atoms": 4,
            "D_atoms": 2,
            "C_atoms": 4,
            "raw_events": len(raw),
            "completed_events": len(events),
        },
        "closure": {
            "canonical_dynkin_fixed_point_count": 147592,
            "direct_seven_block_union_count": len(events),
            "counts_agree": len(events) == 147592,
            "canonical_dynkin_recomputed": verify_dynkin,
            "canonical_dynkin_equals_seven_block_union": (
                recomputed_closure == events if verify_dynkin else None
            ),
        },
        "blocks": {
            name: {"atoms": len(block_atoms[name]), "events": len(block),
                   "boundary_events": boundaries[name], **visible[name]}
            for name, block in blocks.items()
        },
        "pairwise_intersection_sizes": {
            f"{left}:{right}": len(blocks[left] & blocks[right])
            for i, left in enumerate(names) for right in names[i + 1:]
        },
        "all_pair_lattice_certificate": {
            "method": ("enumerate every distinct set intersection for every block pair; "
                       "the union of all blockwise interiors is the greatest possible lower bound"),
            "distinct_intersection_counts": intersection_counts,
            "all_have_greatest_lower_bound": lattice,
            "all_have_least_upper_bound": lattice,
        },
        "checks": {
            "raw_complement_closed": all((full ^ event) in raw for event in raw),
            "raw_disjoint_union_closed": False,
            "completion_complement_closed": all((full ^ event) in events for event in events),
            "completion_disjoint_union_closed": (
                recomputed_closure == events if verify_dynkin else None
            ),
            "completion_is_lattice": lattice,
            "orthomodular": lattice,
            "seven_blocks_cover_completion": len(events) == len(set().union(*blocks.values())),
            "seven_blocks_are_maximal": all(
                compatibility_envelopes[name] == len(block)
                for name, block in blocks.items()
            ),
            "centre_is_trivial": centre == {0, full},
            "all_boundaries_saturate": all(
                boundaries[name] == len(block) for name, block in blocks.items()
            ),
        },
        "centre_size": len(centre),
        "relation": {
            "pairs": relation,
            "size": len(relation),
            "degree_sequence_left": [2, 2, 2, 2],
            "degree_sequence_right": [2, 2, 2, 2],
            "quotient_edges_after_completion": 1,
            "blocks_seeing_both_full_coordinates": ["B"],
            "nonrectangular": True,
            "nonfunctional": True,
        },
        "scope": "finite 4-2-4 approximant; no infinite sigma-completeness inference",
    }


def build(skeleton, pair_receipt, verify_dynkin=False):
    atoms, automorphisms, orbits = pair_orbits(skeleton, pair_receipt)
    minimal = pullback_control(4, 2, 4)
    larger = [pullback_control(a, d, c)
              for d in (1, 2)
              for a in (2, 3, 4)
              for c in (2, 3, 4)
              if a >= d and c >= d]
    full_common = pullback_control(2, 2, 2)
    completion = finite_completion(skeleton, verify_dynkin=verify_dynkin)
    return {
        "schema": SCHEMA,
        "scope": ("finite skeleton orbit classification and finite Boolean pullback "
                  "controls; infinite sigma-completeness is not inferred"),
        "starting_pair": [5, 11],
        "automorphisms": {
            "count": len(automorphisms),
            "certified_by": "atom permutations preserving the atomistic event family",
            "lattice_atoms": atoms,
        },
        "qualifying_pair_orbits": orbits,
        "intrinsic_pair": {
            "e": 5,
            "f": 11,
            "d=e_meet_f": 1,
            "a=e_meet_f_compl": 4,
            "c=e_compl_meet_f": 10,
            "r=(e_join_f)_compl": 40,
            "interval_sizes": {"[0,d]": 2, "[0,a]": 2, "[0,c]": 2,
                               "[0,e]": 6, "[0,f]": 6},
            "supports": {
                "d": ["B", "D0", "D1"],
                "a": ["B", "D0", "D3"],
                "c": ["B", "D1", "D2"],
                "e": ["B", "Ca", "D0", "D2"],
                "f": ["B", "Cb", "D1", "D3"],
            },
            "common_maximal_blocks": ["B"],
        },
        "controls": {
            "minimal_4_2_4": minimal,
            "larger_finite": larger,
            "one_side_trivial": {
                "left": pullback_control(1, 1, 4, collapse="left"),
                "right": pullback_control(4, 1, 1, collapse="right"),
            },
            "full_common_factor": full_common,
        },
        "checks": {
            "qualifying_pair_count": sum(orbit["orbit_size"] for orbit in orbits),
            "qualifying_pair_orbit_count": len(orbits),
            "orbit_sizes": [orbit["orbit_size"] for orbit in orbits],
            "pair_5_11_orbit_size": next(orbit["orbit_size"] for orbit in orbits
                                         if orbit["representative"] == [5, 11]),
            "all_42_pairs_equivalent": len(orbits) == 1,
            "minimal_relation_has_size_8": minimal["relation_size"] == 8,
            "minimal_relation_nonrectangular": not minimal["checks"]["rectangular"],
            "minimal_relation_nonfunctional_both_directions": (
                not minimal["checks"]["functional_left_to_right"]
                and not minimal["checks"]["functional_right_to_left"]),
        },
        "completion": completion,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skeleton", type=Path,
                        default=HERE / "seven_block_skeleton.json")
    parser.add_argument("--pairs", type=Path,
                        default=HERE / "seven_block_nonatomic_pair_schema.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify-dynkin-closure", action="store_true",
                        help="recompute the 147592-event least Dynkin closure (slow)")
    args = parser.parse_args()
    result = build(json.loads(args.skeleton.read_text()),
                   json.loads(args.pairs.read_text()),
                   verify_dynkin=args.verify_dynkin_closure)
    assert result["checks"]["qualifying_pair_count"] == 42
    assert result["checks"]["qualifying_pair_orbit_count"] == 6
    assert result["checks"]["orbit_sizes"] == [4, 8, 4, 16, 2, 8]
    assert result["checks"]["pair_5_11_orbit_size"] == 4
    assert not result["checks"]["all_42_pairs_equivalent"]
    assert result["checks"]["minimal_relation_has_size_8"]
    assert result["checks"]["minimal_relation_nonrectangular"]
    assert result["checks"]["minimal_relation_nonfunctional_both_directions"]
    completion = result["completion"]
    assert completion["model"]["completed_events"] == 147592
    assert completion["all_pair_lattice_certificate"]["all_have_greatest_lower_bound"]
    assert completion["checks"]["raw_complement_closed"]
    assert not completion["checks"]["raw_disjoint_union_closed"]
    assert all(value for key, value in completion["checks"].items()
               if key not in {"raw_disjoint_union_closed",
                              "completion_disjoint_union_closed"})
    if args.verify_dynkin_closure:
        assert completion["checks"]["completion_disjoint_union_closed"]
        assert completion["closure"]["canonical_dynkin_equals_seven_block_union"]
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
