"""P47/P48/P49: the universal impossibility conjecture (2026-07-08).

P47: symmetric non-MD expelled by exchange richness. Cyclic symmetric H ->
     Safe(H) finite-and-small (exchange spectra cofinite). Compute exact
     polytope Safe profiles of C4/C5/C6 TARGET languages on rings, predict
     unsafe at every nondegenerate length except C5@2, C6@4 (within window).
P48: SCC reduction lemma / rho39 membrane. rho39 = {(0,0),(0,2),(1,0),(1,1),
     (1,2),(2,0)} (non-MD exemplar). On strongly-connected recurrent frame:
     u(1) constant (only 1 feeds 1), membrane cells p(10),p(12) vanish ->
     all-1 mixed with NAND-in-costume -> tamed by #7. Predict safe on
     SCC-oriented subdivided-K4, sharp signature u(1) const + both cross-cells
     identically zero at every optimum.
P49: exhaustive scan of strongly connected, non-symmetric, recurrent-branching
     languages <=4 states with Safe ⊇ {6,8}, screened vs the ten-taming
     catalogue. Survivors = the last possible small-scale fork candidates.
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations, permutations
from commensurability_harness import rref, simplex_max
from ring_commensurability import commensurable, scope_contexts
from swap_spectrum_scan import canonical, unsafe_set, base_walk_lengths
from endgame_triage import marginal_determined, pair_bipartite, signable_any_ordering

def hom_arcs(He):
    a=set()
    for (u,v) in He: a.add((u,v));a.add((v,u))
    return frozenset(a)
def variety_A(L, rel, A):
    return [p for p in product(range(A),repeat=L) if all((p[i],p[(i+1)%L]) in rel for i in range(L))]

# ---- P47: exact Safe profiles of C4/C5/C6 target languages ----
print("== P47: Safe profiles of cyclic symmetric targets (exchange expulsion) ==")
for cyc,label in [([(0,1),(1,2),(2,3),(3,0)],"C4-target"),
                  ([(0,1),(1,2),(2,3),(3,4),(4,0)],"C5-target"),
                  ([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],"C6-target")]:
    rel=hom_arcs(cyc); A=1+max(max(a,b) for (a,b) in rel)
    safe=[]; unsafe=[]; degen=[]
    for L in range(3,11):
        V=variety_A(L,rel,A)
        if not V: degen.append(L); continue
        ctxs=scope_contexts(V,[(i,(i+1)%L) for i in range(L)])
        ok,_=commensurable(len(V),ctxs,f"__{label}_L{L}")
        (safe if ok else unsafe).append(L)
    print(f"  {label}: SAFE={safe} UNSAFE={unsafe} DEGEN={degen}")

# ---- P48: rho39 membrane on SCC-oriented subdivided-K4 ----
print("== P48: rho39 membrane sealing on strongly-connected frame ==")
RHO39=frozenset({(0,0),(0,2),(1,0),(1,1),(1,2),(2,0)})
# predecessor structure: who feeds 1?
feeds1=[a for (a,b) in RHO39 if b==1]
print(f"  predecessors of state 1: {feeds1} (only 1 feeds 1: {feeds1==[1]})")
# ring test at even L (strongly connected ring = time-realizable)
for L in (4,6):
    V=variety_A(L,RHO39,3)
    if not V: print(f"  L={L}: empty"); continue
    ctxs=scope_contexts(V,[(i,(i+1)%L) for i in range(L)])
    ok,_=commensurable(len(V),ctxs,f"  rho39 ring L={L} (n={len(V)})")
    # sharp signature: is u(1) constant across vertices in every section? and
    # do membrane cells (1,0),(1,2) appear?
    membrane=any((p[i],p[(i+1)%L]) in {(1,0),(1,2)} for p in V for i in range(L))
    u1_vals={sum(1 for x in p if x==1) for p in V}
    print(f"    membrane cells (1,0)/(1,2) realized in variety: {membrane};"
          f" (on recurrent ring, u(1) flux) — safe={ok}")

# ---- P49: the last fork candidates ----
print("== P49: strongly-connected non-symmetric recurrent-branching, Safe⊇{6,8} ==")
def strongly_connected(arcs,Asz):
    adj={s:[b for (a,b) in arcs if a==s] for s in range(Asz)}
    radj={s:[a for (a,b) in arcs if b==s] for s in range(Asz)}
    def reach(g):
        seen={0};st=[0]
        while st:
            x=st.pop()
            for y in g.get(x,()):
                if y not in seen: seen.add(y);st.append(y)
        return seen
    return reach(adj)==set(range(Asz)) and reach(radj)==set(range(Asz))
def recurrent_branching(arcs,Asz):
    ro={}
    for (a,b) in arcs: ro.setdefault(a,[]).append(b)
    return any(len(v)>=2 for v in ro.values())  # SCC => all arcs recurrent
def is_sym(arcs): return all((b,a) in arcs for (a,b) in arcs)
def deterministic(arcs,Asz):
    ro={}
    for (a,b) in arcs: ro.setdefault(a,[]).append(b)
    return all(len(v)<=1 for v in ro.values())
def graded(arcs,Asz):
    from math import gcd
    W=base_walk_lengths(arcs,Asz,24); g=0
    for L in W: g=gcd(g,L)
    return g>=2
def nonrefl_twin_present(arcs,Asz):
    def sig(x): return (frozenset(b for (a,b) in arcs if a==x),frozenset(a for (a,b) in arcs if b==x))
    for x,y in combinations(range(Asz),2):
        if not((x,x) in arcs or (y,y) in arcs or (x,y) in arcs or (y,x) in arcs) and sig(x)==sig(y):
            return True
    return False
def catalogue_tamed(arcs,Asz):
    """screen vs the ten tamings (the ones detectable at language level)."""
    if deterministic(arcs,Asz): return "determinism"
    if graded(arcs,Asz): return "grading"
    if nonrefl_twin_present(arcs,Asz): return "twin"
    md,_=marginal_determined(arcs,Asz)
    if md and pair_bipartite(arcs,Asz) and signable_any_ordering(arcs,Asz): return "signable"
    # phase-decoupling / bipartite-target: symmetric forest handled elsewhere (non-sym here)
    return None
survivors=[]; scanned=0
for Asz in (2,3,4):
    for mask in range(1,1<<(Asz*Asz)):
        if canonical(mask,Asz)!=mask: continue
        arcs=frozenset((a,b) for a in range(Asz) for b in range(Asz) if mask>>(a*Asz+b)&1)
        if is_sym(arcs): continue
        if not strongly_connected(arcs,Asz): continue
        if not recurrent_branching(arcs,Asz): continue
        U=unsafe_set(arcs,Asz,12)
        if 6 in U or 8 in U: continue      # need Safe ⊇ {6,8}
        W=base_walk_lengths(arcs,Asz,12)
        if 6 not in W or 8 not in W: continue  # nondegenerate at 6,8
        scanned+=1
        tam=catalogue_tamed(arcs,Asz)
        if tam is None:
            survivors.append((Asz,sorted(arcs)))
        # else tamed
print(f"  scanned (SCC non-sym recurrent-branching, Safe⊇{{6,8}}): {scanned}")
print(f"  UNTAMED survivors (last possible fork candidates): {len(survivors)}")
for (a,l) in survivors[:15]: print(f"    |A|={a}: {l}")
if not survivors:
    print("  P49 EMPTY -> no small-scale fork candidate survives the catalogue;")
    print("  universal impossibility conjecture UNREFUTED at <=4 states.")
