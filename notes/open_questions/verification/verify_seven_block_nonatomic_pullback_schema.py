#!/usr/bin/env python3
"""Independent checks for the non-atomic pullback finite receipt."""

import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).parent
skeleton = json.loads((HERE / "seven_block_skeleton.json").read_text())
pairs = json.loads((HERE / "seven_block_nonatomic_pair_schema.json").read_text())
receipt = json.loads((HERE / "seven_block_nonatomic_pullback_schema.json").read_text())

spec = importlib.util.spec_from_file_location(
    "cycle", HERE / "seven_block_two_fibre_cycle_audit.py"
)
cycle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cycle)

meet = skeleton["meet"]
successors, predecessors = cycle.cover_graph(meet)
bottom = next(x for x in successors if not predecessors[x])
atoms = sorted(successors[bottom])
atom_automorphisms = cycle.atom_automorphisms(meet, atoms)
assert len(atom_automorphisms) == 128

atom_masks = {
    event: sum(1 << i for i, atom in enumerate(atoms) if meet[atom][event] == atom)
    for event in range(len(meet))
}
event_by_atom_mask = {mask: event for event, mask in atom_masks.items()}


def image(automorphism, event):
    mask = atom_masks[event]
    mapped = sum(1 << automorphism[i] for i in range(len(atoms)) if mask >> i & 1)
    return event_by_atom_mask[mapped]


qualifying = {tuple(record["pair"]) for record in pairs["qualifying_pairs"]}
orbits = []
unseen = set(qualifying)
while unseen:
    representative = min(unseen)
    orbit = {
        tuple(sorted((image(automorphism, representative[0]),
                      image(automorphism, representative[1]))))
        for automorphism in atom_automorphisms
    }
    assert orbit <= qualifying
    orbits.append(orbit)
    unseen -= orbit

assert len(qualifying) == 42
assert len(orbits) == 6
assert [len(orbit) for orbit in orbits] == [4, 8, 4, 16, 2, 8]
assert sorted(next(orbit for orbit in orbits if (5, 11) in orbit)) == [
    (5, 11), (5, 44), (11, 50), (44, 50)
]

stored = receipt["qualifying_pair_orbits"]
assert [set(map(tuple, orbit["members"])) for orbit in stored] == orbits
assert receipt["checks"]["qualifying_pair_count"] == 42
assert receipt["checks"]["qualifying_pair_orbit_count"] == 6
assert receipt["checks"]["pair_5_11_orbit_size"] == 4
assert not receipt["checks"]["all_42_pairs_equivalent"]

control = receipt["controls"]["minimal_4_2_4"]
relation = set(map(tuple, control["relation"]))
expected = {(u, v) for u, v in itertools.product(range(4), repeat=2)
            if u // 2 == v // 2}
assert relation == expected
assert len(relation) == 8
assert {sum((u, v) in relation for v in range(4)) for u in range(4)} == {2}
assert {sum((u, v) in relation for u in range(4)) for v in range(4)} == {2}
assert not control["checks"]["rectangular"]
assert not control["checks"]["functional_left_to_right"]
assert not control["checks"]["functional_right_to_left"]

completion = receipt["completion"]
assert completion["model"] == {
    "A_atoms": 4, "C_atoms": 4, "D_atoms": 2,
    "carrier_points": 68, "raw_events": 131112,
    "completed_events": 147592,
}
assert {name: data["events"] for name, data in completion["blocks"].items()} == {
    "B": 131072, "D0": 16384, "D1": 16384,
    "D2": 128, "Ca": 16, "D3": 128, "Cb": 16,
}
assert completion["centre_size"] == 2
assert completion["checks"]["completion_is_lattice"]
assert completion["checks"]["completion_disjoint_union_closed"]
assert completion["checks"]["orthomodular"]
assert completion["checks"]["seven_blocks_are_maximal"]
assert completion["checks"]["centre_is_trivial"]
assert completion["checks"]["all_boundaries_saturate"]
assert completion["relation"]["size"] == 8
assert completion["relation"]["quotient_edges_after_completion"] == 1
assert completion["relation"]["blocks_seeing_both_full_coordinates"] == ["B"]
assert completion["closure"]["canonical_dynkin_recomputed"]
assert completion["closure"]["canonical_dynkin_equals_seven_block_union"]

print("PASS: 6 pair orbits; 147592-event 4-2-4 completion is a centre-free seven-block OML with one pullback edge")
