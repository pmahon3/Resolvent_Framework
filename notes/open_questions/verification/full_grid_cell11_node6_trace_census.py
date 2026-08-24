#!/usr/bin/env python3
"""Exact cell11 traces on the full-carrier node-6 17-atom partition.

The 17 atoms are coordinate profiles 0..14 followed by the selected
cell00-definable split of profile 15 and its complement.  Only the previously
proved row-1 activation-arm involution is used for orbit counts.
"""
import argparse, collections, hashlib, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA="full-grid-cell11-node6-trace-census-v1"
SOURCE_EVENT_SHA="ae31a846410eff44a1133601bbc9bdab774ffea3e4aa10a4a5e8009752b7799c"
ARM={"a1":"a2","a2":"a1","u1":"v1","v1":"u1",
     "p11":"p12","p12":"p11"}

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build()
    profile=[0]*16;offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        profile[(q0<<3)|(q1<<2)|(r0<<1)|r1]|=((1<<size)-1)<<offset
        offset+=size
    assert all(profile) and sum(profile)==full
    activations=[]
    for row in (0,1):
        z=full
        for a in cell.SHARED:z&=masks[((row,0),a)]
        activations.append(z)

    def events_with_expressions(pos):
        events={0,full};expr={0:frozenset(),full:frozenset({"__FULL__"})}
        for block in cell.CELL_BLOCKS:
            for bits in range(1<<len(block)):
                z=0;chosen=[]
                for i,a in enumerate(block):
                    if bits>>i&1:z|=masks[(pos,a)];chosen.append(a)
                events.add(z);expr.setdefault(z,frozenset(chosen))
        assert len(events)==56 and set(expr)==events
        return events,expr

    cell00,_=events_with_expressions((0,0));cell11,expressions=events_with_expressions((1,1))
    p15=profile[15]
    traces=sorted({e&p15 for e in cell00 if e&p15 and e&p15!=p15},
                  key=lambda z:(z.bit_count(),z))
    eligible=[z for z in traces if z&~activations[0] and z&~activations[1]]
    # Align provenance by the authoritative 224-state source-event hash.  The
    # source is the local a3 event (56 local states); its full-carrier pullback
    # has 672304 points, while the selected formal-atom splitter is only its
    # trace on coordinate profile 15 and has 128040 points.
    width=(len(states)+7)//8;source_expressions=[]
    for block in cell.CELL_BLOCKS:
        for bits in range(1<<len(block)):
            chosen=frozenset(block[i] for i in range(len(block)) if bits>>i&1)
            local_mask=sum(1<<j for j,s in enumerate(states) if s&chosen)
            if hashlib.sha256(local_mask.to_bytes(width,"little")).hexdigest()==SOURCE_EVENT_SHA:
                source_expressions.append((local_mask,chosen))
    assert source_expressions and len({x[0] for x in source_expressions})==1
    source_local=source_expressions[0][0]
    source_pullbacks=set()
    for _,chosen in source_expressions:
        z=0
        for a in chosen:z|=masks[((0,0),a)]
        source_pullbacks.add(z)
    assert len(source_pullbacks)==1
    source_pullback=next(iter(source_pullbacks));piece=source_pullback&p15
    assert piece==eligible[0]
    atoms=profile[:15]+[piece,p15&~piece]
    assert sum(atoms)==full and all(not atoms[i]&atoms[j]
                                    for i in range(17) for j in range(i))

    def word(e):
        return tuple(0 if not e&a else 2 if e&a==a else 1 for a in atoms)
    words=collections.Counter(word(e) for e in cell11)
    multiplicities=collections.Counter(words.values())
    partial_by_word=collections.Counter(sum(x==1 for x in w) for w in words)
    assert len(words)==21 and multiplicities=={1:16,2:4,32:1}
    assert partial_by_word=={0:16,13:4,17:1}

    residue=profile[7]
    residue_traces={e:e&residue for e in cell11}
    residue_classes=collections.Counter(
        "empty" if not t else "full" if t==residue else "proper"
        for t in residue_traces.values())
    proper_traces={t for t in residue_traces.values() if t and t!=residue}
    assert residue_classes=={"empty":8,"full":8,"proper":40}
    assert len(proper_traces)==36

    all_atoms=sorted({a for b in cell.CELL_BLOCKS for a in b})
    arm={a:ARM.get(a,a) for a in all_atoms}
    perm={}
    for e,chosen in expressions.items():
        if "__FULL__" in chosen:ep=full
        else:
            ep=0
            for a in chosen:ep|=masks[((1,1),arm[a])]
        perm[e]=ep
    assert set(perm.values())==cell11 and all(perm[perm[e]]==e for e in cell11)
    assert all(word(perm[e])==word(e) for e in cell11)

    def involution_orbits(items,image):
        unseen=set(items);out=[]
        while unseen:
            x=min(unseen);o={x,image(x)};assert image(image(x))==x
            unseen-=o;out.append(o)
        return out
    event_orbits=involution_orbits(cell11,lambda e:perm[e])
    distinct_traces=set(residue_traces.values())
    trace_image={residue_traces[e]:residue_traces[perm[e]] for e in cell11}
    assert set(trace_image)==distinct_traces and set(trace_image.values())==distinct_traces
    trace_orbits=involution_orbits(distinct_traces,lambda t:trace_image[t])
    proper_trace_orbits=[o for o in trace_orbits if o.isdisjoint({0,residue})]
    assert len(event_orbits)==50 and collections.Counter(map(len,event_orbits))=={1:44,2:6}
    assert len(distinct_traces)==38 and len(trace_orbits)==32 and len(proper_trace_orbits)==30

    word_rows=[{"word":"".join(map(str,w)),"multiplicity":m,
                "proper_atoms":sum(x==1 for x in w)} for w,m in sorted(words.items())]
    out={"schema":SCHEMA,"schema_version":"1.0","carrier_points":n,
      "cell11_events":len(cell11),"formal_atoms":17,
      "selected_profile15_split_points":piece.bit_count(),
      "selected_source_event_sha256":SOURCE_EVENT_SHA,
      "selected_source_local_state_points":source_local.bit_count(),
      "selected_source_full_carrier_pullback_points":source_pullback.bit_count(),
      "selected_source_expressions":[list(x) for x in sorted({
          tuple(sorted(y[1])) for y in source_expressions})],
      "selected_split_rule":"trace on profile15 of the unique local source event with authoritative SHA; agrees with first by (cardinality,mask) among eligible traces",
      "selected_split_eligible_candidates":len(eligible),
      "ternary_alphabet":{"0":"empty","1":"proper","2":"full"},
      "distinct_ternary_words":len(words),
      "word_multiplicity_histogram":{str(k):v for k,v in sorted(multiplicities.items())},
      "proper_atom_count_per_word_histogram":{str(k):v for k,v in sorted(partial_by_word.items())},
      "word_rows":word_rows,
      "residue_profile_word":"0111","residue_profile_atom_mask_hex":"0x80",
      "residue_points":residue.bit_count(),"residue_event_trace_classes":dict(residue_classes),
      "distinct_proper_residue_traces":len(proper_traces),
      "proven_symmetry":"row-1 arm involution a1<->a2,u1<->v1,p11<->p12",
      "cell11_event_orbits":len(event_orbits),
      "cell11_event_orbit_size_histogram":{str(k):v for k,v in sorted(collections.Counter(map(len,event_orbits)).items())},
      "distinct_residue_traces_including_empty_full":len(distinct_traces),
      "residue_trace_orbits":len(trace_orbits),"proper_residue_trace_orbits":len(proper_trace_orbits),
      "residue_trace_orbit_size_histogram":{str(k):v for k,v in sorted(collections.Counter(map(len,trace_orbits)).items())},
      "word_rows_sha256":hashlib.sha256(json.dumps(word_rows,sort_keys=True,separators=(",",":")).encode()).hexdigest(),
      "scope":"exact cell11 event traces on one full-carrier node6 17-atom partition; only the certified row-1 arm involution; no closure, lattice, boundary, or terminal claim",
      "dependencies":{os.path.basename(grid.__file__):hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
                      os.path.basename(cell.__file__):hashlib.sha256(open(cell.__file__,"rb").read()).hexdigest()},
      "command":"python3 notes/open_questions/verification/full_grid_cell11_node6_trace_census.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_cell11_node6_trace_census.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
      "word_types":out["distinct_ternary_words"],"event_orbits":out["cell11_event_orbits"],
      "proper_residue_trace_orbits":out["proper_residue_trace_orbits"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
