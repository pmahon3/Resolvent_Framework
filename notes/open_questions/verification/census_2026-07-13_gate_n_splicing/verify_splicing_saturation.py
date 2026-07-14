#!/usr/bin/env python3
"""Independent semantic verifier: rebuilds cores without producer imports."""
import json
from pathlib import Path

CELLS=("g","h","W","Vi","Vj","R")
def cores(n):
    ts=tuple(1+i%3 for i in range(n)); full=(1<<(6*n))-1
    def sec(c,names): return sum(1<<(6*c+CELLS.index(a)) for a in names)
    sig=[0,0,0]; gs={(1,2):0,(1,3):0,(2,3):0}
    for c,k in enumerate(ts):
        i,j=sorted({1,2,3}-{k}); tr={k:("g","h"),i:("g","W","Vi"),j:("h","W","Vj")}
        for m in (1,2,3): sig[m-1]|=sec(c,tr[m])
        for p in gs:
            if k in p:
                o=next(a for a in p if a!=k); gs[p]|=sec(c,("g",) if o==i else ("h",))
    cylinders=[sum(63<<(6*c) for c in range(n) if a>>c&1) for a in range(1<<n)]
    S=set(cylinders+sig+list(gs.values())+[0,full])
    while True:
        old=len(S); items=tuple(S); S.update(full^x for x in items); items=tuple(S)
        S.update(x|y for x in items for y in items if not x&y)
        if len(S)==old: return ts,full,sorted(S)

def verify(run):
    n=run["n_columns"]; ts,full,S=cores(n); masks=[63<<(6*c) for c in range(n)]
    good=bad=0; first=None
    for e in range(1<<n):
        erased=[k for k in (1,2,3) if all(e>>c&1 for c,t in enumerate(ts) if t==k)]
        out=full^sum(masks[c] for c in range(n) if e>>c&1); proj={z&out for z in S}
        for x in S:
            for y in S:
                if x&y&out: continue
                if erased: bad+=1
                else: good+=1
                if (x|y)&out not in proj and not erased: raise AssertionError((n,e,x,y))
                if (x|y)&out not in proj and first is None: first=True
    assert len(S)==run["core_count"]
    assert good==run["type_surviving_admissible_pairs_checked"]
    assert bad==run["type_erasing_admissible_pairs_checked"]
    assert bool(run["first_type_erasing_failure"])==bool(first)

cert=json.loads(Path(__file__).with_name("splicing_saturation_certificate.json").read_text())
for r in cert["runs"]: verify(r)
print("PASS: independently rebuilt all cores and reproduced saturation counts")
