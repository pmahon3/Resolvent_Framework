"""
Crossing-parity mechanism, v2: enforce SIMPLICITY (global vertex-disjointness of
the 2-fold cover), which v1 dropped. Re-test vs raw LISC at both parities on
witnesses AND negatives.

A winding-2 LISC is a 2-fold cover of Z_L: an ordered thread-pair (a_i, b_i),
a_i != b_i, at each layer, with (a_i,a_{i+1}),(b_i,b_{i+1}) in rel [parallel] or
crossed. It is a SINGLE simple cycle of winding 2 iff:
  - the LAYERED vertices used are all distinct (simplicity): the multiset of
    (i, state) over both threads has no repeat = at each layer the two states are
    distinct (given) AND no (i,s) used by both/again — automatic since a thread
    visits layer i once and the two threads have distinct states there;
  - it CLOSES as ONE cycle, not two: the monodromy is a swap = ODD crossings.

The subtlety v1 missed: I must not dedup on unordered pair; I must track the
actual thread-states per layer and ensure the two threads never coincide, and that
the closure is a genuine single 2L-cycle. Cleanest: directly reuse the TRUSTED
lisc2_raw as the oracle, and build a SEPARATE combinatorial predicate
'odd_crossing_simple_cover_exists' from scratch, then compare. If they agree, the
combinatorial predicate is validated as the mechanism.

Here 'odd_crossing_simple_cover_exists' = DFS over ordered thread-pairs (a,b),
a!=b, layer 0..L, tracking crossing parity, requiring closure to the SWAPPED start
(a0,b0)->(b0,a0) [odd crossings] AND that the cover is simple: no ordered
(layer, thread-state) reused. Since each thread advances one layer per step and
visits each layer once, simplicity reduces to: the two threads never share a state
at any layer (a_i != b_i, enforced) — that alone does NOT guarantee the 2L-cycle
is simple across the two wraps. The genuine simplicity constraint: the SET of
(layer, state) pairs { (i,a_i) } ∪ { (i,b_i) } has size 2L, i.e. for each layer the
two states differ (given) — this IS size 2L. So a 2-fold cover with a_i!=b_i for
all i is automatically a simple set of 2L layered-vertices. The question is whether
it forms ONE cycle (odd crossings) vs TWO (even). THAT is the only freedom.

So v1's bug was NOT missing simplicity — it was the frozenset dedup PRUNING valid
search paths OR mis-closing. Rebuild carefully: track ordered (a,b), require return
to (b0,a0) at layer L (=swap), NO dedup (path length bounded by L). Compare.
"""
import sys, random
sys.setrecursionlimit(10**7)

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

def odd_cross_cover(rel,A,L):
    """Exists a 2-fold cover: ordered threads (a_i,b_i), a_i!=b_i, i=0..L-1,
    with legal arcs, closing SWAPPED after L layers (a_{L}=b_0, b_{L}=a_0), which
    encodes ODD crossings = single winding-2 cycle. Track the two thread-states;
    require a_i != b_i everywhere (the 2L layered vertices are then all distinct)."""
    # transitions from ordered (a,b): (c,d) with a!=b, c!=d and legal both threads
    def succ(a,b):
        for c in range(A):
            if (a,c) not in rel: continue
            for d in range(A):
                if c==d: continue
                if (b,d) in rel:
                    yield (c,d)
    found=[False]
    def dfs(a0,b0,a,b,layer):
        if found[0]: return
        if layer==L:
            # after exactly L succ-arcs we are back at layer 0 (wrap already taken).
            # single winding-2 cycle = swap monodromy = we land on the SWAPPED start.
            if a==b0 and b==a0:
                found[0]=True
            return
        for (c,d) in succ(a,b):
            dfs(a0,b0,c,d,layer+1)
            if found[0]: return
    for a0 in range(A):
        for b0 in range(A):
            if a0==b0: continue
            dfs(a0,b0,a0,b0,0)
            if found[0]: return True
    return False

witnesses=[
 [(0,0),(0,1),(0,2),(1,0),(2,0)],[(0,0),(0,1),(1,0),(1,2),(2,1)],
 [(0,0),(0,2),(1,2),(2,0),(2,1)],[(0,1),(0,2),(1,0),(1,1),(2,0)],
 [(0,1),(0,2),(1,0),(2,0),(2,2)],[(0,1),(1,0),(1,1),(1,2),(2,1)],
 [(0,1),(1,0),(1,2),(2,1),(2,2)],[(0,2),(1,1),(1,2),(2,0),(2,1)],
 [(0,2),(1,2),(2,0),(2,1),(2,2)],
]
A=3
def test(rel,label):
    mism=[]
    for L in range(3,13):
        o=lisc2_raw(rel,A,L); p=odd_cross_cover(rel,A,L)
        if o!=p: mism.append((L,o,p))
    print(f"  [{label}] {'MATCH' if not mism else 'MISMATCH '+str(mism)}")
    return not mism
print("=== WITNESSES ===")
allok=True
for i,w in enumerate(witnesses): allok=test(frozenset(w),f"w{i+1}") and allok
print("=== NEGATIVES ===")
full=frozenset((a,b) for a in range(A) for b in range(A))
allok=test(full,"full") and allok
random.seed(11); allp=[(a,b) for a in range(A) for b in range(A)]; nt=0
for _ in range(400):
    if nt>=8: break
    rel=frozenset(random.sample(allp,random.randint(A,8)))
    outs={a for (a,b) in rel}; ins={b for (a,b) in rel}
    if outs!=set(range(A)) or ins!=set(range(A)): continue
    if not lisc2_raw(rel,A,6): continue
    nt+=1; allok=test(rel,f"neg{nt}") and allok
print(f"\nOVERALL: {'ALL MATCH' if allok else 'MISMATCH'}")
