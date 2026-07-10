"""
The POTENTIAL / GRADING argument for no-crossed-cycle => imprimitive (2026-07-10).

CLAIM being tested: no crossed cycle => there is a Z-valued (mod d, d>=2) grading
g on states with every arc advancing g by +1, AND d ODD.

But primitive means d=1 (only trivial grading). So if 'no crossed cycle' FORCED a
nontrivial grading, primitivity would be contradicted. The mechanism:

Build a candidate potential DIRECTLY from D-reachability, WITHOUT assuming period.
For off-diagonal ordered pairs, define an integer 'twist' and show no-cross makes it
consistent, yielding a grading.

CONCRETE construction to test:
Fix a spanning structure of rho (strongly connected). Assign g(0)=0. For each state
s, g(s) := (length of some fixed walk 0->s) mod d, for the RIGHT d. The period d is
the gcd of cycle lengths. Claim: no-cross forces a FINER invariant.

Actually the clean test: no-cross <=> the "swap parity cover" D->Dbar is a TRIVIAL
(disconnected) double cover on every SCC of Dbar. Let's compute that directly and
also test: does no-cross <=> rho admits an assignment h: states -> {orientations}
consistent with a linear/cyclic order that arcs rotate by a fixed ODD step.
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

def is_total(rel,A):
    outs={a for (a,b) in rel}; ins={b for (a,b) in rel}
    return outs==set(range(A)) and ins==set(range(A))

def D_adj(rel,A):
    verts=[(a,b) for a in range(A) for b in range(A) if a!=b]
    adj={(a,b):[(c,d) for c in range(A) for d in range(A)
                if c!=d and (a,c) in rel and (b,d) in rel] for (a,b) in verts}
    return verts,adj

def crossed(rel,A):
    verts,adj=D_adj(rel,A)
    for (a,b) in verts:
        if a<b:
            seen={(a,b)};st=[(a,b)]
            while st:
                x=st.pop()
                for y in adj[x]:
                    if y not in seen: seen.add(y);st.append(y)
            if (b,a) in seen: return True
    return False

def sigma_cover_trivial(rel,A):
    """Dbar = unordered off-diag pairs. sigma-cover D->Dbar. The cover over an SCC
    of Dbar is trivial (disconnected) iff no (a,b) reaches (b,a). Compute: for each
    unordered {a,b}, are (a,b),(b,a) in the SAME D-SCC? no-cross <=> never."""
    verts,adj=D_adj(rel,A)
    # SCC via Tarjan-ish (small graphs: use reachability both ways)
    def reach(s):
        seen={s};st=[s]
        while st:
            x=st.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y);st.append(y)
        return seen
    R={v:reach(v) for v in verts}
    same_scc=[]
    for (a,b) in verts:
        if a<b:
            if (b,a) in R[(a,b)] and (a,b) in R[(b,a)]:
                same_scc.append((a,b))
    return same_scc  # empty <=> trivial cover on all SCCs relevant

if __name__=="__main__":
    A=int(sys.argv[1]) if len(sys.argv)>1 else 4
    allp=[(a,b) for a in range(A) for b in range(A)]
    subs=itertools.chain.from_iterable(itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    print("Testing: for NO-CROSS langs, period vs a candidate grading obstruction")
    for combo in subs:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        if crossed(rel,A): continue
        d=period(rel,A)
        # Verify d is odd and >=3 for every no-cross lang (the empirical pattern)
        assert d>=2, f"no-cross but period 1! {sorted(rel)}"
        print(f"  rel={sorted(rel)} period={d} odd={d%2==1}")
    print("DONE (assertion 'no-cross => period>=2' held for all above)")
