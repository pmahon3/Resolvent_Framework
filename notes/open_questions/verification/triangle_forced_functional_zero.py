import itertools
L=3; W=[(0,1),(1,2),(2,0)]
def key(x):
    o=sorted(set(v for v in x if v)); return tuple(0 if v==0 else 1+o.index(v) for v in x)
P=list(itertools.product(range(4),repeat=3))
atoms=sorted({key(x) for x in P}); A=len(atoms); aidx={a:i for i,a in enumerate(atoms)}
def ptype(a,i,j):  # pair type of coords i,j in atom a
    u,v=a[i],a[j]; return (u==0, v==0, (u>v)-(u<v))
full=(1<<A)-1
wev=[]
for (i,j) in W:
    types=sorted({ptype(a,i,j) for a in atoms})
    for r in range(len(types)+1):
        for T in itertools.combinations(types,r):
            m=0
            for a in atoms:
                if ptype(a,i,j) in T: m|=1<<aidx[a]
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
def I(m,x): return (m>>aidx[key(x)])&1
z=(0,0,0)
def pt(d): return tuple(d.get(k,0) for k in range(3))
def Phi(m):
    v=I(m,z)+sum(I(m,pt({k:1}))-I(m,z) for k in range(3))
    for (a,b) in W:   # orientation +++ : lo=a drawn first, hi=b later
        v+=I(m,pt({a:1,b:2}))-I(m,pt({a:1}))-I(m,pt({b:1}))+I(m,z)
    return v
print('atoms',A,'|D_def|',len(D))
C=[sum(1<<aidx[a] for a in atoms if a[i]<a[j]) for (i,j) in W]  # note: key 0 < positives
print('Phi(C_k) =',[Phi(c) for c in C], ' C_k in D:',[c in D for c in C])
bad=[m for m in D if Phi(m) not in (0,1)]
print('sets in D_def with Phi not in {0,1}:',len(bad))
if bad:
    m=min(bad,key=lambda m:bin(m).count('1'))
    print('example Phi=',Phi(m),'atoms:',[atoms[i] for i in range(A) if m>>i&1])
