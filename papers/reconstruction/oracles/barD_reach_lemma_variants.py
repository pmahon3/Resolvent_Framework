import sys
exec(open(__file__.replace('barD_reach_lemma_variants.py','barD_reach_lemma_variants_base.py')).read().split("import itertools")[0])
for A in (3,4):
    allp=[(a,b) for a in range(A) for b in range(A)]
    st=dict(rec=0,nonrec=0,both_fail_rec=0,both_fail_nonrec=0,fixed_fail_rec=0,ex=[])
    for mask in range(1<<len(allp)):
        rel=frozenset(p for i,p in enumerate(allp) if mask>>i&1)
        if not primitive(rel,A): continue
        rec,out=recurrent_pairs(rel,A); rec=set(rec)
        cyc=[C for C in simple_cycles(rel,A) if len(C)>=2]
        for x in range(A):
            for y in range(A):
                if x==y: continue
                f1=any(land(x,y,C,out) for C in cyc if x in C)
                f2=any(land(y,x,C,out) for C in cyc if y in C)
                r=(x,y) in rec
                st['rec' if r else 'nonrec']+=1
                if not (f1 or f2):
                    st['both_fail_rec' if r else 'both_fail_nonrec']+=1
                    if len(st['ex'])<3: st['ex'].append((sorted(rel),(x,y),r))
                if r and not f1: st['fixed_fail_rec']+=1
    print('A',A,st)
