# Control for gate P-stack: which 3x3x3 carrier sets remain carrier sets on 3x3x4 (spare value x2=3)?
import itertools, numpy as np
from collections import Counter
def closure(n):
    pts=list(itertools.product(*[range(k) for k in n])); idx={p:i for i,p in enumerate(pts)}; N=len(pts); FULL=(1<<N)-1
    def mask(pred): return sum(1<<idx[p] for p in pts if pred(p))
    def win(w):
        i,j=w; vals=list(itertools.product(range(n[i]),range(n[j]))); out=set()
        for m in range(1<<len(vals)):
            S={vals[k] for k in range(len(vals)) if m>>k&1}; out.add(mask(lambda p:(p[i],p[j]) in S))
        return out
    def U(X):
        S=set(X); fr=set(X)
        while fr:
            D=np.array(sorted(S),dtype=np.uint64); new=set()
            for x in fr:
                for u in (D[(D & np.uint64(x))==0]|np.uint64(x)).tolist():
                    if u not in S: new.add(u)
            S|=new; fr=new
        return S
    D=U(win((0,1))|win((1,2))|win((2,0)))
    while True:
        D2=U(D|{m^FULL for m in D})
        if D2==D: break
        D=D2
    return pts,D
p3,D3=closure((3,3,3)); p4,D4=closure((3,3,4))
toset=lambda m,pts: frozenset(p for k,p in enumerate(pts) if m>>k&1)
S3={toset(m,p3) for m in D3}
S4avoid={toset(m,p4) for m in D4 if not any(p[2]==3 for p in toset(m,p4))}
print('3^3 carrier sets:',len(S3),'| 3x3x4 carrier sets avoiding x2=3:',len(S4avoid),'| subset:',S4avoid<=S3)
lost=S3-S4avoid; print('lost:',len(lost),'sizes',sorted(Counter(len(s) for s in lost).items()))
E3=frozenset(p for p in p3 if ((p[0]<=p[1])+(p[1]<p[2])+(p[2]<p[0]))==2); print('E3 lost:',E3 in lost)
