#!/usr/bin/env python3
"""Eight-root old-kernel pilot for exact forced-T literal bridges.

This is deliberately a local discriminator.  It reconstructs the banked exact
physical bridge roots, chooses eight roots by a deterministic provenance rule,
and computes their exact old lower and upper kernels on both copies.  It does
not extend the mixed family or claim coverage of the remaining roots.
"""
import argparse
import hashlib
import json
import resource
import statistics
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_forced_T_literal_bridge_census.py"
SOURCE_RECEIPT = HERE / "arr_forced_T_literal_bridge_census.json"
RECEIPT = HERE / "arr_forced_T_bridge_kernel_pilot.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def recover():
    source = SOURCE.read_text()
    needle = "    source = json.loads(SOURCE_RECEIPT.read_text())"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_KERNEL_PILOT'] = {"
        "'d':d,'engine':engine,'carrier':carrier,'specials':specials,"
        "'seen_roots':seen_roots,'bridge_rows':bridge_rows,"
        "'exact_classes':exact_classes,'quantify_exists':quantify_exists,"
        "'projection_carriers':projection_carriers,'left_map':left_map,"
        "'right_map':right_map}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_kernel_pilot"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_KERNEL_PILOT"]


def payload():
    started = time.perf_counter()
    bank = recover()
    reconstruction_seconds = time.perf_counter() - started
    d = bank["d"]
    old = d["d"]
    events, roots = d["events"], d["roots"]
    macros, old_engines = d["macros"], d["engines"]
    principal, atoms = old["principal"], old["atoms"]
    zero, old_join = old["zero"], old["old_join"]
    op, neg, subset, rhash = d["op"], d["neg"], d["subset"], old["rhash"]
    engine, carrier = bank["engine"], bank["carrier"]
    exact_classes = bank["exact_classes"]
    bridge_rows = bank["bridge_rows"]
    quantify_exists = bank["quantify_exists"]
    projection_carriers = bank["projection_carriers"]
    mappings = {"left": bank["left_map"], "right": bank["right_map"]}
    n = len(events)
    assert n == 18676 and len(atoms) == 91
    root_index = {roots[event]: i for i, event in enumerate(events)}
    complement = {i: root_index[neg(roots[event])]
                  for i, event in enumerate(events)}

    root_by_class = {class_id: root for root, class_id
                     in bank["seen_roots"].items()}
    class_by_id = {row["exact_event_class"]: row for row in exact_classes}
    rows_by_class = {
        class_id: [row for row in bridge_rows
                   if row["exact_event_class"] == class_id]
        for class_id in class_by_id
    }

    # Reconstruct the receipt's coarse bucket membership without relying on
    # its arbitrary integer labels.
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
    bucket_size = {
        row["exact_event_class"]: len(rows)
        for _, rows in buckets.items() for row in rows
    }

    selected = []

    def choose(label, candidates):
        candidates = sorted(set(candidates) - {c for _, c in selected})
        assert candidates, label
        selected.append((label, candidates[0]))

    forced = [row for row in bridge_rows
              if row["is_one_of_five_forced_differences"]]
    choose("forced_difference_left", [row["exact_event_class"] for row in forced
                                      if row["source_side"] == "left"])
    choose("forced_difference_right", [row["exact_event_class"] for row in forced
                                       if row["source_side"] == "right"])
    choose("duplicate_provenance_first", [
        row["exact_event_class"] for row in exact_classes
        if row["new_relative_to_specials"] and row["occurrence_count"] > 1
    ])
    choose("duplicate_provenance_second", [
        row["exact_event_class"] for row in exact_classes
        if row["new_relative_to_specials"] and row["occurrence_count"] > 1
    ])
    largest = max(bucket_size.values())
    choose("largest_bucket_union", [
        row["exact_event_class"] for row in bridge_rows
        if bucket_size[row["exact_event_class"]] == largest and
        row["operation"] == "disjoint_union" and
        class_by_id[row["exact_event_class"]][
            "requires_outside_frozen_parent_among_literal_representations"]
    ])
    choose("largest_bucket_difference", [
        row["exact_event_class"] for row in bridge_rows
        if bucket_size[row["exact_event_class"]] == largest and
        row["operation"] == "complementary_difference" and
        class_by_id[row["exact_event_class"]][
            "requires_outside_frozen_parent_among_literal_representations"]
    ])
    choose("singleton_coarse_bucket_outside_parent", [
        row["exact_event_class"] for row in bridge_rows
        if bucket_size[row["exact_event_class"]] == 1 and
        class_by_id[row["exact_event_class"]][
            "requires_outside_frozen_parent_among_literal_representations"]
    ])
    choose("special_Rc_bridge", [
        row["exact_event_class"] for row in bridge_rows
        if row["source_kind"] == "special" and row["source_name"] == "Rc"
    ])
    assert len(selected) == 8 and len({c for _, c in selected}) == 8

    def projection(root, side):
        eliminated = {4, 5, 6} if side == "left" else {0, 1, 2}
        existential = quantify_exists(root, eliminated)
        bad = engine.app(0, carrier, engine.neg(root))
        universal = engine.app(
            0, projection_carriers[side],
            engine.neg(quantify_exists(bad, eliminated)))
        return universal, existential

    # Restrict a projected global root to each authoritative old macro and
    # rebuild it in that macro's original MDD engine.
    def to_old_tuple(global_root, side):
        mapping = mappings[side]
        answer = []
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
                    child = (children[state]
                             if variable == global_variable else root)
                    values.append(go(child, old_variable + 1))
                result = target.node(old_variable, values)
                memo[key] = result
                return result

            answer.append(go(global_root, 0))
        return tuple(answer)

    def extrema(universal, existential):
        lower_indices = [i for i, event in enumerate(events)
                         if subset(roots[event], universal)]
        lower_bits = sum(1 << i for i in lower_indices)
        maximal_lowers = [i for i in lower_indices
                          if (principal[i] & lower_bits) == (1 << i)]

        # Complement duality avoids a quadratic minimal-upper scan: old uppers
        # of X correspond to old lowers of X^c, and minimal becomes maximal.
        complement_universal = neg(existential)
        dual_lowers = [i for i, event in enumerate(events)
                       if subset(roots[event], complement_universal)]
        dual_bits = sum(1 << i for i in dual_lowers)
        dual_maximal = [i for i in dual_lowers
                        if (principal[i] & dual_bits) == (1 << i)]
        minimal_uppers = [complement[i] for i in dual_maximal]

        eligible_atoms = [atom for atom in atoms
                          if subset(roots[events[atom]], universal)]
        fold = zero
        escape = None
        for atom in eligible_atoms:
            prior = fold
            fold = old_join(fold, atom)
            if escape is None and not subset(roots[events[fold]], universal):
                escape = {
                    "prior_index": prior,
                    "atom_index": atom,
                    "escaping_join_index": fold,
                }
        return {
            "universal_shadow_root_sha256": rhash(universal),
            "existential_shadow_root_sha256": rhash(existential),
            "old_lower_count": len(lower_indices),
            "maximal_old_lower_indices": maximal_lowers,
            "greatest_old_lower_exists": len(maximal_lowers) == 1,
            "old_upper_count": len(dual_lowers),
            "minimal_old_upper_indices": minimal_uppers,
            "least_old_upper_exists": len(minimal_uppers) == 1,
            "eligible_old_atom_count": len(eligible_atoms),
            "atom_fold_index": fold,
            "atom_fold_inside_target": subset(roots[events[fold]], universal),
            "first_atom_fold_escape": escape,
        }

    # Calibration against the authoritative forced-interval producer: the new
    # seven-coordinate projection and restriction path must recover all four
    # previously banked T shadows bit-exactly before it is used on new roots.
    for side in ("left", "right"):
        universal, existential = projection(bank["specials"]["T"], side)
        assert to_old_tuple(universal, side) == d["t_univ_" + side]
        assert to_old_tuple(existential, side) == d["t_exist_" + side]

    records = []
    kernel_seconds = []
    for label, class_id in selected:
        root = root_by_class[class_id]
        record_started = time.perf_counter()
        sides = {}
        for side in ("left", "right"):
            universal, existential = projection(root, side)
            row = extrema(to_old_tuple(universal, side),
                          to_old_tuple(existential, side))
            row["creates_source_cut_obligation"] = (
                not row["greatest_old_lower_exists"] or
                not row["least_old_upper_exists"] or
                not row["atom_fold_inside_target"])
            sides[side] = row
        elapsed = time.perf_counter() - record_started
        kernel_seconds.append(elapsed)
        reps = rows_by_class[class_id]
        records.append({
            "selection_label": label,
            "exact_event_class": class_id,
            "exact_mdd_sha256": class_by_id[class_id]["exact_mdd_sha256"],
            "occurrence_count": class_by_id[class_id]["occurrence_count"],
            "coarse_bucket_size": bucket_size[class_id],
            "new_relative_to_specials": class_by_id[class_id][
                "new_relative_to_specials"],
            "requires_outside_frozen_parent_among_literal_representations":
                class_by_id[class_id][
                    "requires_outside_frozen_parent_among_literal_representations"],
            "provenance": [{key: row[key] for key in (
                "operation", "base", "source_kind", "source_name",
                "source_side", "source_old_index",
                "is_one_of_five_forced_differences")}
                for row in reps],
            "kernel_seconds": elapsed,
            "sides": sides,
            "creates_any_source_cut_obligation": any(
                row["creates_source_cut_obligation"] for row in sides.values()),
        })

    mean_kernel = statistics.mean(kernel_seconds)
    # The exact 486-new-root projection is a sequential local estimate.  A
    # sharded production implementation should reconstruct the old bank once
    # per shard but avoid rebuilding all 498 bridge records inside every shard.
    projected = {
        "new_exact_root_count": 486,
        "mean_selected_root_kernel_seconds": mean_kernel,
        "sequential_kernel_only_seconds": mean_kernel * 486,
        "fixed_reconstruction_seconds_this_run": reconstruction_seconds,
        "sequential_total_seconds_estimate": (
            reconstruction_seconds + mean_kernel * 486),
        "suggested_roots_per_shard": 16,
        "suggested_shard_count": 31,
        "memory_basis": "pilot process ru_maxrss; dominated by exact ARR reconstruction",
    }

    source = json.loads(SOURCE_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-T-bridge-kernel-pilot-v1",
        "schema_version": "1.0",
        "source_bridge_payload_sha256": source["payload_sha256"],
        "selection_rule": [label for label, _ in selected],
        "selected_exact_event_classes": [class_id for _, class_id in selected],
        "selected_root_count": len(records),
        "records": records,
        "source_cut_obligation_count": sum(
            row["creates_any_source_cut_obligation"] for row in records),
        "reconstruction_seconds": reconstruction_seconds,
        "kernel_seconds_total": sum(kernel_seconds),
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "projected_exhaustive_resource": projected,
        "evidence_class": "Executable verified — sampled finite scope",
        "scope": (
            "Eight deterministically selected exact physical bridge roots only. "
            "For each, exact old lower/upper kernels on both 18,676-event copies "
            "and old-atom folds are computed. No mixed closure, bridge-to-bridge "
            "cuts, centre, state, sigma, ODBC, MBRC, or Phi claim is made; the "
            "486-root estimate is a measured projection, not an execution."
        ),
        "verification_independence": (
            "One deterministic implementation reusing the authoritative exact "
            "bridge MDD producer and old-event order tables."
        ),
        "first_suspected_failure": (
            "The eight-root sample may understate kernel-time variance, especially "
            "for projection roots with larger reduced MDDs; coarse-bucket size is "
            "not established as a cost or mathematical-behaviour predictor."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "arr_forced_T_bridge_kernel_pilot.py --verify"
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
        # Timings and peak RSS are measurements rather than deterministic data;
        # verify all mathematical fields against the stored receipt.
        stored = json.loads(RECEIPT.read_text())
        volatile = {"reconstruction_seconds", "kernel_seconds_total",
                    "wall_seconds", "peak_rss_bytes_darwin", "payload_sha256"}
        def strip(value):
            value = dict(value)
            for key in volatile:
                value.pop(key, None)
            value["records"] = [{k: v for k, v in row.items()
                                  if k != "kernel_seconds"}
                                 for row in value["records"]]
            projection = dict(value["projected_exhaustive_resource"])
            for key in ("mean_selected_root_kernel_seconds",
                        "sequential_kernel_only_seconds",
                        "fixed_reconstruction_seconds_this_run",
                        "sequential_total_seconds_estimate"):
                projection.pop(key, None)
            value["projected_exhaustive_resource"] = projection
            return value
        assert strip(stored) == strip(out)
    print(json.dumps({
        "status": "PASS",
        "payload_sha256": out["payload_sha256"],
        "selected": out["selected_root_count"],
        "obligations": out["source_cut_obligation_count"],
        "kernel_seconds": out["kernel_seconds_total"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
