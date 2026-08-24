#!/usr/bin/env python3
"""Independent graph/incidence audit of the two s36 k=4 candidates.

This file deliberately does not import relay7_core or the downstream checker.
It reconstructs two-valued states, the compatibility graph, rooted exactly-one
target paths, finite quotient incidence, and principal-master order separation.
"""
from collections import deque
import json
from pathlib import Path

BLOCKS = tuple(frozenset((2*i, 2*i+1, (2*i+2) % 14)) for i in range(7))
FACE_CLUSTER = frozenset((0, 3, 11))
TARGET = 1
PORTS = (
    ((0, 11), (3, 5), (6, 9), (13, 3)),
    ((1, 7), (5, 9), (11, 11), (12, 3)),
)


def states():
    out = set()
    def rec(i, chosen):
        if i == len(BLOCKS):
            if all(len(chosen & b) == 1 for b in BLOCKS):
                out.add(frozenset(chosen))
            return
        for a in BLOCKS[i]:
            rec(i + 1, chosen | {a})
    rec(0, set())
    return tuple(sorted(out, key=lambda x: (len(x), tuple(x))))


STATES = states()
NS = len(STATES)


def edges(port):
    return tuple(tuple(j for j, v in enumerate(STATES)
                       if all((x in u) == (y in v) for x, y in port))
                 for u in STATES)


def can_zero_forever(E):
    good = {i for i, s in enumerate(STATES) if TARGET not in s}
    changed = True
    while changed:
        changed = False
        for i in tuple(good):
            if not any(j in good for j in E[i]):
                good.remove(i); changed = True
    return good


def exact_one_reach(E, maxpos):
    """Possible (state, ones-so-far) at positions on an infinite exact-1 path."""
    zinf = can_zero_forever(E)
    # Suffix viability before reading the current state.
    oneinf = set()
    changed = True
    while changed:
        changed = False
        for i, s in enumerate(STATES):
            nxt = zinf if TARGET in s else oneinf
            if i not in oneinf and any(j in nxt for j in E[i]):
                oneinf.add(i); changed = True
    def post_viable(i, n):
        return any(j in (oneinf if n == 0 else zinf) for j in E[i])
    levels = []
    cur = {(i, int(TARGET in s)) for i, s in enumerate(STATES)
           if post_viable(i, int(TARGET in s))}
    levels.append(cur)
    for _ in range(maxpos):
        nxt = set()
        for i, n in cur:
            for j in E[i]:
                m = n + int(TARGET in STATES[j])
                if m <= 1 and post_viable(j, m):
                    nxt.add((j, m))
        cur = nxt
        levels.append(cur)
    return levels, zinf, oneinf


class DSU:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self.p[x] = y


def quotient(port, ncells):
    d = DSU(14 * ncells)
    for c in range(ncells - 1):
        for x, y in port: d.union(14*c+x, 14*(c+1)+y)
    blocks = [frozenset(d.find(14*c+a) for a in b)
              for c in range(ncells) for b in BLOCKS]
    return d, blocks


def girth(blocks):
    incidence = {}
    for bi, b in enumerate(blocks):
        if len(b) != 3: return 0
        for a in b: incidence.setdefault(a, []).append(bi)
    best = 10**9
    for src in incidence:
        start = ('a', src); dist = {start: 0}; parent = {start: None}
        q = deque([start])
        while q:
            v = q.popleft()
            ns = ([('b', i) for i in incidence[v[1]]] if v[0] == 'a'
                  else [('a', a) for a in blocks[v[1]]])
            for w in ns:
                if w == parent[v]: continue
                if w in dist:
                    best = min(best, (dist[v] + dist[w] + 1)//2)
                else:
                    dist[w] = dist[v] + 1; parent[w] = v; q.append(w)
    return None if best == 10**9 else best


def master_distance(d, blocks, c, gap):
    byatom = {}
    for bi, b in enumerate(blocks):
        for a in b: byatom.setdefault(a, set()).add(bi)
    src = byatom[d.find(14*c+TARGET)]; dst = byatom[d.find(14*(c+gap)+TARGET)]
    q = deque(src); dist = {x: 1 for x in src}
    while q:
        b = q.popleft()
        if b in dst: return dist[b]
        for a in blocks[b]:
            for nb in byatom[a]:
                if nb not in dist: dist[nb] = dist[b]+1; q.append(nb)
    return None


def compatible_pairs(E, levels, i, j):
    """State pairs at positions i,j extendable to rooted exact-one paths."""
    pairs = set()
    for s, n in levels[i]:
        cur = {(s, n)}
        for _ in range(i, j):
            nxt = set()
            for u, k in cur:
                for v in E[u]:
                    m = k + int(TARGET in STATES[v])
                    if m <= 1 and (v, m) in levels[_+1]: nxt.add((v, m))
            cur = nxt
        pairs |= {(s, t) for t, _ in cur}
    return pairs


def val(sym, state):
    kind, atom = sym
    return int(atom in state) if kind == 'a' else int(atom not in state)


def order_audit(port, maxgap=12):
    E = edges(port); levels, zinf, oneinf = exact_one_reach(E, maxgap)
    rows = []
    for gap in range(maxgap + 1):
        pairs = compatible_pairs(E, levels, 0, gap)
        # Atom classes and orthogonality in the (gap+1)-cell quotient determine
        # the height-3 Greechie order among atoms and their complements.
        d, blocks = quotient(port, gap + 1)
        orth = set()
        for b in blocks:
            for x in b:
                for y in b:
                    if x != y: orth.add((x, y))
        false = []
        for kx in ('a', 'c'):
            for ax in range(14):
                xclass = d.find(ax)
                for ky in ('a', 'c'):
                    for ay in range(14):
                        yclass = d.find(14*gap + ay)
                        ordered = ((kx == 'a' and ky == 'a' and xclass == yclass) or
                                   (kx == 'c' and ky == 'c' and xclass == yclass) or
                                   (kx == 'a' and ky == 'c' and
                                    (xclass, yclass) in orth))
                        if ordered: continue
                        if not any(val((kx, ax), STATES[s]) == 1 and
                                   val((ky, ay), STATES[t]) == 0 for s, t in pairs):
                            false.append([kx, ax, ky, ay])
        rows.append({'gap': gap, 'path_state_pairs': len(pairs),
                     'false_nonorders': len(false), 'first_false': false[:10]})
    return rows, len(zinf), len(oneinf), E


def main():
    out = {'state_count': NS, 'face_state_count': sum(FACE_CLUSTER <= s for s in STATES),
           'candidates': []}
    for port in PORTS:
        order, nz, no, E = order_audit(port)
        windows = {}
        for n in (2, 3, 4, 6, 12, 24, 48):
            _, b = quotient(port, n); windows[str(n)] = girth(b)
        d, b = quotient(port, 80)
        md = {str(g): master_distance(d, b, 20, g) for g in range(1, 31)}
        level0 = exact_one_reach(E, 0)[0]
        local_live = {s for s, _ in level0[0]}
        out['candidates'].append({
            'port': port, 'zero_suffix_states': nz, 'one_suffix_states': no,
            'root_live_states': len(local_live),
            'face_free_zero_suffix': all(i in can_zero_forever(E)
                                         for i, s in enumerate(STATES)
                                         if FACE_CLUSTER <= s),
            'face_nonlive_root': not any(FACE_CLUSTER <= STATES[s] for s in local_live),
            'window_berge_girth': windows, 'master_block_distances': md,
            'order_separation_from_root': order,
            'passes_tested_cross_cell_order': all(r['false_nonorders'] == 0 for r in order),
        })
    path = Path(__file__).with_name('audit_s36_candidate_results.json')
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__': main()
