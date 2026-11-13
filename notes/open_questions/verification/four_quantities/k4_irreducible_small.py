# Test of the hand explanation (FOUR_QUANTITIES_GATE.md, hand session 2): irreducible K4 pair-sum sets should exist
# ONLY when every coordinate has exactly two values, and there they should all be images of one 16-world pattern C ⊔ K.
import itertools, sys, numpy as np
from fractions import Fraction
def v01(n):
    pts=list(itertools.product(*[range(k) for k in n])); P=np.array(pts); N=len(pts)
    cols=[((P[:,i]==a)&(P[:,j]==b)).astype(int) for i,j in itertools.combinations(range(4),2) for a in range(n[i]) for b in range(n[j])]
    M=[[Fraction(int(x)) for x in c] for c in cols]; r=0
    for c in range(N):
        k=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        r+=1
    B=np.array([[float(x) for x in row] for row in M[:r]]); out=[]
    for s in range(0,1<<r,1<<18):
        c=np.arange(s,min(s+(1<<18),1<<r)); v=((c[:,None]>>np.arange(r))&1).astype(np.float64)@B
        ok=(np.abs(v-np.rint(v))<1e-6).all(1)&(v>-0.5).all(1)&(v<1.5).all(1); out.append(np.rint(v[ok]).astype(np.int8))
    return np.unique(np.concatenate(out),axis=0).reshape((-1,)+tuple(n))
def irreducible(S):
    m=len(S); red=np.zeros(m,bool)
    for ax in range(1,5):
        for a,b in itertools.combinations(range(S.shape[ax]),2):
            d=np.take(S,a,axis=ax)-np.take(S,b,axis=ax)
            for keep in range(1,4):
                ref=d
                for k in (1,2,3):
                    if k!=keep: ref=np.take(ref,[0],axis=k)
                red|=(d==ref).reshape(m,-1).all(1)
    return S[~red]
for n in [(2,2,2,2),(2,2,2,3),(2,2,3,3),(2,3,3,3)]:
    S=v01(n); I=irreducible(S); print(n,'|V01|',len(S),'irreducible',len(I),flush=True)
    if n==(2,2,2,2):
        I2=I
# the predicted pattern: C = {(u,v,t) in {011,100}} (any p)  ⊔  K = {(p,u,v) in {000,111}} (any t); coordinates (p,u,v,t)
pat=np.zeros((2,2,2,2),np.int8)
for p,u,v,t in itertools.product(range(2),repeat=4):
    if (u,v,t) in [(0,1,1),(1,0,0)] or (p,u,v) in [(0,0,0),(1,1,1)]: pat[p,u,v,t]=1
orbit=set()
for perm in itertools.permutations(range(4)):
    q=np.transpose(pat,perm)
    for flips in itertools.product([0,1],repeat=4):
        r=q
        for ax,f in enumerate(flips):
            if f: r=np.flip(r,axis=ax)
        orbit.add(r.tobytes()); orbit.add((1-r).tobytes())
irr2={x.tobytes() for x in I2}
print('pattern has',int(pat.sum()),'worlds; its images under relabelling, reordering and complement:',len(orbit),'| equals the irreducible sets on 2x2x2x2:',orbit==irr2)
