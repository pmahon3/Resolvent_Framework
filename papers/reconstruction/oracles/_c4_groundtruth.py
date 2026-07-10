"""Ground truth on C4-target L=4: is dim C = dim R yet C != R? (dim-equality is
NECESSARY not SUFFICIENT — the suspected bug in _p47check.py). Exact facet-level
separation + validate the exhibited backtracker witness."""
from fractions import Fraction as F
from itertools import product, combinations

def rref(mat):
    M=[list(map(F,r)) for r in mat]; rows=len(M); cols=len(M[0]) if M else 0
    pc=[];r=0
    for c in range(cols):
        pr=next((i for i in range(r,rows) if M[i][c]!=0),None)
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]; M[r]=[x/M[r][c] for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        pc.append(c);r+=1
        if r==rows: break
    return M[:r],pc

def simplex_max(c,Aeq,beq):
    # maximize c.x s.t. Aeq x = beq, x>=0 (two-phase exact)
    m=len(Aeq); n=len(c)
    rows=[[F(x) for x in Aeq[i]]+[F(beq[i])] for i in range(m)]
    for i in range(m):
        if rows[i][-1]<0: rows[i]=[-x for x in rows[i]]
    T=[rows[i][:n]+[F(1) if j==i else F(0) for j in range(m)]+[rows[i][-1]] for i in range(m)]
    basis=[n+i for i in range(m)]
    def piv(r,col):
        p=T[r][col]; T[r]=[x/p for x in T[r]]
        for i in range(m):
            if i!=r and T[i][col]!=0:
                f=T[i][col]; T[i]=[a-f*b for a,b in zip(T[i],T[r])]
    # phase1
    obj=[F(0)]*(n+m+1)
    for i in range(m):
        for j in range(n+m+1): obj[j]+=T[i][j]
    for j in range(n,n+m): obj[j]=F(0)
    while True:
        col=next((j for j in range(n) if obj[j]>0),-1)
        if col==-1: break
        r,best=-1,None
        for i in range(m):
            if T[i][col]>0:
                ra=T[i][-1]/T[i][col]
                if best is None or ra<best or (ra==best and basis[i]<basis[r]): best,r=ra,i
        if r==-1: return None,None
        piv(r,col); basis[r]=col
        obj=[F(0)]*(n+m+1)
        for i in range(m):
            for j in range(n+m+1): obj[j]+=T[i][j]
        for j in range(n,n+m): obj[j]=F(0)
    if sum(T[i][-1] for i in range(m) if basis[i]>=n)!=0: return 'infeasible',None
    cc=[F(x) for x in c]+[F(0)]*m
    z=[F(0)]*(n+m+1)
    for j in range(n+m): z[j]=cc[j]
    for i in range(m):
        if z[basis[i]]!=0:
            f=z[basis[i]]
            for j in range(n+m+1): z[j]-=f*T[i][j]
    while True:
        col=next((j for j in range(n+m) if z[j]>0),-1)
        if col==-1: break
        r,best=-1,None
        for i in range(m):
            if T[i][col]>0:
                ra=T[i][-1]/T[i][col]
                if best is None or ra<best or (ra==best and basis[i]<basis[r]): best,r=ra,i
        if r==-1: return 'unbounded',None
        piv(r,col); basis[r]=col
        f=z[col]
        for j in range(n+m+1): z[j]-=f*T[r][j]
    x=[F(0)]*(n+m)
    for i in range(m): x[basis[i]]=T[i][-1]
    return sum(cc[j]*x[j] for j in range(n+m)),x[:n]

def hom_arcs(He):
    a=set()
    for (u,v) in He: a.add((u,v));a.add((v,u))
    return frozenset(a)

def build(rel,A,L):
    V=[p for p in product(range(A),repeat=L) if all((p[i],p[(i+1)%L]) in rel for i in range(L))]
    cells=[];ctx=[];bm=[]
    idx={}
    for ei in range(L):
        seen={}
        for i,p in enumerate(V):
            k=(p[ei],p[(ei+1)%L])
            if (ei,k) not in idx:
                idx[(ei,k)]=len(cells); cells.append((ei,k)); ctx.append(ei); bm.append(0)
            bm[idx[(ei,k)]]|=(1<<i)
    d=len(cells)
    E,f=[],[]
    for ei in range(L):
        E.append([F(1) if ctx[j]==ei else F(0) for j in range(d)]);f.append(F(1))
    for e1,e2 in combinations(range(L),2):
        ids=[j for j in range(d) if ctx[j] in (e1,e2)]
        par={j:j for j in ids}
        def fd(z):
            while par[z]!=z: par[z]=par[par[z]];z=par[z]
            return z
        for j1 in ids:
            for j2 in ids:
                if j1<j2 and ctx[j1]!=ctx[j2] and (bm[j1]&bm[j2]):
                    r1,r2=fd(j1),fd(j2)
                    if r1!=r2: par[r1]=r2
        blk={}
        for j in ids: blk.setdefault(fd(j),[]).append(j)
        for b in blk.values():
            row=[F(0)]*d
            for j in b: row[j]=F(1) if ctx[j]==e1 else F(-1)
            if any(x!=0 for x in row): E.append(row);f.append(F(0))
    phis=[tuple(idx[(ei,(p[ei],p[(ei+1)%L]))] for ei in range(L)) for p in V]
    return V,cells,ctx,idx,E,f,phis

rel=hom_arcs([(0,1),(1,2),(2,3),(3,0)]); A=4
V,cells,ctx,idx,E,f,phis=build(rel,A,4)
d=len(cells)
Rr,_=rref([r+[v] for r,v in zip(E,f)]); dimC=d-len(Rr)
# dim R
base=phis[0];piv=[];dimR=0
for phi in phis[1:]:
    row={}
    for c0,c1 in zip(base,phi):
        if c0!=c1: row[c1]=row.get(c1,F(0))+1;row[c0]=row.get(c0,F(0))-1
    for (lc,pr) in piv:
        if row.get(lc):
            cf=row[lc]
            for k,vv in pr.items(): row[k]=row.get(k,F(0))-cf*vv
    row={k:vv for k,vv in row.items() if vv!=0}
    if row:
        lc=min(row);iv=1/row[lc];piv.append((lc,{k:vv*iv for k,vv in row.items()}));dimR+=1
print(f"C4-target L=4: |V|={len(V)}, d={d}, dim C={dimC}, dim R={dimR}, dims equal={dimC==dimR}")
# TRUE test: enumerate R facets, max each over C; if any strictly exceeds -> C != R
# R = conv(phis-as-0/1-vectors in cell space)
verts=[[F(1) if j in phi else F(0) for j in range(d)] for phi in phis]
# affine hull equations of R via rref of differences, then facets by brute (dim small?)
v0=verts[0]
diffs=[[verts[i][j]-v0[j] for j in range(d)] for i in range(1,len(verts))]
B,piv2=rref(diffs); r=len(B)
print(f"  R affine dim = {r}")
# enumerate candidate facets: all subsets of verts of size r defining hyperplanes — too many.
# Instead: the DIRECT unsafe test — is the backtracker witness in C\R?
# Witness at C4-L4: exhibited as all-halves EA-coherent point. Build it:
# the "doubled rotation" was rejected (not injective). The genuine witness:
# C4 backtrack orbit of length 4: token walks 0,1,0,1 vs 0,3,0,3 ... let's search
# for a vertex of C outside R directly via LP: for each R-facet found by
# maximizing a random-ish integer objective over C and checking vs R-vertices.
# Robust exact test: does the LP  max 0  s.t. x in C, x = sum lambda_v verts,
# lambda>=0, sum=1  become INFEASIBLE for some x in C? Equivalent: is every
# C-vertex in R? Enumerate C-vertices is hard; instead test membership of a
# specific coherent point.
# Coherent point p*: uniform over the 2 "rotation" sections gives a point in R.
# The claimed witness: put mass to force a backtracker. Search coherent extreme:
# maximize c.x over C for many integer c, then test if optimum x in R (LP).
import itertools
def in_R(x):
    # x = sum lambda_v verts, lambda>=0 sum 1
    nv=len(verts)
    Aeq=[[verts[v][j] for v in range(nv)] for j in range(d)]+[[F(1)]*nv]
    beq=[x[j] for j in range(d)]+[F(1)]
    st,_=simplex_max([F(0)]*nv,Aeq,beq)
    return st!='infeasible' and st is not None
def max_over_C(c):
    st,x=simplex_max(c,[r[:] for r in E],f[:])
    return st,x
found_gap=False
import random
random.seed(1)
tested=0
for trial in range(400):
    c=[random.randint(-3,3) for _ in range(d)]
    st,x=max_over_C(c)
    if st in ('infeasible','unbounded',None): continue
    tested+=1
    if not in_R(x):
        print(f"  *** C != R: found C-vertex OUTSIDE R (objective trial {trial})")
        print(f"      x = {[str(v) for v in x]}")
        found_gap=True; break
print(f"  tested {tested} C-optima; C != R: {found_gap}")
if not found_gap:
    print("  no gap found in 400 exact integer directions -> consistent with C = R")
    print("  (but this is sampling; dim-equal + no-gap = strong but not proof)")
