#!/usr/bin/env python3
"""Complete finite search for a K_2,2 rectangle OML without side reconstruction.

Search space: complement/disjoint-union-closed set families E contained in the
16-point powerset and containing all four K_2,2 edge Boolean algebras.  At a
deterministically chosen minimum-gap missing join, every possible trace between the forced set union
and the intersection of all current upper bounds is adjoined, with its
complement, before orthogonal closure.  Thus every terminal lattice extension is
represented.  Branches are pruned only after Bool(q0,q1) or Bool(r0,r1) appears.
"""
import argparse, hashlib, itertools, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import bipartite_coordinate_core_audit as core

SCHEMA="rectangle-no-side-reconstruction-search-v2"
PTS=core.carrier(2,2); FULL=(1<<16)-1

def close(seed): return frozenset(core.close(seed,FULL)[0])

def close_until_reconstruction(base,additions):
    """Incremental closure, aborting when one same-side joint atom occurs."""
    ev=set(base); frontier=set(additions)-ev; rounds=0
    while True:
        frontier|={FULL^x for x in frontier}-ev
        qhit=next((z for z in Q_ATOMS if z in ev or z in frontier),None)
        rhit=next((z for z in R_ATOMS if z in ev or z in frontier),None)
        if qhit is not None or rhit is not None:
            return frozenset(ev|frontier),qhit,rhit,rounds,False
        if not frontier:return frozenset(ev),None,None,rounds,True
        snap=sorted(ev|frontier); new=set()
        for x in sorted(frontier):
            for y in snap:
                if not x&y and x|y not in ev and x|y not in frontier:
                    w=x|y;new.add(w)
                    qhit=w if w in Q_ATOMS else None;rhit=w if w in R_ATOMS else None
                    if qhit is not None or rhit is not None:
                        return frozenset(ev|frontier|new),qhit,rhit,rounds+1,False
        rounds+=1
        ev|=frontier;frontier=new

def floor_table(events):
    f=[0]*65536
    for z in events:f[z]=z
    for bit in range(16):
        b=1<<bit
        for z in range(65536):
            if z&b:f[z]|=f[z^b]
    return f

def missing_join(events,minimum_gap=True):
    ev=sorted(events); es=events; f=floor_table(events)
    best=None
    for k,x in enumerate(ev):
        for y in ev[k:]:
            z=FULL^f[FULL^(x|y)]
            if z not in es:
                gap=(z&~(x|y)).bit_count()
                if not minimum_gap:
                    best=(gap,x,y);break
                if best is None or (gap,x,y)<best[:3]:best=(gap,x,y)
                if minimum_gap and gap==0:break
        if not minimum_gap and best is not None:break
        if minimum_gap and best is not None and best[0]==0:break
    if best is None:return None
    _,x,y=best;ub=[u for u in ev if x|u==u and y|u==u]
    mu=[u for u in ub if not any(v!=u and v|u==u for v in ub)]
    return x,y,mu

def pair_atoms(i,j):
    return tuple(core.mask(PTS,lambda p,i=i,j=j,u=u,v=v:p[i]==u and p[j]==v)
                 for u in (0,1) for v in (0,1))

Q_ATOMS=pair_atoms(0,1); R_ATOMS=pair_atoms(2,3)
def reconstruction(events):
    return all(z in events for z in Q_ATOMS),all(z in events for z in R_ATOMS)

# Full 128-element automorphism group of the unlabelled K_2,2 coordinate core:
# independent bit flips and coordinate permutations preserving or exchanging sides.
COORD_PERMS=[p for p in itertools.permutations(range(4))
             if set(p[:2]) in ({0,1},{2,3})]
POINT_INDEX={p:k for k,p in enumerate(PTS)}
POINT_MAPS=[]
for perm in COORD_PERMS:
    for flip in itertools.product((0,1),repeat=4):
        POINT_MAPS.append(tuple(POINT_INDEX[tuple(p[perm[j]]^flip[j] for j in range(4))]
                                for p in PTS))
assert len(set(POINT_MAPS))==128
_POINT_MAP_SET=set(POINT_MAPS)
assert all(tuple(pm.index(k) for k in range(16)) in _POINT_MAP_SET
           for pm in POINT_MAPS)
assert all(tuple(a[b[k]] for k in range(16)) in _POINT_MAP_SET
           for a in POINT_MAPS for b in POINT_MAPS)

_mask_cache={}
def map_mask(z,pm):
    key=(z,pm)
    got=_mask_cache.get(key)
    if got is not None:return got
    out=0
    for k in range(16):
        if z>>k&1:out|=1<<pm[k]
    _mask_cache[key]=out
    return out

def canonical(events):
    return min(tuple(sorted(map_mask(z,pm) for z in events)) for pm in POINT_MAPS)

def family_id(can):
    raw=b"".join(z.to_bytes(2,"little") for z in can)
    return hashlib.sha256(raw).hexdigest()

def oml(events):
    f=floor_table(events); es=events
    meet=lambda x,y:f[x&y]
    join=lambda x,y:FULL^f[FULL^(x|y)]
    return all(join(x,meet(y,FULL^x))==y
               for x in events for y in events if x|y==y)

def search():
    initial=close(core.raw_family(2,2,PTS))
    # Independent shallow validation: without symmetry there are four distinct
    # first children; global canonicalization identifies exactly two orbits.
    root_fail=missing_join(initial);rx,ry,rmu=root_fail
    rlo=rx|ry;rhi=FULL
    for u in rmu:rhi&=u
    rgap=rhi&~rlo;root_candidates=[];sub=rgap
    while True:
        root_candidates.append(rlo|sub)
        if sub==0:break
        sub=(sub-1)&rgap
    root_children=[close(set(initial)|{z,FULL^z}) for z in root_candidates]
    shallow={"depth":1,"symmetry_off_candidate_count":len(root_candidates),
             "symmetry_off_distinct_closed_children":len(set(root_children)),
             "symmetry_on_canonical_classes":len({canonical(e) for e in root_children}),
             "candidate_masks_hex":[hex(z) for z in root_candidates]}
    assert shallow["symmetry_off_distinct_closed_children"]==4
    assert shallow["symmetry_on_canonical_classes"]==2
    assert all(frozenset(map_mask(z,pm) for z in initial)==initial for pm in POINT_MAPS)
    side_atom_sets={frozenset(Q_ATOMS),frozenset(R_ATOMS)}
    assert all(frozenset(map_mask(z,pm) for z in Q_ATOMS) in side_atom_sets and
               frozenset(map_mask(z,pm) for z in R_ATOMS) in side_atom_sets
               for pm in POINT_MAPS)
    # Machine-check the hand forcing lemma used by the early prune.
    assert all(all(a in close(set(initial)|{z,FULL^z}) for a in side)
               for side in (Q_ATOMS,R_ATOMS) for z in side)
    # Compare lex-first and minimum-gap policies as a diagnostic.  They need
    # not visit the same depth-two nodes because they choose different cuts;
    # completeness is supplied by interval branching, not policy equality.
    def children(parent,minimum_gap):
        f=missing_join(parent,minimum_gap);x,y,mu=f;lo=x|y;hi=FULL
        for u in mu:hi&=u
        gap=hi&~lo;out=[];sub=gap;seeds=set()
        while True:
            z=lo|sub;seed=frozenset((z,FULL^z))
            if seed not in seeds:
                seeds.add(seed);child,qh,rh,_,done=close_until_reconstruction(parent,seed)
                if done:
                    assert child==close(set(parent)|set(seed))
                    out.append(child)
            if sub==0:break
            sub=(sub-1)&gap
        return set(out)
    old1=children(initial,False);new1=children(initial,True)
    assert old1==new1
    old2=set().union(*(children(e,False) for e in old1))
    new2=set().union(*(children(e,True) for e in new1))
    shallow["old_new_exact_closed_children_equal_depth_1"]=True
    shallow["old_new_exact_closed_children_equal_depth_2"]=old2==new2
    shallow["old_lex_depth_2_closed_children"]=len(old2)
    shallow["new_min_gap_depth_2_closed_children"]=len(new2)
    shallow["depth_2_exact_child_intersection"]=len(old2&new2)
    shallow["incremental_closure_equals_baseline_through_depth_2"]=True
    stats={"nodes_entered":0,"new_symmetry_classes":0,"memo_prunes":0,
           "q_reconstruction_prunes":0,"r_reconstruction_prunes":0,
           "both_reconstruction_prunes":0,"terminal_lattices":0,
           "terminal_omls":0,"terminal_non_oml_lattices":0,
           "candidate_branches":0,"duplicate_child_prunes":0,
           "max_depth":0,"max_events":len(initial),"max_gap_bits":0,
           "nodes_by_depth":{},"closed_children_by_size":{}}
    stats["unresolved_frontiers"]=0
    seen=set(); first_prune={}; terminal=[]; dag={}; frontiers=[]
    def dfs(events,depth,path):
        stats["nodes_entered"]+=1;stats["max_depth"]=max(stats["max_depth"],depth)
        stats["max_events"]=max(stats["max_events"],len(events))
        stats["nodes_by_depth"][str(depth)]=stats["nodes_by_depth"].get(str(depth),0)+1
        qrec,rrec=reconstruction(events)
        if qrec or rrec:
            key="both" if qrec and rrec else ("q" if qrec else "r")
            stats[key+"_reconstruction_prunes"]+=1
            first_prune.setdefault(key,{"depth":depth,"events":len(events),
                                        "repair_path_hex":[hex(z) for z in path]})
            return
        can=canonical(events)
        node_id=family_id(can)
        if can in seen:
            stats["memo_prunes"]+=1;return
        seen.add(can);stats["new_symmetry_classes"]+=1
        print("NODE",stats["new_symmetry_classes"],"depth",depth,"events",len(events),
              "hist",stats["nodes_by_depth"],flush=True)
        fail=missing_join(events)
        if fail is None:
            stats["terminal_lattices"]+=1
            isoml=oml(events)
            assert isoml  # complement/disjoint-closed subset lattice => OML
            stats["terminal_omls" if isoml else "terminal_non_oml_lattices"]+=1
            terminal.append({"events":len(events),"orthomodular":isoml,
                             "repair_path_hex":[hex(z) for z in path]})
            dag[node_id]={"events":len(events),"outcome":"terminal",
                          "orthomodular":isoml,"children":[]}
            return
        x,y,mu=fail; lower=x|y;upper=FULL
        for u in mu:upper&=u
        gap=upper&~lower;stats["max_gap_bits"]=max(stats["max_gap_bits"],gap.bit_count())
        candidates=[];sub=gap;seeds=set()
        while True:
            z=lower|sub
            seed=frozenset((z,FULL^z))
            if z not in events and seed not in seeds:candidates.append(z);seeds.add(seed)
            if sub==0:break
            sub=(sub-1)&gap
        stats["candidate_branches"]+=len(candidates)
        local=set(); child_records=[]
        for z in candidates:
            child,qhit,rhit,rounds,completed=close_until_reconstruction(events,{z,FULL^z})
            if qhit is not None or rhit is not None:
                key="both" if qhit is not None and rhit is not None else ("q" if qhit is not None else "r")
                stats[key+"_reconstruction_prunes"]+=1
                first_prune.setdefault(key,{"depth":depth+1,"events_at_detection":len(child),
                                            "repair_path_hex":[hex(w) for w in path+(z,)]})
                child_records.append({"candidate_hex":hex(z),"outcome":key+"-side-atom-forces-reconstruction",
                                      "forcing_side_atom_hex":hex(qhit if qhit is not None else rhit),
                                      "events_at_detection":len(child),"closure_rounds":rounds})
                continue
            if not completed:
                stats["unresolved_frontiers"]+=1
                fid=hashlib.sha256(b"".join(w.to_bytes(2,"little") for w in sorted(child))).hexdigest()
                rec={"candidate_hex":hex(z),"outcome":"closure-frontier",
                     "partial_family_id":fid,"events_at_stop":len(child),
                     "closure_rounds":rounds,"q_reconstructed":False,"r_reconstructed":False}
                child_records.append(rec);frontiers.append({"depth":depth+1,
                    "repair_path_hex":[hex(w) for w in path+(z,)],**rec})
                continue
            ck=canonical(child)
            cid=family_id(ck)
            if ck in local:
                stats["duplicate_child_prunes"]+=1
                child_records.append({"candidate_hex":hex(z),"outcome":"sibling-symmetry-duplicate",
                                      "canonical_child_id":cid,"events":len(child)})
                continue
            local.add(ck)
            stats["closed_children_by_size"][str(len(child))]=stats["closed_children_by_size"].get(str(len(child)),0)+1
            child_records.append({"candidate_hex":hex(z),"outcome":"closed-child",
                                  "child_id":cid,"events":len(child),"closure_rounds":rounds})
            dfs(child,depth+1,path+(z,))
        dag[node_id]={"events":len(events),"outcome":"branched",
                      "failed_pair_hex":[hex(x),hex(y)],
                      "minimal_upper_bounds_hex":[hex(u) for u in mu],
                      "admissible_interval_hex":[hex(lower),hex(upper)],
                      "gap_bits":gap.bit_count(),"candidate_count":len(candidates),
                      "children":child_records}
    dfs(initial,0,())
    assert all(v["candidate_count"]==len(v["children"])
               for v in dag.values() if v["outcome"]=="branched")
    referenced=[c.get("child_id") or c.get("canonical_child_id")
                for v in dag.values() for c in v["children"]
                if c["outcome"] in ("closed-child","sibling-symmetry-duplicate")]
    assert all(cid in dag for cid in referenced)
    return {"initial_events":len(initial),"symmetry_group_order":len(POINT_MAPS),
            "symmetry_validation":{"initial_family_invariant_under_group":True,
                                   "same_side_reconstruction_predicate_invariant":True,
                                   "shallow_off_vs_on":shallow},
            "statistics":stats,"first_reconstruction_prunes":first_prune,
            "terminal_families":terminal,"proof_dag":dag,
            "proof_dag_audit":{"every_candidate_has_one_disposition":True,
                               "every_closed_or_memo_child_resolves_to_a_node":True,
                               "branched_nodes":len(dag),
                               "candidate_edges":sum(v.get("candidate_count",0) for v in dag.values())},
            "unresolved_closure_frontiers":frontiers,
            "search_status":"complete-no-go" if not frontiers and stats["terminal_omls"]==0
                            else ("counterexample-found" if stats["terminal_omls"] else "incomplete-frontier"),
            "result_no_unreconstructed_oml":
                (stats["terminal_omls"]==0 if not frontiers else None)}

def payload():
    result=search()
    dep=hashlib.sha256(open(core.__file__,"rb").read()).hexdigest()
    verifier=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out={"schema":SCHEMA,"schema_version":"2.0","result":result,
         "dependency_sha256":dep,"verifier_sha256":verifier,
         "command":"python3 notes/open_questions/verification/rectangle_no_reconstruction_search.py --verify",
         "scope":"complete only inside P(2^4), retaining all 16 profiles and the full K_2,2 edge core"}
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true")
    ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"rectangle_no_reconstruction_search.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path))==out
    if args.verify:
        print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]},sort_keys=True))
    else:
        print(json.dumps(out,sort_keys=True,indent=2))

if __name__=="__main__":main()
