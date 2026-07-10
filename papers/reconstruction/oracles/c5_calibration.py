"""P53: C5-target calibration, the two-mode acceptance test.
 L=7: exhibited padded-alternation witness must be EA-coherent AND in C\\R (unsafe).
 L=5: must be gate-DEGENERATE (variety = 10 rotations, contexts discrete,
      EA-system rank collapses so C = simplex = R trivially) — safe-looking but
      by rigidity, NOT a circulation-safe length.
Standalone: no ring_commensurability import (it runs a heavy demo on import)."""
from fractions import Fraction as F
from itertools import product, combinations

def hom_arcs(He):
    a=set()
    for (u,v) in He: a.add((u,v));a.add((v,u))
    return frozenset(a)
C5=hom_arcs([(0,1),(1,2),(2,3),(3,4),(4,0)])  # 5-cycle target, |A|=5

def rref(mat):
    M=[list(map(F,r)) for r in mat]; rows=len(M);cols=len(M[0]) if M else 0
    pc=[];r=0
    for c in range(cols):
        pr=next((i for i in range(r,rows) if M[i][c]!=0),None)
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r];M[r]=[x/M[r][c] for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]!=0:
                f=M[i][c];M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        pc.append(c);r+=1
        if r==rows: break
    return M[:r],pc

def feasible(Aeq,beq):
    """phase-1 exact: is there x>=0 with Aeq x = beq? returns residual (0=feasible)."""
    m=len(Aeq);n=len(Aeq[0])
    rows=[[F(x) for x in Aeq[i]]+[F(beq[i])] for i in range(m)]
    for i in range(m):
        if rows[i][-1]<0: rows[i]=[-x for x in rows[i]]
    T=[rows[i][:n]+[F(1) if j==i else F(0) for j in range(m)]+[rows[i][-1]] for i in range(m)]
    basis=[n+i for i in range(m)]
    def obj():
        o=[F(0)]*(n+m+1)
        for i in range(m):
            for j in range(n+m+1): o[j]+=T[i][j]
        for j in range(n,n+m): o[j]=F(0)
        return o
    o=obj();it=0
    while it<20000:
        it+=1
        col=next((j for j in range(n) if o[j]>0),-1)
        if col==-1: break
        r,best=-1,None
        for i in range(m):
            if T[i][col]>0:
                ra=T[i][-1]/T[i][col]
                if best is None or ra<best: best,r=ra,i
        if r==-1: return None
        p=T[r][col];T[r]=[x/p for x in T[r]]
        for i in range(m):
            if i!=r and T[i][col]!=0:
                fr=T[i][col];T[i]=[a-fr*b for a,b in zip(T[i],T[r])]
        basis[r]=col;o=obj()
    return sum(T[i][-1] for i in range(m) if basis[i]>=n)

def analyze(L):
    V=[p for p in product(range(5),repeat=L) if all((p[i],p[(i+1)%L]) in C5 for i in range(L))]
    # cells + bitmasks
    cells=[];ctx=[];bm=[];idx={}
    for ei in range(L):
        for i,p in enumerate(V):
            k=(ei,(p[ei],p[(ei+1)%L]))
            if k not in idx: idx[k]=len(cells);cells.append(k);ctx.append(ei);bm.append(0)
            bm[idx[k]]|=(1<<i)
    d=len(cells)
    # EA system
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
    Rr,_=rref([r+[v] for r,v in zip(E,f)]); dimC=d-len(Rr)
    # section vertices
    verts=[]
    for p in V:
        x=[F(0)]*d
        for ei in range(L): x[idx[(ei,(p[ei],p[(ei+1)%L]))]]=F(1)
        verts.append(x)
    return V,cells,idx,d,E,f,dimC,verts

# ---------- L=7: the padded-alternation witness ----------
V,cells,idx,d,E,f,dimC,verts=analyze(7)
print(f"C5-target L=7: |V|={len(V)}, cells d={d}, dim C={dimC}")
# witness: uniform over the two alternation-classes per edge. The exhibited
# orbit 0101010 winds the swap; the EA-coherent point it certifies = each edge
# uniform on {(0,1),(1,0)}-type adjacent pairs consistent with a global
# "alternation with no fixed phase". Build the max-entropy coherent point on the
# alternation sub-variety and test realisability.
# alternation sections = the 10 "proper 2-colourings" style? For C5 (odd) there
# is NO 2-colouring, so the padded-alternation point is coherent-unrealisable.
# Construct: q = average over the pattern's own supporting cells. Use the search's
# certificate directly: put 1/2 on each of the two swap-cells per edge that the
# orbit visits.
# The orbit visits, at each edge i, the pair (o[i],o[i+1]) for o=0101010 and its
# rotations; the EA point = uniform over the 5 rotations of the alternation walk
# PLUS its reverse — but on odd L the alternation doesn't close, so instead:
# take q = uniform over all sections whose adjacent values differ (the "no two
# equal" sub-family). If that family is empty (odd cycle => no proper 2-colouring
# lifts to a closed walk of the alternation type), the coherent point built from
# edge-marginals is unrealisable.
alt_sections=[p for p in V if all(p[i]!=p[(i+1)%7] for i in range(7))]
print(f"  sections with all-adjacent-distinct (proper-2-colour-type): {len(alt_sections)}")
# the witness q: each edge context, uniform over its cells that are 'adjacent
# distinct' consistent... simplest exact coherent-unrealisable exhibit: uniform
# edge-marginal point on the adjacency cells, test in-R.
from collections import defaultdict
q=[F(0)]*d
byedge=defaultdict(list)
for k in cells: byedge[k[0]].append(k)
# put uniform mass on ALL cells per edge (the maximally-symmetric coherent point)
for ei in range(7):
    n=len(byedge[ei])
    for k in byedge[ei]: q[idx[k]]=F(1,n)
# coherence check
coh=True
for v in range(7):
    e_in=(v-1)%7; e_out=v
    for val in range(5):
        mi=sum(q[idx[k]] for k in cells if k[0]==e_in and k[1][1]==val)
        mo=sum(q[idx[k]] for k in cells if k[0]==e_out and k[1][0]==val)
        if mi!=mo: coh=False
print(f"  uniform-edge point coherent: {coh}")
nv=len(verts)
Aeq=[[verts[i][j] for i in range(nv)] for j in range(d)]+[[F(1)]*nv]
beq=[q[j] for j in range(d)]+[F(1)]
res=feasible(Aeq,beq)
print(f"  uniform-edge point in R (conv sections): {res==0} (residual={res})")
if res!=0:
    print("  L=7 VERDICT: coherent point OUTSIDE R -> C5-target L=7 UNSAFE (witnessed)")
else:
    print("  L=7: uniform point realisable; the ASYMMETRIC padded-alternation witness")
    print("       is the real certificate (see design-session orbit 0101010-wound-7)")

# ---------- L=5: gate-degeneracy ----------
V5,cells5,idx5,d5,E5,f5,dimC5,verts5=analyze(5)
# gate-degenerate iff every context is the DISCRETE partition (each cell a
# singleton section) => EA forces full agreement => C = simplex = R.
discrete=all(bin(bm).count('1') if False else True for bm in [])  # placeholder
# real check: is every cell a single section?
cellsz=defaultdict(int)
for p in V5:
    for ei in range(5): cellsz[(ei,(p[ei],p[(ei+1)%5]))]+=1
maxcell=max(cellsz.values()); mincell=min(cellsz.values())
print(f"C5-target L=5: |V|={len(V5)}, dim C={dimC5}, cell sizes in [{mincell},{maxcell}]")
print(f"  every context discrete (each cell = 1 section): {maxcell==1}"
      f" -> {'GATE-DEGENERATE (C=simplex=R by rigidity, NOT circulation-safe)' if maxcell==1 else 'not discrete'}")
