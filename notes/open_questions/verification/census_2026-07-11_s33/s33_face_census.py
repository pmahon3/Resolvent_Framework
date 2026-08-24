#!/usr/bin/env python3
"""s33 removable-FACE census on finite Greechie OMLs (Exit C route).

A Greechie OML here = a connected linear 3-uniform hypergraph (blocks =
3-atom lines, any two share <= 1 atom) with Berge girth >= 5.  Elements:
0, 1, atoms, and per-block coatoms (block-orthocomplements of atoms).
Two-valued states = choices of one value-1 atom per block, consistent on
shared atoms (a value-1 atom set meeting each block in exactly one atom).

Concrete representation over ALL two-valued states Omega:
  atom a  -> {s : a in s},   coatom (a in block B) -> {s : a not in s}.
Non-order pairs among the 2*(#atoms) nontrivial symbols are read off Omega.
A subset S of states is ORDER-DETERMINING iff every canonical non-order
x !<= y has a witness state in S (s(x)=1, s(y)=0).

CLUSTER = set of pairwise-incompatible atoms (pairwise distinct, no shared
block).  FACE F(C) = {s : s(c)=1 for all c in C}.
HIT = |F(C)| >= 2 AND Omega \ F(C) still order-determining.
(The pentagon's single removable state s_* is the |F|=1 degenerate case.)

We census specific high-value families (odd/even loops, pentagon with
pendants, two pentagons sharing one atom) exhaustively and report exactly
what was covered.  Anchors: pentagon (5-loop) must give 11 states, C_* =
odd atoms isolates exactly {s_*}, Omega\{s_*} order-determines, and every
other single state is indispensable.
"""
from itertools import combinations, product


def states_of(blocks, atoms):
    """All two-valued states: value-1 atom sets meeting each block once."""
    out = []
    for chosen in product(*[list(b) for b in blocks]):
        T = frozenset(chosen)
        if all(len(T & set(b)) == 1 for b in blocks):
            out.append(T)
    return sorted(set(out), key=sorted)


def berge_girth_ok(blocks):
    """Linear + bipartite incidence girth >= 10 (no Berge 3/4-cycles)."""
    from collections import deque
    # linearity
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if len(set(blocks[i]) & set(blocks[j])) > 1:
                return False
    at2bl = {}
    for bi, B in enumerate(blocks):
        for a in B:
            at2bl.setdefault(a, []).append(bi)
    for a0, bls in at2bl.items():
        if len(bls) < 2:
            continue
        dist = {('a', a0): 0}
        par = {('a', a0): None}
        q = deque([('a', a0)])
        while q:
            v = q.popleft()
            if dist[v] >= 5:
                continue
            nbrs = ([('b', i) for i in at2bl[v[1]]] if v[0] == 'a'
                    else [('a', x) for x in blocks[v[1]]])
            for w in nbrs:
                if w == par[v]:
                    continue
                if w in dist:
                    if dist[v] + dist[w] + 1 < 10:
                        return False
                else:
                    dist[w] = dist[v] + 1
                    par[w] = v
                    q.append(w)
    return True


def analyze_oml(blocks):
    atoms = sorted({a for b in blocks for a in b})
    Omega = states_of(blocks, atoms)
    if len(Omega) < 2:
        return None
    # symbols and images
    syms = [('a', a) for a in atoms]
    blk_of = {}
    for B in blocks:
        for a in B:
            blk_of.setdefault(a, B)
    syms += [('c', a) for a in atoms]
    idx = {s: i for i, s in enumerate(Omega)}
    ALL = (1 << len(Omega)) - 1
    img = {}
    for kind, a in syms:
        m = 0
        for s in Omega:
            v = 1 if a in s else 0
            if (kind == 'a' and v) or (kind == 'c' and not v):
                m |= 1 << idx[s]
        img[(kind, a)] = m
    nonorder_w = []
    for x in syms:
        for y in syms:
            w = img[x] & ~img[y] & ALL
            if w:
                nonorder_w.append(w)
    return {'blocks': blocks, 'atoms': atoms, 'Omega': Omega, 'idx': idx,
            'ALL': ALL, 'nonorder_w': nonorder_w}


def order_determining(info, Smask):
    return all(w & Smask for w in info['nonorder_w'])


def clusters(info, maxsize=6):
    """Pairwise-incompatible atom sets (no shared block), size >= 1."""
    atoms = info['atoms']
    blk = {}
    for B in info['blocks']:
        for a in B:
            blk.setdefault(a, set()).add(id(B))
    # two atoms incompatible iff no common block
    def incomp(a, b):
        return a != b and not (set(
            i for i, B in enumerate(info['blocks']) if a in B) &
            set(i for i, B in enumerate(info['blocks']) if b in B))
    res = []
    for r in range(1, min(maxsize, len(atoms)) + 1):
        for C in combinations(atoms, r):
            if all(incomp(a, b) for a, b in combinations(C, 2)):
                res.append(C)
    return res


def face_hits(info, min_face=2):
    """Clusters whose face has >= min_face states and whose complement is
    order-determining.  Returns list of (cluster, face_indices)."""
    Omega, idx, ALL = info['Omega'], info['idx'], info['ALL']
    hits = []
    removable_singletons = []
    for C in clusters(info):
        face = [i for i, s in enumerate(Omega) if all(c in s for c in C)]
        if not face:
            continue
        comp = ALL & ~sum(1 << i for i in face)
        od = order_determining(info, comp)
        if len(face) == 1 and od:
            removable_singletons.append((C, face))
        if len(face) >= min_face and od:
            hits.append((C, face))
    return hits, removable_singletons


# ------------------------------------------------------------- geometries
def loop(n):
    """n-loop: blocks {2i,2i+1,2i+2 mod 2n}, i=0..n-1."""
    return [(2 * i, 2 * i + 1, (2 * i + 2) % (2 * n)) for i in range(n)]


def pentagon_with_pendant():
    """5-loop + one extra block hanging off an even atom (fresh atoms)."""
    B = loop(5)
    B.append((0, 100, 101))
    return B


def two_pentagons_share_atom():
    """Two 5-loops sharing exactly one atom."""
    B1 = loop(5)
    B2 = [(a + 200 if a != 0 else 0, b + 200, c + 200) for (a, b, c) in loop(5)]
    return B1 + B2


def report(name, blocks):
    if not berge_girth_ok(blocks):
        print(f'[{name}] girth < 5 -- skipped'); return
    info = analyze_oml(blocks)
    if info is None:
        print(f'[{name}] < 2 states'); return
    nS = len(info['Omega'])
    full_od = order_determining(info, info['ALL'])
    hits, singles = face_hits(info)
    print(f'[{name}] states={nS} full-set-order-determining={full_od} '
          f'removable-singletons={len(singles)} FACE-HITS(|F|>=2)={len(hits)}')
    for C, face in hits[:6]:
        print(f'    HIT cluster={C} |face|={len(face)} '
              f'face_supports={[sorted(info["Omega"][i]) for i in face]}')
    if name == 'loop-5':
        # anchors
        assert nS == 11, nS
        odd = (1, 3, 5, 7, 9)
        f = [i for i, s in enumerate(info['Omega']) if all(c in s for c in odd)]
        assert len(f) == 1, f
        comp = info['ALL'] & ~(1 << f[0])
        assert order_determining(info, comp)
        # every other single state indispensable
        bad = sum(1 for i in range(nS)
                  if i != f[0] and order_determining(info, info['ALL'] & ~(1 << i)))
        assert bad == 0, bad
        print('    [anchor OK] pentagon: 11 states, odd-cluster isolates the '
              'unique removable s_*, all others indispensable')


if __name__ == '__main__':
    for n in (5, 6, 7, 8, 9):
        report(f'loop-{n}', loop(n))
    report('pentagon+pendant', pentagon_with_pendant())
    report('two-pentagons-1shared', two_pentagons_share_atom())
