"""Triangle carrier, finite alphabets (2026-10-15). A=2: |D|=70, every D-set or its complement is a disjoint
union of window fibres (G); "all equal" = {000,111} is in D \ G. A=3: |D|=15914, "all equal" NOT in D;
2088 sets with E, E^c both outside G; smallest = 9-point cyclic pattern. Basis for the puzzle in pointless_coherence.tex."""
import itertools
def run(A):
    W=[(0,1),(1,2),(2,0)]
    pts=list(itertools.product(range(A),repeat=3)); N=len(pts); full=(1<<N)-1
    wev={}
    for w in W:
        cells={}
        for i,x in enumerate(pts): cells.setdefault((x[w[0]],x[w[1]]),0); cells[(x[w[0]],x[w[1]])]|=1<<i
        cl=list(cells.values()); evs=set()
        for r in range(len(cl)+1):
            for c in itertools.combinations(cl,r): evs.add(sum(c))
        wev[w]=evs
    D=set().union(*wev.values())|{0,full}
    frontier=list(D)
    while frontier:
        new=set()
        L=list(D)
        for a in frontier:
            c=full^a
            if c not in D: new.add(c)
            for b in L:
                if a&b==0 and (a|b) not in D: new.add(a|b)
        D|=new; frontier=list(new)
        print(' |D| so far',len(D),flush=True)
        if len(D)>400000: print('too big'); return
    diag=sum(1<<i for i,x in enumerate(pts) if x[0]==x[1]==x[2])
    print('A=%d |D|=%d  all-equal in D: %s'%(A,len(D),diag in D))


def extras(A, maxsize=6):
    W=[(0,1),(1,2),(2,0)]
    pts=list(itertools.product(range(A),repeat=3)); N=len(pts); full=(1<<N)-1
    fib={}
    for w in W:
        cells={}
        for i,x in enumerate(pts): cells.setdefault((x[w[0]],x[w[1]]),0); cells[(x[w[0]],x[w[1]])]|=1<<i
        fib[w]=list(cells.values())
    wev={w:set() for w in W}
    for w in W:
        cl=fib[w]
        for r in range(len(cl)+1):
            for c in itertools.combinations(cl,r): wev[w].add(sum(c))
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
    def inG(S):
        # S = disjoint union of one fibre-union per window: search over which fibres (contained in S) to use
        cand=[(w,f) for w in W for f in fib[w] if f&S==f]
        # exact cover of S by disjoint fibres from cand (any windows) -- grouping by window is automatic
        def rec(rem,used):
            if rem==0: return True
            i=(rem&-rem)
            for w,f in cand:
                if f&i and f&rem==f and f&used==0:
                    if rec(rem^f,used|f): return True
            return False
        return rec(S,0)
    ex=[m for m in D if not inG(m) and not inG(full^m)]
    ex.sort(key=lambda m:bin(m).count('1'))
    print('A=%d: %d carrier sets, %d not a disjoint union of window fibres (nor complement)'%(A,len(D),len(ex)))
    for m in ex[:6]:
        print('  ',sorted(''.join(map(str,pts[i])) for i in range(N) if m>>i&1))
extras(2); extras(3)
