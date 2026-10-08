"""Oracle: Dynkin closure of glued binary delay windows; is it intersection-closed?
See notes/open_questions/delay_embedding/collision_vs_generation.md (bridge hypothesis)."""
import itertools
from fractions import Fraction as Fr
def run(n, windows, alph=2):
    pts=list(itertools.product(range(alph),repeat=n)); N=len(pts); full=(1<<N)-1
    def ev(pred): return sum(1<<i for i,p in enumerate(pts) if pred(p))
    gens=set()
    for w in windows:
        vals=list(itertools.product(range(alph),repeat=len(w)))
        for k in range(1<<len(vals)):
            S={vals[j] for j in range(len(vals)) if k>>j&1}
            gens.add(ev(lambda p,S=S,w=w: tuple(p[i] for i in w) in S))
    D=set(gens)|{0,full}
    while True:
        new={full^a for a in D}|{a|b for a in D for b in D if a&b==0}
        if new<=D: break
        D|=new
    inter=all((a&b) in D for a in D for b in D)
    return pts,D,inter,len(gens)
if __name__=="__main__":
  for name,n,W in [("2 indep",2,[(0,),(1,)]),("chain",3,[(0,1),(1,2)]),("triangle",3,[(0,1),(1,2),(2,0)]),("4-ring",4,[(0,1),(1,2),(2,3),(3,0)])]:
    pts,D,inter,g=run(n,W); print(name,"|union|=",g,"|D|=",len(D),"of",2**len(pts),"intersection-closed:",inter)
