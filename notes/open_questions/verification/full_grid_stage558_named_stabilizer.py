#!/usr/bin/env python3
"""Named semantic stabilizer of the stage-558 fattened-meet interval.

This deliberately does not claim the full concrete automorphism group of the
6,186,568-point set system.  It enumerates the exact 32-element group generated
by row/column swaps, the simultaneous q/r complement induced by the cell
atom permutation e00<->e11, and independent a1/a2 arm swaps in the two rows.
It then stabilizes the selected repair provenance, the fattened meet e_*, its
literal cylinder, and the 160 whole activation/local-state macrofibres.
"""
import argparse, hashlib, itertools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA = "full-grid-stage558-named-stabilizer-v1"

ARM = {"a1":"a2", "a2":"a1", "u1":"v1", "v1":"u1",
       "p11":"p12", "p12":"p11"}
COMP = {"e00":"e11", "e11":"e00"}

def atom_perm(swaps):
    atoms = sorted({a for b in cell.CELL_BLOCKS for a in b})
    return {a: swaps.get(a, a) for a in atoms}

def block_certificate(p):
    blocks = {frozenset(b) for b in cell.CELL_BLOCKS}
    return all(frozenset(p[a] for a in b) in blocks for b in cell.CELL_BLOCKS)

def transform_desc(d, g):
    """Action on (a0,a1,q0,q1,r0,r1,ns), old slots -> new slots."""
    rs, cs, cp, arms = g
    olda = [tuple(d[0]), tuple(d[1])]
    oldq = [d[2], d[3]]; oldr = [d[4], d[5]]; oldns = list(d[6])
    newa = [None, None]; newq = [None, None]; newr = [None, None]
    newns = [None] * 4
    for i in (0, 1):
        ii = i ^ rs
        a = olda[i]
        if arms[i]: a = (a[1], a[0], a[2])
        newa[ii] = a; newq[ii] = oldq[i] ^ cp
    for j in (0, 1): newr[j ^ cs] = oldr[j] ^ cp
    for i in (0, 1):
        for j in (0, 1): newns[2*(i^rs)+(j^cs)] = oldns[2*i+j]
    return (newa[0], newa[1], newq[0], newq[1], newr[0], newr[1], tuple(newns))

def name(g):
    rs, cs, cp, arms = g
    return f"R{rs}C{cs}K{cp}A{arms[0]}{arms[1]}"

def payload():
    states, n, full, masks, raw, labels, interfaces, macro = grid.build()
    descs = [(a0,a1,q0,q1,r0,r1,tuple(ns))
             for a0,a1,q0,q1,r0,r1,ns,size in macro]
    descset = set(descs)
    assert len(descs) == len(descset)
    groups = list(itertools.product((0,1),(0,1),(0,1),
                                    itertools.product((0,1),repeat=2)))
    assert len(groups) == 32
    assert all({transform_desc(d,g) for d in descs} == descset for g in groups)
    root_perms = {tuple(descs.index(transform_desc(d,g)) for d in descs)
                  for g in groups}
    assert len(root_perms) == 32

    # Provenance supports of the three selected repairs.  The third selector is
    # partial; its ambient macrofibre and its invariant n1/s1 literal are marked.
    primary = {d for d in descs if d[0] == d[1] == (1,1,0)
               and d[2:6] in ((0,1,1,0),(1,0,0,1))}
    secondary = {d for d in descs if d[0] == (1,1,1) and d[1] == (1,1,0)
                 and d[2:6] == (0,1,0,0)}
    tertiary = {d for d in descs if d[0] == (1,1,0) and d[1] == (1,1,1)
                and d[2:6] == (0,1,1,1) and d[6] == (2,2,1,1)}
    assert len(primary)==2 and len(secondary)==1 and len(tertiary)==1

    # e_* is the whole 0101 profile fibre plus the unique secondary selector.
    # Hence its cylinder gap consists exactly of the remaining whole q=01
    # macrofibres.  This reconstructs the 160 descriptors without rebuilding
    # the 558-event bitsets.
    gap_desc = {d for d in descs if d[2:4] == (0,1)
                and d[2:6] != (0,1,0,1) and d not in secondary}
    assert len(gap_desc)==160 and gap_desc <= descset
    cylinder_desc = {d for d in descs if d[2:4] == (0,1)}
    fibre0101 = {d for d in descs if d[2:6] == (0,1,0,1)}
    estar_extra = secondary

    def stabilizes(g, subset): return {transform_desc(d,g) for d in subset} == subset
    stages = {}
    filters = [
        ("named_root", lambda g: True),
        ("repair_provenance", lambda g: stabilizes(g,primary) and
             stabilizes(g,secondary) and stabilizes(g,tertiary)),
        ("literal_cylinder", lambda g: stabilizes(g,cylinder_desc)),
        ("fattened_meet_components", lambda g: stabilizes(g,fibre0101) and
             stabilizes(g,estar_extra)),
        ("enlargement_macrofibres", lambda g: stabilizes(g,gap_desc)),
    ]
    live = groups
    for label,pred in filters:
        live = [g for g in live if pred(g)]
        stages[label] = [name(g) for g in live]

    # Action on the 160 pieces.  Descriptors are unique, so this is an exact
    # permutation representation of the named subgroup.
    ordered = sorted(gap_desc)
    index = {d:i for i,d in enumerate(ordered)}
    perms = [tuple(index[transform_desc(d,g)] for d in ordered) for g in live]
    unseen=set(range(160)); orbits=[]
    while unseen:
        i=min(unseen); orb={p[i] for p in perms}; unseen-=orb; orbits.append(sorted(orb))

    arm = atom_perm(ARM); comp = atom_perm(COMP)
    third_receipt=json.load(open(os.path.join(HERE,"full_grid_third_gap_classification.json")))
    chosen=third_receipt["minimum_subrectangle"]["selected_local_state_atoms"]
    third_arm_invariant=all(
        {frozenset(arm[a] for a in s) for s in factor_states}==
        {frozenset(s) for s in factor_states}
        for factor_states in chosen)
    out = {
      "schema":SCHEMA,"schema_version":"1.0","carrier_points":n,
      "named_root_group_order":len(groups),
      "named_root_descriptor_action_is_faithful":len(root_perms)==len(groups),
      "named_generators":{
        "row_swap":"swap cell rows and q0,q1/activation rows",
        "column_swap":"swap cell columns and r0,r1",
        "global_qr_complement":COMP,
        "row_arm_swaps":ARM},
      "cell_atom_permutation_certificates":{
        "arm_maps_declared_blocks_to_declared_blocks":block_certificate(arm),
        "complement_maps_declared_blocks_to_declared_blocks":block_certificate(comp),
        "arm_maps_224_state_set_bijectively":{
          frozenset(arm[a] for a in s) for s in states}==set(states),
        "complement_maps_224_state_set_bijectively":{
          frozenset(comp[a] for a in s) for s in states}==set(states),
        "third_partial_selector_factor_sets_arm_invariant":third_arm_invariant},
      "stabilizer_filtration":{k:{"order":len(v),"elements":v} for k,v in stages.items()},
      "final_named_stabilizer_order":len(live),
      "final_named_stabilizer_generators":["independent a1/a2 arm swap in row 0",
                                            "independent a1/a2 arm swap in row 1"],
      "macrofibre_action":{
        "pieces":160,"distinct_permutations":len(set(perms)),
        "orbits":len(orbits),"orbit_size_histogram":{
          str(s):sum(len(o)==s for o in orbits) for s in sorted({len(o) for o in orbits})},
        "all_pieces_fixed_setwise":all(len(o)==1 for o in orbits),
        "permutation_sha256":hashlib.sha256(json.dumps(perms,separators=(",",":")).encode()).hexdigest()},
      "named_equals_full_gate_preserving_stabilizer":"open",
      "missing_faithfulness_theorem":"every gate/provenance-preserving concrete automorphism of the 558-event set system induces one of the 32 named semantic descriptor transformations",
      "scope":"exact action of the stated named 32-element semantic group on macro descriptors and its exact stabilizer; not the full 6M-point concrete automorphism group",
      "dependency_payload_sha256":json.load(open(os.path.join(
          HERE,"full_grid_stage558_fattened_meet_gap.json")))["payload_sha256"],
      "command":"python3 notes/open_questions/verification/full_grid_stage558_named_stabilizer.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_stage558_named_stabilizer.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):
        assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
      "named_root":out["named_root_group_order"],"final_stabilizer":out["final_named_stabilizer_order"],
      "macrofibre_orbits":out["macrofibre_action"]["orbits"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
