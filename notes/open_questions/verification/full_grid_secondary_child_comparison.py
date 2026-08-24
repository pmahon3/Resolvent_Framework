#!/usr/bin/env python3
"""Compare two four-point children of the symmetric-128 secondary gap.

The children select the whole macrofibre with row0 activation 111, coordinate
profile 0100, and row1 activation respectively 011 and 110.  The comparison
stops at each child's next failed cut and minimum Cartesian descriptor.
"""
import argparse,collections,hashlib,json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_2x2_conditional_cell_audit as grid
import full_grid_third_gap_classification as prior

SCHEMA="full-grid-secondary-four-point-child-comparison-v2"
def sha(z,n):return hashlib.sha256(z.to_bytes((n+7)//8,"little")).hexdigest()

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build();base,_=grid.closure(raw,full);base=set(base)
    x=masks[((0,1),"e01")];y=masks[((1,0),"e10")];lo=x|y;primary={};offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==a1==(1,1,0) and (q0,q1,r0,r1) in ((0,1,1,0),(1,0,0,1)):
            primary["".join(map(str,(q0,q1,r0,r1)))]=((1<<size)-1)<<offset
        offset+=size
    join1=lo|primary["0110"]|primary["1001"]
    sym,_=grid.closure(base|{join1,full^join1},full);sym=set(sym)
    sx,sy,smu,sml=prior.failure(sym);slo=sx|sy;shi=full
    for u in smu:shi&=u
    sgap=shi&~slo;children={};offset=0;secondary_rows=[]
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        segment=(sgap>>offset)&((1<<size)-1)
        if segment:
            projs,cart=prior.factor_projection(segment,ns);assert cart
            secondary_rows.append({"points":segment.bit_count(),"row0_activation":list(a0),
                "row1_activation":list(a1),"coordinate_profile":list((q0,q1,r0,r1)),
                "ambient_factor_sizes":list(ns),"selected_factor_sizes":[len(p) for p in projs]})
        if a0==(1,1,1) and a1 in ((0,1,1),(1,1,0)) and (q0,q1,r0,r1)==(0,1,0,0):
            block=((1<<size)-1)<<offset;assert size==4 and block&~sgap==0
            children["".join(map(str,a1))]=block
        offset+=size
    assert set(children)=={"011","110"}
    secondary_min=min(z["points"] for z in secondary_rows)
    secondary_minima=[z for z in secondary_rows if z["points"]==secondary_min]
    assert secondary_min==4 and len(secondary_minima)==3
    assert {tuple(z["row1_activation"]) for z in secondary_minima}=={(0,1,1),(1,0,1),(1,1,0)}
    assert all(z["row0_activation"]==[1,1,1] and z["coordinate_profile"]==[0,1,0,0]
               and z["ambient_factor_sizes"]==[1,1,2,2] and z["selected_factor_sizes"]==[1,1,2,2]
               for z in secondary_minima)
    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")];q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    r0=masks[((0,0),"e11")]|masks[((0,0),"e01")];r1=masks[((0,1),"e11")]|masks[((0,1),"e01")]
    def recon(es,a,b):return all(z in es for z in (a&b,a&(full^b),(full^a)&b,(full^a)&(full^b)))
    cylinders=[]
    for row in (0,1):
        c=full
        for a in grid.base.SHARED:c&=masks[((row,0),a)]
        cylinders.append(c)
    results=[]
    for key in ("011","110"):
        join=slo|children[key];ev,rounds=grid.closure(sym|{join,full^join},full);es=set(ev)
        ub=[z for z in ev if sx|z==z and sy|z==z];mu=[z for z in ub if not any(w!=z and w|z==z for w in ub)]
        assert mu==[join]
        fx,fy,fmu,fml=prior.failure(es);flo=fx|fy;fhi=full
        for u in fmu:fhi&=u
        gap=fhi&~flo;descriptors=[];hist=collections.Counter();offset=0
        for a0,a1,q0v,q1v,r0v,r1v,ns,size in macro:
            segment=(gap>>offset)&((1<<size)-1)
            if segment:
                projs,cart=prior.factor_projection(segment,ns);assert cart
                rec={"points":segment.bit_count(),"row0_activation":list(a0),"row1_activation":list(a1),
                    "coordinate_profile":list((q0v,q1v,r0v,r1v)),"ambient_factor_sizes":list(ns),
                    "selected_factor_sizes":[len(p) for p in projs]}
                descriptors.append(rec)
                hist[(rec["points"],"".join(map(str,(q0v,q1v,r0v,r1v))),tuple(ns),tuple(rec["selected_factor_sizes"]))]+=1
            offset+=size
        assert len(descriptors)==346
        m=min(z["points"] for z in descriptors);minimum=[z for z in descriptors if z["points"]==m]
        decomposition_sha=hashlib.sha256(json.dumps(descriptors,sort_keys=True,separators=(",",":")).encode()).hexdigest()
        compact_hist=[{"points":k[0],"coordinate_profile":k[1],"ambient_factor_sizes":list(k[2]),
                       "selected_factor_sizes":list(k[3]),"classes":v} for k,v in sorted(hist.items())]
        results.append({"child_row1_activation":list(map(int,key)),"events":len(es),"closure_rounds":rounds,
            "selected_pair_unique_join":True,"join_sha256":sha(join,n),"lattice":False,
            "next_gap_points":gap.bit_count(),"next_gap_sha256":sha(gap,n),
            "next_lower_sha256":sha(flo,n),"next_lower_cardinality":flo.bit_count(),
            "next_upper_sha256":sha(fhi,n),"next_upper_cardinality":fhi.bit_count(),
            "next_gap_cartesian_macrofibres":len(descriptors),
            "next_gap_decomposition_sha256":decomposition_sha,
            "next_gap_factor_type_histogram":compact_hist,
            "minimum_next_gap_descriptors":minimum,
            "q0_q1_boundary_reconstructed":recon(es,q0,q1),"r0_r1_boundary_reconstructed":recon(es,r0,r1)})
        results[-1]["activation_cylinders_absent"]=[c not in es for c in cylinders]
        results[-1]["every_nonzero_event_has_off_cylinder_point"]=[all(not z or z&(full^c) for z in es) for c in cylinders]
    assert [z["events"] for z in results]==[468,492]
    assert results[0]["next_gap_sha256"]==results[1]["next_gap_sha256"]
    assert results[0]["next_gap_decomposition_sha256"]==results[1]["next_gap_decomposition_sha256"]
    prior_receipt=os.path.join(HERE,"full_grid_third_gap_classification.json")
    out={"schema":SCHEMA,"schema_version":"2.0","carrier_points":n,"symmetric_base_events":len(sym),
         "secondary_global_minimum_points":secondary_min,"secondary_global_minimum_descriptors":secondary_minima,
         "children_have_identical_next_gap":True,"children_have_identical_full_decomposition":True,
         "children":results,"dependency_sha256":hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
         "prior_third_gap_receipt_file_sha256":hashlib.sha256(open(prior_receipt,"rb").read()).hexdigest(),
         "command":"python3 notes/open_questions/verification/full_grid_secondary_child_comparison.py --verify",
         "scope":"two exact four-point whole-macrofibre children; no claim about the third minimum or unions"}
    out["verifier_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_secondary_child_comparison.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]} if args.verify else out,sort_keys=True,indent=2))
if __name__=="__main__":main()
