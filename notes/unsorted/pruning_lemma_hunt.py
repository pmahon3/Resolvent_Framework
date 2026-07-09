"""PRUNING LEMMA (registered, prediction WITHHELD): do the two sets agree
cofinitely? --
  TR(rho,k)   = {L : some diagonal-avoiding walk in D^{⊗k} of length L returns
                     to a cyclic shift of its start} (tuple-reachability;
                     tensor-powered; eventual periodicity nearly free)
  LISC(rho,k) = {L : some LAYER-INJECTIVE simple cycle of winding k exists on
                     the layered ring Z_L} (what the winding characterization
                     needs; injectivity is a GLOBAL constraint along the walk)
The clean proof of theorem-let B EXISTS iff TR and LISC agree cofinitely.

This script HUNTS THE DISAGREEMENT (not confirms the pattern): for stress
languages, compute both sets exactly per L and per k, and report every L where
they differ. One exhibited gap = clean proof dead, gap localized. No gap across
the stress set = evidence only, labeled as such. NO "eventually periodic through
L=N => confirmed" inference anywhere.
"""
import sys
from itertools import product

def layered_arcs(rel, A, L):
    return {(i,a,b) for i in range(L) for a in range(A) for b in range(A) if (a,b) in rel}

def simple_cycles_winding(rel, A, L):
    """All simple directed cycles of the layered ring over Z_L, with winding.
    A simple cycle: closed walk (i0,s0)->(i1,s1)->...->(i0,s0), layers advance
    mod L, no repeated (layer,state) vertex. Winding = total_steps / L.
    Returns set of (winding, frozenset-of-(layer,state)-visited, length)."""
    # vertices (i, s); arc (i,s)->((i+1)%L, t) if (s,t) in rel
    adj = {}
    for i in range(L):
        for s in range(A):
            adj[(i,s)] = [((i+1)%L, t) for t in range(A) if (s,t) in rel]
    cycles = []
    # DFS from each start, track visited (layer,state); a return to start closes
    def dfs(start, cur, path, visited):
        for nx in adj[cur]:
            if nx == start and len(path) >= L:  # closed, at least one full wind
                cycles.append(tuple(path))
            elif nx not in visited and len(path) < A*L:  # cap length at A*L (winding<=A)
                visited.add(nx); path.append(nx)
                dfs(start, nx, path, visited)
                path.pop(); visited.discard(nx)
    for s0 in range(A):
        start=(0,s0)
        dfs(start, start, [start], {start})
    return cycles

def LISC_windings(rel, A, L, kmax):
    """Set of windings k>=1 for which a layer-injective simple cycle exists.
    Layer-injective: within the cycle, the k states appearing at each layer are
    DISTINCT (so k<=A). Simple already enforced by no repeated (layer,state)."""
    out=set()
    for cyc in simple_cycles_winding(rel, A, L):
        length=len(cyc)
        if length % L != 0: continue
        k=length//L
        if k>kmax: continue
        # layer-injective: at each layer i, states are distinct
        bylayer={}
        for (i,s) in cyc: bylayer.setdefault(i,[]).append(s)
        if all(len(set(v))==len(v) for v in bylayer.values()) and all(len(bylayer.get(i,[]))==k for i in range(L)):
            out.add(k)
    return out

def TR_windings(rel, A, L, kmax):
    """Windings k for which the tuple digraph D^{⊗k} (all-distinct k-tuples,
    componentwise legal, staying all-distinct) has a length-L walk from some
    all-distinct tuple t to its cyclic shift."""
    out=set()
    for k in range(2, kmax+1):
        nodes=[t for t in product(range(A),repeat=k) if len(set(t))==k]
        if not nodes: continue
        idx={t:i for i,t in enumerate(nodes)}
        out_adj={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
        adj=[0]*len(nodes)
        for t in nodes:
            row=0
            for tp in product(*[out_adj[x] for x in t]):
                if len(set(tp))==k: row|=1<<idx[tp]
            adj[idx[t]]=row
        targ=[idx[t[1:]+(t[0],)] for t in nodes]
        reach=[1<<i for i in range(len(nodes))]
        for step in range(1,L+1):
            nr=[]
            for r in reach:
                o=0; rr=r
                while rr:
                    b=rr&-rr; o|=adj[b.bit_length()-1]; rr^=b
                nr.append(o)
            reach=nr
        if any(reach[i]>>targ[i]&1 for i in range(len(nodes))):
            out.add(k)
    return out

# stress languages: mix of small non-symmetric, symmetric, graded, and the
# ones whose winding structure was subtle (rho13, rho20, NAND, golden, a
# tournament, a mixed-period digraph)
STRESS = {
 "NAND": {(0,0),(0,1),(1,0)},
 "golden": {(0,0),(0,1),(1,0)},
 "rho13": {(0,0),(0,1),(1,2),(2,0)},
 "rho20": {(0,1),(1,0),(2,3),(3,4),(4,2)},
 "rho5":  {(0,1),(0,2),(1,0),(1,1),(2,0)},
 "C4tgt": {(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(3,0),(0,3)},
 "3cyc+loop": {(0,0),(0,1),(1,2),(2,0)},
 "tournament3": {(0,1),(1,2),(2,0)},   # pure 3-cycle (deterministic)
 "mixed": {(0,1),(1,2),(1,3),(2,0),(3,0)},  # periods 3 and 4 share
}
kmax=4
print("=== PRUNING-LEMMA DISAGREEMENT HUNT (TR vs LISC per L,k) ===")
any_gap=False
for name,rel in STRESS.items():
    rel=frozenset(rel); A=1+max(max(a,b) for (a,b) in rel)
    if A>4:  # LISC DFS cost; cap A for the exact simple-cycle enumeration
        Ltop=8
    else:
        Ltop=10
    gaps=[]
    for L in range(3, Ltop+1):
        tr=TR_windings(rel,A,L,kmax)
        lisc=LISC_windings(rel,A,L,kmax)
        # compare on the k>=2 windings (k=1 = sections, both trivially agree)
        tr2={k for k in tr if k>=2}
        lisc2={k for k in lisc if k>=2}
        # UNSAFE-relevant reduction: "L is unsafe" = tr2 nonempty (TR) vs
        # lisc2 nonempty (LISC). The lemma needs these to AGREE.
        tr_unsafe = len(tr2)>0
        lisc_unsafe = len(lisc2)>0
        if tr_unsafe != lisc_unsafe:
            gaps.append((L, sorted(tr2), sorted(lisc2)))
    if gaps:
        any_gap=True
        print(f"  {name} (A={A}): *** DISAGREEMENT ***")
        for (L,t,l) in gaps: print(f"      L={L}: TR-unsafe-windings={t}  LISC-unsafe-windings={l}")
    else:
        print(f"  {name} (A={A}): no TR/LISC unsafe-disagreement, L=3..{Ltop} (evidence only)")
print()
if any_gap:
    print("VERDICT: DISAGREEMENT EXHIBITED -> the clean tensor-power proof of")
    print("theorem-let B is DEAD as stated; TR is not a faithful proxy for LISC.")
    print("The pruning lemma is FALSE (or needs a corrected statement); the")
    print("residue-class argument loses its prerequisite in current form.")
else:
    print("VERDICT: no disagreement across the stress set (L bounded). This is")
    print("EVIDENCE the pruning holds on these languages, NOT proof. The lemma")
    print("remains OPEN; a proof must be structural, not scan-based. Registered")
    print("with prediction withheld.")
