"""P34/P35: rho5 on 2-subdivided K4 and K5 (2026-07-09).

rho5 = {(0,1),(0,2),(1,0),(1,1),(2,0)} — the first fork candidate to survive
hand autopsy: pair digraph natively bipartite (level-one autonomy witness),
base aperiodic with odd cycles, entropy root of x^3 = x^2 + 2x - 1.

P34: 2-subdivided K4 (10v, 12e) — taming-#7 test; predicted SAFE.
P35: 2-subdivided K5 (15v, 20e) — THE decisive one: bipartite, all circuits
     even (all in Safe(rho5)), K5 minor intact = the Barahona-Mahjoub
     boundary. Taming #7 predicts safe; minor theory has room for the first
     time. Method (P32-validated at this scale): exact EA rank (dim C) +
     LOCAL-matching rank (gate) + dim R + exact LP maxima over C vs R on all
     coordinate directions and random integer directions. Any mismatch =
     UNSAFE witness direction (pre-declared autopsy applies); full agreement
     + dim equality = SAFE at sampling grade (facet pass infeasible; the
     taming-#7 proof is the certification path — scope declared).
"""
import sys, random
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import rref, simplex_max

RHO5 = {(0,1),(0,2),(1,0),(1,1),(2,0)}
A = 3

# ---------- hand-fact verification ----------
print("== rho5 hand-fact verification ==")
pairs = [(a,b) for a in range(A) for b in range(A) if a != b]
parcs = [((a,b),(c,d)) for (a,b) in pairs for (c,d) in pairs
         if (a,c) in RHO5 and (b,d) in RHO5]
print(f"  off-diagonal pairs: {len(pairs)}; pair arcs: {len(parcs)}")
col, ok = {}, True
for s in pairs:
    if s in col: continue
    col[s] = 0; stack = [s]
    while stack:
        x = stack.pop()
        for (u,v) in parcs:
            for (p,q2) in ((u,v),(v,u)):
                if p == x:
                    if q2 in col:
                        if col[q2] == col[x]: ok = False
                    else:
                        col[q2] = 1 - col[x]; stack.append(q2)
swap_opp = all((a,b) not in col or (b,a) not in col or col[(a,b)] != col[(b,a)]
               for (a,b) in pairs)
print(f"  pair digraph bipartite: {ok}; swap-pairs in opposite classes: {swap_opp}")
trips = [t for t in product(range(A),repeat=3) if len(set(t))==3]
tarcs = {t: [tp for tp in trips if all((t[i],tp[i]) in RHO5 for i in range(3))]
         for t in trips}
n2cyc = sum(1 for t in trips for tp in tarcs[t] if t in tarcs[tp]) // 2
rot = any(t[1:]+t[:1] in tarcs[t] for t in trips)
print(f"  triple dynamics: {len(trips)} tuples, {sum(len(v) for v in tarcs.values())}"
      f" arcs, {n2cyc} two-cycles, direct rotations exist: {rot}")
lam = 1.8
for _ in range(80): lam = (lam**2 + 2*lam - 1)**(1/3)
print(f"  entropy: lambda = {lam:.6f}; lambda^3-lambda^2-2lambda+1 ="
      f" {lam**3-lam**2-2*lam+1:.2e} (root confirmed, != golden ratio)")

# ---------- structure machinery ----------
def subdivided(K):
    verts = K
    edges = []
    for (u,v) in combinations(range(K), 2):
        m = verts; verts += 1
        edges += [(u,m),(m,v)]
    return verts, edges

def homs(nv, edges):
    adj = {}
    for (x,y) in edges:
        adj.setdefault(x, []).append((y, True))
        adj.setdefault(y, []).append((x, False))
    V = []
    assign = [None]*nv
    def bt(i):
        if i == nv:
            V.append(tuple(assign)); return
        for s in range(A):
            good = True
            for (w, fwd) in adj.get(i, ()):
                if assign[w] is not None:
                    pr = (s, assign[w]) if fwd else (assign[w], s)
                    if pr not in RHO5: good = False; break
            if good:
                assign[i] = s; bt(i+1); assign[i] = None
    bt(0)
    return V

def analyze(K, label, ndirs):
    nv, edges = subdivided(K)
    V = homs(nv, edges)
    print(f"  {label}: |V| = {len(V)}")
    cells, ctx_of, cellkey = [], [], []
    for ei,(x,y) in enumerate(edges):
        bucket = {}
        for i,p in enumerate(V):
            bucket[(p[x],p[y])] = bucket.get((p[x],p[y]), 0) | (1 << i)
        for kk, bm in bucket.items():
            cells.append(bm); ctx_of.append(ei); cellkey.append((ei,kk))
    d = len(cells)
    E, fvec = [], []
    for ei in range(len(edges)):
        E.append([F(1) if ctx_of[j]==ei else F(0) for j in range(d)]); fvec.append(F(1))
    for e1, e2 in combinations(range(len(edges)), 2):
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
        blocks = {}
        for j in ids: blocks.setdefault(find(j), []).append(j)
        for blk in blocks.values():
            row = [F(0)]*d
            for j in blk:
                row[j] = F(1) if ctx_of[j]==e1 else F(-1)
            if any(x!=0 for x in row):
                E.append(row); fvec.append(F(0))
    Rr, Rp = rref([r+[v] for r,v in zip(E,fvec)])
    dimC = d - len(Rr)
    # gate: vertex-marginal matching (LOCAL) system
    L2, f2 = [], []
    for ei in range(len(edges)):
        L2.append([F(1) if ctx_of[j]==ei else F(0) for j in range(d)]); f2.append(F(1))
    incid = {}
    for ei,(x,y) in enumerate(edges):
        incid.setdefault(x, []).append((ei,0)); incid.setdefault(y, []).append((ei,1))
    for v, lst in incid.items():
        (e0,s0) = lst[0]
        for (e1,s1) in lst[1:]:
            for st in range(A):
                row = [F(0)]*d
                for j,(ei,kk) in enumerate(cellkey):
                    if ei == e0 and kk[s0] == st: row[j] += 1
                    if ei == e1 and kk[s1] == st: row[j] -= 1
                if any(x!=0 for x in row):
                    L2.append(row); f2.append(F(0))
    Rr2, _ = rref([r+[v] for r,v in zip(L2,f2)])
    Rr12, _ = rref([r+[v] for r,v in zip(E,fvec)]
                   + [r+[v] for r,v in zip(L2,f2)])
    gate = (len(Rr) == len(Rr2) == len(Rr12))
    cell_of = {ck: j for j, ck in enumerate(cellkey)}
    phis = [tuple(cell_of[(ei,(p[x],p[y]))] for ei,(x,y) in enumerate(edges))
            for p in V]
    base = phis[0]
    pivots = []
    dimR = 0
    for phi in phis[1:]:
        row = {}
        for c0, c1 in zip(base, phi):
            if c0 != c1:
                row[c1] = row.get(c1, F(0)) + 1
                row[c0] = row.get(c0, F(0)) - 1
        for (lc, prow) in pivots:
            if row.get(lc):
                coef = row[lc]
                for k2, v2 in prow.items():
                    row[k2] = row.get(k2, F(0)) - coef*v2
        row = {k2:v2 for k2,v2 in row.items() if v2 != 0}
        if row:
            lc = min(row)
            inv = 1/row[lc]
            pivots.append((lc, {k2: v2*inv for k2,v2 in row.items()}))
            dimR += 1
    print(f"    d = {d}; dim C = {dimC}; gate (EA rank == LOCAL rank == joint):"
          f" {gate}; dim R = {dimR}")
    if dimC != dimR:
        print("    dim C > dim R -> UNSAFE (hull-equation witness exists)")
        return False
    Erref = [r[:-1] for r in Rr]; frref = [r[-1] for r in Rr]
    random.seed(35)
    dirs = []
    for j in range(d):
        e = [F(0)]*d; e[j] = F(1); dirs.append(e)
    for _ in range(ndirs):
        dirs.append([F(random.randint(-3,3)) for _ in range(d)])
    mism = 0
    for t, c_obj in enumerate(dirs):
        st, val, _ = simplex_max(c_obj, Erref, frref, [], [])
        assert st == 'optimal', st
        best = max(sum(c_obj[j] for j in phi) for phi in phis)
        if val != best:
            mism += 1
            if mism == 1:
                print(f"    FIRST MISMATCH (direction {t}): max_C = {val} >"
                      f" max_R = {best} -> UNSAFE WITNESS")
    print(f"    exact LPs: {len(dirs)} directions ({d} coordinate + {ndirs}"
          f" random): mismatches = {mism}")
    return mism == 0

print("== P34: rho5 on 2-subdivided K4 ==")
ok34 = analyze(4, "subdiv-K4", 60)
print("  P34:", "HIT (safe at sampling grade)" if ok34 else "MISS — UNSAFE")
print("== P35: rho5 on 2-subdivided K5 (THE decisive one) ==")
ok35 = analyze(5, "subdiv-K5", 100)
print("  P35:", "SAFE at sampling grade — taming-#7 proof attempt LICENSED"
      if ok35 else "UNSAFE — THE FORK: minor-type frustration exists;"
      " pre-declared autopsy applies")
