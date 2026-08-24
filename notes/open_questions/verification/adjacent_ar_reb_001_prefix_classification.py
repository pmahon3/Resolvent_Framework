#!/usr/bin/env python3
"""Provenance classification of the fixed AR-REB-001 256-event prefix.

The AR-REB producer is instrumented without changing CAP or closure depth.
Every first-round new root receives deterministic first-generation provenance.
We classify the frozen prefix and test whether the proposed coarse descriptor
determines complement and already-present new/new disjoint-union behavior.
Exact root hashes are retained as identities but excluded from the grouping
key, avoiding vacuous singleton classification.
"""
import argparse, collections, hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_ar_reb_001.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_ar_reb_001.json")
SCHEMA = "adjacent-ar-reb-001-prefix-classification-v1"


def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "first_new_records = []"
    assert src.count(needle) == 1
    src = src.replace(
        needle,
        needle
        + "\n    generation_provenance = {}"
        + "\n    for _name,_root in ((\"target\",target),(\"target_complement\",neg(target)),(\"forced_g\",forced),(\"forced_g_complement\",forced_comp)):"
        + "\n        if _root not in roots.values(): generation_provenance.setdefault(_root,{\"operator\":_name,\"depth\":1,\"parents\":[]})",
    )
    needle2 = "additions.add(w)"
    assert src.count(needle2) == 1
    src = src.replace(
        needle2,
        needle2
        + "\n                        generation_provenance.setdefault(w,{\"operator\":\"disjoint_union\" if w==z else \"complement_of_disjoint_union\",\"depth\":1+max(generation_provenance.get(x,{\"depth\":0})[\"depth\"],generation_provenance.get(y,{\"depth\":0})[\"depth\"]),\"parents\":[rhash(x),rhash(y)]})",
    )
    needle3 = "source_receipt = json.load(open(SOURCE_RECEIPT))"
    assert src.count(needle3) == 1
    src = src.replace(
        needle3,
        "globals()['_PREFIX_INTERNAL']={'family':family,'provenance':generation_provenance,'target':target,'forced':forced,'bank':bank,'eligible_atoms':eligible_atoms,'first_escape':first_escape}\n    "
        + needle3,
    )
    ns = {"__file__": SOURCE, "__name__": "_prefix_classifier_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    ns["payload"]()
    data = ns["_PREFIX_INTERNAL"]
    family = data["family"]
    provenance = data["provenance"]
    target = data["target"]
    forced = data["forced"]
    bank = data["bank"]
    events = bank["all_events"]
    macros = bank["macros"]
    engines = bank["engines"]
    states = bank["states"]
    roots = {ev: root for root, ev in bank["root_to_event"].items()}
    old_roots = set(roots.values())
    root_index = {roots[e]: i for i, e in enumerate(events)}
    principal = bank["principal"]
    upmap = {u: i for i, u in enumerate(principal)}
    n = len(events)
    assert len(family) - n == 256

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
        import struct

        return hashlib.sha256(
            b"".join(struct.pack("<I", a) for a in x)
        ).hexdigest()

    allold = (1 << n) - 1
    zero = upmap[allold]

    def old_join(x, y):
        return upmap[principal[x] & principal[y]]

    comp_index = {i: root_index[neg(roots[e])] for i, e in enumerate(events)}

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

    def kernel_type(x):
        fold = zero
        for a in atoms:
            if subset(roots[events[a]], x):
                fold = old_join(fold, a)
        lower_good = subset(roots[events[fold]], x)
        cfold = zero
        nx = neg(x)
        for a in atoms:
            if subset(roots[events[a]], nx):
                cfold = old_join(cfold, a)
        upper_good = subset(roots[events[cfold]], nx)
        return (
            fold if lower_good else None,
            comp_index[cfold] if upper_good else None,
        )

    envelope = roots[events[18331]]
    prior = roots[events[15250]]
    adjoined = roots[events[10752]]
    escaping_old_join = roots[events[18322]]
    new_roots = sorted(family - old_roots, key=rhash)
    family_by_hash = {rhash(x): x for x in family}
    records = []
    coarse_by_root = {}
    for x in new_roots:
        p = provenance[x]
        lower, upper = kernel_type(x)
        descriptor = {
            "operator": p["operator"],
            "depth": p["depth"],
            "parent_depths": sorted(
                provenance.get(family_by_hash[h], {"depth": 0})["depth"]
                for h in p["parents"]
            ),
            "target_relation": (
                "equal" if x == target else "below" if subset(x, target) else "above" if subset(target, x) else "cross"
            ),
            "g_relation": (
                "equal" if x == forced else "below" if subset(x, forced) else "above" if subset(forced, x) else "cross"
            ),
            "envelope_relation": (
                "equal" if x == envelope else "below" if subset(x, envelope) else "above" if subset(envelope, x) else "cross"
            ),
            "physical_side_mapping": (
                "target_side"
                if subset(x, target)
                else "target_complement_side"
                if subset(x, neg(target))
                else "mixed"
            ),
            "old_lower_index": lower,
            "old_upper_index": upper,
            "contains_changed_prior": subset(prior, x),
            "contains_changed_atom": subset(adjoined, x),
            "contains_forced_g": subset(forced, x),
            "below_escaping_old_join": subset(x, escaping_old_join),
        }
        key = digest(descriptor)
        coarse_by_root[x] = key
        records.append(
            {
                "root_sha256": rhash(x),
                "exact_section_root_signature_sha256": rhash(x),
                "provenance": p,
                "descriptor": descriptor,
                "descriptor_sha256": key,
            }
        )

    # Behaviour is restricted to operations whose outcomes are already in the
    # frozen prefix.  No new root is adjoined here.
    behavior = {}
    for x in new_roots:
        comp = neg(x)
        rows = []
        for y in new_roots:
            if op(0, x, y) != zero_root:
                continue
            z = op(1, x, y)
            if z in family:
                rows.append((coarse_by_root[y], coarse_by_root.get(z, "OLD")))
        behavior[x] = {
            "complement_outcome": coarse_by_root.get(comp, "OLD"),
            "new_new_disjoint_union_signature_sha256": digest(sorted(rows)),
            "new_new_disjoint_union_count": len(rows),
        }
    groups = collections.defaultdict(list)
    record_by_hash = {r["root_sha256"]: r for r in records}
    for x in new_roots:
        groups[coarse_by_root[x]].append(x)
    divergent = []
    for key, xs in sorted(groups.items()):
        sigs = collections.defaultdict(list)
        for x in xs:
            sigs[digest(behavior[x])].append(rhash(x))
        if len(sigs) > 1:
            divergent.append(
                {
                    "descriptor_sha256": key,
                    "class_size": len(xs),
                    "distinct_behavior_count": len(sigs),
                    "behavior_examples": [
                        {
                            "behavior_sha256": h,
                            "root_sha256": rs[0],
                            "exact_record": record_by_hash[rs[0]],
                        }
                        for h, rs in sorted(sigs.items())
                    ],
                }
            )
    source_receipt = json.load(open(SOURCE_RECEIPT))
    out = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "source_ar_reb_payload_sha256": source_receipt["payload_sha256"],
        "fixed_new_event_count": len(new_roots),
        "closure_cap_unchanged": 256,
        "closure_depth_not_extended": True,
        "descriptor_class_count": len(groups),
        "descriptor_class_size_histogram": dict(
            sorted(collections.Counter(map(len, groups.values())).items())
        ),
        "descriptor_inadequate_class_count": len(divergent),
        "first_descriptor_divergences": divergent[:24],
        "records_chained_sha256": hashlib.sha256(
            "\n".join(digest(r) for r in records).encode()
        ).hexdigest(),
        "verdict": (
            "candidate provenance descriptor is adequate on frozen prefix"
            if not divergent
            else "candidate provenance descriptor is not behaviorally adequate on frozen prefix"
        ),
        "first_sufficient_refinement_candidate": (
            None
            if not divergent
            else (
                "some refinement beyond the parent-depth multiset is required; "
                "exact parent-root/provenance incidence is the first sufficient "
                "candidate exposed by these witnesses, not proved minimal"
            )
        ),
        "scope": (
            "Exact classification of the already generated AR-REB-001 256-event "
            "prefix. Behaviour tests use only complement and new/new disjoint "
            "unions already present. No cap/depth extension, old/new full table, "
            "lattice, OML, centre, state, sigma, ODBC, or Phi claim."
        ),
        "evidence_class": "Executable verified — sampled finite scope",
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "adjacent_ar_reb_001_prefix_classification.py --verify"
        ),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = digest(out)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = payload()
    path = os.path.join(HERE, "adjacent_ar_reb_001_prefix_classification.json")
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
                "classes": out["descriptor_class_count"],
                "inadequate": out["descriptor_inadequate_class_count"],
            },
            sort_keys=True,
        )
    )
