"""Triangle over a finite alphabet {0..A-1}: enumerate ALL two-valued finitely additive states on the
glued carrier D (Dynkin closure of the three pair-window events) and check whether each is a point.
Audit flag 2026-10-17: 'every finite-alphabet state is a point' was asserted without proof.
Usage: python3 triangle_finite_states_check.py 2
"""
import itertools, sys
A=int(sys.argv[1]) if len(sys.argv)>1 else 2
pts=list(itertools.product(range(A),repeat=3)); n=len(pts); full=(1<<n)-1
W=[(0,1),(1,2),(2,0)]
gens=set()
for i,j in W:
    for S in range(1<<(A*A)):
        m=0
        for k,x in enumerate(pts):
            if S>>(x[i]*A+x[j])&1: m|=1<<k
        gens.add(m)
D=set(gens)|{0,full}; fr=list(D)
while fr:
    new=set(); L=list(D)
    for a in fr:
        if full^a not in D: new.add(full^a)
        for b in L:
            if a&b==0 and (a|b) not in D: new.add(a|b)
    D|=new; fr=list(new)
D=sorted(D); idx={m:i for i,m in enumerate(D)}
print("A",A,"points",n,"|D|",len(D))
# two-valued state: s(full)=1, s(E)+s(E^c)=1, s(a|b)=s(a)+s(b) for disjoint a,b in D. Backtracking with propagation.
pairs=[(a,b) for a in D for b in D if a<b and a&b==0 and (a|b) in idx]
def solve():
    sols=[]
    val={full:1,0:0}
    def consistent(val):
        for a,b in pairs:
            u=a|b
            if a in val and b in val and u in val and val[a]+val[b]!=val[u]: return False
            if a in val and b in val and val[a]+val[b]>1: return False
        return True
    order=[m for m in D if m not in (0,full)]
    def propagate(val):
        changed=True
        while changed:
            changed=False
            for m in list(val):
                c=full^m
                if c not in val: val[c]=1-val[m]; changed=True
                elif val[c]!=1-val[m]: return False
            for a,b in pairs:
                u=a|b; ka,kb,ku=a in val,b in val,u in val
                if ka and kb:
                    s=val[a]+val[b]
                    if s>1: return False
                    if not ku: val[u]=s; changed=True
                    elif val[u]!=s: return False
                elif ku and val[u]==0:
                    if not ka: val[a]=0; changed=True
                    if not kb: val[b]=0; changed=True
                elif ku and ka and not kb: val[b]=val[u]-val[a]; changed=True
                elif ku and kb and not ka: val[a]=val[u]-val[b]; changed=True
                if (a in val and val[a]<0) or (b in val and val[b]<0): return False
        return True
    def rec(val):
        if not propagate(val): return
        free=[m for m in order if m not in val]
        if not free: sols.append(dict(val)); return
        m=free[0]
        for v in (1,0):
            v2=dict(val); v2[m]=v; rec(v2)
    rec(val); return sols
sols=solve()
pointlike=0
for s in sols:
    true=[m for m in D if s[m]==1]
    inter=full
    for m in true: inter&=m
    if inter and all((m&inter)==inter if s[m] else (m&inter)==0 for m in D): pointlike+=1
print("two-valued states",len(sols),"points",pointlike,"pointless",len(sols)-pointlike)
