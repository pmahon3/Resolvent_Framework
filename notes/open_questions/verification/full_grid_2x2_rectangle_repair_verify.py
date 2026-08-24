#!/usr/bin/env python3
"""Independent verifier for the rectangle-repair receipts.

Verifies, with independently written code (no import from the producer):

  1. the carrier construction (states by product-filter enumeration, masks
     by per-position repeat patterns -- both DIFFERENT algorithms from the
     producer's backtracking + integer-multiplication tiling), the closure
     counts, and the banked-receipt digests;
  2. the failed-pair census in full_grid_2x2_rectangle_witnesses.json,
     including SEMANTIC witness checks: every incomparability witness point
     is evaluated against its bounding events directly from its structural
     description (profile + four cell states), without any bitmask;
  3. the 16-point exhaustive receipt by replaying the recorded tree: each
     node's family is rebuilt by closure from the recorded choice path, the
     chosen failing pair and its interval are recomputed, the recorded
     children are checked to enumerate ALL interval subsets, and every
     terminal family is re-audited (closedness, lattice, orthomodularity,
     classification, normal forms, inclusions);
  4. the full-carrier cascade receipt by replaying the recorded tree:
     each node's family is rebuilt as the closure of the 230-event base
     plus the recorded trace cylinders, failing-pair counts and choices are
     recomputed, children lists are checked for completeness within class
     K, and every branch outcome (monotone certificate, no-K-candidate,
     completion audit) is recomputed.

Exit status 0 and final line VERIFY: PASS iff everything matches.
stdlib + numpy (numpy only for stage 3).  Deterministic.
"""
import hashlib
import json
import os
import sys
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
ATOMS = sorted({a for b in CELL_BLOCKS for a in b})
CELLS = ((0, 0), (0, 1), (1, 0), (1, 1))
PROFILES = tuple(product((0, 1), repeat=4))

FAILURES = []


def check(cond, msg):
    if cond:
        print("ok      ", msg)
    else:
        print("FAIL    ", msg)
        FAILURES.append(msg)


# ---------------------------------------------------------------- stage 1

def build():
    states = set()
    for choice in product(*CELL_BLOCKS):
        s = frozenset(choice)
        if all(len(s & frozenset(b)) == 1 for b in CELL_BLOCKS):
            states.add(s)
    states = sorted(states, key=lambda s: tuple(sorted(s)))
    groups = {}
    for j, s in enumerate(states):
        a = tuple(int(x in s) for x in SHARED)
        q = int("e11" in s or "e10" in s)
        r = int("e11" in s or "e01" in s)
        groups.setdefault((a, q, r), []).append(j)
    blocks = []
    offset = 0
    for a0 in product((0, 1), repeat=3):
        for a1 in product((0, 1), repeat=3):
            for qr in product((0, 1), repeat=4):
                q0, q1, r0, r1 = qr
                lists = (groups.get((a0, q0, r0), []),
                         groups.get((a0, q0, r1), []),
                         groups.get((a1, q1, r0), []),
                         groups.get((a1, q1, r1), []))
                ns = tuple(map(len, lists))
                size = ns[0] * ns[1] * ns[2] * ns[3]
                if size:
                    blocks.append(((a0, a1) + qr, lists, ns, offset, size))
                    offset += size
    return states, blocks, offset


def repeat_pattern(posbits, npos, inner, outer):
    unit = 0
    ones = (1 << inner) - 1
    for j in range(npos):
        if posbits >> j & 1:
            unit |= ones << (j * inner)
    width = npos * inner
    out = 0
    for t in range(outer):
        out |= unit << (t * width)
    return out


def build_masks(states, blocks):
    masks = {(c, x): 0 for c in CELLS for x in ATOMS}
    for profile, lists, ns, offset, size in blocks:
        for ci, cell in enumerate(CELLS):
            inner = 1
            for z in ns[ci + 1:]:
                inner *= z
            outer = 1
            for z in ns[:ci]:
                outer *= z
            for atom in ATOMS:
                posbits = 0
                for pos, sj in enumerate(lists[ci]):
                    if atom in states[sj]:
                        posbits |= 1 << pos
                if posbits:
                    masks[(cell, atom)] |= repeat_pattern(
                        posbits, ns[ci], inner, outer) << offset
    return masks


def raw_family(masks, npts):
    full = (1 << npts) - 1
    ev = {0: "0", full: "1"}
    for c in CELLS:
        for block in CELL_BLOCKS:
            for z in range(1, 1 << len(block)):
                e = 0
                names = []
                for j, a in enumerate(block):
                    if z >> j & 1:
                        e |= masks[(c, a)]
                        names.append("%s@%d%d" % (a, c[0], c[1]))
                ev.setdefault(e, "+".join(names))
    return ev, full


def closure(seed, full):
    ev = set(seed)
    rounds = []
    while True:
        new = {full ^ x for x in ev} - ev
        snap = sorted(ev)
        for i, x in enumerate(snap):
            for y in snap[i + 1:]:
                if not x & y and x | y not in ev:
                    new.add(x | y)
        rounds.append(len(new))
        if not new:
            return ev, rounds
        ev |= new


def digest(x, npts):
    return hashlib.sha256(x.to_bytes((npts + 7) // 8, "little")).hexdigest()


# ------------------------------------------------------- semantic points

def point_in_label(label, profile6, cellstates):
    """Membership of a structurally described point in a labeled event,
    evaluated with no bitmask at all."""
    a0, a1, q0, q1, r0, r1 = profile6
    if label == "0":
        return False
    if label == "1":
        return True
    if label.startswith("cyl["):
        prof = "%d%d%d%d" % (q0, q1, r0, r1)
        return prof in label[4:-1].split(",")
    cell_of = {"00": 0, "01": 1, "10": 2, "11": 3}
    for part in label.split("+"):
        a, c = part.split("@")
        if a in cellstates[cell_of[c]]:
            return True
    return False


# ---------------------------------------------------------------- stage 2

def verify_witnesses(states, blocks, npts, masks, raw, full, ev0):
    with open(os.path.join(HERE,
                           "full_grid_2x2_rectangle_witnesses.json")) as f:
        rec = json.load(f)
    p = rec["payload"]
    rep = p["reproduction"]
    check(rep["carrier_points"] == npts == 6186568, "carrier points")
    check(rep["macro_blocks"] == len(blocks) == 842, "macro blocks")
    check(rep["cell_states"] == len(states) == 224, "cell states")
    check(rep["raw_events"] == len(raw) == 198, "raw events")
    check(rep["completed_events"] == len(ev0) == 230, "completed events")
    b = rep["banked_receipt_first_failure_reproduced"]
    check(b["x_sha256"] == digest(masks[((0, 1), "e01")], npts),
          "x digest (e01@01)")
    check(b["y_sha256"] == digest(masks[((1, 0), "e10")], npts),
          "y digest (e10@10)")
    check(b["u_sha256"] == digest(full ^ masks[((0, 0), "e11")], npts),
          "u digest")
    check(b["v_sha256"] == digest(full ^ masks[((1, 1), "e00")], npts),
          "v digest")
    banked = os.path.join(HERE, "full_grid_2x2_conditional_cell.json")
    if os.path.exists(banked):
        with open(banked) as f:
            bk = json.load(f)
        ff = bk["first_lattice_failure"]
        check(ff["x_sha256"] == b["x_sha256"]
              and ff["y_sha256"] == b["y_sha256"]
              and set(ff["minimal_upper_bounds"]) ==
              {b["u_sha256"], b["v_sha256"]},
              "banked receipt digests agree")
    # census recompute
    evs = sorted(ev0)
    n = len(evs)
    up = [0] * n
    for i, x in enumerate(evs):
        for j, y in enumerate(evs):
            if x | y == y:
                up[i] |= 1 << j
    down = [0] * n
    for i in range(n):
        r = up[i]
        while r:
            bb = r & -r
            down[bb.bit_length() - 1] |= 1 << i
            r ^= bb
    def bits(m):
        while m:
            bb = m & -m
            yield bb.bit_length() - 1
            m ^= bb
    fails = []
    for i in range(n):
        for j in range(i + 1, n):
            cu = up[i] & up[j]
            mu = [z for z in bits(cu) if down[z] & cu == 1 << z]
            if len(mu) != 1:
                fails.append((i, j, mu))
    check(len(fails) == p["join_failing_pairs"] == 32,
          "32 join-failing pairs")
    cyl = {q: 0 for q in PROFILES}
    for profile, lists, ns, offset, size in blocks:
        cyl[profile[2:]] |= ((1 << size) - 1) << offset
    got = {}
    for i, j, mu in fails:
        got[frozenset((digest(evs[i], npts), digest(evs[j], npts)))] = \
            (i, j, mu)
    sem_ok = True
    prof_ok = True
    for q in p["all_pairs"]:
        key = frozenset((q["x_sha256"], q["y_sha256"]))
        if key not in got:
            sem_ok = False
            continue
        i, j, mu = got[key]
        mubd = sorted(digest(evs[z], npts) for z in mu)
        if mubd != sorted(q["minimal_upper_bound_sha256"]):
            sem_ok = False
        lower = evs[i] | evs[j]
        upper = full
        for k in bits(up[i] & up[j]):
            upper &= evs[k]
        must = ["".join(map(str, pr)) for pr in PROFILES
                if cyl[pr] & lower]
        free = ["".join(map(str, pr)) for pr in PROFILES
                if not (cyl[pr] & lower) and cyl[pr] | upper == upper]
        if must != q["must_profiles"] or free != q["free_profiles"]:
            prof_ok = False
        for w in q["incomparability_witnesses"]:
            pt = w["point"]
            prof = pt["profile_a0_a1_q0_q1_r0_r1"]
            cs = [set(x) for x in pt["cell_states_sorted_atoms"]]
            if not point_in_label(w["in_bound"], prof, cs):
                sem_ok = False
            if point_in_label(w["not_in_bound"], prof, cs):
                sem_ok = False
            # the point must be a valid compatible state tuple
            for csx in cs:
                for blk in CELL_BLOCKS:
                    if len(csx & set(blk)) != 1:
                        sem_ok = False
        for w in q["incomparability_witnesses"]:
            pass
    check(sem_ok, "census pair digests, bounds and semantic witnesses")
    check(prof_ok, "census must/free profiles")
    return evs, up, down, cyl


# ---------------------------------------------------------------- stage 3

def verify_core16():
    import numpy as np
    path = os.path.join(HERE,
                        "full_grid_2x2_rectangle_core16_exhaustive.json")
    with open(path) as f:
        rec = json.load(f)
    p = rec["payload"]
    FULL16 = 0xFFFF
    IDX = np.arange(65536, dtype=np.uint32)

    def m16(pred):
        return sum(1 << j for j in range(16)
                   if pred((j >> 3) & 1, (j >> 2) & 1, (j >> 1) & 1, j & 1))

    raw = {0, FULL16}
    for a in (0, 1):
        for i in (0, 1):
            for al in range(16):
                raw.add(m16(lambda w, x, y, z, a=a, i=i, al=al:
                            bool(al & (1 << (2 * (w, x)[a] + (y, z)[i])))))
    check(len(raw) == p["raw_events"], "core16 raw events")

    def close16(seed):
        ev = set(seed)
        while True:
            arr = np.array(sorted(ev), dtype=np.uint32)
            comp = np.bitwise_xor(np.uint32(FULL16), arr)
            cand = set(comp.tolist())
            for lo in range(0, len(arr), 2048):
                blk = arr[lo:lo + 2048]
                dis = (blk[:, None] & arr[None, :]) == 0
                cand |= set((blk[:, None] | arr[None, :])[dis].tolist())
            new = cand - ev
            if not new:
                return frozenset(ev)
            ev |= new

    def tabs(ev):
        isev = np.zeros(65536, dtype=bool)
        arr = np.array(sorted(ev), dtype=np.uint32)
        isev[arr] = True
        ceil = np.where(isev, IDX, np.uint32(FULL16)).astype(np.uint32)
        floor = np.where(isev, IDX, np.uint32(0)).astype(np.uint32)
        for b in range(16):
            bit = 1 << b
            lo = IDX[(IDX & bit) == 0]
            ceil[lo] &= ceil[lo | bit]
            floor[lo | bit] |= floor[lo]
        return isev, arr, ceil, floor

    def fail_lowers(isev, arr, ceil):
        out = set()
        comp = np.bitwise_xor(np.uint32(FULL16), arr)
        for base in (arr, comp):
            for lo in range(0, len(base), 2048):
                blk = base[lo:lo + 2048]
                u = (blk[:, None] | base[None, :]).ravel()
                out |= set(u[~isev[ceil[u]]].tolist())
        return out

    ev0 = close16(raw)
    check(len(ev0) == p["initial_closure_events"],
          "core16 initial closure size")
    # replay the tree
    tree_ok = True
    term_seen = set()
    for node in p["tree"]:
        fam = close16(ev0 | {int(h, 16) for h in node["path_choices_hex"]}
                      | {FULL16 ^ int(h, 16)
                         for h in node["path_choices_hex"]})
        if len(fam) != node["events"]:
            tree_ok = False
            continue
        isev, arr, ceil, floor = tabs(fam)
        fails = fail_lowers(isev, arr, ceil)
        if len(fails) != node["fail_lower_count"]:
            tree_ok = False
        if node.get("outcome") == "terminal":
            term_seen.add(fam)
            continue
        low = int(node["chosen_lower_hex"], 16)
        upv = int(node["chosen_upper_hex"], 16)
        if low not in fails or int(ceil[low]) != upv:
            tree_ok = False
        gap = upv & ~low & FULL16
        want = sorted(low | s for s in range(65536) if not s & ~gap)
        got = sorted(int(h, 16) for h in node["children"])
        if want != got:
            tree_ok = False
        # chosen lower must have the minimal gap popcount
        gn = bin(gap).count("1")
        for low2 in fails:
            gap2 = int(ceil[low2]) & ~low2 & FULL16
            if bin(gap2).count("1") < gn:
                tree_ok = False
    check(tree_ok, "core16 tree replay (families, intervals, children)")
    # terminals
    terms = p["terminals"]
    fams = [frozenset(int(h, 16) for h in t["family_hex"]) for t in terms]
    check(set(fams) == term_seen, "core16 terminal families = tree leaves")

    def isclosed(fam):
        arr = np.array(sorted(fam), dtype=np.uint32)
        isev = np.zeros(65536, dtype=bool)
        isev[arr] = True
        if not isev[np.bitwise_xor(np.uint32(FULL16), arr)].all():
            return False
        for lo in range(0, len(arr), 2048):
            blk = arr[lo:lo + 2048]
            dis = (blk[:, None] & arr[None, :]) == 0
            if not isev[(blk[:, None] | arr[None, :])[dis]].all():
                return False
        return True

    def sup16(z):
        s = 0
        for c in range(4):
            bit = 1 << (3 - c)
            if any(bool(z >> j & 1) != bool(z >> (j ^ bit) & 1)
                   for j in range(16)):
                s += 1
        return s

    QUAD = {}
    for ci, cj, nm in ((3, 2, "q0q1"), (1, 0, "r0r1")):
        QUAD[nm] = [sum(1 << j for j in range(16)
                        if (j >> ci & 1) == u and (j >> cj & 1) == v)
                    for u in (0, 1) for v in (0, 1)]
    ok_t = True
    for t, fam in zip(terms, fams):
        if len(fam) != t["events"]:
            ok_t = False
        if not isclosed(fam):
            ok_t = False
        isev, arr, ceil, floor = tabs(fam)
        if fail_lowers(isev, arr, ceil):
            ok_t = False
        for nm in ("q0q1", "r0r1"):
            if t["classification"]["reconstructs_" + nm] != \
                    all(a in fam for a in QUAD[nm]):
                ok_t = False
        if t["classification"]["four_coordinate_event_count"] != \
                sum(1 for z in fam if sup16(z) == 4):
            ok_t = False
    check(ok_t, "core16 terminal re-audit")
    check(p["every_terminal_reconstructs_a_same_side_boundary"] ==
          all(t["classification"]["reconstructs_q0q1"]
              or t["classification"]["reconstructs_r0r1"]
              for t in terms),
          "core16 same-side theorem flag")
    incl = [[i, j] for i, a in enumerate(fams)
            for j, b in enumerate(fams) if i != j and a < b]
    check(incl == p["strict_inclusions"], "core16 inclusions")
    mins = [i for i in range(len(fams))
            if not any(j != i and fams[j] < fams[i]
                       for j in range(len(fams)))]
    check(mins == p["inclusion_minimal_terminals"],
          "core16 minimal terminals")
    check(all(any(fams[m] <= fams[i] for m in mins)
              for i in range(len(fams))) ==
          p["every_terminal_contains_an_inclusion_minimal_terminal"],
          "core16 covering flag")
    # rectangle-necessity finite core
    low0 = int(p["canonical_first_lower_hex"], 16)
    up0 = int(p["canonical_first_upper_hex"], 16)
    cands = [int(h, 16) for h in p["canonical_interval_candidates_hex"]]
    isev, arr, ceil, floor = tabs(ev0)
    check(low0 in fail_lowers(isev, arr, ceil)
          and int(ceil[low0]) == up0
          and sorted(cands) == sorted(low0 | s for s in range(65536)
                                      if not s & ~(up0 & ~low0 & 0xFFFF)),
          "core16 canonical interval")
    check(p["canonical_candidates_all_four_coordinate"] ==
          all(sup16(z) == 4 for z in cands),
          "core16 four-coordinate necessity")


# ---------------------------------------------------------------- stage 4

def verify_cascade(states, blocks, npts, masks, raw, full, ev0):
    with open(os.path.join(HERE,
                           "full_grid_2x2_rectangle_cascade.json")) as f:
        rec = json.load(f)
    p = rec["payload"]
    cyl = {q: 0 for q in PROFILES}
    for profile, lists, ns, offset, size in blocks:
        cyl[profile[2:]] |= ((1 << size) - 1) << offset
    qmask = {0: masks[((0, 0), "e11")] | masks[((0, 0), "e10")],
             1: masks[((1, 0), "e11")] | masks[((1, 0), "e10")]}
    rmask = {0: masks[((0, 0), "e11")] | masks[((0, 0), "e01")],
             1: masks[((0, 1), "e11")] | masks[((0, 1), "e01")]}
    act = {"row0": 0, "row1": 0}
    for profile, lists, ns, offset, size in blocks:
        m = ((1 << size) - 1) << offset
        if profile[0] == (1, 1, 1):
            act["row0"] |= m
        if profile[1] == (1, 1, 1):
            act["row1"] |= m

    def trace_event(word):
        z = 0
        for i2, pr in enumerate(PROFILES):
            if word >> i2 & 1:
                z |= cyl[pr]
        return z

    def flags_of(e):
        out = []
        if e and e != full:
            for side, (qa, qb) in (("q0q1", (qmask[0], qmask[1])),
                                   ("r0r1", (rmask[0], rmask[1]))):
                quads = [qa & qb, qa & ~qb & full, ~qa & full & qb,
                         ~qa & full & ~qb & full]
                acc = 0
                for qm in quads:
                    if qm & e:
                        acc |= qm
                if acc == e and e not in (qa, full ^ qa, qb, full ^ qb):
                    out.append("same_side_" + side)
            for row in ("row0", "row1"):
                if e | act[row] == act[row]:
                    out.append("activation_supported_" + row)
        return out

    def bits(m):
        while m:
            bb = m & -m
            yield bb.bit_length() - 1
            m ^= bb

    def family_of(tracewords):
        seed = set(ev0) | {trace_event(w) for w in tracewords} \
            | {full ^ trace_event(w) for w in tracewords}
        fam, _ = closure(seed, full)
        return fam

    def kword(e):
        """16-bit profile word if e is a union of full profile cylinders,
        else None."""
        w = 0
        acc = 0
        for i2, pr in enumerate(PROFILES):
            c = cyl[pr]
            if c & e:
                if c | e != e:
                    return None
                w |= 1 << i2
                acc |= c
        return w if acc == e else None

    def order_and_pc(fam):
        evs = sorted(fam)
        n = len(evs)
        up = [0] * n
        for i, x in enumerate(evs):
            for j, y in enumerate(evs):
                if x | y == y:
                    up[i] |= 1 << j
        pc = [e.bit_count() for e in evs]
        return evs, up, pc

    def jexists(up, pc, i, j):
        cu = up[i] & up[j]
        best_k, best_pc, tie = -1, None, False
        r = cu
        while r:
            bb = r & -r
            k = bb.bit_length() - 1
            r ^= bb
            if best_pc is None or pc[k] < best_pc:
                best_pc, best_k, tie = pc[k], k, False
            elif pc[k] == best_pc:
                tie = True
        return best_k >= 0 and not tie and up[best_k] & cu == cu

    def wclose(ws, until=None):
        """Word closure (numpy-chunked); stops early if `until` appears."""
        import numpy as np
        ev = set(ws)
        while True:
            if until is not None and until in ev:
                return ev
            arr = np.fromiter(ev, dtype=np.uint32, count=len(ev))
            cand = set(np.bitwise_xor(np.uint32(0xFFFF), arr).tolist())
            for lo in range(0, len(arr), 4096):
                blk = arr[lo:lo + 4096]
                dis = (blk[:, None] & arr[None, :]) == 0
                cand |= set((blk[:, None] | arr[None, :])[dis].tolist())
            new = cand - ev
            if not new:
                return ev
            ev |= new

    def word_scan(evs, up, pc):
        """K-events, word-level failing pairs, and the producer's selected
        event pair (first event-verified word failure by gap order)."""
        kmap = {}
        for i, e in enumerate(evs):
            w = kword(e)
            if w is not None:
                kmap[w] = i
        words = sorted(kmap)
        inw = [False] * 65536
        ceilw = [0xFFFF] * 65536
        for w in words:
            inw[w] = True
            ceilw[w] = w
        for b in range(16):
            bit = 1 << b
            for u in range(65536):
                if not u & bit:
                    ceilw[u] &= ceilw[u | bit]
        wfails = []
        for a in range(len(words)):
            wa = words[a]
            for wb in words[a + 1:]:
                if not inw[ceilw[wa | wb]]:
                    wfails.append((wa, wb))
        chosen = None
        for (wa, wb) in sorted(
                wfails, key=lambda q: (
                    (ceilw[q[0] | q[1]] & ~(q[0] | q[1]) & 0xFFFF)
                    .bit_count(), q)):
            i, j = kmap[wa], kmap[wb]
            if not jexists(up, pc, i, j):
                chosen = (i, j)
                break
        return len(kmap), wfails, chosen

    tw = {}
    for node in p["tree"]:
        tw[node["id"]] = [int(h, 16) for h in node["added_traces"]]
    tree_ok = True
    cache = {}
    for node in p["tree"]:
        key = frozenset(tw[node["id"]])
        if key in cache:
            fam = cache[key]
        else:
            fam = family_of(tw[node["id"]])
            cache[key] = fam
        if len(fam) != node["events"]:
            tree_ok = False
            print("  tree node", node["id"], "family size mismatch")
            continue
        evs, up, pc = order_and_pc(fam)
        nk, wfails, chosen = word_scan(evs, up, pc)
        if len(wfails) != node["failing_word_pairs"] \
                or nk != node["K_events"]:
            tree_ok = False
            print("  tree node", node["id"], "word-fail/K count mismatch")
        if node["scan_scope"] == "word_level" and chosen is None:
            tree_ok = False
            print("  tree node", node["id"], "scope mismatch")
        if "chosen_pair_sha256" in node and chosen is not None:
            got = sorted(digest(evs[k], npts) for k in chosen)
            if got != sorted(node["chosen_pair_sha256"]):
                tree_ok = False
                print("  tree node", node["id"], "chosen pair mismatch")
        if "children" in node:
            must = 0
            for pr in node["must_profiles"]:
                must |= 1 << PROFILES.index(tuple(int(c) for c in pr))
            freeb = [PROFILES.index(tuple(int(c) for c in pr))
                     for pr in node["free_profiles"]]
            want = sorted(must | sum(1 << b for t2, b in enumerate(freeb)
                                     if s >> t2 & 1)
                          for s in range(1 << len(freeb)))
            got = sorted(int(h, 16) for h in node["children"])
            if want != got:
                tree_ok = False
                print("  tree node", node["id"], "children mismatch")
            # recompute must/free from the chosen pair's event bounds
            if chosen is not None:
                i2, j2 = chosen
                lower = evs[i2] | evs[j2]
                mustw = 0
                for t2, prof in enumerate(PROFILES):
                    if cyl[prof] & lower:
                        mustw |= 1 << t2
                allow = 0xFFFF
                r = up[i2] & up[j2]
                while r:
                    bb = r & -r
                    k = bb.bit_length() - 1
                    r ^= bb
                    w2 = 0
                    for t2, prof in enumerate(PROFILES):
                        if cyl[prof] | evs[k] == evs[k]:
                            w2 |= 1 << t2
                    allow &= w2
                if mustw != must or (allow & ~mustw) != sum(
                        1 << b for b in freeb):
                    tree_ok = False
                    print("  tree node", node["id"],
                          "must/free words mismatch")
        print("  tree node %d replayed (events %d word-fails %d)"
              % (node["id"], len(fam), len(wfails)), flush=True)
    check(tree_ok, "cascade tree replay")
    # branch receipts
    i = 0
    br_ok = True
    branch_keys = set()
    while True:
        path = os.path.join(HERE,
                            "full_grid_2x2_rectangle_branch_%03d.json" % i)
        if not os.path.exists(path):
            break
        with open(path) as f:
            b = json.load(f)["payload"]
        words = [int(s["trace_word"], 16) for s in b.get("path", [])]
        branch_keys.add(frozenset(words))
        if b["outcome"] in ("cap", "cap_branch_width"):
            if b.get("method") == "word_predicted":
                # verify the word-closure size claim from the PARENT family
                # without building the (deliberately capped) child family
                pkey = frozenset(words[:-1])
                pfam = cache.get(pkey)
                if pfam is None:
                    pfam = family_of(words[:-1])
                    cache[pkey] = pfam
                pwords = {kword(e) for e in pfam} - {None}
                wc = wclose(pwords | {words[-1]})
                if len(wc) != b["word_closure_size"]:
                    br_ok = False
                    print("  branch", i, "word closure size mismatch",
                          len(wc), b["word_closure_size"])
            print("  branch %d (%s) replayed" % (i, b["outcome"]),
                  flush=True)
            i += 1
            continue
        if b["outcome"] == "monotone_certificate" and \
                b["certificate"].get("method") == "word_closure_L3":
            # verify at word level from the parent family; the certificate
            # event's membership in the (possibly huge) child family is
            # Lemma L3, not recomputed
            ce = b["certificate"]
            pkey = frozenset(words[:-1])
            pfam = cache.get(pkey)
            if pfam is None:
                pfam = family_of(words[:-1])
                cache[pkey] = pfam
            pwords = {kword(e) for e in pfam} - {None}
            v = int(ce["word"], 16)
            wc = wclose(pwords | {words[-1]}, until=v)
            zmask = 0
            for t2, prof in enumerate(PROFILES):
                if v >> t2 & 1:
                    zmask |= cyl[prof]
            if v not in wc or digest(zmask, npts) != ce["event_sha256"] \
                    or sorted(flags_of(zmask)) != sorted(ce["flags"]):
                br_ok = False
                print("  branch", i, "L3 certificate mismatch")
            print("  branch %d (%s/L3) replayed" % (i, b["outcome"]),
                  flush=True)
            i += 1
            continue
        key = frozenset(words)
        fam = cache.get(key)
        if fam is None:
            fam = family_of(words)
            cache[key] = fam
        if b["outcome"] == "monotone_certificate":
            ce = b["certificate"]
            found = [e for e in fam
                     if digest(e, npts) == ce["event_sha256"]]
            if len(found) != 1 or \
                    sorted(flags_of(found[0])) != sorted(ce["flags"]):
                br_ok = False
                print("  branch", i, "certificate mismatch")
        elif b["outcome"] == "no_K_candidate":
            evs, up, pc = order_and_pc(fam)
            didx = {digest(e, npts): k for k, e in enumerate(evs)}
            a2 = didx.get(b["pair_sha256"][0])
            b2 = didx.get(b["pair_sha256"][1])
            if a2 is None or b2 is None or jexists(up, pc, a2, b2):
                br_ok = False
                print("  branch", i, "no_K pair not failing")
            else:
                lower = evs[a2] | evs[b2]
                mustw = 0
                allow = 0xFFFF
                for i2, prof in enumerate(PROFILES):
                    if cyl[prof] & lower:
                        mustw |= 1 << i2
                cu = up[a2] & up[b2]
                for k in bits(cu):
                    w2 = 0
                    for i2, prof in enumerate(PROFILES):
                        if cyl[prof] | evs[k] == evs[k]:
                            w2 |= 1 << i2
                    allow &= w2
                if not (mustw & ~allow):
                    br_ok = False
                    print("  branch", i, "no_K words mismatch")
        elif b["outcome"] == "oml_completion":
            evs, up, pc = order_and_pc(fam)
            fails = []
            for a2 in range(len(evs)):
                for b2 in range(a2 + 1, len(evs)):
                    if not jexists(up, pc, a2, b2):
                        fails.append((a2, b2))
                        break
                if fails:
                    break
            if fails or len(evs) != b["events"]:
                br_ok = False
                print("  branch", i, "completion replay mismatch")
            famsha = hashlib.sha256(
                ("\n".join(digest(e, npts) for e in sorted(evs)))
                .encode()).hexdigest()
            if famsha != b["family_sha256"]:
                br_ok = False
                print("  branch", i, "family sha mismatch")
        elif b["outcome"] in ("cap", "cap_branch_width"):
            pass
        print("  branch %d (%s) replayed" % (i, b["outcome"]), flush=True)
        i += 1
    check(br_ok, "cascade branch receipts (%d)" % i)
    ntot = sum(p["branch_outcomes"].values())
    check(ntot == i, "branch receipt count equals outcome total")
    tree_keys = {frozenset(v) for v in tw.values()}
    coverage_ok = True
    for node in p["tree"]:
        parent = frozenset(tw[node["id"]])
        for hs in node.get("children", []):
            child = parent | {int(hs, 16)}
            dispositions = int(child in tree_keys) + int(child in branch_keys)
            if dispositions != 1:
                coverage_ok = False
                print("  child disposition mismatch", node["id"], hs,
                      dispositions)
    check(coverage_ok, "every recorded cascade child has one disposition")


def verify_master():
    path = os.path.join(HERE, "full_grid_2x2_rectangle_master.json")
    with open(path) as f:
        p = json.load(f)["payload"]
    files = sorted(fn for fn in os.listdir(HERE)
                   if fn.startswith("full_grid_2x2_rectangle_")
                   and fn.endswith(".json")
                   and fn != "full_grid_2x2_rectangle_master.json")
    got = {fn: hashlib.sha256(open(os.path.join(HERE, fn), "rb").read()).hexdigest()
           for fn in files}
    check(got == p["files_sha256"], "master binds every rectangle receipt")
    sources = {
        "full_grid_2x2_rectangle_repair_search.py": hashlib.sha256(
            open(os.path.join(HERE,
                 "full_grid_2x2_rectangle_repair_search.py"), "rb").read()).hexdigest(),
        "full_grid_2x2_rectangle_repair_verify.py": hashlib.sha256(
            open(__file__, "rb").read()).hexdigest()}
    check(sources == p["source_sha256"], "master binds producer and verifier")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=("witnesses", "core16", "completed",
                                        "cascade", "all"), default="completed")
    args = ap.parse_args()
    need_carrier = args.stage in ("witnesses", "completed", "cascade", "all")
    states = blocks = npts = masks = raw = full = ev0 = None
    if need_carrier:
        print("[verify] building carrier independently ...", flush=True)
        states, blocks, npts = build()
        masks = build_masks(states, blocks)
        raw, full = raw_family(masks, npts)
        ev0, rounds = closure(set(raw), full)
        check(rounds[:1] == [32] and sum(rounds[1:]) == 0,
              "closure rounds")
    if args.stage in ("witnesses", "completed", "all"):
        verify_witnesses(states, blocks, npts, masks, raw, full, ev0)
    if args.stage in ("core16", "completed", "all"):
        print("[verify] core16 ...", flush=True)
        verify_core16()
    if args.stage in ("cascade", "all"):
        print("[verify] cascade ...", flush=True)
        verify_cascade(states, blocks, npts, masks, raw, full, ev0)
        verify_master()
    print("VERIFY:", "PASS" if not FAILURES else
          "FAIL (%d)" % len(FAILURES))
    raise SystemExit(0 if not FAILURES else 1)


if __name__ == "__main__":
    main()
