#!/usr/bin/env python3
"""Independent audit of period-two relay bitset semantics.

This deliberately reimplements the fixed points used by relay7_core rather
than calling analyze().  It exhausts p=2,k=1 and checks a deterministic mix
of valid p=2,k=2 pairs.  The comparison includes E1[0], since phase-live is
an any-position union and is not a substitute for root-cell separation.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORE = HERE / "census_2026-07-12_s35"
sys.path.insert(0, str(CORE))
import relay7_core as rc  # noqa: E402


def union_image(rows, mask):
    """Relational image of a state bitmask under 29 successor rows."""
    out = 0
    while mask:
        bit = mask & -mask
        out |= rows[bit.bit_length() - 1]
        mask ^= bit
    return out


def independent(maps, target):
    """Independent monotone-bitset implementation of the rooted semantics."""
    rows = tuple(rc.succ_masks(port) for port in maps)
    p = len(rows)
    letter = tuple(int(target in state) for state in rc.STATES)
    z = sum(1 << s for s, x in enumerate(letter) if not x)
    o = rc.ALL ^ z

    # Greatest fixed point of zero-labelled infinite suffixes.
    e0 = [z] * p
    while True:
        nxt = []
        for phase in range(p):
            good_next = e0[(phase + 1) % p]
            nxt.append(sum(1 << s for s in range(rc.NS)
                           if (z >> s) & 1 and rows[phase][s] & good_next))
        if nxt == e0:
            break
        e0 = nxt

    # Least fixed point: suffix contains exactly one target-one state.
    e1 = [0] * p
    while True:
        nxt = []
        for phase in range(p):
            q = (phase + 1) % p
            nxt.append(e1[phase] | sum(
                1 << s for s in range(rc.NS)
                if rows[phase][s] & (e0[q] if letter[s] else e1[q])))
        if nxt == e1:
            break
        e1 = nxt

    # Rooted prefix reachability, separated by number of ones seen.
    reach = [[0, 0] for _ in range(p)]
    reach[0] = [z, o]
    while True:
        nxt = [x[:] for x in reach]
        for phase in range(p):
            q = (phase + 1) % p
            im0 = union_image(rows[phase], reach[phase][0])
            im1 = union_image(rows[phase], reach[phase][1])
            nxt[q][0] |= im0 & z
            nxt[q][1] |= (im0 & o) | (im1 & z)
        if nxt == reach:
            break
        reach = nxt

    live = [0] * p
    for phase in range(p):
        q = (phase + 1) % p
        live[phase] = sum(
            1 << s for s in range(rc.NS)
            if (((reach[phase][0] >> s) & 1 and rows[phase][s] & e1[q]) or
                ((reach[phase][1] >> s) & 1 and rows[phase][s] & e0[q])))

    zr = [0] * p
    zr[0] = z
    while True:
        nxt = zr[:]
        for phase in range(p):
            nxt[(phase + 1) % p] |= union_image(rows[phase], zr[phase]) & z
        if nxt == zr:
            break
        zr = nxt
    free = [zr[r] & e0[r] for r in range(p)]
    return {"E0": e0, "E1": e1, "reach": reach, "live": live, "free": free}


def compare(maps, target):
    ref = rc.analyze(maps, target)
    got = independent(maps, target)
    for key in ("E0", "E1", "reach", "live", "free"):
        assert got[key] == ref[key], (key, maps, target, got[key], ref[key])


def screen_signature(result):
    face_free = tuple((x & rc.FACE) == rc.FACE for x in result["free"])
    face_nonlive = tuple(not bool(x & rc.FACE) for x in result["live"])
    false = tuple(rc.false_nonorders(x & rc.COMPLEMENT)
                  for x in result["live"])
    return face_free, face_nonlive, false


def main():
    targets = rc.COMMON_ZERO_TARGETS
    k1 = list(rc.two_cell_maps(1))
    compared_k1 = 0
    for a in k1:
        for b in k1:
            for target in targets:
                compare((a, b), target)
                compared_k1 += 1

    # Deterministic coverage: boundary ports plus random pairs drawn only from
    # the individually valid set that defines the 88,510,464-pair census.
    valid = [p for p in rc.two_cell_maps(2) if rc.window_girth_ok((p,), 2)]
    assert len(valid) == 9408
    rng = random.Random(3702)
    pairs = [(valid[0], valid[0]), (valid[0], valid[-1]),
             (valid[-1], valid[0]), (valid[-1], valid[-1])]
    pairs += [(rng.choice(valid), rng.choice(valid)) for _ in range(996)]
    for maps in pairs:
        for target in targets:
            compare(maps, target)

    # A screen computed from the independent masks must exactly match core.
    pass_mismatch = 0
    root_live_differences = 0
    for maps in pairs:
        for target in targets:
            got = independent(maps, target)
            ff, fn, no = screen_signature(got)
            passes = all(ff) and all(fn) and not any(no)
            if passes != rc.screen(maps, target)["passes"]:
                pass_mismatch += 1
            root_live_differences += got["E1"][0] != got["live"][0]

    print(f"p2_k1_map_target_comparisons={compared_k1}")
    print(f"p2_k2_individually_valid_ports={len(valid)}")
    print(f"p2_k2_sample_pairs={len(pairs)}")
    print(f"p2_k2_map_target_comparisons={len(pairs) * len(targets)}")
    print(f"screen_pass_mismatches={pass_mismatch}")
    print(f"sample_E1root_vs_live0_differences={root_live_differences}")
    print("SAFE: bucketing is exact only when the complete ordered successor "
          "row tuple (or a proved sufficient derived signature) is retained")
    print("UNSAFE: phase swap under rooted phase-zero semantics")
    print("MANDATORY: audit E1[0] separately from any-position live[0]")


if __name__ == "__main__":
    main()
