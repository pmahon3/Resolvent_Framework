"""gate.triangle_lambda2_agreement, branch (b) witness (2026-10-17).
F_S = E* + [x0 in S]([x1 < x0] - [x2 < x0]): a sum of window functions (so zero triple interaction).
Check: 0/1-valued; equals {x1 < x2}-type on slices x0 in S (up to ties), E* elsewhere; so for S p-small it has
the cyclic profile (Lambda = 2) yet differs from E* on the unbounded non-band region {x0 in S}.
"""
import itertools
def E(x0,x1,x2): return int(int(x1>=x0)+int(x2>=x1+1)+int(x0>=x2+1)==2)
N=40; S=set(range(1,N,2)); bad=0; dev=0; far_dev=0
for x0,x1,x2 in itertools.product(range(N),repeat=3):
    v=E(x0,x1,x2)+(int(x1<x0)-int(x2<x0) if x0 in S else 0)
    bad+= v not in (0,1)
    if v!=E(x0,x1,x2):
        dev+=1
        if min(abs(x0-x1),abs(x1-x2),abs(x0-x2))>5 and min(x0,x1,x2)>5: far_dev+=1
print("points",N**3,"non-0/1",bad,"deviations from E*",dev,"far deviations (gaps>5, min>5)",far_dev)
