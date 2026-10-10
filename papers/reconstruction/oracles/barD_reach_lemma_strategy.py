import sys, random, itertools
from collections import deque
sys.path.insert(0,'/Users/pmahon/Research/Mathematics/Resolvent_Framework/papers/reconstruction/oracles')
from barD_aperiodic_census import primitive, simple_cycles
def recurrent_pairs(rel,A):
    out={a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    V=[(a,b) for a in range(A) for b in range(A) if a!=b]
    succ={v:[(c,d) for c in out[v[0]] for d in out[v[1]] if c!=d] for v in V}
    rec=[]
    for v in V:
        seen=set(); st=list(succ[v]); found=False
        while st:
            u=st.pop()
            if u==v: found=True; break
            if u in seen: continue
            seen.add(u); st.extend(succ[u])
        if found: rec.append(v)
    return rec, out
def k_star_check(rel,A,cycles,out):
    # Step 1 transit move asserted: chase on C at (v, x_{c-1}) -> one step -> chase on C'
    for C in cycles:
        if len(C)<2: continue
        for C2 in cycles:
            if len(C2)<2 or C2==C: continue
            for v in set(C)&set(C2):
                i=C.index(v); prev=C[(i-1)%len(C)]; k=C2.index(v); nxt=C2[(k+1)%len(C2)]
                assert (v,nxt) in rel and (prev,v) in rel and nxt!=v
def strategy(P, cycles, out):
    """mover on cycle C through its own position circulates C; other walks freely
    (state = other's vertex, time mod c), never colliding, until it stands on C."""
    for mover in (0,1):
        m, o = P[mover], P[1-mover]
        for C in cycles:
            c=len(C)
            if c<2 or m not in C: continue
            pos={v:i for i,v in enumerate(C)}; p0=pos[m]
            onC=lambda w,t: w in pos
            start=(o,0); seen={start}; dq=deque([start]); ok=False
            while dq:
                w,t=dq.popleft()
                for w2 in out[w]:
                    t2=(t+1)%c; mpos=C[(p0+t2)%c]
                    if w2==mpos: continue
                    if w2 in pos: ok=True; break
                    s=(w2,t2)
                    if s not in seen: seen.add(s); dq.append(s)
                if ok: break
            if ok: return True
    return False
def run(rel,A,st):
    rec,out=recurrent_pairs(rel,A); cyc=simple_cycles(rel,A)
    k_star_check(rel,A,cyc,out)
    for P in rec:
        st['n']+=1
        if not strategy(P,cyc,out):
            st['fail']+=1
            if len(st['ex'])<3: st['ex'].append((sorted(rel),P))
for A in (3,4):
    allp=[(a,b) for a in range(A) for b in range(A)]; st=dict(n=0,fail=0,ex=[])
    for mask in range(1<<len(allp)):
        rel=frozenset(p for i,p in enumerate(allp) if mask>>i&1)
        if primitive(rel,A): run(rel,A,st)
    print('A',A,'recurrent pairs',st['n'],'strategy fails',st['fail'],st['ex'])
random.seed(5)
for A in (5,6,7):
    allp=[(a,b) for a in range(A) for b in range(A)]; st=dict(n=0,fail=0,ex=[]); k=0
    while k<1500:
        rel=frozenset(x for x in allp if random.random()<random.choice((1.3,1.7,2.5))/A)
        if not primitive(rel,A): continue
        k+=1; run(rel,A,st)
    print('A',A,'sample recurrent pairs',st['n'],'strategy fails',st['fail'],st['ex'][:2])
