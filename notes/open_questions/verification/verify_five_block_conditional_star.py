#!/usr/bin/env python3
"""Independent verification of the k-cell conditional-diagonal star receipts.

Second implementation, deliberately different code paths from the
producer: rebuilds the universe and raw atlas from the declared
construction using frozensets of points (not integer masks), recomputes
the canonical orthogonal completion by a set-based fixpoint, and
independently rechecks against each receipt:

  - point / raw-event / completed-event counts and closure stabilization;
  - existence of the raw disjoint-union failure (first forced mixed cut);
  - the count of joint two-coordinate splits inside lift(b2);
  - absence of nontrivial central events among all completed events,
    probed by Foulis commutation against the coordinate events, the
    joint region, lift(b2), and a slice of raw events, with meets
    recomputed set-theoretically (largest event inside the intersection);
  - the point-state census (distinct point profiles = state count in the
    receipt, which separately certifies all states are point states);
  - the joint-charged coordinate relation, computed directly from point
    profiles without any clique or gluing machinery.

Receipts verified: five_block_conditional_star_k{1,2,3}.json and the
k=2 joint-hub control five_block_conditional_star_k2joint.json (for the
joint-hub control the centre probe is skipped for runtime; the producer
computes the exact centre there).
"""

import itertools
import json
import pathlib
import sys

SCHEMA = "five-block-conditional-diagonal-star-v1"


def build_sets(k, joint_hub=False):
    W = [(w0, w1, w2) for w0 in range(4) for w1 in range(2)
         for w2 in range(2)]
    b = [frozenset(w for w in W if w[0] == j) for j in range(4)]
    q, r = b[0] | b[1], b[0] | b[2]
    a = [frozenset(w for w in W if w[0] in s and w[1] == t)
         for s in ({0, 1}, {2, 3}) for t in range(2)]
    c = [frozenset(w for w in W if w[0] in s and w[2] == t)
         for s in ({0, 2}, {1, 3}) for t in range(2)]
    pts = []
    for w in W:
        if w in b[0]:
            pts += [(w, v, (v,) * k) for v in range(2)]
        elif w in b[1]:
            pts += [(w, v, (None,) * k) for v in range(2)]
        elif w in b[2]:
            pts += [(w, None, ys) for ys in
                    itertools.product(range(2), repeat=k)]
        else:
            pts.append((w, None, (None,) * k))
    U = frozenset(pts)

    def atoms(base_atoms, sq, sr, i, full_tuple=False):
        out = []
        for atom in base_atoms:
            groups = {}
            for p in U:
                if p[0] in atom:
                    if full_tuple:
                        key = (p[1] if atom <= q else None,
                               p[2] if atom <= r else None)
                    else:
                        key = (p[1] if sq and atom <= q else None,
                               p[2][i] if sr and atom <= r else None)
                    groups.setdefault(key, set()).add(p)
            out += [frozenset(g) for g in groups.values()]
        return out

    block_atoms = [atoms([b[0], b[1], a[2], a[3]], 1, 0, 0),
                   atoms([a[0], a[1], b[2], b[3]], 1, 0, 0),
                   atoms([a[0], a[1], a[2], a[3]], 1, 0, 0)]
    for i in range(k):
        block_atoms.append(atoms([b[0], b[1], b[2], b[3]], 1, 1, i))
        block_atoms.append(atoms([b[0], b[2], c[2], c[3]], 0, 1, i))
    if joint_hub:
        block_atoms.append(
            atoms([b[0], b[1], b[2], b[3]], 1, 1, 0, full_tuple=True))
    events = set()
    for ats in block_atoms:
        for n in range(1 << len(ats)):
            events.add(frozenset().union(
                *(ats[j] for j in range(len(ats)) if n >> j & 1)))
    return U, events


def verify(k, expect, joint_hub=False, centre_probe=True):
    U, carrier = build_sets(k, joint_hub=joint_hub)
    raw = len(carrier)
    raw_events = list(carrier)
    fail = any(x.isdisjoint(y) and (x | y) not in carrier
               for x, y in itertools.combinations(raw_events, 2))
    while True:
        old = set(carrier)
        carrier |= {U - x for x in carrier}
        ev = list(carrier)
        carrier |= {x | y for i, x in enumerate(ev)
                    for y in ev[i:] if x.isdisjoint(y)}
        if carrier == old:
            break
    ok = {"points": len(U) == expect["points"],
          "raw": raw == expect["raw_events"],
          "raw_disjoint_union_failure_exists": fail,
          "completed": len(carrier) == expect["events"]}

    b2 = frozenset(p for p in U if p[0][0] == 2)
    joint_count = 0
    for e in carrier:
        if not e or not e <= b2:
            continue
        deps = set()
        for w in {p[0] for p in e}:
            fib = {p[2] for p in e if p[0] == w}
            allfib = {p[2] for p in b2 if p[0] == w}
            if fib < allfib:
                for i in range(k):
                    if len({t[i] for t in fib}) == 1:
                        deps.add(i)
        if len(deps) >= 2:
            joint_count += 1
    ok["joint_split_count"] = joint_count == expect["joint_split_count"]

    def meet(x, y):
        cut = x & y
        best = frozenset()
        for e in carrier:
            if e <= cut and len(e) > len(best):
                best = e
        return best

    def join(x, y):
        return U - meet(U - x, U - y)

    def commutes(x, y):
        return join(meet(x, y), meet(x, U - y)) == x

    coords = [frozenset(p for p in U if p[0][0] in (0, 1) and p[1] == 0)]
    coords += [frozenset(p for p in U if p[0][0] in (0, 2)
                         and p[2][i] == 0) for i in range(k)]
    jreg = frozenset(p for p in U if p[0][0] == 0)
    if centre_probe:
        probes = list(coords) + [jreg, b2]
        ok["no_nontrivial_centre_probe"] = all(
            (z in (frozenset(), U)) or not all(
                commutes(z, e) for e in probes + raw_events[:40])
            for z in carrier)

    profiles = {}
    for p in U:
        profiles.setdefault(
            frozenset(e for e in carrier if p in e), []).append(p)
    ok["distinct_point_profiles"] = len(profiles) == expect["states"]
    crel = sorted({tuple(int(p in cd) for cd in coords)
                   for p in U if p in jreg})
    diag = [tuple([0] * (k + 1)), tuple([1] * (k + 1))]
    ok["joint_charged_relation_diagonal"] = crel == diag
    return ok


def main():
    base = pathlib.Path(__file__).parent
    targets = [("five_block_conditional_star_k1.json", 1, False, True),
               ("five_block_conditional_star_k2.json", 2, False, True),
               ("five_block_conditional_star_k3.json", 3, False, True),
               ("five_block_conditional_star_k2joint.json", 2, True, False)]
    allok = True
    for name, k, jh, cp in targets:
        exp = json.load(open(base / name))
        assert exp["schema"] == SCHEMA, name
        assert exp.get("joint_hub", False) == jh, name
        expect = {"points": exp["points"],
                  "raw_events": exp["raw_events"],
                  "events": exp["events"],
                  "joint_split_count": exp["joint_split_count"],
                  "states": exp["states"]["count"]}
        ok = verify(k, expect, joint_hub=jh, centre_probe=cp)
        print(f"{name}: " + json.dumps(ok))
        allok &= all(ok.values())
    print("ALL OK" if allok else "MISMATCH", file=sys.stderr)
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
