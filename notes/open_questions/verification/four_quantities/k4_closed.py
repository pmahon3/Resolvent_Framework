# gate.four_quantities_closed (pre-registered in views_across_records/FOUR_QUANTITIES_GATE.md, 2026-11-13).
# Window graph given by EDGES on coordinates with sizes n. Compare D (closure of pair events under complement and
# disjoint union) with V01 (0/1 vectors in the span of the pair indicators).  Usage: python3 k4_closed.py 2 2 2 3 [graph]
import sys, itertools, time, numpy as np
n=tuple(int(a) for a in sys.argv[1:5]); graph=sys.argv[5] if len(sys.argv)>5 else 'K4'
EDGES={'K4':[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],'square':[(0,1),(1,2),(2,3),(3,0)],'diamond':[(0,1),(1,2),(2,3),(3,0),(0,2)]}[graph]
pts=list(itertools.product(*[range(k) for k in n])); N=len(pts); assert N<=62
P=np.array(pts); w=(np.uint64(1)<<np.arange(N,dtype=np.uint64)); FULL=np.uint64((1<<N)-1)
t0=time.time()
# ---- V01 by an information set: a span vector is determined by its values on r pivot points
cols=[((P[:,i]==a)&(P[:,j]==b)).astype(float) for (i,j) in EDGES for a in range(n[i]) for b in range(n[j])]
A=np.array(cols).T
from fractions import Fraction
def rref_pivots(M):
    M=[[Fraction(int(x)) for x in row] for row in M.T.tolist()]   # rows = generators
    piv=[]; r=0
    for c in range(N):
        k=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    return piv, np.array([[float(x) for x in row] for row in M[:r]])   # reduced basis: basis[k][piv[k]]=1
piv,B=rref_pivots(A); r=len(piv)
print(graph,n,'points',N,'span dimension',r,flush=True)
V=[]; chunk=1<<20
for s in range(0,1<<r,chunk):
    c=np.arange(s,min(s+chunk,1<<r),dtype=np.int64)
    coef=((c[:,None]>>np.arange(r))&1).astype(np.float32)
    v=coef@B.astype(np.float32)
    ok=(np.abs(v-np.rint(v))<1e-3).all(axis=1)&(v>-0.5).all(axis=1)&(v<1.5).all(axis=1)
    if ok.any(): V.append((np.rint(v[ok]).astype(np.uint64)*w).sum(axis=1))
V=np.unique(np.concatenate(V)); print('|V01|',len(V),'time %.0fs'%(time.time()-t0),flush=True)
# ---- D by closure (frontier against everything), stopping early if it reaches |V01|
gens=set()
for (i,j) in EDGES:
    cells=[((P[:,i]==a)&(P[:,j]==b)) for a in range(n[i]) for b in range(n[j])]
    for m in range(1<<len(cells)):
        acc=np.zeros(N,bool)
        for k in range(len(cells)):
            if m>>k&1: acc|=cells[k]
        gens.add(int((acc.astype(np.uint64)*w).sum()))
D=set(gens); fr=set(gens); Vset=set(V.tolist()); assert D<=Vset
rnd=0
while fr and len(D)<len(Vset):
    rnd+=1; Darr=np.fromiter(D,dtype=np.uint64,count=len(D)); new=set()
    for x in fr:
        c=int(FULL)^x
        if c not in D: new.add(c)
    for x in fr:
        ux=np.uint64(x); ys=Darr[(Darr&ux)==0]
        if len(ys): new.update((ys|ux).tolist())
    new-=D; D|=new; fr=new
    print(' round',rnd,'new',len(new),'|D|',len(D),'time %.0fs'%(time.time()-t0),flush=True)
print('RESULT',graph,n,'|D|',len(D),'|V01|',len(Vset),'gap',len(Vset)-len(D),'D subset of V01:',D<=Vset)
if len(Vset)>len(D):
    g=sorted(Vset-D,key=lambda m:bin(m).count('1'))[:3]
    for m in g: print(' gap set (%d points):'%bin(m).count('1'),' '.join(''.join(map(str,p)) for k,p in enumerate(pts) if m>>k&1))
