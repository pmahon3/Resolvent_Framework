"""
Push the 6 primitive candidates deep: is their safe set FINITE (Wielandt holds,
they go cofinitely unsafe) or genuinely RICH (a fork)? The conjecture needs
rich-safe = safe at a set covering all circuit-lengths of a K4-minor frame
simultaneously; a finite sparse safe set (e.g. {3,4,7} then unsafe forever) is
NOT rich-safe and is consistent with the conjecture.
"""
import signal
from math import gcd

def digraph_period(rel, A):
    out = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    inn = {a: [b for b in range(A) if (b, a) in rel] for a in range(A)}
    def reach(start, g):
        seen={start}; st=[start]
        while st:
            x=st.pop()
            for y in g[x]:
                if y not in seen: seen.add(y); st.append(y)
        return seen
    if reach(0,out)!=set(range(A)) or reach(0,inn)!=set(range(A)): return 0
    from collections import deque
    level={0:0}; dq=deque([0])
    while dq:
        x=dq.popleft()
        for y in out[x]:
            if y not in level: level[y]=level[x]+1; dq.append(y)
    g=0
    for a in range(A):
        for b in out[a]: g=gcd(g,abs(level[a]+1-level[b]))
    return g if g>0 else 1

def lisc2_raw(rel, A, L):
    adj = {(i, s): [((i + 1) % L, t) for t in range(A) if (s, t) in rel]
           for i in range(L) for s in range(A)}
    lc = [0] * L
    import sys; sys.setrecursionlimit(10**7)
    def dfs(start, cur, steps, vis):
        if steps == 2 * L: return cur == start
        for nx in adj[cur]:
            ni, ns = nx
            if nx == start and steps + 1 == 2 * L: return True
            if nx not in vis and lc[ni] < 2:
                vis.add(nx); lc[ni] += 1
                if dfs(start, nx, steps + 1, vis): lc[ni]-=1; vis.discard(nx); return True
                lc[ni] -= 1; vis.discard(nx)
        return False
    for s0 in range(A):
        lc[0] = 1
        if dfs((0, s0), (0, s0), 0, {(0, s0)}): lc[0] = 0; return True
        lc[0] = 0
    return False

class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM, handler)

candidates = [
    [(0,0),(0,1),(1,2),(2,0)],
    [(0,1),(1,1),(1,2),(2,0)],
    [(0,0),(0,2),(1,0),(2,1)],
    [(0,1),(1,2),(2,0),(2,2)],
]
Lmax = 30
print(f"Pushing primitive candidates to L={Lmax}. safe-length list + last-safe.")
for rel in candidates:
    rel = frozenset(rel); A = 1 + max(max(a,b) for (a,b) in rel)
    p = digraph_period(rel, A)
    safe = []
    maxdone = 2
    for L in range(3, Lmax+1):
        signal.alarm(15)
        try:
            unsafe = lisc2_raw(rel, A, L); signal.alarm(0)
        except TO:
            signal.alarm(0); print(f"  rel={sorted(rel)} NOT-COMPUTED past L={maxdone}"); break
        maxdone = L
        if not unsafe: safe.append(L)
    last_safe = safe[-1] if safe else None
    # heuristic: if safe set stops early relative to maxdone, it's finite (Wielandt holds)
    verdict = "FINITE safe set (Wielandt holds)" if (last_safe and last_safe < maxdone - 5) else "STILL SAFE deep -> investigate"
    print(f"  period={p} rel={sorted(rel)}")
    print(f"    safe@{safe}  (computed to L={maxdone}) last-safe={last_safe} -> {verdict}")
