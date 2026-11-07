import itertools, numpy as np
n=(3,3,3)
pts=list(itertools.product(range(3),repeat=3)); idx={p:i for i,p in enumerate(pts)}; N=27; FULL=(1<<N)-1
def win(w):
    i,j=w; vals=list(itertools.product(range(n[i]),range(n[j]))); out=set()
    for m in range(1<<9):
        S={vals[k] for k in range(9) if m>>k&1}
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
R0=Uclose(win((0,1))|win((1,2))|win((2,0)))
R1=Uclose(R0|{m^FULL for m in R0})
R2=Uclose(R1|{m^FULL for m in R1})
top=sorted(R2-R1)
def show(m): return sorted(p for p in pts if m>>idx[p]&1)
cyc=sum(1<<idx[p] for p in pts if len(set(p))==3 and (p[0]<p[1]<p[2] or p[1]<p[2]<p[0] or p[2]<p[0]<p[1]))
estar=sum(1<<idx[p] for p in pts if (p[0]<=p[1])+(p[1]<p[2])+(p[2]<p[0])==2)
print('E* rank2-only?', estar in R2 and estar not in R1, 'E* in R1', estar in R1)
for m in top[:3]: print(len(show(m)), show(m))
# sizes histogram
from collections import Counter
print(Counter(bin(m).count('1') for m in top))
