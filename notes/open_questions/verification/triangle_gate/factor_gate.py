# Pre-registered pairwise factoring gate (TRIANGLE_GATE_ATTEMPT.md, end of sec 5), run 2026-11-10 on 3x3x3.
# A set factors at coordinate i through the partition merging values a,b iff it is invariant under swapping a<->b in x_i.
import sys; sys.argv=['x','3','3','3']
exec(open('kform.py').read().split("print('|D|'")[0])
import itertools
coR1={m^FULL for m in R1}
new=coR1-R1                      # complements of R1 sets that are not themselves R1 sets
print('|R1|',len(R1),'|co-R1|',len(coR1),'|co-R1 minus R1|',len(new),'|D|',len(D))
def swap(m,i,a,b):
    out=0
    for p in pts:
        if m>>idx[p]&1:
            q=list(p); q[i]= b if p[i]==a else a if p[i]==b else p[i]; out|=1<<idx[tuple(q)]
    return out
merges=[(i,a,b) for i in range(3) for a,b in itertools.combinations(range(n[i]),2)]
inv={m:frozenset(k for k,(i,a,b) in enumerate(merges) if swap(m,i,a,b)==m) for m in coR1}
print('new sets factoring through a 2-class partition at some coordinate:',sum(1 for m in new if inv[m]))
L=sorted(new); dis=[(x,y) for x,y in itertools.combinations(L,2) if x&y==0]
print('disjoint pairs among new sets:',len(dis),' max size of a pairwise-disjoint family:',end=' ')
best=1
for x,y in dis:
    for z in L:
        if z>y and z&x==0 and z&y==0: best=max(best,3)
    best=max(best,2)
print(best)
# all disjoint pairs of nonempty co-R1 sets with at least one new member
C=sorted(coR1-{0}); tot=fac=0
for x in L:
    for y in C:
        if x&y==0 and x!=y:
            tot+=1; fac+= bool(inv[x]&inv[y])
print('disjoint pairs (new, nonempty co-R1):',tot,' factoring with m<=2:',fac)
# Which triples of new sets partition the grid? Are the level sets of x0+x1+x2 mod 3 among the new sets?
Es=mask(lambda p:((p[0]<=p[1])+(p[1]<p[2])+(p[2]<p[0]))==2)
tri=[(x,y,FULL^x^y) for x,y in dis if (FULL^x^y) in new and (FULL^x^y)>y]
print('partitions of the grid into three new sets:',len(tri))
lat=[mask(lambda p,k=k:(p[0]+p[1]+p[2])%3==k) for k in range(3)]
print('sum mod 3 level sets in new:',[m in new for m in lat],' in D:',[m in D for m in lat])
ex=[t for t in tri if Es in t][:1]
for t in ex:
    for m in t: print(sorted(p for p in pts if m>>idx[p]&1))
print('partitions containing E3:',sum(1 for t in tri if Es in t))
