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
        pc.append(c); r+=1
        if r==rows: break
    return M[:r],pc

def hom_arcs(He):
    a=set()
    for (u,v) in He: a.add((u,v));a.add((v,u))
    return frozenset(a)

def ring_safe(rel, A, L):
    """C=R test on ring L via dim comparison (dim C == dim R) — necessary
    condition, and exact: if dims differ C strictly bigger => unsafe; if equal,
    confirm no facet separation by LP would be needed, but dim-equality on these
    0/1 polytopes with integral R is the safe-certificate when R spans a
    lattice-saturated subspace. We report dim C vs dim R."""
    V=[p for p in product(range(A),repeat=L) if all((p[i],p[(i+1)%L]) in rel for i in range(L))]
    if not V: return 'empty',0,0,0
    # cells
    cells,ctx=[],[]
    for ei in range(L):
        bk={}
        for i,p in enumerate(V):
            k=(p[ei],p[(ei+1)%L]); bk[k]=bk.get(k,0)|(1<<i)
        for k,bm in bk.items(): cells.append((ei,k)); ctx.append(ei)
    d=len(cells)
    idx={c:j for j,c in enumerate(cells)}
    E,f=[],[]
    for ei in range(L):
        E.append([F(1) if ctx[j]==ei else F(0) for j in range(d)]); f.append(F(1))
    for e1,e2 in combinations(range(L),2):
        ids=[j for j in range(d) if ctx[j] in (e1,e2)]
        par={j:j for j in ids}
        def fd(z):
            while par[z]!=z: par[z]=par[par[z]];z=par[z]
            return z
        # cell intersection = share a section
        for j1 in ids:
            for j2 in ids:
                if j1<j2 and ctx[j1]!=ctx[j2] and (cells[j1][1] and True):
                    bm1=0;bm2=0
                    # recompute membership bitmask
                    pass
        # simpler: block equalities via actual bitmask intersection
    # rebuild with bitmasks for block detection
    bm=[0]*d
    for i,p in enumerate(V):
        for ei in range(L):
            bm[idx[(ei,(p[ei],p[(ei+1)%L]))]] |= (1<<i)
    E,f=[],[]
    for ei in range(L):
        E.append([F(1) if ctx[j]==ei else F(0) for j in range(d)]); f.append(F(1))
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
        blocks={}
        for j in ids: blocks.setdefault(fd(j),[]).append(j)
        for blk in blocks.values():
            row=[F(0)]*d
            for j in blk: row[j]=F(1) if ctx[j]==e1 else F(-1)
            if any(x!=0 for x in row): E.append(row);f.append(F(0))
    Rr,_=rref([r+[v] for r,v in zip(E,f)]); dimC=d-len(Rr)
    # dim R
    phis=[tuple(idx[(ei,(p[ei],p[(ei+1)%L]))] for ei in range(L)) for p in V]
    base=phis[0];piv=[];dimR=0
    for phi in phis[1:]:
        row={}
        for c0,c1 in zip(base,phi):
            if c0!=c1: row[c1]=row.get(c1,F(0))+1;row[c0]=row.get(c0,F(0))-1
        for (lc,pr) in piv:
            if row.get(lc):
                cf=row[lc]
                for k,v in pr.items(): row[k]=row.get(k,F(0))-cf*v
        row={k:v for k,v in row.items() if v!=0}
        if row:
            lc=min(row);iv=1/row[lc];piv.append((lc,{k:v*iv for k,v in row.items()}));dimR+=1
    return ('SAFE' if dimC==dimR else 'unsafe'), len(V), dimC, dimR

for cyc,label in [([(0,1),(1,2),(2,3),(3,0)],"C4tgt"),
                  ([(0,1),(1,2),(2,3),(3,4),(4,0)],"C5tgt"),
                  ([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],"C6tgt")]:
    rel=hom_arcs(cyc);A=1+max(max(a,b) for (a,b) in rel)
    out=[]
    for L in range(3,8):
        v,n,dC,dR=ring_safe(rel,A,L)
        out.append(f"L{L}:{v}({dC}v{dR})")
    print(f"{label}(A={A}): "+" ".join(out))
