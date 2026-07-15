#!/usr/bin/env python3
"""Classify the same-carrier enlargement interval above the stage-558 fattened meet."""
import argparse, collections, hashlib, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_stage558_splitter_incidence as stage
import full_grid_third_gap_classification as factor

SCHEMA="full-grid-stage558-fattened-meet-gap-v1"
MEET_SHA="50ca1d1b7ed5e5d8cc5f04ec6772c8bdb8f3be6f9629a2a9da6a5edfc88cc83c"

def payload():
    n,full,masks,macro,events,joins=stage.build_stage3()
    matches=[e for e in events if stage.sha(e,n)==MEET_SHA]
    assert len(matches)==1
    meet=matches[0]
    q0=masks[((0,0),"e11")]|masks[((0,0),"e10")]
    q1=masks[((1,0),"e11")]|masks[((1,0),"e10")]
    # De Morgan audit of the current lattice meet: q0 and q1^c have exactly
    # two upper bounds, one proper, and meet is the proper bound's complement.
    ubs=[u for u in events if q0&u==q0 and (full^q1)&u==(full^q1)]
    proper=[u for u in ubs if u!=full]
    assert len(ubs)==2 and len(proper)==1 and meet==(full^proper[0])
    cylinder=0;offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if (q0,q1)==(0,1):cylinder|=((1<<size)-1)<<offset
        offset+=size
    gap=cylinder&~meet
    rows=[];offset=0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        seg=(gap>>offset)&((1<<size)-1)
        if seg:
            projs,cart=factor.factor_projection(seg,ns)
            rows.append({"row0_activation":list(a0),"row1_activation":list(a1),
                "profile":[q0,q1,r0,r1],"ambient_factor_sizes":list(ns),
                "points":seg.bit_count(),"macrofibre_points":size,
                "selected_factor_sizes":[len(x) for x in projs],
                "cartesian":cart,"whole_macrofibre":seg.bit_count()==size})
        offset+=size
    profiles=collections.Counter(tuple(r["profile"]) for r in rows)
    acts=collections.Counter((tuple(r["row0_activation"]),tuple(r["row1_activation"])) for r in rows)
    act_classes=collections.Counter()
    for r in rows:
        a=tuple(r["row0_activation"])==(1,1,1)
        b=tuple(r["row1_activation"])==(1,1,1)
        act_classes["both" if a and b else "row0_only" if a else "row1_only" if b else "neither"]+=1
    assert meet.bit_count()==336404 and cylinder.bit_count()==1355680
    assert gap.bit_count()==1019276 and len(rows)==160
    assert all(r["cartesian"] and r["whole_macrofibre"] for r in rows)
    assert profiles=={(0,1,0,0):55,(0,1,1,0):49,(0,1,1,1):56}
    assert act_classes["row0_only"]==6 and act_classes["row1_only"]==7
    assert act_classes["neither"]==147 and act_classes["both"]==0
    decomp=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    out={"schema":SCHEMA,"schema_version":"1.0","carrier_points":n,
        "stage_events":len(events),"meet_sha256":MEET_SHA,"meet_points":meet.bit_count(),
        "literal_cylinder_points":cylinder.bit_count(),"enlargement_gap_points":gap.bit_count(),
        "enlargement_gap_sha256":stage.sha(gap,n),"macrofibres":len(rows),
        "whole_macrofibres":sum(r["whole_macrofibre"] for r in rows),
        "proper_macrofibres":sum(not r["whole_macrofibre"] for r in rows),
        "minimum_macrofibre_points":min(r["points"] for r in rows),
        "profile_counts":[{"profile":list(k),"macrofibres":v} for k,v in sorted(profiles.items())],
        "activation_pair_counts":[{"row0":list(k[0]),"row1":list(k[1]),"macrofibres":v} for k,v in sorted(acts.items())],
        "activation_class_macrofibres":{k:act_classes[k] for k in ("both","neither","row0_only","row1_only")},
        "decomposition_sha256":decomp,"rows":rows,
        "macro_saturated_candidate_count":"2^160",
        "macro_saturated_gate_B_nonzero_remainders":(2**6-1)+(2**7-1),
        "macro_saturated_gate_A_or_B_candidates":(2**6-1)+(2**7-1)+1,
        "macro_saturated_avoiding_A_and_B_including_unchanged_meet":str(2**160-191),
        "macro_saturated_proper_enlargements_avoiding_A_and_B":str(2**160-192),
        "unrestricted_set_candidate_count":"2^1019276",
        "meet_identity_verified":"q0^c meet q1 via complement of unique proper upper bound of q0 and q1^c",
        "scope":"one exact stage-558 meet enlargement interval; macrofibre decomposition only; no claim that terminal meets remain macrofibre-saturated",
        "command":"python3 notes/open_questions/verification/full_grid_stage558_fattened_meet_gap.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_stage558_fattened_meet_gap.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],"macrofibres":out["macrofibres"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
