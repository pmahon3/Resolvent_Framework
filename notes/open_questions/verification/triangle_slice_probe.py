import itertools
A=3; W=[(0,1),(1,2),(2,0)]
pts=list(itertools.product(range(A),repeat=3)); idx={p:i for i,p in enumerate(pts)}; N=len(pts); full=(1<<N)-1
cells=[]
for (i,j) in W:
    c={}
    for k,x in enumerate(pts): c.setdefault((x[i],x[j]),0); c[(x[i],x[j])]|=1<<k
    cells+=list(c.values())
D=set(cells)|{0,full}; fr=list(D)
while fr:
    new=set(); L=list(D)
    for a in fr:
        cc=full^a
        if cc not in D: new.add(cc)
        for b in L:
            if a&b==0 and (a|b) not in D: new.add(a|b)
    D|=new; fr=list(new)
pairs=list(itertools.product(range(A),repeat=2))
for a in range(A):
    inD=0; tot=0
    for r in range(len(pairs)+1):
        for S in itertools.combinations(pairs,r):
            m=sum(1<<idx[(a,s1,s2)] for (s1,s2) in S); tot+=1; inD+= (m in D)
    print(f"slices x0={a}: {inD}/{tot} subsets S of (x1,x2) give a carrier set")
