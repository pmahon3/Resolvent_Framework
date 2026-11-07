# Compute D3(K) (Dynkin closure of window events) on a finite grid K=n0 x n1 x n2,
# record the first level at which each set appears, compare with B (box-identity 0/1 sets).
import sys, itertools, numpy as np
n=tuple(int(a) for a in sys.argv[1:4])
pts=list(itertools.product(range(n[0]),range(n[1]),range(n[2])))
idx={p:i for i,p in enumerate(pts)}; N=len(pts); FULL=(1<<N)-1
def win(w):
    i,j=w; vals=list(itertools.product(range(n[i]),range(n[j])))
    out=set()
    for m in range(1<<len(vals)):
        S={vals[k] for k in range(len(vals)) if m>>k&1}
        out.add(sum(1<<idx[p] for p in pts if (p[i],p[j]) in S))
    return out
G=win((0,1))|win((1,2))|win((2,0))
def box_ok(m):
    f=lambda p:(m>>idx[p])&1
    for a,a2 in itertools.combinations(range(n[0]),2):
     for b,b2 in itertools.combinations(range(n[1]),2):
      for c,c2 in itertools.combinations(range(n[2]),2):
        if f((a,b,c))+f((a2,b2,c))+f((a2,b,c2))+f((a,b2,c2))!=f((a2,b,c))+f((a,b2,c))+f((a,b,c2))+f((a2,b2,c2)): return False
    return True
level={m:0 for m in G}
cur=set(G); k=0
while True:
    k+=1
    D=np.array(sorted(level),dtype=np.uint64)
    new=set()
    for m in D:
        c=int(m)^FULL
        if c not in level: new.add(c)
    # disjoint unions with at least one member from the previous frontier
    fr=np.array(sorted(cur),dtype=np.uint64)
    for x in fr:
        ys=D[(D & x)==0]
        for u in (ys|x).tolist():
            if u not in level: new.add(u)
    if not new: break
    for m in new: level[m]=k
    cur=new
    print('level',k,'new',len(new),'total',len(level),flush=True)
print('|D|=',len(level))
bad=[m for m in level if not box_ok(m)]
print('D sets failing box:',len(bad))
from collections import Counter
print('level histogram',sorted(Counter(level.values()).items()))
