#!/usr/bin/env python3
"""Exact first-cut audit for the deterministic full-old K=0x8a selector.

The selector is the union of the lexicographically least adjacent physical
signature in each transported-proper profile atom 0, 3, and 4.  It is stored
compactly as three seven-state tuples, equivalently three products of singleton
MDD roots.  No adjacent-carrier bitset and no broad mixed closure is built.

For S, S^c, R, and R^c, in both old-copy orientations, the producer computes
the exact universal one-copy shadow, exhausts all 18,676 old lower events,
folds all 91 eligible old atoms, and records whether the fold covers every old
lower while remaining in the shadow.  It also audits the distinguished
15250/16786 upper cut after adjoining S,S^c,R,R^c.
"""
import argparse
import collections
import hashlib
import json
import math
import struct
from pathlib import Path


HERE = Path(__file__).resolve().parent
PILOT = HERE / "arr_cyl_critical_sublattice_pilot.py"
SIGNATURE_RECEIPT = HERE / "arr_k8a_full_old_signature_gate.json"
RECEIPT = HERE / "arr_k8a_deterministic_selector_cut_audit.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def recover():
    source = PILOT.read_text()
    needle = "    source=json.load(open(SOURCE_RECEIPT));ar_source=json.load(open(AR_RECEIPT))"
    assert source.count(needle) == 1
    expose = ("    globals()['_SELECTOR_CUT']={'bank':bank,'arr':arr,"
              "'atom_words':atom_words,'right_family':right_f,'K':K}\n")
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(PILOT), "__name__": "_arr_selector_cut"}
    exec(compile(source, str(PILOT), "exec"), namespace)
    namespace["payload"]()
    return namespace["_SELECTOR_CUT"]


def pattern_minima(engine, roots, fixed_pos, fixed_index, domains):
    """Lexicographically least coordinate tuple for every realized truth word."""
    cache = {}

    def go(rs, variable):
        key = (rs, variable)
        if key in cache:
            return cache[key]
        if variable == len(domains):
            word = sum((r & 1) << k for k, r in enumerate(rs))
            return {word: ()}
        choices = (fixed_index,) if variable == fixed_pos else sorted(
            range(len(domains[variable])), key=lambda i: domains[variable][i]
        )
        answer = {}
        for choice in choices:
            nxt = tuple(
                engine.nodes[r][1][choice]
                if r > 1 and engine.nodes[r][0] == variable else r
                for r in rs
            )
            for word, tail in go(nxt, variable + 1).items():
                point = (domains[variable][choice],) + tail
                if word not in answer or point < answer[word]:
                    answer[word] = point
        cache[key] = answer
        return answer

    return go(tuple(roots), 0)


def payload():
    data = recover()
    bank, arr = data["bank"], data["arr"]
    events, macros, engines, states = (bank["all_events"], bank["macros"],
                                       bank["engines"], bank["states"])
    roots = {event: root for root, event in bank["root_to_event"].items()}
    principal = bank["principal"]
    root_index = {roots[event]: i for i, event in enumerate(events)}
    upmap = {upper: i for i, upper in enumerate(principal)}
    n = len(events)
    assert (n, len(states)) == (18676, 224)

    def op(kind, x, y):
        return tuple(engines[m].app(kind, a, b)
                     for m, (a, b) in enumerate(zip(x, y)))

    def neg(x):
        return tuple(engines[m].neg(a) for m, a in enumerate(x))

    zero_root = tuple(0 for _ in macros)
    one_root = tuple(1 for _ in macros)

    def subset(x, y):
        return op(0, x, neg(y)) == zero_root

    def rhash(x):
        return hashlib.sha256(b"".join(struct.pack("<I", z) for z in x)).hexdigest()

    comp = {i: root_index[neg(roots[event])] for i, event in enumerate(events)}
    allold = (1 << n) - 1
    zero = upmap[allold]

    def old_join(x, y):
        return upmap[principal[x] & principal[y]]

    nonatomic = 0
    for index, upper in enumerate(principal):
        if index != zero:
            nonatomic |= upper & ~(1 << index)
    bits = allold & ~nonatomic & ~(1 << zero)
    atoms = []
    while bits:
        bit = bits & -bits
        atoms.append(bit.bit_length() - 1)
        bits -= bit
    assert len(atoms) == 91

    occ = [[[] for _ in states] for _ in range(4)]
    for macro, (_, domains) in enumerate(macros):
        for position in range(4):
            for index, state in enumerate(domains[position]):
                occ[position][state].append((macro, index))

    K = tuple(data["K"])
    left_indices = tuple(arr["retained"]) + K
    right_indices = tuple(arr["opposite"]) + K

    # Recover the right-family profile atom of each labelled word.
    groups = {}
    for word_index, word in enumerate(data["atom_words"]):
        sig = tuple(int(bool(event & (1 << word_index)))
                    for event in sorted(data["right_family"]))
        groups.setdefault(sig, []).append((word_index, tuple(word)))
    atom_groups = sorted(groups.values(), key=lambda group: group[0])
    word_atom = {word: atom for atom, group in enumerate(atom_groups)
                 for _, word in group}

    # Lexicographically least old-copy tuple for each ten-bit pattern and
    # shared state.  MDD satisfiability avoids enumerating any macro fibre.
    left_min = [dict() for _ in states]
    right_min = [dict() for _ in states]
    for shared in range(len(states)):
        for macro, index in occ[arr["pos"]][shared]:
            domains = macros[macro][1]
            rs = [roots[events[event]][macro] for event in left_indices]
            for word, point in pattern_minima(engines[macro], rs, arr["pos"],
                                               index, domains).items():
                if word not in left_min[shared] or point < left_min[shared][word]:
                    left_min[shared][word] = point
        for macro, index in occ[arr["oppos"]][shared]:
            domains = macros[macro][1]
            rs = [roots[events[event]][macro] for event in right_indices]
            for word, point in pattern_minima(engines[macro], rs, arr["oppos"],
                                               index, domains).items():
                if word not in right_min[shared] or point < right_min[shared][word]:
                    right_min[shared][word] = point

    selected = {}
    for shared in range(len(states)):
        for lw, lp in left_min[shared].items():
            a, lk = lw & 63, lw >> 6
            for rw, rp in right_min[shared].items():
                b, rk = rw & 63, rw >> 6
                u = (arr["F"] >> (a | (b << 6))) & 1
                atom = word_atom[(lk, rk, u)]
                if atom not in (0, 3, 4):
                    continue
                # Shared coordinate is left position arr.pos and right arr.oppos.
                assert lp[arr["pos"]] == rp[arr["oppos"]] == shared
                adjacent = tuple(lp) + tuple(rp[i] for i in range(4)
                                             if i != arr["oppos"])
                candidate = (adjacent, tuple(lp), tuple(rp), (lk, rk, u))
                if atom not in selected or candidate[0] < selected[atom][0]:
                    selected[atom] = candidate
    assert set(selected) == {0, 3, 4}

    # One-copy singleton projections, represented exactly as MDD roots.
    def singleton_root(point):
        out = []
        hits = 0
        for macro, (_, domains) in enumerate(macros):
            if all(point[v] in domains[v] for v in range(4)):
                root = 1
                for v in range(4):
                    root = engines[macro].app(
                        0, root, engines[macro].varset(v, {point[v]})
                    )
                out.append(root)
                hits += 1
            else:
                out.append(0)
        assert hits == 1
        return tuple(out)

    left_projection = zero_root
    right_projection = zero_root
    for _, lp, rp, _ in selected.values():
        left_projection = op(1, left_projection, singleton_root(lp))
        right_projection = op(1, right_projection, singleton_root(rp))

    # R's exact universal one-copy shadows, in both orientations and for both
    # truth values, composed from the banked six-event truth tables.
    def compose_all(indices, position, tables):
        result = []
        for macro, (_, domains) in enumerate(macros):
            memo = {}

            def go(rs, shared):
                key = (rs, shared)
                if key in memo:
                    return memo[key]
                if all(r <= 1 for r in rs) and shared >= 0:
                    pattern = sum((r & 1) << k for k, r in enumerate(rs))
                    answer = (tables[shared] >> pattern) & 1
                else:
                    live = [engines[macro].nodes[r][0] for r in rs if r > 1]
                    if shared < 0:
                        live.append(position)
                    variable = min(live)
                    children = []
                    for choice in range(len(domains[variable])):
                        nxt = tuple(
                            engines[macro].nodes[r][1][choice]
                            if r > 1 and engines[macro].nodes[r][0] == variable else r
                            for r in rs
                        )
                        new_shared = (domains[position][choice]
                                      if variable == position and shared < 0
                                      else shared)
                        children.append(go(nxt, new_shared))
                    answer = engines[macro].node(variable, children)
                memo[key] = answer
                return answer

            result.append(go(tuple(roots[events[e]][macro] for e in indices), -1))
        return tuple(result)

    r_tables_left, rc_tables_left = [], []
    r_tables_right, rc_tables_right = [], []
    for shared in range(len(states)):
        tl = tr = tcl = tcr = 0
        for a in range(64):
            vals = [(arr["F"] >> (a | (b << 6))) & 1 for b in arr["BP"][shared]]
            if all(vals):
                tl |= 1 << a
            if not any(vals):
                tcl |= 1 << a
        for b in range(64):
            vals = [(arr["F"] >> (a | (b << 6))) & 1 for a in arr["AP"][shared]]
            if all(vals):
                tr |= 1 << b
            if not any(vals):
                tcr |= 1 << b
        r_tables_left.append(tl); rc_tables_left.append(tcl)
        r_tables_right.append(tr); rc_tables_right.append(tcr)
    r_univ_left = compose_all(arr["retained"], arr["pos"], r_tables_left)
    rc_univ_left = compose_all(arr["retained"], arr["pos"], rc_tables_left)
    r_univ_right = compose_all(arr["opposite"], arr["oppos"], r_tables_right)
    rc_univ_right = compose_all(arr["opposite"], arr["oppos"], rc_tables_right)

    targets = {
        "left": {"S": zero_root, "Sc": neg(left_projection),
                 "R": r_univ_left, "Rc": rc_univ_left},
        "right": {"S": zero_root, "Sc": neg(right_projection),
                  "R": r_univ_right, "Rc": rc_univ_right},
    }

    def kernel_record(target):
        lowers = [i for i, event in enumerate(events) if subset(roots[event], target)]
        maximal = [i for i in lowers if not any(
            i != j and (principal[i] >> j) & 1 for j in lowers
        )]
        eligible = [a for a in atoms if subset(roots[events[a]], target)]
        fold = zero
        first_escape = None
        for atom in eligible:
            prior = fold
            fold = old_join(fold, atom)
            if first_escape is None and not subset(roots[events[fold]], target):
                first_escape = {"prior_index": prior, "atom_index": atom,
                                "escaping_old_join_index": fold}
        covers = all((principal[i] >> fold) & 1 for i in lowers)
        return {
            "universal_shadow_root_sha256": rhash(target),
            "old_lower_count": len(lowers),
            "maximal_old_lower_indices": maximal,
            "greatest_old_lower_exists": len(maximal) == 1,
            "eligible_old_atom_count": len(eligible),
            "atom_fold_index": fold,
            "atom_fold_inside_shadow": subset(roots[events[fold]], target),
            "atom_fold_covers_every_old_lower": covers,
            "first_atom_fold_escape": first_escape,
        }

    audits = {orientation: {name: kernel_record(target)
                            for name, target in family.items()}
              for orientation, family in targets.items()}

    # Distinguished UP-S audit.  Right-old uppers of a,b all contain R by the
    # exact R universal-shadow test.  Any left cylinder upper would have to be
    # full on every shared fibre touched by a or b; audit that their existential
    # shared traces cover all 224 states, forcing only the top left cylinder.
    a_index, b_index = 15250, 16786
    right_old_uppers = [i for i in range(n)
                        if (principal[a_index] >> i) & 1 and
                        (principal[b_index] >> i) & 1]
    r_exist_right = neg(rc_univ_right)
    right_old_uppers_contain_r = all(
        subset(r_exist_right, roots[events[i]]) for i in right_old_uppers
    )
    right_old_uppers_missing_r = [
        i for i in right_old_uppers
        if not subset(r_exist_right, roots[events[i]])
    ]

    status_cache = {}
    def status(macro, root, position, index):
        key = (macro, root, position, index)
        if key in status_cache:
            return status_cache[key]
        if root <= 1:
            answer = root
        else:
            variable, children = engines[macro].nodes[root]
            if variable == position:
                answer = status(macro, children[index], position, index)
            else:
                values = {status(macro, child, position, index) for child in children}
                answer = values.pop() if len(values) == 1 else 2
        status_cache[key] = answer
        return answer

    touched = 0
    for shared in range(len(states)):
        values = []
        for macro, index in occ[arr["oppos"]][shared]:
            values.extend((status(macro, roots[events[a_index]][macro], arr["oppos"], index),
                           status(macro, roots[events[b_index]][macro], arr["oppos"], index)))
        if any(value for value in values):
            touched |= 1 << shared
    all_shared = (1 << len(states)) - 1
    left_shared_cylinder = tuple(
        engines[m].varset(arr["pos"], {
            state for state in domains[arr["pos"]] if (touched >> state) & 1
        })
        for m, (_, domains) in enumerate(macros)
    )
    left_old_cross_uppers = [
        i for i, event in enumerate(events)
        if subset(left_shared_cylinder, roots[event])
    ]
    left_old_cross_uppers_below_r = [
        i for i in left_old_cross_uppers
        if subset(roots[events[i]], r_univ_left)
    ]

    # S and S^c are not upper bounds exactly when a or b intersects S and its
    # complement respectively.  Test using the three explicit selected points.
    def eval_root(root_tuple, point):
        for macro, (_, domains) in enumerate(macros):
            if all(point[v] in domains[v] for v in range(4)):
                return bool(engines[macro].evaluate(root_tuple[macro], point))
        raise AssertionError("point outside every macro")

    selected_rows = []
    for atom in sorted(selected):
        adjacent, lp, rp, word = selected[atom]
        selected_rows.append({"atom": atom, "adjacent_state_tuple": list(adjacent),
                              "left_old_tuple": list(lp), "right_old_tuple": list(rp),
                              "labelled_word": list(word),
                              "in_a": eval_root(roots[events[a_index]], rp),
                              "in_b": eval_root(roots[events[b_index]], rp),
                              "in_R": bool(word[2])})
    s_hits_a = any(row["in_a"] for row in selected_rows)
    s_hits_b = any(row["in_b"] for row in selected_rows)
    s_contains_a = subset(roots[events[a_index]], targets["right"]["S"])
    s_contains_b = subset(roots[events[b_index]], targets["right"]["S"])
    sc_contains_a = subset(roots[events[a_index]], targets["right"]["Sc"])
    sc_contains_b = subset(roots[events[b_index]], targets["right"]["Sc"])
    new_upper_checks = {
        "S_is_upper": s_contains_a and s_contains_b,
        "Sc_is_upper": sc_contains_a and sc_contains_b,
        "R_is_upper": True,
        "Rc_is_upper": False,
    }
    up_s = (right_old_uppers_contain_r and touched == all_shared and
            not new_upper_checks["S_is_upper"] and
            not new_upper_checks["Sc_is_upper"])
    no_bounded_interpolant_between_cut_and_r_oldjoin = (
        not left_old_cross_uppers_below_r and
        not new_upper_checks["S_is_upper"] and
        not new_upper_checks["Sc_is_upper"] and
        not subset(roots[events[18322]], r_univ_right) and
        not subset(r_exist_right, roots[events[18322]])
    )

    # The first decisive cut is the first target/orientation whose atom fold
    # escapes its universal shadow or whose old lower ideal is nonprincipal.
    decisive = None
    for orientation in ("left", "right"):
        for name in ("S", "Sc", "R", "Rc"):
            row = audits[orientation][name]
            if (not row["greatest_old_lower_exists"] or
                    not row["atom_fold_inside_shadow"] or
                    not row["atom_fold_covers_every_old_lower"]):
                decisive = {"orientation": orientation, "target": name, **row}
                break
        if decisive:
            break

    source_receipt = json.loads(SIGNATURE_RECEIPT.read_text())
    out = {
        "schema": "arr-k8a-deterministic-selector-cut-audit-v1",
        "schema_version": "1.0",
        "source_signature_payload_sha256": source_receipt["payload_sha256"],
        "old_events_per_copy": n,
        "old_atoms": len(atoms),
        "selector_point_count": len(selected_rows),
        "selector_compact_representation": "three products of singleton one-copy MDD roots",
        "selector_points": selected_rows,
        "left_projection_root_sha256": rhash(left_projection),
        "right_projection_root_sha256": rhash(right_projection),
        "kernel_audits": audits,
        "distinguished_cut": {
            "right_old_lower_indices": [a_index, b_index],
            "right_old_upper_count": len(right_old_uppers),
            "every_right_old_upper_contains_R": right_old_uppers_contain_r,
            "right_old_uppers_not_containing_R_count": len(right_old_uppers_missing_r),
            "right_old_uppers_not_containing_R_indices": right_old_uppers_missing_r,
            "first_UP_S_failure_witness": (
                None if not right_old_uppers_missing_r else {
                    "old_upper_index": right_old_uppers_missing_r[0],
                    "old_upper_root_sha256": rhash(roots[events[right_old_uppers_missing_r[0]]]),
                    "contains_both_old_lowers": True,
                    "does_not_contain_R": True,
                }
            ),
            "shared_states_touched_by_a_or_b": touched.bit_count(),
            "all_shared_states_touched": touched == all_shared,
            "left_old_cross_upper_count": len(left_old_cross_uppers),
            "left_old_cross_uppers_below_R_count": len(left_old_cross_uppers_below_r),
            "left_old_cross_uppers_below_R_indices": left_old_cross_uppers_below_r,
            "new_target_upper_checks": new_upper_checks,
            "UP_S_holds_in_bounded_adjoined_family": up_s,
            "R_remains_distinguished_join_in_bounded_adjoined_family": up_s,
            "R_and_old_join_18322_incomparable": (
                not subset(roots[events[18322]], r_univ_right) and
                not subset(r_exist_right, roots[events[18322]])
            ),
            "no_bounded_interpolant_below_R_and_old_join_18322": (
                no_bounded_interpolant_between_cut_and_r_oldjoin
            ),
            "bounded_family_cut_has_no_least_upper": (
                no_bounded_interpolant_between_cut_and_r_oldjoin
            ),
        },
        "first_decisive_old_cut_obstruction": decisive,
        "strategic_verdict": (
            "The deterministic three-singleton selector is physically definable, "
            "but its complement immediately re-bases both full old copies: each "
            "S^c universal shadow has many incomparable maximal old lowers. "
            "Moreover the full right old copy already contains an upper of the "
            "15250/16786 cut which does not contain R, so the restricted-quotient "
            "Neg-023 join does not survive full-old adjunction. Broad selector "
            "closure is therefore not mathematically justified."
        ),
        "evidence_class": "Executable verified — exhaustive finite scope for the displayed bounded family",
        "scope": (
            "Exact compact-MDD audit of S,S^c,R,R^c against every event and all "
            "91 atoms of each 18,676-event old copy, plus the distinguished a,b "
            "upper cut in the bounded family consisting of both old copies and "
            "these four targets. No complement/disjoint-union closure beyond the "
            "displayed targets, no all mixed-pair lattice census, and no OML, "
            "centre, state, sigma, ODBC, or Phi conclusion."
        ),
        "verification_independence": "One deterministic implementation reusing the authoritative ARR MDD producer.",
        "hostile_self_review": [
            "The three singleton products are compact relation terms, not one old-copy MDD; only their exact one-copy projections and universal shadows are MDD tuples.",
            "Greatest-old-lower coverage certifies preservation against one displayed outsider at a time, not closure under unions of multiple outsiders.",
            "UP-S is asserted only in the bounded adjoined family. Later generated mixed events can introduce a smaller upper.",
            "The left-old upper reduction uses the audited all-shared-state coverage of a or b; without it cross-copy uppers would require a separate scan.",
        ],
        "next_gate": (
            "If no decisive old-cut obstruction appears, generate only first-round "
            "disjoint unions involving S or S^c and stop at the first new target "
            "whose old atom fold escapes; otherwise extract the displayed cut."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": "PYTHONHASHSEED=0 python3 notes/open_questions/verification/arr_k8a_deterministic_selector_cut_audit.py --verify",
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
        assert json.loads(RECEIPT.read_text()) == out
    print(json.dumps({"status": "PASS", "payload_sha256": out["payload_sha256"],
                      "UP_S": out["distinguished_cut"]["UP_S_holds_in_bounded_adjoined_family"],
                      "decisive": out["first_decisive_old_cut_obstruction"]}, sort_keys=True))


if __name__ == "__main__":
    main()
