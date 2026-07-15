#!/usr/bin/env python3
"""Activation escape of every first-PJH-defect join normal form.

Computes profile/activation fibre counts directly from the 224 single-cell
state table, without constructing the 6,186,568-point bitsets, then checks
the 33 nonlower atlas occurrences.  This certifies only that the defect join
itself cannot be activation-supported; derived terminal cuts remain open.
"""
import argparse, collections, hashlib, itertools, json, os, sys

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell

SCHEMA="full-grid-pjh-defect-activation-escape-v1"

def ar(s):return tuple(int(a in s) for a in cell.SHARED)
def qr(s):return (int("e11" in s or "e10" in s),
                  int("e11" in s or "e01" in s))

def payload():
    states=cell.cell_states();groups=collections.Counter((ar(s),*qr(s)) for s in states)
    assert len(states)==224
    counts={p:{"total":0,"row0_activated":0,"row1_activated":0,
               "both_activated":0} for p in itertools.product((0,1),repeat=4)}
    macro_count=0;carrier=0
    for a0,a1,q0,q1,r0,r1 in itertools.product(
            itertools.product((0,1),repeat=3),itertools.product((0,1),repeat=3),
            (0,1),(0,1),(0,1),(0,1)):
        ns=(groups[(a0,q0,r0)],groups[(a0,q0,r1)],
            groups[(a1,q1,r0)],groups[(a1,q1,r1)])
        size=ns[0]*ns[1]*ns[2]*ns[3]
        if not size:continue
        macro_count+=1;carrier+=size;p=(q0,q1,r0,r1);c=counts[p];c["total"]+=size
        if a0==(1,1,1):c["row0_activated"]+=size
        if a1==(1,1,1):c["row1_activated"]+=size
        if a0==a1==(1,1,1):c["both_activated"]+=size
    assert carrier==6186568
    rows=[]
    for p,c in sorted(counts.items()):
        c=dict(c);c["off_row0_activation"]=c["total"]-c["row0_activated"]
        c["off_row1_activation"]=c["total"]-c["row1_activated"]
        assert c["off_row0_activation"]>0 and c["off_row1_activation"]>0
        rows.append({"profile":list(p),**c})
    both={tuple(r["profile"]):r["both_activated"] for r in rows if r["both_activated"]}
    assert set(both)=={(0,0,0,0),(1,1,1,1)}

    atlas=json.load(open(os.path.join(HERE,"full_grid_core16_pjh_defect_atlas.json")))
    defects=[]
    for r in atlas["records"]:
        lo=int(r["failed_lower_hex"],16)
        for e in r["edges"]:
            if not e["can_be_first_pjh_defect"]:continue
            h=int(e["candidate_hull_hex"],16)
            low_profiles=[i for i in range(16) if lo>>i&1]
            entered=[i for i in range(16) if (h&~lo)>>i&1]
            assert low_profiles
            assert all(rows[i]["off_row0_activation"]>0 and
                       rows[i]["off_row1_activation"]>0 for i in low_profiles)
            defects.append({"node_id":r["node_id"],"depth":r["depth"],
                "lower_hex":hex(lo),"hull_hex":hex(h),
                "full_lower_profiles":low_profiles,"entered_profiles":entered,
                "defect_join_contains_off_row0_point":True,
                "defect_join_contains_off_row1_point":True})
    assert len(defects)==33 and min(len(x["full_lower_profiles"]) for x in defects)==3
    out={"schema":SCHEMA,"schema_version":"1.0","single_cell_states":len(states),
      "macrofibres":macro_count,"carrier_points":carrier,"profile_rows":rows,
      "all_16_profiles_have_off_row0_and_off_row1_points":True,
      "both_activated_profiles":[list(p) for p in sorted(both)],
      "possible_first_defect_occurrences":len(defects),
      "minimum_full_lower_profiles":min(len(x["full_lower_profiles"]) for x in defects),
      "every_defect_join_itself_avoids_gate_B_for_both_rows":True,
      "defects":defects,
      "scope":"33 lex-atlas first-defect normal forms; join itself only, not derived cuts or terminal realizability",
      "atlas_payload_sha256":atlas["payload_sha256"],
      "command":"python3 notes/open_questions/verification/full_grid_pjh_defect_activation_escape.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"full_grid_pjh_defect_activation_escape.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
      "defects":out["possible_first_defect_occurrences"],"profiles":len(out["profile_rows"])},sort_keys=True,indent=2))
if __name__=="__main__":main()
