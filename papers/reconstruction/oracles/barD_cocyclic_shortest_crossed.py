import sys, random
from collections import deque
sys.path.insert(0,'/Users/pmahon/Research/Mathematics/Resolvent_Framework/papers/reconstruction/oracles')
from barD_aperiodic_census import primitive, simple_cycles
def cocyclic(rel,A):
    S=set()
    for C in simple_cycles(rel,A):
        for x in C:
            for y in C:
                if x!=y: S.add((x,y))
    return S
def shortest_crossed(rel,A,a,b):
    start=(a,b); prev={start:None}; dq=deque([start])
    while dq:
        u=dq.popleft()
        for c in range(A):
            if (u[0],c) not in rel: continue
            for d in range(A):
                if c==d or (u[1],d) not in rel: continue
                v=(c,d)
                if v in prev: continue
                prev[v]=u; dq.append(v)
    if (b,a) not in prev: return None
    path=[(b,a)]
    while path[-1]!=start: path.append(prev[path[-1]])
    return path[::-1]
def check(rel,A,stats):
    co=cocyclic(rel,A)
    for a in range(A):
        for b in range(A):
            if a==b: continue
            p=shortest_crossed(rel,A,a,b)
            if p is None: continue
            L=len(p)-1
            W=[x for x,_ in p]+[y for _,y in p][1:]   # pi1 then pi2 (W_L=b ... W_2L=a)
            assert W[L]==b and W[2*L]==a
            stats['walks']+=1
            if not any((W[t],W[(t+L)%(2*L)]) in co for t in range(2*L)):
                stats['fail']+=1
                if len(stats['ex'])<3: stats['ex'].append((sorted(rel),a,b,W))
for A in (3,4):
    allp=[(a,b) for a in range(A) for b in range(A)]
    st=dict(walks=0,fail=0,ex=[])
    for mask in range(1<<len(allp)):
        rel=frozenset(p for i,p in enumerate(allp) if mask>>i&1)
        if primitive(rel,A): check(rel,A,st)
    print(A,st['walks'],'shortest crossed walks; no cocyclic pair on antipodal chase:',st['fail'],st['ex'][:2])
random.seed(7)
for A in (5,6):
    allp=[(a,b) for a in range(A) for b in range(A)]; st=dict(walks=0,fail=0,ex=[]); n=0
    while n<1500:
        rel=frozenset(x for x in allp if random.random()<random.choice((1.4,2,3))/A)
        if not primitive(rel,A): continue
        n+=1; check(rel,A,st)
    print(A,'sample',st['walks'],'fail',st['fail'],st['ex'][:2])
