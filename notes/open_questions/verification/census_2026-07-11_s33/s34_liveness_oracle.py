#!/usr/bin/env python3
"""Independent checks for the one-sided, any-position sigma-live semantics.

The chain has cells n >= 0 and interface phase n mod p.  A node (r, s) is
live when a rooted infinite path, starting at an arbitrary state in cell 0,
visits state s at some cell n == r (mod p) and has exactly one target 1.

This oracle deliberately does not use relay_core.analyze or its fixpoints.
It constructs the finite phase/state graph, finds the all-zero vertices from
which an infinite zero path exists by SCC analysis, and performs an explicit
product-graph search with a saturated ones counter and a visited-node flag.
"""
from collections import deque
from itertools import product
import random

from relay_core import NS, LETTER, succ_masks, analyze, two_cell_maps


def graph(maps):
    """Return adjacency lists on vertices (phase, state)."""
    p = len(maps)
    sm = [succ_masks(m) for m in maps]
    adj = [[] for _ in range(p * NS)]
    for r, s in product(range(p), range(NS)):
        mask = sm[r][s]
        for t in range(NS):
            if (mask >> t) & 1:
                adj[r * NS + s].append(((r + 1) % p) * NS + t)
    return adj


def zero_infinite_basin(adj):
    """Zero-letter vertices that can reach a directed zero cycle."""
    n = len(adj)
    zadj = [[w for w in adj[v] if LETTER[w % NS] == 0]
            if LETTER[v % NS] == 0 else [] for v in range(n)]

    # A simple per-source reachability test is intentionally used here rather
    # than the production greatest fixed point.  The graph has at most 33
    # vertices in the current tests.
    basin = set()
    for src in range(n):
        if LETTER[src % NS]:
            continue
        paths = [(src, frozenset({src}))]
        while paths:
            v, seen = paths.pop()
            for w in zadj[v]:
                if w in seen:
                    basin.add(src)
                    paths.clear()
                    break
                paths.append((w, seen | {w}))
    return basin


def oracle_live(maps):
    """Exhaustive product-graph oracle, returned as one mask per phase."""
    p = len(maps)
    adj = graph(maps)
    zbasin = zero_infinite_basin(adj)
    out = [0] * p

    for wanted in range(p * NS):
        # State is (graph vertex, ones so far, wanted vertex has been seen).
        q = deque()
        seen = set()
        for s in range(NS):
            v = s  # phase zero
            item = (v, LETTER[s], v == wanted)
            if item[1] <= 1:
                seen.add(item)
                q.append(item)
        ok = False
        while q and not ok:
            v, ones, hit = q.popleft()
            if hit and ones == 1 and v in zbasin:
                ok = True
                break
            for w in adj[v]:
                no = ones + LETTER[w % NS]
                item = (w, no, hit or w == wanted)
                if no <= 1 and item not in seen:
                    seen.add(item)
                    q.append(item)
        if ok:
            out[wanted // NS] |= 1 << (wanted % NS)
    return out


def check(samples=200, seed=3401):
    rng = random.Random(seed)
    pool = list(two_cell_maps(1)) + list(two_cell_maps(2))
    tested = 0
    for p in (1, 2, 3):
        for _ in range(samples):
            maps = [rng.choice(pool) for _ in range(p)]
            got = analyze(maps)['live']
            want = oracle_live(maps)
            assert got == want, (p, maps, got, want)
            tested += 1
    print('one-sided oracle agreement:', tested, '/', tested)


if __name__ == '__main__':
    check()
