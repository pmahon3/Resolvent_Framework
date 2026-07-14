#!/usr/bin/env python3
"""Independent verifier for q_certificate.json (does not import producer)."""
from __future__ import annotations

import hashlib
import itertools
import json
import time
from pathlib import Path

import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher, categorical_node_match

LABELS = ("g", "h", "W", "Vi", "Vj", "R")
TOP = (1 << 18) - 1
FIBRE_TOP = (1 << 6) - 1


def bits(column, labels):
    return sum(1 << (6 * column + LABELS.index(label)) for label in labels)


def reconstruct_generators():
    s = [0, 0, 0]
    g = {(1, 2): 0, (1, 3): 0, (2, 3): 0}
    for column, typ in enumerate((1, 2, 3)):
        a, b = sorted(set((1, 2, 3)) - {typ})
        local = {typ: ("g", "h"), a: ("g", "W", "Vi"), b: ("h", "W", "Vj")}
        for i in (1, 2, 3):
            s[i - 1] |= bits(column, local[i])
        for edge in g:
            if typ in edge:
                endpoint = next(i for i in edge if i != typ)
                g[edge] |= bits(column, ("g",) if endpoint == a else ("h",))
    c = [FIBRE_TOP << (6 * i) for i in range(3)]
    return c + s + [g[e] for e in ((1, 2), (1, 3), (2, 3))]


def dynkin(seed):
    result = {0, TOP} | set(seed)
    changed = True
    while changed:
        changed = False
        for event in tuple(result):
            if TOP ^ event not in result:
                result.add(TOP ^ event); changed = True
        snapshot = tuple(result)
        for i, left in enumerate(snapshot):
            for right in snapshot[i + 1:]:
                if left & right == 0 and left | right not in result:
                    result.add(left | right); changed = True
    return result


def sections(event):
    return tuple((event >> (6 * i)) & FIBRE_TOP for i in range(3))


def incidence_automorphisms(events):
    graph = nx.Graph()
    graph.add_nodes_from((("point", i), {"colour": 0}) for i in range(18))
    for j, event in enumerate(sorted(events)):
        graph.add_node(("set", j), colour=1)
        graph.add_edges_from((('point', i), ('set', j)) for i in range(18) if event >> i & 1)
    gm = GraphMatcher(graph, graph, node_match=categorical_node_match("colour", -1))
    return sorted({tuple(f[("point", i)][1] for i in range(18)) for f in gm.isomorphisms_iter()})


def main():
    start = time.perf_counter()
    path = Path(__file__).with_name("q_certificate.json")
    cert = json.loads(path.read_text())
    names = ["C1", "C2", "C3", "S1", "S2", "S3", "G12", "G13", "G23"]
    generators = reconstruct_generators()
    assert cert["primitive_masks"] == dict(zip(names, generators))
    events = dynkin(generators)
    assert len(events) == cert["closure_size"] == 88
    digest = hashlib.sha256(",".join(map(str, sorted(events))).encode()).hexdigest()
    assert digest == cert["closure_sha256"]
    profiles = sorted(map(list, map(sections, events)))
    assert profiles == cert["profiles"]
    p1 = [sorted({p[i] for p in profiles}) for i in range(3)]
    assert p1 == cert["projection_1"] and list(map(len, p1)) == [24, 24, 24]
    p2 = {f"{i+1}{j+1}": sorted([list(x) for x in {(p[i], p[j]) for p in profiles}])
          for i, j in ((0, 1), (0, 2), (1, 2))}
    assert p2 == cert["projection_2"]
    assert [len(p2[k]) for k in ("12", "13", "23")] == [78, 78, 78]
    distribution = {str(k): sum(sum(x in (0, FIBRE_TOP) for x in p) == k for p in profiles)
                    for k in range(4)}
    assert distribution == cert["binary_coordinate_count_distribution"] == {"0": 44, "1": 36, "2": 0, "3": 8}
    regenerated = []
    proper = [sorted(set(p1[i]) - {0, FIBRE_TOP}) for i in range(3)]
    for count in range(1, 4):
        for binary in itertools.combinations(range(3), count):
            fixed = tuple(i for i in range(3) if i not in binary)
            for values in itertools.product(*(proper[i] for i in fixed)):
                relation = sorted({tuple(p[i] // FIBRE_TOP for i in binary) for p in profiles
                                   if all(p[i] in (0, FIBRE_TOP) for i in binary)
                                   and all(p[i] == v for i, v in zip(fixed, values))})
                if relation:
                    rectangle = sorted(itertools.product(*[{r[j] for r in relation} for j in range(count)]))
                    regenerated.append({"binary_coordinates": [i + 1 for i in binary],
                                        "fixed_proper": {str(i + 1): v for i, v in zip(fixed, values)},
                                        "relation": [list(r) for r in relation],
                                        "rectangular": relation == rectangle})
    assert regenerated == cert["nonempty_fixed_proper_strata"]
    assert len(regenerated) == 19 and all(x["rectangular"] for x in regenerated)
    minimal = []
    for mask in range(512):
        if dynkin([g for i, g in enumerate(generators) if mask >> i & 1]) == events:
            if not any(mask & old == old for old in minimal): minimal.append(mask)
    named_minimal = [[names[i] for i in range(9) if mask >> i & 1] for mask in minimal]
    assert named_minimal == cert["minimal_named_generating_sets"]
    deletion = {names[i]: len(dynkin(generators[:i] + generators[i + 1:])) for i in range(9)}
    assert deletion == cert["single_deletion_closure_sizes"]
    autos = incidence_automorphisms(events)
    assert [list(p) for p in autos] == cert["incidence_hypergraph_automorphisms"]
    assert len(autos) == 6
    print("ALL CHECKS PASS", {"profiles": len(events), "strata": len(regenerated),
          "automorphisms": len(autos), "runtime_seconds": time.perf_counter() - start})


if __name__ == "__main__":
    main()
