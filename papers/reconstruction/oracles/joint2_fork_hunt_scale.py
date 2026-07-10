"""
ADVERSARIAL: hunt a FORK at >=5 states, past the Wielandt depth, to try to KILL
universal impossibility. Counterexample track — co-equal to the proof.

Rich-safe pinned precisely (girth-locking / frame-covering):
  A fork = a language L + a K4-minor frame F such that EVERY circuit length of F
  lies in Safe(L), yet L is genuinely contextual (escapes all tamings). The
  minimal witness of contextuality is a winding-2 obstruction on SOME frame; a
  fork must AVOID it on a frame that still carries a K4 minor.

Operationally, a necessary condition for a fork candidate: the safe set is RICH
enough to contain a K4-minor frame's circuits. A subdivided-K4 has 3 independent
cycles; if all edges are subdivided to make circuits land in an arithmetic
progression d*Z, the language must be safe on a whole residue class d*Z (like
rho20's 6Z). So: a fork candidate must be SAFE on an infinite arithmetic
progression (a residue class), NOT just finitely many lengths.

THIS is the sharp filter: hunt languages SAFE ON A FULL RESIDUE CLASS d*Z (for
some d>=2) past the Wielandt depth, that are NOT tamed by grading (imprimitive)
or signability (bipartite-residue TU). Such a language would be a fork.

Wielandt index at n=5 is (5-1)^2+1 = 17, so we must probe L up to ~25-30 to be
past the artifact window (recall: 6 candidates looked rich-safe to L=9, died by
L=30).
"""
import signal, itertools
from math import gcd
from functools import reduce

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
    from collections import deque
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

def is_bipartite_target(rel,A):
    # 2-colour states so every arc crosses (signability source). BFS 2-colouring.
    col={}
    for s in range(A):
        if s in col: continue
        col[s]=0; st=[s]
        while st:
            x=st.pop()
            for (a,b) in rel:
                if a==x:
                    if b in col:
                        if col[b]==col[x]: return False
                    else: col[b]=1-col[x]; st.append(b)
    return True

def lisc2_raw(rel,A,L):
    adj={(i,s):[((i+1)%L,t) for t in range(A) if (s,t) in rel] for i in range(L) for s in range(A)}
    lc=[0]*L; import sys; sys.setrecursionlimit(10**7)
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

class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)

def safe_on_residue(rel,A,d,Lmax,perL=8):
    """Is the language safe on the full residue class d*Z (multiples of d) up to Lmax?
    (Necessary for a fork on a subdivided-K4 with circuits in d*Z.) Returns
    (all_safe, tested_lengths, first_unsafe)."""
    tested=[]; first_unsafe=None
    for L in range(d, Lmax+1, d):
        if L<3: continue
        signal.alarm(perL)
        try:
            u=lisc2_raw(rel,A,L); signal.alarm(0)
        except TO:
            signal.alarm(0); return None, tested, ('timeout',L)
        tested.append(L)
        if u:
            first_unsafe=L; return False, tested, first_unsafe
    return True, tested, None

# HUNT: primitive (period 1), strongly-conn, non-symmetric, total, |A|=5,
# NOT bipartite-target (signability excluded), safe on SOME residue class d*Z
# deep past Wielandt index 17.
import random
random.seed(7)
A=5
allp=[(a,b) for a in range(A) for b in range(A)]
Wielandt=(A-1)**2+1
print(f"A={A}, Wielandt index={Wielandt}; probing residue classes to L=30 (well past).")
print("Hunting: primitive, strongly-conn, non-symmetric, non-bipartite, safe on d*Z.")
candidates=[]; scanned=0; N=1500
for _ in range(N*30):
    if scanned>=N: break
    m=random.randint(A, min(len(allp), A+8))  # sparse-ish, branching
    rel=frozenset(random.sample(allp,m))
    if not is_total(rel,A): continue
    if not strongly_conn(rel,A): continue
    if is_symmetric(rel): continue
    if period(rel,A)!=1: continue          # primitive only
    if is_bipartite_target(rel,A): continue # signability excluded
    scanned+=1
    # quick screen: safe on 2Z or 3Z through a modest depth first
    for d in [2,3,4]:
        allsafe,tested,fu = safe_on_residue(rel,A,d,14,perL=5)
        if allsafe and len(tested)>=3:
            # promote: probe DEEP past Wielandt
            deep,dtested,dfu = safe_on_residue(rel,A,d,30,perL=12)
            candidates.append((sorted(rel),d,dtested,deep,dfu))
            print(f"  CANDIDATE d={d} rel={sorted(rel)}")
            print(f"    safe on {d}Z through {dtested}; deep-safe={deep} first_unsafe={dfu}")
            break
print(f"\nscanned {scanned} primitive non-sym non-bipartite langs at A={A}")
forks=[c for c in candidates if c[3] is True]
print(f"FORK CANDIDATES surviving to L=30 on a residue class: {len(forks)}")
if forks:
    print("  ⚠⚠ POTENTIAL FORK (would REFUTE universal impossibility):")
    for rel,d,tested,deep,fu in forks:
        print(f"    rel={rel} safe on {d}Z through L=30")
else:
    print("  none survived deep — consistent with UI (but keep hunting wider/deeper)")
