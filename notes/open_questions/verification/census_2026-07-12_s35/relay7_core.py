#!/usr/bin/env python3
"""General relay machinery, instantiated for the seven-loop OML.

The chain convention is ONE-SIDED ROOTED / ANY-POSITION: cells are
0,1,..., cell 0 has no left constraint, and a phase-r state is live iff
it occurs at some position n == r (mod p) on a rooted infinite path whose
target word contains exactly one 1.
"""
from collections import deque
from itertools import combinations, permutations, product


def loop(n):
    return tuple(frozenset((2*i, 2*i+1, (2*i+2) % (2*n))) for i in range(n))


BLOCKS = loop(7)
ATOMS = tuple(sorted(set().union(*BLOCKS)))
FACE_CLUSTER = frozenset((0, 3, 11))


def enumerate_states(blocks=BLOCKS):
    """All 0/1 states, represented by their value-one atom supports."""
    states = set()
    for choices in product(*[tuple(B) for B in blocks]):
        support = frozenset(choices)
        if all(len(support & B) == 1 for B in blocks):
            states.add(support)
    return tuple(sorted(states, key=lambda s: (len(s), tuple(sorted(s)))))


STATES = enumerate_states()
NS = len(STATES)
ALL = (1 << NS) - 1
SUPP = tuple(sum(1 << a for a in state) for state in STATES)
FACE = sum(1 << s for s, T in enumerate(STATES) if FACE_CLUSTER <= T)
COMPLEMENT = ALL ^ FACE
COMMON_ZERO_TARGETS = tuple(a for a in ATOMS
                            if all(a not in STATES[s] for s in range(NS)
                                   if FACE >> s & 1))

# The finite pasted OML's nontrivial symbols are atoms and their unique
# orthocomplements. Shared atoms have the same complement in every block.
SYMS = tuple([('a', a) for a in ATOMS] + [('c', a) for a in ATOMS])
IMG = {}
for kind, atom in SYMS:
    atom_img = sum(1 << s for s, T in enumerate(STATES) if atom in T)
    IMG[(kind, atom)] = atom_img if kind == 'a' else ALL ^ atom_img
NONORDER_W = tuple(IMG[x] & ~IMG[y] & ALL for x in SYMS for y in SYMS
                   if IMG[x] & ~IMG[y] & ALL)

SET = {a: [0, 0] for a in ATOMS}
for atom in ATOMS:
    for s, support in enumerate(SUPP):
        SET[atom][(support >> atom) & 1] |= 1 << s


def false_nonorders(state_mask):
    return sum(not bool(w & state_mask) for w in NONORDER_W)


def symbol_images(state_mask=ALL):
    """Images restricted to a chosen state set (useful for diagnostics)."""
    return {sym: image & state_mask for sym, image in IMG.items()}


def succ_masks(port):
    """Successor masks for an oriented injective atom port.

    ``port`` is an iterable of (old_atom, new_atom) identifications.
    """
    port = tuple(port)
    if len({i for i, _ in port}) != len(port) or len({j for _, j in port}) != len(port):
        raise ValueError('port must be injective on both sides')
    if any(i not in SET or j not in SET for i, j in port):
        raise ValueError('port contains an atom outside this OML')
    out = []
    for support in SUPP:
        allowed = ALL
        for old, new in port:
            allowed &= SET[new][(support >> old) & 1]
        out.append(allowed)
    return tuple(out)


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[x] = y


def quotient_blocks(maps, ncells):
    """Blocks in a finite window of the periodic relay quotient."""
    if not maps or ncells < 1:
        raise ValueError('maps must be nonempty and ncells positive')
    na = len(ATOMS)
    dsu = DSU(na * ncells)
    for cell in range(ncells - 1):
        for old, new in maps[cell % len(maps)]:
            dsu.union(na * cell + old, na * (cell + 1) + new)
    blocks = tuple(frozenset(dsu.find(na * cell + atom) for atom in block)
                   for cell in range(ncells) for block in BLOCKS)
    return blocks, dsu


def window_girth_ok(maps, ncells=2):
    """Whether the quotient window is linear with Berge girth at least five."""
    blocks, _ = quotient_blocks(maps, ncells)
    if any(len(block) != 3 for block in blocks):
        return False
    at_to_blocks = {}
    for bi, block in enumerate(blocks):
        for atom in block:
            at_to_blocks.setdefault(atom, []).append(bi)
    for atom0, incident in at_to_blocks.items():
        if len(incident) < 2:
            continue
        start = ('a', atom0)
        dist, parent = {start: 0}, {start: None}
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if dist[vertex] >= 5:
                continue
            neighbors = ([('b', b) for b in at_to_blocks[vertex[1]]]
                         if vertex[0] == 'a' else
                         [('a', a) for a in blocks[vertex[1]]])
            for neighbor in neighbors:
                if neighbor == parent[vertex]:
                    continue
                if neighbor in dist:
                    if dist[vertex] + dist[neighbor] + 1 < 10:
                        return False
                else:
                    dist[neighbor] = dist[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)
    return True


def two_cell_maps(k):
    """All labeled oriented injective k-atom ports (no symmetry quotient)."""
    if not 0 <= k <= len(ATOMS):
        raise ValueError('invalid port cardinality')
    for old in combinations(ATOMS, k):
        for new_set in combinations(ATOMS, k):
            for new in permutations(new_set):
                yield tuple(zip(old, new))


def _letters(target):
    if target not in ATOMS:
        raise ValueError('target is not an atom of this OML')
    letter = tuple((mask >> target) & 1 for mask in SUPP)
    l0 = sum(1 << s for s, x in enumerate(letter) if not x)
    return letter, l0, ALL ^ l0


def _forward(succ, l0mask, l1mask):
    """Rooted reachability indexed by phase and ones-so-far (0 or 1)."""
    p = len(succ)
    reach = [[0, 0] for _ in range(p)]
    reach[0] = [l0mask, l1mask]
    changed = True
    while changed:
        changed = False
        for r in range(p):
            r2 = (r + 1) % p
            for ones in (0, 1):
                image = 0
                for s in range(NS):
                    if (reach[r][ones] >> s) & 1:
                        image |= succ[r][s]
                additions = ((image & l0mask, image & l1mask) if ones == 0
                             else (0, image & l0mask))
                for k, add in enumerate(additions):
                    new = add & ~reach[r2][k]
                    if new:
                        reach[r2][k] |= new
                        changed = True
    return reach


def analyze(maps, target):
    """Analyze a nonempty periodic port list under rooted one-sided semantics."""
    if not maps:
        raise ValueError('at least one interface map is required')
    succ = tuple(succ_masks(port) for port in maps)
    p = len(succ)
    letter, l0mask, l1mask = _letters(target)

    # Infinite all-zero suffixes: greatest fixed point.
    e0 = [l0mask] * p
    changed = True
    while changed:
        changed = False
        for r in range(p):
            keep = sum(1 << s for s in range(NS)
                       if (e0[r] >> s) & 1 and succ[r][s] & e0[(r+1) % p])
            if keep != e0[r]:
                e0[r] = keep
                changed = True

    # Infinite suffixes containing exactly one 1: least fixed point over e0.
    e1 = [0] * p
    changed = True
    while changed:
        changed = False
        for r in range(p):
            nxt0, nxt1 = e0[(r+1) % p], e1[(r+1) % p]
            add = sum(1 << s for s in range(NS)
                      if not (e1[r] >> s) & 1 and
                      succ[r][s] & (nxt0 if letter[s] else nxt1))
            if add:
                e1[r] |= add
                changed = True

    reach = _forward(succ, l0mask, l1mask)
    live = [0] * p
    for r in range(p):
        nxt0, nxt1 = e0[(r+1) % p], e1[(r+1) % p]
        for s in range(NS):
            if (((reach[r][0] >> s) & 1 and succ[r][s] & nxt1) or
                    ((reach[r][1] >> s) & 1 and succ[r][s] & nxt0)):
                live[r] |= 1 << s
    # Rooted all-zero reachability intersected with infinite all-zero suffixes.
    zero_reach = [0] * p
    zero_reach[0] = l0mask
    changed = True
    while changed:
        changed = False
        for r in range(p):
            image = 0
            for s in range(NS):
                if zero_reach[r] >> s & 1:
                    image |= succ[r][s]
            r2 = (r + 1) % p
            new = image & l0mask & ~zero_reach[r2]
            if new:
                zero_reach[r2] |= new
                changed = True
    free = [zero_reach[r] & e0[r] for r in range(p)]
    return {'target': target, 'letter': letter, 'succ': succ, 'E0': e0,
            'E1': e1, 'reach': reach, 'live': live, 'free': free}


def screen(maps, target):
    """Operative phasewise conditions, leaving incidence girth to the census."""
    result = analyze(maps, target)
    result['face_free'] = [(mask & FACE) == FACE for mask in result['free']]
    result['face_nonlive'] = [not bool(mask & FACE) for mask in result['live']]
    result['complement_live'] = [mask & COMPLEMENT for mask in result['live']]
    result['false_nonorders'] = [false_nonorders(mask & COMPLEMENT)
                                 for mask in result['live']]
    result['exact_complement'] = [mask == COMPLEMENT for mask in result['live']]
    result['passes'] = (all(result['face_free']) and
                        all(result['face_nonlive']) and
                        not any(result['false_nonorders']))
    return result
