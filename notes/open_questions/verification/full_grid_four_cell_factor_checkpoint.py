#!/usr/bin/env python3
"""Exact symbolic checkpoint for the node-6 full four-cell carrier.

This does not claim closure or latticehood.  It proves the finite carrier and
the factorization needed to run that audit without materializing millions of
point bits per event.  A macro fibre is indexed by (a0,a1,q0,q1,r0,r1) and is
the Cartesian product G(a0,q0,r0) x G(a0,q0,r1) x
G(a1,q1,r0) x G(a1,q1,r1).  Cell events are coordinate cylinders in it.
"""
import collections, hashlib, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_terminal_split_one_cell_quotient as one

SCHEMA="full-grid-four-cell-factor-checkpoint-v1"

def payload():
    states=cell.cell_states(); local=one.local_event_predicates(states)
    groups=collections.defaultdict(list); datum=[]
    for j,s in enumerate(states):
        a=tuple(int(x in s) for x in cell.SHARED)
        q=int("e11" in s or "e10" in s);r=int("e11" in s or "e01" in s)
        groups[a,q,r].append(j);datum.append((a,q,r))
    macros=[]
    for a0 in sorted({x[0] for x in groups}):
      for a1 in sorted({x[0] for x in groups}):
       for q0 in (0,1):
        for q1 in (0,1):
         for r0 in (0,1):
          for r1 in (0,1):
           gs=(groups[a0,q0,r0],groups[a0,q0,r1],groups[a1,q1,r0],groups[a1,q1,r1])
           if all(gs):macros.append(((a0,a1,q0,q1,r0,r1),tuple(map(len,gs)),gs))
    total=sum(__import__('math').prod(sz) for _,sz,_ in macros)
    # Locate the exact cell00 predicate used by the previous audit.
    wanted="ae31a846410eff44a1133601bbc9bdab774ffea3e4aa10a4a5e8009752b7799c"
    sources=[e for e in local if hashlib.sha256(e.to_bytes((len(states)+7)//8,"little")).hexdigest()==wanted]
    assert len(sources)==1; source=sources[0]
    split=0; split_act0=0;split_act1=0;profile_counts=[0]*16
    projections=[set() for _ in range(4)]
    for key,sz,gs in macros:
        a0,a1,q0,q1,r0,r1=key; weight=__import__('math').prod(sz)
        profile_counts[(q0<<3)|(q1<<2)|(r0<<1)|r1]+=weight
        for i,g in enumerate(gs):projections[i].update(g)
        chosen=sum(1 for s in gs[0] if source>>s&1)
        sw=chosen*sz[1]*sz[2]*sz[3]
        split+=sw
        if a0==(1,1,1):split_act0+=sw
        if a1==(1,1,1):split_act1+=sw
    # Each local order is reflected because every one of its 224 states occurs.
    faithful=[]
    for proj in projections:
        faithful.append(len(proj)==len(states) and all(
          ((e&~f)==0)==(((e&sum(1<<s for s in proj))&~(f&sum(1<<s for s in proj)))==0)
          for e in local for f in local))
    out={
      "schema":SCHEMA,"schema_version":"1.0","local_states":len(states),
      "local_events":len(local),"nonempty_macro_fibres":len(macros),
      "full_compatible_four_cell_carrier_points":total,
      "physical_bytes_per_event_mask":(total+7)//8,
      "macro_fibre_size_min":min(__import__('math').prod(x[1]) for x in macros),
      "macro_fibre_size_max":max(__import__('math').prod(x[1]) for x in macros),
      "profile_point_counts":profile_counts,
      "projected_states_by_cell":list(map(len,projections)),
      "all_four_cell_embeddings_order_faithful":all(faithful),
      "selected_split_source_state_event_sha256":wanted,
      "selected_split_lift_points":split,
      "selected_split_points_in_row0_activation":split_act0,
      "selected_split_points_in_row1_activation":split_act1,
      "selected_split_has_off_row0_activation":split>split_act0,
      "selected_split_has_off_row1_activation":split>split_act1,
      "exact_symbolic_factorization":"For each macro (a0,a1,q0,q1,r0,r1), carrier = G(a0,q0,r0) x G(a0,q0,r1) x G(a1,q1,r0) x G(a1,q1,r1); cells 00,01,10,11 are cylinders on factors 0,1,2,3.",
      "smallest_next_engine":"Intern reduced multi-valued decision diagrams independently on each macro fibre; represent a global event by its tuple of macro roots. Complement, disjointness, union and order are componentwise apply operations. Retain the 17-atom outer normal form for the 18432 formal terminal events.",
      "status":"checkpoint; closure, lattice/OML, centre, boundary, activation, PJH, q-meet and Phi-tameness gates remain open",
      "command":"python3 notes/open_questions/verification/full_grid_four_cell_factor_checkpoint.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_four_cell_factor_checkpoint.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    else:assert json.load(open(path))==out
    print(json.dumps(out,sort_keys=True,indent=2))
