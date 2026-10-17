"""gate.triangle_graph_windows (2026-10-17): patterns with ties.
Windows: x1 = x0 (diagonal), x2 = x1 (diagonal), (x2,x0) product with x0 first. Ideal buildings = ordered set
partitions of {0,1,2} (blocks drawn in order, equal within a block). The forced functional is
  Lambda = W[01|2] + W[0|12] - W[0|1|2]     (checked window by window).
A 0/1 set on a homogeneous infinite P has a pattern: type -> {0,1}. Box identities (vanishing triple interaction)
over values from P (cross-coordinate ties allowed) constrain the pattern. List surviving patterns and their Lambda.
"""
import itertools
def otype(x):
    vals=sorted(set(x)); return tuple(tuple(i for i in range(3) if x[i]==v) for v in vals)
types=sorted({otype(x) for x in itertools.product(range(3),repeat=3)})
print("types",len(types))
cons=set()
V=range(6)
for a,a2,b,b2,c,c2 in itertools.product(V,repeat=6):
    if a==a2 or b==b2 or c==c2: continue
    vec={t:0 for t in types}
    for (x0,s0),(x1,s1),(x2,s2) in itertools.product(((a,1),(a2,-1)),((b,1),(b2,-1)),((c,1),(c2,-1))):
        vec[otype((x0,x1,x2))]+=s0*s1*s2
    t=tuple(vec[k] for k in types)
    if any(t): cons.add(t)
print("constraints",len(cons))
B=((0,1),(2,)); C=((0,),(1,2)); D=((0,),(1,),(2,))
iB,iC,iD=types.index(B),types.index(C),types.index(D)
surv=[]
for bits in itertools.product((0,1),repeat=len(types)):
    if all(sum(b*t for b,t in zip(bits,c))==0 for c in cons): surv.append(bits)
print("surviving 0/1 patterns",len(surv))
from collections import Counter
print("Lambda values",Counter(b[iB]+b[iC]-b[iD] for b in surv))
for b in surv:
    if b[iB]+b[iC]-b[iD] not in (0,1): print("BAD", {types[i]:b[i] for i in range(len(types)) if b[i]})
