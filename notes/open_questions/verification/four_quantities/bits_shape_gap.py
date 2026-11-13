# gate.four_loop (views_across_records/FOUR_LOOP_GATE.md). Two values per quantity, any graph of seen pairs.
# V01: exact, via the polynomial form f(x) = c0 + sum_i c_i x_i + sum_{ij seen} c_ij x_i x_j (integer arithmetic).
# D: closure of all pair events under complement and disjoint union, run to a fixed point (Python integers as masks).
import itertools, sys, numpy as np
def run(name,m,edges,verbose=True):
    pts=list(itertools.product([0,1],repeat=m)); N=len(pts); FULL=(1<<N)-1
    terms=[()]+[(i,) for i in range(m)]+[tuple(e) for e in edges]; r=len(terms)
    E=np.array([[int(all(p[i] for i in t)) for t in terms] for p in pts],dtype=np.int64)          # N x r monomial values
    info=[tuple(1 if i in t else 0 for i in range(m)) for t in terms]                             # points with that support
    T=np.array([[int(all(q[i] for i in t)) for t in terms] for q in info],dtype=np.int64)        # r x r unitriangular
    Tinv=np.rint(np.linalg.inv(T)).astype(np.int64); assert (T@Tinv==np.eye(r,dtype=np.int64)).all()
    V=set()
    for s in range(0,1<<r,1<<16):
        c=np.arange(s,min(s+(1<<16),1<<r)); v=((c[:,None]>>np.arange(r))&1).astype(np.int64)     # values on info points
        f=(v@Tinv.T)@E.T; ok=((f==0)|(f==1)).all(1)
        for row in f[ok]: V.add(int(''.join(map(str,row[::-1])),2))
    gens=set()
    for (i,j) in edges:
        cells=[sum(1<<k for k,p in enumerate(pts) if (p[i],p[j])==ab) for ab in itertools.product([0,1],repeat=2)]
        for mask in range(16): gens.add(sum(cells[k] for k in range(4) if mask>>k&1))
    D=set(gens); fr=set(gens)
    while fr:
        new=set(); L=list(D)
        for x in fr:
            if FULL^x not in D: new.add(FULL^x)
            for y in L:
                if x&y==0 and (x|y) not in D: new.add(x|y)
        new-=D; D|=new; fr=new
    assert D<=V
    if verbose: print('%-28s |D| %5d  |V01| %5d  gap %3d'%(name,len(D),len(V),len(V)-len(D)),flush=True)
    return pts,V,D
cyc=lambda L:[(i,(i+1)%L) for i in range(L)]
pts,V,D=run('C4',4,cyc(4))
# images of A4 on four bits: relabel values, reorder quantities, complement
A=np.zeros((2,2,2,2),int)
for p,u,v,t in itertools.product(range(2),repeat=4):
    if (u,v,t) in [(0,1,1),(1,0,0)] or (p,u,v) in [(0,0,0),(1,1,1)]: A[p,u,v,t]=1
orbit=set()
for perm in itertools.permutations(range(4)):
    q=np.transpose(A,perm)
    for flips in itertools.product([0,1],repeat=4):
        rr=q
        for ax,fl in enumerate(flips):
            if fl: rr=np.flip(rr,axis=ax)
        for z in (rr,1-rr): orbit.add(sum(1<<k for k,pt in enumerate(pts) if z[pt]))
print('   C4 gap sets are images of A4:',(V-D)<=orbit,'| images of A4 that add up on C4:',len(orbit&V),'| of those buildable:',len(orbit&D))
run('C5',5,cyc(5)); run('C6',6,cyc(6)); run('C7',7,cyc(7))
run('C6 + long chord 03',6,cyc(6)+[(0,3)]); run('C6 + short chord 02',6,cyc(6)+[(0,2)])
run('K2,3',5,[(a,b) for a in (0,1) for b in (2,3,4)])
run('C5 + chord 02',5,cyc(5)+[(0,2)]); run('K4 minus an edge',4,cyc(4)+[(0,2)])
