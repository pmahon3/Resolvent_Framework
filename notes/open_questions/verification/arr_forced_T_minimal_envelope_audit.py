#!/usr/bin/env python3
"""Minimal-envelope adjunction audit for the first O-child proper-residual cut.

The banked O-child layer (payload fc9c0b22...) stops at the cut
meet(new_consequence(0),new_consequence(1)) whose two maximal represented
lowers U and old_left(4136) overlap and leave a proper residual.  This
producer adjoins exactly the minimal envelope ENV = U union old_left(4136)
and its complement, certifies that the displayed cut resolves at ENV with no
residual progress, classifies the immediate one-transition consequences and
their gate hazards, and records the first unresolved cut of the new envelope
seed layer.  It performs no interval enumeration and no closure round.
"""
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
SOURCE_RECEIPT = HERE / "arr_forced_T_forced_O_child_audit.json"
RECEIPT = HERE / "arr_forced_T_minimal_envelope_audit.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def load_base():
    spec = importlib.util.spec_from_file_location("_arr_envelope_base", BASE)
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
    assert len(events) == 18676
    root_by_class = {class_id: root for root, class_id
                     in bank["seen_roots"].items()}
    assert len(root_by_class) == 488
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

    kernel_cache = {}

    def kernel(target, side):
        key = (target, side)
        if key in kernel_cache:
            return kernel_cache[key]
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
        answer = {
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
        kernel_cache[key] = answer
        return answer

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

    def labels(rows):
        return [{"label": label, "kind": kind} for _, label, kind in rows]

    def dedup(rows):
        priority = {"old": 0, "special": 1, "new": 2, "consequence": 3}
        best = {}
        for row in rows:
            if row[0] not in best or priority[row[2]] < priority[best[row[0]][2]]:
                best[row[0]] = row
        return sorted(best.values(), key=lambda row: (
            row[2], row[1], structural_hash(row[0]).hex()))

    def old_extrema(target, mode):
        rows = []
        for side in ("left", "right"):
            report = kernel(target, side)
            indices = (report["maximal_old_lower_indices"] if mode == "lower"
                       else report["minimal_old_upper_indices"])
            rows += [(physical_old(i, side), f"old_{side}({i})", "old")
                     for i in indices]
        return rows

    def family_extrema(family, target, mode):
        rows = old_extrema(target, mode)
        rows += [row for row in family
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
                [rows for rows in exact if len(rows) == kappa]
                if kappa is not None else [],
        }

    # Gate battery: the same hazard observables used by the literal bridge
    # census.  A coordinate is activated exactly when its local cell state
    # charges all three shared activation atoms.
    states = old["states"]
    activated_states = {i for i, state in enumerate(states)
                        if {"a1", "a2", "a3"}.issubset(state)}
    activation_cylinders = [
        engine.app(0, carrier, engine.varset(variable, activated_states))
        for variable in range(7)]

    def cylindrical(root, side):
        eliminated = {4, 5, 6} if side == "left" else {0, 1, 2}
        existential = quantify_exists(root, eliminated)
        bad = engine.app(0, carrier, engine.neg(root))
        universal = engine.app(0, projection_carriers[side],
                               engine.neg(quantify_exists(bad, eliminated)))
        return existential == universal

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

    def gate_battery(root):
        return {
            "physical_cardinality": count_from(root, 0),
            "singleton_hazard": count_from(root, 0) == 1,
            "activation_supported_coordinates": [
                variable for variable, cylinder in
                enumerate(activation_cylinders) if le(root, cylinder)],
            "left_cylindrical": cylindrical(root, "left"),
            "right_cylindrical": cylindrical(root, "right"),
            "exact_old_representatives": [
                {"side": side, "index": index}
                for side, index in old_representatives(root)],
        }

    # --- Reconstruct the banked current family through the O-child layer. ---
    current_nonold = [(root, name, "special")
                      for name, root in sorted(bank["specials"].items())]
    current_nonold += [(root, f"root({class_id})", "new")
                       for class_id, root in sorted(root_by_class.items())]
    H = engine.app(0, root_by_class[8], root_by_class[106])
    Hc = engine.app(0, carrier, engine.neg(H))
    assert structural_hash(H).hex() == (
        "8a0a0f4b7ce3069459e8d782cec7bf0f9264b243277b032a93da795f8e289e93")
    current_nonold += [(H, "H", "consequence"), (Hc, "Hc", "consequence")]

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
    assert structural_hash(Uc).hex() == (
        "dded70d6569fcba1a9777a546498d576cc537f72c3ed643114576bb6291d86c1")

    # The six banked genuinely new O-child consequence roots, constructed
    # directly from their banked provenance formulas and pinned by hash.
    consequence_roots = [
        engine.app(1, U, physical_old(7568, "right")),
        engine.app(1, U, physical_old(13112, "left")),
        engine.app(1, U, physical_old(15248, "right")),
        engine.app(0, Uc, engine.neg(physical_old(13112, "left"))),
        engine.app(0, Uc, engine.neg(physical_old(15248, "right"))),
        engine.app(0, Uc, engine.neg(physical_old(7568, "right"))),
    ]
    consequence_roots.sort(key=lambda root: structural_hash(root))
    source_receipt = json.loads(SOURCE_RECEIPT.read_text())
    assert source_receipt["payload_sha256"] == (
        "fc9c0b2208a647b7753a092e9a8497061b64b7a4e48002709cb96e7e707fcec4")
    banked_new = source_receipt["genuinely_new_roots"]
    assert [structural_hash(root).hex() for root in consequence_roots] == [
        row["exact_mdd_sha256"] for row in banked_new]
    assert [count_from(root, 0) for root in consequence_roots] == [
        row["physical_cardinality"] for row in banked_new]
    new_rows = [(root, f"new_consequence({i})", "consequence")
                for i, root in enumerate(consequence_roots)]
    layer_nonold = dedup(current_nonold + [(U, "U", "consequence"),
                                           (Uc, "Uc", "consequence")] + new_rows)

    base_receipt = json.loads(BASE_RECEIPT.read_text())
    assert base_receipt["payload_sha256"] == (
        "304ed13bdb227944e6b18d61fb09588ed13d96996fc9d75fc62d7cb9d4df5957")

    # --- Reconfirm the banked first unresolved cut and its envelope. ---
    banked_cut = source_receipt["first_unresolved_seed_cut"]
    target_I = engine.app(0, consequence_roots[0], consequence_roots[1])
    assert structural_hash(target_I).hex() == banked_cut["target_exact_mdd_sha256"]
    assert count_from(target_I, 0) == banked_cut["target_physical_cardinality"]
    I_lowers = family_extrema(layer_nonold, target_I, "lower")
    assert labels(I_lowers) == banked_cut["extrema"]
    banked_cover = banked_cut["cover_discriminator"]
    recomputed_cover = cover_report(target_I, I_lowers)
    for key in ("maximal_lower_count", "maximal_lowers",
                "unrestricted_union_equals_target",
                "unrestricted_residual_exact_mdd_sha256",
                "unrestricted_residual_physical_cardinality",
                "pairwise_overlap_signature", "orthogonal_kappa",
                "orthogonal_minimum_residual_physical_cardinality"):
        assert recomputed_cover[key] == banked_cover[key], key
    residual = engine.app(0, target_I, engine.neg(
        engine.app(1, I_lowers[0][0], I_lowers[1][0])))
    overlap = engine.app(0, I_lowers[0][0], I_lowers[1][0])
    overlap_row = next((row for row in layer_nonold if row[0] == overlap), None)
    overlap_reps = old_representatives(overlap)

    # --- The one adjunction under audit: ENV = U union old_left(4136). ---
    by_label = {label: root for root, label, _ in I_lowers}
    ENV = engine.app(1, by_label["U"], by_label["old_left(4136)"])
    ENVc = engine.app(0, carrier, engine.neg(ENV))
    assert count_from(ENV, 0) == (
        banked_cut["target_physical_cardinality"]
        - banked_cover["unrestricted_residual_physical_cardinality"])
    layer_root_set = {row[0] for row in layer_nonold}
    assert ENV not in layer_root_set and not old_representatives(ENV)
    assert ENVc not in layer_root_set and not old_representatives(ENVc)

    ENV_lowers = family_extrema(layer_nonold, ENV, "lower")
    ENV_uppers = family_extrema(layer_nonold, ENV, "upper")
    ENVc_lowers = family_extrema(layer_nonold, ENVc, "lower")
    ENVc_uppers = family_extrema(layer_nonold, ENVc, "upper")
    ENV_cover = cover_report(ENV, ENV_lowers)
    assert ENV_cover["unrestricted_union_equals_target"]

    post_nonold = dedup(layer_nonold + [(ENV, "ENV", "consequence"),
                                        (ENVc, "ENVc", "consequence")])

    # Resolution certificate: the displayed cut and its complement-dual join
    # after the one adjunction.
    post_I_lowers = family_extrema(post_nonold, target_I, "lower")
    target_Ic = engine.app(0, carrier, engine.neg(target_I))
    post_Ic_uppers = family_extrema(post_nonold, target_Ic, "upper")
    resolution = {
        "post_adjunction_lower_extrema": labels(post_I_lowers),
        "displayed_cut_resolved_at_ENV":
            labels(post_I_lowers) == [{"label": "ENV", "kind": "consequence"}],
        "post_adjunction_dual_upper_extrema": labels(post_Ic_uppers),
        "dual_join_resolved_at_ENVc":
            labels(post_Ic_uppers) == [{"label": "ENVc", "kind": "consequence"}],
        "residual_exact_mdd_sha256": structural_hash(residual).hex(),
        "residual_physical_cardinality": count_from(residual, 0),
        "residual_untouched_by_ENV": engine.app(0, ENV, residual) == 0,
    }

    # --- Immediate one-transition consequences of the ENV,ENVc adjunction. ---
    post_root_set = {row[0] for row in post_nonold}
    occurrences = []
    for base_name, base_root, dual_root, lower_rows in (
            ("ENV", ENV, ENVc, ENV_lowers), ("ENVc", ENVc, ENV, ENVc_lowers)):
        for lower_root, lower_label, lower_kind in lower_rows:
            difference = engine.app(0, base_root, engine.neg(lower_root))
            bridge = engine.app(1, dual_root, lower_root)
            assert bridge == engine.app(0, carrier, engine.neg(difference))
            for operation, root in (("nested_difference", difference),
                                    ("dual_disjoint_union", bridge)):
                reps = old_representatives(root)
                already = root in post_root_set or bool(reps)
                occurrences.append({
                    "_root": root,
                    "base": base_name,
                    "source_lower": lower_label,
                    "source_lower_kind": lower_kind,
                    "operation": operation,
                    "exact_mdd_sha256": structural_hash(root).hex(),
                    "physical_cardinality": count_from(root, 0),
                    "already_current_after_adjunction": already,
                    "exact_old_representatives": [
                        {"side": side, "index": index} for side, index in reps],
                    "contained_in_displayed_target": le(root, target_I),
                    "contained_in_residual": le(root, residual),
                    "meets_residual": engine.app(0, root, residual) != 0,
                })

    occurrences.sort(key=lambda row: (
        row["base"], row["source_lower_kind"], row["source_lower"],
        row["operation"], row["exact_mdd_sha256"]))

    new_roots = {}
    for row in occurrences:
        if not row["already_current_after_adjunction"]:
            new_roots.setdefault(row["_root"], []).append({
                key: row[key] for key in ("base", "source_lower", "operation")})
    for provenance in new_roots.values():
        provenance.sort(key=lambda row: (row["base"], row["source_lower"],
                                         row["operation"]))
    env_new_rows = [(root, f"envelope_consequence({i})", "consequence")
                    for i, root in enumerate(sorted(
                        new_roots, key=lambda z: structural_hash(z)))]
    scan_nonold = dedup(post_nonold + env_new_rows)

    # Final-family recheck: do the envelope consequences reopen the cut?
    final_I_lowers = family_extrema(scan_nonold, target_I, "lower")
    residual_progress_roots = [
        label for root, label, _ in env_new_rows
        if le(root, target_I) and not le(root, ENV)]
    resolution["final_family_lower_extrema"] = labels(final_I_lowers)
    resolution["cut_reopened_by_consequences"] = (
        labels(final_I_lowers) != [{"label": "ENV", "kind": "consequence"}])

    # --- First unresolved cut of the new envelope seed layer. ---
    seeds = [(ENV, "ENV", "consequence"),
             (ENVc, "ENVc", "consequence")] + env_new_rows
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
                extrema = family_extrema(scan_nonold, target, mode)
                if len(extrema) != 1:
                    if operation == "meet":
                        cover_target = target
                        maxima = extrema
                        orientation = "direct"
                    else:
                        cover_target = engine.app(0, carrier, engine.neg(target))
                        maxima = family_extrema(scan_nonold, cover_target, "lower")
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

    # --- Gate battery and dichotomy verdict. ---
    gates = {"ENV": gate_battery(ENV), "ENVc": gate_battery(ENVc)}
    consequence_gates = {label: gate_battery(root)
                         for root, label, _ in env_new_rows}

    def hazardous(report):
        return (report["singleton_hazard"] or
                bool(report["activation_supported_coordinates"]) or
                report["left_cylindrical"] or report["right_cylindrical"] or
                bool(report["exact_old_representatives"]))

    envelope_gate_hazard = any(hazardous(report) for report in gates.values())
    # One nested difference and one dual disjoint union per maximal lower are
    # forced in every complement/disjoint-union-closed family containing the
    # adjunction, so a hazardous consequence is itself gate-forcing.
    consequence_gate_hazard = any(hazardous(report)
                                  for report in consequence_gates.values())
    gate_forcing = envelope_gate_hazard or consequence_gate_hazard
    residual_progress = (bool(residual_progress_roots) or
                         resolution["cut_reopened_by_consequences"])
    if gate_forcing:
        verdict = ("gate-forcing: the adjunction or one of its forced "
                   "one-transition consequences carries a hazard flag")
    elif residual_progress:
        verdict = "lower-ranked residual descent"
    else:
        verdict = ("zero-progress partial-envelope production: the declared "
                   "grammar gains an explicit PENV rule")

    # --- Pointed descriptor for the new PENV cell versus banked H and O. ---
    def consequence_signature(rows):
        return sorted([[row["exact_mdd_sha256"],
                        row["already_current_after_adjunction"]] for row in rows])

    ENV_signature = {
        "cover_size": ENV_cover["maximal_lower_count"],
        "cover_overlap_signature": ENV_cover["pairwise_overlap_signature"],
        "cover_unrestricted_residual_cardinality":
            ENV_cover["unrestricted_residual_physical_cardinality"],
        "parent_provenance_kinds": [row[2] for row in ENV_lowers],
        "current_extrema": {
            "object_lower": labels(ENV_lowers),
            "object_upper": labels(ENV_uppers),
            "complement_lower": labels(ENVc_lowers),
            "complement_upper": labels(ENVc_uppers),
        },
        "consequence_multiset_hash_membership": consequence_signature(
            occurrence_report),
        "dependency_depth": 4,
    }
    banked_pointed = source_receipt["pointed_H_O_comparison"]
    comparisons = {}
    for name in ("H", "O"):
        other = banked_pointed[f"{name}_descriptor"]
        differing = sorted(key for key in ENV_signature
                           if ENV_signature[key] != other[key])
        comparisons[name] = {
            "descriptor_tuples_equal": not differing,
            "differing_descriptor_fields": differing,
        }
        assert differing
    pointed_comparison = {
        "ENV_descriptor": ENV_signature,
        "banked_H_descriptor_source": "arr_forced_T_forced_O_child_audit.json",
        "versus_H": comparisons["H"],
        "versus_O": comparisons["O"],
        "explicit_pointed_isomorphism_search_attempted": False,
        "structural_pointed_isomorphism_status": "open",
        "isomorphism_status_reason": (
            "the recorded descriptors differ, but no category of pointed "
            "cells or exhaustive isomorphism search has been defined"),
        "verdict": "descriptor inequality only",
    }

    out = {
        "schema": "arr-forced-T-minimal-envelope-audit-v1",
        "schema_version": "1.0",
        "source_meet_payload_sha256": base_receipt["payload_sha256"],
        "source_o_child_payload_sha256": source_receipt["payload_sha256"],
        "banked_first_cut_reconfirmed": True,
        "displayed_cut": {
            "target_exact_mdd_sha256": structural_hash(target_I).hex(),
            "target_physical_cardinality": count_from(target_I, 0),
            "maximal_lowers": labels(I_lowers),
            "overlap_exact_mdd_sha256": structural_hash(overlap).hex(),
            "overlap_physical_cardinality": count_from(overlap, 0),
            "overlap_already_current": overlap_row is not None or
                bool(overlap_reps),
            "overlap_current_label": overlap_row[1] if overlap_row else None,
            "overlap_exact_old_representatives": [
                {"side": side, "index": index} for side, index in overlap_reps],
        },
        "ENV_exact_mdd_sha256": structural_hash(ENV).hex(),
        "ENVc_exact_mdd_sha256": structural_hash(ENVc).hex(),
        "ENV_cover": ENV_cover,
        "adjunction_resolution": resolution,
        "gate_battery": gates,
        "consequence_gate_battery": consequence_gates,
        "immediate_occurrence_count": len(occurrence_report),
        "immediate_occurrences": occurrence_report,
        "genuinely_new_exact_root_count": len(env_new_rows),
        "genuinely_new_roots": [{
            "label": label,
            "exact_mdd_sha256": structural_hash(root).hex(),
            "physical_cardinality": count_from(root, 0),
            "provenance": new_roots[root],
        } for root, label, _ in env_new_rows],
        "residual_progress_roots": residual_progress_roots,
        "seed_object_count": len(seeds),
        "tested_pair_count_before_stop": tested_pairs,
        "tested_operation_count_before_stop": tested_operations,
        "first_unresolved_seed_cut": first_cut,
        "pointed_PENV_comparison": pointed_comparison,
        "dichotomy_verdict": verdict,
        "envelope_gate_hazard": envelope_gate_hazard,
        "consequence_gate_hazard": consequence_gate_hazard,
        "gate_forcing": gate_forcing,
        "residual_progress": residual_progress,
        "reconstruction_seconds": reconstruction_seconds,
        "wall_seconds": time.perf_counter() - started,
        "peak_rss_bytes_darwin": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "evidence_class": ("Executable verified — exhaustive finite scope for "
                           "one declared minimal-envelope adjunction seed"),
        "scope": (
            "Only the banked O-child first cut, the single ENV,ENVc adjunction, "
            "its immediate nested/dual consequences with gate hazards, and the "
            "deterministic envelope-seed pair order (meet before join) through "
            "its first unresolved cut. No interval enumeration, closure round, "
            "full-layer first-cut claim, isomorphism theorem, latticehood, OML, "
            "centre, state, sigma, ODBC, MBRC, or Phi claim."
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
                      "verdict": out["dichotomy_verdict"],
                      "new_roots": out["genuinely_new_exact_root_count"],
                      "first_cut": out["first_unresolved_seed_cut"] is not None},
                     sort_keys=True))


if __name__ == "__main__":
    main()
