#!/usr/bin/env python3
"""Independent hull-gap / splitter-incidence audit of the 558-event stage.

Campaign 20 theorem-extraction computation.  No fourth repair is added.

INDEPENDENCE STATEMENT.  Freshly implemented here: closure, order tables
(subset test `x & y == x` instead of `x | y == y`), first-failure scan,
the profile-pair failure census, fibre hulls, and every new census
(all-event hull census, isolation-target checks, rule tests, same-side
residue probe, provenance decomposition, per-fibre trace counts).
SHARED with the banked producers, unavoidably: the carrier/mask
construction `full_grid_2x2_conditional_cell_audit.build` (it *defines*
the object), the three repair-selection descriptions (branch data), the
sorted-bitset first-failure scan convention (branch-defining), Python
big-integer arithmetic, and the banked JSON record format where byte
equality of digests is being checked.
"""
import collections, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import full_grid_2x2_conditional_cell_audit as grid

SCHEMA = "full-grid-stage558-hull-gap-isolation-v1"

def log(*a):
    print(*a, file=sys.stderr, flush=True)

def sha(z, n):
    return hashlib.sha256(z.to_bytes((n + 7) // 8, "little")).hexdigest()

def bits(b):
    while b:
        low = b & -b
        yield low.bit_length() - 1
        b ^= low

# ---------- fresh closure ----------
def closure(seed, full):
    ev = set(seed) | {0, full}
    rounds = []
    while True:
        fresh = set()
        for e in ev:
            c = full ^ e
            if c not in ev:
                fresh.add(c)
        evl = sorted(ev)
        for i, x in enumerate(evl):
            for y in evl[i + 1:]:
                if not x & y:
                    u = x | y
                    if u not in ev:
                        fresh.add(u)
        rounds.append(len(fresh))
        if not fresh:
            return ev, rounds
        ev |= fresh

# ---------- fresh order tables ----------
def order_masks(evl):
    m = len(evl)
    up = [0] * m
    for i, x in enumerate(evl):
        b = 0
        for j, y in enumerate(evl):
            if x & y == x:
                b |= 1 << j
        up[i] = b
    down = [0] * m
    for k in range(m):
        b = up[k]
        for j in bits(b):
            down[j] |= 1 << k
    return up, down

def extrema(evl, up, down, i, j):
    U = up[i] & up[j]
    L = down[i] & down[j]
    mu = [k for k in bits(U) if down[k] & U == 1 << k]
    ml = [k for k in bits(L) if up[k] & L == 1 << k]
    return U, L, mu, ml

def first_failure(evl, up, down):
    m = len(evl)
    for i in range(m):
        for j in range(i, m):
            _, _, mu, ml = extrema(evl, up, down, i, j)
            if len(mu) != 1 or len(ml) != 1:
                return i, j, mu, ml
    return None

# ---------- chain reconstruction ----------
def reconstruct():
    log("build()...")
    states, n, full, masks, raw, labels, interfaces, macro = grid.build()
    log("carrier bits:", n)
    base, rounds0 = closure(raw, full)
    assert len(base) == 230, len(base)
    log("base events:", len(base))

    profiles = collections.defaultdict(int)
    offset = 0
    blocks = []
    for a0, a1, q0, q1, r0, r1, ns, size in macro:
        profiles[(q0, q1, r0, r1)] |= ((1 << size) - 1) << offset
        blocks.append((a0, a1, (q0, q1, r0, r1), offset, size))
        offset += size
    assert len(profiles) == 16
    assert sum(f.bit_count() for f in profiles.values()) == n

    # cut 1: the displayed crossed pair (branch data).
    x = masks[((0, 1), "e01")]
    y = masks[((1, 0), "e10")]
    ubs = [u for u in base if x & u == x and y & u == y]
    W = full
    for u in ubs:
        W &= u
    gap1 = W & ~(x | y)
    assert gap1 == profiles[(0, 1, 1, 0)] | profiles[(1, 0, 0, 1)]
    assert gap1.bit_count() == 672800
    sel1 = 0
    for a0, a1, p, off, size in blocks:
        if a0 == a1 == (1, 1, 0) and p in ((0, 1, 1, 0), (1, 0, 0, 1)):
            sel1 |= ((1 << size) - 1) << off
    assert sel1.bit_count() == 128 and sel1 & ~gap1 == 0
    join1 = x | y | sel1
    stage1, _ = closure(base | {join1, full ^ join1}, full)
    assert len(stage1) == 256, len(stage1)
    log("stage1 events:", len(stage1))

    ev1 = sorted(stage1)
    up1, down1 = order_masks(ev1)
    i1, j1, mu1, _ = first_failure(ev1, up1, down1)
    sx, sy = ev1[i1], ev1[j1]
    W2 = full
    for k in mu1:
        W2 &= ev1[k]
    gap2 = W2 & ~(sx | sy)
    assert gap2.bit_count() == 677840
    sel2 = None
    for a0, a1, p, off, size in blocks:
        if a0 == (1, 1, 1) and a1 == (1, 1, 0) and p == (0, 1, 0, 0):
            sel2 = ((1 << size) - 1) << off
            assert size == 4
    assert sel2 is not None and sel2 & ~gap2 == 0
    join2 = sx | sy | sel2
    stage2, _ = closure(stage1 | {join2, full ^ join2}, full)
    assert len(stage2) == 492, len(stage2)
    log("stage2 events:", len(stage2))

    ev2 = sorted(stage2)
    up2, down2 = order_masks(ev2)
    i2, j2, mu2, _ = first_failure(ev2, up2, down2)
    tx, ty = ev2[i2], ev2[j2]
    W3 = full
    for k in mu2:
        W3 &= ev2[k]
    gap3 = W3 & ~(tx | ty)
    assert gap3.bit_count() == 1666232
    sel3 = None
    for a0, a1, p, off, size in blocks:
        seg = (gap3 >> off) & ((1 << size) - 1)
        if seg and seg.bit_count() == 2:
            assert sel3 is None
            sel3 = seg << off
    assert sel3 is not None
    join3 = (tx | ty) | sel3
    stage3, rounds3 = closure(stage2 | {join3, full ^ join3}, full)
    assert len(stage3) == 558, len(stage3)
    assert rounds3 == [4, 4, 34, 22, 0], rounds3
    log("stage3 events:", len(stage3), "rounds:", rounds3)

    joins = [(x, y, join1), (sx, sy, join2), (tx, ty, join3)]
    return (n, full, masks, profiles, blocks, base, stage1, stage2, stage3,
            joins)

# ---------- hulls ----------
def hulls(e, profiles):
    interior = saturation = 0
    split = []
    for p, f in sorted(profiles.items()):
        c = (e & f).bit_count()
        if c == f.bit_count():
            interior |= f
        if c:
            saturation |= f
        if 0 < c < f.bit_count():
            split.append((p, c, f.bit_count(), e & f))
    return interior, saturation, split

def main():
    (n, full, masks, profiles, blocks, base, stage1, stage2, stage3,
     joins) = reconstruct()
    events = stage3
    evl = sorted(events)
    idx = {e: i for i, e in enumerate(evl)}
    log("order tables at 558...")
    up, down = order_masks(evl)

    plist = sorted(profiles)
    fibre = {p: profiles[p] for p in plist}

    # same-side literals and macro cylinders.
    Q0 = masks[((0, 0), "e11")] | masks[((0, 0), "e10")]
    Q1 = masks[((1, 0), "e11")] | masks[((1, 0), "e10")]
    R0 = masks[((0, 0), "e11")] | masks[((0, 0), "e01")]
    R1 = masks[((0, 1), "e11")] | masks[((0, 1), "e01")]
    lit = {("q", 0): Q0, ("q", 1): Q1, ("r", 0): R0, ("r", 1): R1}
    for (s, i), e in lit.items():
        want = 0
        for p in plist:
            if p[i if s == "q" else 2 + i] == 1:
                want |= fibre[p]
        assert e == want, (s, i)
        assert e in events
    cyl = {}
    for s in ("q", "r"):
        for c in (0, 1):
            for d in (0, 1):
                m0 = lit[(s, 0)] if c else full ^ lit[(s, 0)]
                m1 = lit[(s, 1)] if d else full ^ lit[(s, 1)]
                cyl[(s, c, d)] = m0 & m1
    act = []
    for row in (0, 1):
        cm = full
        for a in grid.base.SHARED:
            cm &= masks[((row, 0), a)]
        act.append(cm)

    # ---------- selected joins: hulls, increments, provenance ----------
    def split_records(e):
        _, _, sp = hulls(e, profiles)
        return [{"profile": list(p), "selected": c, "fibre": fb,
                 "trace_sha256": sha(t, n)} for p, c, fb, t in sp]

    selected = []
    join_traces = []
    for depth, (jx, jy, j) in enumerate(joins, 1):
        lower = jx | jy
        U = up[idx[jx]] & up[idx[jy]]
        meet_ub = full
        for k in bits(U):
            meet_ub &= evl[k]
        interior, saturation, sp = hulls(j, profiles)
        inc = j & ~lower
        _, _, spinc = hulls(inc, profiles)
        _, _, splow = hulls(lower, profiles)
        low_split = {p for p, _, _, _ in splow}
        j_split = {p for p, _, _, _ in sp}
        inc_split = {p for p, _, _, _ in spinc}
        introduced = sorted(p for p in j_split
                            if fibre[p] & lower in (0, fibre[p]))
        join_traces.append({p: j & fibre[p] for p in plist})
        selected.append({
            "depth": depth,
            "join_sha256": sha(j, n),
            "operands_profile_measurable": all(
                all(e & f in (0, f) for f in fibre.values())
                for e in (jx, jy)),
            "forced_lower_sha256": sha(lower, n),
            "forced_lower_is_event": lower in events,
            "repair_increment_sha256": sha(inc, n),
            "repair_increment_points": inc.bit_count(),
            "repair_increment_split_fibres": [list(p) for p in inc_split],
            "join_split_fibres": [list(p) for p in sorted(j_split)],
            "lower_split_fibres": [list(p) for p in sorted(low_split)],
            "fibres_newly_split_by_increment": [list(p) for p in introduced],
            "fibres_inherited_from_lower": [list(p)
                                            for p in sorted(j_split
                                                            & low_split)],
            "join_still_least_at_stage558": meet_ub == j,
            "split_fibres": split_records(j),
            "fibre_interior_is_event": interior in events,
            "fibre_saturation_is_event": saturation in events,
            "hull_gap_is_event": (saturation & ~interior) in events,
            "interior_sha256": sha(interior, n),
            "saturation_sha256": sha(saturation, n)})

    def birth(e):
        if e in base:
            return "base"
        if e in stage1:
            return "stage1"
        if e in stage2:
            return "stage2"
        return "stage3"

    M = [jx | jy for jx, jy, _ in joins]
    Rinc = [j & ~m for (_, _, j), m in zip(joins, M)]
    prov = {
        "cut_operand_birth_stages": [[birth(jx), birth(jy)]
                                     for jx, jy, _ in joins],
        "increment_in_later_forced_lower": {
            "R1_subset_M2": Rinc[0] & ~M[1] == 0,
            "R1_subset_M3": Rinc[0] & ~M[2] == 0,
            "R2_subset_M3": Rinc[1] & ~M[2] == 0,
            "join1_subset_M2": joins[0][2] & ~M[1] == 0,
            "join1_subset_M3": joins[0][2] & ~M[2] == 0,
            "join2_subset_M3": joins[1][2] & ~M[2] == 0},
        "trace_refinement": []}
    for p in plist:
        t = [jt[p] for jt in join_traces]
        if any(0 < z.bit_count() < fibre[p].bit_count() for z in t):
            rel = {}
            for a in range(3):
                for b in range(a + 1, 3):
                    key = f"join{a+1}_vs_join{b+1}"
                    if t[a] == t[b]:
                        rel[key] = "equal"
                    elif t[a] & ~t[b] == 0:
                        rel[key] = "refines_into"
                    elif t[b] & ~t[a] == 0:
                        rel[key] = "contains"
                    else:
                        rel[key] = "incomparable"
            prov["trace_refinement"].append(
                {"profile": list(p),
                 "trace_points": [z.bit_count() for z in t],
                 "relations": rel})

    # ---------- profile-measurable pair failure census ----------
    log("profile pair census...")
    pm = [e for e in evl
          if all(e & f in (0, f) for f in fibre.values())]
    failures = []
    hist = collections.Counter()
    act_gap_pairs = 0
    for a_i, xx in enumerate(pm):
        for yy in pm[a_i + 1:]:
            U = up[idx[xx]] & up[idx[yy]]
            mu = [k for k in bits(U) if down[k] & U == 1 << k]
            Wp = full
            for k in mu:
                Wp &= evl[k]
            in_ev = Wp in events
            assert in_ev == (len(mu) == 1)
            if in_ev:
                continue
            lower = xx | yy
            gap = Wp & ~lower
            touched = []
            for p, f in sorted(profiles.items()):
                c = (gap & f).bit_count()
                if c:
                    touched.append((p, c, f.bit_count(),
                                    c == f.bit_count()))
            hist[(len(touched), sum(1 for z in touched if not z[3]))] += 1
            if gap & (act[0] | act[1]):
                act_gap_pairs += 1
            failures.append({
                "x_sha256": sha(xx, n), "y_sha256": sha(yy, n),
                "lower_sha256": sha(lower, n), "upper_sha256": sha(Wp, n),
                "gap_sha256": sha(gap, n), "gap_points": gap.bit_count(),
                "current_upper_bounds": U.bit_count(),
                "touched_profiles": [{"profile": list(p), "points": c,
                                      "fibre_points": size, "whole": whole}
                                     for p, c, size, whole in touched]})
    failures.sort(key=lambda r: (r["gap_points"], r["x_sha256"],
                                 r["y_sha256"]))
    failure_digest = hashlib.sha256(json.dumps(
        failures, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    # ---------- all-event hull census ----------
    log("all-event hull census...")
    flag_hist = collections.Counter()
    edge_info = {}
    hull_gap_events = {}
    sigma_sets = set()
    trace_shas = {p: set() for p in plist}
    fibre_events = {p: fibre[p] in events for p in plist}
    subfibre_counts = {p: 0 for p in plist}
    for e in evl:
        if not e:
            continue
        interior, saturation, sp = hulls(e, profiles)
        sig = tuple(sorted(p for p, _, _, _ in sp))
        i_ev = interior in events
        s_ev = saturation in events
        H = saturation & ~interior
        g_ev = H in events
        flag_hist[(i_ev, s_ev, g_ev, len(sig))] += 1
        if sig:
            sigma_sets.add(sig)
            if g_ev and H:
                hull_gap_events[H] = sig
                key = json.dumps([list(p) for p in sig])
                rec = edge_info.setdefault(key, {"events": 0,
                                                 "hull_gap_sha256": sha(H, n),
                                                 "hull_gap_points":
                                                     H.bit_count()})
                rec["events"] += 1
        for p, _, _, t in sp:
            trace_shas[p].add(sha(t, n))
        for p in plist:
            if e & fibre[p] == e:
                subfibre_counts[p] += 1

    # ---------- isolation targets ----------
    cyl_events = {}
    cyl_supported = {}
    for (s, c, d), cm in sorted(cyl.items()):
        inside = [e for e in evl if e and e & cm == e]
        maximal = [e for e in inside
                   if not any(o != e and e & o == e for o in inside)]
        cyl_events[f"{s}{c}{d}"] = cm in events
        cyl_supported[f"{s}{c}{d}"] = {
            "nonzero_events_inside": len(inside),
            "maximal_events_inside": len(maximal),
            "max_points": max((e.bit_count() for e in inside), default=0),
            "cylinder_points": cm.bit_count()}
    act_supported = [sum(1 for e in evl if e and e & cm == e)
                     for cm in act]

    # ---------- rule tests on hull-gap events ----------
    hg = sorted(hull_gap_events)
    nested_pairs = []
    one_fibre_diffs = []
    compat = []
    for a_i, Ha in enumerate(hg):
        for Hb in hg[a_i + 1:]:
            sa = set(hull_gap_events[Ha])
            sb = set(hull_gap_events[Hb])
            if Ha & ~Hb == 0 or Hb & ~Ha == 0:
                small, big = (Ha, Hb) if Ha & ~Hb == 0 else (Hb, Ha)
                diff = big & ~small
                nested_pairs.append({
                    "diff_points": diff.bit_count(),
                    "diff_is_event": diff in events,
                    "diff_fibres": len(hull_gap_events[big])
                    - len(hull_gap_events[small])})
            if len(sa ^ sb) == 1:
                fdiff = list(sa ^ sb)[0]
                one_fibre_diffs.append({
                    "fibre": list(fdiff),
                    "nested": Ha & ~Hb == 0 or Hb & ~Ha == 0,
                    "fibre_is_event": fibre[fdiff] in events})
            compat.append({
                "intersection_is_event": Ha & Hb in events,
                "union_is_event": Ha | Hb in events,
                "sigma_intersect": len(sa & sb)})
    lam_viol = 0
    sig_list = sorted(sigma_sets)
    for a_i, sa in enumerate(sig_list):
        for sb in sig_list[a_i + 1:]:
            inter = set(sa) & set(sb)
            if inter and inter != set(sa) and inter != set(sb):
                lam_viol += 1

    # ---------- same-side residue probe ----------
    log("same-side residue probe...")
    probe = []
    for s in ("q", "r"):
        for c in (0, 1):
            for d in (0, 1):
                A = lit[(s, 0)] if c else full ^ lit[(s, 0)]
                B = lit[(s, 1)] if d else full ^ lit[(s, 1)]
                U, L, mu, ml = extrema(evl, up, down, idx[A], idx[B])
                Wp = full
                for k in bits(U):
                    Wp &= evl[k]
                union = A | B
                inter = A & B
                gap = Wp & ~union
                copp = cyl[(s, 1 - c, 1 - d)]
                lower_terminal_meet = full ^ Wp
                gprof = [{"profile": list(p),
                          "points": (gap & fibre[p]).bit_count(),
                          "whole": gap & fibre[p] == fibre[p]}
                         for p in plist if gap & fibre[p]]
                probe.append({
                    "side": s, "signs": [c, d],
                    "join_exists": len(mu) == 1,
                    "meet_exists": len(ml) == 1,
                    "minimal_upper_bounds": len(mu),
                    "maximal_lower_bounds": len(ml),
                    "upper_bounds": U.bit_count(),
                    "lower_bounds": L.bit_count(),
                    "union_is_event": union in events,
                    "intersection_is_event": inter in events,
                    "gap_points": gap.bit_count(),
                    "gap_inside_opposite_cylinder": gap & ~copp == 0,
                    "gap_profile_decomposition": gprof,
                    "gap_activation_points": [
                        (gap & act[0]).bit_count(),
                        (gap & act[1]).bit_count()],
                    "terminal_meet_forced_lower_points":
                        lower_terminal_meet.bit_count(),
                    "terminal_meet_forced_lower_is_event":
                        lower_terminal_meet in events,
                    "opposite_cylinder_points": copp.bit_count()})

    # ---------- banked comparison ----------
    banked_path = os.path.join(HERE,
                               "full_grid_stage558_splitter_incidence.json")
    banked_cmp = None
    if os.path.exists(banked_path):
        bk = json.load(open(banked_path))
        common = [k for k in bk["selected_join_hulls"][0]
                  if k != "repair_increment_split_fibres"]
        bank_min = []
        for r in bk["selected_join_hulls"]:
            d = {k: r[k] for k in common}
            d["repair_increment_split_fibres"] = sorted(
                x["profile"] for x in r["repair_increment_split_fibres"])
            bank_min.append(d)
        mine_min = []
        for r in selected:
            d = {k: r[k] for k in common}
            d["repair_increment_split_fibres"] = sorted(
                r["repair_increment_split_fibres"])
            mine_min.append(d)
        banked_cmp = {
            "banked_producer_sha256": bk.get("producer_sha256"),
            "banked_producer_is_stale_vs_working_tree":
                bk.get("producer_sha256") != hashlib.sha256(
                    open(os.path.join(
                        HERE, "full_grid_stage558_splitter_incidence.py"),
                        "rb").read()).hexdigest(),
            "profile_measurable_events_match":
                bk["profile_measurable_events"] == len(pm),
            "profile_pair_failures_match":
                bk["profile_pair_failures"] == len(failures),
            "failures_sha256_match":
                bk["failures_sha256"] == failure_digest,
            "failure_histogram_match": bk["failure_histogram"] == [
                {"touched_profiles": k[0], "properly_split_profiles": k[1],
                 "pairs": v} for k, v in sorted(hist.items())],
            "selected_join_hulls_match":
                bank_min == mine_min,
            "first_failure_match": bk["first_failure"] == failures[0]}

    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "carrier_points": n,
        "stage_events": len(events),
        "chain": [230, 256, 492, 558],
        "profile_measurable_events": len(pm),
        "profile_pair_failures": len(failures),
        "failure_histogram": [
            {"touched_profiles": k[0], "properly_split_profiles": k[1],
             "pairs": v} for k, v in sorted(hist.items())],
        "failures_sha256": failure_digest,
        "failing_pair_gaps_with_activation_points": act_gap_pairs,
        "first_failure": failures[0] if failures else None,
        "selected_join_hulls": selected,
        "all_selected_joins_remain_least": all(
            r["join_still_least_at_stage558"] for r in selected),
        "provenance": prov,
        "hull_census": {
            "flag_histogram": [
                {"interior_event": k[0], "saturation_event": k[1],
                 "hull_gap_event": k[2], "split_fibres": k[3], "events": v}
                for k, v in sorted(flag_hist.items())],
            "distinct_split_signatures": len(sigma_sets),
            "split_signature_laminarity_violations": lam_viol,
            "distinct_nonzero_hull_gap_events": len(hull_gap_events),
            "hull_gap_event_edges": edge_info},
        "isolation_targets": {
            "profile_fibres_are_events":
                {"".join(map(str, p)): fibre_events[p] for p in plist},
            "nonzero_events_inside_fibre":
                {"".join(map(str, p)): subfibre_counts[p] for p in plist},
            "macro_cylinders_are_events": cyl_events,
            "macro_cylinder_supported_events": cyl_supported,
            "activation_cylinder_supported_events": act_supported,
            "distinct_proper_traces_per_fibre":
                {"".join(map(str, p)): len(trace_shas[p]) for p in plist}},
        "rule_tests": {
            "nested_hull_gap_pairs": nested_pairs,
            "one_fibre_symmetric_difference_pairs": one_fibre_diffs,
            "hull_gap_compatibility_pairs": compat},
        "same_side_residue_probe": probe,
        "banked_comparison": banked_cmp,
        "independence": ("fresh: closure, order tables, first-failure scan, "
                         "pair census, hulls, all new censuses; shared: "
                         "grid.build carrier/mask construction, the three "
                         "repair selections (branch data), sorted-scan "
                         "first-failure convention, banked record format "
                         "for digest comparison"),
        "scope": ("one exact 558-event branch; no fourth repair; no orbit "
                  "quotient; stage facts only -- no terminal theorem is "
                  "claimed from this nonlattice stage"),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_stage558_hull_gap_isolation_audit.py --emit")}
    out["producer_sha256"] = hashlib.sha256(
        open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out

if __name__ == "__main__":
    emit = "--emit" in sys.argv
    out = main()
    path = os.path.join(HERE, "full_grid_stage558_hull_gap_isolation.json")
    if emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2)
            f.write("\n")
    elif os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps({"status": "PASS",
                      "payload_sha256": out["payload_sha256"],
                      "profile_pair_failures": out["profile_pair_failures"],
                      "banked_comparison": out["banked_comparison"]},
                     sort_keys=True, indent=2))
