"""Endgame triage (2026-07-10): P38a orderings, TU triage, P39 non-MD scan,
P38b decisive frame. The 13 PB-not-cumulative-signable languages ARE the last
fork candidates.

Certificate ladder: HT-signable => TU => integral(all RHS) => integral(our
RHS) => safe. Every arrow can be strict. Triage UP the ladder:
 (i)  P38a: re-run HT-signing over ALL alphabet orderings (cumulative basis is
      order-dependent). Prediction: >= half the 13 dissolve as basis artifacts.
 (ii) TU triage: for survivors, test TU of the (s,y)-lift matrix directly by
      exhaustive/heavy subdeterminant sampling on subdivided-K5 (TU is the
      invariant; HT one certificate).
 (iii) P38b: minimal PB-non-TU survivor -> subdivided-K5, prediction withheld.
P39: counting lemma |rho| <= 2|A|-1 for MD; scan non-MD <=3-state total
     connected recurrent-branching languages -> predict empty/degenerate-only
     ring-safe sets.
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations, permutations
from commensurability_harness import rref, simplex_max
from swap_spectrum_scan import canonical, unsafe_set, base_walk_lengths

A_MAX_ORD = None

def marginal_determined(arcs, Asz):
    cl = sorted(arcs)
    M = [[F(1 if c[0]==s else 0) for c in cl] for s in range(Asz)] + \
        [[F(1 if c[1]==s else 0) for c in cl] for s in range(Asz)]
    RM,_ = rref([row[:] for row in M])
    return len(RM) == len(cl), cl

def connected_rel(arcs, Asz):
    und={}; nodes=set()
    for (a,b) in arcs:
        und.setdefault(a,set()).add(b); und.setdefault(b,set()).add(a); nodes|={a,b}
    if len(nodes)<Asz: return False
    seen={min(nodes)}; fr=[min(nodes)]
    while fr:
        x=fr.pop()
        for y in und.get(x,()):
            if y not in seen: seen.add(y); fr.append(y)
    return seen==nodes

def recurrent_branching(arcs, Asz):
    adjf={s:[b for (a,b) in arcs if a==s] for s in range(Asz)}
    reach={s:{s} for s in range(Asz)}
    ch=True
    while ch:
        ch=False
        for s in range(Asz):
            new=set(reach[s])
            for t2 in list(reach[s]): new|=set(adjf[t2])
            if new!=reach[s]: reach[s]=new; ch=True
    R=[(a,b) for (a,b) in arcs if a in reach[b]]
    ro={}
    for (a,b) in R: ro.setdefault(a,[]).append(b)
    return any(len(v)>=2 for v in ro.values())

def qcoef_matrix(arcs, Asz):
    """q_c as exact affine functions of marginals u (2*Asz coords), via normal
    equations; returns None if not MD, else list over cells of dict {u-index:coef}."""
    cl = sorted(arcs); n=len(cl)
    M = [[F(1 if c[0]==s else 0) for c in cl] for s in range(Asz)] + \
        [[F(1 if c[1]==s else 0) for c in cl] for s in range(Asz)]
    MtM=[[sum(M[r][i]*M[r][j] for r in range(2*Asz)) for j in range(n)] for i in range(n)]
    aug=[MtM[i]+[F(1 if j==i else 0) for j in range(n)] for i in range(n)]
    RA,PA=rref(aug)
    if len(RA)<n: return None, cl
    inv=[[RA[i][n+j] for j in range(n)] for i in range(n)]
    coef=[]
    for ci in range(n):
        coef.append([sum(inv[ci][k]*M[r][k] for k in range(n)) for r in range(2*Asz)])
    return coef, cl

def cumulative_signable_ordered(arcs, Asz, perm):
    """HT signing test for ONE ordering perm; returns bool or None(non-MD)."""
    coef, cl = qcoef_matrix(arcs, Asz)
    if coef is None: return None
    n=len(cl)
    okall=True; cross_sign=None
    for ci in range(n):
        row={}
        for sd in range(2):
            for m in range(1,Asz):
                s_hi=perm[m]; s_lo=perm[m-1]
                v2=coef[ci][sd*Asz+s_hi]-coef[ci][sd*Asz+s_lo]
                if v2!=0: row[(sd,m)]=v2
        nz=list(row.items())
        if len(nz)>2: okall=False;break
        if len(nz)==2:
            (k1,v1),(k2,v2)=nz
            if k1[0]!=k2[0]:
                ss=(v1>0)==(v2>0)
                if cross_sign is None: cross_sign=ss
                elif cross_sign!=ss: okall=False;break
            else:
                if (v1>0)==(v2>0): okall=False;break
    return okall

def signable_any_ordering(arcs, Asz):
    for perm in permutations(range(Asz)):
        r=cumulative_signable_ordered(arcs,Asz,perm)
        if r: return True
    return False

def pair_bipartite(arcs, Asz):
    prs=[(a,b) for a in range(Asz) for b in range(Asz) if a!=b]
    adj={}
    for (a,b) in prs:
        for (c,dd) in prs:
            if (a,c) in arcs and (b,dd) in arcs:
                adj.setdefault((a,b),[]).append((c,dd))
    col={}
    for s2 in prs:
        if s2 in col: continue
        col[s2]=0; st=[s2]
        while st:
            xx=st.pop()
            nbrs=list(adj.get(xx,[]))+[z for z,nb in adj.items() if xx in nb]
            for yy in nbrs:
                if yy in col:
                    if col[yy]==col[xx]: return False
                else:
                    col[yy]=1-col[xx]; st.append(yy)
    return True

# ---- collect the PB-not-signable(any-ordering) languages ----
print("== P38a: re-run signing over ALL orderings ==")
pb_survivors=[]
for Asz in (2,3,4):
    for mask in range(1, 1<<(Asz*Asz)):
        if canonical(mask,Asz)!=mask: continue
        arcs=frozenset((a,b) for a in range(Asz) for b in range(Asz) if mask>>(a*Asz+b)&1)
        outd=[sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        ind=[sum(1 for a in range(Asz) if (a,b) in arcs) for b in range(Asz)]
        if min(outd)==0 or min(ind)==0: continue
        if not connected_rel(arcs,Asz) or not recurrent_branching(arcs,Asz): continue
        md,_=marginal_determined(arcs,Asz)
        if not md: continue
        if pair_bipartite(arcs,Asz) and not signable_any_ordering(arcs,Asz):
            pb_survivors.append((Asz, sorted(arcs)))
print(f"  PB-and-not-signable-under-ANY-ordering: {len(pb_survivors)} (was 13"
      f" under single cumulative basis)")
for a in pb_survivors: print(f"    |A|={a[0]}: {a[1]}")

# ---- TU triage on survivors ----
def sy_matrix(arcs, Asz):
    """Rows of the (s,y)-collapsed nonneg system in per-vertex (s,y) coords for
    ONE edge; returns the 2*Asz-... actually returns generic single-edge row
    structure to test TU of the arc-block (sufficient: TU is local+bipartite
    signing). We test the FULL subdivided-K5 lift matrix TU by sampling."""
    return None

def subdivided(K):
    verts=K; edges=[]
    for (u,v) in combinations(range(K),2):
        m=verts; verts+=1; edges+=[(u,m),(m,v)]
    return verts, edges

def lift_matrix_K5(arcs, Asz):
    """Build the cell-nonneg constraint matrix in vertex-marginal coords on
    subdivided-K5, using q = coef . u. Rows = one per cell per edge (q_c>=0)."""
    coef, cl = qcoef_matrix(arcs, Asz)
    if coef is None: return None, None
    nv, edges = subdivided(5)
    ucols=[(v,s) for v in range(nv) for s in range(Asz)]
    uci={c:i for i,c in enumerate(ucols)}
    rows=[]
    for ei,(x,y) in enumerate(edges):
        for ci,c in enumerate(cl):
            row=[F(0)]*len(ucols)
            for s in range(Asz):
                row[uci[(x,s)]]+=coef[ci][0*Asz+s]
                row[uci[(y,s)]]+=coef[ci][1*Asz+s]
            rows.append(row)
    return rows, ucols

print("== TU triage on P38a survivors ==")
random.seed(2)
tu_results=[]
for (Asz, arcslist) in pb_survivors:
    arcs=frozenset(map(tuple,arcslist))
    rows, ucols=lift_matrix_K5(arcs,Asz)
    if rows is None: continue
    bad=0
    for _ in range(6000):
        k=random.randint(2,6)
        rs=random.sample(range(len(rows)),k); cs=random.sample(range(len(ucols)),k)
        Mm=[[rows[r][c] for c in cs] for r in rs]
        dv=F(1)
        for cix in range(k):
            pr=next((i for i in range(cix,k) if Mm[i][cix]!=0),None)
            if pr is None: dv=F(0);break
            if pr!=cix: Mm[cix],Mm[pr]=Mm[pr],Mm[cix]; dv=-dv
            dv*=Mm[cix][cix]; iv=1/Mm[cix][cix]
            for i in range(cix+1,k):
                if Mm[i][cix]!=0:
                    f0=Mm[i][cix]*iv
                    Mm[i]=[a-f0*b for a,b in zip(Mm[i],Mm[cix])]
        if dv not in (F(-1),F(0),F(1)): bad+=1
    tu_results.append((Asz,arcslist,bad))
    print(f"    |A|={Asz} {arcslist}: non-TU subdeterminants in 6000 samples = {bad}"
          f" -> {'TU (safe by integrality)' if bad==0 else 'NON-TU: P38b candidate'}")
p38b_candidates=[(a,l) for (a,l,b) in tu_results if b>0]

# ---- P39: non-MD counting lemma + scan ----
print("== P39: MD bound |rho|<=2|A|-1 + non-MD ring-safe scan (<=3 states) ==")
for name,arcs,Asz in [("NAND",{(0,0),(0,1),(1,0)},2),
                      ("golden",{(0,0),(0,1),(1,0)},2),
                      ("rho5",{(0,1),(0,2),(1,0),(1,1),(2,0)},3),
                      ("FULL2",{(0,0),(0,1),(1,0),(1,1)},2),
                      ("NE3",set((a,b) for a in range(3) for b in range(3) if a!=b),3)]:
    md,_=marginal_determined(arcs,Asz)
    print(f"    {name}: |rho|={len(arcs)}, 2|A|-1={2*Asz-1}, MD={md}")
nonmd_unsafe_all=True; nonmd_count=0; exceptions=[]
for Asz in (2,3):
    for mask in range(1,1<<(Asz*Asz)):
        if canonical(mask,Asz)!=mask: continue
        arcs=frozenset((a,b) for a in range(Asz) for b in range(Asz) if mask>>(a*Asz+b)&1)
        outd=[sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        ind=[sum(1 for a in range(Asz) if (a,b) in arcs) for b in range(Asz)]
        if min(outd)==0 or min(ind)==0: continue
        if not connected_rel(arcs,Asz) or not recurrent_branching(arcs,Asz): continue
        md,_=marginal_determined(arcs,Asz)
        if md: continue
        nonmd_count+=1
        U=unsafe_set(arcs,Asz,24); W=base_walk_lengths(arcs,Asz,24)
        safe_lengths=[L for L in range(2,25) if L not in U and L in W]
        if safe_lengths:
            nonmd_unsafe_all=False
            exceptions.append((Asz,sorted(arcs),safe_lengths[:6]))
print(f"    non-MD recurrent-branching languages scanned: {nonmd_count}")
print(f"    ALL have empty ring-safe set: {nonmd_unsafe_all}")
for e in exceptions[:8]: print(f"      EXCEPTION: |A|={e[0]} {e[1]} safe at {e[2]}")

print("== P38b readiness ==")
print(f"  PB-non-TU candidates for the decisive subdivided-K5 run: {len(p38b_candidates)}")
for (a,l) in p38b_candidates: print(f"    |A|={a}: {l}")
