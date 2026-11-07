# Gate P-stack: is E3 = E*∩[3]^3 in the Dynkin closure D3 of a grid with one spare value on one coordinate?
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
D=Uclose(win((0,1))|win((1,2))|win((2,0))); r=0
while True:
    r+=1; D2=Uclose(D|{m^FULL for m in D})
    if D2==D: break
    D=D2
E3=mask(lambda p:max(p)<3 and ((p[0]<=p[1])+(p[1]<p[2])+(p[2]<p[0]))==2)
print(n,'|D3|',len(D),'rounds',r,'E3 points',bin(E3).count('1'),'E3 in D3:',E3 in D, flush=True)
