#!/usr/bin/env python3
"""Exact audits of two explicit repair branches for the stripped K_2,2 core.

This is not an exhaustive search over all iterated repair choices.  It proves
that rectangle repair is possible inside the 16-point powerset, and records
that the two displayed branches reconstruct five of the six coordinate-pair
Boolean algebras and acquire nontrivial centre.
"""
import hashlib, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import bipartite_coordinate_core_audit as core

SCHEMA="stripped-rectangle-repair-branches-v2"
POINTS=core.carrier(2,2); FULL=(1<<16)-1
RECEIPT=os.path.join(HERE,"rectangle_repair_branch_receipt.json")

def close(seed): return set(core.close(seed,FULL)[0])

def floor_table(events):
    out=[0]*65536
    for z in events: out[z]=z
    for bit in range(16):
        b=1<<bit
        for z in range(65536):
            if z&b: out[z]|=out[z^b]
    return out

def lattice_ops(events):
    floor=floor_table(events)
    return (lambda x,y:floor[x&y],
            lambda x,y:FULL^floor[FULL^(x|y)])

def first_failure(events):
    """Lexicographically first missing extremum, with exact extrema."""
    ev=sorted(events); eset=set(ev); meet,join=lattice_ops(events)
    for k,x in enumerate(ev):
        for y in ev[k:]:
            if meet(x,y) not in eset or join(x,y) not in eset:
                mu,ml=core.extrema(ev,x,y)
                return x,y,mu,ml
    return None

def reconstructs(events,i,j):
    atoms=[core.mask(POINTS,lambda p,i=i,j=j,u=u,v=v:
                     p[i]==u and p[j]==v)
           for u in (0,1) for v in (0,1)]
    return all(a in events for a in atoms)

def repair_step(events,z):
    """Adjoin z,z' to the active first failed cut and certify provenance."""
    f=first_failure(events)
    assert f is not None
    x,y,mu,ml=f
    lower=x|y
    upper=FULL
    for u in mu: upper &= u
    in_interval=(lower|z)==z and (z|upper)==upper
    assert in_interval and z not in events
    after=close(events|{z,FULL^z})
    _,join=lattice_ops(after)
    post_join=join(x,y)
    assert post_join==z and z in after
    cert={"failed_pair_hex":[hex(x),hex(y)],
          "minimal_upper_bounds_hex":[hex(u) for u in mu],
          "maximal_lower_bounds_hex":[hex(u) for u in ml],
          "admissible_interval_hex":[hex(lower),hex(upper)],
          "chosen_mask_hex":hex(z),"chosen_lies_in_interval":in_interval,
          "post_closure_join_hex":hex(post_join),
          "post_closure_join_equals_chosen":post_join==z,
          "events_before":len(events),"events_after":len(after)}
    return after,cert

def audit_branch(name,repairs):
    events=close(core.raw_family(2,2,POINTS)); sizes=[len(events)]
    provenance=[]
    for z in repairs:
        events,cert=repair_step(events,z); provenance.append(cert); sizes.append(len(events))
    ev=sorted(events); eset=set(ev); meet,join=lattice_ops(events)
    lattice=all(meet(x,y) in eset and join(x,y) in eset for x in ev for y in ev)
    oml=lattice and all(join(x,meet(y,FULL^x))==y
                        for x in ev for y in ev if x|y==y)
    reconstruction={}
    names=("q0","q1","r0","r1")
    for i in range(4):
        for j in range(i+1,4):
            reconstruction[f"{names[i]}-{names[j]}"]=reconstructs(eset,i,j)
    centre=[x for x in ev if all(join(meet(x,y),meet(x,FULL^y))==x for y in ev)]
    return {"name":name,"repair_masks_hex":[hex(z) for z in repairs],
            "repair_provenance":provenance,
            "closure_sizes":sizes,"events":len(ev),"lattice":lattice,
            "orthomodular":oml,"coordinate_pair_boolean_reconstruction":reconstruction,
            "centre_size":len(centre),"centre_masks_hex":[hex(z) for z in centre]}

def payload():
    initial=close(core.raw_family(2,2,POINTS))
    x,y,mu,ml=first_failure(initial)
    lower=x|y; upper=FULL
    for u in mu: upper&=u
    gap=upper&~lower
    traces=sorted({lower|s for s in range(65536) if not s&~gap})
    assert traces==[0x537,0x53f,0x1537,0x153f]
    initial_trace_closures=[]
    for z in traces:
        family=close(initial|{z,FULL^z})
        rec=reconstructs(family,0,1)
        assert not rec
        initial_trace_closures.append({"trace_mask_hex":hex(z),
                                       "closure_events":len(family),
                                       "reconstructs_Bool_q0_q1":rec})
    assert [x["closure_events"] for x in initial_trace_closures]==[204,198,198,204]
    source_path=core.__file__
    source_hash=hashlib.sha256(open(source_path,"rb").read()).hexdigest()
    verifier_hash=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out={"schema":SCHEMA,"schema_version":"2.0",
         "command":"python3 notes/open_questions/verification/rectangle_repair_branch_audit.py --verify",
         "verifier_sha256":verifier_hash,"points":16,"raw_events":50,
         "initial_orthogonal_closure_events":82,
         "initial_failed_pair_hex":[hex(x),hex(y)],
         "initial_admissible_interval_hex":[hex(lower),hex(upper)],
         "all_four_initial_trace_closures":initial_trace_closures,
         "dependency":{"file":os.path.basename(source_path),"sha256":source_hash},
         "branches":[
             audit_branch("middle-maximal",(0x53f,0x3f,0xf)),
             audit_branch("maximal-maximal",(0x153f,0x2a3f,0x5f,0xf))],
         "scope":"two explicit iterated branches only; no all-branch no-go or arbitrary-grid claim"}
    raw=json.dumps(out,sort_keys=True,separators=(",",":"))
    out["payload_sha256"]=hashlib.sha256(raw.encode()).hexdigest()
    return out

if __name__=="__main__":
    generated=payload()
    if "--emit" in sys.argv:
        with open(RECEIPT,"w") as f:
            json.dump(generated,f,sort_keys=True,indent=2)
            f.write("\n")
    elif "--verify" in sys.argv:
        with open(RECEIPT) as f:
            stored=json.load(f)
        assert stored==generated
        print(json.dumps({"status":"PASS","payload_sha256":generated["payload_sha256"]},
                         sort_keys=True))
    else:
        print(json.dumps(generated,sort_keys=True,indent=2))
