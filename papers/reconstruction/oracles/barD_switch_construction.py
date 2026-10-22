import sys, random, itertools
from math import gcd
from collections import deque
sys.path.insert(0,'/Users/pmahon/Research/Mathematics/Resolvent_Framework/papers/reconstruction/oracles')
from barD_aperiodic_census import primitive, simple_cycles
exec(open(__file__.replace('barD_switch_construction.py','barD_cocyclic_shortest_crossed.py')).read().split("def check(")[0].split("from barD_aperiodic_census import primitive, simple_cycles")[1])
def switch_ok(W, L, cycles):
    """exists simple cycle C (len>=2), time t, mover in {1,2}: mover circulates C from W_t,
    other follows W from W_{t+L}; collision-free over lcm period; other touches C off mover."""
    n=2*L
    for C in cycles:
        c=len(C)
        if c<2: continue
        pos={v:i for i,v in enumerate(C)}
        for t in range(n):
            if W[t] not in pos: continue
            p0=pos[W[t]]; T=c*n//gcd(c,n); ok=True; touch=False
            for tau in range(T):
                m=C[(p0+tau)%c]; o=W[(t+L+tau)%n]
                if m==o: ok=False; break
                if o in pos: touch=True
            if ok and touch: return True
    return False
def run_lang(rel,A,st):
    cyc=simple_cycles(rel,A)
    for a,b in itertools.permutations(range(A),2):
        p=shortest_crossed(rel,A,a,b)
        if p is None: continue
        L=len(p)-1; W=[x for x,_ in p]+[y for _,y in p][1:-1]
        st['n']+=1
        if not switch_ok(W,L,cyc):
            st['fail']+=1
            if len(st['ex'])<3: st['ex'].append((sorted(rel),W))
for A in (3,4):
    allp=[(a,b) for a in range(A) for b in range(A)]; st=dict(n=0,fail=0,ex=[])
    for mask in range(1<<len(allp)):
        rel=frozenset(p for i,p in enumerate(allp) if mask>>i&1)
        if primitive(rel,A): run_lang(rel,A,st)
    print('A',A,'shortest crossed walks',st['n'],'switch construction fails',st['fail'],st['ex'][:2])
# imprimitive cacti from the exhaustive walk-lemma run: construction must FAIL there
cacti=[[0,1,0,2,3,4,3,2,5,6,5,2],[0,1,2,0,3,4,5,3,6,7,8,6],[0,1,2,1,0,3,4,3,0,5,6,5],[0,1,2,3,1,4,5,6,4,0,7,8]]
for W in cacti:
    L=len(W)//2; A=max(W)+1; rel=frozenset((W[t],W[(t+1)%(2*L)]) for t in range(2*L))
    print('imprimitive cactus',W,'switch ok:',switch_ok(W,L,simple_cycles(rel,A)))
