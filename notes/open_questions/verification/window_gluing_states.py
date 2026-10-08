import itertools, numpy as np, sys
sys.path.insert(0,'.')
from window_gluing_dynkin import run
def test(name,n,W,marg):
    pts,D,inter,_=run(n,W)
    cols=[];vals=[]
    for w in W:
        for v in itertools.product(range(2),repeat=len(w)):
            cols.append([1.0 if tuple(p[i] for i in w)==v else 0.0 for p in pts]); vals.append(marg(w,v))
    A=np.array(cols).T; m=np.array(vals)
    # well-definedness: m orthogonal to kernel of A
    ns=np.linalg.svd(A)[2][np.linalg.matrix_rank(A):]
    wd=np.allclose(ns@m,0)
    lo,hi=9,-9; neg=None
    for E in D:
        y=np.array([float(E>>i&1) for i in range(len(pts))])
        c=np.linalg.lstsq(A,y,rcond=None)[0]; assert np.allclose(A@c,y)
        L=c@m; lo=min(lo,L); hi=max(hi,L)
        if L< -1e-9 and neg is None: neg=[pts[i] for i in range(len(pts)) if E>>i&1]
    print(name,"well-defined:",wd,"state range on D: [%.3f, %.3f]"%(lo,hi),"neg event:",neg)
anti=lambda w,v: 0.5 if (len(v)==2 and v[0]!=v[1]) else (0.0 if len(v)==2 else 0.5)
test("triangle anticorr (contextual)",3,[(0,1),(1,2),(2,0)],anti)
test("4-ring anticorr (realisable, even)",4,[(0,1),(1,2),(2,3),(3,0)],anti)
# 4-ring PR-box-like: three anticorr, one corr -> contextual
def pr(w,v):
    if w==(3,0): return 0.5 if v[0]==v[1] else 0.0
    return anti(w,v)
test("4-ring odd-parity (contextual)",4,[(0,1),(1,2),(2,3),(3,0)],pr)
