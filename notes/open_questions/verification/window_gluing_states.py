"""Oracle (exact, Fraction arithmetic): do contextual window statistics define a
state on the glued binary carrier D?  L(1_E) is computed by solving A c = 1_E
exactly over Q; well-definedness = marginals annihilate ker(A).
See notes/open_questions/delay_embedding/collision_vs_generation.md."""
import itertools, sys
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from window_gluing_dynkin import run

def rref(M):
    M=[r[:] for r in M]; piv=[]; r=0
    for c in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; inv=1/M[r][c]; M[r]=[v*inv for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==len(M): break
    return M,piv

def test(name,n,W,marg):
    pts,D,_,_=run(n,W)
    cols=[];m=[]
    for w in W:
        for v in itertools.product(range(2),repeat=len(w)):
            cols.append([Fr(int(tuple(p[i] for i in w)==v)) for p in pts]); m.append(Fr(marg(w,v)))
    k=len(cols)
    # functional on span: solve via rref of [A^T | I]: rows of A^T are columns
    aug=[cols[j]+[Fr(int(t==j)) for t in range(k)] for j in range(k)]
    R,piv=rref(aug); P=len(pts)
    # rows whose point-part is zero give kernel vectors of the column map
    wd=all(sum(r[P+t]*m[t] for t in range(k))==0 for r in R if all(v==0 for v in r[:P]))
    basis=[(r[:P],sum(r[P+t]*m[t] for t in range(k))) for r in R if any(v!=0 for v in r[:P])]
    vals=[]
    for E in D:
        y=[Fr(E>>i&1) for i in range(P)]; L=Fr(0)
        for vec,lv in basis:
            c=next(i for i,v in enumerate(vec) if v!=0)
            coef=y[c]/vec[c]; y=[a-coef*b for a,b in zip(y,vec)]; L+=coef*lv
        assert all(v==0 for v in y)
        vals.append(L)
    print(name,"| well-defined:",wd,"| range on D: [%s, %s]"%(min(vals),max(vals)))

anti=lambda w,v: Fr(1,2) if v[0]!=v[1] else 0
def pr(w,v):
    if w==(3,0): return Fr(1,2) if v[0]==v[1] else 0
    return anti(w,v)
test("triangle anticorr (contextual)",3,[(0,1),(1,2),(2,0)],anti)
test("4-ring anticorr (realisable)",4,[(0,1),(1,2),(2,3),(3,0)],anti)
test("4-ring odd parity (contextual)",4,[(0,1),(1,2),(2,3),(3,0)],pr)
