"""
Test the GRADING mechanism for no-crossed-cycle (2026-07-10).

Empirical: no-cross => imprimitive, odd period d>=3, consistent sign on off-diag pairs.

Conjecture to test: rho has NO crossed cycle  <=>  rho admits a Z_d grading
g: states -> Z_d (d>=2, arcs advance g by exactly +1) such that d is ODD, i.e.
the transfer digraph fibers over an ODD cycle.

WHY this would obstruct a crossed cycle: a D-path (a,b)~~>(c,d) advances BOTH
coordinates' grading by the same amount k (each step +1). So g(c)-g(a)=g(d)-g(b)=k,
hence g(c)-g(d) = g(a)-g(b) is INVARIANT along D. A swap (a,b)->(b,a) needs
g(b)-g(a) = g(a)-g(b) mod d, i.e. 2(g(a)-g(b))=0 mod d. If a,b off-diagonal we can
have g(a)=g(b) (then invariant=0, swap allowed IF reachable) OR g(a)!=g(b). For d
ODD, 2x=0 mod d => x=0 => g(a)=g(b). So a swap can ONLY connect pairs with g(a)=g(b).
Among SAME-GRADE off-diagonal pairs the obstruction is subtler.

So grading alone (odd d) does NOT immediately forbid all swaps -- only cross-grade
ones. Need to look harder. Test the actual characterization first.
"""
import itertools, sys
from math import gcd
from collections import deque

def strongly_conn(rel, A):
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    inn={a:[b for b in range(A) if (b,a) in rel] for a in range(A)}
    def rch(s,g):
        seen={s};st=[s]
        while st:
            x=st.pop()
            for y in g[x]:
                if y not in seen: seen.add(y);st.append(y)
        return seen
    return rch(0,out)==set(range(A)) and rch(0,inn)==set(range(A))

def period(rel,A):
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    lvl={0:0}; dq=deque([0])
    while dq:
        x=dq.popleft()
        for y in out[x]:
            if y not in lvl: lvl[y]=lvl[x]+1; dq.append(y)
    g=0
    for a in range(A):
        for b in out[a]: g=gcd(g,abs(lvl[a]+1-lvl[b]))
    return g if g>0 else 1

def grading(rel,A):
    """Return the Z_d grading g (d=period): g(state)=BFS level mod d. Well-defined
    because arcs advance level by +1 mod d for strongly-conn digraph of period d."""
    d=period(rel,A)
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    lvl={0:0}; dq=deque([0])
    while dq:
        x=dq.popleft()
        for y in out[x]:
            if y not in lvl: lvl[y]=lvl[x]+1; dq.append(y)
    return {s:lvl[s]%d for s in range(A)}, d

def is_total(rel,A):
    outs={a for (a,b) in rel}; ins={b for (a,b) in rel}
    return outs==set(range(A)) and ins==set(range(A))

def D_reach(rel, A):
    verts=[(a,b) for a in range(A) for b in range(A) if a!=b]
    adj={v:[] for v in verts}
    for (a,b) in verts:
        for (c,d) in verts:
            if (a,c) in rel and (b,d) in rel:
                adj[(a,b)].append((c,d))
    reach={}
    for v in verts:
        seen={v};st=[v]
        while st:
            x=st.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y);st.append(y)
        reach[v]=seen
    return reach

def crossed(rel,A):
    reach=D_reach(rel,A)
    for (a,b) in [(a,b) for a in range(A) for b in range(A) if a!=b]:
        if (b,a) in reach[(a,b)]:
            return True
    return False

if __name__=="__main__":
    A=int(sys.argv[1]) if len(sys.argv)>1 else 4
    allp=[(a,b) for a in range(A) for b in range(A)]
    subs=itertools.chain.from_iterable(itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    for combo in subs:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        if crossed(rel,A): continue
        g,d=grading(rel,A)
        # check: for the SWAP obstruction, look at same-grade off-diagonal pairs.
        samegrade=[(a,b) for a in range(A) for b in range(A) if a!=b and g[a]==g[b]]
        print(f"rel={sorted(rel)} period d={d} grading={g}")
        print(f"   #same-grade off-diag pairs={len(samegrade)}: {samegrade}")
