#!/usr/bin/env python3
"""Exact third-gap census after the symmetric-128 and fixed-four repairs.

This script adds no third repair.  It classifies the next admissible interval
by row activations, coordinate profiles, and exact Cartesian local-state factor
subsets, and records its intersections with activation cylinders and the two
same-side coordinate Boolean atom systems.
"""
import argparse,collections,hashlib,json,os,sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA="full-grid-third-gap-cartesian-classification-v2"

def digest_ids(ids):return hashlib.sha256(json.dumps(sorted(ids),separators=(",",":")).encode()).hexdigest()
def digest_mask(z,n):return hashlib.sha256(z.to_bytes((n+7)//8,"little")).hexdigest()

def failure(ev):
    ev=sorted(ev);up,down=grid.order_tables(ev)
    for i in range(len(ev)):
        for j in range(i,len(ev)):
            mu,ml=grid.extrema_indices(up,down,i,j)
            if len(mu)!=1 or len(ml)!=1:return ev[i],ev[j],[ev[k] for k in mu],[ev[k] for k in ml]

def factor_projection(segment,ns):
    projs=[set() for _ in ns];mult=[]
    for c in range(4):
        m=1
        for z in ns[c+1:]:m*=z
        mult.append(m)
    z=segment
    while z:
        bit=(z&-z).bit_length()-1;z&=z-1
        for c in range(4):projs[c].add((bit//mult[c])%ns[c])
    prod=1
    for p in projs:prod*=len(p)
    return projs,prod==segment.bit_count()

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build()
    groups={}
    for j,s in enumerate(states):
        a=tuple(int(x in s) for x in grid.base.SHARED)
        q=int("e11" in s or "e10" in s);r=int("e11" in s or "e01" in s)
        groups.setdefault((a,q,r),[]).append(j)
    base,_=grid.closure(raw,full);base=set(base)
    x=masks[((0,1),"e01")];y=masks[((1,0),"e10")]
    p_lo=x|y;p_hi=(full^masks[((0,0),"e11")])&(full^masks[((1,1),"e00")])
    primary={};offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==a1==(1,1,0) and (q0,q1,r0,r1) in ((0,1,1,0),(1,0,0,1)):
            primary["".join(map(str,(q0,q1,r0,r1)))]=((1<<size)-1)<<offset
        offset+=size
    join1=p_lo|primary["0110"]|primary["1001"]
    stage1,_=grid.closure(base|{join1,full^join1},full);stage1=set(stage1)
    sx,sy,smu,sml=failure(stage1);slo=sx|sy;shi=full
    for u in smu:shi&=u
    sgap=shi&~slo;fixed=None;offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==(1,1,1) and a1==(1,1,0) and (q0,q1,r0,r1)==(0,1,0,0):
            fixed=((1<<size)-1)<<offset;assert size==4
        offset+=size
    assert fixed is not None and fixed&~sgap==0
    join2=slo|fixed
    stage2,rounds2=grid.closure(stage1|{join2,full^join2},full);stage2=set(stage2)
    tx,ty,tmu,tml=failure(stage2);tlo=tx|ty;thi=full
    for u in tmu:thi&=u
    gap=thi&~tlo;assert gap.bit_count()==1666232

    rows=[];factor_hist=collections.Counter();activation_totals=collections.Counter();coord_totals=collections.Counter()
    structural=collections.Counter();offset=0;whole_count=0
    minimum=[]
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        segment=(gap>>offset)&((1<<size)-1)
        if segment:
            if segment.bit_count()==size:whole_count+=1
            projs,cart=factor_projection(segment,ns);assert cart
            lists=[groups[(a0,q0,r0)],groups[(a0,q0,r1)],groups[(a1,q1,r0)],groups[(a1,q1,r1)]]
            chosen=[[lists[c][j] for j in sorted(projs[c])] for c in range(4)]
            factors=tuple(len(p) for p in projs);coord="".join(map(str,(q0,q1,r0,r1)))
            hashes=tuple(digest_ids(z) for z in chosen);count=segment.bit_count()
            factor_hist[(count,coord,tuple(ns),factors)]+=1
            activation_totals[(a0,a1)]+=count;coord_totals[coord]+=count
            structural[(a0,a1,coord,tuple(ns),factors,hashes)]+=1
            rec={"points":count,"row0_activation":list(a0),"row1_activation":list(a1),
                 "coordinate_profile":list((q0,q1,r0,r1)),"ambient_factor_sizes":list(ns),
                 "selected_factor_sizes":list(factors),"selected_state_index_sha256":list(hashes)}
            rows.append(rec)
            if count==2:
                rec=dict(rec);rec["selected_local_state_indices"]=chosen
                rec["selected_local_state_atoms"]=[[sorted(states[j]) for j in z] for z in chosen]
                minimum.append(rec)
        offset+=size
    assert len(rows)==346 and whole_count==0 and len(minimum)==1
    assert min(r["points"] for r in rows)==2
    assert minimum[0]["row0_activation"]==[1,1,0] and minimum[0]["row1_activation"]==[1,1,1]
    assert minimum[0]["coordinate_profile"]==[0,1,1,1]
    assert minimum[0]["ambient_factor_sizes"]==[2,2,1,1]
    assert minimum[0]["selected_factor_sizes"]==[2,1,1,1]

    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")];q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    r0=masks[((0,0),"e11")]|masks[((0,0),"e01")];r1=masks[((0,1),"e11")]|masks[((0,1),"e01")]
    def atom_counts(a,b):return [int((gap&z).bit_count()) for z in (a&b,a&(full^b),(full^a)&b,(full^a)&(full^b))]
    cylinders=[]
    for row in (0,1):
        c=full
        for a in grid.base.SHARED:c&=masks[((row,0),a)]
        cylinders.append(c)
    histogram=[{"points":k[0],"coordinate_profile":k[1],"ambient_factor_sizes":list(k[2]),
                "selected_factor_sizes":list(k[3]),"classes":v} for k,v in sorted(factor_hist.items())]
    out={"schema":SCHEMA,"schema_version":"2.0","carrier_points":n,
         "recurrence":{"primary_gap_points":(p_hi&~p_lo).bit_count(),
             "secondary_gap_points":sgap.bit_count(),"third_gap_points":gap.bit_count(),
             "primary_structure":"two whole coordinate fibres",
             "secondary_structure":"105 whole Cartesian macrofibres",
             "third_structure":"346 proper Cartesian subrectangles; no whole macrofibre"},
         "stage2_events":len(stage2),"stage2_closure_rounds":rounds2,
         "third_gap_macrofibres":len(rows),"whole_macrofibres":whole_count,
         "all_intersections_cartesian":True,"minimum_subrectangle":minimum[0],
         "factor_type_histogram":histogram,
         "row_activation_pair_totals":[{"row0":list(k[0]),"row1":list(k[1]),"points":v} for k,v in sorted(activation_totals.items())],
         "coordinate_profile_totals":[{"profile":list(map(int,k)),"points":v} for k,v in sorted(coord_totals.items())],
         "activation_intersections":{"row0_111":(gap&cylinders[0]).bit_count(),
             "row1_111":(gap&cylinders[1]).bit_count(),"both_111":(gap&cylinders[0]&cylinders[1]).bit_count()},
         "same_side_boolean_atom_intersections":{"q0_q1_atoms":atom_counts(q0,q1),"r0_r1_atoms":atom_counts(r0,r1)},
         "third_failed_cut":{"x_sha256":digest_mask(tx,n),"x_cardinality":tx.bit_count(),
             "y_sha256":digest_mask(ty,n),"y_cardinality":ty.bit_count(),
             "minimal_upper_bounds":[{"sha256":digest_mask(z,n),"cardinality":z.bit_count()} for z in tmu],
             "maximal_lower_bounds":[{"sha256":digest_mask(z,n),"cardinality":z.bit_count()} for z in tml],
             "admissible_lower_sha256":digest_mask(tlo,n),"admissible_lower_cardinality":tlo.bit_count(),
             "admissible_upper_sha256":digest_mask(thi,n),"admissible_upper_cardinality":thi.bit_count(),
             "gap_sha256":digest_mask(gap,n),"gap_cardinality":gap.bit_count()},
         "structural_factor_descriptors":len(structural),"structural_factor_descriptor_multiplicity_histogram":{
             str(k):v for k,v in sorted(collections.Counter(structural.values()).items())},
         "third_repair_added":False,
         "dependency_sha256":hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
         "command":"python3 notes/open_questions/verification/full_grid_third_gap_classification.py --verify",
         "scope":"exact third-gap census after two fixed repairs; structural factor descriptors are not claimed automorphism orbits"}
    out["verifier_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_third_gap_classification.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]} if args.verify else out,sort_keys=True,indent=2))

if __name__=="__main__":main()
