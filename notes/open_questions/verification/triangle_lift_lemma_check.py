"""Triangle: check the corner conditions of the 'lift' box used in the hand proof that E* is not in the
carrier (2026-10-17). Notation: gap(x) = min |x_i - x_j|; B_n = {gap <= n}; C / A = strict cyclic / anticyclic.
Lift box at a 012-point p=(a,b,c) (b-a, c-b >= 2n+2) with gamma=a+n+1, beta=c+n+1, a' >= beta+n+1:
corners (a,b,c) [+] and (a',b,c) [-] are in C; the other six must lie in A minus B_n (so f=0 there).
Rotations of the triangle (x0->x1->x2) give the lifts of the other two orders.
"""
import itertools, random
def gap(x): return min(abs(x[0]-x[1]), abs(x[1]-x[2]), abs(x[0]-x[2]))
def C(x): a,b,c=x; return (a<b<c) or (b<c<a) or (c<a<b)
def A(x): return len(set(x))==3 and not C(x)
bad=0; tried=0
for n in range(0,6):
    g=2*n+2
    for _ in range(3000):
        a=random.randint(0,50); b=a+g+random.randint(0,20); c=b+g+random.randint(0,20)
        gam=a+n+1; bet=c+n+1; a2=bet+n+1+random.randint(0,20)
        corners={(x0,x1,x2):(s0*s1*s2) for (x0,s0),(x1,s1),(x2,s2) in itertools.product(((a,1),(a2,-1)),((b,1),(bet,-1)),((c,1),(gam,-1)))}
        tried+=1
        ok = C((a,b,c)) and C((a2,b,c)) and gap((a2,b,c))>=g and corners[(a,b,c)]==1 and corners[(a2,b,c)]==-1
        for x,sg in corners.items():
            if x in ((a,b,c),(a2,b,c)): continue
            ok = ok and A(x) and gap(x)>n
        bad += not ok
print("lift boxes tried",tried,"failures",bad)
