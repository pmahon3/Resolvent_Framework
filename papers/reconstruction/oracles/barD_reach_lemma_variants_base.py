import sys, random
from collections import deque
exec(open(__file__.replace('barD_reach_lemma_variants_base.py','barD_reach_lemma_strategy.py')).read().split("def run(")[0])
def land(m,o,C,out):
    c=len(C); pos={v:i for i,v in enumerate(C)}; p0=pos[m]
    start=(o,0); seen={start}; dq=deque([start])
    while dq:
        w,t=dq.popleft()
        for w2 in out[w]:
            t2=(t+1)%c
            if w2==C[(p0+t2)%c]: continue
            if w2 in pos: return True
            s=(w2,t2)
            if s not in seen: seen.add(s); dq.append(s)
    return False
def variants(rel,A,st):
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    cyc=[C for C in simple_cycles(rel,A) if len(C)>=2]
    for x in range(A):
        for y in range(A):
            if x==y: continue
            st['pairs']+=1
            thru=[C for C in cyc if x in C]
            anyC=any(land(x,y,C,out) for C in thru)
            st['fixed_role_anyC_fail']+= not anyC
            sh=min(thru,key=len)
            st['fixed_role_shortestC_fail']+= not land(x,y,sh,out)
            st['every_C_through_x_fail']+= not all(land(x,y,C,out) for C in thru)
import itertools
for A in (3,4):
    allp=[(a,b) for a in range(A) for b in range(A)]
    st=dict(pairs=0,fixed_role_anyC_fail=0,fixed_role_shortestC_fail=0,every_C_through_x_fail=0)
    for mask in range(1<<len(allp)):
        rel=frozenset(p for i,p in enumerate(allp) if mask>>i&1)
        if primitive(rel,A): variants(rel,A,st)
    print('A',A,st)
random.seed(9)
for A in (5,6,7):
    allp=[(a,b) for a in range(A) for b in range(A)]
    st=dict(pairs=0,fixed_role_anyC_fail=0,fixed_role_shortestC_fail=0,every_C_through_x_fail=0); k=0
    while k<800:
        rel=frozenset(x for x in allp if random.random()<random.choice((1.3,1.7,2.5))/A)
        if not primitive(rel,A): continue
        k+=1; variants(rel,A,st)
    print('A',A,'sample',st)
