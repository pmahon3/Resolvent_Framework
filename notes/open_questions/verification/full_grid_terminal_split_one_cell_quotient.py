#!/usr/bin/env python3
"""Exact one-cell quotient test for the node-6 terminal PJH split control.

The carrier records a local state of cell 00 and the remaining shared q1,r1
bits, retaining precisely the information seen by the full node-6 profile
core and every event of cell 00. Multiplicities and the other cells' private
state data are quotiented out only after an exact compatibility-existence
test. This is the first rung of the physical coupling ladder.
"""
import argparse
import collections
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_core16_pjh_defect_atlas as atlas_mod
import full_grid_binary_pjh_split_core_audit as split_mod

SCHEMA = "full-grid-terminal-split-one-cell-quotient-v1"
NODE_ID = 6


def incremental_close(seed, full, cap=100_000):
    events = set(seed)
    arr = sorted(events)
    index = {x: i for i, x in enumerate(arr)}
    cursor = 0
    def add(x):
        if x not in index:
            index[x] = len(arr); arr.append(x); events.add(x)
            return True
        return False
    while cursor < len(arr):
        x = arr[cursor]
        add(full ^ x)
        if len(arr) > cap:
            return frozenset(events), False
        # Every unordered pair is processed when its later-added member is
        # reached. Newly appended events are handled in later cursor steps.
        for y in arr[:cursor]:
            if not x & y:
                add(x | y)
                if len(arr) > cap:
                    return frozenset(events), False
        cursor += 1
    return frozenset(events), True


def local_event_predicates(states):
    out = {0, (1 << len(states)) - 1}
    for block in cell.CELL_BLOCKS:
        for choice in range(1, 1 << len(block)):
            chosen = {block[i] for i in range(len(block)) if choice >> i & 1}
            mask = sum(1 << j for j, s in enumerate(states) if s & chosen)
            out.add(mask)
    return out


def payload():
    states = cell.cell_states()
    local_events_on_states = local_event_predicates(states)
    groups = collections.defaultdict(list)
    for j, s in enumerate(states):
        a = tuple(int(x in s) for x in cell.SHARED)
        q = int("e11" in s or "e10" in s)
        r = int("e11" in s or "e01" in s)
        groups[a, q, r].append(j)

    points = []
    for sidx, s in enumerate(states):
        a0 = tuple(int(x in s) for x in cell.SHARED)
        q0 = int("e11" in s or "e10" in s)
        r0 = int("e11" in s or "e01" in s)
        for q1 in (0, 1):
            for r1 in (0, 1):
                if not groups[a0, q0, r1]:
                    continue
                if not any(groups[a1, q1, r0] and groups[a1, q1, r1]
                           for a1 in set(k[0] for k in groups)):
                    continue
                points.append((sidx, a0, q0, q1, r0, r1))
    full = (1 << len(points)) - 1
    profile_masks = [0] * 16
    for j, (_, _, q0, q1, r0, r1) in enumerate(points):
        p = (q0 << 3) | (q1 << 2) | (r0 << 1) | r1
        profile_masks[p] |= 1 << j
    assert all(profile_masks)

    local_events = set()
    for event_states in local_events_on_states:
        local_events.add(sum(1 << j for j, pt in enumerate(points)
                             if event_states >> pt[0] & 1))

    source = json.load(open(os.path.join(HERE, atlas_mod.SOURCE)))
    node = next(x for x in source["payload"]["tree"] if x["id"] == NODE_ID)
    atlas = json.load(open(os.path.join(
        HERE, "full_grid_core16_pjh_defect_atlas.json")))
    rec = next(x for x in atlas["records"] if x["node_id"] == NODE_ID)
    low = int(rec["failed_lower_hex"], 16)
    high = int(rec["failed_upper_hex"], 16)
    entered = high & ~low
    assert entered == 1 << 15

    family16 = atlas_mod.close16(atlas_mod.raw16())
    for choice in node["path_choices_hex"]:
        z = int(choice, 16)
        family16 = atlas_mod.close16(family16 | {z, atlas_mod.FULL ^ z})

    # Enumerate the distinct nontrivial profile-1111 traces of actual cell-00
    # events, then choose the smallest trace having an off-activation point.
    p15 = profile_masks[15]
    traces = sorted({e & p15 for e in local_events
                     if e & p15 and (e & p15) != p15},
                    key=lambda x: (x.bit_count(), x))
    activation0 = sum(1 << j for j, pt in enumerate(points)
                      if pt[1] == (1, 1, 1))
    eligible = [s for s in traces if s & (full ^ activation0)]
    assert eligible
    split_piece = eligible[0]

    # Build the formal terminal and substitute its two split atoms by the
    # chosen physical trace and its complement within profile 1111.
    pulled16 = {split_mod.lift(e, 15) for e in family16}
    low17 = split_mod.lift(low, 15)
    formal_join = low17 | (1 << 15)
    formal_full = (1 << 17) - 1
    terminal17 = split_mod.close_logic(
        pulled16 | {formal_join, formal_full ^ formal_join}, formal_full)
    atom_masks = profile_masks[:15] + [split_piece, p15 & ~split_piece]
    def realize(formal):
        out = 0
        for i, atom in enumerate(atom_masks):
            if formal >> i & 1:
                out |= atom
        return out
    terminal_events = {realize(e) for e in terminal17}
    assert len(terminal_events) == len(terminal17) == 18432
    seed = terminal_events | local_events
    closed, completed = incremental_close(seed, full)
    hull = sum(profile_masks[p] for p in range(16) if high >> p & 1)
    defect_join = realize(formal_join)
    residue = hull & ~defect_join
    witness = [sum(profile_masks[p] for p in range(16)
                   if int(x, 16) >> p & 1) for x in rec["witness_pair_hex"]]
    witness_union = witness[0] | witness[1]
    actual_join = full
    for e in closed:
        if not witness_union & ~e:
            actual_join &= e
    signatures = {}
    sorted_closed = sorted(closed)
    for point in range(len(points)):
        signature = sum(1 << i for i, e in enumerate(sorted_closed)
                        if e >> point & 1)
        signatures.setdefault(signature, []).append(point)
    central_atoms = []
    # Recompute formal centre atoms using the already audited criterion.
    formal_set = set(terminal17)
    formal_centre = [x for x in terminal17 if all(
        split_mod.concrete_compatibility(x, y, formal_set) for y in terminal17)]
    for x in formal_centre:
        if x and not any(y and y != x and not y & ~x for y in formal_centre):
            central_atoms.append(realize(x))
    closed_set = set(closed)
    commuting_central_atoms = sum(all(
        split_mod.concrete_compatibility(c, e, closed_set)
        for e in local_events) for c in central_atoms)
    # A commutant is closed under complement and orthogonal joins, so it is
    # enough to test centrality against generators of the two closed families.
    formal_generators = {realize(split_mod.lift(e, 15))
                         for e in atlas_mod.raw16()}
    formal_generators.update(realize(split_mod.lift(int(x, 16), 15))
                             for x in node["path_choices_hex"])
    formal_generators.add(defect_join)
    generators = formal_generators | local_events
    centre = [x for x in closed if all(
        split_mod.concrete_compatibility(x, g, closed_set)
        for g in generators)]
    q0_mask = sum(1 << j for j, pt in enumerate(points) if pt[2])
    q1_mask = sum(1 << j for j, pt in enumerate(points) if pt[3])
    r0_mask = sum(1 << j for j, pt in enumerate(points) if pt[4])
    r1_mask = sum(1 << j for j, pt in enumerate(points) if pt[5])
    def boundary_reconstructed(x, y):
        return all(z in closed_set for z in
                   (x & y, x & ~y, ~x & y, full & ~x & ~y))
    activation_supported = [e for e in closed if e and not e & ~activation0]
    # Exact lattice audit. First certify that the old terminal remains a
    # sublattice: for every new event w, the old events below w have a greatest
    # member. Then only pairs involving a new event require direct checking.
    old_set = set(terminal_events)
    new_events = sorted(closed_set - old_set)
    old_sublattice_preserved = True
    for w in new_events:
        greatest_old_below = 0
        for e in terminal_events:
            if not e & ~w:
                greatest_old_below |= e
        if greatest_old_below not in old_set:
            old_sublattice_preserved = False
            break
    sorted_events = sorted(closed)
    event_index = {e: i for i, e in enumerate(sorted_events)}
    contains = [0] * len(points)
    for i, e in enumerate(sorted_events):
        bits = e
        while bits:
            lsb = bits & -bits
            contains[lsb.bit_length() - 1] |= 1 << i
            bits ^= lsb
    all_event_indices = (1 << len(sorted_events)) - 1
    principal_up = []
    for e in sorted_events:
        up = all_event_indices
        bits = e
        while bits:
            lsb = bits & -bits
            up &= contains[lsb.bit_length() - 1]
            bits ^= lsb
        principal_up.append(up)
    upset_to_event = {up: sorted_events[i] for i, up in enumerate(principal_up)}
    assert len(upset_to_event) == len(sorted_events)
    cross_failure = None
    tested_pairs = 0
    if old_sublattice_preserved:
        for x in new_events:
            ix = event_index[x]
            for y in sorted_events:
                tested_pairs += 1
                common_up = principal_up[ix] & principal_up[event_index[y]]
                if common_up not in upset_to_event:
                    cross_failure = {"kind": "join", "new_event": hex(x),
                                     "other_event": hex(y),
                                     "common_upper_set_sha256": hashlib.sha256(
                                         common_up.to_bytes(
                                             (len(sorted_events) + 7) // 8,
                                             "little")).hexdigest()}
                    break
            if cross_failure is not None:
                break
    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "quotient_points": len(points), "local_cell_states": len(states),
        "local_cell_events": len(local_events),
        "profile_1111_points": p15.bit_count(),
        "distinct_nontrivial_local_traces_on_profile_1111": len(traces),
        "selected_split_points": split_piece.bit_count(),
        "selected_split_sha256": hashlib.sha256(split_piece.to_bytes(
            (len(points) + 7) // 8, "little")).hexdigest(),
        "local_events_inducing_selected_trace_sha256": sorted(
            hashlib.sha256(e.to_bytes((len(points) + 7) // 8, "little")).hexdigest()
            for e in local_events if e & p15 == split_piece),
        "selected_split_has_off_row0_activation_point": bool(
            split_piece & (full ^ activation0)),
        "formal_terminal_events": len(terminal_events),
        "seed_events": len(seed), "closed_events": len(closed),
        "point_signature_classes": len(signatures),
        "point_signature_class_size_histogram": {str(k): v for k, v in sorted(
            collections.Counter(len(x) for x in signatures.values()).items())},
        "closure_completed_under_100000_events": completed,
        "residue_extracted": residue in closed,
        "hull_repaired": hull in closed,
        "defect_join_remains_witness_join": actual_join == defect_join,
        "formal_central_atoms": len(central_atoms),
        "central_atoms_commuting_with_all_restored_cell_events":
            commuting_central_atoms,
        "centre_events": len(centre),
        "centre_is_trivial": set(centre) == {0, full},
        "centre_sha256": hashlib.sha256(
            ",".join(map(str, sorted(centre))).encode()).hexdigest(),
        "row0_activation_cylinder_is_event": activation0 in closed_set,
        "nonzero_row0_activation_supported_events": len(activation_supported),
        "q_boundary_reconstructed": boundary_reconstructed(q0_mask, q1_mask),
        "r_boundary_reconstructed": boundary_reconstructed(r0_mask, r1_mask),
        "point_evaluations_order_separate_by_concreteness": True,
        "new_events_beyond_formal_terminal": len(new_events),
        "old_terminal_sublattice_preserved": old_sublattice_preserved,
        "first_exact_new_event_cut_failure": cross_failure,
        "new_event_pairs_tested": tested_pairs,
        "lattice": old_sublattice_preserved and cross_failure is None,
        "lattice_audit_scope": (
            "Exact: old-old pairs follow from the greatest-old-below test; "
            "every pair involving one of the new events is checked through "
            "principal-upper-set intersection. Complement closure supplies meets."),
        "scope": (
            "Exact one-cell quotient for node 6 and the smallest off-row0 "
            "cell-definable split trace. Closure is exact only if the reported "
            "cap flag passes. No other split trace, second cell, row1 activation, "
            "full-grid lattice, or sigma claim."),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_terminal_split_one_cell_quotient.py --verify"),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()
    out = payload()
    path = os.path.join(HERE, "full_grid_terminal_split_one_cell_quotient.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
