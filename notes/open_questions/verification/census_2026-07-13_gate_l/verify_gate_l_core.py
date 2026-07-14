#!/usr/bin/env python3
"""Independent verifier for the minimal three-type Gate-L obstruction."""
import json
from pathlib import Path

C=('g','h','W','Vi','Vj','R'); n=3; full=(1<<18)-1
def sec(c,names): return sum(1<<(6*c+C.index(x)) for x in names)
types=(1,2,3); sig=[0,0,0]; gs={(1,2):0,(1,3):0,(2,3):0}
for c,k in enumerate(types):
    i,j=sorted({1,2,3}-{k}); tr={k:('g','h'),i:('g','W','Vi'),j:('h','W','Vj')}
    for m in (1,2,3): sig[m-1] |= sec(c,tr[m])
    for pair in gs:
        if k in pair:
            other=next(x for x in pair if x!=k)
            gs[pair] |= sec(c,('g',) if other==i else ('h',))
cyl=[sum(63<<(6*c) for c in range(3) if a>>c&1) for a in range(8)]
Q=set(cyl+sig+list(gs.values())+[0,full])
while True:
    old=len(Q); Q |= {full^x for x in Q}; items=list(Q)
    Q |= {x|y for p,x in enumerate(items) for y in items[p+1:] if not x&y}
    if len(Q)==old: break
assert len(Q)==88
A=cyl[1]; G=gs[(1,2)]; U=cyl[3]
V=next(x for x in Q if tuple(x>>(6*c)&63 for c in range(3)) == (63,49,49))
subset=lambda x,y: not x & ~y
assert subset(A,U) and subset(G,U) and subset(A,V) and subset(G,V)
between=[x for x in Q if not (A|G)&~x and not x&~(U&V)]
assert between == []
cert=json.loads(Path(__file__).with_name('gate_l_core_certificate.json').read_text())
assert cert['runs'][0]['core_count']==88 and cert['runs'][0]['join_failures']>0
print('PASS: independently rebuilt Q and verified two upper bounds with no Q-profile between')
