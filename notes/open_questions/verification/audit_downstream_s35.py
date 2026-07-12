#!/usr/bin/env python3
"""Standalone downstream audit of the period-1 k=3 seven-loop survivors.

This deliberately imports neither the census nor its downstream verifier.
It checks incidence-graph girth on finite chain windows, target-to-target
block distance in a larger interior window, and the reflection symmetry that
fixes C={0,3,11}.  A complete single master block adds one incidence block,
so girth >= 5 requires every target gap distance to be at least four.
"""
from collections import deque

N = 14
BLOCKS = tuple(frozenset((2*i, 2*i+1, (2*i+2) % N)) for i in range(7))
SURVIVORS = {
    2: (((0,3),(1,11),(11,13)), ((0,11),(3,1),(13,3)),
        ((0,3),(4,13),(11,11)), ((1,4),(3,11),(10,13)),
        ((1,13),(10,3),(11,11)), ((1,13),(11,11),(12,3)),
        ((3,11),(4,3),(13,13)), ((3,0),(11,11),(13,4)),
        ((4,1),(11,3),(13,10))),
    12: (((0,3),(1,11),(11,13)), ((0,11),(3,3),(10,1)),
         ((0,11),(3,1),(13,3)), ((1,4),(3,11),(10,13)),
         ((1,10),(3,3),(11,0)), ((1,1),(10,11),(11,3)),
         ((2,11),(3,3),(13,1)), ((3,3),(4,11),(13,1)),
         ((4,1),(11,3),(13,10))),
}
EARLY = {
    1: (((2,13),(10,3),(11,11)), ((2,13),(11,11),(12,3))),
    13: (((2,11),(3,3),(12,1)), ((3,3),(4,11),(12,1))),
}


class DSU:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self.p[x] = y


def quotient(mp, cells):
    d = DSU(N*cells)
    for c in range(cells-1):
        for left, right in mp:
            d.union(N*c + left, N*(c+1) + right)
    bs = tuple(frozenset(d.find(N*c+a) for a in B)
               for c in range(cells) for B in BLOCKS)
    return d, bs


def incidence_girth(mp, cells):
    """Exact girth of the finite quotient's bipartite incidence graph."""
    _, bs = quotient(mp, cells)
    if any(len(B) != 3 for B in bs): return 2
    atoms = {}
    for bi, B in enumerate(bs):
        for a in B: atoms.setdefault(a, []).append(bi)
    graph = {}
    for a, ids in atoms.items():
        graph[('a', a)] = [('b', i) for i in ids]
    for i, B in enumerate(bs): graph[('b', i)] = [('a', a) for a in B]
    best = 10**9
    for root in graph:
        dist, parent = {root: 0}, {root: None}
        q = deque((root,))
        while q:
            v = q.popleft()
            for w in graph[v]:
                if w not in dist:
                    dist[w], parent[w] = dist[v]+1, v
                    q.append(w)
                elif parent[v] != w:
                    best = min(best, dist[v] + dist[w] + 1)
    return None if best == 10**9 else best // 2  # number of Greechie blocks


def target_gap_distances(mp, target, maxgap=15, margin=12):
    """Shortest number of blocks joining target in cells c and c+gap."""
    cells = 2*margin + maxgap + 1
    d, bs = quotient(mp, cells)
    by_atom = {}
    for bi, B in enumerate(bs):
        for a in B: by_atom.setdefault(a, []).append(bi)
    adjacency = [set() for _ in bs]
    for ids in by_atom.values():
        for i in ids: adjacency[i].update(j for j in ids if j != i)
    ans = {}
    for gap in range(1, maxgap+1):
        src = by_atom[d.find(N*margin + target)]
        goal = set(by_atom[d.find(N*(margin+gap) + target)])
        distance, q = {i: 1 for i in src}, deque(src)
        answer = None
        while q:
            v = q.popleft()
            if v in goal:
                answer = distance[v]; break
            for w in adjacency[v]:
                if w not in distance:
                    distance[w] = distance[v]+1; q.append(w)
        ans[gap] = answer
    return ans


def reflection(pair):
    target, mp = pair
    f = lambda x: (-x) % N
    return f(target), tuple(sorted((f(a), f(b)) for a, b in mp))


def main():
    print('EARLY GIRTH FAILURES')
    for target, maps in EARLY.items():
        for mp in maps:
            gs = tuple(incidence_girth(mp, n) for n in (2,3,4,6))
            print(target, mp, 'window-girth=', gs)
    print('\nTARGET 2/12 DOWNSTREAM')
    pairs = {(t, mp) for t, maps in SURVIVORS.items() for mp in maps}
    assert len(pairs) == 18
    for target, mp in sorted(pairs):
        gs = tuple(incidence_girth(mp, n) for n in range(2, 13))
        gaps = target_gap_distances(mp, target)
        print(target, mp, 'girth[2..12]=', gs,
              'gap1=', gaps[1], 'min=', min(gaps.values()), 'gaps=', gaps)
        assert all(g is None or g >= 5 for g in gs)
        assert gaps[1] in (2, 3) and gaps[1] < 4
        assert reflection((target, mp)) in pairs
    reps = sorted(min(p, reflection(p)) for p in pairs)
    reps = sorted(set(reps))
    print('\nREFLECTION ORBITS', len(reps))
    for i, p in enumerate(reps, 1): print(i, p, '<->', reflection(p))
    print('\nVERDICT: 18/18 killed by gap-1 master cycle; 0 reach separation.')


if __name__ == '__main__': main()
