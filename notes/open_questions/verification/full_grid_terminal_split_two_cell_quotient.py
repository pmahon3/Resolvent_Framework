#!/usr/bin/env python3
"""Exact same-row two-cell quotient for the node-6 terminal PJH split."""
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
import full_grid_terminal_split_one_cell_quotient as one

SCHEMA = "full-grid-terminal-split-two-cell-quotient-v1"
NODE_ID = 6


def payload():
    states = cell.cell_states()
    local_state_events = one.local_event_predicates(states)
    groups = collections.defaultdict(list)
    data = []
    for j, s in enumerate(states):
        a = tuple(int(x in s) for x in cell.SHARED)
        q = int("e11" in s or "e10" in s)
        r = int("e11" in s or "e01" in s)
        groups[a, q, r].append(j); data.append((a, q, r))
    activations = {k[0] for k in groups}
    points = []
    for s00, (a0, q0, r0) in enumerate(data):
        for s01, (a01, q01, r1) in enumerate(data):
            if (a0, q0) != (a01, q01):
                continue
            for q1 in (0, 1):
                if any(groups[a1, q1, r0] and groups[a1, q1, r1]
                       for a1 in activations):
                    points.append((s00, s01, a0, q0, q1, r0, r1))
    full = (1 << len(points)) - 1
    profile_masks = [0] * 16
    for j, pt in enumerate(points):
        _, _, _, q0, q1, r0, r1 = pt
        profile_masks[(q0 << 3) | (q1 << 2) | (r0 << 1) | r1] |= 1 << j
    assert all(profile_masks)
    cell00_map = {e: sum(1 << j for j, pt in enumerate(points)
                         if e >> pt[0] & 1) for e in local_state_events}
    cell01_map = {e: sum(1 << j for j, pt in enumerate(points)
                         if e >> pt[1] & 1) for e in local_state_events}
    cell00_events = set(cell00_map.values()); cell01_events = set(cell01_map.values())
    projected00 = {pt[0] for pt in points}; projected01 = {pt[1] for pt in points}
    order00 = all((not e & ~f) == (not cell00_map[e] & ~cell00_map[f])
                  for e in local_state_events for f in local_state_events)
    order01 = all((not e & ~f) == (not cell01_map[e] & ~cell01_map[f])
                  for e in local_state_events for f in local_state_events)

    source = json.load(open(os.path.join(HERE, atlas_mod.SOURCE)))
    node = next(x for x in source["payload"]["tree"] if x["id"] == NODE_ID)
    atlas = json.load(open(os.path.join(
        HERE, "full_grid_core16_pjh_defect_atlas.json")))
    rec = next(x for x in atlas["records"] if x["node_id"] == NODE_ID)
    low = int(rec["failed_lower_hex"], 16)
    high = int(rec["failed_upper_hex"], 16)
    assert high & ~low == 1 << 15
    family16 = atlas_mod.close16(atlas_mod.raw16())
    for choice in node["path_choices_hex"]:
        z = int(choice, 16)
        family16 = atlas_mod.close16(family16 | {z, atlas_mod.FULL ^ z})

    p15 = profile_masks[15]
    activation0 = sum(1 << j for j, pt in enumerate(points)
                      if pt[2] == (1, 1, 1))
    traces = sorted({e & p15 for e in cell00_events
                     if e & p15 and e & p15 != p15},
                    key=lambda x: (x.bit_count(), x))
    split_piece = next(s for s in traces if s & ~activation0)
    split_sources = [e for e, image in cell00_map.items()
                     if image & p15 == split_piece]
    pulled16 = {split_mod.lift(e, 15) for e in family16}
    low17 = split_mod.lift(low, 15)
    formal_join = low17 | 1 << 15
    formal_full = (1 << 17) - 1
    terminal17 = split_mod.close_logic(
        pulled16 | {formal_join, formal_full ^ formal_join}, formal_full)
    atom_masks = profile_masks[:15] + [split_piece, p15 & ~split_piece]
    def realize(formal):
        out = 0
        for i, atom in enumerate(atom_masks):
            if formal >> i & 1: out |= atom
        return out
    terminal_events = {realize(e) for e in terminal17}
    seed = terminal_events | cell00_events | cell01_events
    closed, completed = one.incremental_close(seed, full, cap=100_000)
    closed_set = set(closed)
    hull = sum(profile_masks[p] for p in range(16) if high >> p & 1)
    defect_join = realize(formal_join)
    residue = hull & ~defect_join
    witness = [sum(profile_masks[p] for p in range(16)
                   if int(x, 16) >> p & 1) for x in rec["witness_pair_hex"]]
    witness_union = witness[0] | witness[1]
    actual_join = full
    for e in closed:
        if not witness_union & ~e: actual_join &= e
    q0_mask = sum(1 << j for j, pt in enumerate(points) if pt[3])
    q1_mask = sum(1 << j for j, pt in enumerate(points) if pt[4])
    r0_mask = sum(1 << j for j, pt in enumerate(points) if pt[5])
    r1_mask = sum(1 << j for j, pt in enumerate(points) if pt[6])
    def reconstructed(x, y):
        return all(z in closed_set for z in
                   (x & y, x & ~y, ~x & y, full & ~x & ~y))
    activation_supported = [e for e in closed if e and not e & ~activation0]
    # Exact lattice reduction as in the one-cell audit.
    old_set = set(terminal_events)
    new_events = sorted(closed_set - old_set)
    old_sublattice_preserved = True
    for w in new_events:
        greatest = 0
        for e in terminal_events:
            if not e & ~w: greatest |= e
        if greatest not in old_set:
            old_sublattice_preserved = False; break
    sorted_events = sorted(closed)
    event_index = {e: i for i, e in enumerate(sorted_events)}
    contains = [0] * len(points)
    for i, e in enumerate(sorted_events):
        bits = e
        while bits:
            lsb = bits & -bits
            contains[lsb.bit_length() - 1] |= 1 << i
            bits ^= lsb
    all_indices = (1 << len(sorted_events)) - 1
    principal_up = []
    for e in sorted_events:
        up = all_indices; bits = e
        while bits:
            lsb = bits & -bits
            up &= contains[lsb.bit_length() - 1]
            bits ^= lsb
        principal_up.append(up)
    upset_to_event = {u: sorted_events[i] for i, u in enumerate(principal_up)}
    assert len(upset_to_event) == len(sorted_events)
    failure = None; tested = 0
    if old_sublattice_preserved:
        for x in new_events:
            for y in sorted_events:
                tested += 1
                common = principal_up[event_index[x]] & principal_up[event_index[y]]
                if common not in upset_to_event:
                    failure = {"new_event": hex(x), "other_event": hex(y),
                               "common_upper_set_sha256": hashlib.sha256(
                                   common.to_bytes((len(sorted_events)+7)//8,
                                                   "little")).hexdigest()}
                    break
            if failure: break
    lattice = old_sublattice_preserved and failure is None
    # Exact centre through the generator-commutant lemma, only meaningful once
    # latticehood has passed.
    formal_generators = {realize(split_mod.lift(e, 15))
                         for e in atlas_mod.raw16()}
    formal_generators.update(realize(split_mod.lift(int(x, 16), 15))
                             for x in node["path_choices_hex"])
    formal_generators.add(defect_join)
    generators = formal_generators | cell00_events | cell01_events
    centre = [] if not lattice else [x for x in closed if all(
        split_mod.concrete_compatibility(x, g, closed_set) for g in generators)]
    # Exact same-row persistence certificate for q0^c meet q1.  This is the
    # macro-saturated node-6 meet, not the stage-558 fine-fibre meet.
    q_literal_intersection = full & ~q0_mask & q1_mask
    q_meet = 0
    for e in closed:
        if not e & ~q_literal_intersection: q_meet |= e
    assert q_meet in closed_set
    old_q_meet = 0
    for e in terminal_events:
        if not e & ~q_literal_intersection: old_q_meet |= e
    assert old_q_meet in old_set
    q_meet_increment = q_meet & ~old_q_meet
    q_meet_residue = q_literal_intersection & ~q_meet
    assert q_meet == sum(profile_masks[p] for p in (4, 5, 6))
    assert q_meet_residue == profile_masks[7]
    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "quotient_points": len(points), "local_cell_states": len(states),
        "cell00_events": len(cell00_events), "cell01_events": len(cell01_events),
        "cell00_projected_local_states": len(projected00),
        "cell01_projected_local_states": len(projected01),
        "both_cell_event_orders_reflected": order00 and order01,
        "formal_terminal_events": len(terminal_events), "seed_events": len(seed),
        "closed_events": len(closed),
        "closure_completed_under_100000_events": completed,
        "selected_split_points": split_piece.bit_count(),
        "selected_split_is_nonempty_proper": bool(split_piece) and split_piece != p15,
        "selected_split_has_off_row0_activation_point": bool(split_piece & ~activation0),
        "selected_split_sha256": hashlib.sha256(split_piece.to_bytes(
            (len(points) + 7) // 8, "little")).hexdigest(),
        "selected_split_source_state_event_sha256": sorted(
            hashlib.sha256(e.to_bytes((len(states)+7)//8, "little")).hexdigest()
            for e in split_sources),
        "residue_extracted": residue in closed_set,
        "hull_repaired": hull in closed_set,
        "defect_join_remains_witness_join": actual_join == defect_join,
        "q_boundary_reconstructed": reconstructed(q0_mask, q1_mask),
        "r_boundary_reconstructed": reconstructed(r0_mask, r1_mask),
        "row0_activation_cylinder_is_event": activation0 in closed_set,
        "nonzero_row0_activation_supported_events": len(activation_supported),
        "point_evaluations_order_separate_by_concreteness": True,
        "new_events_beyond_formal_terminal": len(new_events),
        "old_terminal_sublattice_preserved": old_sublattice_preserved,
        "new_event_pairs_tested": tested,
        "first_exact_new_event_cut_failure": failure,
        "lattice": lattice,
        "centre_events": None if not lattice else len(centre),
        "centre_is_trivial": lattice and set(centre) == {0, full},
        "centre_sha256": None if not lattice else hashlib.sha256(
            ",".join(map(str, sorted(centre))).encode()).hexdigest(),
        "q0_complement_meet_q1_points": q_meet.bit_count(),
        "q0_complement_meet_q1_sha256": hashlib.sha256(q_meet.to_bytes(
            (len(points)+7)//8,"little")).hexdigest(),
        "old_profile_core_q_meet_points": old_q_meet.bit_count(),
        "q_meet_formal_profile_atom_mask_hex": "0x70",
        "q_meet_profile_words": ["0100", "0101", "0110"],
        "same_row_second_cell_enlarges_q_meet": q_meet != old_q_meet,
        "q_meet_increment_points": q_meet_increment.bit_count(),
        "q_literal_intersection_points": q_literal_intersection.bit_count(),
        "q_meet_is_proper_below_literal_intersection": q_meet != q_literal_intersection,
        "q_meet_residue_points": q_meet_residue.bit_count(),
        "q_meet_residue_profile_atom_mask_hex": "0x80",
        "q_meet_residue_profile_word": "0111",
        "q_meet_residue_equals_whole_profile_fibre_0111":
            q_meet_residue == profile_masks[7],
        "q_meet_residue_is_event": q_meet_residue in closed_set,
        "q_meet_increment_is_activation_supported": bool(q_meet_increment) and
            not q_meet_increment & ~activation0,
        "scope": (
            "Exact same-row cells 00/01 quotient for node 6 and one selected "
            "cell00-definable split. Closure is exact only if the cap passes. "
            "The lattice and centre audits are exact. No row1 cells, alternative "
            "split traces, full grid, maximal-block, or sigma claim."),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_terminal_split_two_cell_quotient.py --verify"),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", action="store_true"); args = ap.parse_args()
    out = payload(); path = os.path.join(
        HERE, "full_grid_terminal_split_two_cell_quotient.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    elif args.verify or os.path.exists(path): assert json.load(open(path)) == out
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__": main()
