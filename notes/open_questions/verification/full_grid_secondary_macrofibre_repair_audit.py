#!/usr/bin/env python3
"""Deepen the symmetric-128 full-grid repair at its secondary cut.

The secondary 677840-point gap is exactly 105 whole row-activation/local-state
Cartesian macrofibres.  Its three minimum four-point macrofibres have row
activations (111,011), (111,101), (111,110), coordinate profile 0100, and
factor sizes 1*1*2*2.  This receipt tests the fixed (111,110) four-point class.
It makes no claim about the other minima, their unions, or corner selections.
"""
import argparse,collections,hashlib,json,os,sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA="full-grid-secondary-fixed-four-macrofibre-repair-v1"

def sha(z,n):return hashlib.sha256(z.to_bytes((n+7)//8,"little")).hexdigest()

def failure(ev):
    ev=sorted(ev);up,down=grid.order_tables(ev)
    for i in range(len(ev)):
        for j in range(i,len(ev)):
            mu,ml=grid.extrema_indices(up,down,i,j)
            if len(mu)!=1 or len(ml)!=1:return ev[i],ev[j],[ev[k] for k in mu],[ev[k] for k in ml]

def payload():
    states,n,full,masks,raw,labels,interfaces,macro=grid.build()
    base,_=grid.closure(raw,full);base=set(base)
    x=masks[((0,1),"e01")];y=masks[((1,0),"e10")]
    lower=x|y;upper=(full^masks[((0,0),"e11")])&(full^masks[((1,1),"e00")])
    primary_gap=upper&~lower;primary={};offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0==a1==(1,1,0) and (q0,q1,r0,r1) in ((0,1,1,0),(1,0,0,1)):
            primary["".join(map(str,(q0,q1,r0,r1)))]=((1<<size)-1)<<offset
        offset+=size
    symmetric_join=lower|primary["0110"]|primary["1001"]
    sym,_=grid.closure(base|{symmetric_join,full^symmetric_join},full);sym=set(sym)
    sx,sy,smu,sml=failure(sym);secondary_lower=sx|sy;secondary_upper=full
    for u in smu:secondary_upper&=u
    secondary_gap=secondary_upper&~secondary_lower

    rows=[];minimum={};hist=collections.Counter();offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        block=((1<<size)-1)<<offset;part=secondary_gap&block
        if part:
            assert part==block
            key=(part.bit_count(),"".join(map(str,(q0,q1,r0,r1))),tuple(ns))
            hist[key]+=1;rows.append((part.bit_count(),a0,a1,(q0,q1,r0,r1),tuple(ns),block))
            if part.bit_count()==4:minimum[a1]=block
        offset+=size
    assert len(rows)==105 and sum(r[0] for r in rows)==677840
    assert set(minimum)=={(0,1,1),(1,0,1),(1,1,0)}
    assert all(r[0]!=4 or (r[1]==(1,1,1) and r[3]==(0,1,0,0) and r[4]==(1,1,2,2)) for r in rows)

    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")]
    q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    r0=masks[((0,0),"e11")]|masks[((0,0),"e01")]
    r1=masks[((0,1),"e11")]|masks[((0,1),"e01")]
    def reconstructed(es,a,b):return all(z in es for z in (a&b,a&(full^b),(full^a)&b,(full^a)&(full^b)))
    cylinders=[]
    for row in (0,1):
        c=full
        for a in grid.base.SHARED:c&=masks[((row,0),a)]
        cylinders.append(c)

    choices=(("fixed-110-four",minimum[(1,1,0)]),)
    variants=[]
    for name,extra in choices:
        join=secondary_lower|extra
        ev,rounds=grid.closure(sym|{join,full^join},full);es=set(ev)
        ub=[z for z in ev if sx|z==z and sy|z==z]
        mu=[z for z in ub if not any(w!=z and w|z==z for w in ub)]
        assert mu==[join]
        f=failure(ev);terminal=f is None
        item={"name":name,"selected_gap_points":extra.bit_count(),"events":len(ev),
              "closure_rounds":rounds,"secondary_pair_unique_join_equals_selection":True,
              "join_sha256":sha(join,n),"lattice":terminal,
              "q0_q1_boundary_reconstructed":reconstructed(es,q0,q1),
              "r0_r1_boundary_reconstructed":reconstructed(es,r0,r1),
              "activation_cylinders_absent":[c not in es for c in cylinders],
              "every_nonzero_event_has_off_cylinder_point":[all(not z or z&(full^c) for z in ev) for c in cylinders]}
        if f:
            fx,fy,fmu,fml=f;flo=fx|fy;fhi=full
            for u in fmu:fhi&=u
            item["next_cut"]={"x_sha256":sha(fx,n),"y_sha256":sha(fy,n),
                "minimal_upper_bounds_sha256":[sha(z,n) for z in fmu],
                "maximal_lower_bounds_sha256":[sha(z,n) for z in fml],
                "admissible_gap_points":(fhi&~flo).bit_count()}
        variants.append(item)
    compact_hist=[{"points":k[0],"coordinate_profile":k[1],"factor_sizes":list(k[2]),"classes":v}
                  for k,v in sorted(hist.items())]
    out={"schema":SCHEMA,"schema_version":"1.0","carrier_points":n,
         "symmetric_base_events":len(sym),"secondary_gap_points":secondary_gap.bit_count(),
         "secondary_gap_whole_cartesian_macrofibres":len(rows),
         "minimum_macrofibres":[{"row0_activation":[1,1,1],"row1_activation":list(a),
             "coordinate_profile":[0,1,0,0],"factor_sizes":[1,1,2,2],"points":4} for a in sorted(minimum)],
         "factor_type_histogram":compact_hist,"variants":variants,
         "dependency_sha256":hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
         "command":"python3 notes/open_questions/verification/full_grid_secondary_macrofibre_repair_audit.py --verify",
         "scope":"one fixed four-point whole macrofibre; no other-minimum, union, corner, or arbitrary-subset exhaustion"}
    out["verifier_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");args=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_secondary_macrofibre_repair.json")
    if args.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif args.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]} if args.verify else out,sort_keys=True,indent=2))

if __name__=="__main__":main()
