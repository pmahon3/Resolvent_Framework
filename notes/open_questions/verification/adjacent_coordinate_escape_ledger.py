#!/usr/bin/env python3
"""Stable 12-row enrichment of the bounded coordinate escape controls.

This instruments the already-banked second-round producer without changing
its sample.  It does not run the exhaustive first-round census and does not
promote coordinate targets to actual generated events.
"""
import argparse, hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_full_cycle_second_round_coordinate_children.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_full_cycle_second_round_coordinate_children.json")
THIRD_RECEIPT = os.path.join(HERE, "adjacent_full_cycle_third_round_phantom_bridge.json")
SCHEMA = "adjacent-coordinate-escape-ledger-v1"


def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "records=[];first_failure=None;shadow_bridges=collections.defaultdict(dict)"
    assert src.count(needle) == 1
    src = src.replace(needle, needle + ";escape_ledger_rows=[]")
    needle2 = "fullk,_,good=kernel(union);ok=good and j==fullk and subset(roots[events[j]],union)"
    assert src.count(needle2) == 1
    inject = """fullk,eligible_all,good=kernel(union);ok=good and j==fullk and subset(roots[events[j]],union)
    if not ok:
     comp_target=neg(union)
     ck,ce,cgood=kernel(comp_target);upper=comp[ck]
     singles=[]
     for aa in bridges:
      landing=old_join(basej,aa);esc=not subset(roots[events[landing]],union)
      singles.append({'atom_index':aa,'atom':old_record(aa),
       'full17_phantom':events[aa][1]==0,'landing_index':landing,
       'landing':old_record(landing),'landing_is_top':landing==comp[zero],
       'single_atom_escapes':esc})
     e0=tuple(0 for _ in macros)
     for aa in eligible_all:e0=op(1,e0,roots[events[aa]])
     sat_equal=e0==union
     escs=[z for z in singles if z['single_atom_escapes']]
     allphantom=all(z['full17_phantom'] for z in escs)
     alltop=all(z['landing_is_top'] for z in escs)
     agg=('CC-'+('E' if sat_equal else 'P')+
       ('P' if allphantom else 'N')+('T' if alltop else 'S'))
     escape_ledger_rows.append({'orientation':name,
      'left_child':child_record(x),'right_child':child_record(y),
      'target_root_sha256':rhash(union),
      'target_E_hex':hex(coarse_shadow(union,pos)[0]),
      'target_U_hex':hex(coarse_shadow(union,pos)[1]),
      'old_atom_fold_index':fullk,'old_atom_fold':old_record(fullk),
      'old_atom_fold_inside_target':good,
      'greatest_old_lower_exists':good,
      'greatest_old_lower_index':fullk if good else None,
      'greatest_old_lower':old_record(fullk) if good else None,
      'least_old_upper_index':upper if cgood else None,
      'least_old_upper':old_record(upper) if cgood else None,
      'least_old_upper_exists':cgood,
      'complement_target_root_sha256':rhash(comp_target),
      'complement_greatest_old_lower_index':ck,
      'complement_greatest_old_lower':old_record(ck),
      'complement_kernel_good':cgood,
      'complement_eligible_atom_count':len(ce),
      'complement_eligible_atom_digest_sha256':hashlib.sha256(
       ','.join(map(str,ce)).encode()).hexdigest(),
      'target_subset_least_old_upper':subset(union,roots[events[upper]]),
      'bridge_atom_indices':list(bridges),'bridge_atoms':list(bridge_records),
      'base_join_index':basej,'base_join':old_record(basej),
      'first_escaping_extension':first_escape,'single_atom_tests':singles,
      'atom_saturation_root_sha256':rhash(e0),
      'atom_saturation_equals_target':sat_equal,
      'atom_saturation_proper_below_target':subset(e0,union) and not sat_equal,
      'atom_saturation_old_fold_index':fullk,
      'atom_saturation_old_fold':old_record(fullk),
      'aggregate_type':agg,'actual_successor':'not_evaluated',
      'collapse_gates':'not_evaluated','state_fields':'not_evaluated'})"""
    src = src.replace(needle2, inject)
    needle3 = "out={'schema':SCHEMA,'schema_version':'1.0',"
    assert src.count(needle3) == 1
    src = src.replace(
        needle3,
        "out={'escape_ledger_internal':escape_ledger_rows,'schema':SCHEMA,'schema_version':'1.0',",
    )
    ns = {"__file__": SOURCE, "__name__": "_escape_ledger_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    base, _ = ns["payload"]()
    rows = base.pop("escape_ledger_internal")
    rows.sort(
        key=lambda r: (
            r["orientation"],
            r["left_child"]["root_sha256"],
            r["right_child"]["root_sha256"],
            r["target_root_sha256"],
        )
    )
    assert len(rows) == 12
    for i, row in enumerate(rows):
        side = "L" if row["orientation"].startswith("left") else "R"
        row["id"] = f"CC-{side}-{i:02d}"
        row["row_sha256"] = digest(row)
    source_receipt = json.load(open(SOURCE_RECEIPT))
    third = json.load(open(THIRD_RECEIPT))
    out = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "source_second_round_payload_sha256": source_receipt["payload_sha256"],
        "source_third_round_payload_sha256": third["payload_sha256"],
        "row_count": len(rows),
        "orientation_counts": {
            o: sum(r["orientation"] == o for r in rows)
            for o in sorted({r["orientation"] for r in rows})
        },
        "aggregate_type_counts": {
            t: sum(r["aggregate_type"] == t for r in rows)
            for t in sorted({r["aggregate_type"] for r in rows})
        },
        "rows": rows,
        "rows_chained_sha256": hashlib.sha256(
            "\n".join(r["row_sha256"] for r in rows).encode()
        ).hexdigest(),
        "scope": (
            "The 12 strict disjoint-union failures in the existing bounded "
            "coordinate-target second/third-round sample only. No actual-event "
            "successor, closure, collapse, state, OML, sigma, ODBC, or Phi claim."
        ),
        "not_evaluated": [
            "actual generated-event transition",
            "successor closure",
            "same-side boundary gate",
            "activation gate",
            "centre",
            "state extension/order separation",
            "conditional relation",
            "Phi",
        ],
        "verification_independence": (
            "Single deterministic instrumentation of the existing second-round "
            "producer; shares its MDD grammar and sample, and cross-references "
            "the independently banked third-round aggregate receipt."
        ),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "adjacent_coordinate_escape_ledger.py --verify"
        ),
        "evidence_class": "Executable verified bounded coordinate-control evidence",
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
    path = os.path.join(HERE, "adjacent_coordinate_escape_ledger.json")
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
                "rows": out["row_count"],
                "types": out["aggregate_type_counts"],
            },
            sort_keys=True,
        )
    )
