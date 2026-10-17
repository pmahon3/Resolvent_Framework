"""Dynkin closure D of pair-window events vs G = disjoint unions of one window event per window.
Locality theorem (pointless_coherence.tex, thm:star): D = G iff the window graph is triangle-free
(windows form a Helly family). Run 2026-10-16:
  star K13 (64,64,True); tree path+branch (84,84,True); 4-cycle (82,82,True); 5-cycle (102,102,True);
  K23 (144,144,True); triangle (70,66,False); triangle+pendant (98,94,False);
  4-cycle+chord (148,132,False); star K13 ternary (8000,8000,True)."""
import itertools,sys
def run(A, n, windows):
    pts=list(itertools.product(range(A),repeat=n)); N=len(pts); full=(1<<N)-1
    wev={}
    for w in windows:
        cells={}
        for i,x in enumerate(pts): cells.setdefault((x[w[0]],x[w[1]]),0); cells[(x[w[0]],x[w[1]])]|=1<<i
        cl=list(cells.values()); evs=set()
        for r in range(len(cl)+1):
            for c in itertools.combinations(cl,r): evs.add(sum(c))
        wev[w]=evs
    D=set().union(*wev.values())|{0,full}
    frontier=list(D)
    while frontier:
        new=set(); L=list(D)
        for a in frontier:
            c=full^a
            if c not in D: new.add(c)
            for b in L:
                if a&b==0 and (a|b) not in D: new.add(a|b)
        D|=new; frontier=list(new)
    G={0}
    for w in windows: G={g|e for g in G for e in wev[w] if g&e==0}
    return (len(D),len(G),D==G)
if __name__=='__main__':
    tests=[('star K13',2,4,[(0,1),(0,2),(0,3)]),('tree path+branch',2,5,[(0,1),(1,2),(2,3),(1,4)]),
           ('4-cycle',2,4,[(0,1),(1,2),(2,3),(3,0)]),('5-cycle',2,5,[(0,1),(1,2),(2,3),(3,4),(4,0)]),
           ('K23',2,5,[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),('triangle',2,3,[(0,1),(1,2),(2,0)]),
           ('triangle+pendant',2,4,[(0,1),(1,2),(2,0),(2,3)]),('4-cycle+chord',2,4,[(0,1),(1,2),(2,3),(3,0),(0,2)])]
    for name,A,n,W in tests: print(name,run(A,n,W)); sys.stdout.flush()
