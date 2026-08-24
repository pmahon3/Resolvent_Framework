#!/usr/bin/env python3
"""Independent finite-window girth check for audit_s35 survivor maps."""
from collections import deque
from audit_s35_7loop_census import BLOCKS

SURVIVORS = {
1:[((2,13),(10,3),(11,11)),((2,13),(11,11),(12,3))],
2:[((0,3),(1,11),(11,13)),((0,11),(3,1),(13,3)),((0,3),(4,13),(11,11)),
   ((1,4),(3,11),(10,13)),((1,13),(10,3),(11,11)),((1,13),(11,11),(12,3)),
   ((3,11),(4,3),(13,13)),((3,0),(11,11),(13,4)),((4,1),(11,3),(13,10))],
12:[((0,3),(1,11),(11,13)),((0,11),(3,3),(10,1)),((0,11),(3,1),(13,3)),
    ((1,4),(3,11),(10,13)),((1,10),(3,3),(11,0)),((1,1),(10,11),(11,3)),
    ((2,11),(3,3),(13,1)),((3,3),(4,11),(13,1)),((4,1),(11,3),(13,10))],
13:[((2,11),(3,3),(12,1)),((3,3),(4,11),(12,1))]}

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x!=y:self.p[x]=y

def window_ok(mp,ncell):
    d=DSU(14*ncell)
    for c in range(ncell-1):
        for x,y in mp:d.union(14*c+x,14*(c+1)+y)
    blocks=[frozenset(d.find(14*c+x) for x in B) for c in range(ncell) for B in BLOCKS]
    if any(len(B)!=3 for B in blocks):return False
    at={}
    for i,B in enumerate(blocks):
        for x in B:at.setdefault(x,[]).append(i)
    for src in at:
        dist={('a',src):0}; par={('a',src):None}; q=deque([('a',src)])
        while q:
            v=q.popleft()
            if dist[v]>=5:continue
            ns=([('b',i) for i in at[v[1]]] if v[0]=='a'
                else [('a',x) for x in blocks[v[1]]])
            for w in ns:
                if w==par[v]:continue
                if w in dist:
                    if dist[v]+dist[w]+1<10:return False
                else:dist[w]=dist[v]+1;par[w]=v;q.append(w)
    return True

def master_gaps(mp,target,gaps=range(1,16),ncell=40,base=10):
    d=DSU(14*ncell)
    for c in range(ncell-1):
        for x,y in mp:d.union(14*c+x,14*(c+1)+y)
    blocks=[frozenset(d.find(14*c+x) for x in B) for c in range(ncell) for B in BLOCKS]
    adj=[[] for _ in blocks]
    byatom={}
    for i,B in enumerate(blocks):
        for x in B:byatom.setdefault(x,[]).append(i)
    for ids in byatom.values():
        for i in ids:
            for j in ids:
                if i!=j:adj[i].append(j)
    out={}
    for gap in gaps:
        src=d.find(14*base+target); dst=d.find(14*(base+gap)+target)
        starts=byatom[src]; goals=set(byatom[dst]); dist={i:1 for i in starts};q=deque(starts)
        while q:
            v=q.popleft()
            if v in goals:break
            for w in adj[v]:
                if w not in dist:dist[w]=dist[v]+1;q.append(w)
        out[gap]=dist[v] if v in goals else None
    return out

def reflected(target,mp):
    f=lambda x:(-x)%14
    return f(target),tuple(sorted((f(x),f(y)) for x,y in mp))

if __name__=='__main__':
    for target,maps in SURVIVORS.items():
        for mp in maps:
            vals=[window_ok(mp,n) for n in (2,3,4,6)]
            gaps=master_gaps(mp,target)
            print(f'a{target} {mp}: windows 2,3,4,6={vals} '
                  f'master_min={min(gaps.values())} gaps={gaps} '
                  f'reflected={reflected(target,mp)}')
