#!/usr/bin/env python3
"""Exact node-6 PJH split quotient with corner cells 00,01,10.

The compatible carrier is the full triple fibre product, restricted only by
existence of a completing state for missing cell 11.  To avoid materializing
18k 553648-bit formal events, events use the exact normal form (partial,full):
`full` is a 17-bit union of whole formal atoms and `partial` contains proper
subsets of the remaining atoms.  Only genuinely split events carry big ints.
"""
import argparse, collections, hashlib, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_core16_pjh_defect_atlas as atlas_mod
import full_grid_binary_pjh_split_core_audit as split_mod
import full_grid_terminal_split_one_cell_quotient as one

SCHEMA="full-grid-terminal-split-three-cell-corner-quotient-v1"; NODE_ID=6

def payload(cap=100000):
    states=cell.cell_states(); local=one.local_event_predicates(states)
    groups=collections.defaultdict(list);data=[]
    for j,s in enumerate(states):
        a=tuple(int(x in s) for x in cell.SHARED)
        q=int("e11" in s or "e10" in s);r=int("e11" in s or "e01" in s)
        groups[a,q,r].append(j);data.append((a,q,r))
    points=[];completion_counts=[]
    for s00,(a0,q0,r0) in enumerate(data):
      for s01,(aa,qq,r1) in enumerate(data):
        if (aa,qq)!=(a0,q0):continue
        for s10,(a1,q1,rr) in enumerate(data):
          if rr==r0 and groups[a1,q1,r1]:
            points.append((s00,s01,s10,a0,a1,q0,q1,r0,r1))
            completion_counts.append(len(groups[a1,q1,r1]))
    n=len(points);full_phys=(1<<n)-1
    profile=[0]*16
    for j,p in enumerate(points):profile[(p[5]<<3)|(p[6]<<2)|(p[7]<<1)|p[8]]|=1<<j
    assert all(profile)
    state_masks=[[0]*len(states) for _ in range(3)]
    for j,p in enumerate(points):
        bit=1<<j
        for pos in range(3):state_masks[pos][p[pos]]|=bit
    maps=[]
    for pos in range(3):
        mp={}
        for e in local:
            image=0;bits=e
            while bits:
                b=bits&-bits;image|=state_masks[pos][b.bit_length()-1];bits^=b
            mp[e]=image
        maps.append(mp)
    cell_events=[set(x.values()) for x in maps]
    projected=[{p[i] for p in points} for i in range(3)]
    faithful=[]
    for mp in maps:
        faithful.append(all(((e&~f)==0)==((mp[e]&~mp[f])==0)
                            for e in local for f in local))

    source=json.load(open(os.path.join(HERE,atlas_mod.SOURCE)))
    node=next(x for x in source["payload"]["tree"] if x["id"]==NODE_ID)
    atlas=json.load(open(os.path.join(HERE,"full_grid_core16_pjh_defect_atlas.json")))
    rec=next(x for x in atlas["records"] if x["node_id"]==NODE_ID)
    low=int(rec["failed_lower_hex"],16);high=int(rec["failed_upper_hex"],16)
    assert high&~low==1<<15
    fam16=atlas_mod.close16(atlas_mod.raw16())
    for choice in node["path_choices_hex"]:
        z=int(choice,16);fam16=atlas_mod.close16(fam16|{z,atlas_mod.FULL^z})
    p15=profile[15]
    act0=sum(1<<j for j,p in enumerate(points) if p[3]==(1,1,1))
    act1=sum(1<<j for j,p in enumerate(points) if p[4]==(1,1,1))
    traces=sorted({e&p15 for e in cell_events[0] if e&p15 and e&p15!=p15},
                  key=lambda x:(x.bit_count(),x))
    piece=next(s for s in traces if s&~act0 and s&~act1)
    formal_join=split_mod.lift(low,15)|(1<<15);FULL17=(1<<17)-1
    terminal17=split_mod.close_logic(
        {split_mod.lift(e,15) for e in fam16}|{formal_join,FULL17^formal_join},FULL17)
    atoms=profile[:15]+[piece,p15&~piece]
    atom_union=0
    for atom in atoms:atom_union|=atom
    assert all(atoms) and atom_union==full_phys
    assert all(not atoms[i]&atoms[j] for i in range(17) for j in range(i))
    au_cache={0:0}
    def au(bits):
        if bits not in au_cache:
            v=0
            for a in range(17):
                if bits>>a&1:v|=atoms[a]
            au_cache[bits]=v
        return au_cache[bits]
    touch_cache={0:0}
    def touch(p):
        if p not in touch_cache:
            touch_cache[p]=sum(1<<a for a,x in enumerate(atoms) if p&x)
        return touch_cache[p]
    def canon_phys(e):
        f=0;p=e
        for a,x in enumerate(atoms):
            if e&x==x:f|=1<<a;p&=~x
        return (p,f)
    def comp(x):
        p,f=x;t=touch(p)
        return (au(t)&~p, FULL17^(f|t))
    def disjoint(x,y):
        p,f=x;q,g=y
        return not(f&g or touch(p)&g or touch(q)&f or p&q)
    def union(x,y):
        p,f=x;q,g=y;p|=q;f|=g
        p&=~au(f)
        for a in range(17):
            if p&atoms[a]==atoms[a]:f|=1<<a;p&=~atoms[a]
        p&=~au(f)
        return (p,f)
    def inter(x,y):
        p,f=x;q,g=y
        if not p and not q:return (0,f&g)
        return union(canon_phys(p&q), union(canon_phys(p&au(g)),
                     union(canon_phys(q&au(f)),(0,f&g))))
    def le(x,y):
        p,f=x;q,g=y
        return not(f&~g) and not((p&~au(g))&~q)
    def canonical(x):
        p,f=x
        return (p&au(f))==0 and all((p&atoms[a])!=atoms[a] for a in range(17))

    old=set((0,e) for e in terminal17); events=set(old); extras=[];cursor=0
    def add(x):
        if x not in events:events.add(x);extras.append(x);return True
        return False
    for ce in cell_events:
        for e in ce:add(canon_phys(e))
    completed=True
    old_codes=sorted(terminal17)
    while cursor<len(extras):
        x=extras[cursor];add(comp(x))
        if len(events)>cap:completed=False;break
        for e in old_codes:
            y=(0,e)
            if disjoint(x,y):add(union(x,y))
            if len(events)>cap:completed=False;break
        if not completed:break
        for y in extras[:cursor]:
            if disjoint(x,y):add(union(x,y))
            if len(events)>cap:completed=False;break
        if not completed:break
        cursor+=1

    hull=(0,split_mod.lift(high,15)); defect=(0,formal_join)
    residue=inter(hull,comp(defect))
    witnesses=[(0,split_mod.lift(int(w,16),15)) for w in rec["witness_pair_hex"]]
    assert all(le(w,defect) for w in witnesses)
    defect_is_join=defect in events and all(not(le(witnesses[0],u) and
        le(witnesses[1],u)) or le(defect,u) for u in events)
    q0=canon_phys(sum(1<<j for j,p in enumerate(points) if p[5]));q1=canon_phys(
        sum(1<<j for j,p in enumerate(points) if p[6]));r0=canon_phys(
        sum(1<<j for j,p in enumerate(points) if p[7]));r1=canon_phys(
        sum(1<<j for j,p in enumerate(points) if p[8]))
    def reconstructed(x,y):
        return all(w in events for w in (inter(x,y),inter(x,comp(y)),
            inter(comp(x),y),inter(comp(x),comp(y))))
    activations=[canon_phys(act0),canon_phys(act1)]
    act_supported=[sum(1 for e in events if e!=(0,0) and le(e,a)) for a in activations]

    # Old terminal is a known lattice.  Principal-upset audit only needs pairs
    # involving extras if every extra has a greatest old lower bound.
    old_sorted=sorted(old_codes); all_events=[(0,e) for e in old_sorted]+sorted(
        set(extras)-old)
    new_events=all_events[len(old_sorted):]; old_preserved=True
    for x in new_events:
        lowers=[e for e in old_sorted if le((0,e),x)]
        greatest=0
        for e in lowers:greatest|=e
        if greatest not in terminal17:old_preserved=False;break
    old_contains=[0]*17
    for j,e in enumerate(old_sorted):
        for a in range(17):
            if e>>a&1:old_contains[a]|=1<<j
    all_old=(1<<len(old_sorted))-1
    principal=[]
    for x in all_events:
        support=x[1]|touch(x[0]);u=all_old
        for a in range(17):
            if support>>a&1:u&=old_contains[a]
        for j,y in enumerate(new_events):
            if le(x,y):u|=1<<(len(old_sorted)+j)
        principal.append(u)
    upset_to_event={u:all_events[i] for i,u in enumerate(principal)}
    assert len(upset_to_event)==len(all_events)
    failure=None;tested=0
    if completed and old_preserved:
        for x in new_events:
            ix=all_events.index(x)
            for iy,y in enumerate(all_events):
                tested+=1;c=principal[ix]&principal[iy]
                if c not in upset_to_event:
                    failure={"new_event_index":ix,"other_event_index":iy,
                        "common_upper_sha256":hashlib.sha256(c.to_bytes(
                        (len(all_events)+7)//8,"little")).hexdigest()};break
            if failure:break
    lattice=completed and old_preserved and failure is None

    # Generator-commutant centre; exact once latticehood holds.
    generator_codes={split_mod.lift(e,15) for e in atlas_mod.raw16()}
    generator_codes|={split_mod.lift(int(x,16),15) for x in node["path_choices_hex"]}
    generators={(0,e) for e in generator_codes}|{defect}
    for ce in cell_events:generators|={canon_phys(e) for e in ce}
    def compatible(x,y):
        return inter(x,y) in events and inter(x,comp(y)) in events and inter(y,comp(x)) in events
    ordered_generators=sorted(generators,key=lambda x:(bool(x[0]),x[1],x[0]))
    centre=[] if not lattice else [x for x in all_events if all(
        compatible(x,g) for g in ordered_generators)]

    qlit=inter(comp(q0),q1); lowers=[e for e in events if le(e,qlit)]
    qmeet=(0,0)
    for e in lowers:qmeet=union(qmeet,e)
    qmeet_event=qmeet in events
    qresidue=inter(qlit,comp(qmeet))
    def physical(x):return x[0]|au(x[1])
    assert all(canonical(e) for e in events)
    old_qmeet=(0,0)
    for e in old:
        if le(e,qlit):old_qmeet=union(old_qmeet,e)
    qincrement=inter(qmeet,comp(old_qmeet))
    def whole_words(x):
        e=physical(x);return [format(i,"04b") for i,p in enumerate(profile) if not p&~e]
    def partial_words(x):
        e=physical(x);return [format(i,"04b") for i,p in enumerate(profile) if e&p and p&~e]
    split_sources=[e for e,image in maps[0].items() if image&p15==piece]
    out={"schema":SCHEMA,"schema_version":"1.0","quotient_points":n,
      "compatible_triples_are_completable_by_cell11":True,
      "minimum_number_of_cell11_completions_per_triple":min(completion_counts),
      "local_cell_states":len(states),"projected_states_by_cell":[len(x) for x in projected],
      "cell_events_by_cell":[len(x) for x in cell_events],
      "all_three_cell_embeddings_order_faithful":all(faithful),
      "formal_terminal_events":len(terminal17),"extra_normal_forms":len(set(extras)-old),
      "closed_events":len(events),"closure_cap":cap,"closure_completed":completed,
      "selected_split_points":piece.bit_count(),"selected_split_off_both_activations":bool(piece&~act0 and piece&~act1),
      "selected_split_sha256":hashlib.sha256(piece.to_bytes((n+7)//8,"little")).hexdigest(),
      "selected_split_source_state_event_sha256":sorted(hashlib.sha256(e.to_bytes(
          (len(states)+7)//8,"little")).hexdigest() for e in split_sources),
      "residue_extracted":residue in events,"hull_repaired":hull in events,
      "defect_join_remains_witness_join":defect_is_join,
      "q_boundary_reconstructed":reconstructed(q0,q1),"r_boundary_reconstructed":reconstructed(r0,r1),
      "activation_cylinders_are_events":[a in events for a in activations],
      "nonzero_activation_supported_events":act_supported,
      "q0_complement_meet_q1_exists":qmeet_event,
      "q0_complement_meet_q1_is_proper":qmeet_event and qmeet!=qlit,
      "q0_complement_meet_q1_points":physical(qmeet).bit_count(),
      "q0_complement_q1_literal_intersection_points":physical(qlit).bit_count(),
      "q_meet_residue_points":physical(qresidue).bit_count(),
      "q_meet_residue_is_event":qresidue in events,
      "q_meet_whole_profile_words":whole_words(qmeet),
      "q_meet_partial_profile_words":partial_words(qmeet),
      "old_profile_core_q_meet_points":physical(old_qmeet).bit_count(),
      "old_profile_core_q_meet_whole_profile_words":whole_words(old_qmeet),
      "q_meet_increment_points":physical(qincrement).bit_count(),
      "q_meet_increment_whole_profile_words":whole_words(qincrement),
      "q_meet_increment_partial_profile_words":partial_words(qincrement),
      "q_meet_increment_is_row0_activation_supported":physical(qincrement)!=0 and le(qincrement,activations[0]),
      "q_meet_residue_whole_profile_words":whole_words(qresidue),
      "q_meet_residue_partial_profile_words":partial_words(qresidue),
      "old_terminal_sublattice_preserved":old_preserved,"new_event_pairs_tested":tested,
      "first_exact_cut_failure":failure,"lattice":lattice,
      "centre_events":None if not lattice else len(centre),
      "centre_is_trivial":lattice and set(centre)=={(0,0),(0,FULL17)},
      "point_evaluations_order_separate_by_concreteness":True,
      "normal_form_representation_exact":True,
      "scope":"Exact completable triple quotient for node6 and cells 00,01,10 with one cell00-definable split. No cell11, alternative split, maximal-block, or arbitrary-base claim.",
      "command":"python3 notes/open_questions/verification/full_grid_terminal_split_three_cell_corner_quotient.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");ap.add_argument("--cap",type=int,default=100000);a=ap.parse_args()
    out=payload(a.cap);path=os.path.join(HERE,"full_grid_terminal_split_three_cell_corner_quotient.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__":main()
