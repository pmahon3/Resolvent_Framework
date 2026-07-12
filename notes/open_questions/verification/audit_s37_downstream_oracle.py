#!/usr/bin/env python3
"""Independent period-p downstream oracle for the seven-loop relay.

No production relay module is imported.  The oracle reconstructs states,
phase-labelled compatibility graphs, rooted exactly-one paths, fixed-position
state restrictions, quotient incidence, master gaps, and local/cross-cell
symbol-order separation.
"""
from collections import deque
from itertools import product

N = 14
BLOCKS = tuple(frozenset((2*i, 2*i+1, (2*i+2) % N)) for i in range(7))
FACE_CLUSTER = frozenset((0, 3, 11))
SYMS = tuple((k, a) for k in ('a', 'c') for a in range(N))


def enumerate_states():
    out = set()
    for choice in product(*[tuple(b) for b in BLOCKS]):
        s = frozenset(choice)
        if all(len(s & b) == 1 for b in BLOCKS): out.add(s)
    return tuple(sorted(out, key=lambda s: (len(s), tuple(s))))


STATES = enumerate_states()
NS = len(STATES)
FACE_IDS = frozenset(i for i, s in enumerate(STATES) if FACE_CLUSTER <= s)


def edges(port):
    return tuple(tuple(j for j, v in enumerate(STATES)
                       if all((a in u) == (b in v) for a, b in port))
                 for u in STATES)


def phase_edges(maps): return tuple(edges(tuple(map(tuple, p))) for p in maps)


def suffix_sets(E, target):
    """Explicit pruning/flooding for zero and exactly-one infinite suffixes."""
    p = len(E); zeros = [{s for s, u in enumerate(STATES) if target not in u}
                         for _ in range(p)]
    changed = True
    while changed:
        changed = False
        for r in range(p):
            drop = {s for s in zeros[r]
                    if not any(t in zeros[(r+1) % p] for t in E[r][s])}
            if drop: zeros[r] -= drop; changed = True
    ones = [set() for _ in range(p)]
    changed = True
    while changed:
        changed = False
        for r in range(p):
            for s, u in enumerate(STATES):
                wanted = zeros[(r+1) % p] if target in u else ones[(r+1) % p]
                if s not in ones[r] and any(t in wanted for t in E[r][s]):
                    ones[r].add(s); changed = True
    return zeros, ones


def rooted_levels(maps, target, maxpos):
    """Viable (state, ones-so-far) restrictions at each fixed position."""
    E = phase_edges(maps); zeros, ones = suffix_sets(E, target); p = len(E)
    def extendable(pos, s, n):
        wanted = ones[(pos+1) % p] if n == 0 else zeros[(pos+1) % p]
        return any(t in wanted for t in E[pos % p][s])
    cur = {(s, int(target in u)) for s, u in enumerate(STATES)
           if extendable(0, s, int(target in u))}
    levels = [cur]
    for pos in range(maxpos):
        nxt = set()
        for s, n in cur:
            for t in E[pos % p][s]:
                m = n + int(target in STATES[t])
                if m <= 1 and extendable(pos+1, t, m): nxt.add((t, m))
        levels.append(nxt); cur = nxt
    return E, zeros, ones, levels


def fixed_pairs(E, levels, target, i, j):
    pairs = set()
    for si, n in levels[i]:
        cur = {(si, n)}
        for pos in range(i, j):
            nxt = set()
            for s, k in cur:
                for t in E[pos % len(E)][s]:
                    m = k + int(target in STATES[t])
                    if m <= 1 and (t, m) in levels[pos+1]: nxt.add((t, m))
            cur = nxt
        pairs.update((si, sj) for sj, _ in cur)
    return pairs


class DSU:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self.p[x] = y


def quotient(maps, ncells):
    d = DSU(N*ncells)
    for c in range(ncells-1):
        for a, b in maps[c % len(maps)]: d.union(N*c+a, N*(c+1)+b)
    blocks = tuple(frozenset(d.find(N*c+a) for a in B)
                   for c in range(ncells) for B in BLOCKS)
    return d, blocks


def berge_girth(blocks):
    if any(len(b) != 3 for b in blocks): return 0
    byatom = {}
    for bi, b in enumerate(blocks):
        for a in b: byatom.setdefault(a, []).append(bi)
    best = 10**9
    for src in byatom:
        root = ('a', src); dist = {root: 0}; parent = {root: None}; q = deque([root])
        while q:
            v = q.popleft()
            ns = ([('b', x) for x in byatom[v[1]]] if v[0] == 'a'
                  else [('a', x) for x in blocks[v[1]]])
            for w in ns:
                if w == parent[v]: continue
                if w in dist: best = min(best, (dist[v]+dist[w]+1)//2)
                else: dist[w] = dist[v]+1; parent[w] = v; q.append(w)
    return None if best == 10**9 else best


def master_gap(maps, target, gap, base=20):
    d, blocks = quotient(maps, 2*base+gap+1)
    byatom = {}
    for bi, b in enumerate(blocks):
        for a in b: byatom.setdefault(a, set()).add(bi)
    src = byatom[d.find(N*base+target)]; goal = byatom[d.find(N*(base+gap)+target)]
    q = deque(src); dist = {b: 1 for b in src}
    while q:
        b = q.popleft()
        if b in goal: return dist[b]
        for a in blocks[b]:
            for c in byatom[a]:
                if c not in dist: dist[c] = dist[b]+1; q.append(c)


def value(sym, state):
    k, a = sym; return (a in state) if k == 'a' else (a not in state)


def false_orders(maps, pairs, i, j):
    d, blocks = quotient(maps, j+1)
    orth = {(x, y) for b in blocks for x in b for y in b if x != y}
    false = []
    for x in SYMS:
        xc = d.find(N*i+x[1])
        for y in SYMS:
            yc = d.find(N*j+y[1])
            actual = ((x[0] == y[0] and xc == yc) or
                      (x[0] == 'a' and y[0] == 'c' and (xc, yc) in orth))
            if not actual and not any(value(x, STATES[s]) and
                                      not value(y, STATES[t]) for s, t in pairs):
                false.append((x, y))
    return false


def audit(maps, target, maxpos=12):
    maps = tuple(tuple(map(tuple, p)) for p in maps)
    # Continue far beyond the requested fixed-position window so phasewise
    # any-position unions stabilize.  There are only 2*NS reachability
    # product vertices per phase; this bound allows two full addition passes.
    phase_bound = 4 * NS * len(maps)
    E, zeros, ones, levels = rooted_levels(maps, target, max(maxpos, phase_bound))
    phase_live = [set() for _ in maps]
    phase_free = [set() for _ in maps]
    # Rooted all-zero reachability, independently of exact-one paths.
    zero_level = {s for s, u in enumerate(STATES) if target not in u}
    for pos, level in enumerate(levels):
        phase_live[pos % len(maps)].update(s for s, _ in level)
        phase_free[pos % len(maps)].update(zero_level & zeros[pos % len(maps)])
        zero_level = {t for s in zero_level for t in E[pos % len(maps)][s]
                      if target not in STATES[t]}
    cross = []
    for j in range(maxpos+1):
        for i in range(j+1):
            pairs = fixed_pairs(E, levels, target, i, j)
            bad = false_orders(maps, pairs, i, j)
            cross.append({'i': i, 'j': j, 'pairs': len(pairs),
                          'false_count': len(bad), 'first_false': bad[:25]})
    return {
        'target': target, 'maps': maps,
        'fixed_restriction_sizes': [len(x) for x in levels[:maxpos+1]],
        'root_restriction_states': sorted(s for s, _ in levels[0]),
        'root_local_false_orders': len(false_orders(
            maps, {(s, s) for s, _ in levels[0]}, 0, 0)),
        'phase_live_sizes_tested': [len(x) for x in phase_live],
        'phase_face_nonlive_tested': [not bool(x & FACE_IDS) for x in phase_live],
        'phase_face_free_tested': [FACE_IDS <= x for x in phase_free],
        'phase_local_false_orders_tested': [
            len(false_orders(maps, {(s, s) for s in live}, 0, 0))
            for live in phase_live],
        'window_girth': {n: berge_girth(quotient(maps, n)[1])
                         for n in (2, 3, 4, 6, 12, 24, 48)},
        'master_gaps': {g: master_gap(maps, target, g) for g in range(1, 16)},
        'cross_cell': cross,
        'passes_tested_cross_cell': not any(r['false_count'] for r in cross),
    }
