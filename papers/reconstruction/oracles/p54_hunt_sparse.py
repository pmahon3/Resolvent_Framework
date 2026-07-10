"""P54 targeted: 5-state SCC non-sym branching languages BY EDGE COUNT, sparse
first (m = 5..9 edges — where minimal fork candidates live; rho5 was 5 edges).
Deduped by canonical form WITHIN each stratum (few sets per low m), full cheap+
expensive screen. A clean per-stratum verdict, certificate-grade."""
import sys
from itertools import product, combinations
from math import gcd
A=5
def strongly_connected(arcs):
    adj={s:[b for (a,b) in arcs if a==s] for s in range(A)}
    radj={s:[a for (a,b) in arcs if b==s] for s in range(A)}
    def reach(g):
        seen={0};st=[0]
        while st:
            x=st.pop()
            for y in g.get(x,()):
                if y not in seen: seen.add(y);st.append(y)
        return seen
    return reach(adj)==set(range(A)) and reach(radj)==set(range(A))
def total(arcs):
    outs={a:0 for a in range(A)}; ins={a:0 for a in range(A)}
    for (a,b) in arcs: outs[a]+=1;ins[b]+=1
    return all(outs[a]>0 for a in range(A)) and all(ins[a]>0 for a in range(A))
def branching(arcs):
    o={}
    for (a,b) in arcs: o.setdefault(a,[]).append(b)
    return any(len(v)>=2 for v in o.values())
def is_sym(arcs): return all((b,a) in arcs for (a,b) in arcs)
def det(arcs):
    o={}
    for (a,b) in arcs: o.setdefault(a,[]).append(b)
    return all(len(v)<=1 for v in o.values())
from itertools import permutations
def canon(arcs):
    best=None
    for p in permutations(range(A)):
        m=tuple(sorted((p[a],p[b]) for (a,b) in arcs))
        if best is None or m<best: best=m
    return best
def base_walks(arcs,Lmax):
    M=[[1 if (a,b) in arcs else 0 for b in range(A)] for a in range(A)]
    have=set();P=[[1 if i==j else 0 for j in range(A)] for i in range(A)]
    for L in range(1,Lmax+1):
        P=[[1 if any(P[i][k] and M[k][j] for k in range(A)) else 0 for j in range(A)] for i in range(A)]
        if any(P[i][i] for i in range(A)): have.add(L)
    return have
def graded(arcs):
    W=base_walks(arcs,30);g=0
    for L in W:g=gcd(g,L)
    return g>=2
def twin(arcs):
    def sig(x):return (frozenset(y for (u,y) in arcs if u==x),frozenset(u for (u,y) in arcs if y==x))
    for x,y in combinations(range(A),2):
        if not((x,x) in arcs or (y,y) in arcs or (x,y) in arcs or (y,x) in arcs) and sig(x)==sig(y):return True
    return False
def md(arcs):
    from fractions import Fraction as F
    cl=sorted(arcs);n=len(cl)
    M=[[F(1 if c[0]==s else 0) for c in cl] for s in range(A)]+[[F(1 if c[1]==s else 0) for c in cl] for s in range(A)]
    rk=0
    for c in range(n):
        pr=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if pr is None:continue
        M[rk],M[pr]=M[pr],M[rk];dv=M[rk][c];M[rk]=[x/dv for x in M[rk]]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c];M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
        if rk==len(M):break
    return rk==n
def pair_bip(arcs):
    prs=[(a,b) for a in range(A) for b in range(A) if a!=b];adj={}
    for (a,b) in prs:
        for (c,dd) in prs:
            if (a,c) in arcs and (b,dd) in arcs: adj.setdefault((a,b),[]).append((c,dd))
    col={}
    for s in prs:
        if s in col:continue
        col[s]=0;st=[s]
        while st:
            x=st.pop()
            for y in list(adj.get(x,[]))+[z for z,n in adj.items() if x in n]:
                if y in col:
                    if col[y]==col[x]:return False
                else:col[y]=1-col[x];st.append(y)
    return True
def tuple_dg(arcs,k):
    nodes=[t for t in product(range(A),repeat=k) if len(set(t))==k];idx={t:i for i,t in enumerate(nodes)}
    out={a:[b for b in range(A) if (a,b) in arcs] for a in range(A)};adj=[0]*len(nodes)
    for t in nodes:
        row=0
        for tp in product(*[out[x] for x in t]):
            if len(set(tp))==k:row|=1<<idx[tp]
        adj[idx[t]]=row
    return nodes,idx,adj
def _mul(r,adj):
    o=0
    while r:
        b=r&-r;o|=adj[b.bit_length()-1];r^=b
    return o
def safe_evens(arcs,rich,Lmax):
    W=base_walks(arcs,Lmax);uc=[L for L in rich if L in W]
    if len(uc)<2:return []
    U=set()
    for k in range(2,A+1):
        nodes,idx,adj=tuple_dg(arcs,k)
        if not nodes:continue
        targ=[idx[t[1:]+(t[0],)] for t in nodes];reach=[1<<i for i in range(len(nodes))]
        for L in range(1,Lmax+1):
            reach=[_mul(r,adj) if r else 0 for r in reach]
            for i in range(len(nodes)):
                if reach[i]>>targ[i]&1:U.add(L);break
        if all(L in U for L in uc):break
    return [L for L in uc if L not in U]

allpairs=[(a,b) for a in range(A) for b in range(A)]  # includes loops
RICH=[6,8,10,12];Lmax=12
for m in range(5,10):
    seen=set();reps=0;forks=[]
    for combo in combinations(allpairs,m):
        arcs=frozenset(combo)
        if is_sym(arcs) or det(arcs) or not branching(arcs) or not total(arcs): continue
        if not strongly_connected(arcs): continue
        c=canon(arcs)
        if c in seen: continue
        seen.add(c);reps+=1
        if graded(arcs) or twin(arcs) or (md(arcs) and pair_bip(arcs)): continue
        se=safe_evens(arcs,RICH,Lmax)
        if len(se)>=2: forks.append((sorted(arcs),se))
    print(f"m={m} edges: {reps} canonical SCC non-sym branching reps; fork candidates: {len(forks)}",flush=True)
    for (l,se) in forks[:6]: print(f"    FORK: arcs={l} safe_even={se}",flush=True)
print("SPARSE-STRATA DONE (m=5..9)",flush=True)
