# Independent re-encoding (integer 0/1 vars, separate code) + unsat core extraction.
import itertools
from z3 import *
N=6   # tower values 1..N, beta = 0 (minimum)
def key(x):  # type: which coords are beta, and rank pattern of the others
    others=sorted(set(v for v in x if v!=0))
    return tuple(0 if v==0 else 1+others.index(v) for v in x)
P=list(itertools.product(range(N+1),repeat=4)); K=sorted(set(key(x) for x in P))
v={k:Int('v'+''.join(map(str,k))) for k in K}
s=Solver(); s.set(unsat_core=True)
for k in K: s.add(Or(v[k]==0,v[k]==1))
val=lambda x: v[key(x)]
def u(x,i,c): y=list(x); y[i]=c; return tuple(y)
cls={}
for x in P:
    for c in range(N+1):
        for d in range(N+1):
            for (i,j) in ((0,2),(1,3)):
                a,b,cc,dd=key(x),key(u(u(x,i,c),j,d)),key(u(x,i,c)),key(u(x,j,d))
                cls.setdefault((a,b,cc,dd),None)
tags=[]
for n,(a,b,cc,dd) in enumerate(cls):
    t=Bool('r%d'%n); tags.append((t,(a,b,cc,dd))); s.assert_and_track(v[a]+v[b]==v[cc]+v[dd],t)
z=(0,0,0,0)
def p(d): return tuple(d.get(k,0) for k in range(4))
Phi=val(z)+Sum([val(p({k:1}))-val(z) for k in range(4)])+Sum([val(p({a:1,b:2}))-val(p({a:1}))-val(p({b:2}))+val(z) for a,b in ((0,1),(1,2),(2,3),(3,0))])
s.add(Or(Phi>=2,Phi<=-1))
print("types",len(K),"classes",len(cls),"->",s.check())
core=s.unsat_core(); print("core size",len(core))
# minimize core
s2=Solver(); [s2.add(Or(v[k]==0,v[k]==1)) for k in K]; s2.add(Or(Phi>=2,Phi<=-1))
m={str(t):c for t,c in tags}; keep=[str(c) for c in core]
i=0
while i<len(keep):
    trial=keep[:i]+keep[i+1:]
    s3=Solver(); s3.add(s2.assertions())
    for nm in trial: a,b,cc,dd=m[nm]; s3.add(v[a]+v[b]==v[cc]+v[dd])
    if s3.check()==unsat: keep=trial
    else: i+=1
print("minimal core size",len(keep))
for nm in keep: print("  ",m[nm][0],"+",m[nm][1],"=",m[nm][2],"+",m[nm][3])
