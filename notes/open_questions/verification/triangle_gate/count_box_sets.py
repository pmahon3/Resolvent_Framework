# 2026-11-10 (5DE check). Count the box sets (0/1 pair-sums, eight-corner identity) on a grid n0 x n1 x n2
# WITHOUT any closure, to compare with the known |D3|.  A set F is box iff every slice difference
# F_a - F_0 is additive: alpha(x1)+beta(x2).  So |B| = sum over base slices G of v(G)^(n0-1),
# v(G) = number of 0/1 slices G' with G'-G additive.  Memory: trivial.
import sys, itertools
n0,n1,n2=(int(a) for a in sys.argv[1:4])
cells=[(i,j) for i in range(n1) for j in range(n2)]
# all additive d with values in {-1,0,1}, as tuples over cells
adds=set()
for al in itertools.product(range(-1,2),repeat=n1):
    for be in itertools.product(range(-2,3),repeat=n2):
        d=tuple(al[i]+be[j] for i,j in cells)
        if all(-1<=v<=1 for v in d): adds.add(d)
adds=sorted(adds)
pos=[sum(1<<k for k,v in enumerate(d) if v==1) for d in adds]
neg=[sum(1<<k for k,v in enumerate(d) if v==-1) for d in adds]
tot=0
for G in range(1<<len(cells)):
    v=0
    for p,m in zip(pos,neg):
        if p&G==0 and m&~G==0: v+=1
    tot+=v**(n0-1)
print('grid',n0,n1,n2,'additive differences:',len(adds),'|B| =',tot)
