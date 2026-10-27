import itertools, sys, numpy as np, cdd, networkx as nx
from fractions import Fraction as Fr
from scipy.optimize import linprog
sz = tuple(int(x) for x in sys.argv[1].split(','))
E = [(0, 1), (1, 2), (2, 0)]
pts = list(itertools.product(*[range(s) for s in sz])); N=len(pts); full=(1<<N)-1
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
CS = [frozenset(t for t,p in enumerate(pts) if p[E[e][0]]==a and p[E[e][1]]==b) for (e,a,b) in cells]
# exact D closure
gens=set()
for (i,j) in E:
    for S in range(1<<(sz[i]*sz[j])):
        gens.add(sum(1<<t for t,p in enumerate(pts) if S>>(p[i]*sz[j]+p[j])&1))
D=gens|{0,full}; fr=list(D)
while fr:
    new=set(); L=list(D)
    for a in fr:
        if full^a not in D: new.add(full^a)
        for b in L:
            if a&b==0 and (a|b) not in D: new.add(a|b)
    D|=new; fr=list(new)
print("|D|=",len(D),flush=True)
M = np.array([[1 if t in CS[k] else 0 for k in range(len(cells))] for t in range(N)])
H = cdd.copy_inequalities(cdd.polyhedron_from_matrix(cdd.matrix_from_array([[1]+list(r) for r in M], rep_type=cdd.RepType.GENERATOR)))
lin=set(H.lin_set); facets=[np.array(H.array[i],float) for i in range(len(H.array)) if i not in lin]
G=nx.Graph(); G.add_nodes_from(range(len(cells)))
for k in range(len(cells)):
    for l in range(k+1,len(cells)):
        if not (CS[k]&CS[l]): G.add_edge(k,l)
cliques=[q for q in nx.find_cliques(G) if len(q)>1]
A_ub=[]; 
for q in cliques:
    r=np.zeros(len(cells)); r[q]=1; A_ub.append(r)
A_eq=[];b_eq=[]
for e in range(3):
    r=np.zeros(len(cells)); r[[k for k,c in enumerate(cells) if c[0]==e]]=1; A_eq.append(r); b_eq.append(1)
for v in range(3):
    (e1,p1),(e2,p2)=[(e,pos) for e in range(3) for pos in (0,1) if E[e][pos]==v]
    for val in range(sz[v]):
        r=np.zeros(len(cells))
        for k,c in enumerate(cells):
            if c[0]==e1 and c[1+p1]==val: r[k]+=1
            if c[0]==e2 and c[1+p2]==val: r[k]-=1
        A_eq.append(r); b_eq.append(0)
viol=0; inD=0; exact_checked=0
for f in facets:
    b0,a=f[0],f[1:]
    res=linprog(a,A_ub=np.array(A_ub),b_ub=np.ones(len(cliques)),A_eq=np.array(A_eq),b_eq=b_eq,bounds=[(0,None)]*len(cells),method='highs')
    if b0+res.fun < -1e-8:
        viol+=1
        g=b0+M@a; S=sum(1<<t for t in range(N) if g[t]>1e-9)
        if S in D: inD+=1
        # exact check of the minimiser: rationalise and verify constraints and value of 1_S
        mu=[Fr(x).limit_denominator(1000) for x in res.x]
        ok = all(m>=0 for m in mu) and all(sum(mu[k] for k in q)<=1 for q in cliques)
        ok = ok and all(sum(Fr(int(r[k]))*mu[k] for k in range(len(cells)))==bb for r,bb in zip(A_eq,b_eq))
        # value of mu on 1_S: solve M c = 1_S exactly via least squares then rationalise; check M c == 1_S
        c=np.linalg.lstsq(M.astype(float),np.array([1.0 if (S>>t)&1 else 0 for t in range(N)]),rcond=None)[0]
        cr=[Fr(x).limit_denominator(1000) for x in c]
        assert all(sum(int(M[t,k])*cr[k] for k in range(len(cells)))==((S>>t)&1) for t in range(N))
        val=sum(cr[k]*mu[k] for k in range(len(cells)))
        if ok and val<0: exact_checked+=1
print(f"{sz}: violated facets {viol}; supports in D: {inD}; exactly verified CE1 point with mu(S)<0: {exact_checked}")
