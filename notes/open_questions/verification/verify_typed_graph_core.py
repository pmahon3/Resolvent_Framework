#!/usr/bin/env python3
"""Independent declarative verifier for typed_graph_core_certificate.json."""
import hashlib,json,sys
N=("g","h","W","Vi","Vj","R")
def verify(run):
 n=run["n_columns"]; typ=[int(x) for x in run["type_word"]]; F=(1<<(6*n))-1
 atom=lambda c,s:sum(1<<(6*c+N.index(z)) for z in s)
 ss=[0,0,0]; gg={(1,2):0,(1,3):0,(2,3):0}
 for c,k in enumerate(typ):
  a,b=sorted({1,2,3}-{k}); tr={k:("g","h"),a:("g","W","Vi"),b:("h","W","Vj")}
  for m in (1,2,3): ss[m-1]|=atom(c,tr[m])
  for p in gg:
   if k in p: gg[p]|=atom(c,("g",) if next(x for x in p if x!=k)==a else ("h",))
 cl={0,F,*ss,*gg.values()}
 for A in range(1<<n): cl.add(sum(63<<(6*c) for c in range(n) if A>>c&1))
 while True:
  nxt=cl|{F^x for x in cl}; q=list(nxt)
  nxt|={x|y for i,x in enumerate(q) for y in q[i+1:] if not x&y}
  if nxt==cl: break
  cl=nxt
 vals=sorted(cl); assert len(vals)==run["closure_size"]
 assert hashlib.sha256(','.join(map(str,vals)).encode()).hexdigest()==run["closure_sha256"]
 h=[]
 for m in (1,2,3): h.append(ss[m-1]&~sum((g for p,g in gg.items() if m in p),0)&F)
 w=sum(1<<(6*c+2) for c in range(n)); T=run["targets"]
 assert T["residuals_present"]==all(x in cl for x in h)
 assert T["sigma_intersections_present"]==[(ss[i]&ss[j]) in cl for i,j in ((0,1),(0,2),(1,2))]
 assert T["residual_intersections_present"]==[(h[i]&h[j]) in cl for i,j in ((0,1),(0,2),(1,2))]
 assert T["nonzero_below_W"]==sum(1 for x in cl if x and not x&~w)
 count=0
 for p,g in gg.items():
  cs=[c for c,t in enumerate(typ) if t in p]
  for A in range(1<<len(cs)):
   r=g&sum(63<<(6*cs[j]) for j in range(len(cs)) if A>>j&1)
   if r not in (0,g) and r in cl: count+=1
 assert count==T["proper_collector_restrictions_present"]
 singles=[x for x in cl if all((x>>(6*c)&63) in (0,1,2) for c in range(n))]
 assert len(singles)==T["singleton_profile_count"]
 assert T["singleton_profiles_are_zero_and_collectors"]==(set(singles)==({0}|set(gg.values())))
 print("verified",n,len(cl))
def main():
 from pathlib import Path
 path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("typed_graph_core_certificate.json")
 cert=json.load(open(path))
 for r in cert["runs"]: verify(r)
 print("ALL CHECKS PASS")
if __name__=="__main__": main()
