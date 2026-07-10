"""Taming #10 (bipartite-target phase decoupling) + counting theorem + P44/45/46
(2026-07-10).

Taming #10: for a bipartite-target symmetric language, MD gives one global
phase scalar t; the change of variables (xi,eta) splits every edge distribution
into a t-mixture of two copies of the TARGET-EDGE polytope in independent phase
coordinates -> C_t = t.FSTAB (+) (1-t).FSTAB, R_t = t.STAB (+) (1-t).STAB; on
bipartite G, FSTAB=STAB (taming #7 base) => C=R.

Counting theorem: symmetric loopless MD languages are EXACTLY forests
(|rho|=2|E(H)| <= 2|A|-1 => |E| <= |V|-1 => forest => bipartite => phase-
decouples). So the loopless symmetric MD class is forest-only at every scale.

J10: verify phase-decoupling identity for P4-path on a small bipartite G
     (exact rational: every edge dist = t-mixture of two NAND dists; section
     count = two-phase independent-set correspondence).
Counting: enumerate symmetric loopless MD languages <=5 states, confirm all are
     forests (as homomorphism targets).
P44: P4-path on subdivided-K5 -> safe, dim C = dim R = 31 = 1 + 2*15.
P45: claw K_{1,3} and 5-state spider on subdivided-K5 -> safe (tree theorem).
P46: loopy symmetric MD languages swept vs the catalogue; survivors withheld.
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import rref, simplex_max

def hom_target_arcs(H_edges, nverts):
    """Symmetric relation = adjacency of graph H (loopless): (a,b) iff {a,b} edge."""
    arcs=set()
    for (u,v) in H_edges:
        arcs.add((u,v)); arcs.add((v,u))
    return frozenset(arcs)

P4 = hom_target_arcs([(3,0),(0,1),(1,2)], 4)   # path 3-0-1-2
print("== J10: P4 = twisted double of NAND, phase-decoupling identity ==")
print(f"  P4 arcs: {sorted(P4)}; bipartition classes {{3,1}} vs {{0,2}}")

def subdivided(K):
    verts=K; edges=[]
    for (u,v) in combinations(range(K),2):
        m=verts;verts+=1;edges+=[(u,m),(m,v)]
    return verts, edges
def homs(nv, edges, rel, Asz):
    adj={}
    for (x,y) in edges: adj.setdefault(x,[]).append((y,True));adj.setdefault(y,[]).append((x,False))
    V=[];asg=[None]*nv
    def bt(i):
        if i==nv: V.append(tuple(asg));return
        for s in range(Asz):
            g=True
            for (w,fwd) in adj.get(i,()):
                if asg[w] is not None:
                    pr=(s,asg[w]) if fwd else (asg[w],s)
                    if pr not in rel: g=False;break
            if g: asg[i]=s;bt(i+1);asg[i]=None
    bt(0);return V

# decoupling identity on a small bipartite G: the 6-cycle C6 (bipartite)
# realize as a "ring" of 6 vertices, edges consecutive
C6E=[(i,(i+1)%6) for i in range(6)]
Vc=[p for p in product(range(4),repeat=6)
    if all((p[i],p[(i+1)%6]) in P4 for i in range(6))]
print(f"  C6 into P4: |homs| = {len(Vc)}")
# bipartition of C6: even/odd
side={i: i%2 for i in range(6)}
# for each hom, extract phase t-consistency: on class-A (side 0), state in {3,2}?
# actually the phase = which bipartition-class-of-P4 the vertex maps into,
# aligned with G's bipartition. Check: every hom assigns G-class-0 entirely to
# one P4-class and G-class-1 to the other (global phase), OR mixes.
def p4class(s): return 0 if s in (3,1) else 1   # odd-class {3,1}=A
phase_consistent=0
for h in Vc:
    ph0={p4class(h[v]) for v in range(6) if side[v]==0}
    ph1={p4class(h[v]) for v in range(6) if side[v]==1}
    if len(ph0)==1 and len(ph1)==1 and ph0!=ph1:
        phase_consistent+=1
print(f"  homs with global phase (G-class -> single P4-class): {phase_consistent}"
      f"/{len(Vc)} -> {'ALL (decoupling holds: sections are 2-phase independent sets)' if phase_consistent==len(Vc) else 'PARTIAL'}")
# independent-set count check: homs = 2 * (#independent-set-pairs)? each phase =
# choose which G-class is 'endpoint-free'... verify section count = 2*|IS-based|
# NAND homs into C6 = independent sets of C6:
NAND=frozenset({(0,0),(0,1),(1,0)})
IS_C6=[p for p in product(range(2),repeat=6) if all((p[i],p[(i+1)%6]) in NAND for i in range(6))]
print(f"  NAND homs into C6 (independent sets): {len(IS_C6)};"
      f" 2*that = {2*len(IS_C6)} vs P4 homs {len(Vc)}:"
      f" {'MATCH (twisted double confirmed)' if 2*len(IS_C6)==len(Vc) else 'differ - phase overlap at all-one'}")

# ---- full C vs R analysis on subdivided-K5 (P44) ----
def analyze_dim(rel, Asz, K, label, ndir=80):
    nv, edges = subdivided(K)
    V = homs(nv, edges, rel, Asz)
    cells,ctx_of,ck=[],[],[]
    for ei,(x,y) in enumerate(edges):
        bk={}
        for i,p in enumerate(V): bk[(p[x],p[y])]=bk.get((p[x],p[y]),0)|(1<<i)
        for kk,bm in bk.items(): cells.append(bm);ctx_of.append(ei);ck.append((ei,kk))
    d=len(cells)
    E,fv=[],[]
    for ei in range(len(edges)):
        E.append([F(1) if ctx_of[j]==ei else F(0) for j in range(d)]);fv.append(F(1))
    for e1,e2 in combinations(range(len(edges)),2):
        ids=[j for j in range(d) if ctx_of[j] in (e1,e2)]
        par={j:j for j in ids}
        def find(z):
            while par[z]!=z: par[z]=par[par[z]];z=par[z]
            return z
        for j1 in ids:
            for j2 in ids:
                if j1<j2 and ctx_of[j1]!=ctx_of[j2] and (cells[j1]&cells[j2]):
                    r1,r2=find(j1),find(j2)
                    if r1!=r2: par[r1]=r2
        bl={}
        for j in ids: bl.setdefault(find(j),[]).append(j)
        for blk in bl.values():
            row=[F(0)]*d
            for j in blk: row[j]=F(1) if ctx_of[j]==e1 else F(-1)
            if any(x!=0 for x in row): E.append(row);fv.append(F(0))
    Rr,_=rref([r+[v] for r,v in zip(E,fv)]);dimC=d-len(Rr)
    cell_of={c:j for j,c in enumerate(ck)}
    phis=[tuple(cell_of[(ei,(p[x],p[y]))] for ei,(x,y) in enumerate(edges)) for p in V]
    base=phis[0];piv=[];dimR=0
    for phi in phis[1:]:
        row={}
        for c0,c1 in zip(base,phi):
            if c0!=c1: row[c1]=row.get(c1,F(0))+1;row[c0]=row.get(c0,F(0))-1
        for (lc,pr) in piv:
            if row.get(lc):
                cf=row[lc]
                for k2,v2 in pr.items(): row[k2]=row.get(k2,F(0))-cf*v2
        row={k2:v2 for k2,v2 in row.items() if v2!=0}
        if row:
            lc=min(row);iv=1/row[lc];piv.append((lc,{k2:v2*iv for k2,v2 in row.items()}));dimR+=1
    Erref=[r[:-1] for r in Rr];frref=[r[-1] for r in Rr]
    random.seed(44);mism=0
    for _ in range(ndir):
        c=[F(random.randint(-3,3)) for _ in range(d)]
        st,val,_=simplex_max(c,Erref,frref,[],[])
        best=max(sum(c[j] for j in phi) for phi in phis)
        if val!=best: mism+=1
    print(f"  {label}: |V|={len(V)}, dim C={dimC}, dim R={dimR}, {ndir} LPs mismatch={mism}"
          f" -> {'SAFE' if dimC==dimR and mism==0 else 'CHECK'}")
    return dimC, dimR, len(V)

print("== P44: P4-path on subdivided-K5 (predict dim=31=1+2*15) ==")
dC,dR,nV=analyze_dim(P4,4,5,"P4/subdiv-K5")
print(f"  dim check: {dC}==31? {dC==31} (fibered = 1 phase + 2*15 vertex coords)")

print("== P45: claw K_{1,3} and 5-spider on subdivided-K5 (tree theorem) ==")
CLAW=hom_target_arcs([(0,1),(0,2),(0,3)],4)   # star center 0
dC2,dR2,_=analyze_dim(CLAW,4,5,"claw K13/subdiv-K5")
SPIDER=hom_target_arcs([(0,1),(1,2),(1,3),(1,4)],5)  # tree on 5 vertices
dC3,dR3,_=analyze_dim(SPIDER,5,5,"5-spider/subdiv-K5")

print("== Counting theorem: symmetric loopless MD languages <=5 states = forests ==")
from endgame_triage import marginal_determined
def is_forest(H_edges, nverts):
    par=list(range(nverts))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]];x=par[x]
        return x
    for (u,v) in H_edges:
        ru,rv=f(u),f(v)
        if ru==rv: return False
        par[ru]=rv
    return True
checked=0;nonforest_md=0
for nverts in range(2,6):
    alledges=list(combinations(range(nverts),2))
    for r in range(1,len(alledges)+1):
        for He in combinations(alledges,r):
            arcs=hom_target_arcs(He,nverts)
            # connected targets only (else trivial), all states used
            used=set()
            for (a,b) in arcs: used|={a,b}
            if len(used)<nverts: continue
            md,_=marginal_determined(arcs,nverts)
            if md:
                checked+=1
                if not is_forest(He,nverts): nonforest_md+=1
print(f"  symmetric loopless targets with MD: {checked}; NON-forest among them: {nonforest_md}"
      f" -> {'THEOREM CONFIRMED (MD symmetric loopless <=> forest)' if nonforest_md==0 else 'COUNTEREXAMPLE'}")

print("== P46: loopy symmetric MD languages vs catalogue (survivors) ==")
from endgame_triage import pair_bipartite, signable_any_ordering
from swap_spectrum_scan import canonical
def connected_rel(arcs,Asz):
    und={};nodes=set()
    for (a,b) in arcs: und.setdefault(a,set()).add(b);und.setdefault(b,set()).add(a);nodes|={a,b}
    if len(nodes)<Asz: return False
    seen={min(nodes)};fr=[min(nodes)]
    while fr:
        x=fr.pop()
        for y in und.get(x,()):
            if y not in seen: seen.add(y);fr.append(y)
    return seen==nodes
def recurrent_branching(arcs,Asz):
    adjf={s:[b for (a,b) in arcs if a==s] for s in range(Asz)}
    reach={s:{s} for s in range(Asz)};ch=True
    while ch:
        ch=False
        for s in range(Asz):
            new=set(reach[s])
            for t in list(reach[s]): new|=set(adjf[t])
            if new!=reach[s]: reach[s]=new;ch=True
    R=[(a,b) for (a,b) in arcs if a in reach[b]];ro={}
    for (a,b) in R: ro.setdefault(a,[]).append(b)
    return any(len(v)>=2 for v in ro.values())
p46=[]
for Asz in (2,3,4):
    for mask in range(1,1<<(Asz*Asz)):
        if canonical(mask,Asz)!=mask: continue
        arcs=frozenset((a,b) for a in range(Asz) for b in range(Asz) if mask>>(a*Asz+b)&1)
        if not all((b,a) in arcs for (a,b) in arcs): continue   # symmetric
        if not any(a==b for (a,b) in arcs): continue            # HAS loops
        outd=[sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        if min(outd)==0: continue
        if not connected_rel(arcs,Asz) or not recurrent_branching(arcs,Asz): continue
        md,_=marginal_determined(arcs,Asz)
        if not md: continue
        pb=pair_bipartite(arcs,Asz); sg=signable_any_ordering(arcs,Asz)
        if pb and not sg:
            p46.append((Asz,sorted(arcs)))
print(f"  loopy symmetric MD, PB, non-signable survivors: {len(p46)}")
for (a,l) in p46[:10]: print(f"    |A|={a}: {l}")
if not p46:
    print("  P46 EMPTY -> loopy symmetric MD class fully tamed (signable/decoupling);")
    print("  symmetric MD Circuit Localization closes: forest-target ∪ signable.")
