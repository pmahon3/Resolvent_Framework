# Test on a finite grid: is every D3 set a disjoint union of window events and antipodal cube pairs
# K(S)=S0xS1xS2 ⊔ S0^c x S1^c x S2^c ?  Also verify K(S) satisfies Box and is in D3.
import sys, itertools, numpy as np
n=tuple(int(a) for a in sys.argv[1:4])
pts=list(itertools.product(*[range(k) for k in n])); idx={p:i for i,p in enumerate(pts)}; N=len(pts); FULL=(1<<N)-1
def mask(pred): return sum(1<<idx[p] for p in pts if pred(p))
def win(w):
    i,j=w; vals=list(itertools.product(range(n[i]),range(n[j]))); out=set()
    for m in range(1<<len(vals)):
        S={vals[k] for k in range(len(vals)) if m>>k&1}
        out.add(mask(lambda p:(p[i],p[j]) in S))
    return out
def Uclose(X):
    S=set(X); fr=set(X)
    while fr:
        D=np.array(sorted(S),dtype=np.uint64); new=set()
        for x in fr:
            ys=D[(D & np.uint64(x))==0]
            for u in (ys|np.uint64(x)).tolist():
                if u not in S: new.add(u)
        S|=new; fr=new
    return S
W=win((0,1))|win((1,2))|win((2,0))
def subsets(k): return [frozenset(c for c in range(k) if m>>c&1) for m in range(1<<k)]
Ks=set()
for S0 in subsets(n[0]):
 for S1 in subsets(n[1]):
  for S2 in subsets(n[2]):
    Ks.add(mask(lambda p:(p[0] in S0 and p[1] in S1 and p[2] in S2) or (p[0] not in S0 and p[1] not in S1 and p[2] not in S2)))
R0=Uclose(W); R1=Uclose(R0|{m^FULL for m in R0}); D=Uclose(R1|{m^FULL for m in R1})
print('|D|',len(D),'all K in D:',Ks<=D, 'all K in R1:', Ks<=R1)
Q=Uclose(W|Ks)
print('|Q|=|closure of windows+K under disjoint union|',len(Q),' Q==D:',Q==D, ' Q closed under complement:', all((m^FULL) in Q for m in Q))
