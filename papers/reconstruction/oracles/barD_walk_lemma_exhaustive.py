import sys
sys.path.insert(0,'/Users/pmahon/Research/Mathematics/Resolvent_Framework/papers/reconstruction/oracles')
from barD_aperiodic_census import simple_cycles
def rgs(n, L):
    # restricted growth strings of length n with antipodal-free pruning (W[t] != W[t-L])
    W=[0]
    def rec(m):
        if len(W)==n: yield W; return
        t=len(W)
        for x in range(m+1):
            if t>=L and W[t-L]==x: continue
            W.append(x); yield from rec(max(m,x+1)); W.pop()
    yield from rec(1)
tot=0; fail=0
for L in range(1,7):
    cnt=0
    for W in rgs(2*L,L):
        m=max(W)+1
        rel=frozenset((W[t],W[(t+1)%(2*L)]) for t in range(2*L))
        co=set()
        for C in simple_cycles(rel,m):
            for x in C:
                for y in C:
                    if x!=y: co.add((x,y))
        cnt+=1
        if not any((W[t],W[(t+L)%(2*L)]) in co for t in range(2*L)):
            fail+=1; print('FAIL',W)
    print('L=',L,'antipodal-free closed walks (up to relabel):',cnt); tot+=cnt
print('total',tot,'fails',fail)
