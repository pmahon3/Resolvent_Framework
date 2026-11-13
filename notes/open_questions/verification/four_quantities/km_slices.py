# gate.five_quantities (views_across_records/FIVE_QUANTITIES_GATE.md). V01(K_m(n)) by slices, for any m:
# a pair-sum 0/1 set on K_m is a pair-sum set on K_{m-1} (slice x0 = 0) plus, for each further value of x0,
# a slice difference that is a sum of one-quantity functions with values in {-1,0,1}.
import itertools, sys, time, numpy as np
def diffs(rest):
    """all d = sum_j h_j(x_j) on the grid `rest` with values in {-1,0,1} (T1: at most two non-constant parts)."""
    out=set(); k=len(rest)
    def add(arr):
        for c in (-1,0,1):
            d=arr+c
            if d.min()>=-1 and d.max()<=1: out.add(d.astype(np.int8).tobytes())
    add(np.zeros(rest,int))
    def lift(g,j):
        sh=[1]*k; sh[j]=rest[j]; return np.array(g).reshape(sh)+np.zeros(rest,int)
    for j in range(k):
        for g in itertools.product(range(3),repeat=rest[j]):
            if min(g)==0 and max(g)>0: add(lift(g,j))
    for j,l in itertools.combinations(range(k),2):
        for g in itertools.product(range(2),repeat=rest[j]):
            if min(g)==0 and max(g)==1:
                for h in itertools.product(range(2),repeat=rest[l]):
                    if min(h)==0 and max(h)==1: add(lift(g,j)+lift(h,l))
    return np.array([np.frombuffer(b,np.int8).reshape(rest) for b in sorted(out)])
_cache={}
def v01(sizes):
    sizes=tuple(sizes)
    if sizes in _cache: return _cache[sizes]
    if len(sizes)==1:
        S=np.array(list(itertools.product(range(2),repeat=sizes[0])),dtype=np.int8)
    else:
        rest=sizes[1:]; base=v01(rest); D=diffs(rest); flatB=base.reshape(len(base),-1); flatD=D.reshape(len(D),-1)
        adm=[[] for _ in range(len(base))]
        for d in flatD:
            Fn=flatB+d; good=((Fn>=0)&(Fn<=1)).all(1)
            for i in np.nonzero(good)[0]: adm[i].append(Fn[i])
        rows=[]
        for i in range(len(base)):
            for combo in itertools.product(adm[i],repeat=sizes[0]-1):
                rows.append(np.concatenate((flatB[i],)+combo))
        S=np.array(rows,dtype=np.int8).reshape((-1,)+sizes)
    _cache[sizes]=S; return S
def irreducible_mask(S):
    m=S.ndim-1; M=len(S); red=np.zeros(M,bool)
    for ax in range(1,m+1):
        if S.shape[ax]<2: red[:]=True; continue
        for a,b in itertools.combinations(range(S.shape[ax]),2):
            d=np.take(S,a,axis=ax).astype(np.int8)-np.take(S,b,axis=ax)
            for keep in range(1,m):
                ref=d
                for k in range(1,m):
                    if k!=keep: ref=np.take(ref,[0],axis=k)
                red|=(d==ref).reshape(M,-1).all(1)
    return ~red
def depends(S):
    m=S.ndim-1; cnt=np.zeros(len(S),int)
    for ax in range(1,m+1):
        first=np.take(S,[0],axis=ax); cnt+=~((S==first).reshape(len(S),-1).all(1))
    return cnt
if __name__=='__main__':
    t0=time.time()
    for sizes in [(3,3,3),(2,2,2,2),(3,3,3,3)]:
        print('validate',sizes,'|V01|',len(v01(sizes)),flush=True)
    for sizes in [tuple(int(c) for c in a) for a in sys.argv[1:]]:
        S=v01(sizes); irr=irreducible_mask(S); dep=depends(S)
        print('K%d'%len(sizes),sizes,'|V01|',len(S),'| irreducible',int(irr.sum()),'| depends on k quantities:',dict(sorted({int(k):int((dep==k).sum()) for k in set(dep.tolist())}.items())),'| time %.0fs'%(time.time()-t0),flush=True)
