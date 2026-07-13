#!/usr/bin/env python3
"""Census block-subfamily completions of the certified 56-event OML.

The universe is exactly the 127 nonempty subfamilies of the seven labelled
maximal blocks of the fixed 56-event carrier.  This is not a classification
of arbitrary finite OMLs or arbitrary completions.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "seven-block-subfamily-boundary-census-v1"
OMEGA = tuple(itertools.product(range(4), range(2), range(2)))
UNIV = frozenset(OMEGA)


def boolean_block(atoms):
    return {
        frozenset().union(*(atoms[i] for i in range(len(atoms)) if mask >> i & 1))
        for mask in range(1 << len(atoms))
    }


def generated(generators):
    out = {frozenset(), UNIV, *generators}
    while True:
        old = set(out)
        out |= {UNIV - x for x in old}
        out |= {x & y for x in old for y in old}
        if out == old:
            return out


def unique_extreme(carrier, x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    extrema = [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates
    )]
    return extrema[0] if len(extrema) == 1 else None


def maximal_cliques(vertices, adjacent):
    vertices = set(vertices)
    out = []

    def visit(r, p, x):
        if not p and not x:
            out.append(frozenset(r))
            return

        pivot = next(iter(p | x), None)
        neighbours = ({w for w in vertices if w != pivot and adjacent(pivot, w)}
                      if pivot is not None else set())
        for v in tuple(p - neighbours):
            vn = {w for w in vertices if w != v and adjacent(v, w)}
            visit(r | {v}, p & vn, x & vn)
            p.remove(v)
            x.add(v)

    visit(set(), set(vertices), set())
    return out


def labelled_blocks():
    base = [frozenset(w for w in OMEGA if w[0] == i) for i in range(4)]
    a = [
        frozenset(w for w in OMEGA if w[0] in side and w[1] == bit)
        for side in ({0, 1}, {2, 3}) for bit in range(2)
    ]
    c = [
        frozenset(w for w in OMEGA if w[0] in side and w[2] == bit)
        for side in ({0, 2}, {1, 3}) for bit in range(2)
    ]
    adec = ((base[0:2], a[0:2]), (base[2:4], a[2:4]))
    cdec = (((base[0], base[2]), c[0:2]), ((base[1], base[3]), c[2:4]))
    blocks = {}
    for x, y in itertools.product(range(2), repeat=2):
        blocks[f"A{x}{y}"] = boolean_block((*adec[0][x], *adec[1][y]))
        blocks[f"C{x}{y}"] = boolean_block((*cdec[0][x], *cdec[1][y]))
    del blocks["C00"]  # It equals A00.
    return blocks


def atom_list(block):
    return sorted(
        [x for x in block if x and not any(y < x for y in block if y)],
        key=lambda x: sorted(x),
    )


def analyse_family(chosen, all_blocks, include_states=False):
    carrier = set().union(*(all_blocks[name] for name in chosen))
    if not all(UNIV - x in carrier for x in carrier):
        return {"status": "not_concrete_logic"}
    if not all(x | y in carrier for x in carrier for y in carrier if x.isdisjoint(y)):
        return {"status": "not_concrete_logic"}

    meet = {(x, y): unique_extreme(carrier, x, y, False)
            for x in carrier for y in carrier}
    join = {(x, y): unique_extreme(carrier, x, y, True)
            for x in carrier for y in carrier}
    if any(z is None for z in (*meet.values(), *join.values())):
        return {"status": "not_lattice"}
    if not all(join[x, meet[y, UNIV - x]] == y
               for x in carrier for y in carrier if x <= y):
        return {"status": "not_orthomodular"}

    compatible = lambda x, y: join[meet[x, y], meet[x, UNIV - y]] == x
    max_blocks = maximal_cliques(carrier, compatible)
    named_max_blocks = {frozenset(all_blocks[name]): name for name in chosen}
    maximal_names = sorted(named_max_blocks[block] for block in max_blocks
                           if block in named_max_blocks)
    exact_named_classification = (
        len(max_blocks) == len(chosen) and set(maximal_names) == set(chosen)
    )
    centre = {x for x in carrier if all(compatible(x, y) for y in carrier)}
    boundaries = {
        name: generated(set().union(*(
            all_blocks[name] & all_blocks[other]
            for other in chosen if other != name
        )))
        for name in chosen
    }
    proper_names = sorted(name for name in chosen
                          if boundaries[name] < all_blocks[name])

    triangles = []
    for triangle in itertools.combinations(chosen, 3):
        blocks = [all_blocks[name] for name in triangle]
        interfaces = [blocks[i] & blocks[j] for i, j in ((0, 1), (0, 2), (1, 2))]
        closures = [
            generated((blocks[i] & blocks[j]) | (blocks[i] & blocks[k]))
            for i, j, k in ((0, 1, 2), (1, 0, 2), (2, 0, 1))
        ]
        if (all(len(x) > 2 for x in interfaces) and
                all(blocks[i] & blocks[j] != blocks[i] & blocks[k]
                    for i, j, k in ((0, 1, 2), (1, 0, 2), (2, 0, 1))) and
                all(closures[i] < blocks[i] for i in range(3))):
            triangles.append(list(triangle))

    result = {
        "status": "oml",
        "events": len(carrier),
        "maximal_block_count": len(max_blocks),
        "maximal_block_sizes": sorted(map(len, max_blocks)),
        "exact_named_maximal_block_classification": exact_named_classification,
        "centre_size": len(centre),
        "trivial_centre": centre == {frozenset(), UNIV},
        "boundary_sizes": {name: len(boundaries[name]) for name in chosen},
        "proper_boundary_blocks": proper_names,
        "proper_transverse_triangles": triangles,
    }
    if not include_states:
        return result

    atoms = {name: atom_list(all_blocks[name]) for name in chosen}
    coherent = []
    for values in itertools.product(range(4), repeat=len(chosen)):
        if all(
            all((atoms[chosen[i]][values[i]] <= event) ==
                (atoms[chosen[j]][values[j]] <= event)
                for event in all_blocks[chosen[i]] & all_blocks[chosen[j]])
            for i in range(len(chosen)) for j in range(i + 1, len(chosen))
        ):
            coherent.append(values)
    point_states = {
        tuple(next(i for i, atom in enumerate(atoms[name]) if point in atom)
              for name in chosen)
        for point in OMEGA
    }
    triangle_extensions = {}
    for triangle in triangles:
        positions = [chosen.index(name) for name in triangle]
        local = {
            values for values in itertools.product(range(4), repeat=3)
            if all(
                all((atoms[triangle[i]][values[i]] <= event) ==
                    (atoms[triangle[j]][values[j]] <= event)
                    for event in all_blocks[triangle[i]] & all_blocks[triangle[j]])
                for i in range(3) for j in range(i + 1, 3)
            )
        }
        restrictions = {tuple(values[i] for i in positions) for values in coherent}
        triangle_extensions["/".join(triangle)] = {
            "locally_coherent_two_valued_states": len(local),
            "globally_extendable_restrictions": len(restrictions),
            "every_local_state_extends": local == restrictions,
        }
    result["state_gates"] = {
        "global_two_valued_states": len(coherent),
        "distinct_point_evaluation_states": len(point_states),
        "all_global_states_are_point_evaluations": set(coherent) == point_states,
        "point_evaluations_order_separate": all(
            x <= y or any(point in x and point not in y for point in OMEGA)
            for x in carrier for y in carrier
        ),
        "phi_tame_by_finiteness": True,
        "sigma_essential_state": False,
        "transverse_triangle_extensions": triangle_extensions,
    }
    return result


def build():
    blocks = labelled_blocks()
    names = tuple(blocks)
    status_counts = {}
    survivors = []
    analyses = {}
    for mask in range(1, 1 << len(names)):
        chosen = tuple(names[i] for i in range(len(names)) if mask >> i & 1)
        result = analyse_family(chosen, blocks)
        status_counts[result["status"]] = status_counts.get(result["status"], 0) + 1
        if result["status"] == "oml":
            analyses[chosen] = result
            if (result["exact_named_maximal_block_classification"] and
                    result["trivial_centre"] and
                    result["proper_boundary_blocks"] and
                    result["proper_transverse_triangles"]):
                survivors.append(chosen)

    # `survivors` is in mask order, so ties retain the first labelled family.
    chosen = min(survivors, key=lambda family: analyses[family]["events"])
    chosen_result = analyse_family(chosen, blocks, include_states=True)
    return {
        "schema": SCHEMA,
        "scope": (
            "all 127 nonempty subfamilies of the seven labelled maximal blocks "
            "of one fixed 56-event OML; no arbitrary-completion classification"
        ),
        "census": {
            "labelled_blocks": list(names),
            "nonempty_subfamilies": (1 << len(names)) - 1,
            "status_counts": status_counts,
            "survivor_count": len(survivors),
            "survivor_families": [list(family) for family in survivors],
            "minimum_survivor_event_count": min(analyses[x]["events"] for x in survivors),
        },
        "selected_survivor": {"blocks": list(chosen), **chosen_result},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")
