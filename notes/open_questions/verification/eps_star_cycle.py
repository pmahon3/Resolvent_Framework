# Iteration 1: eps* on binary L-cycles of pair views, vs V/L, where V = max violation of the
# cycle inequalities sum_{e in F} d_e - sum_{e notin F} d_e <= |F|-1 over odd F (Barahona–Mahjoub).
import itertools, numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(1)
def pair_table(pa,pb,r):
    lo=max(0,pa+pb-1); hi=min(pa,pb); p11=lo+r*(hi-lo)
    return {(1,1):p11,(1,0):pa-p11,(0,1):pb-p11,(0,0):1-pa-pb+p11}
cells=list(itertools.product([0,1],repeat=2))
def eps_star(L,fam):
    pts=list(itertools.product([0,1],repeat=L)); nq=len(pts); nt=4*L; n=nq+nt+1
    c=np.zeros(n); c[-1]=1; A=[];b=[]
    for k in range(L):
        i,j=k,(k+1)%L
        for m,cell in enumerate(cells):
            row=np.zeros(n)
            for a,x in enumerate(pts):
                if (x[i],x[j])==cell: row[a]=1
            ti=nq+4*k+m
            r1=row.copy(); r1[ti]=-1; A.append(r1); b.append(fam[k][cell])
            r2=-row; r2[ti]=-1; A.append(r2); b.append(-fam[k][cell])
        r=np.zeros(n); r[nq+4*k:nq+4*k+4]=.5; r[-1]=-1; A.append(r); b.append(0)
    Aeq=[[1]*nq+[0]*(nt+1)]
    return linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=[1],bounds=[(0,None)]*n).fun
def V_of(L,fam):
    d=[fam[k][(0,1)]+fam[k][(1,0)] for k in range(L)]; best=0
    for size in range(1,L+1,2):
        for F in itertools.combinations(range(L),size):
            v=sum(d[e] for e in F)-sum(d[e] for e in range(L) if e not in F)-(size-1)
            best=max(best,v)
    return best
for L in (3,4,5,6):
    worst=0; nv=0; maxe=0
    for t in range(800):
        m=rng.uniform(0,1,L); rs=rng.choice([0.,1.],L) if t%2==0 else rng.uniform(0,1,L)
        fam=[pair_table(m[k],m[(k+1)%L],rs[k]) for k in range(L)]
        e=eps_star(L,fam); v=V_of(L,fam)
        worst=max(worst,abs(e-v/L)); nv+=v>1e-9; maxe=max(maxe,e)
    print(f"L={L}: max|eps*-V/L|={worst:.2e}  violating={nv}/800  max eps*={maxe:.4f}  (1/L={1/L:.4f})")
