#!/usr/bin/env python3
"""Rectangle-cut repair search for the full conditional 2x2 grid.

Deterministic producer.  Campaign 16, 2026-07-14.  Read-only with respect to
all previously banked artifacts; emits its own receipts only.

CONTENTS
  1. Independent reconstruction of the 6,186,568-point compatible carrier of
     four pasted incompatible-H4 conditional cells (rows share (a1,a2,a3,q_a),
     columns share r_i), with the canonical bit order of
     full_grid_2x2_conditional_cell_audit.py, so little-endian sha256 digests
     of event bitmasks are directly comparable with the banked receipt.
     The construction code is independent (backtracking state enumeration,
     integer-multiplication mask tiling).
  2. Exhaustive failed-pair census of the 230-event concrete orthogonal
     closure: ALL unordered pairs with non-unique minimal upper bounds or
     maximal lower bounds, with explicit incomparable-extrema witnesses,
     admissible intervals, free coordinate profiles, and orbits under the
     row-swap/column-swap symmetry group (symmetry validated semantically).
  3. Class-K branch-cascade search for an OML completion inside the same
     concrete powerset representation.  CANDIDATE CLASS K (stated precisely):
     an admissible repair candidate for a failing pair (x,y) is a union of
     full (q0,q1,r0,r1) coordinate-profile cylinders z with
     x|y <= z <= AND of all current upper bounds of (x,y).
     At every node the failing pair with the fewest free profiles is chosen
     among pairs of two K-events first (Lemma L2 permits any choice of
     failing pair; K-pairs keep the branching inside the finite word game
     below), falling back to arbitrary failing pairs only when no K-pair
     fails, and ALL K-candidates are branched on.  Branches are pruned
     exactly when a MONOTONE certificate appears, i.e. one inherited by
     every extension of the current family:
       - a nontrivial same-side measurable event ((q0,q1)- or (r0,r1)-
         measurable, beyond 0,1 and the marginals), or
       - a nonzero activation-supported event (inside a row activation
         cylinder), or
       - no K-candidate exists for some failing pair.
     WORD-CLOSURE PRUNING (Lemma L3).  The word of a K-event is its 16-bit
     set of coordinate profiles.  Complements and disjoint unions of
     K-events are K-events whose words are the complement and disjoint
     union of the words.  Hence, if the complement/disjoint-union closure
     of {words of K-events present} u {candidate word} contains a
     same-side-measurable word w, then the child family already contains
     the K-event with word w (realized by the mirrored complement/disjoint-
     union steps), and the branch carries the same-side certificate without
     any event-level computation.  The certificate event is the cylinder
     union of w, checked explicitly.
     Termination without failure = concrete OML completion (orthomodularity
     is automatic, Lemma L1 below); each such terminal is fully audited.
     Searches are exhaustive ONLY within class K; candidates outside K
     (unions of partial macro-blocks) are not enumerated.
  4. Stripped-core exhaustive classification on the 16-point carrier
     {0,1}^4: ALL concrete-logic OML completions of the union R of the four
     edge algebras Bool(q_a,r_i) inside P(16), via the same branch cascade
     with candidate class = ALL subsets of the admissible interval (genuinely
     exhaustive there), plus the covering lemma L2.  Classifies every
     terminal for same-side boundary reconstruction and verifies the normal
     form of the two inclusion-minimal terminals.

LEMMA L1 (orthomodularity is automatic).  Let F be a finite family of
subsets of a set X, containing 0 and X, closed under set complement and
disjoint set union, that is a lattice under inclusion (every pair has a
unique minimal upper bound and a unique maximal lower bound).  Then F with
set complementation is an orthomodular lattice.  Proof: let x <= y in F.
y \\ x = (y' u x)' is in F because y',x are disjoint members.  y\\x is a
lower bound of {x',y}; any event l <= x',y satisfies l <= x' n y = y\\x, so
meet(x',y) = y\\x.  x and y\\x are disjoint, so x u (y\\x) = y is in F and is
an upper bound of {x, y\\x}; every upper bound contains their union y, so
join(x, meet(x',y)) = y.  QED.

LEMMA L2 (covering).  Let F be a concrete-logic OML completion of a closed
family E0 inside P(X) (F closed under complement and disjoint union, lattice
under inclusion, F >= E0).  Consider any cascade tree rooted at E0 in which
each node N (a closed family <= F by induction) either is a lattice (leaf)
or selects one failing pair (x,y) of N and branches over candidates z with
x|y <= z <= AND of all upper bounds of (x,y) IN N, recursing on the closure
of N u {z, z'}.  Then join_F(x,y) is such a candidate (it contains x|y and
is contained in every N-upper bound, N <= F), and closure(N u {join_F(x,y),
its complement}) <= F.  Hence, by induction, F contains at least one leaf
family of any tree that branches over ALL candidates from a class containing
join_F(x,y).  For the 16-point search the class is all interval subsets, so
EVERY completion contains a terminal family.  For the full-carrier search
the class is K, so the covering statement is restricted to completions whose
selected joins lie in K.

Usage:
  python3 full_grid_2x2_rectangle_repair_search.py --emit     # write receipts
  python3 full_grid_2x2_rectangle_repair_search.py            # recompute, compare
  python3 full_grid_2x2_rectangle_repair_search.py --stage census   # one stage

stdlib + numpy (numpy used only for the 16-point stage and the semantic
symmetry validation).  Deterministic.  Evidence class: exhaustive finite
censuses and machine-checked finite branch trees; the two lemmas above are
hand proofs whose finite ingredients are machine-checked.  NO finite-to-
infinite promotion and NO claim of canonicality of any closure is made.
"""
import argparse
import hashlib
import json
import os
import sys
from itertools import product

SCHEMA = "full-grid-2x2-rectangle-repair-v1"
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
ATOMS = sorted({a for b in CELL_BLOCKS for a in b})
CELLS = ((0, 0), (0, 1), (1, 0), (1, 1))
PROFILES = tuple(product((0, 1), repeat=4))   # (q0,q1,r0,r1)

# caps for the class-K cascade (counts, not wall clock: deterministic)
CAP_NODES = 200
CAP_FAMILY = 3000
CAP_DEPTH = 30
CAP_CORE16_NODES = 500000

SAMESIDE_TRIVIAL = (0x0000, 0xFFFF, 0x00FF, 0xFF00, 0x0F0F, 0xF0F0,
                    0x3333, 0xCCCC, 0x5555, 0xAAAA)


def sameside_word(w):
    """'q0q1' / 'r0r1' if the 16-bit profile word is nontrivially measurable
    in that same-side coordinate pair (profile index = 8*q0+4*q1+2*r0+r1)."""
    if w in SAMESIDE_TRIVIAL:
        return None
    if all((w >> (4 * k)) & 0xF in (0, 0xF) for k in range(4)):
        return "q0q1"
    col = w & 0xF
    if w == col | (col << 4) | (col << 8) | (col << 12):
        return "r0r1"
    return None


def word_closure(ws):
    """Least complement/disjoint-union-closed set of 16-bit words."""
    ws = set(ws)
    frontier = set(ws)
    while frontier:
        new = set()
        snap = sorted(ws)
        for a in frontier:
            c = 0xFFFF ^ a
            if c not in ws:
                new.add(c)
            for b in snap:
                if not a & b:
                    u = a | b
                    if u not in ws:
                        new.add(u)
        new -= ws
        ws |= new
        frontier = new
    return ws


# ----------------------------------------------------------------------
# section 1: construction
# ----------------------------------------------------------------------

def cell_states():
    """All 224 two-valued states of the 24-atom cell, by backtracking."""
    blocks = [tuple(b) for b in CELL_BLOCKS]
    out = []
    val = {}

    def bt(i):
        if i == len(blocks):
            out.append(frozenset(a for a, v in val.items() if v))
            return
        blk = blocks[i]
        for cand in blk:
            if val.get(cand) is False:
                continue
            others = [a for a in blk if a != cand]
            if any(val.get(a) is True for a in others):
                continue
            touched = []
            if cand not in val:
                val[cand] = True
                touched.append(cand)
            for a in others:
                if a not in val:
                    val[a] = False
                    touched.append(a)
            bt(i + 1)
            for a in touched:
                del val[a]

    bt(0)
    uniq = sorted(set(out), key=lambda s: tuple(sorted(s)))
    assert len(uniq) == len(out) == 224
    return uniq


def sig_aqr(state):
    a = tuple(int(x in state) for x in SHARED)
    q = int("e11" in state or "e10" in state)
    r = int("e11" in state or "e01" in state)
    return a, q, r


def build_carrier():
    """(states, blocks, npts); blocks = (profile6, lists, ns, offset, size),
    profile6 = (a0,a1,q0,q1,r0,r1) in lexicographic order, a0 slowest; within
    a block, cell-state tuples (s00,s01,s10,s11), s11 fastest."""
    states = cell_states()
    groups = {}
    for j, s in enumerate(states):
        a, q, r = sig_aqr(s)
        groups.setdefault((a, q, r), []).append(j)
    blocks = []
    offset = 0
    P3 = list(product((0, 1), repeat=3))
    for a0 in P3:
        for a1 in P3:
            for q0, q1, r0, r1 in product((0, 1), repeat=4):
                lists = (groups.get((a0, q0, r0), []),
                         groups.get((a0, q0, r1), []),
                         groups.get((a1, q1, r0), []),
                         groups.get((a1, q1, r1), []))
                ns = tuple(len(x) for x in lists)
                size = ns[0] * ns[1] * ns[2] * ns[3]
                if not size:
                    continue
                blocks.append(((a0, a1, q0, q1, r0, r1), lists, ns,
                               offset, size))
                offset += size
    return states, blocks, offset


def rep_int(period, copies):
    if copies == 0:
        return 0
    return ((1 << (copies * period)) - 1) // ((1 << period) - 1)


def atom_masks(states, blocks):
    """Bitmask per (cell, atom-base), integer-multiplication tiling."""
    masks = {(c, x): 0 for c in CELLS for x in ATOMS}
    state_has = [{x: (x in s) for x in ATOMS} for s in states]
    for profile, lists, ns, offset, size in blocks:
        inner = (ns[1] * ns[2] * ns[3], ns[2] * ns[3], ns[3], 1)
        for ci, cell in enumerate(CELLS):
            period = ns[ci] * inner[ci]
            rep = rep_int(period, size // period)
            ones = (1 << inner[ci]) - 1
            for atom in ATOMS:
                unit = 0
                for pos, sj in enumerate(lists[ci]):
                    if state_has[sj][atom]:
                        unit |= ones << (pos * inner[ci])
                if unit:
                    masks[(cell, atom)] |= (unit * rep) << offset
    return masks


def raw_events(masks, npts):
    full = (1 << npts) - 1
    events = {0: "0", full: "1"}
    for c in CELLS:
        for block in CELL_BLOCKS:
            for z in range(1, 1 << len(block)):
                e = 0
                names = []
                for j, a in enumerate(block):
                    if z >> j & 1:
                        e |= masks[(c, a)]
                        names.append("%s@%d%d" % (a, c[0], c[1]))
                events.setdefault(e, "+".join(names))
    return events, full


def profile_cylinders(blocks):
    cyl = {p: 0 for p in PROFILES}
    for profile, lists, ns, offset, size in blocks:
        cyl[profile[2:]] |= ((1 << size) - 1) << offset
    return cyl


def activation_cylinders(blocks):
    act = {"row0": 0, "row1": 0, "both": 0}
    for profile, lists, ns, offset, size in blocks:
        m = ((1 << size) - 1) << offset
        if profile[0] == (1, 1, 1):
            act["row0"] |= m
        if profile[1] == (1, 1, 1):
            act["row1"] |= m
        if profile[0] == (1, 1, 1) and profile[1] == (1, 1, 1):
            act["both"] |= m
    return act


def close_orthogonally(seed, full):
    """Least complement/disjoint-union-closed superfamily, incremental."""
    ev = set(seed)
    frontier = set(seed)
    rounds = []
    while frontier:
        new = set()
        for x in frontier:
            c = full ^ x
            if c not in ev:
                new.add(c)
        snap = sorted(ev)
        for x in sorted(frontier):
            for y in snap:
                if x != y and not x & y:
                    u = x | y
                    if u not in ev:
                        new.add(u)
        new -= ev
        rounds.append(len(new))
        ev |= new
        frontier = new
    return ev, rounds


def point_key(bitpos, states, blocks):
    """Structural, order-independent description of a carrier point."""
    lo, hi = 0, len(blocks)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if blocks[mid][3] <= bitpos:
            lo = mid
        else:
            hi = mid
    profile, lists, ns, offset, size = blocks[lo]
    rem = bitpos - offset
    inner = (ns[1] * ns[2] * ns[3], ns[2] * ns[3], ns[3], 1)
    idxs = []
    for ci in range(4):
        idxs.append(lists[ci][(rem // inner[ci]) % ns[ci]])
    return {
        "profile_a0_a1_q0_q1_r0_r1": [list(profile[0]), list(profile[1]),
                                      profile[2], profile[3], profile[4],
                                      profile[5]],
        "cell_states_sorted_atoms": [sorted(states[j]) for j in idxs],
    }


# ----------------------------------------------------------------------
# section 2: reproduction, census, witnesses
# ----------------------------------------------------------------------

def digest(x, npts):
    return hashlib.sha256(x.to_bytes((npts + 7) // 8, "little")).hexdigest()


def bits(m):
    while m:
        b = m & -m
        yield b.bit_length() - 1
        m ^= b


class Grid:
    def __init__(self):
        self.states, self.blocks, self.npts = build_carrier()
        self.masks = atom_masks(self.states, self.blocks)
        raw, self.full = raw_events(self.masks, self.npts)
        self.raw = raw
        ev, self.rounds = close_orthogonally(set(raw), self.full)
        self.ev0 = sorted(ev)
        self.labels = dict(raw)
        self.cyl = profile_cylinders(self.blocks)
        self.act = activation_cylinders(self.blocks)
        self.qmask = {0: self.masks[((0, 0), "e11")] | self.masks[((0, 0), "e10")],
                      1: self.masks[((1, 0), "e11")] | self.masks[((1, 0), "e10")]}
        self.rmask = {0: self.masks[((0, 0), "e11")] | self.masks[((0, 0), "e01")],
                      1: self.masks[((0, 1), "e11")] | self.masks[((0, 1), "e01")]}

    def label(self, e):
        got = self.labels.get(e)
        if got:
            return got
        # canonical label for a coordinate-cylinder union, else digest tag
        tr = self.trace_of(e)
        if tr is not None:
            return "cyl[" + ",".join("".join(map(str, p))
                                     for p in tr) + "]"
        return "set:" + digest(e, self.npts)[:16]

    def trace_of(self, e):
        """If e is a union of full profile cylinders, its sorted profile
        list; else None."""
        tr = []
        acc = 0
        for p in PROFILES:
            c = self.cyl[p]
            if c & e:
                if c | e != e:
                    return None
                tr.append(p)
                acc |= c
        return tr if acc == e else None

    def cylword(self, e):
        """16-bit word: bit i set iff cylinder of PROFILES[i] <= e."""
        w = 0
        for i, p in enumerate(PROFILES):
            c = self.cyl[p]
            if c | e == e:
                w |= 1 << i
        return w

    def touchword(self, e):
        w = 0
        for i, p in enumerate(PROFILES):
            if self.cyl[p] & e:
                w |= 1 << i
        return w


def order_tables(evs):
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
            b = r & -r
            down[b.bit_length() - 1] |= 1 << i
            r ^= b
    return up, down


def extrema(up, down, i, j):
    cu = up[i] & up[j]
    cd = down[i] & down[j]
    mu = [z for z in bits(cu) if down[z] & cu == 1 << z]
    ml = [z for z in bits(cd) if up[z] & cd == 1 << z]
    return mu, ml


def census(g):
    evs = g.ev0
    up, down = order_tables(evs)
    n = len(evs)
    join_fail = []
    meet_fail = []
    for i in range(n):
        for j in range(i + 1, n):
            mu, ml = extrema(up, down, i, j)
            if len(mu) != 1:
                join_fail.append((i, j, mu))
            if len(ml) != 1:
                meet_fail.append((i, j, ml))
    idx = {e: k for k, e in enumerate(evs)}
    comp_of = {(min(i, j), max(i, j)) for i, j, _ in join_fail}
    meets_are_complements = all(
        (min(idx[g.full ^ evs[i]], idx[g.full ^ evs[j]]),
         max(idx[g.full ^ evs[i]], idx[g.full ^ evs[j]])) in comp_of
        for i, j, _ in meet_fail)
    pairs = []
    for i, j, mu in join_fail:
        x, y = evs[i], evs[j]
        lower = x | y
        upper = g.full
        for k in bits(up[i] & up[j]):
            upper &= evs[k]
        must = [p for p in PROFILES if g.cyl[p] & lower]
        free = [p for p in PROFILES
                if not (g.cyl[p] & lower) and g.cyl[p] | upper == upper]
        interval_is_profile_clean = (
            all(g.cyl[p] | upper == upper for p in must)
            and sum(g.cyl[p] for p in must + free) == upper)
        wit = []
        for a in range(len(mu)):
            for b in range(len(mu)):
                if a != b:
                    d = evs[mu[a]] & ~evs[mu[b]] & g.full
                    wit.append({
                        "in_bound": g.label(evs[mu[a]]),
                        "not_in_bound": g.label(evs[mu[b]]),
                        "point": point_key(next(bits(d)), g.states,
                                           g.blocks)})
        pairs.append({
            "x_label": g.label(x), "y_label": g.label(y),
            "x_sha256": digest(x, g.npts), "y_sha256": digest(y, g.npts),
            "minimal_upper_bound_labels": [g.label(evs[k]) for k in mu],
            "minimal_upper_bound_sha256": [digest(evs[k], g.npts)
                                           for k in mu],
            "minimal_upper_bound_count": len(mu),
            "maximal_lower_bound_labels": [
                g.label(evs[k]) for k in extrema(up, down, i, j)[1]],
            "lower_sha256": digest(lower, g.npts),
            "upper_sha256": digest(upper, g.npts),
            "must_profiles": ["".join(map(str, p)) for p in must],
            "free_profiles": ["".join(map(str, p)) for p in free],
            "interval_is_profile_clean": interval_is_profile_clean,
            "incomparability_witnesses": wit,
        })
    return join_fail, meet_fail, meets_are_complements, pairs, (up, down)


def symmetry_check(g):
    """Semantic validation of row-swap and column-swap symmetries: the point
    permutation maps the raw 198-family onto itself.  numpy required."""
    try:
        import numpy as np
    except ImportError:
        return {"validated": False, "reason": "numpy unavailable"}
    perm = {}
    for name, f in (("row_swap", lambda pr: (pr[1], pr[0], pr[3], pr[2],
                                             pr[4], pr[5])),
                    ("col_swap", lambda pr: (pr[0], pr[1], pr[2], pr[3],
                                             pr[5], pr[4]))):
        p = np.zeros(g.npts, dtype=np.int64)
        bidx = {b[0]: b for b in g.blocks}
        for profile, lists, ns, offset, size in g.blocks:
            tp = f(profile)
            tprofile, tlists, tns, toffset, tsize = bidx[tp]
            inner = (ns[1] * ns[2] * ns[3], ns[2] * ns[3], ns[3], 1)
            tinner = (tns[1] * tns[2] * tns[3], tns[2] * tns[3], tns[3], 1)
            # cell map: row swap sends cells (00,01,10,11)->(10,11,00,01);
            # col swap sends them to (01,00,11,10)
            cmap = (2, 3, 0, 1) if name == "row_swap" else (1, 0, 3, 2)
            for rem in range(size):
                pos = [(rem // inner[ci]) % ns[ci] for ci in range(4)]
                tpos = [0, 0, 0, 0]
                for ci in range(4):
                    tpos[cmap[ci]] = pos[ci]
                trem = sum(tpos[ci] * tinner[ci] for ci in range(4))
                p[offset + rem] = toffset + trem
        perm[name] = p
    nb = (g.npts + 7) // 8
    results = {}
    for name, p in perm.items():
        ok = True
        raws = set(g.raw)
        for e in sorted(g.raw):
            b = np.frombuffer(int(e).to_bytes(nb, "little"), dtype=np.uint8)
            u = np.unpackbits(b, bitorder="little")[:g.npts]
            t = np.zeros(g.npts, dtype=np.uint8)
            t[p] = u
            te = int.from_bytes(np.packbits(t, bitorder="little").tobytes(),
                                "little")
            if te not in raws:
                ok = False
                break
        results[name] = ok
    return {"validated": True, "raw_family_invariant": results}


def pair_orbit_key(xl, yl):
    """Canonical representative of the unordered pair {xl,yl} under the
    row-swap/column-swap group acting on cell tags in labels."""
    def t(l, m):
        out = []
        for part in l.split("+"):
            if "@" in part:
                a, c = part.split("@")
                out.append(a + "@" + m.get(c, c))
            else:
                out.append(part)
        return "+".join(out)
    rmap = {"00": "10", "01": "11", "10": "00", "11": "01"}
    cmap = {"00": "01", "01": "00", "10": "11", "11": "10"}
    orb = set()
    frontier = {(xl, yl)}
    while frontier:
        new = set()
        for (a, b) in frontier:
            for m in (rmap, cmap):
                cand = (t(a, m), t(b, m))
                if cand not in orb and cand not in frontier:
                    new.add(cand)
        orb |= frontier
        frontier = new - orb
    return min("|".join(sorted(p)) for p in orb)


# ----------------------------------------------------------------------
# section 3: class-K cascade on the full carrier
# ----------------------------------------------------------------------

class Cascade:
    """DFS over class-K repair choices with monotone-certificate pruning."""

    def __init__(self, g):
        self.g = g
        self.nodes = 0
        self.branch_count = 0
        self.memo = set()          # frozensets of added trace words
        self.tree = []             # per-node records
        self.branches = []         # terminal branch records
        self.capped = False

    def event_flags(self, e):
        g = self.g
        flags = []
        if e and e != g.full:
            for side, masks in (("q0q1", (g.qmask[0], g.qmask[1])),
                                ("r0r1", (g.rmask[0], g.rmask[1]))):
                qa, qb = masks
                quads = [qa & qb, qa & ~qb & g.full,
                         ~qa & g.full & qb, ~qa & g.full & ~qb & g.full]
                acc = 0
                for qm in quads:
                    if qm & e:
                        acc |= qm
                if acc == e and e not in (qa, g.full ^ qa, qb, g.full ^ qb):
                    flags.append("same_side_" + side)
            for row in ("row0", "row1"):
                if e | g.act[row] == g.act[row]:
                    flags.append("activation_supported_" + row)
        return flags

    def run(self):
        g = self.g
        evs = list(g.ev0)
        up, down = order_tables(evs)
        pc = [e.bit_count() for e in evs]
        cylw = [g.cylword(e) for e in evs]
        tchw = [g.touchword(e) for e in evs]
        for e in evs:
            assert not self.event_flags(e), \
                "initial family already carries a certificate"
        self.dfs(evs, up, down, pc, cylw, tchw, frozenset(), [], 0)
        return self

    @staticmethod
    def join_exists(up, pc, i, j):
        """Join exists iff the min-popcount member of the common upper set is
        unique and lies below every other member."""
        cu = up[i] & up[j]
        best_k = -1
        best_pc = None
        tie = False
        r = cu
        while r:
            b = r & -r
            k = b.bit_length() - 1
            r ^= b
            p = pc[k]
            if best_pc is None or p < best_pc:
                best_pc, best_k, tie = p, k, False
            elif p == best_pc:
                tie = True
        if best_k < 0 or tie:
            return False
        return up[best_k] & cu == cu

    def extend(self, evs, up, down, pc, cylw, tchw, newmask):
        """Close over newmask and its complement; extend order tables.
        Returns extended copies plus the list of added events."""
        g = self.g
        ev = set(evs)
        pending = {newmask, g.full ^ newmask} - ev
        added = []
        while pending:
            batch = sorted(pending)
            allev = sorted(ev)
            new = set()
            for x in batch:
                c = g.full ^ x
                new.add(c)
                for y in allev:
                    if not x & y:
                        new.add(x | y)
                for y in batch:
                    if x < y and not x & y:
                        new.add(x | y)
            ev |= pending
            added.extend(batch)
            pending = new - ev
        evs2 = list(evs) + added
        up2 = list(up) + [0] * len(added)
        down2 = list(down) + [0] * len(added)
        n0 = len(evs)
        n2 = len(evs2)
        for i in range(n0, n2):
            a = evs2[i]
            up2[i] |= 1 << i
            down2[i] |= 1 << i
            for j in range(i):
                b = evs2[j]
                u = a | b
                if u == b:
                    up2[i] |= 1 << j
                    down2[j] |= 1 << i
                if u == a:
                    up2[j] |= 1 << i
                    down2[i] |= 1 << j
        pc2 = pc + [e.bit_count() for e in added]
        cylw2 = cylw + [g.cylword(e) for e in added]
        tchw2 = tchw + [g.touchword(e) for e in added]
        return evs2, up2, down2, pc2, cylw2, tchw2, added

    def pair_words(self, up, cylw, tchw, i, j):
        cu = up[i] & up[j]
        must = tchw[i] | tchw[j]
        allowed = 0xFFFF
        r = cu
        while r:
            b = r & -r
            allowed &= cylw[b.bit_length() - 1]
            r ^= b
        return must, allowed

    def dfs(self, evs, up, down, pc, cylw, tchw, tracekey, path, depth):
        g = self.g
        if tracekey in self.memo:
            return
        self.memo.add(tracekey)
        self.nodes += 1
        if self.nodes > CAP_NODES or depth > CAP_DEPTH \
                or len(evs) > CAP_FAMILY:
            self.capped = True
            self.branch_count += 1
            self.branches.append({"path": path, "outcome": "cap",
                                  "events": len(evs), "depth": depth})
            return
        n = len(evs)
        isK = [cylw[k] == tchw[k] for k in range(n)]
        kidx = [k for k in range(n) if isK[k]]
        kmap = {tchw[k]: k for k in kidx}
        # word-level failing pairs among K-events (Lemma L2 permits
        # selecting any failing pair; a word-level failure that verifies
        # at event level is selected without an all-pairs event scan)
        words = sorted(kmap)
        inw = [False] * 65536
        for w in words:
            inw[w] = True
        ceilw = [0xFFFF] * 65536
        for w in words:
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
                u = wa | wb
                if not inw[ceilw[u]]:
                    wfails.append((wa, wb))
        chosen = None
        scan_scope = "word_level"
        for (wa, wb) in sorted(
                wfails, key=lambda p: (
                    (ceilw[p[0] | p[1]] & ~(p[0] | p[1]) & 0xFFFF)
                    .bit_count(), p)):
            i, j = kmap[wa], kmap[wb]
            if not self.join_exists(up, pc, i, j):
                chosen = (i, j)
                break
        if chosen is None:
            scan_scope = "all_pairs"
            fails = []
            for i in range(n):
                for j in range(i + 1, n):
                    if not self.join_exists(up, pc, i, j):
                        fails.append((i, j))
                        break
                if fails:
                    break
            chosen = fails[0] if fails else None
        print("[cascade] node %d depth %d events %d K-events %d "
              "word-fails %d scope %s path %s"
              % (self.nodes, depth, n, len(kidx), len(wfails), scan_scope,
                 "/".join("%04x" % t for t in sorted(tracekey))),
              flush=True)
        node_rec = {"id": self.nodes, "depth": depth,
                    "added_traces": sorted("%04x" % t for t in tracekey),
                    "events": n, "K_events": len(kidx),
                    "scan_scope": scan_scope,
                    "failing_word_pairs": len(wfails)}
        self.tree.append(node_rec)
        if chosen is None:
            # the all_pairs scan found no failing pair: genuine terminal
            node_rec["outcome"] = "oml_completion"
            self.terminal_audit(evs, up, down, pc, tracekey, path, depth)
            return
        i, j = chosen
        must, allowed = self.pair_words(up, cylw, tchw, i, j)
        if must & ~allowed:
            self.branch_count += 1
            self.branches.append({
                "path": path, "outcome": "no_K_candidate",
                "depth": depth, "events": n,
                "pair": [g.label(evs[i]), g.label(evs[j])],
                "pair_sha256": [digest(evs[i], g.npts),
                                digest(evs[j], g.npts)],
                "must_word": "%04x" % must,
                "allowed_word": "%04x" % allowed,
                "witness": self.pair_witness(evs, up, down, i, j),
            })
            node_rec["chosen_pair"] = [g.label(evs[i]), g.label(evs[j])]
            node_rec["outcome"] = "no_K_candidate"
            return
        freebits = [b for b in range(16) if (allowed & ~must) >> b & 1]
        node_rec["chosen_pair"] = [g.label(evs[i]), g.label(evs[j])]
        node_rec["chosen_pair_sha256"] = [digest(evs[i], g.npts),
                                          digest(evs[j], g.npts)]
        node_rec["must_profiles"] = ["".join(map(str, PROFILES[b]))
                                     for b in bits(must)]
        node_rec["free_profiles"] = ["".join(map(str, PROFILES[b]))
                                     for b in freebits]
        node_rec["children"] = []
        if len(freebits) > 6:
            self.capped = True
            self.branch_count += 1
            node_rec["outcome"] = "cap_branch_width"
            self.branches.append({"path": path,
                                  "outcome": "cap_branch_width",
                                  "free_bits": len(freebits),
                                  "events": len(evs), "depth": depth})
            return
        words_present = {tchw[k] for k in kidx}
        for s in range(1 << len(freebits)):
            w = must
            for t, b in enumerate(freebits):
                if s >> t & 1:
                    w |= 1 << b
            z = 0
            for b in bits(w):
                z |= g.cyl[PROFILES[b]]
            child_key = tracekey | {w}
            node_rec["children"].append("%04x" % w)
            if child_key in self.memo:
                continue
            newpath = path + [{"trace_word": "%04x" % w,
                               "trace_profiles": [
                                   "".join(map(str, PROFILES[b]))
                                   for b in bits(w)],
                               "repaired_pair": [g.label(evs[i]),
                                                 g.label(evs[j])]}]
            # Lemma L3: word-closure pruning, no event-level work needed
            wc = word_closure(words_present | {w})
            ssw = sorted(v for v in wc if sameside_word(v))
            if ssw:
                v = ssw[0]
                zmask = 0
                for b in bits(v):
                    zmask |= g.cyl[PROFILES[b]]
                flags = self.event_flags(zmask)
                assert any(f.startswith("same_side_") for f in flags)
                self.branch_count += 1
                self.branches.append({
                    "path": newpath,
                    "outcome": "monotone_certificate",
                    "certificate": {
                        "method": "word_closure_L3",
                        "event_label": g.label(zmask),
                        "event_sha256": digest(zmask, g.npts),
                        "flags": flags,
                        "word": "%04x" % v,
                        "word_closure_size": len(wc),
                        "same_side_words": ["%04x" % u for u in ssw]},
                    "depth": depth + 1})
                self.memo.add(child_key)
                continue
            evs2, up2, down2, pc2, cylw2, tchw2, added = \
                self.extend(evs, up, down, pc, cylw, tchw, z)
            newpath[-1]["closure_added"] = len(added)
            cert = None
            for e in added:
                flags = self.event_flags(e)
                if flags:
                    cert = {"method": "event_level",
                            "event_label": g.label(e),
                            "event_sha256": digest(e, g.npts),
                            "flags": flags,
                            "trace": (["".join(map(str, p))
                                       for p in g.trace_of(e)]
                                      if g.trace_of(e) is not None
                                      else None)}
                    break
            if cert is not None:
                self.branch_count += 1
                self.branches.append({
                    "path": newpath,
                    "outcome": "monotone_certificate",
                    "certificate": cert,
                    "depth": depth + 1, "events": len(evs2)})
                self.memo.add(child_key)
                continue
            self.dfs(evs2, up2, down2, pc2, cylw2, tchw2,
                     child_key, newpath, depth + 1)

    def pair_witness(self, evs, up, down, i, j):
        g = self.g
        mu, ml = extrema(up, down, i, j)
        wit = []
        for a in range(len(mu)):
            for b in range(len(mu)):
                if a != b:
                    d = evs[mu[a]] & ~evs[mu[b]] & g.full
                    wit.append({"in_bound": g.label(evs[mu[a]]),
                                "not_in_bound": g.label(evs[mu[b]]),
                                "point": point_key(next(bits(d)),
                                                   g.states, g.blocks)})
        return {"minimal_upper_bound_labels": [g.label(evs[k]) for k in mu],
                "minimal_upper_bound_count": len(mu),
                "incomparability_witnesses": wit}

    def terminal_audit(self, evs, up, down, pc, tracekey, path, depth):
        g = self.g
        n = len(evs)
        join = {}
        meet = {}
        ok = True
        for i in range(n):
            for j in range(i, n):
                cu = up[i] & up[j]
                jj = None
                best_pc, tie, r = None, False, cu
                while r:
                    b = r & -r
                    k = b.bit_length() - 1
                    r ^= b
                    if best_pc is None or pc[k] < best_pc:
                        best_pc, jj, tie = pc[k], k, False
                    elif pc[k] == best_pc:
                        tie = True
                if jj is None or tie or up[jj] & cu != cu:
                    jj = None
                cd = down[i] & down[j]
                mm = None
                best_pc, tie, r = None, False, cd
                while r:
                    b = r & -r
                    k = b.bit_length() - 1
                    r ^= b
                    if best_pc is None or pc[k] > best_pc:
                        best_pc, mm, tie = pc[k], k, False
                    elif pc[k] == best_pc:
                        tie = True
                if mm is None or tie or down[mm] & cd != cd:
                    mm = None
                if jj is None or mm is None:
                    ok = False
                join[i, j] = join[j, i] = jj
                meet[i, j] = meet[j, i] = mm
        idx = {e: k for k, e in enumerate(evs)}
        comp = [idx[g.full ^ e] for e in evs]
        oml = ok and all(
            join[i, meet[j, comp[i]]] == j
            for i in range(n) for j in range(n) if up[i] >> j & 1)
        centre = [i for i in range(n)
                  if ok and all(join[meet[i, j], meet[i, comp[j]]] == i
                                for j in range(n))]
        # cell sub-OML faithfulness
        faithful = True
        cell_events = {}
        for c in CELLS:
            fam = set()
            for block in CELL_BLOCKS:
                for zz in range(1, 1 << len(block)):
                    e = 0
                    for jj2, a in enumerate(block):
                        if zz >> jj2 & 1:
                            e |= g.masks[(c, a)]
                    fam.add(e)
            fam |= {0, g.full}
            cell_events[c] = sorted(fam)
        for c in CELLS:
            fam = cell_events[c]
            sub = [idx[e] for e in fam]
            fup, fdown = order_tables(fam)
            for a in range(len(fam)):
                for b in range(a + 1, len(fam)):
                    mu2, ml2 = extrema(fup, fdown, a, b)
                    if len(mu2) == 1 and join[sub[a], sub[b]] != sub[mu2[0]]:
                        faithful = False
                    if len(ml2) == 1 and meet[sub[a], sub[b]] != sub[ml2[0]]:
                        faithful = False
        # blocks: partitions of the carrier into minimal nonzero events
        # (maximal Boolean blocks of a complement/disjoint-union-closed
        # concrete lattice family are exactly such partitions)
        zero_i = idx[0]
        mins = [i for i in range(n) if evs[i]
                and down[i] == (1 << i) | (1 << zero_i)]
        partitions = []
        part_cap = [False]

        def cover(acc, used):
            if len(partitions) >= 20000:
                part_cap[0] = True
                return
            if acc == g.full:
                partitions.append(sorted(used))
                return
            rest = g.full & ~acc
            lowbit = rest & -rest
            for i in mins:
                if evs[i] & lowbit and not (evs[i] & acc):
                    cover(acc | evs[i], used + [i])
        cover(0, [])
        sameside = {}
        for side, (qa, qb) in (("q0q1", (g.qmask[0], g.qmask[1])),
                               ("r0r1", (g.rmask[0], g.rmask[1]))):
            quads = [qa & qb, qa & ~qb & g.full, ~qa & g.full & qb,
                     ~qa & g.full & ~qb & g.full]
            present = []
            for t in range(16):
                m = 0
                for k2 in range(4):
                    if t >> k2 & 1:
                        m |= quads[k2]
                if m in idx:
                    present.append(t)
            sameside[side] = {
                "represented_joint_boolean_cylinder_count": len(present),
                "only_marginals": set(present) <= {0, 15, 3, 12, 5, 10},
            }
        relation = sorted({
            sig_aqr(s)[0] + (sig_aqr(s)[1], sig_aqr(s)[2])
            for s in g.states})
        expected = sorted(set(product((0, 1), repeat=5))
                          - {(1, 1, 1, 1, 0), (1, 1, 1, 0, 1)})
        both = [p for p in PROFILES
                if any(pr[0] == (1, 1, 1) and pr[1] == (1, 1, 1)
                       and pr[2:] == p
                       for pr, _, _, _, _ in g.blocks)]
        layers = []
        for step in path:
            w = int(step["trace_word"], 16)
            supp = trace_support(w)
            layers.append({"trace_word": step["trace_word"],
                           "support": supp,
                           "support_arity": len(supp),
                           "closure_added": step["closure_added"]})
        self.branch_count += 1
        self.branches.append({
            "path": path, "outcome": "oml_completion",
            "depth": depth, "events": n,
            "lattice": ok, "orthomodular": oml,
            "centre_size": len(centre),
            "centre_labels": [g.label(evs[i]) for i in centre],
            "cell_sub_oml_faithful": faithful,
            "maximal_block_count": len(partitions),
            "maximal_block_enumeration_capped": part_cap[0],
            "minimal_event_count": len(mins),
            "same_side": {k: {kk: (sorted(vv) if isinstance(vv, set) else vv)
                              for kk, vv in v.items()}
                          for k, v in sameside.items()},
            "cell_relation_is_30_profiles": relation == expected,
            "both_rows_activated_profiles": ["".join(map(str, p))
                                             for p in both],
            "activation_cylinder_is_event": {
                row: (g.act[row] in idx) for row in ("row0", "row1", "both")},
            "every_nonzero_event_off_cylinder": all(
                (e & ~g.act[row] & g.full) for e in evs if e
                for row in ("row0", "row1")),
            "r0_r1_distinct": g.rmask[0] != g.rmask[1],
            "q0_q1_distinct": g.qmask[0] != g.qmask[1],
            "repair_layers": layers,
            "family_sha256": hashlib.sha256(
                ("\n".join(digest(e, g.npts) for e in sorted(evs)))
                .encode()).hexdigest(),
        })


def trace_support(w):
    """Coordinates of (q0,q1,r0,r1) on which a 16-bit profile trace depends."""
    supp = []
    for c in range(4):
        dep = False
        for i, p in enumerate(PROFILES):
            q = list(p)
            q[c] ^= 1
            j = PROFILES.index(tuple(q))
            if (w >> i & 1) != (w >> j & 1):
                dep = True
        if dep:
            supp.append(("q0", "q1", "r0", "r1")[c])
    return supp


# ----------------------------------------------------------------------
# section 4: stripped 16-point exhaustive classification
# ----------------------------------------------------------------------

def core16():
    import numpy as np
    FULL16 = (1 << 16) - 1
    IDX16 = np.arange(65536, dtype=np.uint32)
    POP = np.array([bin(i).count("1") for i in range(65536)], dtype=np.uint8)

    def mask16(pred):
        return sum(1 << j for j in range(16)
                   if pred((j >> 3) & 1, (j >> 2) & 1, (j >> 1) & 1, j & 1))

    def raw16():
        out = {0, FULL16}
        for a in (0, 1):
            for i in (0, 1):
                for al in range(16):
                    out.add(mask16(
                        lambda q0, q1, r0, r1, a=a, i=i, al=al:
                        bool(al & (1 << (2 * (q0, q1)[a] + (r0, r1)[i])))))
        return frozenset(out)

    def close16(seed):
        ev = set(seed)
        while True:
            arr = np.fromiter(ev, dtype=np.uint32, count=len(ev))
            comp = np.bitwise_xor(np.uint32(FULL16), arr)
            cand = set(comp.tolist())
            step = 4096
            for lo in range(0, len(arr), step):
                blockv = arr[lo:lo + step]
                u = blockv[:, None] | arr[None, :]
                d = (blockv[:, None] & arr[None, :]) == 0
                cand |= set(u[d].tolist())
            new = cand - ev
            if not new:
                return frozenset(ev)
            ev |= new

    def tables16(ev):
        isev = np.zeros(65536, dtype=bool)
        arr = np.fromiter(ev, dtype=np.uint32, count=len(ev))
        isev[arr] = True
        ceil = np.where(isev, IDX16, np.uint32(FULL16)).astype(np.uint32)
        floor = np.where(isev, IDX16, np.uint32(0)).astype(np.uint32)
        for b in range(16):
            bit = 1 << b
            sub = IDX16[(IDX16 & bit) == 0]
            sup = sub | bit
            ceil[sub] &= ceil[sup]
            floor[sup] |= floor[sub]
        return isev, np.sort(arr), ceil, floor

    def fail_lowers(isev, arr, ceil):
        lowers = set()
        step = 4096
        comp = np.bitwise_xor(np.uint32(FULL16), arr)
        for base in (arr, comp):
            for lo in range(0, len(base), step):
                blockv = base[lo:lo + step]
                u = (blockv[:, None] | base[None, :]).ravel()
                bad = ~isev[ceil[u]]
                lowers |= set(u[bad].tolist())
        return lowers

    state = {"nodes": 0, "capped": False, "terminals": {}, "tree": []}
    memo = set()

    def search(ev, depth, node_path):
        if ev in memo:
            return "memo"
        memo.add(ev)
        state["nodes"] += 1
        my_id = state["nodes"]
        if state["nodes"] > CAP_CORE16_NODES:
            state["capped"] = True
            return "cap"
        isev, arr, ceil, floor = tables16(ev)
        fails = fail_lowers(isev, arr, ceil)
        rec = {"id": my_id, "depth": depth, "events": len(ev),
               "path_choices_hex": list(node_path),
               "fail_lower_count": len(fails)}
        state["tree"].append(rec)
        if not fails:
            if ev not in state["terminals"]:
                state["terminals"][ev] = {"first_seen_node": my_id}
            rec["outcome"] = "terminal"
            return "terminal"
        best = None
        for low in sorted(fails):
            upv = int(ceil[low])
            gap = upv & ~low & FULL16
            gn = int(POP[gap])
            key = (gn, low, gap)
            if best is None or key < best:
                best = key
                if gn == 0:
                    break
        gn, low, gap = best
        rec["chosen_lower_hex"] = hex(low)
        rec["chosen_upper_hex"] = hex(low | gap)
        rec["gap_bits"] = gn
        rec["children"] = []
        gb = [b for b in range(16) if gap >> b & 1]
        for s in range(1 << gn):
            z = low
            for t, b in enumerate(gb):
                if s >> t & 1:
                    z |= 1 << b
            rec["children"].append(hex(z))
            search(close16(ev | {z, FULL16 ^ z}), depth + 1,
                   node_path + [hex(z)])
        return "internal"

    raw = raw16()
    ev0 = close16(raw)
    isev, arr, ceil, floor = tables16(ev0)
    init_fails = fail_lowers(isev, arr, ceil)
    # canonical first pair analysis (rectangle necessity, finite core)
    low0 = min(init_fails, key=lambda low: (int(POP[int(ceil[low]) & ~low
                                                    & FULL16]), low))
    up0 = int(ceil[low0])
    gap0 = up0 & ~low0 & FULL16
    cands = []
    gb = [b for b in range(16) if gap0 >> b & 1]
    for s in range(1 << len(gb)):
        z = low0
        for t, b in enumerate(gb):
            if s >> t & 1:
                z |= 1 << b
        cands.append(z)

    def support16(z):
        supp = []
        for c in range(4):
            bit = 1 << (3 - c)
            if any(bool(z >> j & 1) != bool(z >> (j ^ bit) & 1)
                   for j in range(16)):
                supp.append(("q0", "q1", "r0", "r1")[c])
        return supp

    search(ev0, 0, [])

    QUAD = {}
    for ci, cj, nm in ((3, 2, "q0q1"), (1, 0, "r0r1"), (3, 1, "q0r0"),
                       (3, 0, "q0r1"), (2, 1, "q1r0"), (2, 0, "q1r1")):
        QUAD[nm] = [sum(1 << j for j in range(16)
                        if (j >> ci & 1) == u and (j >> cj & 1) == v)
                    for u in (0, 1) for v in (0, 1)]

    def isclosed(fam):
        arr2 = np.fromiter(fam, dtype=np.uint32, count=len(fam))
        isev2 = np.zeros(65536, dtype=bool)
        isev2[arr2] = True
        if not isev2[np.bitwise_xor(np.uint32(FULL16), arr2)].all():
            return False
        step = 2048
        for lo in range(0, len(arr2), step):
            blockv = arr2[lo:lo + step]
            d = (blockv[:, None] & arr2[None, :]) == 0
            u = (blockv[:, None] | arr2[None, :])[d]
            if not isev2[u].all():
                return False
        return True

    def islattice(fam):
        isev2, arr2, ceil2, floor2 = tables16(fam)
        return not fail_lowers(isev2, arr2, ceil2)

    def om_check(fam):
        """Explicit orthomodular-law check (chunked)."""
        isev2, arr2, ceil2, floor2 = tables16(fam)
        step = 1024
        for lo in range(0, len(arr2), step):
            X = arr2[lo:lo + step]
            for lo2 in range(0, len(arr2), step):
                Y = arr2[lo2:lo2 + step]
                pairs = (X[:, None] & Y[None, :]) == X[:, None]
                xs, ys = np.nonzero(pairs)
                if not len(xs):
                    continue
                xv = X[xs].astype(np.uint32)
                yv = Y[ys].astype(np.uint32)
                m = floor2[yv & np.bitwise_xor(np.uint32(FULL16), xv)]
                if not isev2[m].all():
                    return False
                j = np.bitwise_xor(
                    np.uint32(FULL16),
                    floor2[np.bitwise_xor(np.uint32(FULL16), xv | m)])
                if not (isev2[j].all() and (j == yv).all()):
                    return False
        return True

    def classify(fam):
        eset = fam
        out = {}
        for nm2, atoms in QUAD.items():
            out["reconstructs_" + nm2] = all(a in eset for a in atoms)
            combos = set()
            for t in range(16):
                m = 0
                for k in range(4):
                    if t >> k & 1:
                        m |= atoms[k]
                combos.add(m)
            marg = {0, FULL16, atoms[0] | atoms[1], atoms[2] | atoms[3],
                    atoms[0] | atoms[2], atoms[1] | atoms[3]}
            out["nontrivial_measurable_" + nm2] = sorted(
                hex(m) for m in combos if m in eset and m not in marg)
        out["four_coordinate_event_count"] = sum(
            1 for z in fam if len(support16(z)) == 4)
        out["singleton_count"] = sum(1 for j in range(16)
                                     if (1 << j) in eset)
        return out

    def normal_form_T(fam, hub):
        """Check fam == direct sum over hub-quadrants of the 4-point
        MO2 on the other two coordinates.  hub in ('q','r')."""
        if hub == "q":
            hubatoms = QUAD["q0q1"]
            others = (1, 0)     # r0 bit index 1, r1 bit index 0
        else:
            hubatoms = QUAD["r0r1"]
            others = (3, 2)
        per_quadrant = []
        for a in hubatoms:
            opts = {0, a}
            for c in others:
                m0 = sum(1 << j for j in range(16)
                         if (a >> j & 1) and (j >> c & 1) == 0)
                opts |= {m0, a ^ m0}
            per_quadrant.append(sorted(opts))
        expect = set()
        for combo in product(*per_quadrant):
            expect.add(combo[0] | combo[1] | combo[2] | combo[3])
        return frozenset(expect) == fam

    terms = sorted(state["terminals"],
                   key=lambda f: (len(f), sorted(f)))
    term_data = []
    for i, fam in enumerate(terms):
        cls = classify(fam)
        small = len(fam) <= 9216
        term_data.append({
            "terminal_id": i,
            "events": len(fam),
            "family_sha256": hashlib.sha256(
                ",".join(str(z) for z in sorted(fam)).encode()).hexdigest(),
            "family_hex": [hex(z) for z in sorted(fam)],
            "complement_and_disjoint_union_closed": isclosed(fam),
            "lattice": islattice(fam),
            "orthomodular_check": ("explicit" if small else
                                   "lemma_L1_from_closed_plus_lattice"),
            "orthomodular": (om_check(fam) if small else True),
            "classification": cls,
            "normal_form_q_hub_sum_of_MO2": normal_form_T(fam, "q"),
            "normal_form_r_hub_sum_of_MO2": normal_form_T(fam, "r"),
        })
    fams = terms
    inclusions = [[i, j] for i, a in enumerate(fams)
                  for j, b in enumerate(fams) if i != j and a < b]
    minimal_terms = [i for i in range(len(fams))
                     if not any(j != i and fams[j] < fams[i]
                                for j in range(len(fams)))]
    every_terminal_reconstructs_same_side = all(
        d["classification"]["reconstructs_q0q1"]
        or d["classification"]["reconstructs_r0r1"] for d in term_data)
    every_terminal_contains_a_minimal = all(
        any(fams[m] <= fams[i] for m in minimal_terms)
        for i in range(len(fams)))
    return {
        "points": 16,
        "raw_events": len(raw),
        "initial_closure_events": len(ev0),
        "initial_fail_lower_count": len(init_fails),
        "canonical_first_lower_hex": hex(low0),
        "canonical_first_upper_hex": hex(up0),
        "canonical_interval_candidates_hex": [hex(z) for z in cands],
        "canonical_candidates_all_four_coordinate": all(
            len(support16(z)) == 4 for z in cands),
        "search_nodes": state["nodes"],
        "search_capped": state["capped"],
        "distinct_terminals": len(term_data),
        "terminals": term_data,
        "strict_inclusions": inclusions,
        "inclusion_minimal_terminals": minimal_terms,
        "every_terminal_reconstructs_a_same_side_boundary":
            every_terminal_reconstructs_same_side,
        "every_terminal_contains_an_inclusion_minimal_terminal":
            every_terminal_contains_a_minimal,
        "tree": state["tree"],
        "covering_theorem": (
            "By Lemma L2 with all-subset candidate intervals, every "
            "concrete-logic OML completion of the four edge algebras inside "
            "P(16) contains one of the terminal families listed here; every "
            "terminal reconstructs Bool(q0,q1) or Bool(r0,r1) in full, and "
            "the two inclusion-minimal terminals are the q-hub and r-hub "
            "Boolean sums of four 4-point MO2 fibres."),
        "scope": ("exhaustive over ALL subsets of each admissible interval "
                  "on the 16-point carrier; concrete-logic semantics "
                  "(complement/disjoint-union closed, order = inclusion); "
                  "no arbitrary-grid or infinite promotion"),
    }


# ----------------------------------------------------------------------
# section 5: emit / verify
# ----------------------------------------------------------------------

def canonical(p):
    return json.dumps(p, sort_keys=True, indent=1) + "\n"


def wrap(payload):
    return {"schema": SCHEMA, "emitted": EMIT_DATE,
            "generator": os.path.basename(__file__),
            "payload_sha256": hashlib.sha256(
                canonical(payload).encode()).hexdigest(),
            "payload": payload}


def emit(path, payload, do_emit):
    rec = wrap(payload)
    if do_emit:
        with open(path, "w") as f:
            f.write(canonical(rec))
        print("wrote", path, flush=True)
    else:
        with open(path) as f:
            got = json.load(f)
        assert got == rec, "MISMATCH %s" % path
        print("MATCH", path, flush=True)


def stage_witnesses(g, do_emit):
    jf, mf, meets_ok, pairs, _ = census(g)
    sym = symmetry_check(g)
    orbits = {}
    for p in pairs:
        key = pair_orbit_key(p["x_label"], p["y_label"])
        orbits.setdefault(key, []).append(
            "|".join(sorted((p["x_label"], p["y_label"]))))
    payload = {
        "reproduction": {
            "carrier_points": g.npts,
            "macro_blocks": len(g.blocks),
            "cell_states": len(g.states),
            "raw_events": len(g.raw),
            "completed_events": len(g.ev0),
            "closure_rounds": g.rounds,
            "banked_receipt_first_failure_reproduced": {
                "x_sha256": digest(g.masks[((0, 1), "e01")], g.npts),
                "y_sha256": digest(g.masks[((1, 0), "e10")], g.npts),
                "u_sha256": digest(g.full ^ g.masks[((0, 0), "e11")],
                                   g.npts),
                "v_sha256": digest(g.full ^ g.masks[((1, 1), "e00")],
                                   g.npts),
            },
        },
        "join_failing_pairs": len(jf),
        "meet_failing_pairs": len(mf),
        "meet_failures_are_complement_images_of_join_failures": meets_ok,
        "all_pairs": pairs,
        "orbits_under_row_and_column_swap": {
            k: sorted(v) for k, v in sorted(orbits.items())},
        "symmetry_semantic_validation": sym,
        "scope": ("exhaustive over all unordered pairs of the 230-event "
                  "closed family; witnesses are structural point "
                  "descriptions independent of bit order"),
    }
    emit(os.path.join(HERE, "full_grid_2x2_rectangle_witnesses.json"),
         payload, do_emit)
    return payload


def stage_core16(do_emit):
    payload = core16()
    emit(os.path.join(HERE,
                      "full_grid_2x2_rectangle_core16_exhaustive.json"),
         payload, do_emit)
    return payload


def stage_cascade(g, do_emit):
    c = Cascade(g).run()
    outcomes = {}
    for b in c.branches:
        outcomes[b["outcome"]] = outcomes.get(b["outcome"], 0) + 1
    for i, b in enumerate(c.branches):
        emit(os.path.join(
            HERE, "full_grid_2x2_rectangle_branch_%03d.json" % i),
            b, do_emit)
    payload = {
        "candidate_class_K": (
            "unions of full (q0,q1,r0,r1) coordinate-profile cylinders z "
            "with x|y <= z <= AND of all current upper bounds; branching "
            "is over ALL such candidates for the failing pair with the "
            "fewest free profiles (deterministic tie-break)"),
        "monotone_certificates": [
            "nontrivial same-side ((q0,q1)- or (r0,r1)-) measurable event",
            "nonzero event inside a row activation cylinder",
            "failing pair with no K-candidate"],
        "caps": {"nodes": CAP_NODES, "family": CAP_FAMILY,
                 "depth": CAP_DEPTH},
        "nodes": c.nodes,
        "capped": c.capped,
        "branch_outcomes": outcomes,
        "tree": c.tree,
        "scope": ("exhaustive ONLY within class K; candidates outside K "
                  "(partial macro-block unions) are not enumerated; no "
                  "canonicality of the closure and no arbitrary-grid or "
                  "infinite promotion is claimed"),
    }
    emit(os.path.join(HERE, "full_grid_2x2_rectangle_cascade.json"),
         payload, do_emit)
    return payload, c


def stage_master(do_emit):
    files = sorted(fn for fn in os.listdir(HERE)
                   if fn.startswith("full_grid_2x2_rectangle_")
                   and fn.endswith(".json")
                   and fn != "full_grid_2x2_rectangle_master.json")
    payload = {
        "stages": ["witnesses", "core16", "cascade"],
        "files_sha256": {
            fn: hashlib.sha256(
                open(os.path.join(HERE, fn), "rb").read()).hexdigest()
            for fn in files},
        "scope": ("all finite searches are exhaustive only within their "
                  "precisely stated candidate classes (all interval "
                  "subsets on the 16-point core; class K on the full "
                  "carrier); no closure is claimed canonical; no promotion "
                  "of the 2x2 result to arbitrary grids"),
    }
    emit(os.path.join(HERE, "full_grid_2x2_rectangle_master.json"),
         payload, do_emit)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--stage", choices=("witnesses", "core16", "cascade",
                                        "master", "all"), default="all")
    args = ap.parse_args()
    g = None
    if args.stage in ("witnesses", "cascade", "all"):
        print("[build] constructing carrier ...", flush=True)
        g = Grid()
        assert g.npts == 6186568 and len(g.blocks) == 842
        assert len(g.raw) == 198 and len(g.ev0) == 230
        assert g.rounds[:1] == [32] and sum(g.rounds[1:]) == 0
    if args.stage in ("witnesses", "all"):
        stage_witnesses(g, args.emit)
    if args.stage in ("core16", "all"):
        stage_core16(args.emit)
    if args.stage in ("cascade", "all"):
        stage_cascade(g, args.emit)
    if args.stage in ("master", "all"):
        stage_master(args.emit)


if __name__ == "__main__":
    main()
