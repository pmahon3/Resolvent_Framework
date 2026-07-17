#!/usr/bin/env python3
"""Exact forced-meet interval for immediate roots 8 and 106.

Let x=root(8), y=root(106), H=x intersection y, and let L be the
literal union of old_left(1024) and old_right(2).  The producer audits the
fixed current family only and enumerates the nested differences forced by
one hypothetical H,H^c adjunction.  It performs no closure round.
"""
import argparse
import functools
import hashlib
import json
import math
import resource
import struct
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_forced_T_literal_bridge_census.py"
SOURCE_RECEIPT = HERE / "arr_forced_T_literal_bridge_census.json"
CROSS_RECEIPT = HERE / "arr_forced_T_same_half_cross_root_pilot.json"
RECEIPT = HERE / "arr_forced_T_cross_root_meet_interval.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def recover():
    source = SOURCE.read_text()
    needle = "    source = json.loads(SOURCE_RECEIPT.read_text())"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_MEET_INTERVAL'] = {"
        "'d':d,'engine':engine,'carrier':carrier,'specials':specials,"
        "'seen_roots':seen_roots,'quantify_exists':quantify_exists,"
        "'projection_carriers':projection_carriers,'left_map':left_map,"
        "'right_map':right_map,'lift':lift,'le':le}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_meet_interval"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_MEET_INTERVAL"]


def payload():
    started = time.perf_counter()
    bank = recover()
    reconstruction_seconds = time.perf_counter() - started
    d, old = bank["d"], bank["d"]["d"]
    events, roots = d["events"], d["roots"]
    macros, old_engines = d["macros"], d["engines"]
    principal, atoms = old["principal"], old["atoms"]
    zero, old_join = old["zero"], old["old_join"]
    neg, subset, rhash = d["neg"], d["subset"], old["rhash"]
    engine, carrier = bank["engine"], bank["carrier"]
    quantify_exists = bank["quantify_exists"]
    projection_carriers = bank["projection_carriers"]
    mappings = {"left": bank["left_map"], "right": bank["right_map"]}
    lift, le = bank["lift"], bank["le"]
    root_by_class = {class_id: root for root, class_id
                     in bank["seen_roots"].items()}
    assert len(events) == 18676 and len(root_by_class) == 488
    root_index = {roots[event]: i for i, event in enumerate(events)}
    complement = {i: root_index[neg(roots[event])]
                  for i, event in enumerate(events)}

    def physical_old(index, side):
        return engine.app(0, carrier, lift(index, side))

    x, y = root_by_class[8], root_by_class[106]
    H = engine.app(0, x, y)
    Hc = engine.app(0, carrier, engine.neg(H))
    left_lower = physical_old(1024, "left")
    right_lower = physical_old(2, "right")
    L = engine.app(1, left_lower, right_lower)

    def projection(root, side):
        eliminated = {4, 5, 6} if side == "left" else {0, 1, 2}
        existential = quantify_exists(root, eliminated)
        bad = engine.app(0, carrier, engine.neg(root))
        universal = engine.app(
            0, projection_carriers[side],
            engine.neg(quantify_exists(bad, eliminated)))
        return universal, existential

    def to_old_tuple(global_root, side):
        mapping = mappings[side]
        answer = []
        domain = engine.domains[0]
        for macro_index, (_, domains) in enumerate(macros):
            target = old_engines[macro_index]
            memo = {}

            def go(root, old_variable):
                key = (root, old_variable)
                if key in memo:
                    return memo[key]
                if old_variable == 4:
                    assert root <= 1
                    return root
                global_variable = mapping[old_variable]
                if root > 1:
                    variable, children = engine.nodes[root]
                    assert variable >= global_variable
                else:
                    variable, children = 7, None
                values = []
                for state in domains[old_variable]:
                    child = children[state] if variable == global_variable else root
                    values.append(go(child, old_variable + 1))
                result = target.node(old_variable, values)
                memo[key] = result
                return result

            answer.append(go(global_root, 0))
        return tuple(answer)

    projection_cache = {}

    def old_shadows(target, side):
        key = (target, side)
        if key not in projection_cache:
            universal, existential = projection(target, side)
            projection_cache[key] = (to_old_tuple(universal, side),
                                     to_old_tuple(existential, side))
        return projection_cache[key]

    # Calibrate the new physical projection path against banked T shadows.
    for side in ("left", "right"):
        universal, existential = old_shadows(bank["specials"]["T"], side)
        assert universal == d["t_univ_" + side]
        assert existential == d["t_exist_" + side]

    def kernel(target, side):
        universal, existential = old_shadows(target, side)
        lowers = [i for i, event in enumerate(events)
                  if subset(roots[event], universal)]
        lower_bits = sum(1 << i for i in lowers)
        maximal = [i for i in lowers
                   if (principal[i] & lower_bits) == (1 << i)]
        dual_shadow = neg(existential)
        dual_lowers = [i for i, event in enumerate(events)
                       if subset(roots[event], dual_shadow)]
        dual_bits = sum(1 << i for i in dual_lowers)
        dual_maximal = [i for i in dual_lowers
                        if (principal[i] & dual_bits) == (1 << i)]
        minimal = [complement[i] for i in dual_maximal]
        eligible = [atom for atom in atoms
                    if subset(roots[events[atom]], universal)]
        fold = zero
        escape = None
        for atom in eligible:
            prior = fold
            fold = old_join(fold, atom)
            if escape is None and not subset(roots[events[fold]], universal):
                escape = {"prior_index": prior, "atom_index": atom,
                          "escaping_join_index": fold}
        return {
            "universal_shadow_root_sha256": rhash(universal),
            "existential_shadow_root_sha256": rhash(existential),
            "old_lower_count": len(lowers),
            "maximal_old_lower_indices": maximal,
            "greatest_old_lower_exists": len(maximal) == 1,
            "old_upper_count": len(dual_lowers),
            "minimal_old_upper_indices": minimal,
            "least_old_upper_exists": len(minimal) == 1,
            "eligible_old_atom_count": len(eligible),
            "atom_fold_index": fold,
            "atom_fold_inside_target": subset(roots[events[fold]], universal),
            "first_atom_fold_escape": escape,
        }

    current_nonold = []
    for name, root in bank["specials"].items():
        current_nonold.append((root, name, "special"))
    for class_id, root in sorted(root_by_class.items()):
        current_nonold.append((root, f"root({class_id})", "new"))

    def dedup(rows):
        priority = {"old": 0, "special": 1, "new": 2}
        best = {}
        for row in rows:
            if row[0] not in best or priority[row[2]] < priority[best[row[0]][2]]:
                best[row[0]] = row
        return list(best.values())

    def old_extrema(target, mode):
        rows = []
        for side in ("left", "right"):
            row = kernel(target, side)
            indices = (row["maximal_old_lower_indices"] if mode == "lower"
                       else row["minimal_old_upper_indices"])
            rows += [(physical_old(i, side), f"old_{side}({i})", "old")
                     for i in indices]
        return rows

    def current_extrema(target, mode):
        rows = old_extrema(target, mode)
        if mode == "lower":
            rows += [row for row in current_nonold if le(row[0], target)]
        else:
            rows += [row for row in current_nonold if le(target, row[0])]
        rows = dedup(rows)
        answer = []
        for row in rows:
            root = row[0]
            if mode == "lower":
                dominated = any(other[0] != root and le(root, other[0])
                                for other in rows)
            else:
                dominated = any(other[0] != root and le(other[0], root)
                                for other in rows)
            if not dominated:
                answer.append(row)
        return sorted(answer, key=lambda row: (row[2], row[1]))

    @functools.lru_cache(None)
    def structural_hash(root):
        if root <= 1:
            return hashlib.sha256(bytes((root,))).digest()
        variable, children = engine.nodes[root]
        h = hashlib.sha256(b"M" + struct.pack("<I", variable))
        for child in children:
            h.update(structural_hash(child))
        return h.digest()

    @functools.lru_cache(None)
    def count_from(root, level=0):
        if root <= 1:
            return root * math.prod(len(engine.domains[v])
                                    for v in range(level, 7))
        variable, children = engine.nodes[root]
        skipped = math.prod(len(engine.domains[v])
                            for v in range(level, variable))
        return skipped * sum(count_from(child, variable + 1)
                             for child in children)

    current_root_set = set(root_by_class.values()) | set(bank["specials"].values())
    relation = {
        "L_subset_H": le(L, H),
        "L_equals_H": L == H,
        "L_proper_subset_H": le(L, H) and L != H,
        "H_subset_x": le(H, x),
        "H_subset_y": le(H, y),
        "x_equals_H": x == H,
        "y_equals_H": y == H,
        "H_current": H in current_root_set,
        "Hc_current": Hc in current_root_set,
        "lower_pieces_disjoint": engine.app(0, left_lower, right_lower) == 0,
        "lower_piece_overlap_points": count_from(
            engine.app(0, left_lower, right_lower), 0),
        "L_points": count_from(L, 0),
        "H_points": count_from(H, 0),
        "cut_local_descent_rank_H_minus_L": count_from(
            engine.app(0, H, engine.neg(L)), 0),
        "L_exact_mdd_sha256": structural_hash(L).hex(),
        "H_exact_mdd_sha256": structural_hash(H).hex(),
        "Hc_exact_mdd_sha256": structural_hash(Hc).hex(),
    }
    assert (relation["L_subset_H"] and not relation["H_current"] and
            relation["lower_pieces_disjoint"])

    kernels = {
        name: {side: kernel(root, side) for side in ("left", "right")}
        for name, root in (("H", H), ("Hc", Hc))
    }
    current = {
        name: {
            mode: current_extrema(root, mode)
            for mode in ("lower", "upper")
        } for name, root in (("H", H), ("Hc", Hc))
    }

    def labels(rows):
        return [{"label": label, "kind": kind} for _, label, kind in rows]

    current_report = {}
    for name, family in current.items():
        row = {}
        for mode, xs in family.items():
            row[mode + "_extrema"] = labels(xs)
            row[mode + "_extremum_count"] = len(xs)
            row[("greatest_current_lower_exists" if mode == "lower"
                 else "least_current_upper_exists")] = len(xs) == 1
        current_report[name] = row

    # Exact interpolant calibration: scan current nonold roots and minimal old
    # uppers of L.  Any old interpolant dominates a minimal old upper of L.
    interpolants = [row for row in current_nonold if le(L, row[0]) and le(row[0], H)]
    for row in old_extrema(L, "upper"):
        if le(row[0], H):
            interpolants.append(row)
    interpolants = dedup(interpolants)
    assert not interpolants

    # One-transition literal consequences only.  For each maximal current
    # lower e of B, record B\e and its complement B^c union e.
    immediate = []
    seen = set()
    for base_name, base, dual in (("H", H, Hc), ("Hc", Hc, H)):
        for lower_root, lower_label, lower_kind in current[base_name]["lower"]:
            difference = engine.app(0, base, engine.neg(lower_root))
            bridge = engine.app(1, dual, lower_root)
            assert bridge == engine.app(0, carrier, engine.neg(difference))
            for operation, root in (("nested_difference", difference),
                                    ("dual_disjoint_union", bridge)):
                key = (operation, root, base_name, lower_label)
                if key in seen:
                    continue
                seen.add(key)
                immediate.append({
                    "base": base_name,
                    "source_lower": lower_label,
                    "source_lower_kind": lower_kind,
                    "operation": operation,
                    "exact_mdd_sha256": structural_hash(root).hex(),
                    "physical_cardinality": count_from(root, 0),
                    "already_current": root in current_root_set,
                    "contained_in_H": le(root, H),
                    "contained_in_Hc": le(root, Hc),
                })

    # Complement-dual calibration at the current-family level.
    h_lower_roots = {root for root, _, _ in current["H"]["lower"]}
    hc_upper_roots = {root for root, _, _ in current["Hc"]["upper"]}
    dual_of_h_lowers = {engine.app(0, carrier, engine.neg(root))
                        for root in h_lower_roots}
    complement_dual = {
        "H_maximal_lower_count": len(h_lower_roots),
        "Hc_minimal_upper_count": len(hc_upper_roots),
        "exact_duality": dual_of_h_lowers == hc_upper_roots,
        "H_maximal_lower_labels": labels(current["H"]["lower"]),
        "Hc_minimal_upper_labels": labels(current["Hc"]["upper"]),
    }
    assert complement_dual["exact_duality"]

    bridge_source = json.loads(SOURCE_RECEIPT.read_text())
    cross_source = json.loads(CROSS_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-T-cross-root-meet-interval-v1",
        "schema_version": "1.0",
        "source_bridge_payload_sha256": bridge_source["payload_sha256"],
        "source_cross_root_payload_sha256": cross_source["payload_sha256"],
        "source_classes": [8, 106],
        "relations": relation,
        "current_interpolant_count": len(interpolants),
        "current_interpolants": labels(interpolants),
        "old_kernels": kernels,
        "current_family_extrema": current_report,
        "complement_dual_source_cut": complement_dual,
        "immediate_one_transition_occurrence_count": len(immediate),
        "immediate_one_transition_consequences": immediate,
        "forced_meet_status": (
            "H is uniquely forced and is the immediate literal disjoint union "
            "of old_left(1024) and old_right(2): L equals H and the pieces are "
            "disjoint, so complement/disjoint-union closure must adjoin H"
            if relation["L_equals_H"] else
            "H is only the greatest set-theoretic envelope; every valid repair "
            "need only lie in the proper interval L <= h <= H"
        ),
        "reconstruction_seconds": reconstruction_seconds,
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "evidence_class": "Executable verified — exhaustive finite scope for displayed cut",
        "scope": (
            "Exact interval, old kernels, fixed-current-family extrema, complement "
            "duality, and immediate H/Hc nested consequences for source classes "
            "8 and 106 only. No choice of a smaller repair h, closure round, later "
            "cross-root pair, lattice, OML, centre, state, sigma, ODBC, MBRC, or "
            "Phi claim is made."
        ),
        "verification_independence": (
            "One deterministic implementation reusing the authoritative bridge "
            "MDD producer and old-event order tables."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "arr_forced_T_cross_root_meet_interval.py --verify"
        ),
    }
    out["payload_sha256"] = digest(out)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = payload()
    if args.emit:
        RECEIPT.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    if args.verify or not args.emit:
        stored = json.loads(RECEIPT.read_text())
        volatile = {"reconstruction_seconds", "wall_seconds",
                    "peak_rss_bytes_darwin", "payload_sha256"}
        assert ({k: v for k, v in stored.items() if k not in volatile} ==
                {k: v for k, v in out.items() if k not in volatile})
    print(json.dumps({
        "status": "PASS",
        "payload_sha256": out["payload_sha256"],
        "rank": out["relations"]["cut_local_descent_rank_H_minus_L"],
        "interpolants": out["current_interpolant_count"],
        "immediate": out["immediate_one_transition_occurrence_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
