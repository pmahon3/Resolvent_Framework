#!/usr/bin/env python3
"""Exact forced interval top for the full-old Neg-023 cut.

Let R be actual Neg-023 and E the right old event 18322, the old join of
15250 and 16786.  This producer audits the literal relation

    T = R intersection cyl_right(E).

Any repair join of the two lowers that lies below both incomparable uppers R
and cyl_right(E) must lie below T.  No closure rounds are performed.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_k8a_deterministic_selector_cut_audit.py"
SOURCE_RECEIPT = HERE / "arr_k8a_deterministic_selector_cut_audit.json"
RECEIPT = HERE / "arr_forced_interval_top_audit.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def recover():
    source = SOURCE.read_text()
    needle = "    source_receipt = json.loads(SIGNATURE_RECEIPT.read_text())"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_FORCED_TOP']={'bank':bank,'arr':arr,'events':events,"
        "'macros':macros,'engines':engines,'states':states,'roots':roots,"
        "'principal':principal,'atoms':atoms,'zero':zero,'old_join':old_join,"
        "'op':op,'neg':neg,'subset':subset,'rhash':rhash,"
        "'compose_all':compose_all,'r_univ_left':r_univ_left,"
        "'rc_univ_left':rc_univ_left,'r_univ_right':r_univ_right,"
        "'rc_univ_right':rc_univ_right}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_forced_top"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_FORCED_TOP"]


def payload():
    d = recover()
    arr, events, macros = d["arr"], d["events"], d["macros"]
    engines, states, roots = d["engines"], d["states"], d["roots"]
    principal, atoms, zero = d["principal"], d["atoms"], d["zero"]
    old_join, op, neg, subset, rhash = (d["old_join"], d["op"], d["neg"],
                                       d["subset"], d["rhash"])
    compose_all = d["compose_all"]
    n = len(events)
    assert n == 18676 and len(atoms) == 91
    E_INDEX = 18322
    A_INDEX, B_INDEX = 15250, 16786
    eroot = roots[events[E_INDEX]]

    # Extend the exact opposite six-bit pattern atlas by E's membership bit.
    occ = arr["occ"]
    cache = {}
    def patterns(macro, rs, position, index):
        key = (macro, rs, position, index)
        if key in cache:
            return cache[key]
        if all(root <= 1 for root in rs):
            answer = frozenset((sum((root & 1) << k
                                    for k, root in enumerate(rs)),))
        else:
            variables = [engines[macro].nodes[root][0]
                         for root in rs if root > 1]
            variable = min(variables)
            if variable == position:
                nxt = tuple(
                    engines[macro].nodes[root][1][index]
                    if root > 1 and engines[macro].nodes[root][0] == variable
                    else root for root in rs
                )
                answer = patterns(macro, nxt, position, index)
            else:
                values = set()
                for choice in range(len(macros[macro][1][variable])):
                    nxt = tuple(
                        engines[macro].nodes[root][1][choice]
                        if root > 1 and engines[macro].nodes[root][0] == variable
                        else root for root in rs
                    )
                    values.update(patterns(macro, nxt, position, index))
                answer = frozenset(values)
        cache[key] = answer
        return answer

    opposite7 = tuple(arr["opposite"]) + (E_INDEX,)
    bp7 = [set() for _ in states]
    for shared in range(len(states)):
        for macro, index in occ[arr["oppos"]][shared]:
            rs = tuple(roots[events[event]][macro] for event in opposite7)
            bp7[shared].update(patterns(macro, rs, arr["oppos"], index))
        assert bp7[shared]

    # Left shadows: for each retained six-bit pattern a, quantify over the
    # exact seven-bit opposite patterns (b,e).  T(a,b,e)=F(a,b)&e.
    t_univ_left_tables = []
    t_exist_left_tables = []
    for shared in range(len(states)):
        universal = existential = 0
        for a in range(64):
            values = [((arr["F"] >> (a | ((word & 63) << 6))) & 1)
                      and ((word >> 6) & 1) for word in bp7[shared]]
            if all(values):
                universal |= 1 << a
            if any(values):
                existential |= 1 << a
        t_univ_left_tables.append(universal)
        t_exist_left_tables.append(existential)
    t_univ_left = compose_all(arr["retained"], arr["pos"], t_univ_left_tables)
    t_exist_left = compose_all(arr["retained"], arr["pos"], t_exist_left_tables)

    # Right shadows factor because E is right-cylindrical.
    t_univ_right = op(0, d["r_univ_right"], eroot)
    r_exist_right = neg(d["rc_univ_right"])
    t_exist_right = op(0, r_exist_right, eroot)

    def kernel(target):
        lowers = [i for i, event in enumerate(events)
                  if subset(roots[event], target)]
        maximal = [i for i in lowers if not any(
            i != j and (principal[i] >> j) & 1 for j in lowers
        )]
        eligible = [atom for atom in atoms
                    if subset(roots[events[atom]], target)]
        fold = zero
        escape = None
        for atom in eligible:
            prior = fold
            fold = old_join(fold, atom)
            if escape is None and not subset(roots[events[fold]], target):
                escape = {"prior_index": prior, "atom_index": atom,
                          "escaping_join_index": fold}
        return {
            "universal_shadow_root_sha256": rhash(target),
            "old_lower_count": len(lowers),
            "maximal_old_lower_indices": maximal,
            "greatest_old_lower_exists": len(maximal) == 1,
            "eligible_old_atom_count": len(eligible),
            "atom_fold_index": fold,
            "atom_fold_inside_shadow": subset(roots[events[fold]], target),
            "first_atom_fold_escape": escape,
        }

    contains_a = subset(roots[events[A_INDEX]], t_univ_right)
    contains_b = subset(roots[events[B_INDEX]], t_univ_right)
    # Seed equality tests.  Cylindricity is exactly existential=universal.
    right_cyl = t_exist_right == t_univ_right
    left_cyl = t_exist_left == t_univ_left
    right_old_index = next((i for i, event in enumerate(events)
                            if roots[event] == t_univ_right), None) if right_cyl else None
    left_old_index = next((i for i, event in enumerate(events)
                           if roots[event] == t_univ_left), None) if left_cyl else None
    r_subset_e = subset(r_exist_right, eroot)
    t_equals_r = r_subset_e

    source = json.loads(SOURCE_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-interval-top-audit-v1",
        "schema_version": "1.0",
        "source_selector_cut_payload_sha256": source["payload_sha256"],
        "definition": "T = R intersection cyl_right(old event 18322)",
        "right_old_event_index": E_INDEX,
        "distinguished_lower_indices": [A_INDEX, B_INDEX],
        "lower_15250_subset_T": contains_a,
        "lower_16786_subset_T": contains_b,
        "T_is_upper_of_distinguished_cut": contains_a and contains_b,
        "forced_interval_theorem": (
            "For every concrete relation h, if both distinguished lowers are "
            "subsets of h and h is a subset of R and of cyl_right(18322), then "
            "h is a subset of T. This is set intersection and needs no closure "
            "or lattice assumption."
        ),
        "left_old_lower_kernel": kernel(t_univ_left),
        "right_old_lower_kernel": kernel(t_univ_right),
        "left_existential_shadow_root_sha256": rhash(t_exist_left),
        "left_universal_shadow_root_sha256": rhash(t_univ_left),
        "right_existential_shadow_root_sha256": rhash(t_exist_right),
        "right_universal_shadow_root_sha256": rhash(t_univ_right),
        "left_cylindrical": left_cyl,
        "right_cylindrical": right_cyl,
        "left_old_seed_index_if_cylindrical": left_old_index,
        "right_old_seed_index_if_cylindrical": right_old_index,
        "T_equals_R": t_equals_r,
        "T_equals_right_old_18322": right_cyl and right_old_index == E_INDEX,
        "equal_to_any_current_single_seed": bool(t_equals_r or left_old_index is not None
                                                  or right_old_index is not None),
        "generated_by_complement_disjoint_union_closure_of_current_seeds": "Open — no closure rounds were run.",
        "evidence_class": "Executable verified — exhaustive finite scope",
        "scope": (
            "Exact MDD quantifier shadows and exhaustive old-lower kernel folds "
            "for the single set target T. It proves the displayed forced-interval "
            "property and seed/cylindricity tests only. No closure, lattice, OML, "
            "centre, state, sigma, ODBC, or Phi claim."
        ),
        "verification_independence": "One deterministic implementation reusing the authoritative ARR and selector-cut MDD producer.",
        "hostile_self_review": [
            "T is a set target, not yet a generated event.",
            "A greatest old lower kernel does not force T into an ambient OML.",
            "Noncylindricity excludes equality with an old cylinder seed but not generation by later mixed closure.",
            "The left seven-bit pattern extension shares the source MDD engine and was not independently reimplemented.",
        ],
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": "PYTHONHASHSEED=0 python3 notes/open_questions/verification/arr_forced_interval_top_audit.py --verify",
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
                      "T_upper": out["T_is_upper_of_distinguished_cut"],
                      "left_cyl": out["left_cylindrical"],
                      "right_cyl": out["right_cylindrical"]}, sort_keys=True))


if __name__ == "__main__":
    main()
