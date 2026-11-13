# Sanity checks for stage 1: (i) the slice method reproduces |V01| = 23,206 on 2x3x3x3;
# (ii) the same reducibility test on the triangle 3^3 finds the known irreducible sets (72 cyclic orders + complements).
import itertools, numpy as np
exec(open('k4_3333_stage1.py').read().split("# --- reducibility test")[0].replace("print('admissible","pass #print('admissible"))
print('(i) slice method on 2x3x3x3: sum over F0 of admissible second slices =',int(cnt.sum()),'(closure count: 23206)')
S=T.reshape(-1,3,3,3).astype(np.int8); red=np.zeros(len(S),bool)
for ax in range(1,4):
    for a,b in itertools.combinations(range(3),2):
        diff=np.take(S,a,axis=ax)-np.take(S,b,axis=ax)              # (m,3,3): depends on at most one remaining axis?
        red|=(diff==diff[:,:1,:]).reshape(len(S),-1).all(1)|(diff==diff[:,:,:1]).reshape(len(S),-1).all(1)
irr=S[~red]; sizes=sorted(set(int(x.sum()) for x in irr))
E=np.array([[[int(((a<=b)+(b<c)+(c<a))==2) for c in range(3)] for b in range(3)] for a in range(3)],dtype=np.int8)
print('(ii) triangle 3^3: irreducible sets',len(irr),'sizes',sizes,'| E*∩[3]^3 irreducible:',any((x==E).all() for x in irr))
