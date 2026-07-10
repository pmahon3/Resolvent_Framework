"""Adversarial probe for the pruning lemma's FALSITY in the imprimitive case
(design-side structural prediction): build non-symmetric D whose diagonal-
avoiding D^{⊗2} is imprimitive with a diagonal-stranded state; hunt L in
TR_2 \\ LISC_2 at the offending residue, out to L~30 (PAST the periodicity
threshold a small scan can't see), NOT stopping at 9.

TR_2(L): exact reachability in the distinct-pair digraph (off-diagonal D⊗D),
  length-L walk from some (a,b) to (b,a). Bitset BFS, cheap even at L=30.
LISC_2(L): exists a layer-injective winding-2 simple cycle on the ring Z_L.
  Computed EXACTLY but scalably: a winding-2 layer-injective simple cycle = a
  closed walk of the PAIR (top token, bottom token) that (i) advances one layer
  per step for 2L steps returning to start-rotated, (ii) at each layer the two
  tokens are in DISTINCT states, (iii) never repeats a (layer,state) vertex
  across the whole 2L-walk = the two single-token paths are VERTEX-DISJOINT on
  the layered ring. So: LISC_2(L) iff the distinct-pair digraph has a
  length-2L closed pair-walk returning to start whose two projected single
  paths are vertex-disjoint on Z_L x A. We test this via a product-state search
  that tracks the SET of used (layer,state) — expensive in general, so we use
  the pair-walk-with-disjointness DP bounded by A (tokens distinct per layer)
  and check global disjointness by tracking both tokens' layer-state sequences.
  For small A (<=5) and L<=30 the layered pair graph has <=30*A*A states and we
  DFS with the visited-vertex set, which is the exact object.
"""
import sys
from itertools import product

def tr2_set(rel, A, Lmax):
    pairs=[(a,b) for a in range(A) for b in range(A) if a!=b]
    idx={p:i for i,p in enumerate(pairs)}
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    adj=[0]*len(pairs)
    for (a,b) in pairs:
        row=0
        for c in out[a]:
            for d in out[b]:
                if c!=d: row|=1<<idx[(c,d)]
        adj[idx[(a,b)]]=row
    targ=[idx[(b,a)] for (a,b) in pairs]
    reach=[1<<i for i in range(len(pairs))]
    res=set()
    for L in range(1,Lmax+1):
        nr=[]
        for r in reach:
            o=0;rr=r
            while rr:
                bb=rr&-rr;o|=adj[bb.bit_length()-1];rr^=bb
            nr.append(o)
        reach=nr
        if any(reach[i]>>targ[i]&1 for i in range(len(pairs))): res.add(L)
    return res

def lisc2_exists(rel, A, L):
    """Layer-injective winding-2 simple cycle on ring Z_L: two vertex-disjoint
    single-token paths that TOGETHER form one closed walk of winding 2 with
    distinct tokens per layer. Equivalent: a closed pair-walk (top,bottom) of
    2L steps... but the cleanest exact model: find a single closed walk of length
    2L on the layered ring, winding 2, simple (no repeated (layer,state)).
    We search: DFS on layered-ring vertices (i,s), from (0,s0), taking steps to
    ((i+1)%L, t) with (s,t) in rel, closing at (0,s0) after exactly 2L steps,
    never repeating a vertex. Prune: at most 2 visits per layer (winding 2)."""
    adj={}
    for i in range(L):
        for s in range(A):
            adj[(i,s)]=[((i+1)%L,t) for t in range(A) if (s,t) in rel]
    layercount=[0]*L
    def dfs(start, cur, steps, visited):
        if steps==2*L:
            return cur==start
        i,s=cur
        for nx in adj[cur]:
            ni,ns=nx
            if nx==start and steps+1==2*L:
                return True
            if nx not in visited and layercount[ni]<2:
                visited.add(nx); layercount[ni]+=1
                if dfs(start,nx,steps+1,visited):
                    layercount[ni]-=1; visited.discard(nx); return True
                layercount[ni]-=1; visited.discard(nx)
        return False
    for s0 in range(A):
        start=(0,s0)
        layercount[0]=1
        if dfs(start,start,0,{start}):
            layercount[0]=0; return True
        layercount[0]=0
    return False

def analyze(name, rel, A, Lmax):
    rel=frozenset(rel)
    tr=tr2_set(rel,A,Lmax)
    # diagnose D^{⊗2} off-diagonal primitivity/period
    pairs=[(a,b) for a in range(A) for b in range(A) if a!=b]
    # period of the pair digraph (gcd of cycle lengths through a recurrent pair)
    print(f"=== {name} (A={A}) ===")
    print(f"  rel: {sorted(rel)}")
    gaps=[]
    for L in range(3,Lmax+1):
        tr_has = L in tr
        lisc_has = lisc2_exists(rel,A,L)
        if tr_has != lisc_has:
            gaps.append((L,tr_has,lisc_has))
    if gaps:
        print(f"  *** DISAGREEMENT (TR_2 vs LISC_2), the predicted falsity: ***")
        for (L,t,l) in gaps:
            print(f"      L={L}: TR_2={t}  LISC_2={l}  -> {'TR-only (proxy overclaims, pruning FAILS)' if t and not l else 'LISC-only (should be impossible!)'}")
    else:
        print(f"  no TR_2/LISC_2 disagreement through L={Lmax}")
    return gaps

# ---- adversarial targets: state reachable only into the diagonal ----
# T1: state 3 reachable, but 3 only goes to states that force diagonal collision
#     for the pair dynamics; period-2 pair structure.
targets={
 # bipartite-ish base with a stranded state 3 (3 -> 0 only, and into 3 only from 2)
 "adv1": {(0,1),(1,0),(1,2),(2,1),(2,3),(3,0)},
 # period-2 core (0<->1) plus a branch that stalls the pair dynamics
 "adv2": {(0,1),(1,0),(1,2),(2,0),(0,3),(3,1)},
 # explicit: 2-cycle 0<->1 (pair period 2), state 2 diagonal-stranded (2->2 only via... no, make 2 reachable only where it pairs with itself)
 "adv3": {(0,1),(1,0),(0,2),(2,1),(1,3),(3,0)},
 # a genuinely imprimitive pair graph: bipartite base, odd extra
 "adv4": {(0,1),(1,2),(2,3),(3,0),(0,2)},
 "adv5": {(0,1),(1,2),(2,0),(2,3),(3,1)},
}
Lmax=28
anyg=False
for name,rel in targets.items():
    A=1+max(max(a,b) for (a,b) in rel)
    g=analyze(name,rel,A,Lmax)
    if g: anyg=True
print()
print("OVERALL:", "DISAGREEMENT FOUND -> pruning lemma FALSE in imprimitive case (as predicted)" if anyg
      else "no disagreement out to L=28 across adversarial imprimitive targets -> stronger evidence, still not proof")
