# 5BC check: (i) box_of_mem => no nonempty set inside a product of proper subsets is in D3 (spare value on EVERY coord).
# Test on 3^3: no nonempty carrier set avoids value 2 on all three coords; also count sets avoiding a spare on 1 or 2 coords.
# (ii) Lambda well-definedness / 5c general form on random coordinatewise maps is hand-checked; here: E*_n pair-sum identity.
import itertools, numpy as np
exec(open('pstack_control.py').read().split('p3,D3=closure')[0])
pts,D=closure((3,3,3))
toset=lambda m: [p for k,p in enumerate(pts) if m>>k&1]
for spare in [(0,),(0,1),(0,1,2)]:
    c=sum(1 for m in D if m and all(all(p[i]!=2 for i in spare) for p in toset(m)))
    print('nonempty carrier sets of 3^3 avoiding value 2 on coords',spare,':',c)
# E* pair-sum identity: count of [x0<=x1],[x1<x2],[x2<x0] is always 1 or 2
print('E* count in {1,2} on [7]^3:',all(((a<=b)+(b<c)+(c<a)) in (1,2) for a,b,c in itertools.product(range(7),repeat=3)))
# Etilde_n -> E* pointwise, not monotone: examples
E=lambda x:((x[0]<=x[1])+(x[1]<x[2])+(x[2]<x[0]))==2
cap=lambda x,n:tuple(min(v,n-1) for v in x)
for x in [(5,3,0),(5,0,3)]:
    print(x,'E*',E(x),'Etilde_n for n=1..7',[int(E(cap(x,n))) for n in range(1,8)])
