#!/usr/bin/env python3
"""Reachable kernel-observational congruence pilot.

Instrument the fixed six-generator actual-event audit.  For every reachable
semantic signature, observe both actual universal shadows by:

* greatest old lower index, or ``None`` when the old atom fold escapes;
* complement-dual least old upper index, or ``None``.

For each typed Neg/And/OrthoOr occurrence, group by the observation(s) of its
parents.  Two different child observations in one group refute compatibility
of this observation descriptor.  This is the reachable depth-one family only;
the full 512-element Boolean algebra is not enumerated.
"""
import argparse, hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_full_cycle_actual_event_shadow.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_full_cycle_actual_event_shadow.json")
SCHEMA = "adjacent-kernel-observational-congruence-v1"


def canon(x):
    if isinstance(x, tuple):
        return [canon(y) for y in x]
    if isinstance(x, list):
        return [canon(y) for y in x]
    if isinstance(x, dict):
        return {k: canon(v) for k, v in x.items()}
    return x


def digest(x):
    return hashlib.sha256(
        json.dumps(canon(x), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "def mddneg(x):return tuple(engines[m].neg(a) for m,a in enumerate(x))"
    assert src.count(needle) == 1
    src = src.replace(
        needle,
        needle
        + "\n root_index={roots[e]:i for i,e in enumerate(events)}"
        + "\n comp={i:root_index[mddneg(roots[e])] for i,e in enumerate(events)}",
    )
    global_needle = "records=[];global_first=None"
    assert src.count(global_needle) == 1
    src = src.replace(
        global_needle, global_needle + ";kernel_observation_rows=[]"
    )
    needle2 = "mismatches=[];actual_bad=coord_bad=0;mismatch_kinds=collections.Counter()"
    assert src.count(needle2) == 1
    src = src.replace(
        needle2,
        needle2
        + ";observation_by_signature={};occurrence_id_by_signature={};occurrence_counter=0",
    )
    needle3 = "actual=compose_all(retained,pos,tables)"
    assert src.count(needle3) == 1
    inject = """actual=compose_all(retained,pos,tables)
   actual_right=compose_all(opposite,oppos,RT)
   def side_observation(target):
    lk,lg,lec,led=kernel(target)
    ck,cg,cec,ced=kernel(mddneg(target))
    return {'greatest_old_lower_index':lk if lg else None,
     'greatest_old_lower_exists':lg,'least_old_upper_index':comp[ck] if cg else None,
     'least_old_upper_exists':cg}
   obs={'left_shadow':side_observation(actual),
    'right_shadow':side_observation(actual_right)}
   parent_sigs=tuple(t.get('parents') or ())
   parent_obs=tuple(observation_by_signature[p] for p in parent_sigs)
   parent_ids=tuple(occurrence_id_by_signature[p] for p in parent_sigs)
   oid=name+'-'+t['kind']+'-'+str(occurrence_counter).zfill(3);occurrence_counter+=1
   if sig in observation_by_signature:assert observation_by_signature[sig]==obs
   kernel_observation_rows.append({'occurrence_id':oid,'kind':t['kind'],
    'semantic_signature_sha256':sh,'parent_signature_sha256':ph,
    'parent_occurrence_ids':parent_ids,'parent_observations':parent_obs,
    'left_universal_shadow_root_sha256':rhash(actual),
    'right_universal_shadow_root_sha256':rhash(actual_right),
    'exact_disjoint_parents':True if t['kind']=='OrthoOr' else None,
    'child_observation':obs})
   observation_by_signature.setdefault(sig,obs)
   occurrence_id_by_signature.setdefault(sig,oid)"""
    src = src.replace(needle3, inject)
    needle4 = "'old_atom_count':len(atoms),'orientation_records':records,'first_discriminator':global_first,"
    assert src.count(needle4) == 1
    src = src.replace(
        needle4,
        "'kernel_observation_internal':kernel_observation_rows,"
        + needle4,
    )
    ns = {"__file__": SOURCE, "__name__": "_kernel_observation_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    base, _ = ns["payload"]()
    rows = base.pop("kernel_observation_internal")
    source_receipt = json.load(open(SOURCE_RECEIPT))

    first = None
    offset = 0
    orientation_results = []
    for rec in base["orientation_records"]:
        count = rec["terms_tested"]
        subset = rows[offset : offset + count]
        offset += count
        nonexistence_counts = {}
        first_nonexistence = {}
        for kind in ("Leaf", "Neg", "And", "OrthoOr"):
            for side in ("left_shadow", "right_shadow"):
                for bound in ("greatest_old_lower", "least_old_upper"):
                    key = f"{kind}:{side}:{bound}"
                    failures = [
                        row
                        for row in subset
                        if row["kind"] == kind
                        and not row["child_observation"][side][
                            bound + "_exists"
                        ]
                    ]
                    nonexistence_counts[key] = len(failures)
                    if failures:
                        row = failures[0]
                        first_nonexistence[key] = {
                            "occurrence_id": row["occurrence_id"],
                            "semantic_signature_sha256": row[
                                "semantic_signature_sha256"
                            ],
                            "parent_occurrence_ids": row[
                                "parent_occurrence_ids"
                            ],
                            "parent_signature_sha256": row[
                                "parent_signature_sha256"
                            ],
                            "universal_shadow_root_sha256": row[
                                "left_universal_shadow_root_sha256"
                                if side == "left_shadow"
                                else "right_universal_shadow_root_sha256"
                            ],
                            "child_observation": row["child_observation"][
                                side
                            ],
                        }
        local = {}
        for row in subset:
            if row["kind"] == "Leaf":
                continue
            key = digest(
                {
                    "kind": row["kind"],
                    "parents": row["parent_observations"],
                }
            )
            local.setdefault(
                key,
                {
                    "kind": row["kind"],
                    "parent_observations": row["parent_observations"],
                    "children": {},
                },
            )
            ch = digest(row["child_observation"])
            local[key]["children"].setdefault(
                ch,
                {
                    "child_observation": row["child_observation"],
                    "semantic_signature_sha256": row[
                        "semantic_signature_sha256"
                    ],
                    "parent_signature_sha256": row[
                        "parent_signature_sha256"
                    ],
                    "parent_occurrence_ids": row["parent_occurrence_ids"],
                    "occurrence_id": row["occurrence_id"],
                    "left_universal_shadow_root_sha256": row[
                        "left_universal_shadow_root_sha256"
                    ],
                    "right_universal_shadow_root_sha256": row[
                        "right_universal_shadow_root_sha256"
                    ],
                    "exact_disjoint_parents": row[
                        "exact_disjoint_parents"
                    ],
                },
            )
        bad = []
        for key, group in sorted(local.items()):
            if len(group["children"]) > 1:
                examples = list(group["children"].values())
                first_difference = None
                for side in ("left_shadow", "right_shadow"):
                    for component in (
                        "greatest_old_lower_exists",
                        "greatest_old_lower_index",
                        "least_old_upper_exists",
                        "least_old_upper_index",
                    ):
                        a = examples[0]["child_observation"][side][component]
                        b = examples[1]["child_observation"][side][component]
                        if a != b:
                            first_difference = {
                                "side": side,
                                "component": component,
                                "first_value": a,
                                "second_value": b,
                            }
                            break
                    if first_difference:
                        break
                witness = {
                    "typed_parent_observation_sha256": key,
                    "kind": group["kind"],
                    "parent_observations": group["parent_observations"],
                    "distinct_child_observation_count": len(group["children"]),
                    "first_differing_component": first_difference,
                    "child_examples": examples,
                }
                bad.append(witness)
                if first is None:
                    first = {"orientation": rec["orientation"], **witness}
        endpoint_failures = []
        endpoint_failure_count_by_side_kind = {}
        for row in subset:
            for side in ("left_shadow", "right_shadow"):
                for endpoint, field in (
                    ("lower", "greatest_old_lower_exists"),
                    ("upper", "least_old_upper_exists"),
                ):
                    if row["child_observation"][side][field]:
                        continue
                    key = f"{side}:{endpoint}:{row['kind']}"
                    endpoint_failure_count_by_side_kind[key] = (
                        endpoint_failure_count_by_side_kind.get(key, 0) + 1
                    )
                    endpoint_failures.append(
                        {
                            "occurrence_id": row["occurrence_id"],
                            "kind": row["kind"],
                            "side": side,
                            "endpoint": endpoint,
                            "semantic_signature_sha256": row[
                                "semantic_signature_sha256"
                            ],
                            "parent_occurrence_ids": row[
                                "parent_occurrence_ids"
                            ],
                            "parent_signature_sha256": row[
                                "parent_signature_sha256"
                            ],
                            "left_universal_shadow_root_sha256": row[
                                "left_universal_shadow_root_sha256"
                            ],
                            "right_universal_shadow_root_sha256": row[
                                "right_universal_shadow_root_sha256"
                            ],
                            "child_observation": row[
                                "child_observation"
                            ],
                        }
                    )
        orientation_results.append(
            {
                "orientation": rec["orientation"],
                "shadow_role_mapping": (
                    {
                        "left_shadow": "retained_physical_left",
                        "right_shadow": "opposite_physical_right",
                    }
                    if rec["orientation"] == "left_retained_position11"
                    else {
                        "left_shadow": "retained_physical_right",
                        "right_shadow": "opposite_physical_left",
                    }
                ),
                "reachable_occurrence_count": len(subset),
                "bound_nonexistence_counts": nonexistence_counts,
                "first_bound_nonexistence": first_nonexistence,
                "typed_parent_observation_group_count": len(local),
                "incompatible_group_count": len(bad),
                "incompatible_group_count_by_kind": {
                    kind: sum(x["kind"] == kind for x in bad)
                    for kind in ("Neg", "And", "OrthoOr")
                },
                "incompatible_groups": bad,
                "endpoint_failure_count": len(endpoint_failures),
                "endpoint_failure_count_by_side_kind": (
                    endpoint_failure_count_by_side_kind
                ),
                "first_endpoint_failure": (
                    endpoint_failures[0] if endpoint_failures else None
                ),
                "first_lower_endpoint_failure": next(
                    (
                        failure
                        for failure in endpoint_failures
                        if failure["endpoint"] == "lower"
                    ),
                    None,
                ),
                "first_upper_endpoint_failure": next(
                    (
                        failure
                        for failure in endpoint_failures
                        if failure["endpoint"] == "upper"
                    ),
                    None,
                ),
                "endpoint_failures": endpoint_failures,
                "group_transition_sha256": digest(
                    [
                        (
                            key,
                            sorted(group["children"]),
                        )
                        for key, group in sorted(local.items())
                    ]
                ),
            }
        )
    assert offset == len(rows)
    out = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "source_actual_event_payload_sha256": source_receipt["payload_sha256"],
        "orientation_records": orientation_results,
        "first_incompatibility": first,
        "compatible_on_reachable_occurrences": first is None,
        "verdict": (
            "reachable observation is compatible"
            if first is None
            else "kernel/dual-upper observation is not a typed Boolean congruence"
        ),
        "neg_sanity_interpretation": (
            "A Neg conflict here does not contradict complement-stability of "
            "the abstract K=(lower,upper) section type: the observed objects "
            "are universal shadows of full relations, and the universal "
            "shadow of a complement is not generally the complement of the "
            "universal shadow."
        ),
        "scope": (
            "The canonical fixed six-generator reachable Leaf/And/Neg/"
            "OrthoOr occurrences from the actual-event audit only. No full "
            "512-element transition enumeration, other witnesses, arbitrary "
            "depth, closure, OML, sigma, ODBC, or Phi claim."
        ),
        "verification_independence": (
            "Single deterministic instrumentation sharing the actual-event "
            "producer's exact MDD grammar and leaf selection."
        ),
        "evidence_class": "Executable verified — sampled finite scope",
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "adjacent_kernel_observational_congruence.py --verify"
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
    path = os.path.join(HERE, "adjacent_kernel_observational_congruence.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(canon(out), f, sort_keys=True, indent=2)
            f.write("\n")
    else:
        assert json.load(open(path)) == canon(out)
    print(
        json.dumps(
            {
                "status": "PASS",
                "payload_sha256": out["payload_sha256"],
                "verdict": out["verdict"],
            },
            sort_keys=True,
        )
    )
