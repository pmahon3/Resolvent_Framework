#!/usr/bin/env python3
"""Independent declared-block replay of the H4 cell automorphism receipt."""
import json, os, sys
import networkx as nx

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell

def main():
    receipt=json.load(open(os.path.join(HERE,"h4_cell_incidence_automorphism.json")))
    states=cell.cell_states();atoms=sorted({a for b in cell.CELL_BLOCKS for a in b})
    G=nx.Graph()
    for a in atoms:G.add_node(("a",a),kind="atom")
    for i,b in enumerate(cell.CELL_BLOCKS):
        G.add_node(("b",i),kind="block",size=len(b))
        for a in b:G.add_edge(("a",a),("b",i))
    match=nx.algorithms.isomorphism.categorical_node_match(["kind","size"],[None,None])
    autos=[]
    for M in nx.algorithms.isomorphism.GraphMatcher(G,G,node_match=match).isomorphisms_iter():
        p={a:M[("a",a)][1] for a in atoms}
        if {p["a1"],p["a2"]}!={"a1","a2"}:continue
        if p["a3"]!="a3" or p["n1"]!="n1" or p["s1"]!="s1":continue
        if {p[x] for x in ("e11","e10")}!={"e11","e10"}:continue
        if {p[x] for x in ("e11","e01")}!={"e11","e01"}:continue
        # Direct state-code check, independent of intrinsic atom-downsets.
        if {frozenset(p[a] for a in s) for s in states}!=set(states):continue
        autos.append(p)
    unique={tuple(sorted(p.items())) for p in autos}
    certified={tuple(sorted(x["atom_map"].items())) for x in receipt["automorphisms"]}
    assert len(unique)==2 and unique==certified
    assert receipt["named_equals_full_provenance_fixed_group"] is True
    print(json.dumps({"status":"PASS","declared_block_automorphisms":len(unique),
      "matches_intrinsic_certificate":True,"payload_sha256":receipt["payload_sha256"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
