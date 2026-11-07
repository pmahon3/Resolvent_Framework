# Alternation rank: R0 = window events; U(X) = closure of X under finite disjoint unions;
# R_{k+1} = U(R_k ∪ complements(R_k)). Report |R_k| until stable; compare with |B|.
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
R=Uclose(win((0,1))|win((1,2))|win((2,0)))
k=0; print('R0',len(R),flush=True)
while True:
    R2=Uclose(R|{m^FULL for m in R}); k+=1
    print('R%d'%k,len(R2),flush=True)
    if len(R2)==len(R): break
    R=R2
# B count: values on points with some coordinate 0 are free; rest determined by box with base 0
free=[p for p in pts if 0 in p]; det=[p for p in pts if 0 not in p]
cnt=0
for m in range(1<<len(free)):
    v={p:(m>>i)&1 for i,p in enumerate(free)}
    ok=True
    for p in det:
        x0,x1,x2=p
        val=v[(x0,x1,0)]+v[(0,x1,x2)]+v[(x0,0,x2)]-v[(x0,0,0)]-v[(0,x1,0)]-v[(0,0,x2)]+v[(0,0,0)]
        if val not in (0,1): ok=False;break
    cnt+=ok
print('|B|',cnt)
