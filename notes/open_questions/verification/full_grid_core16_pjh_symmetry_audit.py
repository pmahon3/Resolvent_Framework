#!/usr/bin/env python3
"""Post-hoc symmetry audit of the complete first-PJH-defect atlas.

The raw 48-node/64-edge atlas is never pruned.  This verifier asks which
elements of the full 128-element unlabelled K22 coordinate group preserve
(a) its node families, (b) selector-free defect edges, and (c) joint edges
including the serialized witness pair.  These groups are computed, not
assumed.
"""
import argparse, collections, hashlib, itertools, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_core16_pjh_defect_atlas as atlas

SCHEMA="full-grid-core16-pjh-symmetry-audit-v1"

POINTS=list(itertools.product((0,1),repeat=4));PI={p:i for i,p in enumerate(POINTS)}
COORD_PERMS=[p for p in itertools.permutations(range(4))
             if set(p[:2]) in ({0,1},{2,3})]
GROUP=[]
for perm in COORD_PERMS:
    for flip in itertools.product((0,1),repeat=4):
        GROUP.append(tuple(PI[tuple(x[perm[j]]^flip[j] for j in range(4))]
                           for x in POINTS))
GROUP=sorted(set(GROUP));assert len(GROUP)==128

def mm(z,p):
    return sum(1<<p[i] for i in range(16) if z>>i&1)
def mf(f,p):return tuple(sorted(mm(z,p) for z in f))
def cycles_on(items,action):
    unseen=set(items);out=[]
    while unseen:
        seed=min(unseen);orb={action(seed,p) for p in action.group}
        assert orb<=set(items);unseen-=orb;out.append(sorted(orb))
    return out

def payload():
    source=json.load(open(os.path.join(HERE,"full_grid_2x2_rectangle_core16_exhaustive.json")))["payload"]
    tree=source["tree"]
    by_path={tuple(n["path_choices_hex"]):n for n in tree}
    fams={():atlas.close16(atlas.raw16())}
    for n in sorted(tree,key=lambda x:(x["depth"],x["id"])):
        path=tuple(n["path_choices_hex"])
        if path:
            z=int(path[-1],16);fams[path]=atlas.close16(fams[path[:-1]]|{z,atlas.FULL^z})
        assert len(fams[path])==n["events"]
    node_family={n["id"]:tuple(sorted(fams[tuple(n["path_choices_hex"])])) for n in tree}
    family_id={f:i for i,f in node_family.items()};assert len(family_id)==48

    receipt=json.load(open(os.path.join(HERE,"full_grid_core16_pjh_defect_atlas.json")))
    raw=[]
    for r in receipt["records"]:
        f=node_family[r["node_id"]];a,b=map(lambda x:int(x,16),r["witness_pair_hex"])
        lo=int(r["failed_lower_hex"],16);hi=int(r["failed_upper_hex"],16)
        for e in r["edges"]:
            h=int(e["candidate_hull_hex"],16)
            raw.append((f,a,b,lo,hi,h,e["target_outcome"]))
    assert len(raw)==64 and len(set(raw))==64
    rawset=set(raw)
    bare={(x[0],x[3],x[4],x[5],x[6]) for x in raw};assert len(bare)==64
    defects=[x for x in raw if x[5]!=x[3]];assert len(defects)==33
    defectset=set(defects)
    entered=collections.Counter(tuple(i for i in range(16) if (h&~lo)>>i&1)
                                for _,_,_,lo,_,h,_ in defects)
    assert set(k for k in entered if len(k)==1)=={(i,) for i in range(16)}
    assert entered[(3,12)]==1 and sum(entered.values())==33

    node_group=[p for p in GROUP if {mf(f,p) for f in family_id}==set(family_id)]
    bare_group=[];joint_group=[]
    for p in GROUP:
        image={(mf(f,p),mm(lo,p),mm(hi,p),mm(h,p),out) for f,lo,hi,h,out in bare}
        if image==bare:bare_group.append(p)
        image2={(mf(f,p),*sorted((mm(a,p),mm(b,p))),mm(lo,p),mm(hi,p),mm(h,p),out)
                for f,a,b,lo,hi,h,out in raw}
        if image2==rawset:joint_group.append(p)
    assert set(joint_group)<=set(bare_group)<=set(node_group)<=set(GROUP)
    defect_group=[]
    for p in GROUP:
        image={(mf(f,p),*sorted((mm(a,p),mm(b,p))),mm(lo,p),mm(hi,p),mm(h,p),out)
               for f,a,b,lo,hi,h,out in defects}
        if image==defectset:defect_group.append(p)

    def orbit_data(items,grp,mapper):
        unseen=set(items);orbs=[]
        while unseen:
            x=min(unseen);orb={mapper(x,p) for p in grp};assert orb<=set(items)
            unseen-=orb;orbs.append(orb)
        fixed=[sum(mapper(x,p)==x for x in items) for p in grp]
        assert sum(fixed)%len(grp)==0 and sum(fixed)//len(grp)==len(orbs)
        return {"orbits":len(orbs),"orbit_size_histogram":{
            str(k):sum(len(o)==k for o in orbs) for k in sorted({len(o) for o in orbs})},
            "burnside_fixed_count_histogram":{
            str(k):fixed.count(k) for k in sorted(set(fixed))}}
    bare_map=lambda x,p:(mf(x[0],p),mm(x[1],p),mm(x[2],p),mm(x[3],p),x[4])
    joint_map=lambda x,p:(mf(x[0],p),*sorted((mm(x[1],p),mm(x[2],p))),
                           mm(x[3],p),mm(x[4],p),mm(x[5],p),x[6])
    bare_stats=orbit_data(bare,bare_group,bare_map)
    joint_stats=orbit_data(raw,joint_group,joint_map)
    defect_stats=orbit_data(defects,defect_group,joint_map)

    def gdigest(g):return hashlib.sha256(json.dumps(g,separators=(",",":")).encode()).hexdigest()
    out={"schema":SCHEMA,"schema_version":"1.0","raw_nodes":48,"raw_edges":64,
      "ambient_coordinate_group_order":len(GROUP),
      "node_family_set_stabilizer_order":len(node_group),
      "selector_free_edge_set_stabilizer_order":len(bare_group),
      "joint_witness_edge_set_stabilizer_order":len(joint_group),
      "possible_first_defect_edges":len(defects),
      "possible_first_defect_set_stabilizer_order":len(defect_group),
      "entered_profile_pattern_histogram":[{"profile_bits":list(k),"edges":v}
        for k,v in sorted(entered.items(),key=lambda x:(len(x[0]),x[0]))],
      "every_single_profile_bit_occurs_as_an_entered_fibre":True,
      "node_group_sha256":gdigest(node_group),"bare_group_sha256":gdigest(bare_group),
      "joint_group_sha256":gdigest(joint_group),
      "defect_group_sha256":gdigest(defect_group),
      "selector_free_edge_orbits":bare_stats,"joint_witness_edge_orbits":joint_stats,
      "possible_first_defect_orbits":defect_stats,
      "quotient_is_post_hoc":True,"raw_atlas_never_pruned":True,
      "path_provenance_transport":"not claimed; lexicographic selector equivariance is not assumed",
      "stage558_provenance_projection":"not applied; stage-decorated quotient requires a separately certified action",
      "scope":"exact post-hoc action on the completed core16 node/edge atlas; no full-grid terminal realization claim",
      "dependency_payload_sha256":receipt["payload_sha256"],
      "command":"python3 notes/open_questions/verification/full_grid_core16_pjh_symmetry_audit.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_core16_pjh_symmetry_audit.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
      "node_group":out["node_family_set_stabilizer_order"],
      "bare_edge_group":out["selector_free_edge_set_stabilizer_order"],
      "joint_edge_group":out["joint_witness_edge_set_stabilizer_order"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
