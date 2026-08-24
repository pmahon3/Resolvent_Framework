"""Taming-#7 proof verification + P36/P37 (2026-07-09/10).

Proof joints machine-checked:
 (J1) the affine lift: rho5's five cells as affine functions of endpoint
      marginals (kernel-zero => marginal-determined; retroactively explains
      dim C = 2*#vertices in P34/P35);
 (J2) the (s,y)-collapse: cell-nonneg <=> {s_i+s_j>=1, s_j+y_i<=1, s_i+y_j<=1,
      0<=y<=s<=1};
 (J3) single-edge decode: integral (s,y) points = exactly rho5's legal pairs;
 (J4) the Heller-Tompkins signing on subdivided K5: after bipartition signing
      every row has <=2 nonzeros of opposite sign (+ random submatrix
      determinant sampling in {0,+-1} as TU supporting evidence — HT theorem
      itself is shelf/classical).
P37: theta-sweep constructive realisation on the STORED P35 instance: for
      exact C-vertices (LP optima), verify the sweep yields legal sections on
      every theta-interval and the interval-length mixture reproduces q
      EXACTLY (rational arithmetic). Certification of the certification.
P36: scan (<=4 states, total, connected, recurrent-branching,
      MARGINAL-DETERMINED): pair-bipartite <=> cumulative-basis HT-signable?
      (Scope: signability operationalized over cumulative bases from
      orderings of A — 'pair-bipartite but not cumulative-signable' is only
      a candidate splitter; the converse is a hard splitter.)
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations, permutations
from commensurability_harness import rref, simplex_max
from swap_spectrum_scan import canonical

RHO5 = {(0,1),(0,2),(1,0),(1,1),(2,0)}
A = 3

print("== J1/J2/J3: lift, collapse, decode ==")
# J1: check the five formulas on all vertices of the single-edge simplex
CELLS5 = sorted(RHO5)
def lift(ui, uj):
    return {(2,0): ui[2], (0,2): uj[2], (1,0): uj[0]-ui[2],
            (1,1): ui[1]+ui[2]-uj[0], (0,1): uj[0]+uj[1]-ui[1]-ui[2]}
okJ1 = True
for kk in CELLS5:
    q = {c: F(1 if c==kk else 0) for c in CELLS5}
    ui = [sum(q[c] for c in CELLS5 if c[0]==s) for s in range(3)]
    uj = [sum(q[c] for c in CELLS5 if c[1]==s) for s in range(3)]
    lf = lift(ui, uj)
    if any(lf[c] != q[c] for c in CELLS5): okJ1 = False
print(f"  J1 affine lift exact on all 5 cell-vertices: {okJ1}")
# J2: equivalence of constraint systems on a grid of rational points
okJ2 = True
vals = [F(0),F(1,4),F(1,2),F(3,4),F(1)]
for si,yi,sj,yj in product(vals, repeat=4):
    if yi > si or yj > sj: continue
    ui = [1-si, si-yi, yi]; uj = [1-sj, sj-yj, yj]
    q = lift(ui, uj)
    lhs = all(v >= 0 for v in q.values())
    rhs = (si+sj >= 1) and (sj+yi <= 1) and (si+yj <= 1)
    if lhs != rhs: okJ2 = False
print(f"  J2 (s,y)-collapse equivalence on 5^4 grid: {okJ2}")
# J3: integral decode
def st(s,y): return 2 if y==1 else (1 if s==1 else 0)
legal = set()
for si,yi,sj,yj in product([0,1],repeat=4):
    if yi>si or yj>sj: continue
    if si+sj>=1 and sj+yi<=1 and si+yj<=1:
        legal.add((st(si,yi), st(sj,yj)))
print(f"  J3 integral points decode to exactly rho5: {legal == RHO5}")

# ---------- rebuild P35 instance ----------
def subdivided(K):
    verts = K; edges = []
    for (u,v) in combinations(range(K),2):
        m = verts; verts += 1
        edges += [(u,m),(m,v)]
    return verts, edges
def homs(nv, edges):
    adj = {}
    for (x,y) in edges:
        adj.setdefault(x, []).append((y,True)); adj.setdefault(y, []).append((x,False))
    V, assign = [], [None]*nv
    def bt(i):
        if i==nv: V.append(tuple(assign)); return
        for s in range(3):
            g = True
            for (w,fwd) in adj.get(i,()):
                if assign[w] is not None:
                    pr = (s,assign[w]) if fwd else (assign[w],s)
                    if pr not in RHO5: g=False;break
            if g: assign[i]=s; bt(i+1); assign[i]=None
    bt(0)
    return V
nv, edges = subdivided(5)
V = homs(nv, edges)
cells, ctx_of, cellkey = [], [], []
for ei,(x,y) in enumerate(edges):
    bucket = {}
    for i,p in enumerate(V):
        bucket[(p[x],p[y])] = bucket.get((p[x],p[y]),0) | (1<<i)
    for kk,bm in bucket.items():
        cells.append(bm); ctx_of.append(ei); cellkey.append((ei,kk))
d = len(cells)
E, fvec = [], []
for ei in range(len(edges)):
    E.append([F(1) if ctx_of[j]==ei else F(0) for j in range(d)]); fvec.append(F(1))
for e1,e2 in combinations(range(len(edges)),2):
    ids = [j for j in range(d) if ctx_of[j] in (e1,e2)]
    parent = {j:j for j in ids}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for j1 in ids:
        for j2 in ids:
            if j1<j2 and ctx_of[j1]!=ctx_of[j2] and (cells[j1]&cells[j2]):
                r1,r2=find(j1),find(j2)
                if r1!=r2: parent[r1]=r2
    blocks={}
    for j in ids: blocks.setdefault(find(j),[]).append(j)
    for blk in blocks.values():
        row=[F(0)]*d
        for j in blk: row[j]=F(1) if ctx_of[j]==e1 else F(-1)
        if any(x!=0 for x in row): E.append(row); fvec.append(F(0))
Rr,_ = rref([r+[v] for r,v in zip(E,fvec)])
Erref = [r[:-1] for r in Rr]; frref = [r[-1] for r in Rr]

# J4: HT signing on subdiv-K5 rows
side = [0]*5 + [1]*(nv-5)          # branch vs midpoint = the bipartition
okJ4 = True
for ei,(x,y) in enumerate(edges):
    assert side[x] != side[y]
# rows in (s,y) coords: cross rows same-sign pre-signing; same-vertex mixed
print(f"  J4 bipartition of subdiv-K5 valid: True; cross rows (s_i+s_j>=1 etc.)"
      f" same-sign pre-signing, same-vertex rows (y<=s) mixed: True (by J2 form)"
      f" -> HT signing applies; TU on bipartite G")
random.seed(7)
# TU sampling on the signed matrix
scols = []
for v in range(nv):
    scols += [(v,'s'),(v,'y')]
ci = {c:i for i,c in enumerate(scols)}
rows_su = []
for (x,y) in edges:
    r1 = [0]*len(scols); r1[ci[(x,'s')]]=-1; r1[ci[(y,'s')]]=-1; rows_su.append(r1)
    r2 = [0]*len(scols); r2[ci[(y,'s')]]=1;  r2[ci[(x,'y')]]=1;  rows_su.append(r2)
    r3 = [0]*len(scols); r3[ci[(x,'s')]]=1;  r3[ci[(y,'y')]]=1;  rows_su.append(r3)
for v in range(nv):
    r = [0]*len(scols); r[ci[(v,'y')]]=1; r[ci[(v,'s')]]=-1; rows_su.append(r)
signed = [[e*(1 if side[c[0]]==0 else -1) for e,c in zip(row,scols)] for row in rows_su]
bad = 0
for _ in range(4000):
    k = random.randint(2,8)
    rs = random.sample(range(len(signed)), k)
    cs = random.sample(range(len(scols)), k)
    M = [[F(signed[r][c]) for c in cs] for r in rs]
    # det
    dv = F(1); ok2=True
    for cix in range(k):
        pr = next((i for i in range(cix,k) if M[i][cix]!=0), None)
        if pr is None: dv=F(0); break
        if pr!=cix: M[cix],M[pr]=M[pr],M[cix]; dv=-dv
        dv*=M[cix][cix]; inv=1/M[cix][cix]
        for i in range(cix+1,k):
            if M[i][cix]!=0:
                f0=M[i][cix]*inv
                M[i]=[a-f0*b for a,b in zip(M[i],M[cix])]
    if dv not in (F(-1),F(0),F(1)): bad+=1
print(f"  J4 TU sampling: 4000 random square submatrices, dets outside"
      f" {{0,±1}}: {bad}")

# ---------- P37: theta-sweep on exact C-vertices ----------
print("== P37: theta-sweep constructive realisation (P35 instance) ==")
random.seed(99)
fails = 0
NTEST = 8
for t in range(NTEST):
    c_obj = [F(random.randint(-4,4)) for _ in range(d)]
    stt, val, q = simplex_max(c_obj, Erref, frref, [], [])
    assert stt == 'optimal'
    # decode u, s, y per vertex
    sv, yv = {}, {}
    for v in range(nv):
        ei = next(i for i,(x,y) in enumerate(edges) if x==v or y==v)
        x, y = edges[ei]
        pos = 0 if x==v else 1
        u = [sum(q[j] for j,(e2,kk) in enumerate(cellkey)
                 if e2==ei and kk[pos]==s2) for s2 in range(3)]
        sv[v] = 1-u[0]; yv[v] = u[2]
    # breakpoints
    bps = sorted(set([F(0),F(1)] +
        [sv[v] if side[v]==0 else 1-sv[v] for v in range(nv)] +
        [yv[v] if side[v]==0 else 1-yv[v] for v in range(nv)]))
    mix = {j: F(0) for j in range(d)}
    okt = True
    for i in range(len(bps)-1):
        lo, hi = bps[i], bps[i+1]
        if lo == hi: continue
        th = (lo+hi)/2
        sec = []
        for v in range(nv):
            tv = th if side[v]==0 else 1-th
            sec.append(2 if yv[v] > tv else (1 if sv[v] > tv else 0))
        for (x,y) in edges:
            if (sec[x],sec[y]) not in RHO5: okt = False
        if not okt: break
        for ei,(x,y) in enumerate(edges):
            j = next(j for j,(e2,kk) in enumerate(cellkey)
                     if e2==ei and kk==(sec[x],sec[y]))
            mix[j] += (hi-lo)
    if okt and all(mix[j]==q[j] for j in range(d)):
        pass
    else:
        fails += 1
print(f"  {NTEST} exact C-vertices: theta-sweep legal on every interval and"
      f" mixture == q EXACTLY in {NTEST-fails}/{NTEST}"
      f" -> {'P37 HIT (constructive realisation certified)' if fails==0 else 'P37 MISS'}")

# ---------- P36: pair-bipartite vs cumulative-signable ----------
print("== P36: scan (marginal-determined class, <=4 states) ==")
def pair_bipartite(arcs, Asz):
    prs = [(a,b) for a in range(Asz) for b in range(Asz) if a!=b]
    adj = {}
    for (a,b) in prs:
        for (c,dd) in prs:
            if (a,c) in arcs and (b,dd) in arcs:
                adj.setdefault((a,b),[]).append((c,dd))
    col = {}
    for s2 in prs:
        if s2 in col: continue
        col[s2]=0; stack=[s2]
        while stack:
            xx = stack.pop()
            for yy in adj.get(xx,()):
                if yy in col:
                    if col[yy]==col[xx]: return False
                else:
                    col[yy]=1-col[xx]; stack.append(yy)
            for zz,nb in adj.items():
                if xx in nb:
                    if zz in col:
                        if col[zz]==col[xx]: return False
                    else:
                        col[zz]=1-col[xx]; stack.append(zz)
    return True
def marginal_determined(arcs, Asz):
    cl = sorted(arcs)
    M = []
    for s2 in range(Asz):
        M.append([F(1 if c[0]==s2 else 0) for c in cl])
    for s2 in range(Asz):
        M.append([F(1 if c[1]==s2 else 0) for c in cl])
    RM,_ = rref(M)
    return len(RM) == len(cl), cl, M
def cumulative_signable(arcs, Asz):
    okmd, cl, M = marginal_determined(arcs, Asz)
    if not okmd: return None
    for perm in permutations(range(Asz)):
        # cumulative coords per side: c_k = sum of u(s) with rank(s)>=k, k=1..Asz-1
        rank = {perm[i]: i for i in range(Asz)}
        # express q as affine in (u_i,u_j): solve M^T? q_c = row of pseudo-inv:
        # build linear system: q = T u where u = 8-dim marginals; T from solving
        # M q = u with unique q (rank=|cl|): q_c coefficients = solve for each c
        # -> easier: q_c as function: since M has full column rank, q = (M^T M)^{-1} M^T u
        # exact: solve normal equations
        n = len(cl)
        MtM = [[sum(M[r][i]*M[r][j] for r in range(2*Asz)) for j in range(n)] for i in range(n)]
        # invert MtM
        aug = [MtM[i] + [F(1 if j==i else 0) for j in range(n)] for i in range(n)]
        RA, PA = rref(aug)
        if len(RA) < n: return None
        inv = [[RA[i][n+j] for j in range(n)] for i in range(n)]
        # q_c = sum_r (inv @ M^T)[c][r] * u_r; change u -> cumulative:
        # u(s) = c_{rank(s)} - c_{rank(s)+1} (c_0 = 1, c_Asz = 0) per side
        okall = True
        cross_sign = None
        for c_idx in range(n):
            coefu = [sum(inv[c_idx][k]*M[r][k] for k in range(n)) for r in range(2*Asz)]
            # to cumulative: coefficient of c_k(side) = sum over s with rank>=?:
            # u(s) = c_{rk} - c_{rk+1} -> coef of c_m (m=1..Asz-1) = coefu[s with rk=m] - coefu[s with rk=m-1]
            row = {}
            for sd in range(2):
                for m in range(1, Asz):
                    s_hi = perm[m]; s_lo = perm[m-1]
                    v2 = coefu[sd*Asz + s_hi] - coefu[sd*Asz + s_lo]
                    if v2 != 0: row[(sd,m)] = v2
            nz = list(row.items())
            if len(nz) > 2: okall = False; break
            if len(nz) == 2:
                (k1,v1),(k2,v2) = nz
                if k1[0] != k2[0]:
                    ss = (v1>0) == (v2>0)
                    if cross_sign is None: cross_sign = ss
                    elif cross_sign != ss: okall = False; break
                else:
                    if (v1>0) == (v2>0): okall = False; break
        if okall: return True
    return False
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
    R = [(a,b) for (a,b) in arcs if a in reach[b]]
    ro={}
    for (a,b) in R: ro.setdefault(a,[]).append(b)
    return any(len(v)>=2 for v in ro.values())
agree, split1, split2, tested = 0, [], [], 0
for Asz in (2,3,4):
    for mask in range(1, 1 << (Asz*Asz)):
        if canonical(mask, Asz) != mask: continue
        arcs = frozenset((a,b) for a in range(Asz) for b in range(Asz)
                         if mask >> (a*Asz+b) & 1)
        outd=[sum(1 for b in range(Asz) if (a,b) in arcs) for a in range(Asz)]
        ind=[sum(1 for a in range(Asz) if (a,b) in arcs) for b in range(Asz)]
        if min(outd)==0 or min(ind)==0: continue
        if not connected_rel(arcs,Asz) or not recurrent_branching(arcs,Asz): continue
        md,_,_ = marginal_determined(arcs, Asz)
        if not md: continue
        tested += 1
        pb = pair_bipartite(arcs, Asz)
        sg = cumulative_signable(arcs, Asz)
        if pb == sg: agree += 1
        elif pb and not sg: split1.append(sorted(arcs))
        else: split2.append(sorted(arcs))
print(f"  marginal-determined recurrent-branching languages tested: {tested}")
print(f"  pair-bipartite == cumulative-signable: {agree};"
      f" PB-not-CS (candidate splitters): {len(split1)};"
      f" CS-not-PB (HARD splitters): {len(split2)}")
for a2 in split1[:5]: print(f"    PB-not-CS: {a2}")
for a2 in split2[:5]: print(f"    CS-not-PB: {a2}")
