"""Triangle staircase: the FORCED values. Any state extending the window ultrafilters p(x)p (+++) must equal
Lambda(f) = sum_k lim_{u_k} f_k on every FINITELY built question (indicator = f0(x0,x1)+f1(x1,x2)+f2(x2,x0);
Lambda well defined because zero-sum triples are coboundaries + constants and marginals agree).
This checks Lambda in {0,1} on definable (order + thresholds <= T) finitely built questions.
Results 2026-10-16: T=0: 26 atoms, 430 sets, 0 bad; T=1: 51 atoms, 74738 sets, 0 bad. Necessary condition only."""
import itertools,sys
def run(T, NV):
    W=[(0,1),(1,2),(2,0)]
    def key(x):
        big=sorted(set(v for v in x if v>T))
        return tuple(v if v<=T else T+1+big.index(v) for v in x)
    P=list(itertools.product(range(NV),repeat=3))
    atoms=sorted({key(x) for x in P}); A=len(atoms); aidx={a:i for i,a in enumerate(atoms)}
    def ptype(a,i,j):
        u,v=a[i],a[j]
        cu=u if u<=T else 'B'; cv=v if v<=T else 'B'
        return (cu,cv,(u>v)-(u<v) if (u>T and v>T) else 0)
    full=(1<<A)-1; wev=[]
    for (i,j) in W:
        types=sorted({ptype(a,i,j) for a in atoms},key=str)
        for r in range(len(types)+1):
            for Tset in itertools.combinations(types,r):
                m=0
                for a in atoms:
                    if ptype(a,i,j) in Tset: m|=1<<aidx[a]
                wev.append(m)
    D=set(wev)|{0,full}; frontier=list(D)
    while frontier:
        new=set(); Lst=list(D)
        for a in frontier:
            c=full^a
            if c not in D: new.add(c)
            for b in Lst:
                if a&b==0 and (a|b) not in D: new.add(a|b)
        D|=new; frontier=list(new)
        if len(D)>400000: return ('too big',len(D))
    def I(m,x): return (m>>aidx[key(x)])&1
    base=0; f1=T+1; f2=T+2
    def pt(d): return tuple(d.get(k,base) for k in range(3))
    def Phi(m):
        z=pt({}); v=I(m,z)+sum(I(m,pt({k:f1}))-I(m,z) for k in range(3))
        for (a,b) in W: v+=I(m,pt({a:f1,b:f2}))-I(m,pt({a:f1}))-I(m,pt({b:f1}))+I(m,z)
        return v
    bad=sum(1 for m in D if Phi(m) not in (0,1))
    return (A,len(D),bad)
for T,NV in [(1,6),(2,7)]:
    print('T=%d'%T, run(T,NV)); sys.stdout.flush()
