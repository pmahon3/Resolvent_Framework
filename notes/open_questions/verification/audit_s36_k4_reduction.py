#!/usr/bin/env python3
"""Independent exact reductions for the seven-loop period-one k=4 class.

This does not import relay7_core.  It reconstructs the cell, its 0/1 states,
atom distances, period-one transition relation, and exact two-cell quotient.
The pair criterion d(x,x')+d(y,y') >= 5 is only a necessary prefilter:
four-identification alternating cycles need not be witnessed by one pair.
"""
from itertools import combinations, permutations, product
from collections import deque, Counter

N = 7
ATOMS = tuple(range(2*N))
BLOCKS = tuple(frozenset((2*i, 2*i+1, (2*i+2) % (2*N))) for i in range(N))
CLUSTER = frozenset((0, 3, 11))


def states():
    ans = set()
    for choice in product(*[tuple(b) for b in BLOCKS]):
        s = frozenset(choice)
        if all(len(s & b) == 1 for b in BLOCKS):
            ans.add(s)
    return tuple(sorted(ans, key=lambda x: (len(x), tuple(x))))


STATES = states()
FACE = tuple(i for i, s in enumerate(STATES) if CLUSTER <= s)


def atom_distances():
    adj = {a: set() for a in ATOMS}
    for b in BLOCKS:
        for a in b:
            adj[a].update(b - {a})
    d = [[99]*len(ATOMS) for _ in ATOMS]
    for root in ATOMS:
        d[root][root] = 0
        q = deque([root])
        while q:
            a = q.popleft()
            for z in adj[a]:
                if d[root][z] == 99:
                    d[root][z] = d[root][a] + 1
                    q.append(z)
    return d


DIST = atom_distances()


def subset_types():
    return {old: tuple(sorted(DIST[a][b] for a, b in combinations(old, 2)))
            for old in combinations(ATOMS, 4)}


def pair_prefilter(old, image):
    return all(DIST[old[i]][old[j]] + DIST[image[i]][image[j]] >= 5
               for i in range(4) for j in range(i+1, 4))


def exact_girth_ok(old, image):
    """Exact linearity and incidence-girth >=10 in the two-cell quotient."""
    parent = list(range(28))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(x, y):
        x, y = find(x), find(y)
        if x != y: parent[x] = y
    for x, y in zip(old, image): union(x, 14+y)
    blocks = [frozenset(find(14*c+a) for a in b)
              for c in range(2) for b in BLOCKS]
    if any(len(b) != 3 for b in blocks): return False
    inc = {}
    for bi, b in enumerate(blocks):
        for a in b: inc.setdefault(a, []).append(bi)
    # Direct BFS cycle detection in the bipartite incidence graph.
    graph = {}
    for bi, b in enumerate(blocks):
        bv = ('b', bi); graph.setdefault(bv, set())
        for a in b:
            av = ('a', a); graph.setdefault(av, set())
            graph[bv].add(av); graph[av].add(bv)
    for root in graph:
        dist = {root: 0}; par = {root: None}; q = deque([root])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if w == par[v]: continue
                if w in dist:
                    if dist[v] + dist[w] + 1 < 10: return False
                else:
                    dist[w] = dist[v]+1; par[w] = v; q.append(w)
    return True


def transition(port, i, j):
    """Whether state i in old cell coheres with state j in new cell."""
    x, y = port
    return all((a in STATES[i]) == (b in STATES[j]) for a, b in zip(x, y))


def face_free(port, target):
    """Exact period-one all-zero continuation test for every FACE state.

    Cell zero is unconstrained, hence every target-zero state is root
    reachable.  It is free precisely when it can reach a directed cycle in
    the target-zero transition graph.
    """
    x, y = port
    def sig(s, atoms):
        return sum((a in s) << k for k, a in enumerate(atoms))
    zero = [s for s in STATES if target not in s]
    # Signature graph: p -> q iff a target-zero successor has new signature
    # p and old signature q.  This is equivalent to the state graph but has
    # at most 16 vertices.
    adj = {p: set() for p in range(16)}
    for s in zero:
        adj[sig(s, y)].add(sig(s, x))
    live = set(range(16))
    changed = True
    while changed:
        changed = False
        for p in tuple(live):
            if not (adj[p] & live):
                live.remove(p); changed = True
    return all(sig(STATES[i], x) in live for i in FACE)


def transforms():
    """The 14 dihedral automorphisms of the labeled seven-loop cell."""
    out = []
    # Acting on the cyclic block/connector incidence labeling.
    for shift in range(7):
        out.append(tuple((a + 2*shift) % 14 for a in ATOMS))
        out.append(tuple((2*shift - a) % 14 for a in ATOMS))
    assert len(set(out)) == 14
    assert all({frozenset(g[a] for a in b) for b in BLOCKS} == set(BLOCKS)
               for g in out)
    return tuple(dict.fromkeys(out))


AUT = transforms()
STAB = tuple(g for g in AUT if {g[a] for a in CLUSTER} == set(CLUSTER))


def canon(port, group):
    x, y = port
    images = []
    for g in group:
        pairs = sorted((g[a], g[b]) for a, b in zip(x, y))
        images.append(tuple(pairs))
    return min(images)


def main():
    raw = 0; pair_valid = 0; valid = 0; free = Counter(); valid_orbits = set(); stab_orbits = set()
    types = Counter()
    targets = (1, 2, 4, 10, 12, 13)
    for old in combinations(ATOMS, 4):
        for newset in combinations(ATOMS, 4):
            for image in permutations(newset):
                raw += 1
                if not pair_prefilter(old, image):
                    continue
                pair_valid += 1
                if not exact_girth_ok(old, image): continue
                valid += 1
                port = (old, image)
                types[(tuple(sorted(DIST[old[i]][old[j]] for i in range(4)
                                    for j in range(i+1, 4))),
                       tuple(sorted(DIST[image[i]][image[j]] for i in range(4)
                                    for j in range(i+1, 4))))] += 1
                valid_orbits.add(canon(port, AUT))
                stab_orbits.add(canon(port, STAB))
                for t in targets:
                    if face_free(port, t):
                        free[t] += 1
    print('states', len(STATES), 'face', FACE)
    print('automorphisms', len(AUT), 'cluster_stabilizer', len(STAB))
    print('raw', raw, 'pair_prefilter', pair_valid, 'exact_girth_valid', valid,
          'four_crossing_rejects', pair_valid-valid)
    print('valid_full_dihedral_orbits', len(valid_orbits))
    print('valid_cluster_stabilizer_orbits', len(stab_orbits))
    print('face_free', dict(free))
    print('valid_pair_distance_types', len(types))


if __name__ == '__main__':
    main()
