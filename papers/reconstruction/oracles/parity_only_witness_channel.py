"""
WITNESS CHANNEL for the parity-only target (advisor-directed, 2026-07-09).

The non-circular question (NOT elimination-over-carrier-list, which is circular
with UI): among PRIMITIVE languages with an INFINITE safe set, is the safe set
always "all even L via bipartite layered ring"?

METHOD: enumerate primitive strongly-connected total languages, compute the ACTUAL
safe set via the trusted LISC (winding-2) oracle with NO pre-filter on d. Then
classify the residue structure of the safe set directly. Surface — do not filter —
the two refuters:
  (R1) primitive safe on d*Z with d != 2  (a non-parity residue carrier);
  (R2) primitive safe on 2Z whose LAYERED RING is NOT bipartite at the safe evens
       (parity carrier absent — safety from something else).

If every primitive infinite-safe language is (R1)-free and (R2)-free, the safe set
= evens-and-bipartite = parity, and parity-only holds empirically at this scale.
A hit on R1 or R2 is the missing taming / fork.

Oracle = lisc2_raw (safe at L  <=>  no layer-injective simple cycle of winding 2).
Same oracle prior sessions trusted; scope = winding-2 (the operative proxy).
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

def is_symmetric(rel):
    return all((b,a) in rel for (a,b) in rel)

def is_total(rel,A):
    outs={a for (a,b) in rel}; ins={b for (a,b) in rel}
    return outs==set(range(A)) and ins==set(range(A))

def lisc2_raw(rel,A,L):
    """True = UNSAFE at L (a winding-2 layer-injective simple cycle exists)."""
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

def safe_at(rel,A,L):
    return not lisc2_raw(rel,A,L)

def layered_ring_bipartite(rel,A,L):
    """Is the layered ring over Z_L bipartite? Vertices (i,s), arcs (i,s)->(i+1,t)
    for (s,t) in rel. 2-colour by BFS; return True iff no odd closed walk."""
    col={}
    verts=[(i,s) for i in range(L) for s in range(A)]
    adj={}
    for i in range(L):
        for s in range(A):
            adj[(i,s)]=[((i+1)%L,t) for t in range(A) if (s,t) in rel]
    # treat as UNDIRECTED for bipartiteness of the layered graph
    uadj={v:set() for v in verts}
    for v in verts:
        for w in adj[v]:
            uadj[v].add(w); uadj[w].add(v)
    for s0 in verts:
        if s0 in col: continue
        col[s0]=0; dq=deque([s0])
        while dq:
            x=dq.popleft()
            for y in uadj[x]:
                if y in col:
                    if col[y]==col[x]: return False
                else:
                    col[y]=1-col[x]; dq.append(y)
    return True

def residue_signature(safe_set, Lmax):
    """Given the set of safe L in [3,Lmax], describe its residue structure.
    Return (d, pattern) where d is the smallest modulus s.t. safe-status is
    eventually periodic mod d, and pattern = the safe residues mod d (tail)."""
    Ls=list(range(3,Lmax+1))
    for d in range(2, Lmax//2+1):
        # check: for L large enough, safe(L) depends only on L mod d
        ok=True; tail_start=d*2  # skip small artifact window
        resmap={}
        for L in Ls:
            if L<tail_start: continue
            r=L%d
            v=(L in safe_set)
            if r in resmap and resmap[r]!=v: ok=False; break
            resmap[r]=v
        if ok:
            safe_res=sorted(r for r,v in resmap.items() if v)
            return d, safe_res
    return None, None

# ---- ENUMERATE primitive strongly-conn total languages, no d pre-filter ----
def run(A, Lmax):
    allp=[(a,b) for a in range(A) for b in range(A)]
    seen_iso=set()  # crude dedup by sorted rel
    n_prim=0; infinite_safe=[]; refuters_R1=[]; refuters_R2=[]
    # enumerate all subsets is 2^(A^2); feasible A<=3 fully, A=4 sample by size
    if A<=3:
        subsets=itertools.chain.from_iterable(
            itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    else:
        # A=4: 2^16=65536 subsets — full enum is fine
        subsets=itertools.chain.from_iterable(
            itertools.combinations(allp,m) for m in range(A,len(allp)+1))
    for combo in subsets:
        rel=frozenset(combo)
        if not is_total(rel,A): continue
        if not strongly_conn(rel,A): continue
        if period(rel,A)!=1: continue           # PRIMITIVE only
        n_prim+=1
        safe_set={L for L in range(3,Lmax+1) if safe_at(rel,A,L)}
        # "infinite safe" heuristic: safe at >= 3 lengths in the tail half
        tail=[L for L in safe_set if L> Lmax//2]
        if len(tail)<2: continue                 # finite/sparse safe set — skip
        infinite_safe.append((sorted(rel), sorted(safe_set)))
        d, safe_res = residue_signature(safe_set, Lmax)
        # R1: safe on a residue class with d != 2 (non-parity carrier)
        # parity = safe exactly on evens = d=2, safe_res=[0]
        is_parity_residue = (d==2 and safe_res==[0])
        if d is not None and not is_parity_residue and safe_res:
            refuters_R1.append((sorted(rel), d, safe_res, sorted(safe_set)))
        # R2: safe on evens but layered ring NOT bipartite at a safe even L
        if is_parity_residue:
            bad=[L for L in safe_set if L%2==0 and L>4 and not layered_ring_bipartite(rel,A,L)]
            if bad:
                refuters_R2.append((sorted(rel), bad, sorted(safe_set)))
    return n_prim, infinite_safe, refuters_R1, refuters_R2

import sys
A = int(sys.argv[1]) if len(sys.argv)>1 else 3
Lmax = int(sys.argv[2]) if len(sys.argv)>2 else (16 if A==3 else 14)
def P(*a):
    print(*a); sys.stdout.flush()
P(f"===== A={A}, Lmax={Lmax} =====")
n_prim, inf_safe, R1, R2 = run(A, Lmax)
P(f"primitive strongly-conn total langs: {n_prim}")
P(f"with infinite (tail>=2) safe set: {len(inf_safe)}")
for rel,ss in inf_safe:
    d,sr = residue_signature(set(ss), Lmax)
    P(f"    rel={rel}")
    P(f"      safe={ss}  residue: d={d} safe_res={sr}")
P(f"  REFUTER R1 (d!=2 residue carrier): {len(R1)}")
for rel,d,sr,ss in R1:
    P(f"    ** R1 rel={rel} d={d} safe_res={sr} safe={ss}")
P(f"  REFUTER R2 (evens but NON-bipartite layered ring): {len(R2)}")
for rel,bad,ss in R2:
    P(f"    ** R2 rel={rel} nonbip_at={bad} safe={ss}")
P("DONE")
