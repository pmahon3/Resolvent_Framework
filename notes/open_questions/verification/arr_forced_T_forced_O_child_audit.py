#!/usr/bin/env python3
"""Forced O-child audit and pointed comparison with the first H cell."""
import argparse
import functools
import hashlib
import importlib.util
import json
import math
import resource
import struct
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = HERE / "arr_forced_T_cross_root_meet_interval.py"
BASE_RECEIPT = HERE / "arr_forced_T_cross_root_meet_interval.json"
SOURCE_RECEIPT = HERE / "arr_forced_T_nonorthogonal_rebase_audit.json"
RECEIPT = HERE / "arr_forced_T_forced_O_child_audit.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def load_base():
    spec = importlib.util.spec_from_file_location("_arr_cover_base", BASE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def payload():
    started = time.perf_counter()
    base = load_base()
    bank = base.recover()
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
    root_index = {roots[event]: i for i, event in enumerate(events)}
    complement = {i: root_index[neg(roots[event])]
                  for i, event in enumerate(events)}

    def physical_old(index, side):
        return engine.app(0, carrier, lift(index, side))

    def projection(root, side):
        eliminated = {4, 5, 6} if side == "left" else {0, 1, 2}
        existential = quantify_exists(root, eliminated)
        bad = engine.app(0, carrier, engine.neg(root))
        universal = engine.app(0, projection_carriers[side],
                               engine.neg(quantify_exists(bad, eliminated)))
        return universal, existential

    def to_old_tuple(global_root, side):
        mapping = mappings[side]
        answer = []
        for macro_index, (_, domains) in enumerate(macros):
            target_engine = old_engines[macro_index]
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
                result = target_engine.node(old_variable, values)
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
        fold, escape = zero, None
        for atom in eligible:
            prior = fold
            fold = old_join(fold, atom)
            if escape is None and not subset(roots[events[fold]], universal):
                escape = {"prior_index": prior, "atom_index": atom,
                          "escaping_join_index": fold}
        return {
            "maximal_old_lower_indices": maximal,
            "greatest_old_lower_exists": len(maximal) == 1,
            "minimal_old_upper_indices": minimal,
            "least_old_upper_exists": len(minimal) == 1,
            "old_lower_count": len(lowers),
            "old_upper_count": len(dual_lowers),
            "eligible_old_atom_count": len(eligible),
            "atom_fold_index": fold,
            "atom_fold_inside_target": subset(roots[events[fold]], universal),
            "first_atom_fold_escape": escape,
            "universal_shadow_root_sha256": rhash(universal),
            "existential_shadow_root_sha256": rhash(existential),
        }

    current_nonold = [(root, name, "special")
                      for name, root in sorted(bank["specials"].items())]
    current_nonold += [(root, f"root({class_id})", "new")
                       for class_id, root in sorted(root_by_class.items())]
    H = engine.app(0, root_by_class[8], root_by_class[106])
    Hc = engine.app(0, carrier, engine.neg(H))
    current_nonold += [(H, "H", "consequence"), (Hc, "Hc", "consequence")]

    def old_extrema(target, mode):
        rows = []
        for side in ("left", "right"):
            report = kernel(target, side)
            indices = (report["maximal_old_lower_indices"] if mode == "lower"
                       else report["minimal_old_upper_indices"])
            rows += [(physical_old(i, side), f"old_{side}({i})", "old")
                     for i in indices]
        return rows

    def dedup(rows):
        priority = {"old": 0, "special": 1, "new": 2, "consequence": 3}
        best = {}
        for row in rows:
            if row[0] not in best or priority[row[2]] < priority[best[row[0]][2]]:
                best[row[0]] = row
        return sorted(best.values(), key=lambda row: (
            row[2], row[1], structural_hash(row[0]).hex()))

    def current_extrema(target, mode):
        rows = old_extrema(target, mode)
        rows += [row for row in current_nonold
                 if (le(row[0], target) if mode == "lower" else le(target, row[0]))]
        rows = dedup(rows)
        return sorted([row for row in rows if not any(
            other[0] != row[0] and
            (le(row[0], other[0]) if mode == "lower" else le(other[0], row[0]))
            for other in rows)], key=lambda row: (row[2], row[1]))

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
            return root * math.prod(len(engine.domains[v]) for v in range(level, 7))
        variable, children = engine.nodes[root]
        skipped = math.prod(len(engine.domains[v]) for v in range(level, variable))
        return skipped * sum(count_from(child, variable + 1) for child in children)

    parent_U = engine.app(0, physical_old(18406, "right"),
                          physical_old(17407, "left"))
    assert structural_hash(parent_U).hex() == (
        "809b2d45da2e83aa06242789a4acf615f570373f5da80e8384b5d2c0f737bad2")
    parent_Uc = engine.app(0, carrier, engine.neg(parent_U))
    root487 = root_by_class[487]
    special_S = bank["specials"]["S"]
    parent_new = [
        engine.app(1, parent_U, root487),
        engine.app(0, parent_Uc, engine.neg(root487)),
        engine.app(1, parent_Uc, special_S),
        engine.app(0, parent_U, engine.neg(special_S)),
    ]
    assert [structural_hash(root).hex() for root in parent_new] == [
        "0ca4aa198580387deb73ed1aed70300f92c003935ea247ac4d811aba77c48ba6",
        "95232f9c77afd7ddd7a641f9017ea9ae6b87fe5219bc35d7f35b28bd8c90ddbc",
        "a95fec543af6e72a3ef762739f5f1d181c1e4219ca0ca3c163aa2db4a496a3fc",
        "f1778d59f3a12373ecc0d3f8c9eb0149a592633b01f26b13c2692e433792275f",
    ]
    current_nonold += [(parent_U, "parent_U", "consequence"),
                       (parent_Uc, "parent_Uc", "consequence")]
    current_nonold += [(root, f"parent_new({i})", "consequence")
                       for i, root in enumerate(parent_new)]
    U = engine.app(1, root487, special_S)
    assert structural_hash(U).hex() == (
        "803fd9af09b4285b21d2614b1556ed15e9c853fa220fd252874c4eac4692d187")
    Uc = engine.app(0, carrier, engine.neg(U))

    def labels(rows):
        return [{"label": label, "kind": kind} for _, label, kind in rows]

    @functools.lru_cache(None)
    def old_representatives(target):
        answer = []
        for side in ("left", "right"):
            report = kernel(target, side)
            lo, hi = (report["maximal_old_lower_indices"],
                      report["minimal_old_upper_indices"])
            if len(lo) == len(hi) == 1 and lo[0] == hi[0]:
                if physical_old(lo[0], side) == target:
                    answer.append({"side": side, "index": lo[0]})
        return tuple((row["side"], row["index"]) for row in answer)

    base_root_set = {row[0] for row in current_nonold}
    U_lowers = current_extrema(U, "lower")
    U_uppers = current_extrema(U, "upper")
    Uc_lowers = current_extrema(Uc, "lower")
    Uc_uppers = current_extrema(Uc, "upper")
    assert labels(U_lowers) == [
        {"label": "root(487)", "kind": "new"},
        {"label": "S", "kind": "special"},
    ]

    occurrences = []
    for base_name, base_root, dual_root, lower_rows in (
            ("U", U, Uc, U_lowers), ("Uc", Uc, U, Uc_lowers)):
        for lower_root, lower_label, lower_kind in lower_rows:
            difference = engine.app(0, base_root, engine.neg(lower_root))
            bridge = engine.app(1, dual_root, lower_root)
            assert bridge == engine.app(0, carrier, engine.neg(difference))
            for operation, root in (("nested_difference", difference),
                                    ("dual_disjoint_union", bridge)):
                reps = old_representatives(root)
                already = root in base_root_set or root in {U, Uc} or bool(reps)
                occurrences.append({
                    "_root": root,
                    "base": base_name,
                    "source_lower": lower_label,
                    "source_lower_kind": lower_kind,
                    "operation": operation,
                    "exact_mdd_sha256": structural_hash(root).hex(),
                    "physical_cardinality": count_from(root, 0),
                    "already_current_after_rebase": already,
                    "exact_old_representatives": [
                        {"side": side, "index": index} for side, index in reps],
                })

    occurrences.sort(key=lambda row: (
        row["base"], row["source_lower_kind"], row["source_lower"],
        row["operation"], row["exact_mdd_sha256"]))

    new_roots = {}
    for row in occurrences:
        if not row["already_current_after_rebase"]:
            new_roots.setdefault(row["_root"], []).append({
                key: row[key] for key in ("base", "source_lower", "operation")})
    for provenance in new_roots.values():
        provenance.sort(key=lambda row: (row["base"], row["source_lower"],
                                         row["operation"]))
    new_rows = [(root, f"new_consequence({i})", "consequence")
                for i, root in enumerate(sorted(new_roots,
                                                key=lambda z: structural_hash(z)))]
    layer_nonold = dedup(current_nonold + [(U, "U", "consequence"),
                                           (Uc, "Uc", "consequence")] + new_rows)

    def layer_extrema(target, mode):
        rows = old_extrema(target, mode)
        rows += [row for row in layer_nonold
                 if (le(row[0], target) if mode == "lower" else le(target, row[0]))]
        rows = dedup(rows)
        return sorted([row for row in rows if not any(
            other[0] != row[0] and
            (le(row[0], other[0]) if mode == "lower" else le(other[0], row[0]))
            for other in rows)], key=lambda row: (row[2], row[1]))

    def cover_report(target, maxima):
        n = len(maxima)
        assert n <= 20
        unrestricted = 0
        for row in maxima:
            unrestricted = engine.app(1, unrestricted, row[0])
        unrestricted_residual = engine.app(0, target, engine.neg(unrestricted))
        overlaps = []
        for i, left in enumerate(maxima):
            for right in maxima[i + 1:]:
                overlap = engine.app(0, left[0], right[0])
                overlaps.append({"left": left[1], "right": right[1],
                                 "exact_mdd_sha256": structural_hash(overlap).hex(),
                                 "physical_cardinality": count_from(overlap, 0),
                                 "empty": overlap == 0})
        overlaps.sort(key=lambda row: (row["left"], row["right"],
                                       row["exact_mdd_sha256"]))
        best_size, best_hashes, exact = None, set(), []
        orthogonal_count = 0
        for mask in range(1 << n):
            chosen = [maxima[i] for i in range(n) if mask & (1 << i)]
            if any(engine.app(0, a[0], b[0]) != 0
                   for i, a in enumerate(chosen) for b in chosen[i + 1:]):
                continue
            orthogonal_count += 1
            union = 0
            for row in chosen:
                union = engine.app(1, union, row[0])
            residual = engine.app(0, target, engine.neg(union))
            size = count_from(residual, 0)
            rh = structural_hash(residual).hex()
            if best_size is None or size < best_size:
                best_size, best_hashes = size, {rh}
            elif size == best_size:
                best_hashes.add(rh)
            if residual == 0:
                exact.append(labels(chosen))
        kappa = min((len(rows) for rows in exact), default=None)
        exact.sort(key=lambda rows: json.dumps(rows, sort_keys=True,
                                               separators=(",", ":")))
        return {
            "maximal_lower_count": n,
            "maximal_lowers": labels(maxima),
            "unrestricted_union_equals_target": unrestricted == target,
            "unrestricted_residual_exact_mdd_sha256":
                structural_hash(unrestricted_residual).hex(),
            "unrestricted_residual_physical_cardinality":
                count_from(unrestricted_residual, 0),
            "pairwise_overlap_signature": overlaps,
            "orthogonal_subset_search": "exhaustive",
            "orthogonal_subset_count": orthogonal_count,
            "orthogonal_kappa": kappa if kappa is not None else "infinity",
            "orthogonal_minimum_residual_physical_cardinality": best_size,
            "orthogonal_minimum_residual_exact_mdd_sha256s": sorted(best_hashes),
            "orthogonal_minimum_exact_covers":
                [rows for rows in exact if len(rows) == kappa] if kappa is not None else [],
        }

    seeds = [(U, "U", "consequence"), (Uc, "Uc", "consequence")] + new_rows
    first_cut = None
    tested_pairs = tested_operations = 0
    for i, left in enumerate(seeds):
        for right in seeds[i + 1:]:
            tested_pairs += 1
            for operation, target in (
                    ("meet", engine.app(0, left[0], right[0])),
                    ("join", engine.app(1, left[0], right[0]))):
                tested_operations += 1
                mode = "lower" if operation == "meet" else "upper"
                extrema = layer_extrema(target, mode)
                if len(extrema) != 1:
                    if operation == "meet":
                        cover_target = target
                        maxima = extrema
                        orientation = "direct"
                    else:
                        cover_target = engine.app(0, carrier, engine.neg(target))
                        maxima = layer_extrema(cover_target, "lower")
                        orientation = "complement-dual"
                    first_cut = {
                        "left": left[1], "right": right[1],
                        "operation": operation, "orientation": orientation,
                        "target_exact_mdd_sha256": structural_hash(target).hex(),
                        "target_physical_cardinality": count_from(target, 0),
                        "extrema": labels(extrema),
                        "cover_discriminator": cover_report(cover_target, maxima),
                    }
                    break
            if first_cut is not None:
                break
        if first_cut is not None:
            break

    occurrence_report = [{k: v for k, v in row.items() if k != "_root"}
                         for row in occurrences]

    H = engine.app(0, root_by_class[8], root_by_class[106])
    Hc = engine.app(0, carrier, engine.neg(H))
    H_lowers = [(physical_old(1024, "left"), "old_left(1024)", "old"),
                (physical_old(2, "right"), "old_right(2)", "old")]
    H_cover = cover_report(H, H_lowers)
    O_cover = cover_report(U, U_lowers)

    base_receipt = json.loads(BASE_RECEIPT.read_text())
    source_receipt = json.loads(SOURCE_RECEIPT.read_text())
    assert base_receipt["payload_sha256"] == (
        "304ed13bdb227944e6b18d61fb09588ed13d96996fc9d75fc62d7cb9d4df5957")
    assert source_receipt["payload_sha256"] == (
        "63cfb83d72a5e97f1367ee0fa00087bce694c270e4d05392cc3ad9a5299fe08e")

    def consequence_signature(rows):
        return sorted([[row["exact_mdd_sha256"],
                        row.get("already_current_after_rebase",
                                row.get("already_current"))] for row in rows])

    H_extrema = base_receipt["current_family_extrema"]
    H_signature = {
        "cover_size": H_cover["maximal_lower_count"],
        "cover_overlap_signature": H_cover["pairwise_overlap_signature"],
        "cover_unrestricted_residual_cardinality":
            H_cover["unrestricted_residual_physical_cardinality"],
        "parent_provenance_kinds": ["old", "old"],
        "current_extrema": {
            "object_lower": H_extrema["H"]["lower_extrema"],
            "object_upper": H_extrema["H"]["upper_extrema"],
            "complement_lower": H_extrema["Hc"]["lower_extrema"],
            "complement_upper": H_extrema["Hc"]["upper_extrema"],
        },
        "consequence_multiset_hash_membership": consequence_signature(
            base_receipt["immediate_one_transition_consequences"]),
        "dependency_depth": 1,
    }
    O_signature = {
        "cover_size": O_cover["maximal_lower_count"],
        "cover_overlap_signature": O_cover["pairwise_overlap_signature"],
        "cover_unrestricted_residual_cardinality":
            O_cover["unrestricted_residual_physical_cardinality"],
        "parent_provenance_kinds": [row[2] for row in U_lowers],
        "current_extrema": {
            "object_lower": labels(U_lowers),
            "object_upper": labels(U_uppers),
            "complement_lower": labels(Uc_lowers),
            "complement_upper": labels(Uc_uppers),
        },
        "consequence_multiset_hash_membership": consequence_signature(
            occurrence_report),
        "dependency_depth": 3,
    }
    differing_descriptor_fields = sorted(key for key in H_signature
                                         if H_signature[key] != O_signature[key])
    descriptor_tuples_equal = not differing_descriptor_fields
    assert not descriptor_tuples_equal
    pointed_comparison = {
        "H_descriptor": H_signature,
        "O_descriptor": O_signature,
        "descriptor_tuples_equal": descriptor_tuples_equal,
        "differing_descriptor_fields": differing_descriptor_fields,
        "explicit_pointed_isomorphism_search_attempted": False,
        "structural_pointed_isomorphism_status": "open",
        "isomorphism_status_reason": (
            "the recorded descriptors differ, but no category of pointed "
            "cells or exhaustive isomorphism search has been defined"),
        "verdict": "descriptor inequality only",
    }

    out = {
        "schema": "arr-forced-T-forced-O-child-audit-v1",
        "schema_version": "1.0",
        "source_meet_payload_sha256": base_receipt["payload_sha256"],
        "source_parent_rebase_payload_sha256": source_receipt["payload_sha256"],
        "O_exact_mdd_sha256": structural_hash(U).hex(),
        "Oc_exact_mdd_sha256": structural_hash(Uc).hex(),
        "pre_rebase_O_maximal_lowers": labels(U_lowers),
        "pre_rebase_Oc_maximal_lowers": labels(Uc_lowers),
        "exact_containment": {
            "O_subset_parent_U": le(U, parent_U),
            "parent_U_subset_O": le(parent_U, U),
            "O_proper_subset_parent_U": le(U, parent_U) and U != parent_U,
            "O_subset_parent_Uc": le(U, parent_Uc),
            "parent_Uc_subset_O": le(parent_Uc, U),
            "O_subset_H": le(U, H),
            "H_subset_O": le(H, U),
            "O_proper_subset_H": le(U, H) and U != H,
            "H_exact_mdd_sha256": structural_hash(H).hex(),
            "parent_U_exact_mdd_sha256": structural_hash(parent_U).hex(),
        },
        "immediate_occurrence_count": len(occurrence_report),
        "immediate_occurrences": occurrence_report,
        "genuinely_new_exact_root_count": len(new_rows),
        "genuinely_new_roots": [{
            "label": label,
            "exact_mdd_sha256": structural_hash(root).hex(),
            "physical_cardinality": count_from(root, 0),
            "provenance": new_roots[root],
        } for root, label, _ in new_rows],
        "seed_object_count": len(seeds),
        "tested_pair_count_before_stop": tested_pairs,
        "tested_operation_count_before_stop": tested_operations,
        "first_unresolved_seed_cut": first_cut,
        "pointed_H_O_comparison": pointed_comparison,
        "reconstruction_seconds": reconstruction_seconds,
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "evidence_class": "Executable verified — exhaustive finite scope for one forced O-child seed layer",
        "scope": (
            "Only O,Oc immediate nested/dual consequences and the deterministic "
            "eight-seed pair order (meet before join) through its first unresolved "
            "cut; descriptor-tuple comparison versus H only. No unrelated pair "
            "scan, full-layer first-cut claim, isomorphism theorem, or closure."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
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
        left = {k: v for k, v in stored.items() if k not in volatile}
        right = {k: v for k, v in out.items() if k not in volatile}

        def mismatch_paths(a, b, path="$"):
            if type(a) is not type(b):
                return [path + f" [type {type(a).__name__}!={type(b).__name__}]"]
            if isinstance(a, dict):
                paths = []
                for key in sorted(set(a) | set(b)):
                    if key not in a or key not in b:
                        paths.append(path + "." + key + " [missing]")
                    else:
                        paths += mismatch_paths(a[key], b[key], path + "." + key)
                return paths
            if isinstance(a, list):
                if len(a) != len(b):
                    return [path + f" [length {len(a)}!={len(b)}]"]
                paths = []
                for i, (x, y) in enumerate(zip(a, b)):
                    paths += mismatch_paths(x, y, path + f"[{i}]")
                return paths
            return [] if a == b else [path + f" [{a!r}!={b!r}]"]

        if left != right:
            print(json.dumps({"status": "MISMATCH",
                              "paths": mismatch_paths(left, right)[:100]},
                             sort_keys=True))
        assert left == right
    print(json.dumps({"status": "PASS", "payload_sha256": out["payload_sha256"],
                      "new_roots": out["genuinely_new_exact_root_count"],
                      "first_cut": out["first_unresolved_seed_cut"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
