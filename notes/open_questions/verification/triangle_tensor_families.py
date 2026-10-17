"""All 27 tensor-type window families on the triangle (each window: diagonal, or product in one of its two
orders; all slot ultrafilters p). For each: solve the forced functional as a signed sum of the 13 ordered-partition
buildings, list the 0/1 tie-patterns allowed by every box identity, and check that every pattern with
Lambda outside {0,1} agrees on the 6 strict orders with the cyclic or the anticyclic set.
If so, Lean's not_inP_of_mem + ultrafilter Ramsey give: the family extends to a state on D3 (2026-10-17).
"""
import itertools
from fractions import Fraction
import sympy as sp
def otype(x):
    vals=sorted(set(x)); return tuple(tuple(i for i in range(3) if x[i]==v) for v in vals)
types=sorted({otype(x) for x in itertools.product(range(3),repeat=3)})
def wtype(pi,i,j):   # what building pi says on window (i,j): 'D' diagonal, 'ij' i first, 'ji'
    bi=[k for k,b in enumerate(pi) if i in b][0]; bj=[k for k,b in enumerate(pi) if j in b][0]
    return 'D' if bi==bj else ('ij' if bi<bj else 'ji')
W=[(0,1),(1,2),(2,0)]
cons=set()
for a,a2,b,b2,c,c2 in itertools.product(range(6),repeat=6):
    if a==a2 or b==b2 or c==c2: continue
    vec={t:0 for t in types}
    for (x0,s0),(x1,s1),(x2,s2) in itertools.product(((a,1),(a2,-1)),((b,1),(b2,-1)),((c,1),(c2,-1))):
        vec[otype((x0,x1,x2))]+=s0*s1*s2
    t=tuple(vec[k] for k in types)
    if any(t): cons.add(t)
surv=[bits for bits in itertools.product((0,1),repeat=13) if all(sum(b*t for b,t in zip(bits,c))==0 for c in cons)]
strict=[t for t in types if len(t)==3]
def cyc(t):   # t = ((a,),(b,),(c,)) order from smallest
    o=tuple(b[0] for b in t); return o in ((0,1,2),(1,2,0),(2,0,1))
allok=True
for fam in itertools.product(['D','ij','ji'],repeat=3):
    rows=[];rhs=[]
    for (i,j),target in zip(W,fam):
        for val in ('D','ij','ji'):
            rows.append([1 if wtype(pi,i,j)==val else 0 for pi in types]); rhs.append(1 if val==target else 0)
    M=sp.Matrix(rows); bvec=sp.Matrix(rhs)
    sol,params=M.gauss_jordan_solve(bvec)
    c=sol.subs({p:0 for p in params})
    lam=[sum(c[k]*b[k] for k in range(13)) for b in surv]
    bad=[b for b,l in zip(surv,lam) if l not in (0,1)]
    kinds=[]
    for b in bad:
        sb=tuple(b[types.index(t)] for t in strict)
        if all(sb[k]==(1 if cyc(t) else 0) for k,t in enumerate(strict)): kinds.append('cyc')
        elif all(sb[k]==(0 if cyc(t) else 1) for k,t in enumerate(strict)): kinds.append('acy')
        else: kinds.append('OTHER'); allok=False
    print(fam, "bad patterns:",len(bad), sorted(set(kinds)))
print("ALL bad patterns cyclic/anticyclic on strict orders:",allok)
