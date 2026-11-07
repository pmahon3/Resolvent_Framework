# (3) On 2 x n1 x n2: every 0/1 box set is (a) a disjoint union of three window events, or
# (b) K(U,V) ⊔ G with K = {1}xUxV ⊔ {0}xU^c xV^c and G a {1,2}-window event.  Check by enumeration.
import itertools, sys
n1,n2=int(sys.argv[1]),int(sys.argv[2])
pts=list(itertools.product(range(2),range(n1),range(n2)))
free=[p for p in pts if 0 in p]
def boxsets():
    for m in range(1<<len(free)):
        v={p:(m>>i)&1 for i,p in enumerate(free)}; ok=True
        for p in pts:
            if p in v: continue
            x0,x1,x2=p
            val=v[(x0,x1,0)]+v[(0,x1,x2)]+v[(x0,0,x2)]-v[(x0,0,0)]-v[(0,x1,0)]-v[(0,0,x2)]+v[(0,0,0)]
            if val not in (0,1): ok=False;break
            v[p]=val
        if ok: yield frozenset(p for p in pts if v[p])
def is_R0(E):
    # E = A01 ⊔ B12 ⊔ C20 ; decide by trying: for each x1-value choose whether 01 or not... brute force over
    # assignment of each point to a window, via the slice-difference characterisation instead:
    d={(b,c):((1,b,c) in E)-((0,b,c) in E) for b in range(n1) for c in range(n2)}
    dep1=all(d[(b,c)]==d[(b,0)] for b in range(n1) for c in range(n2))
    dep2=all(d[(b,c)]==d[(0,c)] for b in range(n1) for c in range(n2))
    if not(dep1 or dep2): return False
    # explicit decomposition check
    if dep2:
        Z={c for c in range(n2) if d[(0,c)]==1}; Zp={c for c in range(n2) if d[(0,c)]==-1}
        A=set(); B={p for p in pts if p[2] not in Z|Zp and (0,p[1],p[2]) in E}
        C={p for p in pts if (p[2] in Z and p[0]==1) or (p[2] in Zp and p[0]==0)}
    else:
        Z={b for b in range(n1) if d[(b,0)]==1}; Zp={b for b in range(n1) if d[(b,0)]==-1}
        B={p for p in pts if p[1] not in Z|Zp and (0,p[1],p[2]) in E}
        A={p for p in pts if (p[1] in Z and p[0]==1) or (p[1] in Zp and p[0]==0)}; C=set()
    return (A|B|C)==set(E) and not (A&B or B&C or A&C)
def is_KG(E):
    d={(b,c):((1,b,c) in E)-((0,b,c) in E) for b in range(n1) for c in range(n2)}
    for U in itertools.product((0,1),repeat=n1):
        for V in itertools.product((0,1),repeat=n2):
            if all(d[(b,c)]==U[b]+V[c]-1 for b in range(n1) for c in range(n2)):
                Kset={p for p in pts if (p[0]==1 and U[p[1]] and V[p[2]]) or (p[0]==0 and not U[p[1]] and not V[p[2]])}
                rest=set(E)-Kset
                if Kset<=set(E) and all(((0,p[1],p[2]) in rest)==((1,p[1],p[2]) in rest) for p in pts): return True
    return False
tot=bad=0
for E in boxsets():
    tot+=1
    if not(is_R0(E) or is_KG(E)): bad+=1
print('2x%dx%d: box sets'%(n1,n2),tot,'not of form R0 or K+G:',bad)
