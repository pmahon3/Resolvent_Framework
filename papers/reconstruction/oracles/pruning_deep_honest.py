"""Correct LISC (raw layered-ring simple-cycle DFS, validated ==new failed so we
KEEP the raw one) pushed as deep as completes within a per-L wall. adv1/adv5
(validated imprimitive). Honest: each L completes-correctly or is marked
NOT-COMPUTED. No reformulation — the raw DFS is the correct object."""
import signal
def tr2_set(rel,A,Lmax):
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
    reach=[1<<i for i in range(len(pairs))];res=set()
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
class TO(Exception): pass
def lisc2_raw(rel,A,L):
    adj={(i,s):[((i+1)%L,t) for t in range(A) if (s,t) in rel] for i in range(L) for s in range(A)}
    lc=[0]*L
    import sys; sys.setrecursionlimit(10**7)
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
def handler(sig,frm): raise TO()
signal.signal(signal.SIGALRM,handler)
targets={"adv1":{(0,1),(1,0),(1,2),(2,1),(2,3),(3,0)},
         "adv5":{(0,1),(1,2),(2,0),(2,3),(3,1)}}
Lmax=40; PERL=20  # 20s per L wall
for name,rel in targets.items():
    rel=frozenset(rel);A=1+max(max(a,b) for (a,b) in rel)
    tr=tr2_set(rel,A,Lmax); maxdone=2; disagree=[]
    for L in range(3,Lmax+1):
        signal.alarm(PERL)
        try:
            l=lisc2_raw(rel,A,L); signal.alarm(0)
        except TO:
            signal.alarm(0)
            print(f"  {name} L={L}: NOT-COMPUTED (>{PERL}s) -- stopping this target",flush=True)
            break
        t=L in tr; maxdone=L
        if t!=l: disagree.append((L,t,l)); print(f"  {name} L={L}: TR={int(t)} LISC={int(l)} <-- DISAGREE",flush=True)
    print(f"{name}: correct through L={maxdone}; disagreements={disagree if disagree else 'NONE'}",flush=True)
print("DONE",flush=True)
