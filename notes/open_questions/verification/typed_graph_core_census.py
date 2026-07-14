#!/usr/bin/env python3
"""Producer for finite typed global-core quotients of Gate N."""
import hashlib, json, sys

CELLS = ("g", "h", "W", "Vi", "Vj", "R")

def data(n):
    types = tuple(1 + i % 3 for i in range(n)); full = (1 << (6*n))-1
    def sec(c, names): return sum(1 << (6*c+CELLS.index(x)) for x in names)
    sig = [0, 0, 0]; gs = {(1,2):0, (1,3):0, (2,3):0}
    for c,k in enumerate(types):
        others = sorted({1,2,3}-{k}); i,j=others
        traces={k:("g","h"), i:("g","W","Vi"), j:("h","W","Vj")}
        for m in (1,2,3): sig[m-1] |= sec(c,traces[m])
        for pair in gs:
            if k in pair:
                other = next(x for x in pair if x != k)
                gs[pair] |= sec(c,("g",) if other == i else ("h",))
    cyl=[]
    for a in range(1<<n):
        cyl.append(sum(((1<<6)-1) << (6*c) for c in range(n) if a>>c&1))
    gens=set(cyl+sig+list(gs.values())+[0,full])
    cl=set(gens); changed=True
    while changed:
        old=len(cl); items=list(cl); cl.update(full^x for x in items); items=list(cl)
        for p,x in enumerate(items):
            for y in items[p+1:]:
                if not x&y: cl.add(x|y)
        changed=len(cl)>old
    return types, full, sig, gs, sorted(cl)

def targets(types, full, sig, gs, cl):
    S=set(cl); n=len(types); w=sum(1<<(6*c+2) for c in range(n))
    hs=[]
    for m in (1,2,3):
        inc=0
        for pair,g in gs.items():
            if m in pair: inc |= g
        hs.append(sig[m-1] & ~inc & full)
    restrictions=[]
    for pair,g in gs.items():
        support=[c for c,t in enumerate(types) if t in pair]
        for a in range(1<<len(support)):
            mask=sum(((1<<6)-1)<<(6*support[j]) for j in range(len(support)) if a>>j&1)
            r=g&mask
            if r not in (0,g): restrictions.append(r in S)
    singleton_profiles=[x for x in S if all((x>>(6*c)&63) in (0,1,2) for c in range(n))]
    return {"residuals_present":all(h in S for h in hs),
      "sigma_intersections_present":[(sig[i]&sig[j]) in S for i,j in ((0,1),(0,2),(1,2))],
      "residual_intersections_present":[(hs[i]&hs[j]) in S for i,j in ((0,1),(0,2),(1,2))],
      "nonzero_below_W":sum(1 for x in S if x and not x&~w),
      "proper_collector_restrictions_present":sum(restrictions),
      "singleton_profile_count":len(singleton_profiles),
      "singleton_profiles_are_zero_and_collectors":set(singleton_profiles)==({0}|set(gs.values()))}

def main():
    ns=[int(x) for x in sys.argv[1:]] or [3,6,9]
    runs=[]
    for n in ns:
        types,full,sig,gs,cl=data(n); raw=','.join(map(str,cl)).encode()
        runs.append({"n_columns":n,"type_word":"".join(map(str,types)),
          "closure_size":len(cl),"closure_sha256":hashlib.sha256(raw).hexdigest(),
          "targets":targets(types,full,sig,gs,cl)})
        print(n,len(cl),runs[-1]["targets"])
    out={"scope":"exhaustive finite global core; local column generators omitted", "runs":runs}
    path="typed_graph_core_certificate.json"
    with open(path,"w") as f: json.dump(out,f,indent=2,sort_keys=True)
    print(path)
if __name__=="__main__": main()
