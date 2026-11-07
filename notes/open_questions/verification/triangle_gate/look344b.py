# For the 1728 'odd' M-sets on 3x4x4: is each a disjoint union c ⊔ r with c a cyclic-order M-set and r ∈ D¹ (N1)?
import sys, itertools, numpy as np
from collections import Counter
sys.argv = ['x', '3', '4', '4']
exec(open('check5a_cyc.py').read().split("print('(iii)")[0])
odd = sorted(M - cyc); cm = np.array(sorted(M & cyc), dtype=np.uint64)
res = Counter(); ex = None
for m in odd:
    sub = cm[(cm & ~np.uint64(m)) == 0]
    ok = [int(c) for c in sub.tolist() if (m ^ int(c)) in N1]
    res["some r in R0"] += any((m ^ c) in R0 for c in ok)
    res[len(ok) > 0] += 1
    if ok and ex is None: ex = (m, ok[0])
print('odd decomposable as cyclic ⊔ D1:', dict(res))
if ex:
    m, c = ex; r = m ^ c
    print('example: |c|', bin(c).count('1'), '|r|', bin(r).count('1'), 'r in R0:', r in R0)
    print('r points', [p for p in pts if r >> idx[p] & 1])
