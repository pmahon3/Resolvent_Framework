#!/usr/bin/env python3
"""Add the unique two-point third-gap rectangle and classify the fourth gap.

This follows the already certified symmetric-128 and fixed-four repairs, adds
the unique two-point third-gap Cartesian subrectangle as the third selected
join, closes concretely, audits the structural/state gates, and stops after an
exact macrofibre classification of the next gap.  No fourth repair is added.
"""
import argparse,collections,hashlib,json,os,sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_2x2_conditional_cell_audit as grid
import full_grid_third_gap_classification as prior

SCHEMA="full-grid-third-repair-fourth-gap-v1"
def sha(z,n):return hashlib.sha256(z.to_bytes((n+7)//8,"little")).hexdigest()

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build()
    base,_=grid.closure(raw,full);base=set(base)
    x=masks[((0,1),"e01")];y=masks[((1,0),"e10")]
    lo=x|y;primary={};offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==a1==(1,1,0) and (q0,q1,r0,r1) in ((0,1,1,0),(1,0,0,1)):
            primary["".join(map(str,(q0,q1,r0,r1)))]=((1<<size)-1)<<offset
        offset+=size
    join1=lo|primary["0110"]|primary["1001"]
    stage1,_=grid.closure(base|{join1,full^join1},full);stage1=set(stage1)
    sx,sy,smu,sml=prior.failure(stage1);slo=sx|sy;shi=full
    for u in smu:shi&=u
    sgap=shi&~slo;fixed=None;offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==(1,1,1) and a1==(1,1,0) and (q0,q1,r0,r1)==(0,1,0,0):
            fixed=((1<<size)-1)<<offset;assert size==4
        offset+=size
    join2=slo|fixed
    stage2,_=grid.closure(stage1|{join2,full^join2},full);stage2=set(stage2)
    tx,ty,tmu,tml=prior.failure(stage2);tlo=tx|ty;thi=full
    for u in tmu:thi&=u
    tgap=thi&~tlo;selected=None;selected_descriptor=None;offset=0;third_counts=[]
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        segment=(tgap>>offset)&((1<<size)-1)
        if segment:
            third_counts.append(segment.bit_count())
            projs,cart=prior.factor_projection(segment,ns);assert cart
            if segment.bit_count()==2:
                assert selected is None
                selected=segment<<offset
                selected_descriptor={"row0_activation":list(a0),"row1_activation":list(a1),
                    "coordinate_profile":list((q0,q1,r0,r1)),"ambient_factor_sizes":list(ns),
                    "selected_factor_sizes":[len(p) for p in projs],"points":2}
        offset+=size
    assert min(third_counts)==2 and third_counts.count(2)==1
    assert selected_descriptor=={"row0_activation":[1,1,0],"row1_activation":[1,1,1],
        "coordinate_profile":[0,1,1,1],"ambient_factor_sizes":[2,2,1,1],
        "selected_factor_sizes":[2,1,1,1],"points":2}
    join3=tlo|selected
    stage3,rounds3=grid.closure(stage2|{join3,full^join3},full);stage3=set(stage3)
    ub=[z for z in stage3 if tx|z==z and ty|z==z]
    mu=[z for z in ub if not any(w!=z and w|z==z for w in ub)]
    assert mu==[join3]

    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")];q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    r0=masks[((0,0),"e11")]|masks[((0,0),"e01")];r1=masks[((0,1),"e11")]|masks[((0,1),"e01")]
    def recon(a,b):return all(z in stage3 for z in (a&b,a&(full^b),(full^a)&b,(full^a)&(full^b)))
    cylinders=[]
    for row in (0,1):
        c=full
        for a in grid.base.SHARED:c&=masks[((row,0),a)]
        cylinders.append(c)
    activated=sorted({(q0,q1,r0,r1) for a0,a1,q0,q1,r0,r1,_,_ in macro if a0==a1==(1,1,1)})
    assert activated==[(0,0,0,0),(1,1,1,1)]

    fail4=prior.failure(stage3);assert fail4 is not None
    fx,fy,fmu,fml=fail4;flo=fx|fy;fhi=full
    for u in fmu:fhi&=u
    gap4=fhi&~flo;assert gap4.bit_count()==205248
    rows=[];whole=0;minimum=[];hist=collections.Counter();activation=collections.Counter();coords=collections.Counter();offset=0
    for a0,a1,q0v,q1v,r0v,r1v,ns,size in macro:
        segment=(gap4>>offset)&((1<<size)-1)
        if segment:
            projs,cart=prior.factor_projection(segment,ns);assert cart
            count=segment.bit_count();factors=tuple(len(p) for p in projs);coord="".join(map(str,(q0v,q1v,r0v,r1v)))
            if count==size:whole+=1
            hist[(count,coord,tuple(ns),factors)]+=1;activation[(a0,a1)]+=count;coords[coord]+=count
            rec={"points":count,"row0_activation":list(a0),"row1_activation":list(a1),
                 "coordinate_profile":list((q0v,q1v,r0v,r1v)),"ambient_factor_sizes":list(ns),
                 "selected_factor_sizes":list(factors),"whole_macrofibre":count==size}
            rows.append(rec)
            if count==4:minimum.append(rec)
        offset+=size
    assert len(rows)==116 and whole==29 and min(z["points"] for z in rows)==4 and len(minimum)==1
    assert minimum[0]=={"points":4,"row0_activation":[1,1,0],"row1_activation":[1,1,1],
        "coordinate_profile":[1,0,0,0],"ambient_factor_sizes":[2,2,1,1],
        "selected_factor_sizes":[2,2,1,1],"whole_macrofibre":True}
    compact_hist=[{"points":k[0],"coordinate_profile":k[1],"ambient_factor_sizes":list(k[2]),
                   "selected_factor_sizes":list(k[3]),"classes":v} for k,v in sorted(hist.items())]
    decomposition_digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    out={"schema":SCHEMA,"schema_version":"1.1","carrier_points":n,
         "stage2_events":len(stage2),"selected_third_subrectangle":selected_descriptor,
         "stage3_events":len(stage3),"stage3_closure_rounds":rounds3,
         "third_pair_unique_join_equals_selected_join":True,"third_join_sha256":sha(join3,n),
         "lattice":False,"q0_q1_boundary_reconstructed":recon(q0,q1),"r0_r1_boundary_reconstructed":recon(r0,r1),
         "activation_cylinders_absent":[c not in stage3 for c in cylinders],
         "every_nonzero_event_has_off_cylinder_point":[all(not z or z&(full^c) for z in stage3) for c in cylinders],
         "both_rows_activated_relation":[list(z) for z in activated],
         "fourth_failed_cut":{"x_sha256":sha(fx,n),"x_cardinality":fx.bit_count(),
             "y_sha256":sha(fy,n),"y_cardinality":fy.bit_count(),
             "minimal_upper_bounds":[{"sha256":sha(z,n),"cardinality":z.bit_count()} for z in fmu],
             "maximal_lower_bounds":[{"sha256":sha(z,n),"cardinality":z.bit_count()} for z in fml],
             "lower_sha256":sha(flo,n),"lower_cardinality":flo.bit_count(),
             "upper_sha256":sha(fhi,n),"upper_cardinality":fhi.bit_count(),
             "gap_sha256":sha(gap4,n),"gap_cardinality":gap4.bit_count()},
         "fourth_gap_macrofibres":len(rows),"fourth_gap_whole_macrofibres":whole,
         "all_fourth_gap_intersections_cartesian":True,"minimum_fourth_gap_subrectangle":minimum[0],
         "prior_third_gap_global_minimum_points":min(third_counts),
         "fourth_gap_global_minimum_points":min(z["points"] for z in rows),
         "fourth_gap_factor_type_histogram":compact_hist,
         "fourth_gap_decomposition_sha256":decomposition_digest,
         "fourth_gap_coordinate_totals":[{"profile":list(map(int,k)),"points":v} for k,v in sorted(coords.items())],
         "fourth_gap_activation_pair_totals":[{"row0":list(k[0]),"row1":list(k[1]),"points":v} for k,v in sorted(activation.items())],
         "fourth_repair_added":False,
         "dependency_sha256":hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
         "command":"python3 notes/open_questions/verification/full_grid_third_repair_fourth_gap_audit.py --verify",
         "scope":"one exact unique two-point third repair and fourth-gap census; no fourth repair"}
    out["verifier_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_third_repair_fourth_gap.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]} if args.verify else out,sort_keys=True,indent=2))
if __name__=="__main__":main()
