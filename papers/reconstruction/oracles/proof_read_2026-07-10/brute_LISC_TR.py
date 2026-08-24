"""Independent from-scratch brute force (not copied from the instrument):
 - LISC_k(L): does R_L(rho) have a simple cycle of winding k?
 - TR_k^(r)(L): does T_k(rho) have a walk of length L from some u to sigma_r(u)?
Cross check Theorem P (r with gcd(r,k)=1 => LISC_k(L) <=> TR_k^r(L))
and Lemma NG (gcd(r,k)=d>1: TR fires but need not mean LISC_k; decomposes to d
cycles of winding k/d).
"""
from itertools import permutations, product
from math import gcd

def raw_LISC_windings(rel, A, L, kmax):
    # independent simple implementation: DFS on ring digraph for simple cycles
    adj = {}
    for i in range(L):
        for s in range(A):
            adj[(i,s)] = [((i+1)%L, t) for t in range(A) if (s,t) in rel]
    out = set()
    def dfs(start, cur, path, visited):
        for nx in adj[cur]:
            if nx == start and len(path) >= L and len(path) % L == 0:
                k = len(path)//L
                if 2 <= k <= kmax:
                    out.add(k)
            elif nx not in visited and len(path) < kmax*L:
                visited.add(nx); path.append(nx)
                dfs(start, nx, path, visited)
                path.pop(); visited.discard(nx)
    for s0 in range(A):
        st=(0,s0)
        dfs(st, st, [st], {st})
    return out

def TR_walk_exists(rel, A, k, r, L):
    """Does T_k have a walk of length L from some u to sigma_r(u)?"""
    tuples = list(permutations(range(A), k))
    outn = {a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    def succs(u):
        res=[]
        for v in product(*(outn[a] for a in u)):
            if len(set(v))==k:
                res.append(v)
        return res
    def sigma_r(u):
        return tuple(u[(j+r)%k] for j in range(k))
    # BFS layer by layer over all tuples simultaneously (frontier per start)
    # Do it per start u (small state spaces in these tests)
    for u in tuples:
        frontier = {u}
        for _ in range(L):
            nxt=set()
            for x in frontier:
                nxt.update(succs(x))
            frontier = nxt
            if not frontier:
                break
        if sigma_r(u) in frontier:
            return True
    return False

def LISC_all_k_windings_via_TR(rel, A, L, r_map):
    """for each k use given r (must be coprime to k) -> should equal raw LISC"""
    out=set()
    for k in range(2, A+1):
        r = r_map(k)
        if gcd(r,k)!=1:
            continue
        if TR_walk_exists(rel, A, k, r, L):
            out.add(k)
    return out

# Targets: adversarial disconnected / non-SC multi-component graphs NOT in the 15
TARGETS = {
    "two_disjoint_2cycles": ({(0,1),(1,0),(2,3),(3,2)}, 4),   # A=4, two 2-cycles, not SC
    "3cyc_plus_isolated_selfloop_free": ({(0,1),(1,2),(2,0)}, 3),  # A=3 pure 3-cycle (isolated from nothing but small)
    "2cyc_join_4cyc_disjoint": ({(0,1),(1,0),(2,3),(3,4),(4,5),(5,2)}, 6),  # A=6: 2-cycle sqcup 4-cycle
    "star_plus_2cycle_no_SC": ({(0,1),(1,0),(2,3),(3,2),(0,2)}, 4),  # 2-cycle + 2-cycle + bridge arc (still not SC as whole since no return 2->0)
    "three_disjoint_2cycles": ({(0,1),(1,0),(2,3),(3,2),(4,5),(5,4)}, 6),
    "4cycle_and_3cycle_disjoint": ({(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,4)}, 7),
}

for name, (rel, A) in TARGETS.items():
    print(f"=== {name} (A={A}) ===")
    for L in range(1, 9):
        raw = raw_LISC_windings(rel, A, L, A)
        # rotation-by-generator (r=1) prediction
        via_r1 = LISC_all_k_windings_via_TR(rel, A, L, lambda k: 1)
        match = (raw == via_r1)
        flag = "" if match else "  <<<< MISMATCH"
        print(f"  L={L}: raw={sorted(raw)} TRr1={sorted(via_r1)}{flag}")
