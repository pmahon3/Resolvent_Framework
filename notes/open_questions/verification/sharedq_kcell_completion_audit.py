#!/usr/bin/env python3
"""k-cell shared-q paste of the 24-atom literal-H4 conditional cell: concrete
orthogonal closure, exhaustive finite audit, and k-scaling census.

Construction. k copies of the incompatible-H4 conditional cell (blocks below)
share ONLY the three H4 activation atoms a1,a2,a3 and the four-element
subalgebra {0,q,q',1}, where q = e11 v e10 is a rank-2 element of each copy's
private maximal coordinate block E_i = {e11,e10,e01,e00}@i.  All cascade atoms
and the private output r_i = e11@i v e01@i stay private.  The concrete carrier
is the state fibre product over the shared signature (a1,a2,a3,q); the raw
event family is the union of the k pulled-back 56-event cell families.  The
raw paste is audited for latticehood (first failing pair reported with ALL its
incomparable minimal upper bounds / maximal lower bounds); the canonical
orthogonal completion (least complement/disjoint-union-closed superfamily) is
then computed inside that representation and audited exhaustively: unique binary extrema,
orthomodular law, centre, q-commutant, lattice-level maximal blocks (clique
search over lattice compatibility, NOT declared-block cohabitation), per-copy
conditional relations, joint activated relation, joint (r_i,r_j) boundary
reconstruction, activation representability, off-cylinder escape, and the
k-scaling formulas
    events(k)  = 10 + 46k + 4k(k-1)      blocks(k) = 11k + k^2
    states(k)  = 2 * sum_abc n(abc)^k     rawbad(k) = 8k(k-1)
    closure rounds = [4k(k-1), 0]        (one substantive round, uniformly).

Abstract two-valued-state exhaustiveness: for k=1 ALL two-valued finitely
additive states on the 56-event family are enumerated event-level by
constraint backtracking (exactly 224 = the carrier points).  For k >= 2 the
receipt records the machine-checked premises of the restriction lemma
(every raw event is a cell event or shared; every added event is a disjoint
union of two cell events; every cell state extends to a carrier point), which
reduce abstract-state completeness to the k=1 census; the k=2 census can be
recomputed directly with --deep.

Usage:
  python3 sharedq_kcell_completion_audit.py --emit     # write receipts k=1,2,3
  python3 sharedq_kcell_completion_audit.py --verify   # recompute and compare
  python3 sharedq_kcell_completion_audit.py --k 2 [--deep]   # print one payload

stdlib only, deterministic.  Evidence class: exhaustive finite censuses at
k = 1,2,3 plus executable verification; NO finite-to-infinite promotion is
claimed anywhere in the receipts.
"""
import argparse
import hashlib
import json
import os
from itertools import combinations, product

SCHEMA = "sharedq-kcell-completion-v1"
EMIT_DATE = "2026-07-14"
HERE = os.path.dirname(os.path.abspath(__file__))

CELL_BLOCKS = (
    ("a1", "u1", "p11"), ("a2", "v1", "p12"), ("u1", "v1", "w1"),
    ("a3", "n1", "p15"), ("w1", "m1", "p14"), ("m1", "n1", "t1"),
    ("a3", "n2", "p25"), ("w1", "m2", "p24"), ("m2", "n2", "t2"),
    ("t1", "e10", "s1"), ("t2", "e01", "s2"),
    ("e11", "e10", "e01", "e00"),
)
SHARED = ("a1", "a2", "a3")
EXPECTED_CELL_STATES = 224


def cell_states():
    """All two-valued block states of the single cell, deterministic order."""
    out = set()
    for choice in product(*CELL_BLOCKS):
        s = frozenset(choice)
        if all(len(s & frozenset(b)) == 1 for b in CELL_BLOCKS):
            out.add(s)
    return sorted(out, key=lambda s: tuple(sorted(s)))


def signature(state):
    q = 1 if ("e11" in state or "e10" in state) else 0
    return tuple(int(a in state) for a in SHARED) + (q,)


def atom_name(base, cell):
    return base if base in SHARED else "%s@%d" % (base, cell)


def build_carrier(k, states):
    """Fibre product of k cell-state spaces over the shared signature."""
    by_sig = {}
    for i, s in enumerate(states):
        by_sig.setdefault(signature(s), []).append(i)
    points = []
    for sig in sorted(by_sig):
        for tup in product(by_sig[sig], repeat=k):
            points.append((sig, tup))
    return points


def build_atom_masks(k, states, points):
    """Bitmask over carrier points for every pasted atom."""
    names = []
    for base in sorted({a for b in CELL_BLOCKS for a in b}):
        if base in SHARED:
            names.append(base)
        else:
            names.extend(atom_name(base, c) for c in range(1, k + 1))
    names = sorted(set(names))
    buf = {n: bytearray((len(points) + 7) // 8) for n in names}
    for idx, (sig, tup) in enumerate(points):
        byte, bit = idx >> 3, 1 << (idx & 7)
        charged = set()
        for c, si in enumerate(tup, start=1):
            for base in states[si]:
                charged.add(atom_name(base, c))
        for n in charged:
            buf[n][byte] |= bit
    return {n: int.from_bytes(bytes(b), "little") for n, b in buf.items()}


def block_event_masks(k, atom_masks):
    """Raw pulled-back events: all subset-unions inside every declared block,
    tagged with canonical names (sorted atom decompositions)."""
    events = {0: "0"}
    blocks = []
    for c in range(1, k + 1):
        for b in CELL_BLOCKS:
            blocks.append(tuple(atom_name(a, c) for a in b))
    full = 0
    for n, m in atom_masks.items():
        full |= m
    events[full] = "1"
    for b in blocks:
        for r in range(1, len(b) + 1):
            for sub in combinations(b, r):
                m = 0
                for a in sub:
                    m |= atom_masks[a]
                if m not in events or len(events[m]) > len("+".join(sub)):
                    events.setdefault(m, "+".join(sorted(sub)))
    return events, blocks, full


def extrema_sets(evs, x, y, full):
    ubs = [z for z in evs if x | z == z and y | z == z]
    min_ubs = [z for z in ubs
               if not any(w != z and w | z == z for w in ubs)]
    lbs = [z for z in evs if z | x == x and z | y == y]
    max_lbs = [z for z in lbs
               if not any(w != z and z | w == w for w in lbs)]
    return min_ubs, max_lbs


def close_orthogonally(raw, full):
    events = set(raw)
    rounds = []
    while True:
        new = {full ^ x for x in events} - events
        snap = sorted(events)
        for i, x in enumerate(snap):
            for y in snap[i + 1:]:
                if not x & y:
                    u = x | y
                    if u not in events:
                        new.add(u)
        rounds.append(len(new))
        if not new:
            break
        events |= new
    return sorted(events), rounds


def enumerate_abstract_states(evs, full):
    """Event-level exhaustive census of two-valued finitely additive states:
    complement equations + additivity on every disjoint pair, backtracking."""
    n = len(evs)
    idx = {e: i for i, e in enumerate(evs)}
    comp_pairs = [(i, idx[full ^ e]) for i, e in enumerate(evs)]
    sum_triples = [(i, j, idx[evs[i] | evs[j]])
                   for i in range(n) for j in range(i + 1, n)
                   if not evs[i] & evs[j]]
    watch = [[] for _ in range(n)]
    for t, (i, j) in enumerate(comp_pairs):
        watch[i].append(("c", t))
        watch[j].append(("c", t))
    for t, (i, j, u) in enumerate(sum_triples):
        for z in (i, j, u):
            watch[z].append(("s", t))
    order = sorted(range(n), key=lambda i: (-len(watch[i]), i))
    val = {idx[0]: 0, idx[full]: 1}
    found = []

    def ok(i):
        for kind, t in watch[i]:
            if kind == "c":
                a, b = comp_pairs[t]
                if a in val and b in val and val[a] + val[b] != 1:
                    return False
            else:
                a, b, u = sum_triples[t]
                if a in val and b in val and u in val \
                        and val[a] + val[b] != val[u]:
                    return False
                if a in val and b in val and val[a] + val[b] > 1:
                    return False
        return True

    def bt(pos):
        while pos < n and order[pos] in val:
            pos += 1
        if pos == n:
            found.append(tuple(val[i] for i in range(n)))
            return
        i = order[pos]
        for v in (0, 1):
            val[i] = v
            if ok(i):
                bt(pos + 1)
        del val[i]

    bt(0)
    return found


def audit(k, deep=False):
    states = cell_states()
    assert len(states) == EXPECTED_CELL_STATES
    sig_counts = {}
    for s in states:
        sig_counts[signature(s)] = sig_counts.get(signature(s), 0) + 1
    points = build_carrier(k, states)
    npts = len(points)
    expected_points = sum(v ** k for v in sig_counts.values())
    atom_masks = build_atom_masks(k, states, points)
    events_named, blocks, full = block_event_masks(k, atom_masks)
    raw = sorted(events_named)
    name = dict(events_named)

    def nm(m):
        return name.get(m, "?")

    # ---- raw latticehood -------------------------------------------------
    raw_bad = []
    first_witness = None
    for i, x in enumerate(raw):
        for y in raw[i + 1:]:
            mubs, mlbs = extrema_sets(raw, x, y, full)
            if len(mubs) != 1 or len(mlbs) != 1:
                raw_bad.append((x, y))
                if first_witness is None:
                    first_witness = {
                        "x": nm(x), "y": nm(y),
                        "minimal_upper_bounds": sorted(nm(z) for z in mubs),
                        "maximal_lower_bounds": sorted(nm(z) for z in mlbs),
                    }

    # ---- concrete orthogonal closure in the fibre-product representation --
    evs, rounds = close_orthogonally(raw, full)
    added = [m for m in evs if m not in events_named]
    e_side = {"q1": ("e11", "e10"), "q0": ("e01", "e00")}
    added_decomp = []
    for m in added:
        hit = None
        for i in range(1, k + 1):
            for j in range(1, k + 1):
                if i == j:
                    continue
                for x in e_side["q1"]:
                    for y in e_side["q0"]:
                        if m == atom_masks[atom_name(x, i)] | \
                                atom_masks[atom_name(y, j)]:
                            hit = "%s+%s" % (atom_name(x, i), atom_name(y, j))
        added_decomp.append(hit)
        if hit:
            name[m] = hit
    repair_pair_local = all(h is not None for h in added_decomp)

    n = len(evs)
    idx = {e: i for i, e in enumerate(evs)}
    le_row = [0] * n            # bit j of le_row[i]: evs[i] <= evs[j]
    le_col = [0] * n
    for i, x in enumerate(evs):
        for j, y in enumerate(evs):
            if x | y == y:
                le_row[i] |= 1 << j
                le_col[j] |= 1 << i

    def bits(m):
        while m:
            b = m & -m
            yield b.bit_length() - 1
            m ^= b

    meet = [[None] * n for _ in range(n)]
    join = [[None] * n for _ in range(n)]
    unique_extrema = True
    for i in range(n):
        for j in range(i, n):
            lows = le_col[i] & le_col[j]
            tops = [t for t in bits(lows) if not (le_row[t] & lows & ~(1 << t))]
            ups = le_row[i] & le_row[j]
            bots = [t for t in bits(ups) if not (le_col[t] & ups & ~(1 << t))]
            if len(tops) != 1 or len(bots) != 1:
                unique_extrema = False
            else:
                meet[i][j] = meet[j][i] = tops[0]
                join[i][j] = join[j][i] = bots[0]
    comp = [idx[full ^ e] for e in evs]
    orthomodular = unique_extrema and all(
        join[i][meet[j][comp[i]]] == j
        for i in range(n) for j in range(n) if le_row[i] >> j & 1)

    def compatible(i, j):
        return join[meet[i][j]][meet[i][comp[j]]] == i

    com = [[compatible(i, j) for j in range(n)] for i in range(n)]
    centre = [nm(evs[i]) for i in range(n) if all(com[i])]
    qmask = atom_masks[atom_name("e11", 1)] | atom_masks[atom_name("e10", 1)]
    qi = idx[qmask]
    q_commutant = sum(com[qi])

    # ---- lattice-level maximal blocks (atom cliques + Boolean check) -----
    atom_events = sorted(m for m in atom_masks.values())
    a_idx = [idx[m] for m in atom_events]
    a_com = {(p, r) for p in a_idx for r in a_idx if com[p][r]}
    cliques = []

    def bk(R, P, X):
        if not P and not X:
            cliques.append(sorted(R))
            return
        for v in sorted(P):
            bk(R | {v}, {w for w in P if (v, w) in a_com and w != v},
               {w for w in X if (v, w) in a_com and w != v})
            P = P - {v}
            X = X | {v}
    bk(set(), set(a_idx), set())
    block_ok = True
    block_sizes = []
    mixed_blocks = []
    for c in cliques:
        masks = [evs[i] for i in c]
        for r in range(len(masks) + 1):
            for sub in combinations(masks, r):
                u = 0
                for m in sub:
                    u |= m
                if u not in idx:
                    block_ok = False
        block_sizes.append(2 ** len(masks))
        cells = {nm(evs[i]).split("@")[1] for i in c if "@" in nm(evs[i])}
        if len(cells) > 1:
            mixed_blocks.append(sorted(nm(evs[i]) for i in c))

    # ---- states ----------------------------------------------------------
    profiles = set()
    for p in range(npts):
        profiles.add(tuple((evs[i] >> p) & 1 for i in range(n)))
    points_injective = len(profiles) == npts
    abstract_state_count = None
    if k == 1 or deep:
        abstract_state_count = len(enumerate_abstract_states(evs, full))
    every_raw_is_cell_or_shared = all(
        "+" not in v or len({t.split("@")[1] for t in v.split("+")
                             if "@" in t}) <= 1
        for m, v in events_named.items())
    every_added_disjoint_union_of_two_raw_events = all(
        any(not x & y and x | y == m for x in raw for y in raw)
        for m in added)
    point_index = set(points)
    every_cell_state_has_repeated_fibre_extension = all(
        (signature(states[i]), tuple([i] * k)) in point_index
        for i in range(len(states)))

    # ---- relations -------------------------------------------------------
    act = atom_masks["a1"] & atom_masks["a2"] & atom_masks["a3"]
    act_points = bin(act).count("1")
    off = full & ~act
    projections = {}
    for c in range(1, k + 1):
        r_c = atom_masks[atom_name("e11", c)] | atom_masks[atom_name("e01", c)]
        fib = {}
        for p in range(npts):
            key = "".join(str((m >> p) & 1) for m in
                          (atom_masks["a1"], atom_masks["a2"],
                           atom_masks["a3"], qmask, r_c))
            fib[key] = fib.get(key, 0) + 1
        projections["cell%d" % c] = {
            "contains_11100": fib.get("11100", 0) > 0,
            "contains_11111": fib.get("11111", 0) > 0,
            "excludes_11101": fib.get("11101", 0) == 0,
            "excludes_11110": fib.get("11110", 0) == 0,
            "off_111_all_four_qr_profiles": all(
                fib.get("%d%d%d%d%d" % (x, y, z, u, v), 0) > 0
                for x, y, z in product((0, 1), repeat=3)
                if (x, y, z) != (1, 1, 1) for u, v in product((0, 1), repeat=2)),
        }
        if c == 1:
            projections["cell1"]["fiber_counts"] = {
                kk: fib[kk] for kk in sorted(fib)}
    r_masks = {c: atom_masks[atom_name("e11", c)] |
               atom_masks[atom_name("e01", c)] for c in range(1, k + 1)}
    joint = sorted({"".join(str((m >> p) & 1)
                            for m in [qmask] + [r_masks[c]
                                                for c in range(1, k + 1)])
                    for p in bits(act)})
    boundary = {}
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            ri, rj = r_masks[i], r_masks[j]
            key = "r%d,r%d" % (i, j)
            boundary[key] = {
                "intersection_is_event": (ri & rj) in idx,
                "equalizer_is_event": ((ri & rj) | (full & ~ri & ~rj)) in idx,
                "compatible": com[idx[ri]][idx[rj]],
                "some_maximal_block_contains_both": any(
                    all(any(evs[a] | m == m and True for a in c1) or True
                        for m in ())  # placeholder, replaced below
                    for c1 in ()),
            }
            in_block = False
            for c in cliques:
                masks = [evs[t] for t in c]
                span_i = any(u == ri for r0 in range(len(masks) + 1)
                             for sub in combinations(masks, r0)
                             for u in [sum_or(sub)])
                span_j = any(u == rj for r0 in range(len(masks) + 1)
                             for sub in combinations(masks, r0)
                             for u in [sum_or(sub)])
                if span_i and span_j:
                    in_block = True
            boundary[key]["some_maximal_block_contains_both"] = in_block
            four_atoms = [ri & rj, ri & (full ^ rj),
                          (full ^ ri) & rj, (full ^ ri) & (full ^ rj)]
            cylinders = set()
            for take in range(16):
                u = 0
                for a, atom in enumerate(four_atoms):
                    if take >> a & 1:
                        u |= atom
                if u in idx:
                    cylinders.add(u)
            boundary[key]["represented_joint_boolean_cylinder_count"] = len(cylinders)
            boundary[key]["only_marginal_joint_cylinders_represented"] = cylinders == {
                0, full, ri, full ^ ri, rj, full ^ rj}

    payload = {
        "schema": SCHEMA,
        "k": k,
        "shared_structure": "H4 activation atoms a1,a2,a3 and the four-element"
                            " subalgebra {0,q,q',1}; private coordinate blocks"
                            " E_i and outputs r_i = e11@i v e01@i",
        "carrier_points": npts,
        "carrier_points_formula_2_sum_n_pow_k": expected_points,
        "cell_states": len(states),
        "raw_events": len(raw),
        "raw_events_formula_10_plus_46k": 10 + 46 * k,
        "raw_is_lattice": not raw_bad,
        "raw_bad_unordered_pairs": len(raw_bad),
        "raw_bad_formula_8k_kminus1": 8 * k * (k - 1),
        "raw_first_failure": first_witness,
        "closure_added_by_round": rounds,
        "closure_added_formula_4k_kminus1": 4 * k * (k - 1),
        "closure_stabilizes_in_one_substantive_round": len(
            [r for r in rounds if r]) <= 1,
        "repair_pair_local_qside_x_qprimeside": repair_pair_local,
        "added_events": sorted(h for h in added_decomp if h),
        "completed_events": n,
        "completed_events_formula": 10 + 46 * k + 4 * k * (k - 1),
        "completed_unique_binary_extrema": unique_extrema,
        "completed_complement_closed": all(full ^ e in idx for e in evs),
        "completed_disjoint_union_closed": all(
            (x | y) in idx for x in evs for y in evs if not x & y),
        "completed_orthomodular": orthomodular,
        "centre": centre,
        "q_is_central": nm(qmask) in centre or qi in
        [i for i in range(n) if all(com[i])],
        "q_commutant_size": q_commutant,
        "maximal_block_count": len(cliques),
        "maximal_block_count_formula_11k_plus_k2": 11 * k + k * k,
        "maximal_block_event_sizes": sorted(block_sizes),
        "maximal_blocks_all_boolean_complete": block_ok,
        "mixed_private_coordinate_blocks": len(mixed_blocks),
        "mixed_private_coordinate_blocks_formula_k_kminus1": k * (k - 1),
        "mixed_block_examples": mixed_blocks[:2],
        "point_profiles_injective": points_injective,
        "point_evaluations_order_separate": all(
            x & (full ^ y) for x in evs for y in evs if x | y != y),
        "abstract_two_valued_state_count": abstract_state_count,
        "abstract_states_equal_points": (
            abstract_state_count == npts if abstract_state_count is not None
            else None),
        "state_completeness_reduction_premises": {
            "every_raw_event_is_single_cell_or_shared":
                every_raw_is_cell_or_shared,
            "every_added_event_disjoint_union_of_two_raw_events":
                every_added_disjoint_union_of_two_raw_events,
            "every_cell_state_has_repeated_fibre_extension":
                every_cell_state_has_repeated_fibre_extension,
        },
        "activation_cylinder_points": act_points,
        "activation_is_event": act in idx,
        "nonzero_events_inside_activation": sum(
            1 for e in evs if e and e | act == act),
        "every_nonzero_event_has_off_cylinder_point": all(
            e & off for e in evs if e),
        "projections": projections,
        "joint_activated_relation_q_r1_to_rk": joint,
        "joint_relation_is_diagonal": joint == ["0" * (k + 1), "1" * (k + 1)],
        "joint_output_boundaries": boundary,
    }
    return payload


def sum_or(masks):
    u = 0
    for m in masks:
        u |= m
    return u


def canonical(payload):
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def receipt_path(k):
    return os.path.join(HERE, "sharedq_kcell_completion_k%d.json" % k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--k", type=int)
    ap.add_argument("--deep", action="store_true")
    args = ap.parse_args()
    if args.k:
        print(json.dumps(audit(args.k, deep=args.deep), indent=1,
                         sort_keys=True))
        return
    ks = (1, 2, 3)
    if args.emit:
        for k in ks:
            payload = audit(k)
            receipt = {
                "schema": SCHEMA, "emitted": EMIT_DATE,
                "generator": os.path.basename(__file__),
                "payload_sha256": hashlib.sha256(canonical(payload)).hexdigest(),
                "payload": payload,
            }
            with open(receipt_path(k), "w") as f:
                json.dump(receipt, f, indent=1, sort_keys=True)
                f.write("\n")
            print("wrote", receipt_path(k))
    if args.verify or not args.emit:
        ok = True
        for k in ks:
            with open(receipt_path(k)) as f:
                receipt = json.load(f)
            payload = json.loads(canonical(audit(k)).decode())
            stored = receipt["payload"]
            sha = hashlib.sha256(canonical(stored)).hexdigest()
            if sha != receipt["payload_sha256"]:
                print("CORRUPT ", receipt_path(k))
                ok = False
            elif payload != stored:
                diff = [kk for kk in set(payload) | set(stored)
                        if payload.get(kk) != stored.get(kk)]
                print("MISMATCH", receipt_path(k), sorted(diff))
                ok = False
            else:
                print("MATCH   k=%d payload_sha256=%s..." % (k, sha[:16]))
        print("VERIFY:", "PASS" if ok else "FAIL")
        raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
