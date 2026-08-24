#!/usr/bin/env python3
"""Companion witness audit for the stage-558 same-side meet event.

Identifies the unique nontrivial same-side meet at the 558-event stage
(q0^c wedge q1), verifies its exact decomposition as the 0101 profile
fibre plus the fully-activated four-point second-repair block, dates its
birth stage, and identifies the two events whose hull gap is an event
while neither hull is.  Independence as in the main isolation audit.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import full_grid_stage558_hull_gap_isolation_audit as aud
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA = "full-grid-stage558-meet-witness-v1"

def main():
    (n, full, masks, profiles, blocks, base, stage1, stage2, stage3,
     joins) = aud.reconstruct()
    events = stage3
    fibre = dict(profiles)

    Q0 = masks[((0, 0), "e11")] | masks[((0, 0), "e10")]
    Q1 = masks[((1, 0), "e11")] | masks[((1, 0), "e10")]
    x, y = Q0, full ^ Q1
    ubs = [u for u in events if x & u == x and y & u == y]
    proper = [u for u in ubs if u != full]
    assert len(ubs) == 2 and len(proper) == 1
    u = proper[0]
    estar = full ^ u

    sel2 = None
    for a0, a1, p, off, size in blocks:
        if a0 == (1, 1, 1) and a1 == (1, 1, 0) and p == (0, 1, 0, 0):
            sel2 = ((1 << size) - 1) << off
    act = []
    for row in (0, 1):
        cm = full
        for a in grid.base.SHARED:
            cm &= masks[((row, 0), a)]
        act.append(cm)

    def birth(e):
        if e in base:
            return "base"
        if e in stage1:
            return "stage1"
        if e in stage2:
            return "stage2"
        return "stage3" if e in events else "absent"

    hull_only = []
    for e in sorted(events):
        if not e:
            continue
        interior, saturation, sp = aud.hulls(e, profiles)
        H = saturation & ~interior
        if (H in events and H
                and not (interior in events and saturation in events)):
            hull_only.append({
                "event_sha256": aud.sha(e, n),
                "points": e.bit_count(),
                "birth": birth(e),
                "split_fibres": [list(p) for p, _, _, _ in sp],
                "hull_gap_sha256": aud.sha(H, n),
                "interior_is_event": interior in events,
                "saturation_is_event": saturation in events})

    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "carrier_points": n,
        "pair": "q0 join with complement of q1 (side q, signs (1,0))",
        "upper_bounds_at_stage558": len(ubs),
        "proper_upper_bound_sha256": aud.sha(u, n),
        "proper_upper_bound_birth": birth(u),
        "meet_event": {
            "identity": "q0^c wedge q1 = complement of the unique proper "
                        "upper bound of (q0, q1^c)",
            "sha256": aud.sha(estar, n),
            "points": estar.bit_count(),
            "birth": birth(estar),
            "equals_fibre0101_disjoint_union_sel2":
                estar == fibre[(0, 1, 0, 1)] | sel2,
            "contains_whole_fibre_0101": fibre[(0, 1, 0, 1)] & ~estar == 0,
            "extra_part_is_second_repair_block":
                estar & ~fibre[(0, 1, 0, 1)] == sel2,
            "sel2_fully_activated_row0": sel2 & ~act[0] == 0,
            "activation_points": [(estar & act[0]).bit_count(),
                                  (estar & act[1]).bit_count()],
            "fibre0101_activation_free":
                (fibre[(0, 1, 0, 1)] & (act[0] | act[1])) == 0},
        "hull_gap_event_without_event_hulls": hull_only,
        "independence": "same shared components as the main isolation "
                        "audit (grid.build, repair selections); all checks "
                        "freshly computed",
        "scope": "one exact 558-event branch; witness identification only",
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_stage558_meet_witness_audit.py --emit")}
    out["producer_sha256"] = hashlib.sha256(
        open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out

if __name__ == "__main__":
    emit = "--emit" in sys.argv
    out = main()
    path = os.path.join(HERE, "full_grid_stage558_meet_witness.json")
    if emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2)
            f.write("\n")
    elif os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps(out, sort_keys=True, indent=2))
