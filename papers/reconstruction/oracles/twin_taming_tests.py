"""Taming #8 (twin expansion) + P40/P41 (2026-07-10).

Twin-expansion lemma: expanding state x with (x,x) NOT in rho into twins
(identical in- and out-neighborhoods) preserves Safe and graph-safety; the
polytope factors as quotient x per-vertex label conditionals. Scope: reflexive
twins ((x,x) in rho) FACE each other -> full-language sub-blocks -> UNSAFETY
generator, not a taming.

J-twin: verify states 1,2 are non-reflexive twins in rho_min={(0,1),(0,2),
        (1,0),(2,0)} (identical rows AND columns; (1,1),(2,2) not in rho).
P40: iterated non-reflexive twin-collapse of the 13 PB-non-TU languages; re-run
     the full catalogue (decomposition/transience/determinism/grading/
     signable) on quotients. Predict: rho_min's class dissolves; survivor
     count withheld.
P41: reflexive twin-expand equality's fixed point; predict ring-unsafety
     appears.
Cross-check: rho_min safe on subdivided-K5 via phase-mixture (the taming-#8
     constructive proof) — decomposition-conditioned-on-forced-phase.
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations, permutations
from commensurability_harness import rref, simplex_max
from swap_spectrum_scan import canonical, unsafe_set, base_walk_lengths
from ring_commensurability import commensurable, scope_contexts

def twins(arcs, Asz, x, y):
    """x,y are twins iff same out-set and same in-set (excluding the pair
    itself for the neighborhood comparison), reflexivity-agnostic."""
    out_x = {b for (a,b) in arcs if a==x and b not in (x,y)}
    out_y = {b for (a,b) in arcs if a==y and b not in (x,y)}
    in_x  = {a for (a,b) in arcs if b==x and a not in (x,y)}
    in_y  = {a for (a,b) in arcs if b==y and a not in (x,y)}
    # cross terms: does x reach y iff y reaches x, x->x iff y->y etc.
    cross_ok = (((x,y) in arcs)==((y,x) in arcs)
                and ((x,x) in arcs)==((y,y) in arcs)
                and ((x,y) in arcs)==((y,x) in arcs))
    return out_x==out_y and in_x==in_y and cross_ok
def reflexive_twin(arcs, x, y):
    return (x,x) in arcs or (y,y) in arcs or (x,y) in arcs or (y,x) in arcs

RMIN = {(0,1),(0,2),(1,0),(2,0)}
print("== J-twin: states 1,2 twins in rho_min ==")
row1={b for (a,b) in RMIN if a==1}; row2={b for (a,b) in RMIN if a==2}
col1={a for (a,b) in RMIN if b==1}; col2={a for (a,b) in RMIN if b==2}
print(f"  out(1)={row1} out(2)={row2} in(1)={col1} in(2)={col2}")
print(f"  identical rows: {row1==row2}; identical cols: {col1==col2};"
      f" (1,1),(2,2) in rho: {(1,1) in RMIN},{(2,2) in RMIN} (non-reflexive twins)")
print(f"  twins(rho_min,1,2) = {twins(RMIN,3,1,2)}; reflexive = {reflexive_twin(RMIN,1,2)}")

# quotient: merge y into x, relabel
def quotient(arcs, Asz, x, y):
    rel = {}
    def m(s): return x if s==y else (s if s<y else s-1)
    narcs = set()
    for (a,b) in arcs:
        narcs.add((m(a), m(b)))
    return frozenset(narcs), Asz-1

print("== rho_min quotient ==")
q, qA = quotient(RMIN, 3, 1, 2)
print(f"  collapse 2->1: {sorted(q)} on {qA} states = strict alternation"
      f" (deterministic): {q=={(0,1),(1,0)}}")

# phase-mixture constructive check of rho_min on subdivided-K5
def subdivided(K):
    verts=K; edges=[]
    for (u,v) in combinations(range(K),2):
        m=verts; verts+=1; edges+=[(u,m),(m,v)]
    return verts, edges
def homs(nv, edges, rel, Asz):
    adj={}
    for (x,y) in edges:
        adj.setdefault(x,[]).append((y,True)); adj.setdefault(y,[]).append((x,False))
    V=[]; asg=[None]*nv
    def bt(i):
        if i==nv: V.append(tuple(asg)); return
        for s in range(Asz):
            g=True
            for (w,fwd) in adj.get(i,()):
                if asg[w] is not None:
                    pr=(s,asg[w]) if fwd else (asg[w],s)
                    if pr not in rel: g=False;break
            if g: asg[i]=s; bt(i+1); asg[i]=None
    bt(0); return V
print("== taming-#8 cross-check: rho_min safe on subdivided-K5 (phase-mixture) ==")
nv, edges = subdivided(5)
V = homs(nv, edges, RMIN, 3)
print(f"  |V| = {len(V)}")
# build C, compare dim C vs dim R + exact LP sampling
cells,ctx_of,cellkey=[],[],[]
for ei,(x,y) in enumerate(edges):
    bk={}
    for i,p in enumerate(V): bk[(p[x],p[y])]=bk.get((p[x],p[y]),0)|(1<<i)
    for kk,bm in bk.items(): cells.append(bm); ctx_of.append(ei); cellkey.append((ei,kk))
d=len(cells)
E,fv=[],[]
for ei in range(len(edges)):
    E.append([F(1) if ctx_of[j]==ei else F(0) for j in range(d)]); fv.append(F(1))
for e1,e2 in combinations(range(len(edges)),2):
    ids=[j for j in range(d) if ctx_of[j] in (e1,e2)]
    par={j:j for j in ids}
    def find(z):
        while par[z]!=z: par[z]=par[par[z]]; z=par[z]
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
        if any(x!=0 for x in row): E.append(row); fv.append(F(0))
Rr,_=rref([r+[v] for r,v in zip(E,fv)]); dimC=d-len(Rr)
cell_of={ck:j for j,ck in enumerate(cellkey)}
phis=[tuple(cell_of[(ei,(p[x],p[y]))] for ei,(x,y) in enumerate(edges)) for p in V]
base=phis[0]; piv=[]; dimR=0
for phi in phis[1:]:
    row={}
    for c0,c1 in zip(base,phi):
        if c0!=c1: row[c1]=row.get(c1,F(0))+1; row[c0]=row.get(c0,F(0))-1
    for (lc,pr) in piv:
        if row.get(lc):
            cf=row[lc]
            for k2,v2 in pr.items(): row[k2]=row.get(k2,F(0))-cf*v2
    row={k2:v2 for k2,v2 in row.items() if v2!=0}
    if row:
        lc=min(row); iv=1/row[lc]; piv.append((lc,{k2:v2*iv for k2,v2 in row.items()})); dimR+=1
Erref=[r[:-1] for r in Rr]; frref=[r[-1] for r in Rr]
random.seed(8); mism=0
for _ in range(80):
    c=[F(random.randint(-3,3)) for _ in range(d)]
    st,val,_=simplex_max(c,Erref,frref,[],[])
    best=max(sum(c[j] for j in phi) for phi in phis)
    if val!=best: mism+=1
print(f"  dim C = {dimC}, dim R = {dimR}, 80 exact LPs mismatches = {mism}"
      f" -> {'SAFE (taming #8 confirmed on K5, no TU needed)' if dimC==dimR and mism==0 else 'CHECK'}")

# ---- P40: twin-collapse the 13, re-triage ----
THIRTEEN = [
 (3,[(0,1),(0,2),(1,0),(2,0)]),
 (4,[(0,1),(0,2),(0,3),(1,0),(2,0),(3,0)]),
 (4,[(0,1),(0,2),(0,3),(1,1),(2,0),(3,0)]),
 (4,[(0,2),(0,3),(1,0),(1,1),(2,0),(3,0)]),
 (4,[(0,2),(0,3),(1,1),(1,2),(2,0),(3,0)]),
 (4,[(0,0),(0,1),(0,3),(1,2),(2,1),(3,0)]),
 (4,[(0,0),(0,3),(1,0),(1,2),(2,1),(3,0)]),
 (4,[(0,1),(0,3),(1,0),(1,2),(2,1),(3,0)]),
 (4,[(0,2),(0,3),(1,1),(1,2),(2,1),(3,0)]),
 (4,[(0,2),(0,3),(1,3),(2,1),(3,0)]),
 (4,[(0,2),(0,3),(1,1),(2,0),(2,1),(3,0)]),
 (4,[(0,3),(1,1),(1,2),(2,0),(2,1),(3,0)]),
 (4,[(0,2),(0,3),(1,3),(2,0),(2,1),(3,0)]),
]
def full_collapse(arcs, Asz):
    changed=True
    while changed and Asz>1:
        changed=False
        for x,y in combinations(range(Asz),2):
            if twins(arcs,Asz,x,y) and not reflexive_twin(arcs,x,y):
                arcs,Asz=quotient(arcs,Asz,x,y); changed=True; break
    return arcs,Asz
print("== P40: twin-collapse + re-triage the 13 ==")
def signable_any(arcs,Asz):
    from endgame_triage import signable_any_ordering
    return signable_any_ordering(arcs,Asz)
survivors=0; dissolved=0
for (Asz,al) in THIRTEEN:
    arcs=frozenset(map(tuple,al))
    q,qA=full_collapse(arcs,Asz)
    # classify quotient: deterministic? signable?
    outd={s:[b for (a,b) in q if a==s] for s in range(qA)}
    det=all(len(v)<=1 for v in outd.values())
    sg=signable_any(q,qA) if qA>=1 else True
    tamed = det or sg or (qA<=1)
    if tamed: dissolved+=1
    else: survivors+=1
    print(f"  {al} (|A|={Asz}) -> quotient |A|={qA}: {sorted(q)}"
          f" | det={det} signable={sg} -> {'DISSOLVED' if tamed else 'SURVIVOR'}")
print(f"  P40: dissolved {dissolved}/13, survivors {survivors}"
      f" -> {'ALL DISSOLVE (rho_min class + rest); twin-tower classification shape confirmed' if survivors==0 else 'SURVIVORS REMAIN — genuine twin-free forks'}")

# ---- P41: reflexive twin-expand equality's fixed point ----
print("== P41: reflexive twin-expansion of equality's fixed point ==")
# equality = {(0,0),(1,1)}; expand state 0 into twins 0,0' reflexively:
# new states {0,1,2} with 0,2 twins of the reflexive fixed point 0:
# arcs: (0,0),(0,2),(2,0),(2,2),(1,1) — 0 and 2 face each other (reflexive twin)
REFLEX = frozenset({(0,0),(0,2),(2,0),(2,2),(1,1)})
Us=unsafe_set(REFLEX,3,14); Ws=base_walk_lengths(REFLEX,3,14)
# the {0,2} block is the FULL language on 2 states -> unsafe everywhere it appears
block_full = all((a,b) in REFLEX for a in (0,2) for b in (0,2))
print(f"  reflexive-twin block {{0,2}} = full 2-language: {block_full}")
ringsafe=[L for L in range(3,10) if L not in Us and L in Ws]
print(f"  ring-safe lengths 3..9: {ringsafe}"
      f" -> {'P41 HIT: unsafety generated (no even-safe set, full-block appears)' if not ringsafe else 'P41 CHECK: safe at '+str(ringsafe)}")
