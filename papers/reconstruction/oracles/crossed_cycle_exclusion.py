"""
CROSSED-CYCLE EXCLUSION oracle + structure probe (2026-07-10).

Target (L-B easier half): primitive + strongly-connected rho on A states =>
in the ordered-pair digraph D on OFF-DIAGONAL vertices {(a,b): a!=b}, with arcs
(a,b)->(c,d) iff (a,c) in rho and (b,d) in rho, there is a D-path (a,b) ~~> (b,a)
that never touches a diagonal vertex.

Equivalently: primitive => NOT-safe-at-all-L (a crossed cycle exists).

Conventions match parity_only_witness_channel.py:
  rel = set of ordered pairs (s,t) meaning "s can be followed by t".
"""
import itertools, sys
from math import gcd
from collections import deque
sys.setrecursionlimit(10**7)

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

def is_primitive(rel,A):
    return strongly_conn(rel,A) and period(rel,A)==1

# ---- ordered-pair off-diagonal digraph D ----
def D_arcs(rel, A):
    """arcs of D: (a,b)->(c,d), a!=b, c!=d, (a,c) in rel, (b,d) in rel."""
    verts=[(a,b) for a in range(A) for b in range(A) if a!=b]
    adj={v:[] for v in verts}
    for (a,b) in verts:
        for (c,d) in verts:
            if (a,c) in rel and (b,d) in rel:
                adj[(a,b)].append((c,d))
    return verts, adj

def has_crossed_cycle(rel, A):
    """True iff some off-diagonal (a,b) reaches (b,a) in D (never touching diagonal
    because D vertices ARE off-diagonal only)."""
    verts, adj = D_arcs(rel, A)
    # reachability in D from each vertex
    for (a,b) in verts:
        if a<b:  # unordered, test (a,b) ~~> (b,a)
            seen={(a,b)}; st=[(a,b)]
            while st:
                x=st.pop()
                for y in adj[x]:
                    if y not in seen: seen.add(y); st.append(y)
            if (b,a) in seen:
                return True
    return False

# ---- LISC-based ground truth: safe at all L? ----
def lisc2_raw(rel,A,L):
    adj={(i,s):[((i+1)%L,t) for t in range(A) if (s,t) in rel] for i in range(L) for s in range(A)}
    lc=[0]*L
    def dfs(start,cur,steps,vis):
        if steps==2*L: return cur==start
        for nx in adj[cur]:
            ni,ns=nx
            if nx==start and steps+1==2*L: return True
            if nx not in vis and lc[ni]<2:
                vis.add(nx);lc[ni]+=1
                if dfs(start,nx,steps+1,vis): lc[ni]-=1;vis.discard(nx);return True
                lc[ni]-=1;vis.discard(nx)
        return False
    for s0 in range(A):
        lc[0]=1
        if dfs((0,s0),(0,s0),0,{(0,s0)}): lc[0]=0;return True
        lc[0]=0
    return False

def not_safe_at_all_L(rel,A,Lmax=16):
    """True iff UNSAFE at some L in [3,Lmax] (i.e. NOT safe at all L, up to Lmax)."""
    return any(lisc2_raw(rel,A,L) for L in range(3,Lmax+1))

# ---- VERIFY: has_crossed_cycle <=> not_safe_at_all_L on primitives ----
def verify(A, Lmax=16):
    allp=[(a,b) for a in range(A) for b in range(A)]
    n=0; mism=0; examples=[]
    subsets=itertools.chain.from_iterable(
        itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    for combo in subsets:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        n+=1
        cc = has_crossed_cycle(rel,A)
        # for primitives, cc should always be True (that's the theorem);
        # for imprimitives, cc <=> not-safe-at-all is the general reframe.
        prim = period(rel,A)==1
        if prim and not cc:
            mism+=1
            examples.append(('PRIM-NO-CC', sorted(rel)))
    return n, mism, examples

if __name__=="__main__":
    A=int(sys.argv[1]) if len(sys.argv)>1 else 3
    n,mism,ex=verify(A)
    print(f"A={A}: {n} strongly-conn total langs scanned")
    print(f"  PRIMITIVE with NO crossed cycle (should be 0): {mism}")
    for tag,rel in ex[:10]:
        print(f"    {tag}: {rel}")
    print("DONE")
