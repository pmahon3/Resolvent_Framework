#!/usr/bin/env python3
"""k-cell conditional-diagonal star over the certified 16-point base.

Campaign 11 producer. Generalizes the Campaign-10 diagonal cell
(`five_block_nonatomic_diagonal_completion_audit.py`); at k=1 it must
reproduce that cell's certified receipts exactly: 28 points, 264 raw
events, completion 264->392, nine maximal blocks (4x128, 5x64), trivial
centre, 20 states all point states, raw obstruction 0x55/0xa0a with
missing union 0xa5f, joint-charged relation diagonal.  This calibration
is the correctness anchor for k>=2.

Architecture for k cells:
  hub blocks A01, A10, A11 see the hub coordinate x on q = b0|b1;
  cell i contributes A00_i (sees x and y_i) and C01_i (sees y_i),
  with y_i supported on r = b0|b2 and the conditional diagonal
  x = y_i imposed pointwise on the joint region b0 = q meet r.
  On b2 the k cells carry a free product fibre {0,1}^k of which each
  cell block sees only its own y_i quotient (distributed nonseparating
  quotient copies of the b2 boundary; the copies are pairwise meet-zero
  and non-orthogonal in the completion).

The --joint-hub flag adds one control block HJOINT that sees x together
with the full (y_1,...,y_k) product on b2: the "reconstructed faithful
boundary" comparison.  At k=2 this absorbs both cells' A00 blocks into
one maximal container and regenerates the full product algebra on b2.

Audited per run: raw counts and first forced mixed cut, canonical
orthogonal completion rounds, unique binary extrema, orthomodularity,
centre, exact Bron--Kerbosch maximal-block census with per-block b0/b2
fibre partitions, joint two-coordinate splits inside lift(b2), the
compatible-ultrafilter state census, and the full and joint-charged
coordinate relations.
"""

import argparse
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

SCHEMA = "five-block-conditional-diagonal-star-v1"


def build(k, joint_hub=False):
    W = [(w0, w1, w2) for w0 in range(4) for w1 in range(2) for w2 in range(2)]
    breg = [frozenset(w for w in W if w[0] == j) for j in range(4)]
    q = breg[0] | breg[1]
    r = breg[0] | breg[2]
    a_atoms = [frozenset(w for w in W if w[0] in side and w[1] == bit)
               for side in ({0, 1}, {2, 3}) for bit in range(2)]
    c_atoms = [frozenset(w for w in W if w[0] in side and w[2] == bit)
               for side in ({0, 2}, {1, 3}) for bit in range(2)]
    a0, a1, a2, a3 = a_atoms
    c0, c1, c2, c3 = c_atoms

    points = []
    for w in W:
        if w in breg[0]:
            for v in range(2):
                points.append((w, v, (v,) * k))
        elif w in breg[1]:
            for v in range(2):
                points.append((w, v, (None,) * k))
        elif w in breg[2]:
            for ys in itertools.product(range(2), repeat=k):
                points.append((w, None, ys))
        else:
            points.append((w, None, (None,) * k))
    universe = sorted(points, key=repr)
    index = {p: i for i, p in enumerate(universe)}
    full = (1 << len(universe)) - 1

    def block_from_atoms(base_atoms, sees_q, sees_r, cell):
        atom_masks = []
        for atom in base_atoms:
            groups = {}
            for p in universe:
                if p[0] not in atom:
                    continue
                key = (p[1] if sees_q and atom <= q else None,
                       p[2][cell] if sees_r and atom <= r else None)
                groups.setdefault(key, 0)
                groups[key] |= 1 << index[p]
            atom_masks.extend(groups.values())
        block = set()
        for sel in range(1 << len(atom_masks)):
            m = 0
            for j, am in enumerate(atom_masks):
                if sel >> j & 1:
                    m |= am
            block.add(m)
        return frozenset(block)

    blocks = {}
    blocks["A01"] = block_from_atoms([breg[0], breg[1], a2, a3], True, False, 0)
    blocks["A10"] = block_from_atoms([a0, a1, breg[2], breg[3]], True, False, 0)
    blocks["A11"] = block_from_atoms([a0, a1, a2, a3], True, False, 0)
    for i in range(k):
        blocks[f"A00_{i}"] = block_from_atoms(
            [breg[0], breg[1], breg[2], breg[3]], True, True, i)
        blocks[f"C01_{i}"] = block_from_atoms(
            [breg[0], breg[2], c2, c3], False, True, i)
    if joint_hub:
        atom_masks = []
        for atom in [breg[0], breg[1], breg[2], breg[3]]:
            groups = {}
            for p in universe:
                if p[0] not in atom:
                    continue
                key = (p[1] if atom <= q else None,
                       p[2] if atom <= r else None)
                groups.setdefault(key, 0)
                groups[key] |= 1 << index[p]
            atom_masks.extend(groups.values())
        block = set()
        for sel in range(1 << len(atom_masks)):
            m = 0
            for j, am in enumerate(atom_masks):
                if sel >> j & 1:
                    m |= am
            block.add(m)
        blocks["HJOINT"] = frozenset(block)
    return universe, index, full, blocks, breg, q, r


def audit(k, do_states=True, verbose=True, joint_hub=False):
    t0 = time.time()
    universe, index, full, blocks, breg, q, r = build(k, joint_hub=joint_hub)
    names = sorted(blocks)
    carrier = set().union(*blocks.values())
    raw_events = sorted(carrier)
    raw_count = len(raw_events)

    def signature(m):
        return [n for n in names if m in blocks[n]]

    first_fail = None
    for x, y in itertools.combinations(raw_events, 2):
        if not x & y and (x | y) not in carrier:
            first_fail = {
                "left_mask": hex(x), "right_mask": hex(y),
                "union_mask": hex(x | y),
                "left_signature": signature(x),
                "right_signature": signature(y),
                "cardinalities": [bin(x).count("1"), bin(y).count("1")]}
            break

    rounds = [len(carrier)]
    while True:
        old = set(carrier)
        carrier |= {full ^ x for x in carrier}
        events = sorted(carrier)
        carrier |= {x | y for i, x in enumerate(events)
                    for y in events[i:] if not x & y}
        rounds.append(len(carrier))
        if carrier == old:
            break
        if len(carrier) > 200000:
            raise RuntimeError("carrier blow-up")

    events = sorted(carrier)
    E = len(events)
    if verbose:
        print(f"[k={k}] closure {rounds} ({time.time()-t0:.1f}s)",
              file=sys.stderr, flush=True)
    descending = sorted(carrier, key=lambda x: (-bin(x).count("1"), x))
    meet_cache = {}

    def meet(x, y):
        cut = x & y
        got = meet_cache.get(cut)
        if got is None:
            if cut in carrier:
                got = cut
            else:
                lows = [e for e in descending if not e & ~cut]
                got = lows[0]
                for e in lows[1:]:
                    if e & ~got:
                        raise RuntimeError(
                            f"non-unique meet at cut {hex(cut)}")
            meet_cache[cut] = got
        return got

    def join(x, y):
        return full ^ meet(full ^ x, full ^ y)

    def commutes(x, y):
        return join(meet(x, y), meet(x, full ^ y)) == x

    for x in events:
        for y in events:
            meet(x, y)
    if verbose:
        print(f"[k={k}] meets done, {len(meet_cache)} cuts "
              f"({time.time()-t0:.1f}s)", file=sys.stderr, flush=True)
    orthomodular = all(join(x, meet(y, full ^ x)) == y
                       for x in events for y in events if not x & ~y)
    centre = [x for x in events if all(commutes(x, y) for y in events)]
    if verbose:
        print(f"[k={k}] OML+centre done ({time.time()-t0:.1f}s)",
              file=sys.stderr, flush=True)

    vertices = [x for x in events if x not in (0, full)]
    neighbours = []
    for i, x in enumerate(vertices):
        m = 0
        for j, y in enumerate(vertices):
            if i != j and commutes(x, y):
                m |= 1 << j
        neighbours.append(m)
    if verbose:
        print(f"[k={k}] adjacency done ({time.time()-t0:.1f}s)",
              file=sys.stderr, flush=True)
    cliques = []

    def bron_kerbosch(current, possible, excluded):
        if not possible and not excluded:
            cliques.append(frozenset({0, full,
                                      *(vertices[i] for i in current)}))
            return
        union = possible | excluded
        indices = []
        rest = union
        while rest:
            bit = rest & -rest
            indices.append(bit.bit_length() - 1)
            rest -= bit
        pivot = max(indices,
                    key=lambda i: bin(possible & neighbours[i]).count("1"))
        candidates = possible & ~neighbours[pivot]
        while candidates:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            bron_kerbosch(current + (v,), possible & neighbours[v],
                          excluded & neighbours[v])
            possible -= bit
            excluded |= bit
            candidates -= bit

    sys.setrecursionlimit(100000)
    bron_kerbosch((), (1 << len(vertices)) - 1, 0)
    cliques.sort(key=lambda c: (-len(c), tuple(sorted(c))))
    if verbose:
        print(f"[k={k}] {len(cliques)} maximal blocks "
              f"({time.time()-t0:.1f}s)", file=sys.stderr, flush=True)

    named_masks = {n: frozenset(blocks[n]) for n in names}
    clique_records = []
    b2mask = sum(1 << index[p] for p in universe if p[0][0] == 2)
    b0mask = sum(1 << index[p] for p in universe if p[0][0] == 0)

    def fibre_partition(clique, region_mask, coord):
        atoms = [e for e in clique if e and not any(
            f and f != e and not f & ~e for f in clique)]
        shapes = set()
        for am in atoms:
            cut = am & region_mask
            if not cut:
                continue
            per_base = {}
            for p in universe:
                if (1 << index[p]) & cut:
                    key = p[0]
                    per_base.setdefault(key, set()).add(
                        p[1] if coord == "x" else p[2])
            for s in per_base.values():
                shapes.add(tuple(sorted(map(str, s))))
        return sorted(shapes)

    for number, clique in enumerate(cliques):
        enc = "\n".join(map(hex, sorted(clique)))
        clique_records.append({
            "id": number, "size": len(clique),
            "sha256": hashlib.sha256(enc.encode()).hexdigest()[:16],
            "contains_named_blocks": [n for n in names
                                      if named_masks[n] <= clique],
            "b2_fibre_shapes": fibre_partition(clique, b2mask, "y"),
            "b0_fibre_shapes": fibre_partition(clique, b0mask, "y"),
        })
    named_containers = {
        n: [rec["id"] for rec, cl in zip(clique_records, cliques)
            if named_masks[n] <= cl] for n in names}

    # joint-split reconstruction audit: events contained in lift(b2)
    # whose trace pins two or more distinct cell coordinates
    joint_split_events = []
    for e in events:
        cut = e & b2mask
        if not cut or cut != e:
            continue
        deps = set()
        for w0base in {p[0] for p in universe if p[0][0] == 2}:
            fib = [p[2] for p in universe
                   if p[0] == w0base and (1 << index[p]) & e]
            if not fib or len(fib) == 2 ** k:
                continue
            for i in range(k):
                vals = {t[i] for t in fib}
                if len(vals) == 1:
                    deps.add(i)
        if len(deps) >= 2:
            joint_split_events.append(hex(e))

    result = {
        "schema": SCHEMA,
        "k": k, "joint_hub": joint_hub,
        "points": len(universe),
        "raw_events": raw_count,
        "first_disjoint_union_failure": first_fail,
        "closure_rounds": rounds,
        "events": E,
        "distinct_cuts": len(meet_cache),
        "orthomodular": orthomodular,
        "centre": [hex(x) for x in centre],
        "trivial_centre": centre == [0, full],
        "maximal_blocks": len(cliques),
        "maximal_block_sizes": sorted((len(c) for c in cliques),
                                      reverse=True),
        "named_block_containers": named_containers,
        "clique_records": clique_records,
        "events_inside_b2": sum(1 for e in events
                                if e and not e & ~b2mask),
        "joint_split_events_in_b2": joint_split_events,
        "joint_split_count": len(joint_split_events),
        "elapsed_construction_s": round(time.time() - t0, 1),
    }

    if do_states:
        atoms = [[e for e in clique if e and not any(
            f and f != e and not f & ~e for f in clique)]
            for clique in cliques]
        order = sorted(range(len(cliques)), key=lambda i: len(atoms[i]))
        selected = {}
        state_fingerprints = set()

        def choice_compatible(i, atom):
            for j, other in selected.items():
                for event in cliques[i] & cliques[j]:
                    if (not atom & ~event) != (not other & ~event):
                        return False
            return True

        def enumerate_states(depth):
            if depth == len(order):
                fp = 0
                for en, event in enumerate(events):
                    for i, atom in selected.items():
                        if event in cliques[i]:
                            if not atom & ~event:
                                fp |= 1 << en
                            break
                state_fingerprints.add(fp)
                return
            i = order[depth]
            for atom in atoms[i]:
                if choice_compatible(i, atom):
                    selected[i] = atom
                    enumerate_states(depth + 1)
                    del selected[i]

        enumerate_states(0)
        point_fps = {sum(1 << en for en, event in enumerate(events)
                         if event >> pt & 1)
                     for pt in range(len(universe))}
        q0 = sum(1 << index[p] for p in universe
                 if p[0][0] in (0, 1) and p[1] == 0)
        r0 = [sum(1 << index[p] for p in universe
                  if p[0][0] in (0, 2) and p[2][i] == 0) for i in range(k)]
        joint = sum(1 << index[p] for p in universe if p[0][0] == 0)
        assert q0 in carrier and joint in carrier
        assert all(m in carrier for m in r0)
        qi = events.index(q0)
        ris = [events.index(m) for m in r0]
        ji = events.index(joint)
        rel = sorted({tuple([s >> qi & 1] + [s >> i & 1 for i in ris])
                      for s in state_fingerprints})
        crel = sorted({tuple([s >> qi & 1] + [s >> i & 1 for i in ris])
                       for s in state_fingerprints if s >> ji & 1})
        pairwise = {}
        for i in range(k):
            pairwise[f"x_y{i}_joint"] = sorted(
                {(s >> qi & 1, s >> ris[i] & 1)
                 for s in state_fingerprints if s >> ji & 1})
        for i in range(k):
            for j in range(i + 1, k):
                pairwise[f"y{i}_y{j}_joint"] = sorted(
                    {(s >> ris[i] & 1, s >> ris[j] & 1)
                     for s in state_fingerprints if s >> ji & 1})
        result["states"] = {
            "count": len(state_fingerprints),
            "distinct_point_profiles": len(point_fps),
            "all_states_are_point_states":
                state_fingerprints == point_fps,
            "full_relation_x_y1_yk": rel,
            "joint_charged_relation_x_y1_yk": crel,
            "pairwise_joint_charged": pairwise,
        }
        result["elapsed_total_s"] = round(time.time() - t0, 1)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=1)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--no-states", action="store_true")
    ap.add_argument("--joint-hub", action="store_true")
    args = ap.parse_args()
    res = audit(args.k, do_states=not args.no_states,
                joint_hub=args.joint_hub)
    text = json.dumps(res, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
