#!/usr/bin/env python3
"""Exact smallest whole-macrofibre repairs in the full conditional K_2,2 grid.

The two ambiguous coordinate fibres are (q0,q1,r0,r1)=0110 and 1001.
Each splits into 49 activation-pair macrofibres.  The unique smallest macrofibre
in either has 64 points, at activation pair (110,110).  We adjoin the forced
lower union plus one such class, or the symmetric pair of classes, then take
the exact concrete complement/disjoint-union closure and report the next cut.
No exhaustive claim over arbitrary subsets of an ambiguous macrofibre is made.
"""
import argparse,hashlib,json,os,sys

HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA="full-grid-whole-activation-pair-macrofibre-repair-v2"; VERSION="2.0"

def sha_mask(z,n):return hashlib.sha256(z.to_bytes((n+7)//8,"little")).hexdigest()

def first_failure(ev):
    ev=sorted(ev);up,down=grid.order_tables(ev)
    for i in range(len(ev)):
        for j in range(i,len(ev)):
            mu,ml=grid.extrema_indices(up,down,i,j)
            if len(mu)!=1 or len(ml)!=1:
                return ev[i],ev[j],[ev[k] for k in mu],[ev[k] for k in ml]
    return None

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build()
    base,base_rounds=grid.closure(raw,full);base=set(base)
    x=masks[((0,1),"e01")];y=masks[((1,0),"e10")]
    U=full^masks[((0,0),"e11")]; V=full^masks[((1,1),"e00")]
    lower=x|y;upper=U&V;gap=upper&~lower
    targets={}
    offset=0
    class_census={};class_keyed={}
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        coord=(q0,q1,r0,r1);key="".join(map(str,coord))
        if coord in ((0,1,1,0),(1,0,0,1)):
            class_census.setdefault(key,[]).append(size)
            class_keyed.setdefault(key,[]).append((a0,a1,size))
            if a0==(1,1,0) and a1==(1,1,0):
                targets[key]=((1<<size)-1)<<offset
        offset+=size
    assert set(targets)=={"0110","1001"}
    assert all(z.bit_count()==64 and z&~gap==0 for z in targets.values())
    assert all(len(v)==49 and sum(v)==336400 and min(v)==64 for v in class_census.values())
    assert all([(a0,a1,size) for a0,a1,size in class_keyed[k] if size==64]
               ==[((1,1,0),(1,1,0),64)] for k in ("0110","1001"))
    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")]
    q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    r0=masks[((0,0),"e11")]|masks[((0,0),"e01")]
    r1=masks[((0,1),"e11")]|masks[((0,1),"e01")]
    cylinders=[]
    for row in (0,1):
        c=full
        for a in grid.base.SHARED:c&=masks[((row,0),a)]
        cylinders.append(c)
    activated_diagonal=sorted({(q0,q1,r0,r1) for a0,a1,q0,q1,r0,r1,_,_ in macro
                               if a0==(1,1,1) and a1==(1,1,1)})
    assert activated_diagonal==[(0,0,0,0),(1,1,1,1)]
    def reconstructed(ev,a,b):
        return all(z in ev for z in (a&b,a&(full^b),(full^a)&b,(full^a)&(full^b)))
    variants=[]
    for name,extra in (("one-sided-0110-64",targets["0110"]),
                       ("symmetric-128",targets["0110"]|targets["1001"])):
        repair=lower|extra
        ev,rounds=grid.closure(base|{repair,full^repair},full);es=set(ev)
        original_ub=[z for z in ev if x|z==z and y|z==z]
        original_mu=[z for z in original_ub if not any(w!=z and w|z==z for w in original_ub)]
        assert original_mu==[repair]
        failure=first_failure(ev);assert failure is not None
        fx,fy,mu,ml=failure
        next_lower=fx|fy;next_upper=full
        for u in mu:next_upper&=u
        next_gap=next_upper&~next_lower
        variants.append({"name":name,"selected_optional_points":extra.bit_count(),
            "repair_sha256":sha_mask(repair,n),"events":len(ev),"closure_rounds":rounds,
            "original_crossed_pair_post_closure_unique_join":True,
            "original_crossed_pair_join_sha256":sha_mask(original_mu[0],n),
            "lattice":False,"first_next_cut":{"x_sha256":sha_mask(fx,n),
                "y_sha256":sha_mask(fy,n),"x_cardinality":fx.bit_count(),
                "y_cardinality":fy.bit_count(),
                "x_original_label":labels.get(fx),"y_original_label":labels.get(fy),
                "admissible_lower_sha256":sha_mask(next_lower,n),
                "admissible_upper_sha256":sha_mask(next_upper,n),
                "admissible_lower_cardinality":next_lower.bit_count(),
                "admissible_upper_cardinality":next_upper.bit_count(),
                "admissible_gap_points":next_gap.bit_count(),
                "minimal_upper_bounds_sha256":[sha_mask(z,n) for z in mu],
                "minimal_upper_bound_cardinalities":[z.bit_count() for z in mu],
                "minimal_upper_bound_original_labels":[labels.get(z) for z in mu],
                "maximal_lower_bounds_sha256":[sha_mask(z,n) for z in ml],
                "maximal_lower_bound_cardinalities":[z.bit_count() for z in ml]},
            "q0_q1_boundary_reconstructed":reconstructed(es,q0,q1),
            "r0_r1_boundary_reconstructed":reconstructed(es,r0,r1),
            "activation_cylinders_are_not_events":[c not in es for c in cylinders],
            "no_nonzero_event_is_subset_of_activation_cylinder":[
                all(not z or bool(z&(full^c)) for z in ev) for c in cylinders],
            "every_nonzero_event_has_off_cylinder_point":[
                all(not z or bool(z&(full^c)) for z in ev) for c in cylinders],
            "both_rows_activated_coordinate_relation":[list(z) for z in activated_diagonal]})
    dep=hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest()
    out={"schema":SCHEMA,"schema_version":VERSION,"carrier_points":n,
         "raw_events":len(raw),"base_events":len(base),"base_closure_rounds":base_rounds,
         "ambiguous_gap_points":gap.bit_count(),"ambiguous_coordinate_fibres":{
             k:{"activation_pair_classes":len(v),"points":sum(v),"smallest_class":min(v),
                "unique_smallest_class_activation_pair":[[1,1,0],[1,1,0]],
                "unique_smallest_class_points":64}
             for k,v in class_census.items()},"variants":variants,
         "dependency_sha256":dep,
         "command":"python3 notes/open_questions/verification/full_grid_fine_fibre_repair_audit.py --verify",
         "scope":"two smallest whole activation-pair-macrofibre repair choices; not exhaustive over unions or subsets of macrofibres"}
    out["verifier_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_fine_fibre_repair.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]} if args.verify else out,sort_keys=True,indent=2))

if __name__=="__main__":main()
