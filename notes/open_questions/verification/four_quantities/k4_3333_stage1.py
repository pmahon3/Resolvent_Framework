# gate.four_quantities_3333, stage 1: enumerate V01 on 3x3x3x3 by slices, count reducible sets, save irreducible ones.
import itertools, time, numpy as np
from fractions import Fraction
t0=time.time(); n=3
pts=list(itertools.product(range(n),repeat=3)); P=np.array(pts)
# --- triangle pair-sum sets on 3^3 (should be 15,914): information-set enumeration, exact reduced basis
cols=[((P[:,i]==a)&(P[:,j]==b)).astype(int) for (i,j) in [(0,1),(1,2),(0,2)] for a in range(n) for b in range(n)]
M=[[Fraction(int(x)) for x in c] for c in cols]; piv=[]; r=0
for c in range(27):
    k=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
    if k is None: continue
    M[r],M[k]=M[k],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
    for i in range(len(M)):
        if i!=r and M[i][c]!=0:
            f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
    piv.append(c); r+=1
B=np.array([[float(x) for x in row] for row in M[:r]])
c=np.arange(1<<r); v=((c[:,None]>>np.arange(r))&1).astype(np.float64)@B
ok=(np.abs(v-np.rint(v))<1e-6).all(1)&(v>-0.5).all(1)&(v<1.5).all(1)
T=np.unique(np.rint(v[ok]).astype(np.int8),axis=0); print('triangle 3^3 pair-sum sets:',len(T),flush=True)
# --- slice differences d = h0(x0)+h1(x1)+h2(x2) with values in {-1,0,1}
ds=set()
for g in itertools.product(itertools.product(range(3),repeat=3),repeat=3):      # g_j : X_j -> {0,1,2}
    if any(min(gj)!=0 for gj in g) or sum(max(gj) for gj in g)>2: continue
    base=np.array([g[0][p[0]]+g[1][p[1]]+g[2][p[2]] for p in pts])
    for cst in (-1,0,1):
        d=base+cst
        if d.min()>=-1 and d.max()<=1: ds.add(tuple(d.tolist()))
ds=np.array(sorted(ds),dtype=np.int8); print('slice differences:',len(ds),flush=True)
# --- for each triangle set F0, the admissible other slices F0+d
Tb=T.astype(bool); lists=[[] for _ in range(len(T))]
for d in ds:
    Fn=T+d; good=((Fn>=0)&(Fn<=1)).all(1)
    for i in np.nonzero(good)[0]: lists[i].append(Fn[i])
cnt=np.array([len(l) for l in lists]); Mtot=int((cnt**2).sum())
print('admissible second slices per F0: min %d mean %.1f max %d'%(cnt.min(),cnt.mean(),cnt.max()),'| |V01| =',Mtot,'time %.0fs'%(time.time()-t0),flush=True)
# --- reducibility test on arrays S of shape (m,3,3,3,3) [axes: x3,x0,x1,x2]
def reducible(S):
    S=S.astype(np.int8); red=np.zeros(len(S),bool)
    for ax in range(1,5):
        for a,b in itertools.combinations(range(3),2):
            diff=np.take(S,a,axis=ax)-np.take(S,b,axis=ax)          # (m,3,3,3)
            for keep in range(1,4):                                  # depends only on axis `keep` (or on none)
                others=[k for k in (1,2,3) if k!=keep]; ref=diff
                for k in others: ref=np.take(ref,[0],axis=k)
                red|=(diff==ref).reshape(len(S),-1).all(1)
    return red
irr=[]; nred=0; buf=[]; 
def flush():
    global nred,buf
    if not buf: return
    S=np.array(buf,dtype=np.int8).reshape(-1,3,3,3,3); red=reducible(S); nred+=int(red.sum()); irr.extend(S[~red]); buf=[]
for i,l in enumerate(lists):
    F0=T[i]
    for F1 in l:
        for F2 in l:
            buf.append(np.concatenate([F0,F1,F2]))
    if len(buf)>200000: flush()
flush()
irr=np.array(irr,dtype=np.int8); np.save('k4_3333_irreducible.npy',irr)
print('RESULT |V01| =',Mtot,'reducible',nred,'irreducible',len(irr),'time %.0fs'%(time.time()-t0))
