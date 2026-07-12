#!/usr/bin/env python3
"""s33 relay-census core (2026-07-11).

Machinery for the corrected three-condition screen of attack-note S26 /
HANDOFF_2026-07-11_s32.md, written from scratch against the stated
semantics.  Conventions (pinned by exact reproduction of the s32 numbers
in s33_reproduce_s32.py before any new census ran):

Architecture.  One-sided infinite chain of pentagon (Greechie 5-loop)
cells n = 0,1,2,...; the interface between cell n and cell n+1 is the
oriented injective atom identification maps[n mod p] (old atom i of cell
n = new atom j of cell n+1).  Cell 0 is unconstrained on the left.
Every cell carries its own target D_n = a_0^n (census over all maps
covers the other even targets by rotational symmetry).

States.  Two-valued states of a pentagon = 11; s_* = the all-odd state
supp {a1,a3,a5,a7,a9}.  A chain path is a sequence (T_0,T_1,...) with
T_n(i) = T_{n+1}(j) for each identification (i,j) at interface n.  The
target word is w_n = T_n(a_0).

sigma-liveness (S24).  A local state T at phase r is sigma-live
(any-position convention, the default) iff some infinite chain path has
T at a position congruent to r and total target word with exactly one 1.
Boundary-root-only convention: the exactly-one path must start at T in
cell 0.

Important: this is a ONE-SIDED, boundary-rooted chain with an
ANY-POSITION query.  Consequently, replacing [m] by [m,m,m] need not give
the same live set at phases 1 and 2: those phases require a compatible
finite prefix from cell 0.  Cyclic rotation likewise moves the boundary.
Period-collapse and rotation invariance are tests for a different,
two-sided/translation-invariant convention, not for this definition.

Corrected screen (S26), filter order per HANDOFF s32:
  0. incidence validity / two-cell-window girth >= 5 (linear, no Berge
     3/4-cycles);
  1. s_* has a free path: an all-zero-target infinite chain path through
     s_* (fixed point OR basin; s32 used the self-loop form, also
     computed here for the reproduction);
  2. s_* is NOT sigma-live;
  3. the sigma-live local states order-determine the pentagon: zero
     false non-orders among the 20 nontrivial symbols (10 atoms + 10
     coatoms; 350 non-order pairs total, so empty live set scores 350).
Later stages (adjacent/cross-cell separation, master geometry) apply
only to survivors.  Master-cycle girth diagnostic: shortest master Berge
cycle = d_g + 1 where d_g = minimal number of blocks in a block-chain
from a D_m-block to a D_{m+g}-block in the chain quotient; requirement
min_g d_g >= 4.
"""
from itertools import combinations, permutations
from collections import deque

# ---------------------------------------------------------------- pentagon
BLOCKS = [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % 10}) for i in range(5)]


def _all_states():
    out = []
    for r in range(3):
        for pos in combinations(range(5), r):
            if any(((b - a) % 5) in (1, 4) for a in pos for b in pos if a != b):
                continue
            T = {2 * i for i in pos}
            for i in range(5):
                if not (T & BLOCKS[i]):
                    T.add(2 * i + 1)
            out.append(frozenset(T))
    assert len(out) == len(set(out)) == 11
    return sorted(out, key=sorted)


STATES = _all_states()
NS = 11
SUPP = [sum(1 << a for a in T) for T in STATES]          # atom bitmask per state
S_STAR = next(s for s in range(NS) if STATES[s] == frozenset({1, 3, 5, 7, 9}))
TARGET = 0                                                # D = a_0
LETTER = [(SUPP[s] >> TARGET) & 1 for s in range(NS)]
ALL = (1 << NS) - 1
L0MASK = sum(1 << s for s in range(NS) if LETTER[s] == 0)
L1MASK = ALL ^ L0MASK

# symbols: 20 nontrivial elements (atoms + coatoms), imgs as 11-bit masks
SYMS = [('a', i) for i in range(10)] + [('c', i) for i in range(10)]
IMG = {}
for sym in SYMS:
    kind, i = sym
    m = 0
    for s in range(NS):
        v = (SUPP[s] >> i) & 1
        if (kind == 'a' and v) or (kind == 'c' and not v):
            m |= 1 << s
    IMG[sym] = m

# non-orders in the canonical (all-11-state) order; witness masks
NONORDER_W = []
for x in SYMS:
    for y in SYMS:
        if IMG[x] & ~IMG[y] & ALL:                        # x <= y fails
            NONORDER_W.append(IMG[x] & ~IMG[y] & ALL)
assert len(NONORDER_W) == 350

# SET[j][b] = mask of states giving atom j value b (for succ computation)
SET = [[0, 0] for _ in range(10)]
for j in range(10):
    for s in range(NS):
        SET[j][(SUPP[s] >> j) & 1] |= 1 << s


def false_nonorders(live_mask):
    """Number of abstract non-orders x !<= y that the live set fails to
    witness (0 = live states order-determine the pentagon)."""
    return sum(1 for w in NONORDER_W if not (w & live_mask))


def succ_masks(mp):
    """mp = tuple of (i, j): old atom i of cell n = new atom j of cell n+1.
    Returns succ[s] = bitmask of allowed next-cell states."""
    out = []
    for s in range(NS):
        m = ALL
        sup = SUPP[s]
        for i, j in mp:
            m &= SET[j][(sup >> i) & 1]
        out.append(m)
    return out


# ------------------------------------------------------- liveness automaton
def analyze(maps):
    """maps = list of p interface maps (period p; maps[r] glues cell n=r mod p
    to cell n+1).  Returns dict with per-phase data:
      E0, E1, live, live_root, free  -- lists (len p) of 11-bit masks.
    Node (r, s) encoded as bit s of phase-r mask.
    """
    p = len(maps)
    succ = [succ_masks(mp) for mp in maps]                # succ[r][s] -> phase r+1 mask

    # E0: greatest fixed point of {letter 0, has successor in E0}
    E0 = [L0MASK] * p
    changed = True
    while changed:
        changed = False
        for r in range(p):
            nxt = E0[(r + 1) % p]
            m = 0
            cur = E0[r]
            for s in range(NS):
                if (cur >> s) & 1 and (succ[r][s] & nxt):
                    m |= 1 << s
            if m != cur:
                E0[r] = m
                changed = True

    # E1: least fixed point: letter1 & succ-in-E0, or letter0 & succ-in-E1
    E1 = [0] * p
    changed = True
    while changed:
        changed = False
        for r in range(p):
            nxtE0, nxtE1 = E0[(r + 1) % p], E1[(r + 1) % p]
            m = E1[r]
            for s in range(NS):
                if (m >> s) & 1:
                    continue
                if LETTER[s]:
                    if succ[r][s] & nxtE0:
                        m |= 1 << s
                else:
                    if succ[r][s] & nxtE1:
                        m |= 1 << s
            if m != E1[r]:
                E1[r] = m
                changed = True

    # forward reachability from cell 0 (phase 0, all 11 states admissible),
    # tracking ones-so-far INCLUDING the current node's letter, capped at 2
    R = [[0, 0] for _ in range(p)]                        # R[r][k] masks, k=0,1
    R[0][0] = L0MASK
    R[0][1] = L1MASK
    # BFS over (phase, k); phases wrap, so iterate to fixpoint
    changed = True
    while changed:
        changed = False
        for r in range(p):
            r2 = (r + 1) % p
            for k in (0, 1):
                src = R[r][k]
                if not src:
                    continue
                agg = 0
                for s in range(NS):
                    if (src >> s) & 1:
                        agg |= succ[r][s]
                # distribute by letter of target node
                add0 = agg & (L0MASK if k == 0 else 0)
                add1 = agg & ((L1MASK if k == 0 else 0) | (L0MASK if k == 1 else 0))
                if k == 0:
                    new0 = add0 & ~R[r2][0]
                    new1 = (agg & L1MASK) & ~R[r2][1]
                    if new0:
                        R[r2][0] |= new0
                        changed = True
                    if new1:
                        R[r2][1] |= new1
                        changed = True
                else:
                    new1 = (agg & L0MASK) & ~R[r2][1]
                    if new1:
                        R[r2][1] |= new1
                        changed = True

    # all-zero-prefix reachability (for the free-path condition)
    Z = [0] * p
    Z[0] = L0MASK
    changed = True
    while changed:
        changed = False
        for r in range(p):
            src = Z[r]
            if not src:
                continue
            r2 = (r + 1) % p
            agg = 0
            for s in range(NS):
                if (src >> s) & 1:
                    agg |= succ[r][s]
            new = agg & L0MASK & ~Z[r2]
            if new:
                Z[r2] |= new
                changed = True

    live = [0] * p
    for r in range(p):
        nxtE0, nxtE1 = E0[(r + 1) % p], E1[(r + 1) % p]
        for s in range(NS):
            c0 = bool(succ[r][s] & nxtE0)
            c1 = bool(succ[r][s] & nxtE1)
            ok = ((R[r][0] >> s) & 1 and c1) or ((R[r][1] >> s) & 1 and c0)
            # a terminal 1 with all-zero continuation: letter 1, R0 impossible
            if ok:
                live[r] |= 1 << s

    live_root = [E1[0] if r == 0 else 0 for r in range(p)]
    free = [Z[r] & E0[r] for r in range(p)]
    return {'succ': succ, 'E0': E0, 'E1': E1, 'live': live,
            'live_root': live_root, 'free': free}


# ------------------------------------------------- incidence quotient/girth
class DSU:
    __slots__ = ('p',)

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def quotient_blocks(maps, ncells):
    """Blocks of the ncells-cell window quotient, as frozensets of atom
    classes.  maps applied periodically.  Returns (blocks, atom_class fn)."""
    p = len(maps)
    n_at = 10 * ncells
    dsu = DSU(n_at)
    for c in range(ncells - 1):
        for i, j in maps[c % p]:
            dsu.union(10 * c + i, 10 * (c + 1) + j)
    blocks = []
    for c in range(ncells):
        for B in BLOCKS:
            blocks.append(frozenset(dsu.find(10 * c + a) for a in B))
    return blocks, dsu


def window_girth_ok(maps, ncells):
    """True iff the ncells-window quotient is a linear (pairwise block
    intersections <= 1) Greechie incidence with no Berge 3- or 4-cycles,
    i.e. bipartite block-atom incidence girth >= 10.  Blocks must keep 3
    distinct atoms."""
    blocks, dsu = quotient_blocks(maps, ncells)
    if any(len(B) != 3 for B in blocks):
        return False
    # adjacency: atom class -> list of block indices
    at2bl = {}
    for bi, B in enumerate(blocks):
        for a in B:
            at2bl.setdefault(a, []).append(bi)
    # linearity: two blocks sharing two atoms = bipartite 4-cycle; catch below
    # bipartite girth via BFS from every atom class that lies in >= 2 blocks
    # (every Berge cycle passes through such atoms); need girth >= 10
    nb = len(blocks)
    for a0, bls in at2bl.items():
        if len(bls) < 2:
            continue
        # BFS in bipartite graph from atom a0; vertices ('a',x) / ('b',i)
        dist = {('a', a0): 0}
        par = {('a', a0): None}
        q = deque([('a', a0)])
        while q:
            v = q.popleft()
            dv = dist[v]
            if dv >= 5:                                   # half of 10
                continue
            if v[0] == 'a':
                nbrs = [('b', i) for i in at2bl[v[1]]]
            else:
                nbrs = [('a', x) for x in blocks[v[1]]]
            for w in nbrs:
                if w == par[v]:
                    continue
                if w in dist:
                    # cycle through a0 of length dist[v]+dist[w]+1 <= 10?
                    if dist[v] + dist[w] + 1 < 10:
                        return False
                else:
                    dist[w] = dv + 1
                    par[w] = v
                    q.append(w)
    return True


# ---- fast necessary pre-filter for two-cell windows: pairwise crossing rule
# BODIST[x][y] = minimal number of blocks in a pentagon block-chain from an
# x-block to a y-block (1 if they share a block).
def _block_dist_table():
    # block graph of the pentagon: blocks 0..4 in a 5-cycle
    import itertools
    tbl = [[None] * 10 for _ in range(10)]
    at_bl = {a: [i for i in range(5) if a in BLOCKS[i]] for a in range(10)}
    # distance between blocks in C5
    def bdist(i, j):
        d = abs(i - j) % 5
        return min(d, 5 - d)
    for x in range(10):
        for y in range(10):
            tbl[x][y] = 1 + min(bdist(i, j) for i in at_bl[x] for j in at_bl[y])
            if any(i == j for i in at_bl[x] for j in at_bl[y]) and x != y:
                tbl[x][y] = 1
            if x == y:
                tbl[x][y] = 1
    return tbl


BODIST = _block_dist_table()


def pair_prefilter_ok(mp):
    """Necessary condition for two-cell girth >= 5: every pair of crossings
    (i1,j1),(i2,j2) satisfies BODIST[i1][i2] + BODIST[j1][j2] >= 5."""
    for (i1, j1), (i2, j2) in combinations(mp, 2):
        if BODIST[i1][i2] + BODIST[j1][j2] < 5:
            return False
    return True


# ------------------------------------------------------ master-cycle girth
def master_gap_dists(maps, gaps=(1, 2, 3, 4, 5, 6), window=16, base=4):
    """d_g = minimal number of blocks in a chain of pairwise-adjacent blocks
    from a block containing D_base to a block containing D_{base+g}, in the
    window quotient.  Master-cycle girth requirement: min d_g >= 4."""
    blocks, dsu = quotient_blocks(maps, window)
    nb = len(blocks)
    adj = [[] for _ in range(nb)]
    for a in range(nb):
        for b in range(a + 1, nb):
            if blocks[a] & blocks[b]:
                adj[a].append(b)
                adj[b].append(a)
    out = {}
    for g in gaps:
        src = dsu.find(10 * base + TARGET)
        tgt = dsu.find(10 * (base + g) + TARGET)
        starts = [i for i in range(nb) if src in blocks[i]]
        goals = {i for i in range(nb) if tgt in blocks[i]}
        dist = {i: 1 for i in starts}
        q = deque(starts)
        best = None
        while q:
            v = q.popleft()
            if v in goals:
                best = dist[v]
                break
            for w in adj[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
        out[g] = best
    return out


# ------------------------------------------------------------- enumeration
def two_cell_maps(k):
    """All oriented injective k-atom identifications between two pentagons:
    sorted tuples of (i, j), old atoms distinct, new atoms distinct."""
    olds = list(combinations(range(10), k))
    news = list(combinations(range(10), k))
    for O in olds:
        for N in news:
            for perm in permutations(N):
                yield tuple(sorted(zip(O, perm)))
