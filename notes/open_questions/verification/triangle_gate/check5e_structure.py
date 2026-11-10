# 2026-11-10 (5DE check).  Evidence (finite grids only, never a proof over N) for the hand argument in
# TRIANGLE_5DE_CHECK.md section C6.
#  (T) Transposition certificate: E*|[n]^3 is reduced to a 1x1x1 grid by adjacent swaps of differently
#      coloured elements of the circular arrangement (each swap adds/removes ONE window line) and merges
#      of adjacent same-colour elements (equal slices = pullback).  Hence E*|[n]^3 in D3([n]^3).
#  (S) Cell structure: for random box sets and random labelled partitions into parts lying inside
#      type classes, the column lemmas hold and three window-event removals leave only
#      one-coordinate products in every cell.
import sys, itertools, random
import numpy as np
random.seed(1)

def cyc_set(arr, sizes):
    # arr: list of (colour, value) in linear order; set of x with exactly two of
    # pos(x0)<pos(x1), pos(x1)<pos(x2), pos(x2)<pos(x0)
    pos={e:i for i,e in enumerate(arr)}
    F=np.zeros(sizes,dtype=bool)
    for x in itertools.product(*[range(s) for s in sizes]):
        p=[pos[(i,x[i])] for i in range(3)]
        F[x]=((p[0]<p[1])+(p[1]<p[2])+(p[2]<p[0]))==2
    return F

def transposition_certificate(n):
    arr=[]
    for v in range(n): arr+= [(0,v),(2,v),(1,v)]     # x0<=x1 , x1<x2 , x2<x0 as position comparisons
    F=cyc_set(arr,(n,n,n))
    E=np.zeros((n,n,n),dtype=bool)
    for x in itertools.product(range(n),repeat=3):
        E[x]=((x[0]<=x[1])+(x[1]<x[2])+(x[2]<x[0]))==2
    assert (F==E).all()
    swaps=0
    # bubble sort by colour; verify each swap toggles exactly one full window line
    changed=True
    while changed:
        changed=False
        for t in range(len(arr)-1):
            (ci,p),(cj,q)=arr[t],arr[t+1]
            if ci>cj:
                arr2=arr[:]; arr2[t],arr2[t+1]=arr2[t+1],arr2[t]
                F2=cyc_set(arr2,(n,n,n))
                D=F^F2
                line=np.zeros((n,n,n),dtype=bool)
                idx=[slice(None)]*3; idx[ci]=p; idx[cj]=q; line[tuple(idx)]=True
                assert (D==line).all()
                assert (F[line].all() and not F2[line].any()) or (F2[line].all() and not F[line].any())
                arr,F=arr2,F2; swaps+=1; changed=True
    # now colours sorted: all slices equal in every coordinate, set is empty or full
    assert F.all() or not F.any()
    return swaps

for n in range(2,7):
    print('E*|[%d]^3: reduced to a trivial set by %d single-line swaps (certificate that it is in D3)'%(n,transposition_certificate(n)))

# ---------- (S) ----------
def box_sets_sample(sizes, count):
    n0,n1,n2=sizes; out=[]
    cells=[(i,j) for i in range(n1) for j in range(n2)]
    adds=set()
    for al in itertools.product(range(-1,2),repeat=n1):
        for be in itertools.product(range(-2,3),repeat=n2):
            d=np.add.outer(np.array(al),np.array(be))
            if np.abs(d).max()<=1: adds.add(d.tobytes())
    adds=[np.frombuffer(b,dtype=d.dtype).reshape(n1,n2) for b in adds]
    tries=0
    while len(out)<count:
        tries+=1
        # structured base slices make rich examples likelier
        G=np.zeros((n1,n2),dtype=int)
        mode=random.random()
        if mode<0.4: G=(np.random.rand(n1,n2)<0.5).astype(int)
        elif mode<0.7:
            r=np.random.permutation(n1); c=np.random.permutation(n2)
            G=(np.add.outer(r,-c)>random.choice([-1,0,1])).astype(int)
        else:
            G=np.add.outer((np.random.rand(n1)<0.5).astype(int),np.zeros(n2,dtype=int))
            G=G if random.random()<0.5 else np.add.outer(np.zeros(n1,dtype=int),(np.random.rand(n2)<0.5).astype(int))
        valid=[d for d in adds if ((G+d)>=0).all() and ((G+d)<=1).all()]
        F=np.stack([G]+[G+random.choice(valid) for _ in range(n0-1)]).astype(bool)
        out.append(F)
    return out

def is_box(F):
    f=F.astype(int)
    d=f-f[:1]; d=d-d[:,:1]; d=d-d[:,:,:1]
    return not d.any()

def labelled_partition(F, axis):
    # other axes in cyclic bookkeeping: label t means "slices in the part differ by functions of x_t alone"
    f=np.moveaxis(F.astype(int),axis,0); others=[a for a in range(3) if a!=axis]   # remaining axes, increasing
    n=f.shape[0]; parts={}
    for a in range(n):
        t=random.choice([0,1])                      # which other axis the part points to
        # class representative: canonical form of slice modulo functions of x_{others[t]} alone
        s=f[a]
        key=None
        for (lab,rep),mem in parts.items():
            if lab!=t: continue
            d=s-f[rep]
            const_along_other = (d==d[:, :1]).all() if t==0 else (d==d[:1, :]).all()
            if const_along_other: key=(lab,rep); break
        if key is None: key=(t,a); parts[key]=[]
        parts[key].append(a)
    return [(others[lab],mem) for (lab,rep),mem in parts.items()]

def indep(sub, ax):   # sub independent of axis ax
    return (sub==np.take(sub,[0],axis=ax)).all()
def only(sub, ax):    # sub depends only on axis ax
    return all(indep(sub,b) for b in range(3) if b!=ax)
def onecoord(sub): return any(only(sub,a) for a in range(3))

def test(F):
    assert is_box(F)
    parts=[labelled_partition(F,i) for i in range(3)]
    stats={'mutual':0,'chain':0}
    # column lemmas
    for i in range(3):
        for j in range(3):
            if i>=j: continue
            k=3-i-j
            for (li,P) in parts[i]:
                for (lj,Q) in parts[j]:
                    ix=[None]*3; ix[i]=P; ix[j]=Q; ix[k]=list(range(F.shape[k]))
                    col=F[np.ix_(*ix)]
                    if li==j and lj==i:
                        assert indep(col,k) or only(col,k), ('mutual',F,i,j,P,Q); stats['mutual']+=1
                    elif li==j and lj==k:
                        assert indep(col,i) or only(col,i), ('chain',F,i,j,P,Q); stats['chain']+=1
                    elif li==k and lj==i:
                        assert indep(col,j) or only(col,j), ('chain2',F,i,j,P,Q); stats['chain']+=1
    # three removals, each of window events contained in the current set
    H=F.copy()
    for (i,j) in [(0,1),(1,2),(2,0)]:
        k=3-i-j
        for (li,P) in parts[i]:
            for (lj,Q) in parts[j]:
                ix=[None]*3; ix[i]=P; ix[j]=Q; ix[k]=list(range(F.shape[k]))
                col=H[np.ix_(*ix)]
                if indep(col,k): H[np.ix_(*ix)]=False
    bad=0
    for (l0,P) in parts[0]:
        for (l1,Q) in parts[1]:
            for (l2,R) in parts[2]:
                if not onecoord(H[np.ix_(P,Q,R)]): bad+=1
    assert bad==0, ('residual cell not a one-coordinate product',F,parts)
    return stats, max(len(p) for p in parts)

for sizes in [(3,3,4),(4,4,4),(3,4,5),(5,4,4)]:
    S=box_sets_sample(sizes,3000); m=c=0; big=0
    for F in S:
        st,mx=test(F); m+=st['mutual']; c+=st['chain']; big=max(big,mx)
    print(sizes,'box sets tested:',len(S),'distinct:',len({F.tobytes() for F in S}),' mutual columns:',m,' chain columns:',c,' no failures')
