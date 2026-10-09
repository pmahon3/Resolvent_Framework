"""Tower relaxation for ring length L with per-window orientation eps_k in {+1,-1}.
Pattern: C_k = {x_k < x_{k+1}} if eps=+1 else {x_k > x_{k+1}}; window ultrafilter p(x)p oriented accordingly.
Checks (a) Phi(C_k)=1 for all k, (b) Phi two-valued on S_L (UNSAT for off-range), (c) sigma-realisability
(a global point in all C_k). S_L constraints: vanishing interaction on every minimal non-window index set
(non-adjacent pairs; for L=3 the triple), with resets in the tower."""
import itertools, sys
from z3 import *
def run(L, eps):
    W=[(k,(k+1)%L) for k in range(L)]
    winsets=[set(w) for w in W]
    # minimal non-window sets
    pairs=[(i,j) for i in range(L) for j in range(i+1,L) if not any({i,j}<=w for w in winsets)]
    mins=[ (i,j) for (i,j) in pairs]
    if L==3: mins=[(0,1,2)]
    nres=max(len(m) for m in mins)
    M=L+nres  # tower values 1..M, beta=0
    def key(x):
        o=sorted(set(v for v in x if v)); return tuple(0 if v==0 else 1+o.index(v) for v in x)
    P=list(itertools.product(range(M+1),repeat=L)); K={}
    for x in P: K.setdefault(key(x),len(K))
    g=[Bool('g%d'%i) for i in range(len(K))]; I=lambda x: If(g[K[key(x)]],1,0)
    s=Solver(); seen=set()
    for x in P:
        for m in mins:
            for res in itertools.product(range(M+1),repeat=len(m)):
                terms=[]
                for S in itertools.product([0,1],repeat=len(m)):
                    y=list(x)
                    for idx,bit in zip(m,S):
                        if bit: y[idx]=res[m.index(idx)]
                    terms.append(((-1)**sum(S),key(tuple(y))))
                sig=tuple(sorted(terms))
                if sig in seen: continue
                seen.add(sig); s.add(Sum([c*If(g[K[k]],1,0) for c,k in terms])==0)
    z=(0,)*L
    def pt(d): return tuple(d.get(k,0) for k in range(L))
    def Phi(Ifun):
        v=Ifun(z)+Sum([Ifun(pt({k:1}))-Ifun(z) for k in range(L)])
        for k,(a,b) in enumerate(W):
            lo,hi=(a,b) if eps[k]>0 else (b,a)
            v=v+Ifun(pt({lo:1,hi:2}))-Ifun(pt({lo:1}))-Ifun(pt({hi:1}))+Ifun(z)
        return v
    # (a) pattern values
    def C(k): a,b=W[k]; return (lambda x: (x[a]<x[b]) if eps[k]>0 else (x[a]>x[b]))
    pat=[simplify(Phi(lambda x,k=k: IntVal(1 if C(k)(x) else 0))).as_long() for k in range(L)]
    # (b)
    s.add(Or(Phi(I)>=2,Phi(I)<=-1)); two = (s.check()==unsat)
    # (c) sigma-realisable iff some global order type satisfies all C_k
    real=any(all(C(k)(x) for k in range(L)) for x in itertools.product(range(L),repeat=L))
    return pat,two,real
for L in [3,4,5]:
    for eps in sorted(set(itertools.product([1,-1],repeat=L))):
        if eps[0]<0: continue
        pat,two,real=run(L,eps)
        ess = all(v==1 for v in pat) and two and not real
        print("L=%d eps=%s  Phi(C_k)=%s  two-valued=%s  sigma-realisable=%s  => sigma-essential: %s"%(L,''.join('+' if e>0 else '-' for e in eps),pat,two,real,ess),flush=True)
