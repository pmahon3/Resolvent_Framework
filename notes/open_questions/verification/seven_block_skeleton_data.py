#!/usr/bin/env python3
"""Emit a stable, substitution-ready certificate for the 56-event OML.

Events are encoded as 16-bit carrier masks.  The JSON contains the two
MO2 x MO2 charts, the seven maximal Boolean blocks, their atoms and
intersections, the centre, boundaries, and complete meet/join tables.
"""

import argparse
import json
from itertools import product
from pathlib import Path


SCHEMA = "seven-block-skeleton-v1"


def unions(atoms):
    return {frozenset().union(*(atoms[i] for i in range(len(atoms)) if mask >> i & 1))
            for mask in range(1 << len(atoms))}


def mo2(first, second):
    top = first[0] | first[1]
    assert top == second[0] | second[1]
    return {frozenset(), top, *first, *second}


def extrema(candidates, maximal):
    ans = [z for z in candidates
           if not any((z < w if maximal else w < z) for w in candidates)]
    assert len(ans) == 1
    return ans[0]


def maximal_cliques(vertices, adjacent):
    out = []

    def visit(r, p, x):
        if not p and not x:
            out.append(frozenset(r))
            return
        pivot = next(iter(p | x), None)
        neighbours = ({w for w in vertices if adjacent(pivot, w)} if pivot is not None
                      else set())
        for v in tuple(p - neighbours):
            nv = {w for w in vertices if w != v and adjacent(v, w)}
            visit(r | {v}, p & nv, x & nv)
            p.remove(v)
            x.add(v)

    visit(set(), set(vertices), set())
    return out


def boolean_closure(generators, univ):
    out = {frozenset(), univ, *generators}
    while True:
        old = set(out)
        out |= {univ - x for x in old}
        out |= {x & y for x in old for y in old}
        if out == old:
            return out


def has_join_tree(blocks, event_count):
    """Brute-force the 7^(7-2) labelled trees via Prüfer codes."""
    n = len(blocks)
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append((leaf, x))
            degree[leaf] -= 1
            degree[x] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.append((leaves[0], leaves[1]))
        valid = True
        for event in range(event_count):
            sites = {i for i, block in enumerate(blocks) if event in block}
            if len(sites) < 2:
                continue
            adjacency = {i: set() for i in sites}
            for left, right in edges:
                if left in sites and right in sites:
                    adjacency[left].add(right)
                    adjacency[right].add(left)
            seen, stack = set(), [next(iter(sites))]
            while stack:
                node = stack.pop()
                if node not in seen:
                    seen.add(node)
                    stack.extend(adjacency[node] - seen)
            if seen != sites:
                valid = False
                break
        if valid:
            return True
    return False


def build():
    omega = tuple(product(range(4), range(2), range(2)))
    univ = frozenset(omega)
    b = [frozenset(v for v in omega if v[0] == i) for i in range(4)]
    ca = [frozenset(v for v in omega if v[0] in side and v[1] == r)
          for side in ({0, 1}, {2, 3}) for r in range(2)]
    cb = [frozenset(v for v in omega if v[0] in side and v[2] == r)
          for side in ({0, 2}, {1, 3}) for r in range(2)]
    b_block, ca_block, cb_block = unions(b), unions(ca), unions(cb)
    la = {x | y for x in mo2(b[0:2], ca[0:2]) for y in mo2(b[2:4], ca[2:4])}
    lb = {x | y for x in mo2((b[0], b[2]), cb[0:2])
          for y in mo2((b[1], b[3]), cb[2:4])}
    logic = la | lb

    mask = lambda e: sum(1 << omega.index(v) for v in e)
    events = sorted(logic, key=mask)
    event_id = {e: i for i, e in enumerate(events)}
    meet = [[event_id[extrema([z for z in events if z <= x and z <= y], True)]
             for y in events] for x in events]
    join = [[event_id[extrema([z for z in events if x <= z and y <= z], False)]
             for y in events] for x in events]
    comp = {e: univ - e for e in events}

    def compatible(x, y):
        return join[event_id[meet_event(x, y)]][event_id[meet_event(x, comp[y])]] == event_id[x]

    def meet_event(x, y):
        return events[meet[event_id[x]][event_id[y]]]

    blocks = maximal_cliques(events, lambda x, y: x != y and compatible(x, y))
    blocks.sort(key=lambda block: tuple(sorted(mask(e) for e in block)))

    def atoms(block):
        return sorted((e for e in block if e and not any(f and f < e for f in block)), key=mask)

    boundaries = []
    for block in blocks:
        shared = set().union(*(block & other for other in blocks if other != block))
        boundaries.append(boolean_closure(shared, univ))
    centre = {e for e in events if all(compatible(e, f) for f in events)}

    named = {"B": b_block, "Ca": ca_block, "Cb": cb_block}
    name_by_block = {frozenset(v): k for k, v in named.items()}
    block_names = [name_by_block.get(block, f"D{i}") for i, block in enumerate(blocks)]
    # Make generated names stable even if a Python implementation changes clique order.
    next_d = 0
    for i, name in enumerate(block_names):
        if name.startswith("D"):
            block_names[i] = f"D{next_d}"
            next_d += 1

    pairwise = []
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            overlap = blocks[i] & blocks[j]
            pairwise.append({"left": block_names[i], "right": block_names[j],
                             "size": len(overlap),
                             "events": sorted(event_id[e] for e in overlap)})

    id_blocks = [{event_id[e] for e in block} for block in blocks]

    return {
        "schema": SCHEMA,
        "carrier": {"coordinates": ["q in 0..3", "r in 0..1", "s in 0..1"],
                    "size": len(omega)},
        "counts": {"events": len(events), "La": len(la), "Lb": len(lb),
                   "La_inter_Lb": len(la & lb), "maximal_blocks": len(blocks),
                   "centre": len(centre)},
        "event_masks": [mask(e) for e in events],
        "complement": [event_id[comp[e]] for e in events],
        "meet": meet,
        "join": join,
        "charts": {"La": sorted(event_id[e] for e in la),
                   "Lb": sorted(event_id[e] for e in lb),
                   "intersection": sorted(event_id[e] for e in la & lb),
                   "rule": "La and Lb are products of two six-element MO2 intervals"},
        "generators": {"B_atoms": [event_id[e] for e in b],
                       "Ca_atoms": [event_id[e] for e in ca],
                       "Cb_atoms": [event_id[e] for e in cb],
                       "rule": "La=<B,Ca>, Lb=<B,Cb>, L*=La union Lb"},
        "blocks": [{"name": block_names[i], "events": sorted(event_id[e] for e in block),
                    "atoms": [event_id[e] for e in atoms(block)],
                    "boundary": sorted(event_id[e] for e in boundaries[i])}
                   for i, block in enumerate(blocks)],
        "pairwise_intersections": pairwise,
        "centre": sorted(event_id[e] for e in centre),
        "checks": {
            "La_inter_Lb_is_B": la & lb == b_block,
            "orthomodular": all(join[event_id[x]][meet[event_id[y]][event_id[comp[x]]]] == event_id[y]
                                 for x in events for y in events if x <= y),
            "all_boundaries_saturate": all(boundaries[i] == set(blocks[i]) for i in range(7)),
            "centre_is_trivial": centre == {frozenset(), univ},
            "incidence_has_join_tree": has_join_tree(id_blocks, len(events)),
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
