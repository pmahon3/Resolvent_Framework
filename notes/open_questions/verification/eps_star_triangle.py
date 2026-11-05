# epsilon* for the binary triangle: min eps s.t. exists joint Q on {0,1}^3 with
# TV(marg_ij Q, P_ij) <= eps for all three pairs. LP: variables q(8), t(3 pairs x 4 cells), eps.
import itertools, numpy as np
from scipy.optimize import linprog
pts=list(itertools.product([0,1],repeat=3)); pairs=[(0,1),(1,2),(2,0)]; cells=list(itertools.product([0,1],repeat=2))
def eps_star(P):
    nq=8; nt=12; n=nq+nt+1; c=np.zeros(n); c[-1]=1
    A=[];b=[]; Aeq=[];beq=[]
    Aeq.append([1]*nq+[0]*(nt+1)); beq.append(1)
    for k,(i,j) in enumerate(pairs):
        for m,cell in enumerate(cells):
            row=np.zeros(n)
            for a,x in enumerate(pts):
                if (x[i],x[j])==cell: row[a]=1
            ti=nq+4*k+m
            r1=row.copy(); r1[ti]=-1; A.append(r1); b.append(P[k][cell])     # marg - P <= t
            r2=-row.copy(); r2[ti]=-1; A.append(r2); b.append(-P[k][cell])   # P - marg <= t
        r=np.zeros(n); r[nq+4*k:nq+4*k+4]=0.5; r[-1]=-1; A.append(r); b.append(0)  # TV = 1/2 sum t <= eps
    res=linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*n)
    return res.fun
eq={(0,0):.5,(1,1):.5,(0,1):0,(1,0):0}; ne={(0,1):.5,(1,0):.5,(0,0):0,(1,1):0}
print("parity contradiction eps* =",round(eps_star([eq,eq,ne]),6))
# worst case over random families (incl. signalling) to see max eps*
rng=np.random.default_rng(0); best=0
for _ in range(3000):
    fam=[]
    for k in range(3):
        v=rng.dirichlet([0.3]*4); fam.append(dict(zip(cells,v)))
    best=max(best,eps_star(fam))
print("max eps* over 3000 random families (any, incl. inconsistent marginals) =",round(best,4))

# margin-consistent families: pair tables built from fixed single-variable marginals + a correlation per pair
def pair_table(pa,pb,r):
    # P(a=1)=pa, P(b=1)=pb, P(1,1)=r within Frechet bounds
    lo=max(0,pa+pb-1); hi=min(pa,pb); p11=lo+r*(hi-lo)
    return {(1,1):p11,(1,0):pa-p11,(0,1):pb-p11,(0,0):1-pa-pb+p11}
best=0; arg=None
for _ in range(4000):
    m=rng.uniform(0,1,3); rs=rng.uniform(0,1,3)
    fam=[pair_table(m[0],m[1],rs[0]),pair_table(m[1],m[2],rs[1]),pair_table(m[2],m[0],rs[2])]
    e=eps_star(fam)
    if e>best: best=e; arg=(m.round(2),rs.round(2))
print("max eps* over 4000 margin-consistent families =",round(best,4),arg)
