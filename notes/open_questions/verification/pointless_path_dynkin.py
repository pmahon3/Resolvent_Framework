"""Dynkin closure of window events vs disjoint unions of window events (one per window).
Finite-alphabet check for the pointless-coherence kit, Problem path (c). 2026-10-15.
Output: path2/3/4 binary and path2 ternary: D == G; ring4: D == G; ring3: D != G (70 vs 66)."""
import itertools, sys
def run(A, n, windows):
    pts=list(itertools.product(range(A),repeat=n)); N=len(pts); full=(1<<N)-1
    gens=set()
    wev={}
    for w in windows:
        cells={}
        for i,x in enumerate(pts): cells.setdefault(tuple(x[j] for j in w),0); cells[tuple(x[j] for j in w)]|=1<<i
        cl=list(cells.values()); evs=set()
        for r in range(len(cl)+1):
            for c in itertools.combinations(cl,r): evs.add(sum(c))
        wev[w]=evs; gens|=evs
    # Dynkin closure
    D=set(gens)|{0,full}
    changed=True
    while changed:
        changed=False; L=list(D)
        new=set()
        for a in L:
            if full^a not in D: new.add(full^a)
        for i,a in enumerate(L):
            for b in L[i+1:]:
                if a&b==0 and (a|b) not in D: new.add(a|b)
        if new: D|=new; changed=True
    # G: disjoint unions of one event per window
    G={0}
    for w in windows:
        G={g|e for g in G for e in wev[w] if g&e==0}
    return len(D),len(G),D==G, G<=D
for A,n,W,name in [(2,3,[(0,1),(1,2)],'path2'),(2,4,[(0,1),(1,2),(2,3)],'path3'),(3,3,[(0,1),(1,2)],'path2 A3'),(2,5,[(0,1),(1,2),(2,3),(3,4)],'path4'),(2,3,[(0,1),(1,2),(2,0)],'ring3'),(2,4,[(0,1),(1,2),(2,3),(3,0)],'ring4')]:
    print(name, run(A,n,W)); sys.stdout.flush()
