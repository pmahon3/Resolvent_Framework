import itertools
# (1) E* indicator is the 0/1 pair-sum [x0<=x1]+[x1<x2]+[x2<x0]-1  (so E* satisfies Box)
for n in range(1,9):
    for x in itertools.product(range(n),repeat=3):
        x0,x1,x2=x; s=(x0<=x1)+(x1<x2)+(x2<x0)
        assert s in (1,2)
        assert (s==2)==((x0<=x1)+(x1<x2)+(x2<x0)==2)
print('(1) E* = pair-sum - 1, values in {0,1}: OK n<=8')
# (2) nondegenerate antipodal cube pairs K(S): disjoint => some coordinate equal or complementary
def K(S,n):
    return frozenset(p for p in itertools.product(*[range(k) for k in n])
       if all(p[i] in S[i] for i in range(3)) or all(p[i] not in S[i] for i in range(3)))
for n in [(3,3,4),(3,4,4),(4,4,4)]:
    props=[[frozenset(c for c in range(k) if m>>c&1) for m in range(1,(1<<k)-1)] for k in n]
    Ss=list(itertools.product(*props)); Kd={S:K(S,n) for S in Ss}
    bad=0; pairs=0
    for a in range(len(Ss)):
        S=Ss[a]; KS=Kd[S]
        for b in range(a+1,len(Ss)):
            T=Ss[b]
            if KS.isdisjoint(Kd[T]):
                pairs+=1
                full=[frozenset(range(k)) for k in n]
                if not any(T[i]==S[i] or T[i]==full[i]-S[i] for i in range(3)): bad+=1
    print('(2)',n,'disjoint nondegenerate pairs',pairs,'violations',bad)
