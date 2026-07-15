#!/usr/bin/env python3
"""Audit that one four-coordinate profile atom does not reconstruct a side."""
import argparse, hashlib, json, os
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = "core16-single-profile-noncollapse-v1"
PROFILES = tuple(product((0,1), repeat=4))
TRIVIAL = {0,0xffff,0x00ff,0xff00,0x0f0f,0xf0f0,
           0x3333,0xcccc,0x5555,0xaaaa}

def closure(seed):
    ev=set(seed)
    while True:
        new={0xffff^x for x in ev}
        snap=sorted(ev)
        for i,x in enumerate(snap):
            for y in snap[i:]:
                if not x&y:new.add(x|y)
        old=len(ev);ev|=new
        if len(ev)==old:return ev

def side(w):
    if w in TRIVIAL:return None
    n=[(w>>(4*k))&15 for k in range(4)]
    if all(x in (0,15) for x in n):return "q"
    if n[0]==n[1]==n[2]==n[3]:return "r"
    return None

def payload():
    raw=set()
    for a,b in ((0,2),(0,3),(1,2),(1,3)):
        atoms=[]
        for x,y in product((0,1),repeat=2):
            w=sum(1<<i for i,p in enumerate(PROFILES)
                  if p[a]==x and p[b]==y)
            atoms.append(w)
        for mask in range(16):
            raw.add(sum(atoms[k] for k in range(4) if mask>>k&1))
    base=closure(raw);assert len(base)==82
    rows=[]
    for i,p in enumerate(PROFILES):
        cl=closure(base|{1<<i})
        ss=sorted(w for w in cl if side(w))
        assert len(cl)==204 and not ss
        rows.append({"profile":list(p),"closure_words":len(cl),
            "same_side_words":0,
            "closure_sha256":hashlib.sha256(
                b"".join(w.to_bytes(2,"little") for w in sorted(cl))).hexdigest()})
    out={"schema":SCHEMA,"schema_version":"1.0","base_words":82,
         "profiles_tested":16,"all_singleton_closures_words":204,
         "all_same_side_words":0,"rows":rows,
         "scope":"all 16 singleton profile additions to the stripped K22 edge-word core; no full-carrier or multi-repair promotion",
         "command":"python3 notes/open_questions/verification/core16_single_profile_noncollapse.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args()
    out=payload();path=os.path.join(HERE,"core16_single_profile_noncollapse.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    elif a.verify or os.path.exists(path):assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"]},sort_keys=True,indent=2))
if __name__=="__main__":main()
