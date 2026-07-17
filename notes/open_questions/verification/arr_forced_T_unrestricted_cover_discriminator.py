#!/usr/bin/env python3
"""One-object unrestricted-cover discriminator for target 809b2d45...."""
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
SAMPLED_RECEIPT = HERE / "arr_forced_T_displayed_layer_audit.json"
RECEIPT = HERE / "arr_forced_T_unrestricted_cover_discriminator.json"


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
                      for name, root in bank["specials"].items()]
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
        return list(best.values())

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

    target = engine.app(0, physical_old(18406, "right"),
                        physical_old(17407, "left"))
    assert structural_hash(target).hex() == (
        "809b2d45da2e83aa06242789a4acf615f570373f5da80e8384b5d2c0f737bad2")
    lowers = [(physical_old(17082, "left"), "old_left(17082)"),
              (physical_old(18306, "right"), "old_right(18306)"),
              (bank["specials"]["S"], "S")]
    union = 0
    for root, _ in lowers:
        union = engine.app(1, union, root)
    residual = engine.app(0, target, engine.neg(union))
    overlaps = []
    for i, (a, alabel) in enumerate(lowers):
        for b, blabel in lowers[i + 1:]:
            overlap = engine.app(0, a, b)
            overlaps.append({"left": alabel, "right": blabel,
                             "exact_mdd_sha256": structural_hash(overlap).hex(),
                             "physical_cardinality": count_from(overlap, 0),
                             "empty": overlap == 0})

    lower_rows = current_extrema(union, "lower")
    upper_rows = current_extrema(union, "upper")
    represented = any(row[0] == union for row in lower_rows + upper_rows)
    unionc = engine.app(0, carrier, engine.neg(union))
    dual_lower = current_extrema(unionc, "lower")
    dual_upper = current_extrema(unionc, "upper")

    def labels(rows):
        return [{"label": label, "kind": kind} for _, label, kind in rows]

    base_receipt = json.loads(BASE_RECEIPT.read_text())
    sampled_receipt = json.loads(SAMPLED_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-T-unrestricted-cover-discriminator-v1",
        "schema_version": "1.0",
        "source_meet_payload_sha256": base_receipt["payload_sha256"],
        "source_sampled_payload_sha256": sampled_receipt["payload_sha256"],
        "target_exact_mdd_sha256": structural_hash(target).hex(),
        "target_physical_cardinality": count_from(target, 0),
        "full_union_exact_mdd_sha256": structural_hash(union).hex(),
        "full_union_physical_cardinality": count_from(union, 0),
        "full_union_equals_target": union == target,
        "full_union_subset_target": le(union, target),
        "full_union_residual_exact_mdd_sha256": structural_hash(residual).hex(),
        "full_union_residual_physical_cardinality": count_from(residual, 0),
        "pairwise_overlaps": overlaps,
        "full_union_already_represented": represented,
        "full_union_current_lower_extrema": labels(lower_rows),
        "full_union_current_upper_extrema": labels(upper_rows),
        "full_union_old_kernels": {side: kernel(union, side)
                                   for side in ("left", "right")},
        "complement_dual": {
            "union_complement_exact_mdd_sha256": structural_hash(unionc).hex(),
            "maximal_current_lowers": labels(dual_lower),
            "minimal_current_uppers": labels(dual_upper),
            "complements_of_union_maximal_lowers_equal_dual_minimal_uppers": (
                {engine.app(0, carrier, engine.neg(row[0])) for row in lower_rows} ==
                {row[0] for row in dual_upper}),
        },
        "reconstruction_seconds": reconstruction_seconds,
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "evidence_class": "Executable verified — exhaustive finite scope for one object",
        "scope": "Only the unrestricted union of the three certified maximal lowers of target 809b2d45 and its complement dual. No pair scan or closure.",
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
        assert ({k: v for k, v in stored.items() if k not in volatile} ==
                {k: v for k, v in out.items() if k not in volatile})
    print(json.dumps({"status": "PASS", "payload_sha256": out["payload_sha256"],
                      "equals_target": out["full_union_equals_target"],
                      "residual": out["full_union_residual_physical_cardinality"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
