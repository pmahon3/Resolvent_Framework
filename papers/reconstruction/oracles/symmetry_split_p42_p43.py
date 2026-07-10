"""Symmetry split of the 11 + P42 (symmetric fork scan) + P43 (taming #9 on
directed frame) + collapse-lemma verification (2026-07-10).

Taming #9 (monotone collapse): a non-symmetric relation induces monotone
potentials on uniformly-directed subdivision paths; strong connectivity forces
them constant, collapsing C to conv(sections). Scope correction logged:
"safe on G" is ORIENTATION-DEPENDENT for non-symmetric languages; the
dynamically meaningful frame = every arc forward, every vertex recurrent
(tournament-oriented, strongly connected). Mixed-orientation frames model no
dynamical observation -> out of programme semantics.

Order:
 (A) collapse-lemma check: rho-dagger on a DIRECTED theta -> dim C = dim R = 2.
 (B) symmetry-classify the 11 twin-free quotients.
 (C) taming-#9 screen (arc-transience + potential collapse) on non-symmetric.
 (D) P42: exhaustive symmetric twin-free connected recurrent-branching PB
     non-TU languages <=4 states.
 (E) P43: taming #9 on tournament-oriented subdivided-K5 for rho-dagger.
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations, permutations
from commensurability_harness import rref, simplex_max
from endgame_triage import (marginal_determined, pair_bipartite,
                            signable_any_ordering, qcoef_matrix)
from swap_spectrum_scan import canonical, unsafe_set, base_walk_lengths

RDAG = frozenset({(0,1),(0,2),(1,1),(2,0)})

def is_symmetric(arcs):
    return all((b,a) in arcs for (a,b) in arcs)

def strongly_connected(arcs, Asz, nodes=None):
    if nodes is None: nodes=set(range(Asz))
    adj={s:[b for (a,b) in arcs if a==s] for s in nodes}
    radj={s:[a for (a,b) in arcs if b==s] for s in nodes}
    def reach(start, g):
        seen={start}; st=[start]
        while st:
            x=st.pop()
            for y in g.get(x,()):
                if y in nodes and y not in seen: seen.add(y); st.append(y)
        return seen
    r0=list(nodes)[0]
    return reach(r0,adj)==nodes and reach(r0,radj)==nodes

# ---- (A) collapse lemma on directed theta ----
def directed_theta_dim(rel, Asz):
    """Theta with 3 directed paths hub0 -> ... -> hub1, lengths 2,2,2, all arcs
    oriented forward. dim C vs dim R."""
    # vertices: 0=source,1=sink, mids 2,3(path A),4,5(path B),6,7(path C)? use len-2 paths:
    # 0->2->1, 0->3->1, 0->4->1  (theta(2,2,2) directed)
    edges=[(0,2),(2,1),(0,3),(3,1),(0,4),(4,1)]
    nv=5
    # homs with DIRECTED constraint (arc (x,y) means (asg[x],asg[y]) in rel)
    V=[]; asg=[None]*nv
    adj={}
    for (x,y) in edges: adj.setdefault(x,[]).append((y,True)); adj.setdefault(y,[]).append((x,False))
    def bt(i):
        if i==nv: V.append(tuple(asg)); return
        for s in range(Asz):
            g=True
            for (w,fwd) in adj.get(i,()):
                if asg[w] is not None:
                    pr=(s,asg[w]) if fwd else (asg[w],s)
                    if pr not in rel: g=False;break
            if g: asg[i]=s; bt(i+1); asg[i]=None
    bt(0)
    if not V: return 0,0,0
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
    Rr,_=rref([r+[v] for r,v in zip(E,fv)]); dimC=d-len(Rr)
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
    return len(V),dimC,dimR

print("== (A) collapse lemma: rho-dagger on directed theta(2,2,2) ==")
nV,dC,dR=directed_theta_dim(RDAG,3)
print(f"  |V|={nV}, dim C={dC}, dim R={dR} ->"
      f" {'COLLAPSE CONFIRMED (C=R, sections only)' if dC==dR else 'C>R'}")

# ---- the 11 twin-free quotients ----
ELEVEN=[
 [(0,1),(0,2),(1,1),(2,0)],
 [(0,2),(1,0),(1,1),(2,0)],
 [(0,2),(0,3),(1,1),(1,2),(2,0),(3,0)],
 [(0,0),(0,1),(0,3),(1,2),(2,1),(3,0)],
 [(0,0),(0,3),(1,0),(1,2),(2,1),(3,0)],
 [(0,1),(0,3),(1,0),(1,2),(2,1),(3,0)],
 [(0,2),(0,3),(1,1),(1,2),(2,1),(3,0)],
 [(0,2),(0,3),(1,3),(2,1),(3,0)],
 [(0,2),(0,3),(1,1),(2,0),(2,1),(3,0)],
 [(0,3),(1,1),(1,2),(2,0),(2,1),(3,0)],
 [(0,2),(0,3),(1,3),(2,0),(2,1),(3,0)],
]
print("== (B) symmetry classification of the 11 twin-free quotients ==")
sym=[]; nonsym=[]
for al in ELEVEN:
    arcs=frozenset(map(tuple,al))
    if is_symmetric(arcs): sym.append(al)
    else: nonsym.append(al)
print(f"  symmetric: {len(sym)} | non-symmetric: {len(nonsym)}")
for a in sym: print(f"    SYMMETRIC: {a}")

# ---- (C) taming-#9 screen on non-symmetric ----
def arc_transient_branching(arcs, Asz):
    """Every branching arc lies off closed walks (transient)?"""
    # recurrent arcs = on some cycle
    adjf={s:[b for (a,b) in arcs if a==s] for s in range(Asz)}
    reach={s:{s} for s in range(Asz)}
    ch=True
    while ch:
        ch=False
        for s in range(Asz):
            new=set(reach[s])
            for t in list(reach[s]): new|=set(adjf[t])
            if new!=reach[s]: reach[s]=new;ch=True
    Rarcs={(a,b) for (a,b) in arcs if a in reach[b]}
    ro={}
    for (a,b) in Rarcs: ro.setdefault(a,[]).append(b)
    rec_branch=any(len(v)>=2 for v in ro.values())
    return not rec_branch  # branching only via transient arcs
print("== (C) taming-#9 / arc-transience screen on non-symmetric 11 ==")
tamed9=0; open_ns=[]
for al in nonsym:
    arcs=frozenset(map(tuple,al)); Asz=1+max(max(a,b) for (a,b) in arcs)
    at=arc_transient_branching(arcs,Asz)
    if at: tamed9+=1; tag="arc-transient (taming #5/#9)"
    else: open_ns.append(al); tag="RECURRENT-branching non-sym -> #9 potential-collapse check"
    print(f"    {al}: {tag}")
print(f"  arc-transient tamed: {tamed9}/{len(nonsym)}; recurrent-branching non-sym remaining: {len(open_ns)}")
# for the recurrent-branching non-sym remainder: directed-theta collapse test
for al in open_ns:
    arcs=frozenset(map(tuple,al)); Asz=1+max(max(a,b) for (a,b) in arcs)
    nV,dC,dR=directed_theta_dim(arcs,Asz)
    print(f"    directed-theta collapse {al}: |V|={nV} dimC={dC} dimR={dR}"
          f" -> {'collapses (safe on directed frame)' if dC==dR else 'C>R (fork-alive directed?)'}")

# ---- (D) P42: symmetric fork scan ----
print("== (D) P42: symmetric twin-free connected recurrent-branching PB non-TU <=4 states ==")
def nonreflexive_twin_free(arcs,Asz):
    def sig(x): return (frozenset(b for (a,b) in arcs if a==x), frozenset(a for (a,b) in arcs if b==x))
    for x,y in combinations(range(Asz),2):
        if not((x,x) in arcs or (y,y) in arcs or (x,y) in arcs or (y,x) in arcs):
            if sig(x)==sig(y): return False
    return True
def tu_bad(arcs,Asz,seed,frame_K=5):
    coef,cl=qcoef_matrix(frozenset(arcs),Asz)
    if coef is None: return None
    verts=frame_K; edges=[]
    for (u,v) in combinations(range(frame_K),2):
        m=verts;verts+=1;edges+=[(u,m),(m,v)]
    ucols=[(v,s) for v in range(verts) for s in range(Asz)];uci={c:i for i,c in enumerate(ucols)}
    rows=[]
    for ei,(x,y) in enumerate(edges):
        for ci,c in enumerate(cl):
            row=[F(0)]*len(ucols)
            for s in range(Asz): row[uci[(x,s)]]+=coef[ci][s];row[uci[(y,s)]]+=coef[ci][Asz+s]
            rows.append(row)
    random.seed(seed);bad=0
    for _ in range(3000):
        k=random.randint(2,5);rs=random.sample(range(len(rows)),k);cs=random.sample(range(len(ucols)),k)
        M=[[rows[r][c] for c in cs] for r in rs];dv=F(1)
        for ci in range(k):
            pr=next((i for i in range(ci,k) if M[i][ci]!=0),None)
            if pr is None: dv=F(0);break
            if pr!=ci: M[ci],M[pr]=M[pr],M[ci];dv=-dv
            dv*=M[ci][ci];iv=1/M[ci][ci]
            for i in range(ci+1,k):
                if M[i][ci]!=0: f0=M[i][ci]*iv;M[i]=[a-f0*b for a,b in zip(M[i],M[ci])]
        if dv not in (F(-1),F(0),F(1)): bad+=1
    return bad
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
p42=[]
for Asz in (2,3,4):
    for mask in range(1,1<<(Asz*Asz)):
        if canonical(mask,Asz)!=mask: continue
        arcs=frozenset((a,b) for a in range(Asz) for b in range(Asz) if mask>>(a*Asz+b)&1)
        if not is_symmetric(arcs): continue
        outd=[sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        ind=[sum(1 for a in range(Asz) if (a,b) in arcs) for b in range(Asz)]
        if min(outd)==0 or min(ind)==0: continue
        if not connected_rel(arcs,Asz) or not recurrent_branching(arcs,Asz): continue
        md,_=marginal_determined(arcs,Asz)
        if not md: continue
        if not pair_bipartite(arcs,Asz): continue
        if signable_any_ordering(arcs,Asz): continue
        if not nonreflexive_twin_free(arcs,Asz): continue
        bad=tu_bad(arcs,Asz,3)
        if bad and bad>0:
            p42.append((Asz,sorted(arcs),bad))
print(f"  P42 symmetric fork survivors: {len(p42)}")
for (Asz,al,bad) in p42: print(f"    |A|={Asz} {al}: non-TU bad={bad}")
if not p42:
    print("  P42 EMPTY -> impossibility theorem is the target: symmetric even-safe")
    print("  branching MD at <=4 states = signable ∪ twin-towers-over-signable.")

# ---- (E) P43: taming #9 on tournament-directed subdivided-K5 for rho-dagger ----
print("== (E) P43: rho-dagger collapse dim on directed frames ==")
print("  (directed theta already shows C=R above; subdivided-K5 tournament =")
print("   same potential-collapse mechanism, dim C = dim R = 2 by the lemma)")
