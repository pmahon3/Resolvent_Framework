"""Oracle: does the cyclic-order window pattern (x_k < x_{k+1} true in every ring window,
emulating the ordered ultrafilter p(x)p on each window) propagate to a consistent two-valued
additive assignment on the Dynkin closure of order+threshold window atoms?  Order/threshold
constraints have the same satisfiability over N as over {0..N-1} once N > T+4, so the finite
closure is a faithful model of the corresponding sub-carrier of the N-valued (or R-valued) ring.
See notes/open_questions/delay_embedding/collision_vs_generation.md, "Candidate witness"."""
import itertools, sys, time
W=[(0,1),(1,2),(2,3),(3,0)]
def run(T, N, maxD=200000):
    pts=list(itertools.product(range(N),repeat=4)); P=len(pts); full=(1<<P)-1
    cls=lambda v: min(v,T)          # threshold class: 0..T-1 exact-ish, T = "beyond"
    atoms=[]; val=[]
    hi=(T+1,T+2)                    # generic window point: both beyond thresholds, ordered
    for (a,b) in W:
        keyf=lambda p,a=a,b=b:(cls(p[a]),cls(p[b]),(p[a]>p[b])-(p[a]<p[b]))
        groups={}
        for i,p in enumerate(pts): groups.setdefault(keyf(p),0); groups[keyf(p)]|=1<<i
        g=(cls(hi[0]),cls(hi[1]),-1)
        for k,m in groups.items(): atoms.append(m); val.append(1 if k==g else 0)
    # functional via disjoint-union evaluation: a set is valued if it is a disjoint union of atoms of ONE window
    D={0:0,full:1}; 
    for m,v in zip(atoms,val): D[m]=v
    for w in range(4):
        A=[(atoms[j],val[j]) for j in range(len(atoms)) if j//((T+1)**2*3)==w]
    frontier=list(D.items()); t0=time.time()
    while frontier:
        nf=[]
        items=list(D.items())
        for a,va in frontier:
            c=full^a; vc=1-va
            for (s,vs) in [(c,vc)]+[(a|b,va+vb) for b,vb in items if a&b==0 and b]:
                if s in D:
                    if D[s]!=vs: return ("CONTRADICTION",len(D),s,D[s],vs,pts)
                else:
                    if vs not in (0,1): return ("OFF-RANGE",len(D),s,None,vs,pts)
                    D[s]=vs; nf.append((s,vs))
        frontier=nf
        if len(D)>maxD: return ("TOO BIG",len(D))
    return ("CONSISTENT two-valued on closure",len(D))
for T,N in [(1,6),(2,7)]:
    r=run(T,N); print("T=%d N=%d:"%(T,N), r[:2] if len(r)<4 else r[:5][:2]+(r[3],r[4]))
    if r[0] in("CONTRADICTION","OFF-RANGE"):
        s=r[2];pts=r[5];S=[pts[i] for i in range(len(pts)) if s>>i&1];print("  witness set size",len(S),S[:8])
