#!/usr/bin/env python3
"""Targeted same-half cross-root locality pilot.

The current family is exactly the two full old cylinder copies, the six
distinguished physical events R,Rc,S,Sc,T,Tc, and the 488 banked immediate
literal roots.  Candidate A/A pairs (disjoint-union roots) and D/D pairs
(complementary-difference roots) are selected around the five pilot failures,
then from provenance-diverse positions in the 189-occurrence buckets.

No event is adjoined.  The producer stops at the first literal join or meet
whose two source parents are new and whose current extrema are nonunique.
"""
import argparse
import hashlib
import json
import resource
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_forced_T_literal_bridge_census.py"
SOURCE_RECEIPT = HERE / "arr_forced_T_literal_bridge_census.json"
KERNEL_RECEIPT = HERE / "arr_forced_T_bridge_kernel_pilot.json"
RECEIPT = HERE / "arr_forced_T_same_half_cross_root_pilot.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def recover():
    source = SOURCE.read_text()
    needle = "    source = json.loads(SOURCE_RECEIPT.read_text())"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_CROSS_ROOT'] = {"
        "'d':d,'engine':engine,'carrier':carrier,'specials':specials,"
        "'seen_roots':seen_roots,'bridge_rows':bridge_rows,"
        "'exact_classes':exact_classes,'quantify_exists':quantify_exists,"
        "'projection_carriers':projection_carriers,'left_map':left_map,"
        "'right_map':right_map,'lift':lift,'le':le}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_cross_root"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_CROSS_ROOT"]


def payload():
    started = time.perf_counter()
    bank = recover()
    reconstruction_seconds = time.perf_counter() - started
    d, old = bank["d"], bank["d"]["d"]
    events, roots = d["events"], d["roots"]
    macros, old_engines = d["macros"], d["engines"]
    principal = old["principal"]
    neg, subset = d["neg"], d["subset"]
    engine, carrier = bank["engine"], bank["carrier"]
    quantify_exists = bank["quantify_exists"]
    projection_carriers = bank["projection_carriers"]
    mappings = {"left": bank["left_map"], "right": bank["right_map"]}
    lift, le = bank["lift"], bank["le"]
    root_by_class = {class_id: root for root, class_id
                     in bank["seen_roots"].items()}
    bridge_rows = bank["bridge_rows"]
    class_rows = {
        class_id: [row for row in bridge_rows
                   if row["exact_event_class"] == class_id]
        for class_id in root_by_class
    }
    n = len(events)
    assert n == 18676 and len(root_by_class) == 488
    root_index = {roots[event]: i for i, event in enumerate(events)}
    complement = {i: root_index[neg(roots[event])]
                  for i, event in enumerate(events)}

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

    # Calibration before using the projection path on cross-root literals.
    for side in ("left", "right"):
        universal, existential = projection(bank["specials"]["T"], side)
        assert to_old_tuple(universal, side) == d["t_univ_" + side]
        assert to_old_tuple(existential, side) == d["t_exist_" + side]

    def old_extrema(target, mode):
        # For upper extrema use the existential shadow; complement duality
        # turns minimal old uppers into maximal old lowers.
        result = []
        for side in ("left", "right"):
            universal, existential = projection(target, side)
            if mode == "lower":
                shadow = to_old_tuple(universal, side)
                candidates = [i for i, event in enumerate(events)
                              if subset(roots[event], shadow)]
                bits = sum(1 << i for i in candidates)
                extrema = [i for i in candidates
                           if (principal[i] & bits) == (1 << i)]
                result.extend((engine.app(0, carrier, lift(i, side)),
                               f"old_{side}({i})", "old")
                              for i in extrema)
            else:
                shadow = neg(to_old_tuple(existential, side))
                dual = [i for i, event in enumerate(events)
                        if subset(roots[event], shadow)]
                bits = sum(1 << i for i in dual)
                dual_max = [i for i in dual
                            if (principal[i] & bits) == (1 << i)]
                result.extend((engine.app(0, carrier,
                                          lift(complement[i], side)),
                               f"old_{side}({complement[i]})", "old")
                              for i in dual_max)
        return result

    # Exact current non-old events.  T,Tc occur in the 488 roots; deduplication
    # is by physical root, with old > special > immediate-root label priority.
    current_nonold = []
    for name, root in bank["specials"].items():
        current_nonold.append((root, name, "special"))
    for class_id, root in sorted(root_by_class.items()):
        current_nonold.append((root, f"root({class_id})", "new"))

    def dedup(rows):
        priority = {"old": 0, "special": 1, "new": 2}
        best = {}
        for root, label, kind in rows:
            if root not in best or priority[kind] < priority[best[root][2]]:
                best[root] = (root, label, kind)
        return list(best.values())

    def extrema(target, mode):
        rows = old_extrema(target, mode)
        if mode == "upper":
            rows += [(root, label, kind) for root, label, kind in current_nonold
                     if le(target, root)]
        else:
            rows += [(root, label, kind) for root, label, kind in current_nonold
                     if le(root, target)]
        rows = dedup(rows)
        answer = []
        for row in rows:
            root = row[0]
            if mode == "upper":
                dominated = any(other[0] != root and le(other[0], root)
                                for other in rows)
            else:
                dominated = any(other[0] != root and le(root, other[0])
                                for other in rows)
            if not dominated:
                answer.append(row)
        return sorted(answer, key=lambda row: (row[2], row[1]))

    # Exact coarse descriptor, used only to pick provenance-diverse 189-root
    # controls; it is not assumed to be a transition congruence.
    descriptor_fields = (
        "operation", "base", "source_kind", "source_side",
        "left_cylindrical", "right_cylindrical", "contained_in_T",
        "contained_in_Tc", "contained_in_R", "contains_T", "contains_Tc",
        "contains_R", "contained_in_source_parent", "contains_source_parent",
        "is_one_of_five_forced_differences",
        "source_in_frozen_five_parent_pool", "singleton_hazard",
        "activation_supported",
    )
    buckets = {}
    for row in bridge_rows:
        key = tuple(row[field] for field in descriptor_fields)
        buckets.setdefault(key, []).append(row)
    large_buckets = [rows for rows in buckets.values() if len(rows) == 189]
    large_classes = {}
    for rows in large_buckets:
        operation = rows[0]["operation"]
        ids = sorted({row["exact_event_class"] for row in rows})
        large_classes.setdefault(operation, set()).update(ids)
    large_classes = {key: sorted(value) for key, value in large_classes.items()}

    operations = {
        class_id: {row["operation"] for row in rows}
        for class_id, rows in class_rows.items()
    }
    A = sorted(class_id for class_id, kinds in operations.items()
               if "disjoint_union" in kinds and class_id not in (0, 1))
    D = sorted(class_id for class_id, kinds in operations.items()
               if "complementary_difference" in kinds and class_id not in (0, 1))
    failure_A, failure_D = (8, 14, 106), (15, 105)
    assert all(x in A for x in failure_A) and all(x in D for x in failure_D)

    def quantiles(values):
        if not values:
            return []
        return sorted({values[0], values[len(values) // 2], values[-1]})

    candidates = []

    def add(kind, left, right, reason):
        if left == right:
            return
        pair = tuple(sorted((left, right)))
        key = (kind, pair)
        if not any((row[0], row[1]) == key for row in candidates):
            candidates.append((kind, pair, reason))

    # Highest priority: all same-kind pairs among the known failures.
    for failures, kind in ((failure_A, "A/A"), (failure_D, "D/D")):
        for i, left in enumerate(failures):
            for right in failures[i + 1:]:
                add(kind, left, right, "two_pilot_failures")

    # Then pair every failure with first/middle/last provenance controls from
    # the corresponding 189-occurrence bucket.
    for failure in failure_A:
        for control in quantiles(large_classes.get("disjoint_union", [])):
            add("A/A", failure, control, "failure_vs_189_bucket_quantile")
    for failure in failure_D:
        for control in quantiles(large_classes.get(
                "complementary_difference", [])):
            add("D/D", failure, control, "failure_vs_189_bucket_quantile")

    # Finally compare the provenance-diverse quantiles internally.
    for operation, kind in (("disjoint_union", "A/A"),
                            ("complementary_difference", "D/D")):
        controls = quantiles(large_classes.get(operation, []))
        for i, left in enumerate(controls):
            for right in controls[i + 1:]:
                add(kind, left, right, "within_189_bucket_quantiles")

    current_roots = set(root_by_class.values()) | set(bank["specials"].values())
    records = []
    algebraically_pruned = 0
    first_witness = None
    exact_targets_audited = 0
    target_cache = {}

    def audit_target(target, mode):
        nonlocal exact_targets_audited
        key = (target, mode)
        if key in target_cache:
            return target_cache[key]
        exact_targets_audited += 1
        xs = extrema(target, mode)
        row = {
            "mode": mode,
            "literal_target_already_current": target in current_roots,
            "extremum_count": len(xs),
            "extrema": [{"label": label, "kind": kind}
                        for _, label, kind in xs],
            "interpolant_exists": len(xs) == 1,
            "exactly_two_new_extrema": (
                len(xs) == 2 and all(kind == "new" for _, _, kind in xs)),
        }
        target_cache[key] = row
        return row

    for kind, (left_id, right_id), reason in candidates:
        left, right = root_by_class[left_id], root_by_class[right_id]
        if le(left, right) or le(right, left):
            algebraically_pruned += 1
            records.append({
                "kind": kind, "classes": [left_id, right_id],
                "selection_reason": reason, "pruned": "comparable",
            })
            continue
        union = engine.app(1, left, right)
        intersection = engine.app(0, left, right)
        preferred = (("lower", intersection), ("upper", union)) if kind == "A/A" else (
            ("upper", union), ("lower", intersection))
        pair_row = {
            "kind": kind,
            "classes": [left_id, right_id],
            "selection_reason": reason,
            "pruned": None,
            "literal_union_is_current": union in current_roots,
            "literal_intersection_is_current": intersection in current_roots,
            "audits": [],
        }
        for mode, target in preferred:
            if target in current_roots:
                pair_row["audits"].append({
                    "mode": mode, "literal_target_already_current": True,
                    "extremum_count": 1, "extrema": [],
                    "interpolant_exists": True,
                    "exactly_two_new_extrema": False,
                })
                continue
            target_row = audit_target(target, mode)
            pair_row["audits"].append(target_row)
            # Both source classes are new immediate roots by construction.
            # One-new-parent locality is refuted by any nonunique current
            # extremum; the extrema themselves may be old, special, or new.
            if not target_row["interpolant_exists"]:
                first_witness = {
                    "kind": kind,
                    "classes": [left_id, right_id],
                    "two_new_source_parents": True,
                    "selection_reason": reason,
                    "mode": mode,
                    "extrema": target_row["extrema"],
                }
                break
        records.append(pair_row)
        if first_witness is not None:
            break

    bridge_source = json.loads(SOURCE_RECEIPT.read_text())
    kernel_source = json.loads(KERNEL_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-T-same-half-cross-root-pilot-v1",
        "schema_version": "1.0",
        "source_bridge_payload_sha256": bridge_source["payload_sha256"],
        "source_kernel_pilot_payload_sha256": kernel_source["payload_sha256"],
        "current_family_definition": (
            "two full 18,676-event old cylinder copies plus R,Rc,S,Sc,T,Tc "
            "plus the 488 exact immediate literal roots; exact-root deduplicated"
        ),
        "candidate_pair_count": len(candidates),
        "candidate_selection_order": [
            {"kind": kind, "classes": list(pair), "reason": reason}
            for kind, pair, reason in candidates
        ],
        "pairs_processed_before_stop": len(records),
        "algebraically_pruned_pair_count": algebraically_pruned,
        "exact_literal_targets_audited": exact_targets_audited,
        "records": records,
        "first_two_new_source_parent_unresolved_cut": first_witness,
        "stopped_early": first_witness is not None,
        "reconstruction_seconds": reconstruction_seconds,
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "evidence_class": "Executable verified — sampled finite scope",
        "scope": (
            "Deterministic targeted same-half pairs incident to five pilot "
            "failures and first/middle/last controls from 189-occurrence buckets. "
            "Extrema are exact in the fixed current family only. The run stops "
            "at the first two-new-source-parent cut and performs no closure, repair, "
            "lattice, OML, centre, state, sigma, ODBC, MBRC, or Phi audit."
        ),
        "verification_independence": (
            "One deterministic implementation reusing the authoritative exact "
            "bridge MDD producer and old-event order tables."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "arr_forced_T_same_half_cross_root_pilot.py --verify"
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
        "processed": out["pairs_processed_before_stop"],
        "targets": out["exact_literal_targets_audited"],
        "witness": out["first_two_new_source_parent_unresolved_cut"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
