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
rot=[(0,1,2),(1,2,0),(2,0,1)]; rev=[(0,2,1),(1,0,2),(2,1,0)]
R=sum(1<<idx[p] for p in rot); V=sum(1<<idx[p] for p in rev)
bad=[m for m in D if m&R==R and m&V==0]
bad2=[m for m in D if m&V==V and m&R==0]
print('|D|',len(D),' sets with all rotations & no reversals:',len(bad),' mirror:',len(bad2))
# sanity: the advisor's explicit E* in the span
def inV(m):  # zero triple interaction on the 3x3x3 box
    f=lambda x:(m>>idx[x])&1
    for a,a2 in itertools.combinations(range(A),2):
        for b,b2 in itertools.combinations(range(A),2):
            for c,c2 in itertools.combinations(range(A),2):
                s=0
                for (x,sx) in ((a,1),(a2,-1)):
                    for (y,sy) in ((b,1),(b2,-1)):
                        for (z,sz) in ((c,1),(c2,-1)):
                            s+=sx*sy*sz*f((x,y,z))
                if s: return False
    return True
Estar=sum(1<<idx[x] for x in pts if (x[0]<=x[1])+(x[1]<x[2])+(x[2]<x[0])==2)
vals={(x[0]<=x[1])+(x[1]<x[2])+(x[2]<x[0])-1 for x in pts}
print('E* in span:',inV(Estar),' sum-1 values on all points:',sorted(vals),' E* in D:',Estar in D, ' contains rotations & no reversals:', Estar&R==R and Estar&V==0)
