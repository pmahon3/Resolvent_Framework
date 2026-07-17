#!/usr/bin/env python3
"""Restricted-quotient eligibility gate for an actual Neg-023 K=0x8a transplant.

This producer proves only the pointed finite-quotient comparison.  It recovers
the exact 14-word ARR-CYL quotient and its right-only 12-event family, atomizes
that family, and enumerates every point permutation carrying it to the generic
eight-point split-selector base while preserving A, B, and H.  It computes the
exact profile atoms crossed by the clean one-point-inflated event K=0x8a and
transports the complete crossing signature through every pointed isomorphism.

The labelled-word multiplicity is not a physical-carrier multiplicity and is
not a full-old-cylinder refinement certificate.  Those are deliberately left
as the next eligibility gate.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_cyl_critical_sublattice_pilot.py"
SOURCE_RECEIPT = HERE / "arr_cyl_critical_sublattice_pilot.json"
RECEIPT = HERE / "arr_k8a_transplant_eligibility.json"
GENERIC_BASE = {0x00, 0x02, 0x0D, 0x31, 0x0F, 0x33,
                0xCC, 0xF0, 0xCE, 0xF2, 0xFD, 0xFF}
GENERIC_A, GENERIC_B, GENERIC_H = 0xF0, 0xCC, 0xFD
INFLATED_K = 0x8A


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()


def recover():
    source = SOURCE.read_text()
    needle = "    source=json.load(open(SOURCE_RECEIPT));ar_source=json.load(open(AR_RECEIPT))"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_K8A_ELIGIBILITY']={'atom_words':atom_words,"
        "'right_family':right_f,'right_masks':right_masks,'target':u_mask,"
        "'K':K,'kpos':kpos}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_k8a_eligibility"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_K8A_ELIGIBILITY"]


def quotient_atoms(data):
    family = sorted(data["right_family"])
    groups = {}
    for word_index, word in enumerate(data["atom_words"]):
        signature = tuple(int(bool(event & (1 << word_index))) for event in family)
        groups.setdefault(signature, []).append((word_index, tuple(word)))
    ordered = sorted(groups.values(), key=lambda group: group[0])
    word_to_atom = {word_index: atom for atom, group in enumerate(ordered)
                    for word_index, _ in group}

    def compress(mask):
        out = 0
        for word_index in range(len(data["atom_words"])):
            if mask & (1 << word_index):
                out |= 1 << word_to_atom[word_index]
        # Membership is constant on every atom.
        assert all(bool(mask & (1 << i)) == bool(out & (1 << word_to_atom[i]))
                   for i in range(len(data["atom_words"])))
        return out

    compressed = {compress(event) for event in family}
    kpos = data["kpos"]
    a = compress(data["right_masks"][kpos[15250]])
    b = compress(data["right_masks"][kpos[16786]])
    h = compress(data["target"])
    return ordered, compressed, a, b, h


def representation_atoms(family, point_count):
    groups = {}
    for point in range(point_count):
        signature = tuple(int(bool(event & (1 << point))) for event in sorted(family))
        groups.setdefault(signature, []).append(point)
    return sorted(groups.values(), key=lambda group: group[0])


def compress_on_atoms(mask, atoms):
    out = 0
    for atom, points in enumerate(atoms):
        values = {bool(mask & (1 << point)) for point in points}
        assert len(values) == 1
        if values.pop():
            out |= 1 << atom
    return out


def permute(mask, permutation):
    return sum(1 << permutation[i] for i in range(len(permutation))
               if mask & (1 << i))


def payload():
    data = recover()
    atoms, family, a, b, h = quotient_atoms(data)
    generic_atoms = representation_atoms(GENERIC_BASE, 8)
    generic_family = {compress_on_atoms(event, generic_atoms)
                      for event in GENERIC_BASE}
    generic_a = compress_on_atoms(GENERIC_A, generic_atoms)
    generic_b = compress_on_atoms(GENERIC_B, generic_atoms)
    generic_h = compress_on_atoms(GENERIC_H, generic_atoms)
    # Inflation sends points 1,2 to old point 1 and sends inflated p>=3 to
    # old p-1.  Record K's exact action on every generic base profile atom.
    old_of_inflated = [0, 1, 1, 2, 3, 4, 5, 6, 7]
    generic_crossing = []
    for generic_atom, old_points in enumerate(generic_atoms):
        inflated_points = [p for p, old in enumerate(old_of_inflated)
                           if old in old_points]
        selected = [p for p in inflated_points if INFLATED_K & (1 << p)]
        generic_crossing.append({
            "generic_atom": generic_atom,
            "old_points": list(old_points),
            "inflated_points": inflated_points,
            "k_selected_inflated_points": selected,
            "k_membership": (
                "empty" if not selected else
                "full" if len(selected) == len(inflated_points) else "proper"
            ),
        })
    crossed_generic_atoms = {
        row["generic_atom"] for row in generic_crossing
        if row["k_membership"] == "proper"
    }
    assert crossed_generic_atoms == {1, 2, 4}
    isomorphisms = []
    permutations = (itertools.permutations(range(len(atoms)))
                    if len(atoms) == len(generic_atoms) else ())
    for permutation in permutations:
        if permute(a, permutation) != generic_a:
            continue
        if permute(b, permutation) != generic_b:
            continue
        if permute(h, permutation) != generic_h:
            continue
        if {permute(event, permutation) for event in family} != generic_family:
            continue
        transported_atoms = []
        selector_count = 1
        for actual_atom, labelled_words in enumerate(atoms):
            generic_atom = permutation[actual_atom]
            generic_row = generic_crossing[generic_atom]
            crossed = generic_atom in crossed_generic_atoms
            choices = (2 ** len(labelled_words) - 2) if crossed else 1
            selector_count *= choices
            transported_atoms.append({
                "actual_atom": actual_atom,
                "generic_atom": generic_atom,
                "generic_k_membership": generic_row["k_membership"],
                "requires_proper_split": crossed,
                "proper_nonempty_labelled_word_subset_count": choices,
                "labelled_word_count": len(labelled_words),
                "labelled_words": [
                    {"word_index": index, "word": list(word)}
                    for index, word in labelled_words
                ],
            })
        crossed_actual = [row for row in transported_atoms
                          if row["requires_proper_split"]]
        isomorphisms.append({
            "actual_to_generic_permutation": list(permutation),
            "transported_atoms": transported_atoms,
            "crossed_actual_atoms": [row["actual_atom"] for row in crossed_actual],
            "all_crossed_atoms_labelled_word_split_eligible": all(
                row["labelled_word_count"] >= 2 for row in crossed_actual
            ),
            "labelled_word_level_selector_count": selector_count,
        })
    source_receipt = json.loads(SOURCE_RECEIPT.read_text())
    result = {
        "schema": "arr-k8a-transplant-eligibility-v2",
        "schema_version": "2.0",
        "source_payload_sha256": source_receipt["payload_sha256"],
        "realized_labelled_word_count": len(data["atom_words"]),
        "right_only_event_count": len(data["right_family"]),
        "right_only_atom_count": len(atoms),
        "right_only_atom_labelled_word_multiplicities": [len(x) for x in atoms],
        "generic_representation_atom_count": len(generic_atoms),
        "generic_representation_atom_point_multiplicities": [len(x) for x in generic_atoms],
        "inflated_clean_k_hex": hex(INFLATED_K),
        "generic_k_crossing_signature": generic_crossing,
        "generic_k_crossed_atom_count": len(crossed_generic_atoms),
        "pointed_isomorphism_count": len(isomorphisms),
        "pointed_isomorphisms": isomorphisms,
        "restricted_eligibility": bool(isomorphisms) and any(
            row["all_crossed_atoms_labelled_word_split_eligible"]
            for row in isomorphisms
        ),
        "literal_carrier_transplant_obstruction": (
            None if isomorphisms else
            "The right-only actual concrete representation has a different "
            "pointed representation type from the generic control, so the "
            "profile-level K=0x8a transplant is unavailable."
        ),
        "scope": (
            "Exact atomization and pointed-isomorphism census for the 14-word "
            "right-only restricted Neg-023 quotient, including the complete "
            "three-profile crossing signature of clean inflated K=0x8a. "
            "Labelled-word subset choices are not physical-carrier subsets and "
            "do not certify survival under both full old cylinder copies. No "
            "transplant closure, lattice, centre, state, sigma, "
            "ODBC, or Phi conclusion."
        ),
        "next_gate": (
            "Refine all three transported crossed atoms by the complete labelled "
            "signature of both full old cylinder copies and prove completeness "
            "of that signature. Each crossed atom must retain a proper nonempty "
            "physical split, and the three choices must combine to one event "
            "with the transported empty/full memberships on the other atoms."
        ),
        "evidence_class": "Executable verified — exhaustive finite scope",
        "verification_independence": "One deterministic implementation; source quotient producer reused.",
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": "PYTHONHASHSEED=0 python3 notes/open_questions/verification/arr_k8a_transplant_eligibility.py --verify",
    }
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
        assert json.loads(RECEIPT.read_text()) == result
    print(json.dumps({
        "status": "PASS",
        "payload_sha256": result["payload_sha256"],
        "pointed_isomorphisms": result["pointed_isomorphism_count"],
        "restricted_eligibility": result["restricted_eligibility"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
