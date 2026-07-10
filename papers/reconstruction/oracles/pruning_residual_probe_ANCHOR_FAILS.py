"""k=2 RESIDUAL probe (design-side reduction): the pruning lemma at k=2 reduces
to 'exchange-linking implies simple'. For each L in TR_2, the tuple-walk
witnesses an EXCHANGE PATH (a length-L pair-walk (a,b)->(b,a), tokens distinct
each step). The residual question: does there EXIST such an exchange whose two
single-token trajectories are vertex-disjoint on the layered ring Z_L x A
(= a layer-injective winding-2 simple cycle exists = LISC_2(L))?

CRITICAL (avoid the false-counterexample trap): test EXISTENCE over ALL
exchange witnesses, not one. This is exactly LISC_2 recomputed as a finite
structural check on exchanges. The residual FAILS at L iff L in TR_2 but EVERY
exchange self-intersects -> minimal non-resolving exchange = the counterexample,
a finite object.

CORRECTNESS ANCHOR: this must reproduce raw-DFS LISC where both compute. Baked
in below as an assert on small L before any verdict is trusted.
"""
import sys
sys.setrecursionlimit(10**7)

def tr2_reachable(rel,A,L):
    """returns the set of start-pairs (a,b) from which a length-L exchange
    (a,b)->(b,a), tokens distinct each step, exists (via forward DP)."""
    pairs=[(a,b) for a in range(A) for b in range(A) if a!=b]
    idx={p:i for i,p in enumerate(pairs)}
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    step={p:{p} for p in pairs}  # reachable-in-0 from p is p itself; we go forward
    # forward: reach[t] = set of pairs reachable from start in t steps; but we
    # want per-start. Do BFS layers of the pair graph as sets.
    def succ(p):
        a,b=p; return [(c,d) for c in out[a] for d in out[b] if c!=d]
    reach={p:{p} for p in pairs}
    cur={p:{p} for p in pairs}
    for t in range(L):
        nxt={p:set() for p in pairs}
        for p in pairs:
            for q in cur[p]:
                for r in succ(q): nxt[p].add(r)
        cur=nxt
    return {p for p in pairs if (p[1],p[0]) in cur[p]}

def lisc2_via_exchange(rel,A,L):
    """EXISTS a vertex-disjoint exchange of length L (over ALL witnesses).
    DFS over exchange paths, but pruned: track used (layer,state) for BOTH
    tokens; success = reach (t0,s0) from (s0,t0) after L steps disjointly.
    This is existence over all exchanges = LISC_2(L)."""
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    def rec(step,top,bot,used,s0,t0):
        if step==L: return top==t0 and bot==s0
        ni=(step+1)%L
        for c in out[top]:
            if (ni,c) in used: continue
            for d in out[bot]:
                if c==d or (ni,d) in used: continue
                used.add((ni,c));used.add((ni,d))
                if rec(step+1,c,d,used,s0,t0): used.discard((ni,c));used.discard((ni,d));return True
                used.discard((ni,c));used.discard((ni,d))
        return False
    for s0 in range(A):
        for t0 in range(A):
            if s0!=t0 and rec(0,s0,t0,{(0,s0),(0,t0)},s0,t0): return True
    return False

def lisc2_raw(rel,A,L):
    """ground-truth: raw layered-ring simple-cycle DFS, winding 2."""
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

# --- CORRECTNESS ANCHOR: exchange-existence LISC == raw LISC, small L ---
anchor={"rho5":{(0,1),(0,2),(1,0),(1,1),(2,0)},
        "rho13":{(0,0),(0,1),(1,2),(2,0)},
        "adv1":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,0)},
        "adv5":{(0,1),(1,2),(2,0),(2,3),(3,1)},
        "C4tgt":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(3,0),(0,3)}}
bad=0
for name,rel in anchor.items():
    rel=frozenset(rel);A=1+max(max(a,b) for (a,b) in rel)
    for L in range(3,9):
        a=lisc2_via_exchange(rel,A,L); b=lisc2_raw(rel,A,L)
        if a!=b: print(f"ANCHOR FAIL {name} L={L}: exchange={a} raw={b}");bad+=1
print(f"CORRECTNESS ANCHOR: exchange-LISC == raw-LISC on {len(anchor)} langs L=3..8: {'PASS' if bad==0 else 'FAIL('+str(bad)+')'}",flush=True)
if bad: sys.exit(1)

# --- RESIDUAL: for each TR_2 length, does an exchange resolve to simple? ---
# The residual FAILS iff exists L with TR_2(L) but not LISC_2(L).
# We already know (2.2y) no such L to depth 35 on adv1/adv5. Here the POINT is
# different: verify the REDUCTION holds structurally = TR_2(L) <=> LISC_2(L)
# via the exchange-existence characterization, and hunt a MINIMAL non-resolver.
stress={"rho5":{(0,1),(0,2),(1,0),(1,1),(2,0)},
        "rho13":{(0,0),(0,1),(1,2),(2,0)},
        "adv1":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,0)},
        "adv5":{(0,1),(1,2),(2,0),(2,3),(3,1)},
        "C4tgt":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(3,0),(0,3)},
        "mixed":{(0,1),(1,2),(1,3),(2,0),(3,0)}}
def tr2(rel,A,L):
    pairs=[(a,b) for a in range(A) for b in range(A) if a!=b]
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    cur={p:{p} for p in pairs}
    def succ(p):
        a,b=p;return [(c,d) for c in out[a] for d in out[b] if c!=d]
    for _ in range(L):
        nxt={p:set() for p in pairs}
        for p in pairs:
            for q in cur[p]:
                for r in succ(q): nxt[p].add(r)
        cur=nxt
    return any((p[1],p[0]) in cur[p] for p in pairs)
Lmax=20; nonres=[]
for name,rel in stress.items():
    rel=frozenset(rel);A=1+max(max(a,b) for (a,b) in rel)
    for L in range(3,Lmax+1):
        t=tr2(rel,A,L)
        if t and not lisc2_via_exchange(rel,A,L):
            nonres.append((name,L)); print(f"  NON-RESOLVING EXCHANGE: {name} L={L} (TR_2 but no simple)",flush=True)
    print(f"  {name}: checked L=3..{Lmax}",flush=True)
print("RESIDUAL:", "NON-RESOLVER FOUND -> k=2 pruning FALSE, minimal counterexample exhibited" if nonres
      else f"every TR_2 length resolves to a simple exchange across stress set (L<=20): k=2 residual CLEAN -> reduction holds, k=2 lemma modulo general-k induction",flush=True)
