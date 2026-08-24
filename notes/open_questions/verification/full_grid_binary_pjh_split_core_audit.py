#!/usr/bin/env python3
"""Audit the formal 17-atom core of every binary first-PJH defect.

For each of the thirty binary nodes in the certified profile-hull atlas, split
the unique entered profile atom into two nonempty formal atoms.  Pull back the
node's whole 16-atom concrete logic, adjoin the putative defect join consisting
of the full lower word plus one of the two split atoms, and close under
complement and disjoint union.  This is an exact finite set-logic calculation;
it does not assert that either formal split is realizable inside a physical
full-grid fibre, and it carries no activation labels within that fibre.
"""
import argparse
import collections
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ATLAS = "full_grid_core16_pjh_defect_atlas.json"
SCHEMA = "full-grid-binary-pjh-split-core-v1"


def digest(obj):
    return hashlib.sha256(json.dumps(
        obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def close_logic(seed, full):
    events = set(seed)
    while True:
        old = tuple(events)
        new = {full ^ x for x in old}
        for i, x in enumerate(old):
            for y in old[i:]:
                if not x & y:
                    new.add(x | y)
        new -= events
        if not new:
            return frozenset(events)
        events.update(new)


def lift(mask, split_profile):
    """Replace split_profile by two adjacent formal atoms, preserving order."""
    below = mask & ((1 << split_profile) - 1)
    above = mask >> (split_profile + 1)
    doubled = 3 << split_profile if mask & (1 << split_profile) else 0
    return below | doubled | (above << (split_profile + 2))


def lattice_audit(events, atoms=17):
    """Exact lattice test using zeta/Mobius transforms on the subset cube.

    `or_count[s]` is the number of ordered event pairs with literal union s.
    `upper_hull[s]` is the intersection of all event supersets of s.  A join
    exists exactly when upper_hull[s] is an event for every realized pair-union
    s. Complement closure then supplies the dual meet statement.
    """
    size = 1 << atoms
    full = size - 1
    event_set = set(events)
    subset_count = [0] * size
    upper_hull = [full] * size
    for e in events:
        subset_count[e] = 1
        upper_hull[e] = e
    for bit_index in range(atoms):
        bit = 1 << bit_index
        for mask in range(size):
            if mask & bit:
                subset_count[mask] += subset_count[mask ^ bit]
            else:
                upper_hull[mask] &= upper_hull[mask | bit]
    or_count = [n * n for n in subset_count]
    for bit_index in range(atoms):
        bit = 1 << bit_index
        for mask in range(size):
            if mask & bit:
                or_count[mask] -= or_count[mask ^ bit]
    failing_union = next((s for s, n in enumerate(or_count)
                          if n and upper_hull[s] not in event_set), None)
    witness = None
    if failing_union is not None:
        candidates = [e for e in events if not e & ~failing_union]
        for x in candidates:
            y = next((e for e in candidates if x | e == failing_union), None)
            if y is not None:
                witness = [hex(x), hex(y)]
                break
    return {
        "lattice": failing_union is None,
        "first_failed_literal_union": (None if failing_union is None
                                         else hex(failing_union)),
        "first_failed_pair": witness,
        "first_failed_upper_intersection": (None if failing_union is None else
                                              hex(upper_hull[failing_union])),
    }


def concrete_compatibility(x, y, event_set):
    """Compatibility criterion for a complement/orthogonal-union set logic."""
    return ((x & y) in event_set and (x & ~y) in event_set and
            (y & ~x) in event_set)


def structural_audit(events, full):
    event_set = set(events)
    centre = []
    for x in sorted(events):
        if all(concrete_compatibility(x, y, event_set) for y in events):
            centre.append(x)
    atoms = []
    for x in sorted(events):
        if x and not any(y and y != x and not y & ~x for y in events):
            atoms.append(x)
    point_signatures = {tuple(bool(e & (1 << p)) for e in events)
                        for p in range(17)}
    centre_atoms = [x for x in centre if x and not any(
        y and y != x and not y & ~x for y in centre)]
    centre_interval_sizes = [sum(not e & ~c for e in events)
                             for c in centre_atoms]
    return {
        "centre_events": len(centre),
        "centre_sha256": hashlib.sha256(
            ",".join(map(str, centre)).encode()).hexdigest(),
        "centre_sample": [hex(x) for x in centre[:16]],
        "centre_is_trivial": centre == [0, full],
        "centre_atoms": len(centre_atoms),
        "central_factor_interval_sizes": sorted(centre_interval_sizes),
        "central_factor_sizes_match_B9_times_MO2_squared": (
            sorted(centre_interval_sizes) == [2] * 9 + [6] * 2),
        "lattice_atoms": len(atoms),
        "lattice_atom_sizes": {str(k): v for k, v in sorted(
            collections.Counter(x.bit_count() for x in atoms).items())},
        "distinct_point_state_signatures": len(point_signatures),
        "formal_carrier_is_point_reduced": len(point_signatures) == 17,
        "point_evaluations_order_separate_by_concreteness": True,
    }


def side_atoms(side, split_profile):
    # Profile bit order is q0,q1,r0,r1 from most to least significant.
    shifts = (3, 2) if side == "q" else (1, 0)
    out = []
    for a in (0, 1):
        for b in (0, 1):
            word = sum(1 << p for p in range(16)
                       if ((p >> shifts[0]) & 1) == a and
                          ((p >> shifts[1]) & 1) == b)
            out.append(lift(word, split_profile))
    return out


def payload():
    atlas = json.load(open(os.path.join(HERE, ATLAS)))
    cases = []
    for rec in atlas["records"]:
        if rec["gap_bits"] != 1:
            continue
        low = int(rec["failed_lower_hex"], 16)
        high = int(rec["failed_upper_hex"], 16)
        entered_word = high & ~low
        assert entered_word.bit_count() == 1
        p = entered_word.bit_length() - 1
        family16 = None
        # Reconstruct the node family through the atlas module, avoiding any
        # reliance on a serialized event list that the receipt does not store.
        import full_grid_core16_pjh_defect_atlas as atlas_module
        source = json.load(open(os.path.join(HERE, atlas_module.SOURCE)))
        tree = source["payload"]["tree"]
        node = next(n for n in tree if n["id"] == rec["node_id"])
        family16 = atlas_module.close16(atlas_module.raw16())
        for choice in node["path_choices_hex"]:
            z16 = int(choice, 16)
            family16 = atlas_module.close16(family16 | {z16, atlas_module.FULL ^ z16})
        assert len(family16) == rec["events_in_profile_family"]

        full17 = (1 << 17) - 1
        pulled = {lift(e, p) for e in family16}
        low17 = lift(low, p)
        split0 = 1 << p
        split1 = 1 << (p + 1)
        defect_join = low17 | split0
        closed = close_logic(pulled | {defect_join, full17 ^ defect_join}, full17)
        witness = [lift(int(x, 16), p) for x in rec["witness_pair_hex"]]
        witness_union = witness[0] | witness[1]
        witness_join = full17
        for e in closed:
            if not witness_union & ~e:
                witness_join &= e
        if witness_join not in closed:
            witness_join = None
        hull17 = lift(high, p)
        lattice_result = lattice_audit(closed)
        structure = structural_audit(closed, full17) if lattice_result["lattice"] else None
        q_atoms = side_atoms("q", p)
        r_atoms = side_atoms("r", p)
        case = {
            "node_id": rec["node_id"], "depth": rec["depth"],
            "split_profile": p,
            "profile_family_events": len(family16),
            "pulled_events": len(pulled), "closed_events": len(closed),
            "defect_join": hex(defect_join),
            "split_atom_complement_choice": hex(low17 | split1),
            "split_atoms_are_events": [split0 in closed, split1 in closed],
            "defect_hull_is_absent": hull17 not in closed,
            "defect_join_remains_witness_join": witness_join == defect_join,
            "actual_witness_join": None if witness_join is None else hex(witness_join),
            "q_boundary_reconstructed": all(a in closed for a in q_atoms),
            "r_boundary_reconstructed": all(a in closed for a in r_atoms),
            **lattice_result,
            "terminal_structure": structure,
            "event_family_sha256": hashlib.sha256(
                ",".join(map(str, sorted(closed))).encode()).hexdigest(),
        }
        cases.append(case)
    assert len(cases) == 30
    histogram = collections.Counter(
        (c["closed_events"], c["defect_hull_is_absent"],
         c["defect_join_remains_witness_join"],
         c["q_boundary_reconstructed"], c["r_boundary_reconstructed"],
         c["lattice"])
        for c in cases)
    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "source_atlas": ATLAS,
        "source_atlas_payload_sha256": atlas["payload_sha256"],
        "binary_cases": len(cases),
        "cases": cases,
        "outcome_histogram": [
            {"closed_events": k[0], "defect_hull_is_absent": k[1],
             "defect_join_remains_witness_join": k[2],
             "q_boundary_reconstructed": k[3],
             "r_boundary_reconstructed": k[4], "lattice": k[5], "cases": v}
            for k, v in sorted(histogram.items())],
        "scope": (
            "Exact complement/disjoint-union closure and lattice audit on the "
            "formal 17-atom split-profile cores for the thirty binary atlas "
            "defects, including an exact all-pairs lattice decision by subset "
            "zeta/Mobius transform. "
            "No physical-fibre realization, activation classification, terminal "
            "completion, larger-carrier, or sigma-limit claim."),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_binary_pjh_split_core_audit.py --verify"),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = digest(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()
    out = payload()
    path = os.path.join(HERE, "full_grid_binary_pjh_split_core_audit.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps({"status": "PASS", "payload_sha256": out["payload_sha256"],
                      "binary_cases": out["binary_cases"],
                      "outcome_histogram": out["outcome_histogram"]},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
