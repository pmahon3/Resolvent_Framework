#!/usr/bin/env python3
"""Exact automorphisms of the 224-state/56-event conditional H4 cell code."""
import argparse, hashlib, itertools, json, os, sys
import networkx as nx

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell

SCHEMA="h4-cell-incidence-automorphism-v1"

def construction():
    states=cell.cell_states(); atoms=sorted({a for b in cell.CELL_BLOCKS for a in b})
    named={a:frozenset(i for i,s in enumerate(states) if a in s) for a in atoms}
    events={frozenset(),frozenset(range(len(states)))}
    for b in cell.CELL_BLOCKS:
        for bits in range(1<<len(b)):
            chosen={b[k] for k in range(len(b)) if bits>>k&1}
            events.add(frozenset(i for i,s in enumerate(states) if s&chosen))
    events=sorted(events,key=lambda e:(len(e),tuple(e))); ei={e:i for i,e in enumerate(events)}
    assert len(states)==224 and len(events)==56
    return states,atoms,named,events,ei

def payload():
    states,names,named,events,ei=construction(); full=frozenset(range(224))
    # Intrinsic lattice atoms: minimal nonzero events in the incidence order.
    latoms=[e for e in events if e and not any(f and f<e for f in events)]
    assert len(latoms)==24
    ai={e:i for i,e in enumerate(latoms)}
    down=[frozenset(i for i,a in enumerate(latoms) if a<=e) for e in events]
    assert len(set(down))==56 # event is determined by its intrinsic atom downset

    # Intrinsic orthogonality graph; maximal cliques recover all maximal blocks.
    G=nx.Graph();G.add_nodes_from(range(24))
    for i,a in enumerate(latoms):
        for j,b in enumerate(latoms[i+1:],i+1):
            if a <= (full-b):G.add_edge(i,j)
    blocks=sorted(tuple(sorted(c)) for c in nx.find_cliques(G))
    assert len(blocks)==12 and sorted(map(len,blocks))==[3]*11+[4]

    # Every graph automorphism is tested on all 56 intrinsic downsets.  This is
    # both an exact upper bound and a constructive extension test.
    raw=[]
    for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
        image={frozenset(m[i] for i in d) for d in down}
        if image==set(down):raw.append(tuple(m[i] for i in range(24)))
    raw=sorted(set(raw));assert len(raw)==32
    down_index={d:i for i,d in enumerate(down)}

    def event_perm(p):return tuple(down_index[frozenset(p[i] for i in d)] for d in down)
    eperms=[event_perm(p) for p in raw]
    # Point signatures are unique, so each event permutation has at most one
    # incidence-code lift.  Construct it and verify every incidence bit.
    sigs=[tuple(int(k in e) for e in events) for k in range(224)]
    assert len(set(sigs))==224
    sig_index={s:k for k,s in enumerate(sigs)}
    point_perms=[]
    for ep in eperms:
        pp=tuple(sig_index[tuple(sigs[k][ep.index(j)] for j in range(56))]
                 for k in range(224))
        assert len(set(pp))==224
        assert all((k in events[i])==(pp[k] in events[ep[i]])
                   for k in range(224) for i in range(56))
        point_perms.append(pp)

    def event_id(e):return ei[e]
    q=named["e11"]|named["e10"];r=named["e11"]|named["e01"]
    armset={event_id(named["a1"]),event_id(named["a2"])}
    fixed_gate={event_id(named["a3"]),event_id(q),event_id(r)}
    fixed_prov=fixed_gate|{event_id(named["n1"]),event_id(named["s1"])}
    gate=[];prov=[]
    for p,ep,pp in zip(raw,eperms,point_perms):
        if {ep[i] for i in armset}==armset and all(ep[i]==i for i in fixed_gate):gate.append((p,ep,pp))
        if {ep[i] for i in armset}==armset and all(ep[i]==i for i in fixed_prov):prov.append((p,ep,pp))
    assert len(gate)==2 and len(prov)==2

    # Express the two certified maps by the original atom names.
    lattice_name={ai[e]:a for a,e in named.items() if e in ai}
    maps=[]
    for p,ep,pp in prov:
        amap={lattice_name[i]:lattice_name[p[i]] for i in range(24)}
        maps.append({"atom_map":amap,
          "event_permutation_sha256":hashlib.sha256(bytes(ep)).hexdigest(),
          "point_permutation_sha256":hashlib.sha256(bytes(pp)).hexdigest()})
    maps.sort(key=lambda x:json.dumps(x["atom_map"],sort_keys=True))
    named_arm={a:a for a in names};named_arm.update({"a1":"a2","a2":"a1",
      "u1":"v1","v1":"u1","p11":"p12","p12":"p11"})
    assert {tuple(sorted(x["atom_map"].items())) for x in maps}=={
      tuple(sorted({a:a for a in names}.items())),tuple(sorted(named_arm.items()))}

    out={"schema":SCHEMA,"schema_version":"1.0","states":224,"events":56,
      "intrinsic_lattice_atoms":24,"intrinsic_maximal_blocks":12,
      "maximal_block_size_histogram":{"3":11,"4":1},
      "point_signatures_unique":True,"uncoloured_orthogonality_graph_automorphisms":32,
      "all_graph_automorphisms_extend_to_event_order":True,
      "gate_color_convention":{
        "setwise_activation_arm_pair":["a1","a2"],"fixed_events":["a3","q","r"]},
      "gate_fixed_group_order":len(gate),
      "provenance_color_convention":{"additional_fixed_events":["n1","s1"]},
      "provenance_fixed_group_order":len(prov),
      "named_subgroup_order":2,"named_equals_full_provenance_fixed_group":True,
      "automorphisms":maps,
      "proof_certificate":"intrinsic atom/block automorphism exhaustion plus unique point-signature lift",
      "scope":"exact single-cell 224-point/56-event incidence-code group under displayed colors; no full-grid faithfulness claim",
      "command":"python3 notes/open_questions/verification/h4_cell_incidence_automorphism.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"h4_cell_incidence_automorphism.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
      "gate_group":out["gate_fixed_group_order"],"provenance_group":out["provenance_fixed_group_order"]},indent=2,sort_keys=True))
if __name__=="__main__":main()
