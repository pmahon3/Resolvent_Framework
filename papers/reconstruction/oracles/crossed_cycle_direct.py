"""
DIRECT attack: primitive => crossed cycle (2026-07-10).

The Kronecker lever: rho primitive => rho x rho is primitive on ALL A^2 ordered
pairs => (a,b) reaches (b,a) in the FULL product for every a,b. Content = avoid
the diagonal Delta = {(x,x)}.

STRATEGY (potential/grading argument, run in reverse):
Suppose NO off-diagonal (a,b) reaches (b,a) within D (off-diagonal digraph).
Define a relation on off-diagonal unordered pairs. Claim this forces a Z_d grading
with d ODD >= 3, hence rho IMPRIMITIVE. Contrapositive gives the theorem.

Here we test the KEY LEMMA that would drive a clean proof:

  LEMMA (candidate): If rho is primitive then for SOME state x, and some a!=b,
  there are rho-walks a->...->b and b->...->a of the SAME length that are
  vertex-disjoint AT EVERY LAYER (never simultaneously at the same state) and
  return swapped. Equivalently D has a path (a,b)~~>(b,a).

Test a sharper sufficient condition that primitivity supplies:
  If rho has TWO distinct states u,v with a common out-neighbor OR common
  in-neighbor (a 'fork'/'merge' = the primitivity signature beyond a permutation),
  can we route a swap avoiding the diagonal?
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

def D_reach_from(rel, A, start):
    adj={}
    verts=[(a,b) for a in range(A) for b in range(A) if a!=b]
    for (a,b) in verts:
        adj[(a,b)]=[(c,d) for c in range(A) for d in range(A)
                    if c!=d and (a,c) in rel and (b,d) in rel]
    seen={start};st=[start]
    while st:
        x=st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y);st.append(y)
    return seen

def crossed(rel,A):
    for (a,b) in [(a,b) for a in range(A) for b in range(A) if a<b]:
        if (b,a) in D_reach_from(rel,A,(a,b)):
            return True
    return False

def has_fork_or_merge(rel,A):
    """A fork: state with out-degree>=2. A merge: state with in-degree>=2.
    A pure permutation has neither. Primitive with >1 state has at least one."""
    outdeg={a:0 for a in range(A)}; indeg={a:0 for a in range(A)}
    for (a,b) in rel: outdeg[a]+=1; indeg[b]+=1
    fork=any(v>=2 for v in outdeg.values())
    merge=any(v>=2 for v in indeg.values())
    return fork, merge

if __name__=="__main__":
    A=int(sys.argv[1]) if len(sys.argv)>1 else 4
    allp=[(a,b) for a in range(A) for b in range(A)]
    subs=itertools.chain.from_iterable(itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    # For NO-CROSS languages: do they have a fork/merge? (permutations have none)
    print("=== NO-CROSS languages: fork/merge structure ===")
    for combo in subs:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        if crossed(rel,A): continue
        fork,merge=has_fork_or_merge(rel,A)
        d=period(rel,A)
        print(f"  rel={sorted(rel)} period={d} fork={fork} merge={merge}")
