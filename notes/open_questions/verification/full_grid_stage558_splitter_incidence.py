#!/usr/bin/env python3
"""Profile-splitter census for the certified 558-event fine-repair stage.

This is a discriminating Campaign-19 theorem-extraction test, not a fourth
repair.  It reconstructs the exact 230->256->492->558 branch, rechecks all
three selected joins at the final stage, classifies their fibre hulls, and
enumerates every join-failing pair among the final profile-measurable events.
"""
import argparse, collections, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import full_grid_2x2_conditional_cell_audit as grid
import full_grid_third_gap_classification as prior

SCHEMA = "full-grid-stage558-splitter-incidence-v1"

def sha(z, n):
    return hashlib.sha256(z.to_bytes((n + 7) // 8, "little")).hexdigest()

def build_stage3():
    states, n, full, masks, raw, labels, interfaces, macro = grid.build()
    base, _ = grid.closure(raw, full); base = set(base)
    x = masks[((0, 1), "e01")]; y = masks[((1, 0), "e10")]
    lo = x | y; primary = {}; offset = 0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0 == a1 == (1,1,0) and (q0,q1,r0,r1) in ((0,1,1,0),(1,0,0,1)):
            primary[(q0,q1,r0,r1)] = ((1 << size) - 1) << offset
        offset += size
    join1 = lo | primary[(0,1,1,0)] | primary[(1,0,0,1)]
    stage1, _ = grid.closure(base | {join1, full ^ join1}, full); stage1 = set(stage1)
    sx, sy, smu, sml = prior.failure(stage1); slo = sx | sy
    fixed = None; offset = 0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        if a0 == (1,1,1) and a1 == (1,1,0) and (q0,q1,r0,r1) == (0,1,0,0):
            fixed = ((1 << size) - 1) << offset
        offset += size
    assert fixed is not None and fixed.bit_count() == 4
    join2 = slo | fixed
    stage2, _ = grid.closure(stage1 | {join2, full ^ join2}, full); stage2 = set(stage2)
    tx, ty, tmu, tml = prior.failure(stage2); tlo = tx | ty; thi = full
    for u in tmu: thi &= u
    tgap = thi & ~tlo; selected = None; offset = 0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        segment = (tgap >> offset) & ((1 << size) - 1)
        if segment and segment.bit_count() == 2:
            assert selected is None
            selected = segment << offset
        offset += size
    assert selected is not None
    join3 = tlo | selected
    stage3, rounds = grid.closure(stage2 | {join3, full ^ join3}, full)
    assert len(stage3) == 558 and rounds == [4,4,34,22,0]
    return n, full, masks, macro, set(stage3), [(x,y,join1),(sx,sy,join2),(tx,ty,join3)]

def payload():
    n, full, masks, macro, events, joins = build_stage3()
    profiles = collections.defaultdict(int); offset = 0
    for a0,a1,q0,q1,r0,r1,ns,size in macro:
        profiles[(q0,q1,r0,r1)] |= ((1 << size) - 1) << offset
        offset += size
    assert len(profiles) == 16 and sum(z.bit_count() for z in profiles.values()) == n

    def hulls(e):
        interior = saturation = 0; split = []
        for p, f in sorted(profiles.items()):
            c = (e & f).bit_count()
            if c == f.bit_count(): interior |= f
            if c: saturation |= f
            if 0 < c < f.bit_count():
                split.append({"profile": list(p), "selected": c,
                              "fibre": f.bit_count(),
                              "trace_sha256": sha(e & f, n)})
        return interior, saturation, split

    selected = []
    for depth, (x,y,j) in enumerate(joins, 1):
        lower = x | y
        ub = [u for u in events if x | u == u and y | u == u]
        meet_ub = full
        for u in ub: meet_ub &= u
        interior, saturation, split = hulls(j)
        _, _, increment_split = hulls(j & ~lower)
        selected.append({
            "depth": depth, "join_sha256": sha(j,n),
            "operands_profile_measurable": all(
                all((e & f) in (0,f) for f in profiles.values())
                for e in (x,y)),
            "forced_lower_sha256": sha(lower,n),
            "repair_increment_sha256": sha(j & ~lower,n),
            "repair_increment_points": (j & ~lower).bit_count(),
            "repair_increment_split_fibres": increment_split,
            "join_still_least_at_stage558": meet_ub == j,
            "split_fibres": split,
            "fibre_interior_is_event": interior in events,
            "fibre_saturation_is_event": saturation in events,
            "hull_gap_is_event": (saturation & ~interior) in events,
            "interior_sha256": sha(interior,n),
            "saturation_sha256": sha(saturation,n)})

    profile_events = []
    for e in events:
        if all((e & f) in (0,f) for f in profiles.values()):
            profile_events.append(e)
    profile_events.sort()
    event_set = set(events); failures = []; hist = collections.Counter()
    for ia, x in enumerate(profile_events):
        for y in profile_events[ia+1:]:
            lower = x | y; upper = full; nub = 0
            for u in events:
                if lower | u == u:
                    upper &= u; nub += 1
            if upper in event_set:
                continue
            gap = upper & ~lower
            touched = []
            for p,f in sorted(profiles.items()):
                c = (gap & f).bit_count()
                if c:
                    touched.append((p,c,f.bit_count(), c == f.bit_count()))
            hist[(len(touched), sum(1 for z in touched if not z[3]))] += 1
            failures.append({
                "x_sha256": sha(x,n), "y_sha256": sha(y,n),
                "lower_sha256": sha(lower,n), "upper_sha256": sha(upper,n),
                "gap_sha256": sha(gap,n), "gap_points": gap.bit_count(),
                "current_upper_bounds": nub,
                "touched_profiles": [{"profile":list(p),"points":c,
                    "fibre_points":size,"whole":whole}
                    for p,c,size,whole in touched]})
    failures.sort(key=lambda r:(r["gap_points"],r["x_sha256"],r["y_sha256"]))
    failure_digest = hashlib.sha256(json.dumps(failures,sort_keys=True,
        separators=(",",":")).encode()).hexdigest()

    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "carrier_points": n, "stage_events": len(events),
        "profile_measurable_events": len(profile_events),
        "selected_join_hulls": selected,
        "all_selected_joins_remain_least": all(r["join_still_least_at_stage558"] for r in selected),
        "profile_pair_failures": len(failures),
        "failure_histogram": [{"touched_profiles":k[0],
            "properly_split_profiles":k[1],"pairs":v}
            for k,v in sorted(hist.items())],
        "first_failure": failures[0] if failures else None,
        "failures_sha256": failure_digest,
        "scope": "one exact 558-event branch; every pair of final profile-measurable events; no fourth repair, no orbit quotient, no arbitrary terminal theorem",
        "dependency_sha256": {
            os.path.basename(grid.__file__): hashlib.sha256(open(grid.__file__,"rb").read()).hexdigest(),
            os.path.basename(prior.__file__): hashlib.sha256(open(prior.__file__,"rb").read()).hexdigest()},
        "command": "python3 notes/open_questions/verification/full_grid_stage558_splitter_incidence.py --verify"}
    out["producer_sha256"] = hashlib.sha256(open(__file__,"rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(out,sort_keys=True,
        separators=(",",":")).encode()).hexdigest()
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--emit",action="store_true"); ap.add_argument("--verify",action="store_true"); args=ap.parse_args()
    out=payload(); path=os.path.join(HERE,"full_grid_stage558_splitter_incidence.json")
    if args.emit:
        with open(path,"w") as f: json.dump(out,f,sort_keys=True,indent=2); f.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],
        "profile_pair_failures":out["profile_pair_failures"]},sort_keys=True,indent=2))

if __name__ == "__main__": main()
