#!/usr/bin/env python3
"""Exhaustive audit of two literal-H4 conditional cells pasted over H4.

The single cell is specified by its 12 atom blocks.  We enumerate all cell
states, construct its canonical concrete representation, generate the shared
sublogic <a1,a2,a3,q>, form the exact state-fibre product of two copies, and
take the concrete orthogonal closure of the raw event union under complements
and disjoint unions. Every executable structural, fibre-point-state,
interface, relation, escape, and maximal-block claim in the receipt is then
recomputed. Completeness of the fibre points among all abstract two-valued
states is separately hand proved and is not claimed as an exhaustive check.

Evidence class: exhaustive finite evidence plus executable verification.
"""

import argparse
import json
from itertools import product
from pathlib import Path

import networkx as nx


BLOCKS = (
    ('a1', 'u1', 'p11'), ('a2', 'v1', 'p12'), ('u1', 'v1', 'w1'),
    ('a3', 'n1', 'p15'), ('w1', 'm1', 'p14'), ('m1', 'n1', 't1'),
    ('a3', 'n2', 'p25'), ('w1', 'm2', 'p24'), ('m2', 'n2', 't2'),
    ('e11', 'e10', 'e01', 'e00'), ('t1', 'e10', 's1'),
    ('t2', 'e01', 's2'),
)


def subset(x, y):
    return x <= y if isinstance(x, frozenset) else x & ~y == 0


def extrema(events, x, y, lower):
    if lower:
        candidates = [z for z in events if subset(z, x) and subset(z, y)]
    else:
        candidates = [z for z in events if subset(x, z) and subset(y, z)]
    return [z for z in candidates if not any(
        z != w and (subset(z, w) if lower else subset(w, z))
        for w in candidates)]


def compute():
    atoms_names = sorted(set().union(*map(set, BLOCKS)))
    states = set()
    for choices in product(*BLOCKS):
        state = frozenset(choices)
        if all(len(state & set(block)) == 1 for block in BLOCKS):
            states.add(state)
    states = sorted(states, key=lambda s: sorted(s))
    cell_top = frozenset(range(len(states)))
    atoms = {a: frozenset(i for i, s in enumerate(states) if a in s)
             for a in atoms_names}
    cell_events = {frozenset(), cell_top}
    for block in BLOCKS:
        for flags in product((0, 1), repeat=len(block)):
            cell_events.add(frozenset().union(*(
                atoms[a] for a, flag in zip(block, flags) if flag)))
    cell_events = tuple(cell_events)
    cell_meet = {(x, y): extrema(cell_events, x, y, True)[0]
                 for x in cell_events for y in cell_events}
    cell_join = {(x, y): extrema(cell_events, x, y, False)[0]
                 for x in cell_events for y in cell_events}

    q = atoms['e11'] | atoms['e10']
    interface = {frozenset(), cell_top, atoms['a1'], atoms['a2'],
                 atoms['a3'], q}
    while True:
        enlarged = (interface | {cell_top - x for x in interface} |
                    {cell_meet[x, y] for x in interface for y in interface} |
                    {cell_join[x, y] for x in interface for y in interface})
        if enlarged == interface:
            break
        interface = enlarged

    ordered_interface = sorted(interface, key=lambda x: (len(x), sorted(x)))
    fibres = {}
    for i in range(len(states)):
        signature = tuple(i in x for x in ordered_interface)
        fibres.setdefault(signature, []).append(i)
    points = [(i, j) for fibre in fibres.values() for i in fibre for j in fibre]
    top = (1 << len(points)) - 1
    left = {x: sum(1 << k for k, (i, _) in enumerate(points) if i in x)
            for x in cell_events}
    right = {x: sum(1 << k for k, (_, j) in enumerate(points) if j in x)
             for x in cell_events}
    raw = set(left.values()) | set(right.values())

    raw_bad_ordered = 0
    for x in raw:
        for y in raw:
            if (len(extrema(raw, x, y, True)) != 1 or
                    len(extrema(raw, x, y, False)) != 1):
                raw_bad_ordered += 1

    events = set(raw)
    closure_additions = []
    while True:
        enlarged = (events | {top ^ x for x in events} |
                    {x | y for x in events for y in events if not x & y})
        closure_additions.append(len(enlarged) - len(events))
        if enlarged == events:
            break
        events = enlarged

    meet, join, bad = {}, {}, []
    for x in events:
        for y in events:
            glb = extrema(events, x, y, True)
            lub = extrema(events, x, y, False)
            if len(glb) != 1 or len(lub) != 1:
                bad.append((x, y))
            else:
                meet[x, y], join[x, y] = glb[0], lub[0]
    assert not bad
    orthomodular = all(
        join[x, meet[y, top ^ x]] == y
        for x in events for y in events if subset(x, y))

    def compatible(x, y):
        return join[meet[x, y], meet[x, top ^ y]] == x

    centre = {x for x in events if all(compatible(x, y) for y in events)}
    graph = nx.Graph()
    graph.add_nodes_from(events)
    event_list = list(events)
    graph.add_edges_from(
        (x, y) for i, x in enumerate(event_list) for y in event_list[i + 1:]
        if compatible(x, y))
    maximal_blocks = list(nx.find_cliques(graph))

    a = [left[atoms[z]] for z in ('a1', 'a2', 'a3')]
    q_lift = left[q]
    r1 = left[atoms['e11'] | atoms['e01']]
    r2 = right[atoms['e11'] | atoms['e01']]
    profiles = {tuple(int((event >> k) & 1)
                      for event in (*a, q_lift, r1, r2))
                for k in range(len(points))}
    activated = {p for p in profiles if p[:3] == (1, 1, 1)}
    activation = a[0] & a[1] & a[2]

    point_evaluations_order_separate = all(
        bool(x & ~y) for x in events for y in events if not subset(x, y))
    point_evaluations_additive = all(
        x | y in events for x in events for y in events if not x & y)
    result = {
        'schema': 'h4-fixed-interface-two-cell-paste-v1',
        'single_cell_atoms': len(atoms),
        'single_cell_blocks': len(BLOCKS),
        'single_cell_events': len(cell_events),
        'single_cell_states': len(states),
        'interface_events': len(interface),
        'interface_state_characters': len(fibres),
        'interface_fibre_sizes': sorted(len(f) for f in fibres.values()),
        'state_fibre_product_points': len(points),
        'raw_events': len(raw),
        'raw_bad_ordered_pairs': raw_bad_ordered,
        'raw_bad_unordered_pairs': raw_bad_ordered // 2,
        'orthogonal_closure_additions_by_round': closure_additions,
        'completed_events': len(events),
        'completed_unique_binary_extrema': not bad,
        'completed_complement_closed': all(top ^ x in events for x in events),
        'completed_disjoint_union_closed': all(
            x | y in events for x in events for y in events if not x & y),
        'completed_orthomodular': orthomodular,
        'completed_centre_size': len(centre),
        'maximal_block_count': len(maximal_blocks),
        'maximal_block_event_sizes': sorted(len(block) for block in maximal_blocks),
        'private_outputs_distinct': r1 != r2,
        'projected_profile_count': len(profiles),
        'activated_profiles': sorted(''.join(map(str, p)) for p in activated),
        'activation_support_is_event': activation in events,
        'nonzero_events_inside_activation': sum(
            bool(x) and subset(x, activation) for x in events),
        'every_nonzero_event_has_off_activation_point': all(
            x & (top ^ activation) for x in events if x),
        'fibre_point_evaluation_count': len(points),
        'fibre_point_evaluations_two_valued_additive': point_evaluations_additive,
        'fibre_point_evaluations_order_separate': point_evaluations_order_separate,
        'abstract_state_completeness': 'hand-proved-outside-executable-verifier',
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--receipt', type=Path)
    args = parser.parse_args()
    result = compute()
    if args.verify:
        receipt = Path(__file__).with_name('h4_fixed_interface_paste_receipt.json')
        expected = json.loads(receipt.read_text())
        assert result == expected, json.dumps(
            {'computed': result, 'receipt': expected}, indent=2, sort_keys=True)
    rendered = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        args.receipt.write_text(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
