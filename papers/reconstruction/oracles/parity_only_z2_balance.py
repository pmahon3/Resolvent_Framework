"""
Forcing test. The validated predicate: unsafe at L <=> a walk of length L from
(a,b) to (b,a) in the ORDERED-PAIR digraph D [vertices (a,b) a!=b; arc
(a,b)->(c,d) iff (a,c),(b,d) in rho]. sigma:(a,b)->(b,a) is a digraph automorphism.

Quotient bar-D = unordered-pair graph; D->bar-D is a Z2-cover with a monodromy
label m(arc) in {0,1} (0 = parallel (a,c)&(b,d) keeping order; 1 = crossed, i.e.
the lift flips the sheet). unsafe at L <=> bar-D has a CLOSED walk of length L with
ODD total monodromy.

CLAIM (safe-on-evens characterization): safe exactly on evens <=> the monodromy
label m is COHOMOLOGOUS TO CONSTANT-1, i.e. exists phi: V(bar-D)->Z2 with
m(P->Q) = 1 + phi(P) + phi(Q)  (mod 2) for every arc that exists. Then any closed
walk has total monodromy = L*1 + sum(Δphi) = L (mod 2), so odd-monodromy closed
walk exists <=> L odd => unsafe<=>odd => safe on evens.

If m is NOT cohomologous to constant-1 (on some strongly-connected component of
bar-D that is reachable/relevant), there is an even-length odd-monodromy closed
walk => unsafe at some even L => NOT safe-on-evens.

TEST: does "m ~ const-1 on the relevant part" predict safe-on-evens, matching the
LISC oracle, on witnesses (safe) AND negatives (unsafe-at-even)? AND is it IMPLIED
by primitivity? (The forcing claim: primitive => m ~ const-1.)

We compute cohomology via: build bar-D as an undirected graph with Z2 edge-labels
(a P-Q edge exists if some arc P->Q or Q->P; label = its monodromy; if both
orientations exist with DIFFERENT labels, that's a 'label conflict' = no potential
even locally => there IS an even odd-monodromy 2-cycle => unsafe at even). Then
check: is the labelling a Z2-coboundary-plus-const-1? Equivalent: define new label
m'(edge)=m+1; m ~ const-1  <=>  m' ~ 0  <=> m' is a coboundary <=> every CYCLE in
bar-D has even m'-sum <=> the signed graph (V, edges, sign=m') is BALANCED.
So: safe-on-evens  <=>  the signed graph (bar-D, sign = monodromy+1) is BALANCED.
Check balance by 2-colouring (union-find / BFS with parity).
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

def safe_on_evens_oracle(rel,A,Lmax=12):
    """Ground truth: safe at all even L in [4,Lmax] and unsafe at some odd L."""
    evens=[L for L in range(4,Lmax+1,2)]
    odds=[L for L in range(3,Lmax+1,2)]
    all_even_safe = all(not lisc2_raw(rel,A,L) for L in evens)
    some_odd_unsafe = any(lisc2_raw(rel,A,L) for L in odds)
    return all_even_safe and some_odd_unsafe

def signed_balance_predicts_safe_evens(rel,A):
    """Build bar-D signed graph, sign(edge P-Q) = monodromy(P->Q) + 1 (mod 2).
    Return (balanced, has_infinite_safe_structure).
    Balanced <=> exists 2-colouring c:V->Z2 with sign(P,Q)=c(P)+c(Q) for every edge.
    We ALSO must restrict to the part of bar-D that carries closed walks (else
    isolated conflict-free parts are vacuous). Simplest faithful check: build ALL
    edges with their sign; if any edge has BOTH orientations present with different
    monodromy => a 2-cycle with odd sign => unbalanced. Then BFS-2-colour."""
    # ordered pairs
    verts=[(a,b) for a in range(A) for b in range(A) if a!=b]
    # arcs D: (a,b)->(c,d) iff (a,c),(b,d) in rel. monodromy relative to sigma:
    # the lift is 'parallel' (m=0) — sigma sends (a,b)->(b,a); the arc (b,a)->(d,c)
    # is the sigma-image. An UNORDERED edge {(a,b),(b,a)}=P. Between unordered P and
    # Q, an arc P->Q in bar-D comes from an ordered arc; monodromy = 0 if it maps
    # the chosen sheet (a,b)->(c,d), = 1 if (a,b)->(d,c).
    def key(a,b): return frozenset({a,b})
    # collect edges of bar-D with signs
    # sign convention: for ordered arc (a,b)->(c,d) [both in rel-pairwise], the
    # bar-edge key(a,b)-key(c,d) gets monodromy 0 if (c,d) is the 'same-orientation'
    # rep and 1 if flipped. But orientation of unordered pair is ambiguous; the
    # WELL-DEFINED invariant is: fix an orientation rep for each unordered pair
    # (say sorted ascending = sheet 0). Then arc (a,b)->(c,d): let s_P = 0 if (a,b)
    # is ascending else 1; s_Q likewise for (c,d). monodromy of this arc in the
    # sheet-0 frame = s_P xor s_Q ... plus the intrinsic. Cleanest: the SIGNED edge
    # label between P,Q is m = [ (a,b) ascending? ] xor [ (c,d) ascending? ] is NOT
    # intrinsic. Instead: an unordered edge P-Q is 'parallel-type' if BOTH (asc_P ->
    # asc_Q via rel-preserving order) hold, 'crossed-type' if asc_P -> desc_Q.
    # We record for each unordered pair-edge the set of achievable signs.
    def asc(p):
        a,b=min(p),max(p); return (a,b)
    edges={}  # frozenset({P,Q}) -> set of signs achievable
    for (a,b) in verts:
        P=key(a,b)
        for c in range(A):
            if (a,c) not in rel: continue
            for d in range(A):
                if c==d: continue
                if (b,d) not in rel: continue
                Q=key(c,d)
                if P==Q:
                    # loop in bar-D: a arc (a,b)->(c,d) with {c,d}={a,b}
                    # sign = 0 if (c,d)==(a,b) [identity], 1 if (c,d)==(b,a) [swap]
                    s = 0 if (c,d)==(a,b) else 1
                    edges.setdefault(frozenset({P}),set()).add(s)
                    continue
                # sign in the ascending frame: does the arc preserve ascending?
                # ascending rep of P is asc(P); of Q is asc(Q). The arc (a,b)->(c,d)
                # maps sheet[(a,b)] to sheet[(c,d)]. sheet index of (a,b) = 0 if
                # (a,b)==asc(P) else 1. sign = sheetindex(a,b) xor sheetindex(c,d).
                spi = 0 if (a,b)==asc(P) else 1
                sqi = 0 if (c,d)==asc(Q) else 1
                s = spi ^ sqi
                edges.setdefault(frozenset({P,Q}),set()).add(s)
    # signed graph: edge P-Q with sign = m+1 where m in achievable signs. If an edge
    # achieves BOTH m=0 and m=1, then it carries both sign 1 and sign 0 => any cycle
    # through it can hit either => effectively unconstrained on that edge => cannot
    # force balance => treat as unbalanced-capable. Conservative: unsafe-at-even
    # possible iff NOT (every edge has a UNIQUE sign AND the unique-signed graph is
    # balanced).
    # Build unique-sign graph:
    unbalanced=False
    adjs={}
    for e,signs in edges.items():
        if len(e)==1:  # bar-D self-loop on node P
            # sign(loop) = m+1. A self-loop with sign 1 (i.e. m=0, a PARALLEL loop)
            # is a frustrated cycle: closed walk of length 1 with monodromy m=0 !=
            # length(1) mod 2. It lets a walk gain a monodromy-0 step of odd length,
            # breaking 'monodromy == length mod 2'. => imbalance. (Both signs => also
            # imbalance.) Signs here are m; sign_signed = (m+1)%2; frustrated if any
            # loop-sign == 1, i.e. any m==0 present.
            if 0 in signs:   # a parallel self-loop => sign 1 => frustration
                unbalanced=True
            continue
        if len(signs)>1:
            unbalanced=True  # edge supports both parities => odd-monodromy even cycle
            continue
        m=next(iter(signs)); sign=(m+1)%2  # want m ~ const 1 <=> (m+1) coboundary
        P,Q=tuple(e)
        adjs.setdefault(P,[]).append((Q,sign))
        adjs.setdefault(Q,[]).append((P,sign))
    # balance check: 2-colour so color[P]^color[Q]==sign for each edge
    color={}
    for s0 in list(adjs.keys()):
        if s0 in color: continue
        color[s0]=0; st=[s0]
        while st:
            x=st.pop()
            for (y,sg) in adjs[x]:
                want=color[x]^sg
                if y in color:
                    if color[y]!=want: unbalanced=True
                else:
                    color[y]=want; st.append(y)
    balanced = not unbalanced
    return balanced

def strongly_conn(rel,A):
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
    from collections import deque
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    lvl={0:0}; dq=deque([0])
    while dq:
        x=dq.popleft()
        for y in out[x]:
            if y not in lvl: lvl[y]=lvl[x]+1; dq.append(y)
    g=0
    for a in range(A):
        if a not in lvl: continue
        for b in out[a]:
            if b not in lvl: continue
            g=gcd(g,abs(lvl[a]+1-lvl[b]))
    return g if g>0 else 1

# TEST: does 'signed graph balanced' predict 'safe on evens' (oracle)?
for A in [3,4]:
    allp=[(a,b) for a in range(A) for b in range(A)]
    random.seed(5)
    tested=0; mism=0; examples=[]
    # also track a contingency table to detect a tautology (like R2)
    n_bal=0; n_soe=0
    for _ in range(20000):
        rel=frozenset(random.sample(allp,random.randint(A,min(len(allp),A+6))))
        if not strongly_conn(rel,A): continue
        tested+=1
        soe = safe_on_evens_oracle(rel,A)
        bal = signed_balance_predicts_safe_evens(rel,A)
        if bal: n_bal+=1
        if soe: n_soe+=1
        if soe!=bal:
            mism+=1
            if len(examples)<8: examples.append((sorted(rel),soe,bal,period(rel,A)))
        if tested>=800: break
    print(f"A={A}: tested {tested} strongly-conn langs; MISMATCHES={mism}; "
          f"#balanced={n_bal} #safe_on_evens={n_soe} (both should be >0 and <tested "
          f"— else it's a tautology like R2)")
    for rel,soe,bal,p in examples:
        print(f"    MISM rel={rel} safe_on_evens={soe} balanced={bal} period={p}")
