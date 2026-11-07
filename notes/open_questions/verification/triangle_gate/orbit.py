# Is D3\Q on 3x3x3 (sets needing rank 2) exactly the orbit of E*∩[3]^3 under independent relabelings of each coordinate?
import itertools, numpy as np, sys
exec(open('kform.py').read().split("print('|D|'")[0])
Q=Uclose(W|Ks); new=D-Q
print('|D|',len(D),'|Q|',len(Q),'|D\\Q|',len(new))
def pts_of(m): return [p for p in pts if m>>idx[p]&1]
Es=mask(lambda p:((p[0]<=p[1])+(p[1]<p[2])+(p[2]<p[0]))==2)
print('E* in new:',Es in new, '|E*∩[3]^3|',bin(Es).count('1'))
orb=set()
for s0 in itertools.permutations(range(3)):
 for s1 in itertools.permutations(range(3)):
  for s2 in itertools.permutations(range(3)):
    orb.add(mask(lambda p:((s0[p[0]]<=s1[p[1]])+(s1[p[1]]<s2[p[2]])+(s2[p[2]]<s0[p[0]]))==2))
orbc={m^FULL for m in orb}
print('|orbit|',len(orb),'orbit==new:',orb==new,'orbit∪complements==new:',(orb|orbc)==new, '|new∩orb|',len(new&orb))
for m in list(new)[:2]: print(sorted(pts_of(m)))
