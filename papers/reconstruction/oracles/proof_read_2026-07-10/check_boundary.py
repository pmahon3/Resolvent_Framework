"""Boundary-case audit:
1. L=1 with a self-loop: does raw DFS correctly find winding-k cycles collapsed
   onto a single layer (i.e. simple k-cycles in D itself, since R_1(rho) = D
   with a single layer, self-loops allowed by the layer-arc rule (a,b) in rho
   for (0,0) since (0+1) mod 1 = 0)?
2. k=1 remark check: TR_1(L) should equal existence of ANY closed walk of
   length L in D (not necessarily simple in D) -- and the remark claims every
   such walk is automatically simple in R_L. Test with a graph that has a
   non-simple closed walk in D of length L to see if R_L still forces simplicity.
3. k = n (max alphabet size): tuples are permutations of all of A.
4. Empty safe set / totally unsafe example already covered by rho13-like; test
   a fully-unsafe-at-all-L graph (e.g. complete digraph on 2 nodes with self-loops)
"""
from itertools import permutations, product

def raw_LISC_windings(rel, A, L, kmax):
    adj = {}
    for i in range(L):
        for s in range(A):
            adj[(i,s)] = [((i+1)%L, t) for t in range(A) if (s,t) in rel]
    out=set()
    def dfs(start, cur, path, visited):
        for nx in adj[cur]:
            if nx==start and len(path)>=L and len(path)%L==0:
                k=len(path)//L
                if 2<=k<=kmax: out.add(k)
            elif nx not in visited and len(path) < kmax*L:
                visited.add(nx); path.append(nx)
                dfs(start,nx,path,visited)
                path.pop(); visited.discard(nx)
    for s0 in range(A):
        st=(0,s0); dfs(st,st,[st],{st})
    return out

def TR_walk_exists(rel, A, k, r, L):
    tuples = list(permutations(range(A), k))
    outn = {a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    def succs(u):
        return [v for v in product(*(outn[a] for a in u)) if len(set(v))==k]
    def sigma_r(u):
        return tuple(u[(j+r)%k] for j in range(k))
    for u in tuples:
        frontier={u}
        for _ in range(L):
            nxt=set()
            for x in frontier: nxt.update(succs(x))
            frontier=nxt
            if not frontier: break
        if sigma_r(u) in frontier:
            return True
    return False

print("--- TEST 1: L=1 with self-loops present, k up to A ---")
rel = {(0,0),(1,1),(0,1),(1,0)}  # A=2, full digraph w/ self loops
A=2
for L in [1,2,3]:
    raw = raw_LISC_windings(rel, A, L, A)
    print(f"  L={L}: raw LISC windings (k>=2) = {sorted(raw)}")
    for k in range(2, A+1):
        tr = TR_walk_exists(rel, A, k, 1, L)
        print(f"    k={k} TR^(1)={tr}  match={ (k in raw) == tr }")

print()
print("--- TEST 2: k=1 remark. D has a non-simple closed walk (figure-8) ---")
# Node 0 with two loops back via 1 and via 2: 0->1->0 and 0->2->0, closed walk
# 0->1->0->2->0 has length 4 but revisits 0 -- not simple in D.
rel2 = {(0,1),(1,0),(0,2),(2,0)}
A2 = 3
for L in [1,2,3,4]:
    raw = raw_LISC_windings(rel2, A2, L, A2)
    tr1 = TR_walk_exists(rel2, A2, 1, 0, L)  # k=1: r must be 0 mod 1 trivially; sigma_0=id
    print(f"  L={L}: raw(k>=2)={sorted(raw)}  TR_1^(id)(L) [any closed walk len L?] = {tr1}")

print()
print("--- TEST 3: k = n (max alphabet size), full permutation tuples ---")
rel3 = {(0,1),(1,2),(2,0)}  # 3-cycle, A=3, k=3=n
A3=3
for L in [1,2,3,4,5,6]:
    raw = raw_LISC_windings(rel3, A3, L, A3)
    tr = TR_walk_exists(rel3, A3, 3, 1, L)
    print(f"  L={L}: raw={sorted(raw)}  TR_3^(1)={tr}  3 in raw match TR: {(3 in raw)==tr}")

print()
print("--- TEST 4: totally-unsafe-at-every-L (complete digraph incl. self-loops, A=2) ---")
rel4 = {(0,0),(0,1),(1,0),(1,1)}
A4=2
allunsafe = True
for L in range(1,10):
    raw = raw_LISC_windings(rel4, A4, L, A4)
    unsafe = len(raw)>0
    allunsafe &= unsafe
    print(f"  L={L}: unsafe={unsafe} raw={sorted(raw)}")
print("Totally unsafe for L=1..9:", allunsafe)
