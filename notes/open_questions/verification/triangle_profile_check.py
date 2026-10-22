import itertools, sys
def carrier(T):
    NV=T+4
    def key(x):
        big=sorted(set(v for v in x if v>T)); return tuple(v if v<=T else T+1+big.index(v) for v in x)
    atoms=sorted({key(x) for x in itertools.product(range(NV),repeat=3)}); aidx={a:i for i,a in enumerate(atoms)}
    W=[(0,1),(1,2),(2,0)]
    def ptype(a,i,j):
        u,v=a[i],a[j]; return (u if u<=T else 'B', v if v<=T else 'B', ((u>v)-(u<v)) if (u>T and v>T) else 0)
    cells=[]
    for (i,j) in W:
        for t in {ptype(a,i,j) for a in atoms}:
            cells.append(sum(1<<aidx[a] for a in atoms if ptype(a,i,j)==t))
    full=(1<<len(atoms))-1
    D=set(cells)|{0,full}; fr=list(D)
    while fr:
        new=set(); L=list(D)
        for a in fr:
            c=full^a
            if c not in D: new.add(c)
            for b in L:
                if a&b==0 and (a|b) not in D: new.add(a|b)
        D|=new; fr=list(new)
    f1,f2,f3=T+1,T+2,T+3
    def far(order):  # atom with coords far out, ordered by order (first drawn smallest)
        x=[0,0,0]
        for rank,c in enumerate(order): x[c]=[f1,f2,f3][rank]
        return 1<<aidx[key(tuple(x))]
    orders=list(itertools.permutations(range(3)))
    def prof(m): return tuple(1 if m&far(o) else 0 for o in orders)
    def pt(d): return 1<<aidx[key(tuple(d.get(k,0) for k in range(3)))]
    z=pt({}); e=[pt({k:f1}) for k in range(3)]; pw=[pt({a:f1,b:f2}) for (a,b) in W]
    def Lam(m): return (1 if m&z else 0)-sum(1 for b in e if m&b)+sum(1 for b in pw if m&b)
    # halves: profile = [i before j] over orders
    halves=set()
    for (i,j) in W:
        h=tuple(1 if o.index(i)<o.index(j) else 0 for o in orders); halves.add(h); halves.add(tuple(1-v for v in h))
    allowed=halves|{(0,)*6,(1,)*6}
    W1=far((0,1,2)); W2=far((1,2,0)); W3=far((1,0,2))  # cut window2 -> 012, cut window0 -> 120, cut {0,2} -> 102
    bad_prof=sum(1 for m in D if prof(m) not in allowed)
    bad_id=sum(1 for m in D if Lam(m)!=(1 if m&W1 else 0)+(1 if m&W2 else 0)-(1 if m&W3 else 0))
    return len(atoms),len(D),bad_prof,bad_id
for T in (0,1):
    print('T=%d atoms,|D|,non-half profiles,identity failures:'%T, carrier(T)); sys.stdout.flush()
