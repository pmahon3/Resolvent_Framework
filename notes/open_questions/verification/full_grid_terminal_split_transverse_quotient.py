#!/usr/bin/env python3
"""Exact transverse cells-00/10 quotient for the node-6 PJH split."""
import argparse, collections, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_core16_pjh_defect_atlas as atlas_mod
import full_grid_binary_pjh_split_core_audit as split_mod
import full_grid_terminal_split_one_cell_quotient as one

SCHEMA = "full-grid-terminal-split-transverse-quotient-v1"
NODE_ID = 6


def payload():
    states = cell.cell_states(); local_state_events = one.local_event_predicates(states)
    groups = collections.defaultdict(list); data = []
    for j, s in enumerate(states):
        a = tuple(int(x in s) for x in cell.SHARED)
        q = int("e11" in s or "e10" in s)
        r = int("e11" in s or "e01" in s)
        groups[a, q, r].append(j); data.append((a, q, r))
    points = []
    for s00, (a0, q0, r0) in enumerate(data):
        for s10, (a1, q1, r10) in enumerate(data):
            if r0 != r10: continue
            for r1 in (0, 1):
                if groups[a0, q0, r1] and groups[a1, q1, r1]:
                    points.append((s00, s10, a0, a1, q0, q1, r0, r1))
    full = (1 << len(points)) - 1
    profile_masks = [0] * 16
    for j, pt in enumerate(points):
        p = (pt[4] << 3) | (pt[5] << 2) | (pt[6] << 1) | pt[7]
        profile_masks[p] |= 1 << j
    assert all(profile_masks)
    cell00_map = {e: sum(1 << j for j, pt in enumerate(points) if e >> pt[0] & 1)
                  for e in local_state_events}
    cell10_map = {e: sum(1 << j for j, pt in enumerate(points) if e >> pt[1] & 1)
                  for e in local_state_events}
    cell00_events = set(cell00_map.values()); cell10_events = set(cell10_map.values())
    projected00 = {pt[0] for pt in points}; projected10 = {pt[1] for pt in points}
    order00 = all((not e & ~f) == (not cell00_map[e] & ~cell00_map[f])
                  for e in local_state_events for f in local_state_events)
    order10 = all((not e & ~f) == (not cell10_map[e] & ~cell10_map[f])
                  for e in local_state_events for f in local_state_events)

    source = json.load(open(os.path.join(HERE, atlas_mod.SOURCE)))
    node = next(x for x in source["payload"]["tree"] if x["id"] == NODE_ID)
    atlas = json.load(open(os.path.join(HERE, "full_grid_core16_pjh_defect_atlas.json")))
    rec = next(x for x in atlas["records"] if x["node_id"] == NODE_ID)
    low = int(rec["failed_lower_hex"], 16); high = int(rec["failed_upper_hex"], 16)
    assert high & ~low == 1 << 15
    family16 = atlas_mod.close16(atlas_mod.raw16())
    for choice in node["path_choices_hex"]:
        z = int(choice, 16)
        family16 = atlas_mod.close16(family16 | {z, atlas_mod.FULL ^ z})

    p15 = profile_masks[15]
    activation0 = sum(1 << j for j, pt in enumerate(points) if pt[2] == (1,1,1))
    activation1 = sum(1 << j for j, pt in enumerate(points) if pt[3] == (1,1,1))
    traces = sorted({e & p15 for e in cell00_events if e & p15 and e & p15 != p15},
                    key=lambda x: (x.bit_count(), x))
    split_piece = next(s for s in traces if s & ~activation0 and s & ~activation1)
    split_sources = [e for e, image in cell00_map.items() if image & p15 == split_piece]
    pulled16 = {split_mod.lift(e, 15) for e in family16}
    low17 = split_mod.lift(low, 15); formal_join = low17 | 1 << 15
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
    seed = terminal_events | cell00_events | cell10_events
    closed, completed = one.incremental_close(seed, full, cap=100_000)
    closed_set = set(closed)
    hull = sum(profile_masks[p] for p in range(16) if high >> p & 1)
    defect_join = realize(formal_join); residue = hull & ~defect_join
    witness = [sum(profile_masks[p] for p in range(16) if int(x,16) >> p & 1)
               for x in rec["witness_pair_hex"]]
    actual_join = full
    for e in closed:
        if not (witness[0] | witness[1]) & ~e: actual_join &= e
    q0 = sum(1 << j for j, pt in enumerate(points) if pt[4])
    q1 = sum(1 << j for j, pt in enumerate(points) if pt[5])
    r0 = sum(1 << j for j, pt in enumerate(points) if pt[6])
    r1 = sum(1 << j for j, pt in enumerate(points) if pt[7])
    def reconstructed(x,y):
        return all(z in closed_set for z in (x&y, x&~y, ~x&y, full&~x&~y))
    act0 = [e for e in closed if e and not e & ~activation0]
    act1 = [e for e in closed if e and not e & ~activation1]
    # Exact lattice audit exploiting the 17-atom old normal form. Only 128
    # physical events are new, so principal upsets need no point-level table.
    old_set = set(terminal_events); new_events = sorted(closed_set - old_set)
    realized_to_formal = {realize(f): f for f in terminal17}
    assert len(realized_to_formal) == len(terminal17)
    old_sorted = sorted(old_set); new_sorted = new_events
    old_index = {e:i for i,e in enumerate(old_sorted)}
    old_contains_atom = [0] * 17
    for i,e in enumerate(old_sorted):
        f = realized_to_formal[e]
        for a in range(17):
            if f >> a & 1: old_contains_atom[a] |= 1 << i
    all_old = (1 << len(old_sorted)) - 1
    def old_uppers_for_physical(x):
        support = 0
        for a,atom in enumerate(atom_masks):
            if x & atom: support |= 1 << a
        up = all_old
        for a in range(17):
            if support >> a & 1: up &= old_contains_atom[a]
        return up
    all_sorted = old_sorted + new_sorted
    event_index = {e:i for i,e in enumerate(all_sorted)}
    principal_up = []
    for e in all_sorted:
        up = old_uppers_for_physical(e)
        for j,w in enumerate(new_sorted):
            if not e & ~w: up |= 1 << (len(old_sorted)+j)
        principal_up.append(up)
    upset_to_event = {u:all_sorted[i] for i,u in enumerate(principal_up)}
    assert len(upset_to_event) == len(all_sorted)
    old_sublattice_preserved = True
    for w in new_sorted:
        greatest = 0
        for e in old_sorted:
            if not e & ~w: greatest |= e
        if greatest not in old_set:
            old_sublattice_preserved = False; break
    failure=None;tested=0
    if old_sublattice_preserved:
        for x in new_sorted:
            for y in all_sorted:
                tested += 1
                common = principal_up[event_index[x]] & principal_up[event_index[y]]
                if common not in upset_to_event:
                    failure={"new_event":hex(x),"other_event":hex(y),
                             "common_upper_set_sha256":hashlib.sha256(
                                 common.to_bytes((len(all_sorted)+7)//8,
                                                 "little")).hexdigest()}
                    break
            if failure: break
    lattice = old_sublattice_preserved and failure is None
    formal_generators={realize(split_mod.lift(e,15)) for e in atlas_mod.raw16()}
    formal_generators.update(realize(split_mod.lift(int(x,16),15))
                             for x in node["path_choices_hex"])
    formal_generators.add(defect_join)
    generators=formal_generators|cell00_events|cell10_events
    centre=[] if not lattice else [x for x in closed if all(
        split_mod.concrete_compatibility(x,g,closed_set) for g in generators)]
    out = {
        "schema": SCHEMA, "schema_version": "1.0", "quotient_points": len(points),
        "cell00_projected_local_states": len(projected00),
        "cell10_projected_local_states": len(projected10),
        "cell00_events": len(cell00_events), "cell10_events": len(cell10_events),
        "both_cell_event_orders_reflected": order00 and order10,
        "formal_terminal_events": len(terminal_events), "seed_events": len(seed),
        "closed_events": len(closed), "closure_completed_under_100000_events": completed,
        "selected_split_points": split_piece.bit_count(),
        "selected_split_is_nonempty_proper": bool(split_piece) and split_piece != p15,
        "selected_split_has_off_both_activations": bool(
            split_piece & ~activation0 and split_piece & ~activation1),
        "selected_split_source_state_event_sha256": sorted(
            hashlib.sha256(e.to_bytes((len(states)+7)//8,"little")).hexdigest()
            for e in split_sources),
        "residue_extracted": residue in closed_set, "hull_repaired": hull in closed_set,
        "defect_join_remains_witness_join": actual_join == defect_join,
        "q_boundary_reconstructed": reconstructed(q0,q1),
        "r_boundary_reconstructed": reconstructed(r0,r1),
        "row0_activation_cylinder_is_event": activation0 in closed_set,
        "row1_activation_cylinder_is_event": activation1 in closed_set,
        "nonzero_row0_activation_supported_events": len(act0),
        "nonzero_row1_activation_supported_events": len(act1),
        "point_evaluations_order_separate_by_concreteness": True,
        "new_events_beyond_formal_terminal":len(new_events),
        "old_terminal_sublattice_preserved":old_sublattice_preserved,
        "new_event_pairs_tested":tested,
        "first_exact_new_event_cut_failure":failure,
        "lattice":lattice,
        "lattice_audit_uses_17_atom_support":True,
        "centre_events":None if not lattice else len(centre),
        "centre_is_trivial":lattice and set(centre)=={0,full},
        "centre_sha256":None if not lattice else hashlib.sha256(
            ",".join(map(hex,sorted(centre))).encode()).hexdigest(),
        "scope": ("Exact transverse cells 00/10 quotient for node 6 and one "
                  "cell00-definable split. Closure exact if cap passes. No "
                  "alternative split or remaining cells; lattice and centre "
                  "audits are exact. No "
                  "maximal blocks, full grid, or sigma claim."),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_terminal_split_transverse_quotient.py --verify")}
    out["producer_sha256"] = hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true")
    ap.add_argument("--verify",action="store_true");args=ap.parse_args();out=payload()
    path=os.path.join(HERE,"full_grid_terminal_split_transverse_quotient.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__":main()
