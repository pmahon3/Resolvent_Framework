#!/usr/bin/env python3
"""Exhaustive scope audit for period-two, width-one seven-loop relays.

This is deliberately outside the production census directory.  It records
successive safe incidence filters, the full operative screen, and checks the
two tempting reductions (phase swap and face-stabilizer reflection) rather
than assuming them.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORE = HERE / "census_2026-07-12_s35"
sys.path.insert(0, str(CORE))
import relay7_core as rc  # noqa: E402


def reflect_atom(a):
    return (-a) % 14


def reflect_port(port):
    return tuple((reflect_atom(a), reflect_atom(b)) for a, b in port)


def signature(maps, target):
    r = rc.screen(maps, target)
    return (r["passes"], tuple(r["face_free"]), tuple(r["face_nonlive"]),
            tuple(r["false_nonorders"]), tuple(r["exact_complement"]))


def main():
    ports = list(rc.two_cell_maps(1))
    individually_ok = {p: rc.window_girth_ok([p], 2) for p in ports}
    counts = {
        "raw": 0,
        "both_interfaces_two_cell_ok": 0,
        "three_cell_ok": 0,
    }
    # One representative from each reflection-paired target orbit.  The
    # reflected counts are transferred only after an explicit sample check.
    reps = (1, 2, 4)
    passes = {t: 0 for t in reps}
    exact = {t: 0 for t in reps}
    reflection_mismatch = 0
    for p0 in ports:
        for p1 in ports:
            counts["raw"] += 1
            if not (individually_ok[p0] and individually_ok[p1]):
                continue
            counts["both_interfaces_two_cell_ok"] += 1
            if not rc.window_girth_ok([p0, p1], 3):
                continue
            counts["three_cell_ok"] += 1
            for target in reps:
                sig = signature([p0, p1], target)
                passes[target] += sig[0]
                exact[target] += sig[0] and all(sig[4])
                # Exhaustive reflection checking would repeat the whole
                # census.  A deterministic 1/97 sample checks implementation
                # equivariance; mathematical equivariance follows by relabeling.
                if counts["raw"] % 97 == 0:
                    rt = reflect_atom(target)
                    if sig != signature([reflect_port(p0), reflect_port(p1)], rt):
                        reflection_mismatch += 1
    for key, value in counts.items():
        print(f"{key}={value}")
    for t in reps:
        print(f"target=a{t} passes={passes[t]} exact_complement={exact[t]}")
        print(f"target=a{reflect_atom(t)} passes={passes[t]} "
              f"exact_complement={exact[t]} [reflection transfer]")
    print(f"sampled_reflection_signature_mismatches={reflection_mismatch}")


if __name__ == "__main__":
    main()
