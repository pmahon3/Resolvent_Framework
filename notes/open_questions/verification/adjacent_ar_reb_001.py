#!/usr/bin/env python3
"""AR-REB-001: capped re-basing pilot for actual occurrence Neg-023.

Materialize the opposite/right universal-shadow target as an exact MDD tuple
on the 18,676-event full-cycle carrier.  Compute its complete old lower/upper
sets, the physical union of all contained old atoms as an explicitly adjoined
candidate lower envelope, the first old join that this candidate upper bound
invalidates, and a capped incremental complement/disjoint-union closure.

The candidate lower envelope is seeded explicitly.  This pilot does not claim
that it is generated without that seed, or that an arbitrary ambient lattice
must contain the literal union rather than an order-theoretic join which
strictly overshoots it.

No adjacent-carrier point bitsets are constructed.  A capped closure is not a
completed lattice or OML.
"""
import argparse, hashlib, json, os, struct

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_full_cycle_actual_event_shadow.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_full_cycle_actual_event_shadow.json")
KERNEL_RECEIPT = os.path.join(HERE, "adjacent_kernel_observational_congruence.json")
SCHEMA = "adjacent-ar-reb-001-v1"
CAP = 256


def jhash(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']"
    assert src.count(needle) == 1
    src = src.replace(needle, needle + ";globals()['_REB_BANK']=b")
    needle2 = "mismatches=[];actual_bad=coord_bad=0;mismatch_kinds=collections.Counter()"
    assert src.count(needle2) == 1
    src = src.replace(needle2, needle2 + ";reb_occurrence_counter=0")
    needle3 = "actual=compose_all(retained,pos,tables)"
    assert src.count(needle3) == 1
    inject = """actual=compose_all(retained,pos,tables)
   actual_right_reb=compose_all(opposite,oppos,RT)
   if name=='left_retained_position11' and t['kind']=='Neg' and reb_occurrence_counter==23:
    globals()['_REB_TARGET']=actual_right_reb
    globals()['_REB_SIGNATURE']=sh
   reb_occurrence_counter+=1"""
    src = src.replace(needle3, inject)
    ns = {"__file__": SOURCE, "__name__": "_ar_reb_001_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    ns["payload"]()
    target = ns["_REB_TARGET"]
    signature = ns["_REB_SIGNATURE"]
    bank = ns["_REB_BANK"]
    events = bank["all_events"]
    macros = bank["macros"]
    engines = bank["engines"]
    roots = {ev: root for root, ev in bank["root_to_event"].items()}
    principal = bank["principal"]
    root_index = {roots[e]: i for i, e in enumerate(events)}
    upmap = {u: i for i, u in enumerate(principal)}
    n = len(events)
    assert n == 18676

    def op(kind, x, y):
        return tuple(
            engines[m].app(kind, a, b)
            for m, (a, b) in enumerate(zip(x, y))
        )

    def neg(x):
        return tuple(engines[m].neg(a) for m, a in enumerate(x))

    zero_root = tuple(0 for _ in macros)

    def subset(x, y):
        return op(0, x, neg(y)) == zero_root

    def rhash(x):
        return hashlib.sha256(
            b"".join(struct.pack("<I", a) for a in x)
        ).hexdigest()

    comp = {i: root_index[neg(roots[e])] for i, e in enumerate(events)}
    allold = (1 << n) - 1
    zero = upmap[allold]

    def old_join(x, y):
        return upmap[principal[x] & principal[y]]

    def old_record(i):
        return {
            "index": i,
            "physical_root_sha256": rhash(roots[events[i]]),
            "full17_hex": hex(events[i][1]),
        }

    nonatomic = 0
    for d, upper in enumerate(principal):
        if d != zero:
            nonatomic |= upper & ~(1 << d)
    bits = allold & ~nonatomic & ~(1 << zero)
    atoms = []
    while bits:
        q = bits & -bits
        atoms.append(q.bit_length() - 1)
        bits -= q
    assert len(atoms) == 91

    lowers = [i for i, e in enumerate(events) if subset(roots[e], target)]
    uppers = [i for i, e in enumerate(events) if subset(target, roots[e])]
    maximal_lowers = [
        i
        for i in lowers
        if not any(i != j and (principal[i] >> j) & 1 for j in lowers)
    ]
    minimal_uppers = [
        i
        for i in uppers
        if not any(i != j and (principal[j] >> i) & 1 for j in uppers)
    ]
    eligible_atoms = [a for a in atoms if subset(roots[events[a]], target)]
    forced = zero_root
    for a in eligible_atoms:
        forced = op(1, forced, roots[events[a]])
    forced_comp = neg(forced)
    forced_dominates_all_old_lowers = all(
        subset(roots[events[i]], forced) for i in lowers
    )

    fold = zero
    first_escape = None
    for a in eligible_atoms:
        prior = fold
        fold = old_join(fold, a)
        if first_escape is None and not subset(roots[events[fold]], target):
            first_escape = {
                "prior": old_record(prior),
                "adjoined_atom": old_record(a),
                "old_join": old_record(fold),
                "new_concrete_union_root_sha256": rhash(
                    op(1, roots[events[prior]], roots[events[a]])
                ),
                "target_is_new_upper_bound": subset(
                    roots[events[prior]], target
                )
                and subset(roots[events[a]], target),
                "old_join_escapes_target": not subset(
                    roots[events[fold]], target
                ),
            }

    # Incremental closure: only pairs with at least one newly adjoined root.
    family = set(roots.values())
    frontier = []
    for x in (target, neg(target), forced, forced_comp):
        if x not in family:
            family.add(x)
            frontier.append(x)
    rounds = []
    first_new_records = []
    capped = False
    while frontier and len(family) - n < CAP:
        snapshot = sorted(family, key=rhash)
        additions = set()
        for x in sorted(frontier, key=rhash):
            for y in snapshot:
                if op(0, x, y) != zero_root:
                    continue
                z = op(1, x, y)
                for w in (z, neg(z)):
                    if w not in family:
                        additions.add(w)
                        if len(first_new_records) < 24:
                            first_new_records.append(
                                {
                                    "left_root_sha256": rhash(x),
                                    "right_root_sha256": rhash(y),
                                    "union_root_sha256": rhash(z),
                                    "adjoined_root_sha256": rhash(w),
                                }
                            )
                if len(family) + len(additions) - n >= CAP:
                    capped = True
                    break
            if capped:
                break
        rounds.append(len(additions))
        family.update(additions)
        frontier = list(additions)
        if capped:
            break

    source_receipt = json.load(open(SOURCE_RECEIPT))
    kernel_receipt = json.load(open(KERNEL_RECEIPT))
    out = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "source_actual_event_payload_sha256": source_receipt["payload_sha256"],
        "source_kernel_observation_payload_sha256": kernel_receipt[
            "payload_sha256"
        ],
        "occurrence_id": "left_retained_position11-Neg-023",
        "semantic_signature_sha256": signature,
        "ambient_old_event_count": n,
        "target_root_sha256": rhash(target),
        "target_is_old_event": target in root_index,
        "old_lower_count": len(lowers),
        "old_maximal_lower_indices": maximal_lowers,
        "old_upper_count": len(uppers),
        "old_minimal_upper_indices": minimal_uppers,
        "greatest_old_lower_exists": len(maximal_lowers) == 1,
        "least_old_upper_exists": len(minimal_uppers) == 1,
        "eligible_old_atom_count": len(eligible_atoms),
        "eligible_old_atom_indices": eligible_atoms,
        "eligible_old_atom_digest_sha256": hashlib.sha256(
            ",".join(map(str, eligible_atoms)).encode()
        ).hexdigest(),
        "old_atom_fold": old_record(fold),
        "old_atom_fold_inside_target": subset(roots[events[fold]], target),
        "seeded_literal_lower_envelope_root_sha256": rhash(forced),
        "seeded_literal_lower_envelope_complement_root_sha256": rhash(
            forced_comp
        ),
        "seeded_literal_lower_envelope_equals_target": forced == target,
        "seeded_literal_lower_envelope_subset_target": subset(forced, target),
        "seeded_literal_lower_envelope_dominates_all_old_lowers": (
            forced_dominates_all_old_lowers
        ),
        "seeded_literal_lower_envelope_is_join_in_seeded_family": (
            forced_dominates_all_old_lowers and subset(forced, target)
        ),
        "target_minus_seeded_literal_lower_envelope_nonempty": forced != target,
        "seed_is_not_claimed_generated_or_ambient_forced": True,
        "first_changed_old_join_certificate": first_escape,
        "closure_cap_new_events": CAP,
        "closure_new_event_count": len(family) - n,
        "closure_round_addition_counts": rounds,
        "closure_hit_cap": capped,
        "first_closure_generation_records": first_new_records,
        "scope": (
            "Exact old-carrier MDD materialization of actual opposite-shadow "
            "Neg-023 and a capped incremental concrete-logic closure. No "
            "claim of terminal closure, latticehood, OML, centre, states, "
            "sigma completion, ODBC, or Phi."
        ),
        "evidence_class": "Executable verified — sampled finite scope",
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "adjacent_ar_reb_001.py --verify"
        ),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = jhash(out)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = payload()
    path = os.path.join(HERE, "adjacent_ar_reb_001.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2)
            f.write("\n")
    else:
        assert json.load(open(path)) == out
    print(
        json.dumps(
            {
                "status": "PASS",
                "payload_sha256": out["payload_sha256"],
                "closure_new": out["closure_new_event_count"],
                "capped": out["closure_hit_cap"],
            },
            sort_keys=True,
        )
    )
