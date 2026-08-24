#!/usr/bin/env python3
"""Independent first census for the 7-loop FACE C={a0,a3,a11}.

Scope: every period-one oriented injective port map of widths k=1,2,3.
The relay is the one-sided chain rooted at cell 0.  A state is sigma-live
when it occurs somewhere on a rooted infinite path whose selected target word
has one 1.  The target is one of the six atoms vanishing on the whole face.

This audit is self-contained: it does not import relay_core or the expected
s35 builder.  It reports exact incidence/girth and operative FACE counts.
"""
from collections import deque, Counter
from itertools import combinations, permutations, product
from time import perf_counter
import argparse
import os

NATOM = 14
BLOCKS = [frozenset((2*i, 2*i+1, (2*i+2) % NATOM)) for i in range(7)]
FACE_CLUSTER = frozenset((0, 3, 11))
# The face states have common value zero exactly on these atoms.  Select one
# with AUDIT_TARGET; a0 is intentionally excluded from the operative audit.
TARGET = int(os.environ.get('AUDIT_TARGET', '1'))


def all_states():
    out = set()
    for chosen in product(*[tuple(b) for b in BLOCKS]):
        s = frozenset(chosen)
        if all(len(s & b) == 1 for b in BLOCKS):
            out.add(s)
    return sorted(out, key=lambda x: tuple(sorted(x)))


STATES = all_states()
NS = len(STATES)
SUPP = [sum(1 << a for a in s) for s in STATES]
ALL = (1 << NS) - 1
LETTER = [(m >> TARGET) & 1 for m in SUPP]
L0 = sum(1 << s for s in range(NS) if not LETTER[s])
FACE = sum(1 << s for s, T in enumerate(STATES) if FACE_CLUSTER <= T)
COMP = ALL ^ FACE
SET = [[[s for s in range(NS) if ((SUPP[s] >> a) & 1) == v]
        for v in (0, 1)] for a in range(NATOM)]
SETMASK = [[sum(1 << s for s in SET[a][v]) for v in (0, 1)]
           for a in range(NATOM)]


def witness_masks():
    imgs = []
    for a in range(NATOM):
        m = SETMASK[a][1]
        imgs.extend((m, ALL ^ m))
    return [x & ~y & ALL for x in imgs for y in imgs if x & ~y & ALL]


WITNESSES = witness_masks()


def order_determines(mask):
    return all(mask & w for w in WITNESSES)


def block_dist():
    atbl = [[i for i, B in enumerate(BLOCKS) if a in B] for a in range(NATOM)]
    adj = [[j for j in range(7) if BLOCKS[i] & BLOCKS[j]] for i in range(7)]
    d = [[99]*7 for _ in range(7)]
    for i in range(7):
        d[i][i] = 0
        q = deque([i])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if d[i][y] > d[i][x] + 1:
                    d[i][y] = d[i][x] + 1; q.append(y)
    return [[1 + min(d[i][j] for i in atbl[a] for j in atbl[b])
             for b in range(NATOM)] for a in range(NATOM)]


BD = block_dist()


def pair_ok(mp):
    return all(BD[a][b] + BD[x][y] >= 5
               for (a, x), (b, y) in combinations(mp, 2))


def window2_ok(mp):
    # In a two-cell window, every short cross-cell Berge cycle uses at least
    # two identifications.  Pair rule is therefore sufficient as well as
    # necessary, provided no block collapses under identifications.
    # Since each port is across distinct cells and maps are injective, blocks
    # cannot collapse internally.  Retain this named check for audit clarity.
    return pair_ok(mp)


def maps(k):
    for old in combinations(range(NATOM), k):
        for new in combinations(range(NATOM), k):
            for p in permutations(new):
                yield tuple(zip(old, p))


def succ(mp):
    out = []
    for s in range(NS):
        m = ALL
        for a, b in mp:
            m &= SETMASK[b][(SUPP[s] >> a) & 1]
        out.append(m)
    return out


def production_live(mp):
    """Period-one specialization of the rooted one-sided fixpoint method."""
    su = succ(mp)
    e0 = L0
    while True:
        z = sum(1 << s for s in range(NS)
                if (e0 >> s) & 1 and su[s] & e0)
        if z == e0: break
        e0 = z
    e1 = 0
    while True:
        z = e1
        for s in range(NS):
            if LETTER[s] and su[s] & e0 or not LETTER[s] and su[s] & e1:
                z |= 1 << s
        if z == e1: break
        e1 = z
    r0, r1 = L0, ALL ^ L0
    while True:
        a0 = a1 = 0
        for s in range(NS):
            if (r0 >> s) & 1:
                a0 |= su[s] & L0; a1 |= su[s] & ~L0
            if (r1 >> s) & 1:
                a1 |= su[s] & L0
        z0, z1 = r0 | a0, r1 | a1
        if (z0, z1) == (r0, r1): break
        r0, r1 = z0, z1
    live = 0
    for s in range(NS):
        if ((r0 >> s) & 1 and su[s] & e1) or ((r1 >> s) & 1 and su[s] & e0):
            live |= 1 << s
    zr = L0
    while True:
        image = 0
        for s in range(NS):
            if (zr >> s) & 1: image |= su[s]
        z = zr | (image & L0)
        if z == zr: break
        zr = z
    return live, zr & e0


def oracle_live(mp):
    """Independent explicit graph oracle: cycle detection + product BFS."""
    su = succ(mp)
    zbasin = 0
    for src in range(NS):
        if LETTER[src]: continue
        q = [(src, frozenset((src,)))]
        while q:
            v, seen = q.pop()
            for w in range(NS):
                if not ((su[v] >> w) & 1) or LETTER[w]: continue
                if w in seen:
                    zbasin |= 1 << src; q.clear(); break
                q.append((w, seen | {w}))
    ans = 0
    for wanted in range(NS):
        q = deque((s, LETTER[s], s == wanted) for s in range(NS))
        seen = set(q)
        while q:
            v, ones, hit = q.popleft()
            if hit and ones == 1 and ((zbasin >> v) & 1):
                ans |= 1 << wanted; break
            for w in range(NS):
                no = ones + LETTER[w]
                x = (w, no, hit or w == wanted)
                if no <= 1 and (su[v] >> w) & 1 and x not in seen:
                    seen.add(x); q.append(x)
    return ans


def census(k, limit=None, oracle_every=0):
    t = perf_counter(); total = valid = face_nonlive = operative = exact = checked = 0
    live_sizes = Counter()
    survivors = []
    for mp in maps(k):
        total += 1
        if limit and total > limit: break
        if not window2_ok(mp): continue
        valid += 1
        live, free = production_live(mp)
        if oracle_every and valid % oracle_every == 0:
            assert live == oracle_live(mp), mp
            checked += 1
        if (free & FACE) != FACE or live & FACE: continue
        face_nonlive += 1
        live_sizes[live.bit_count()] += 1
        if order_determines(live & COMP):
            operative += 1
            survivors.append((mp, live == COMP, live.bit_count()))
        if live == COMP:
            exact += 1
    dt = perf_counter() - t
    print(f'k={k} total={total if not limit else min(total,limit)} '
          f'girth2={valid} FACE-nonlive={face_nonlive} operative={operative} '
          f'exact-complement={exact} '
          f'oracle={checked} seconds={dt:.3f}')
    print('  FACE-nonlive live-size distribution:', dict(sorted(live_sizes.items())))
    for mp, is_exact, nlive in survivors:
        print(f'  SURVIVOR map={mp} live={nlive} exact-complement={is_exact}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--ks', nargs='+', type=int, default=(1, 2, 3))
    ap.add_argument('--limit', type=int)
    ap.add_argument('--oracle-every', type=int, default=500)
    args = ap.parse_args()
    assert TARGET in (1, 2, 4, 10, 12, 13), TARGET
    assert NS == 29 and FACE.bit_count() == 3
    assert order_determines(COMP)
    print(f'anchors: target=a{TARGET} states={NS} face={FACE.bit_count()} complement-OD=True '
          f'nonorders={len(WITNESSES)}')
    for k in args.ks:
        census(k, args.limit, args.oracle_every)
