#!/usr/bin/env python3
"""Independent verifier for the sharedq_kcell_completion receipts (k = 1,2,3).

Recomputes the receipts' structural claims from the definition with plain
declarative code that shares nothing with the producer beyond the block
presentation: cell states are enumerated by depth-first block choice (not
product filtering), the carrier is rebuilt as the literal fibre product over
the shared (a1,a2,a3,q) signature, events are subset-unions inside declared
blocks, the orthogonal closure is recomputed by a naive sweep, and every
lattice/orthomodularity/centre/block/relation/escape claim is re-derived with
straightforward O(n^3) scans.  The k=1 abstract two-valued state census is
recomputed by an independent event-level backtracker.  Finally the k=2
receipt is cross-checked against the concurrent two-cell audit
h4_fixed_interface_paste_receipt.json on every overlapping field.

Usage: python3 verify_sharedq_kcell_completion.py        (exit 0 iff all pass)
stdlib only, deterministic.
"""
import hashlib
import json
import os
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
CELL_BLOCKS = (
    ("a1", "u1", "p11"), ("a2", "v1", "p12"), ("u1", "v1", "w1"),
    ("a3", "n1", "p15"), ("w1", "m1", "p14"), ("m1", "n1", "t1"),
    ("a3", "n2", "p25"), ("w1", "m2", "p24"), ("m2", "n2", "t2"),
    ("t1", "e10", "s1"), ("t2", "e01", "s2"),
    ("e11", "e10", "e01", "e00"),
)
SHARED = ("a1", "a2", "a3")
FAILURES = []


def check(label, got, want):
    if got != want:
        FAILURES.append((label, got, want))
        print("FAIL  %s: got %r want %r" % (label, got, want))


def cell_states_dfs():
    """Cell states by depth-first block choice with propagation."""
    val = {}
    out = []

    def dfs(bi):
        if bi == len(CELL_BLOCKS):
            out.append(frozenset(a for a, v in val.items() if v))
            return
        blk = CELL_BLOCKS[bi]
        ones = [a for a in blk if val.get(a) == 1]
        if len(ones) > 1:
            return
        cands = ones if ones else [a for a in blk if val.get(a) is None]
        for c in cands:
            touched = []
            ok = True
            if val.get(c) is None:
                val[c] = 1
                touched.append(c)
            for a in blk:
                if a == c:
                    continue
                if val.get(a) == 1:
                    ok = False
                    break
                if val.get(a) is None:
                    val[a] = 0
                    touched.append(a)
            if ok:
                dfs(bi + 1)
            for a in touched:
                del val[a]

    dfs(0)
    return sorted(set(out), key=lambda s: tuple(sorted(s)))


def name(base, c):
    return base if base in SHARED else "%s@%d" % (base, c)


def build(k):
    states = cell_states_dfs()
    sig = [tuple(int(a in s) for a in SHARED) +
           (1 if ("e11" in s or "e10" in s) else 0,) for s in states]
    by_sig = {}
    for i, sg in enumerate(sig):
        by_sig.setdefault(sg, []).append(i)
    points = [(sg, tup) for sg in sorted(by_sig)
              for tup in product(by_sig[sg], repeat=k)]
    npts = len(points)
    masks = {}
    for c in range(1, k + 1):
        for base in sorted({a for b in CELL_BLOCKS for a in b}):
            masks.setdefault(name(base, c), 0)
    for pi, (sg, tup) in enumerate(points):
        for c, si in enumerate(tup, start=1):
            for base in states[si]:
                masks[name(base, c)] |= 1 << pi
    full = (1 << npts) - 1
    raw = {0: "0", full: "1"}
    for c in range(1, k + 1):
        for b in CELL_BLOCKS:
            named = [name(a, c) for a in b]
            for r in range(1, len(named) + 1):
                for sub in combinations(named, r):
                    m = 0
                    for a in sub:
                        m |= masks[a]
                    raw.setdefault(m, "+".join(sorted(sub)))
    return states, points, masks, full, raw


def sub(x, y):
    return x | y == y


def extrema(evs, x, y):
    ubs = [z for z in evs if sub(x, z) and sub(y, z)]
    mubs = [z for z in ubs if not any(w != z and sub(w, z) for w in ubs)]
    lbs = [z for z in evs if sub(z, x) and sub(z, y)]
    mlbs = [z for z in lbs if not any(w != z and sub(z, w) for w in lbs)]
    return mubs, mlbs


def census_abstract(evs, full):
    n = len(evs)
    order = sorted(range(n), key=lambda i: bin(evs[i]).count("1"))
    idx = {e: i for i, e in enumerate(evs)}
    val = {idx[0]: 0, idx[full]: 1}
    count = [0]
    pairs = [(i, j, idx[evs[i] | evs[j]]) for i in range(n)
             for j in range(i + 1, n) if not evs[i] & evs[j]]
    comp = [(i, idx[full ^ evs[i]]) for i in range(n)]

    def consistent():
        for i, j in comp:
            if i in val and j in val and val[i] + val[j] != 1:
                return False
        for i, j, u in pairs:
            if i in val and j in val:
                if val[i] + val[j] > 1:
                    return False
                if u in val and val[i] + val[j] != val[u]:
                    return False
        return True

    def bt(pos):
        while pos < n and order[pos] in val:
            pos += 1
        if pos == n:
            count[0] += 1
            return
        i = order[pos]
        for v in (0, 1):
            val[i] = v
            if consistent():
                bt(pos + 1)
        del val[i]

    bt(0)
    return count[0]


def verify_k(k, payload):
    states, points, masks, full, raw = build(k)
    tag = "k=%d" % k
    check(tag + " cell_states", payload["cell_states"], len(states))
    check(tag + " carrier_points", payload["carrier_points"], len(points))
    check(tag + " raw_events", payload["raw_events"], len(raw))
    evs = sorted(raw)
    bad = []
    witness = None
    for i, x in enumerate(evs):
        for y in evs[i + 1:]:
            mubs, mlbs = extrema(evs, x, y)
            if len(mubs) != 1 or len(mlbs) != 1:
                bad.append((x, y))
                if witness is None:
                    witness = {
                        "x": raw[x], "y": raw[y],
                        "minimal_upper_bounds": sorted(raw[z] for z in mubs),
                        "maximal_lower_bounds": sorted(raw[z] for z in mlbs)}
    check(tag + " raw_is_lattice", payload["raw_is_lattice"], not bad)
    check(tag + " raw_bad_unordered_pairs",
          payload["raw_bad_unordered_pairs"], len(bad))
    check(tag + " raw_first_failure", payload["raw_first_failure"], witness)

    events = set(evs)
    rounds = []
    while True:
        add = {full ^ x for x in events}
        for x in events:
            for y in events:
                if x < y and not x & y:
                    add.add(x | y)
        add -= events
        rounds.append(len(add))
        if not add:
            break
        events |= add
    check(tag + " closure_added_by_round",
          payload["closure_added_by_round"], rounds)
    check(tag + " completed_events", payload["completed_events"], len(events))
    evc = sorted(events)
    n = len(evc)
    idx = {e: i for i, e in enumerate(evc)}
    meets, joins = {}, {}
    unique = True
    for i, x in enumerate(evc):
        for y in evc[i:]:
            mubs, mlbs = extrema(evc, x, y)
            if len(mubs) != 1 or len(mlbs) != 1:
                unique = False
            else:
                joins[x, y] = joins[y, x] = mubs[0]
                meets[x, y] = meets[y, x] = mlbs[0]
    check(tag + " completed_unique_binary_extrema",
          payload["completed_unique_binary_extrema"], unique)
    om = unique and all(
        joins[x, meets[y, full ^ x]] == y
        for x in evc for y in evc if sub(x, y))
    check(tag + " completed_orthomodular", payload["completed_orthomodular"], om)

    def com(x, y):
        return joins[meets[x, y], meets[x, full ^ y]] == x

    centre = sorted(raw.get(x, "?") for x in evc
                    if all(com(x, y) for y in evc))
    check(tag + " centre", payload["centre"], centre)
    q = masks["e11@1"] | masks["e10@1"]
    check(tag + " q_is_central", payload["q_is_central"],
          all(com(q, y) for y in evc))
    check(tag + " q_commutant_size", payload["q_commutant_size"],
          sum(1 for y in evc if com(q, y)))

    atoms = sorted(set(masks.values()))
    cliques = []

    def bk(r, p, x):
        if not p and not x:
            cliques.append(sorted(r))
            return
        for v in sorted(p):
            bk(r | {v}, {w for w in p if w != v and com(v, w)},
               {w for w in x if w != v and com(v, w)})
            p = p - {v}
            x = x | {v}

    bk(set(), set(atoms), set())
    check(tag + " maximal_block_count",
          payload["maximal_block_count"], len(cliques))
    check(tag + " maximal_block_event_sizes",
          payload["maximal_block_event_sizes"],
          sorted(2 ** len(c) for c in cliques))
    inv = {m: nm for nm, m in masks.items()}
    mixed = [c for c in cliques
             if len({inv[m].split("@")[1] for m in c if "@" in inv[m]}) > 1]
    check(tag + " mixed_private_coordinate_blocks",
          payload["mixed_private_coordinate_blocks"], len(mixed))

    act = masks["a1"] & masks["a2"] & masks["a3"]
    check(tag + " activation_cylinder_points",
          payload["activation_cylinder_points"], bin(act).count("1"))
    check(tag + " activation_is_event",
          payload["activation_is_event"], act in events)
    check(tag + " nonzero_events_inside_activation",
          payload["nonzero_events_inside_activation"],
          sum(1 for e in evc if e and sub(e, act)))
    check(tag + " every_nonzero_event_has_off_cylinder_point",
          payload["every_nonzero_event_has_off_cylinder_point"],
          all(e & (full & ~act) for e in evc if e))

    rms = {c: masks["e11@%d" % c] | masks["e01@%d" % c]
           for c in range(1, k + 1)}
    joint = sorted({
        "".join(str(int(bool(m & (1 << pi)))) for m in
                [q] + [rms[c] for c in range(1, k + 1)])
        for pi in range(len(points)) if act & (1 << pi)})
    check(tag + " joint_activated_relation",
          payload["joint_activated_relation_q_r1_to_rk"], joint)
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            key = "r%d,r%d" % (i, j)
            b = payload["joint_output_boundaries"][key]
            check(tag + " %s intersection_is_event" % key,
                  b["intersection_is_event"], (rms[i] & rms[j]) in events)
            check(tag + " %s equalizer_is_event" % key,
                  b["equalizer_is_event"],
                  ((rms[i] & rms[j]) | (full & ~rms[i] & ~rms[j])) in events)
            check(tag + " %s compatible" % key,
                  b["compatible"], com(rms[i], rms[j]))

    for c in range(1, k + 1):
        pr = payload["projections"]["cell%d" % c]
        fib = {}
        for pi, (sg, tup) in enumerate(points):
            rv = 1 if ("e11" in states[tup[c - 1]] or
                       "e01" in states[tup[c - 1]]) else 0
            kk = "%d%d%d%d%d" % (sg + (rv,))
            fib[kk] = fib.get(kk, 0) + 1
        check(tag + " cell%d contains_11100" % c,
              pr["contains_11100"], fib.get("11100", 0) > 0)
        check(tag + " cell%d contains_11111" % c,
              pr["contains_11111"], fib.get("11111", 0) > 0)
        check(tag + " cell%d excludes_11101" % c,
              pr["excludes_11101"], fib.get("11101", 0) == 0)
        check(tag + " cell%d excludes_11110" % c,
              pr["excludes_11110"], fib.get("11110", 0) == 0)
        off_ok = all(fib.get("%d%d%d%d%d" % (x, y, z, u, v), 0) > 0
                     for x, y, z in product((0, 1), repeat=3)
                     if (x, y, z) != (1, 1, 1)
                     for u, v in product((0, 1), repeat=2))
        check(tag + " cell%d off_111_all_four" % c,
              pr["off_111_all_four_qr_profiles"], off_ok)
        if "fiber_counts" in pr:
            check(tag + " cell%d fiber_counts" % c, pr["fiber_counts"], fib)

    if k == 1:
        check(tag + " abstract_two_valued_state_count",
              payload["abstract_two_valued_state_count"],
              census_abstract(evc, full))


def main():
    payloads = {}
    for k in (1, 2, 3):
        path = os.path.join(HERE, "sharedq_kcell_completion_k%d.json" % k)
        with open(path) as f:
            receipt = json.load(f)
        blob = json.dumps(receipt["payload"], sort_keys=True,
                          separators=(",", ":")).encode()
        check("k=%d payload_sha256" % k,
              hashlib.sha256(blob).hexdigest(), receipt["payload_sha256"])
        payloads[k] = receipt["payload"]
        verify_k(k, receipt["payload"])

    cross = os.path.join(HERE, "h4_fixed_interface_paste_receipt.json")
    if os.path.exists(cross):
        with open(cross) as f:
            other = json.load(f)
        mine = payloads[2]
        check("cross completed_events",
              other["completed_events"], mine["completed_events"])
        check("cross carrier_points",
              other["state_fibre_product_points"], mine["carrier_points"])
        check("cross closure rounds",
              other["closure_additions_by_round"][:1] if
              "closure_additions_by_round" in other else
              other.get("orthogonal_closure_additions_by_round", [None])[:1],
              mine["closure_added_by_round"][:1])
        check("cross raw_bad_unordered",
              other["raw_bad_unordered_pairs"],
              mine["raw_bad_unordered_pairs"])
        check("cross centre size", other["completed_centre_size"],
              len(mine["centre"]))
        check("cross orthomodular", other["completed_orthomodular"],
              mine["completed_orthomodular"])
        check("cross block sizes", other["maximal_block_event_sizes"],
              mine["maximal_block_event_sizes"])
        check("cross activation event", other["activation_support_is_event"],
              mine["activation_is_event"])
        check("cross escape",
              other["every_nonzero_event_has_off_activation_point"],
              mine["every_nonzero_event_has_off_cylinder_point"])
        check("cross diagonal",
              sorted(other["activated_profiles"]) == ["111000", "111111"],
              mine["joint_relation_is_diagonal"])
    else:
        print("NOTE: cross receipt not present, skipped")

    print("PASS" if not FAILURES else "FAIL (%d)" % len(FAILURES))
    raise SystemExit(0 if not FAILURES else 1)


if __name__ == "__main__":
    main()
