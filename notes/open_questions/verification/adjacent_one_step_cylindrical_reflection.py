#!/usr/bin/env python3
"""One-step cylindrical-reflection control on exact adjacent shadow types."""
import argparse, collections, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import adjacent_full_cycle_tagged_grid_prototype as tagged

SCHEMA = "adjacent-one-step-cylindrical-reflection-v1"


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def payload():
    base, b = tagged.capture(); L, R = b["L"], b["R"]
    left_shared = {E for E, U in L if E == U}
    right_shared = {E for E, U in R if E == U}
    shared = left_shared & right_shared
    rows = []
    counts = collections.Counter(); weighted = collections.Counter(); first_failure = None
    for A, nA in sorted(L.items()):
        EA, UA = A; PA = EA & ~UA
        for B, nB in sorted(R.items()):
            EB, UB = B; PB = EB & ~UB
            if EA & EB: continue
            left_cyl = not (PB & ~UA)
            right_cyl = not (PA & ~UB)
            for orientation, cyl, opposite in (("left", left_cyl, B), ("right", right_cyl, A)):
                if not cyl: continue
                counts[(orientation, "declared")] += 1; weighted[(orientation, "declared")] += nA*nB
                E, U = opposite; saturated = E == U; represented = saturated and E in shared
                key = "represented_saturated" if represented else "not_represented_saturated"
                counts[(orientation, key)] += 1; weighted[(orientation, key)] += nA*nB
                if not represented and first_failure is None:
                    first_failure = {"orientation": orientation, "left_E_hex": hex(EA), "left_U_hex": hex(UA),
                      "right_E_hex": hex(EB), "right_U_hex": hex(UB), "opposite_trace_saturated": saturated,
                      "opposite_trace_represented_in_shared_overlap": represented,
                      "left_type_multiplicity": nA, "right_type_multiplicity": nB}
    def nest(counter):
        return {o:{k:counter[(o,k)] for k in ("declared","represented_saturated","not_represented_saturated")}
          for o in ("left","right")}
    out = {"schema":SCHEMA,"schema_version":"1.0","source_tagged_shadow_payload_sha256":base["payload_sha256"],
      "shared_saturated_trace_count":len(shared),"left_saturated_trace_count":len(left_shared),"right_saturated_trace_count":len(right_shared),
      "shadow_type_counts":nest(counts),"event_pair_weighted_counts":nest(weighted),
      "all_declared_cylindrical_pairs_have_represented_saturated_opposite_trace":first_failure is None,
      "first_counterexample":first_failure,
      "interpretation":("The proposed one-step implication holds on every exact shadow type." if first_failure is None else
        "Cylinder-shaped union alone does not force the opposite operand to be shared-cell-saturated; partial opposite traces can be hidden where the retained operand is universal."),
      "neg023_cut_locality":"not touched: Neg-023 is a complemented actual-relation occurrence, not a declared first-round disjoint cylinder pair in this census.",
      "scope":"Exact census of all disjoint (E,U) shadow-type pairs for the certified adjacent full-cycle factors. Tests cylinder shape and membership of globally saturated opposite traces in the common overlap trace set; does not test exact partial section roots, generated closure, extrema persistence, latticehood, OML, sigma, ODBC, or Phi.",
      "evidence_class":"Executable verified — exhaustive finite scope",
      "exhaustive_scope":"All declared disjoint exact shadow-type pairs in both orientations; model-specific represented-overlap trace check.",
      "command":"PYTHONHASHSEED=0 python3 notes/open_questions/verification/adjacent_one_step_cylindrical_reflection.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest();out["payload_sha256"]=digest(out);return out


if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args();out=payload();path=os.path.join(HERE,"adjacent_one_step_cylindrical_reflection.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    else:assert json.load(open(path))==out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],"theorem":out["all_declared_cylindrical_pairs_have_represented_saturated_opposite_trace"]},sort_keys=True))
