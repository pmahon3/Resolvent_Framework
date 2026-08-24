"""Finer discriminator: does the WINDING-SET agree (not just emptiness)? And
directly probe the structural gap: exhibit, if it exists, a length-L tuple-walk
(TR-witness) at winding k whose length admits NO layer-injective simple cycle at
that k -- the exact 'proxy unfaithful' event. Also the converse (LISC without
TR). Report winding-set mismatches, not just unsafe/safe."""
import sys
from itertools import product

def simple_cycles(rel, A, L, kmax):
    adj={(i,s):[((i+1)%L,t) for t in range(A) if (s,t) in rel] for i in range(L) for s in range(A)}
    res=[]
    def dfs(start,cur,path,visited):
        for nx in adj[cur]:
            if nx==start and len(path)>=L:
                res.append(tuple(path))
            elif nx not in visited and len(path)<kmax*L:
                visited.add(nx);path.append(nx);dfs(start,nx,path,visited);path.pop();visited.discard(nx)
    for s0 in range(A):
        dfs((0,s0),(0,s0),[(0,s0)],{(0,s0)})
    return res

def LISC_windings(rel,A,L,kmax):
    out=set()
    for cyc in simple_cycles(rel,A,L,kmax):
        if len(cyc)%L: continue
        k=len(cyc)//L
        if not (2<=k<=kmax): continue
        bl={}
        for (i,s) in cyc: bl.setdefault(i,[]).append(s)
        if all(len(set(v))==len(v) for v in bl.values()) and all(len(bl.get(i,[]))==k for i in range(L)):
            out.add(k)
    return out

def TR_windings(rel,A,L,kmax):
    out=set()
    for k in range(2,kmax+1):
        nodes=[t for t in product(range(A),repeat=k) if len(set(t))==k]
        if not nodes: continue
        idx={t:i for i,t in enumerate(nodes)}
        oa={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
        adj=[0]*len(nodes)
        for t in nodes:
            row=0
            for tp in product(*[oa[x] for x in t]):
                if len(set(tp))==k: row|=1<<idx[tp]
            adj[idx[t]]=row
        targ=[idx[t[1:]+(t[0],)] for t in nodes]
        reach=[1<<i for i in range(len(nodes))]
        for _ in range(L):
            nr=[]
            for r in reach:
                o=0;rr=r
                while rr:
                    b=rr&-rr;o|=adj[b.bit_length()-1];rr^=b
                nr.append(o)
            reach=nr
        if any(reach[i]>>targ[i]&1 for i in range(len(nodes))): out.add(k)
    return out

STRESS={
 "rho13":{(0,0),(0,1),(1,2),(2,0)},
 "rho5":{(0,1),(0,2),(1,0),(1,1),(2,0)},
 "3cyc+loop":{(0,0),(0,1),(1,2),(2,0)},
 "mixed":{(0,1),(1,2),(1,3),(2,0),(3,0)},
 "C4tgt":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,2),(3,0),(0,3)},
 "rho20":{(0,1),(1,0),(2,3),(3,4),(4,2)},
 # deliberately gnarly: a digraph where higher-winding tuple walks revisit
 "revisit":{(0,1),(0,2),(1,0),(2,3),(3,0)},
 "bigcycle":{(0,1),(1,2),(2,3),(3,4),(4,0),(2,0)},
}
kmax=4; anymis=False
print("=== FINE DISCRIMINATOR: winding-set agreement TR vs LISC ===")
for name,rel in STRESS.items():
    rel=frozenset(rel);A=1+max(max(a,b) for (a,b) in rel)
    Ltop=8 if A>=5 else 9
    mism=[]
    for L in range(3,Ltop+1):
        tr={k for k in TR_windings(rel,A,L,kmax) if k>=2}
        li=LISC_windings(rel,A,L,kmax)
        if tr!=li:
            mism.append((L,sorted(tr),sorted(li)))
    if mism:
        anymis=True
        print(f"  {name} (A={A}): WINDING-SET MISMATCH:")
        for (L,t,l) in mism:
            extra_tr=sorted(set(t)-set(l)); extra_li=sorted(set(l)-set(t))
            print(f"      L={L}: TR={t} LISC={l}  | TR-only(proxy-overclaims)={extra_tr} LISC-only={extra_li}")
    else:
        print(f"  {name} (A={A}): winding-sets AGREE exactly, L=3..{Ltop}")
print()
if anymis:
    print("FINDING: TR and LISC winding-sets DIVERGE. The pruning is FALSE at the")
    print("winding level. Whether it survives at the UNSAFE level (emptiness) is a")
    print("separate, weaker question -- but the clean 'TR = LISC' proof is dead,")
    print("and theorem-let B needs either the unsafe-level pruning (weaker, maybe")
    print("still true) or a different argument. Gap LOCALIZED to specific (L,k).")
else:
    print("Winding-sets agree exactly across the fine stress set (L bounded).")
    print("Stronger evidence than the emptiness check -- but STILL not proof.")
