"""Directly test Lemma NG's claim: for gcd(r,k)=d>1, does TR_k^(r)(L) hold
while LISC_k(L) fails, and does the TR witness decompose into d disjoint
cycles of winding k/d?  Test beyond C4dir: try several non-generator (r,k)
pairs on adversarial targets, including multi-component graphs."""
from itertools import permutations, product
from math import gcd

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

TARGETS = {
    "C4dir": ({(0,1),(1,2),(2,3),(3,0)}, 4),
    "C6dir": ({(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)}, 6),
    "two_disjoint_3cycles": ({(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)}, 6),
    "C8dir": ({(i,(i+1)%8) for i in range(8)}, 8),
}

for name,(rel,A) in TARGETS.items():
    print(f"=== {name} (A={A}) ===")
    for L in range(1,9):
        raw = raw_LISC_windings(rel,A,L,A)
        for k in range(2, A+1):
            for r in range(1,k):
                d = gcd(r,k)
                if d==1: continue  # generator case tested elsewhere
                tr = TR_walk_exists(rel,A,k,r,L)
                if tr:
                    liskk = k in raw
                    lisc_kd = (k//d) in raw
                    print(f"  L={L} k={k} r={r} d={d}: TR^(r)_k={tr}  "
                          f"LISC_k(actual)={liskk}  LISC_(k/d)={lisc_kd}  "
                          f"NG-predicts: TR fires, LISC_k need not hold, LISC_(k/d) should hold")
