"""
MECHANISM probe for crossed-cycle exclusion (2026-07-10).

Goal: find the structural reason primitive+s.c. => a swap-path in D avoids diagonal.

Key idea to test: consider the D-reachability relation on off-diagonal pairs.
"No crossed cycle" means: for EVERY off-diagonal {a,b}, (a,b) does NOT reach (b,a)
in D. Define an equivalence-ish structure: partition off-diagonal ordered pairs by
D-reachability. If (a,b) never reaches (b,a), then the "orientation" of a pair is a
D-invariant. Test: is there a consistent 2-colouring / potential that D-arcs preserve
when no crossed cycle exists? That colouring would be an imprimitivity obstruction.

Specifically: suppose NO crossed cycle. Then reachability in D gives a preorder where
(a,b) and (b,a) are in different classes for all a!=b. Conjecture: this yields a
Z_2-grading (a "sign"/order function) on states forcing rho imprimitive.
"""
import itertools, sys
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
    from math import gcd
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

def D_reach(rel, A):
    """Return dict: for each off-diag vertex, set of off-diag vertices reachable in D."""
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
    return verts, adj, reach

def crossed(rel,A):
    verts,adj,reach=D_reach(rel,A)
    for (a,b) in verts:
        if (b,a) in reach[(a,b)]:
            return True, (a,b)
    return False, None

def analyze_no_cross(rel, A):
    """For a language with NO crossed cycle, probe the invariant structure."""
    verts,adj,reach=D_reach(rel,A)
    # Build the 'order-consistency' graph: try to 2-colour ordered pairs so that
    # D-arcs preserve colour and (a,b),(b,a) get opposite colours.
    # If no crossed cycle, reachability classes are consistent with an orientation.
    # Try: assign to each off-diag pair a value in {+1,-1} with sign(a,b)=-sign(b,a)
    # and D-arcs preserve sign. Solvable iff no odd frustration.
    sign={}
    ok=True
    for start in verts:
        if start in sign: continue
        sign[start]=+1
        dq=deque([start])
        while dq:
            x=dq.popleft()
            # x and swap(x) opposite
            sw=(x[1],x[0])
            if sw in sign:
                if sign[sw]!=-sign[x]: ok=False
            else:
                sign[sw]=-sign[x]; dq.append(sw)
            # D-arcs preserve sign (same reachability orientation)
            for y in adj[x]:
                if y in sign:
                    if sign[y]!=sign[x]: ok=False
                else:
                    sign[y]=sign[x]; dq.append(y)
    return ok, sign

if __name__=="__main__":
    A=int(sys.argv[1]) if len(sys.argv)>1 else 3
    allp=[(a,b) for a in range(A) for b in range(A)]
    n_nocross=0; n_prim_nocross=0
    subsets=itertools.chain.from_iterable(
        itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    for combo in subsets:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        has,_=crossed(rel,A)
        if not has:
            n_nocross+=1
            prim = period(rel,A)==1
            if prim: n_prim_nocross+=1
            ok,sign=analyze_no_cross(rel,A)
            print(f"NO-CROSS rel={sorted(rel)} prim={prim} period={period(rel,A)} sign_consistent={ok}")
    print(f"A={A}: no-cross langs={n_nocross}, of which primitive={n_prim_nocross}")
