#!/usr/bin/env python3
"""Ten-control old-context test for all 16 inadequate prefix doubletons."""
import argparse, collections, hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_ar_reb_001_doubleton_old_context.py")
PREFIX_RECEIPT = os.path.join(HERE, "adjacent_ar_reb_001_prefix_classification.json")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_ar_reb_001_doubleton_old_context.json")
SCHEMA = "adjacent-ar-reb-001-all-doubleton-old-context-v1"


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "    source = json.load(open(SOURCE_RECEIPT))"
    assert src.count(needle) == 1
    src = src.replace(
        needle,
        "    globals()['_ALL_CTX']={'new_roots':new_roots,'critical':critical,'context_row':context_row,'rhash':rhash,'n':n}\n" + needle,
    )
    ns = {"__file__": SOURCE, "__name__": "_all_doubleton_context_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    ns["payload"]()
    data = ns["_ALL_CTX"]
    new_roots, critical, context_row, rhash, n = (
        data["new_roots"], data["critical"], data["context_row"], data["rhash"], data["n"]
    )
    by_hash = {rhash(x): x for x in new_roots}
    prefix = json.load(open(PREFIX_RECEIPT))
    pairs = []
    for div in prefix["first_descriptor_divergences"]:
        hs = [x["root_sha256"] for x in div["behavior_examples"]]
        assert len(hs) == 2
        pairs.append((div["descriptor_sha256"], hs))
    assert len(pairs) == 16

    results = []
    first_distribution = collections.Counter()
    survivor_count = 0
    full_scan_split = 0
    for descriptor, hs in pairs:
        xs = [by_hash[h] for h in hs]
        rows = [[context_row(x, i) for i in critical] for x in xs]
        first = None
        for i, (a, b) in enumerate(zip(*rows)):
            if a != b:
                first = {"old_index": critical[i], "first": a, "second": b}
                first_distribution[critical[i]] += 1
                break
        full = None
        if first is None:
            survivor_count += 1
            hashes = []
            first_full = None
            for x in xs:
                hashes.append(digest([context_row(x, i) for i in range(n)]))
            if hashes[0] != hashes[1]:
                full_scan_split += 1
                for i in range(n):
                    a, b = context_row(xs[0], i), context_row(xs[1], i)
                    if a != b:
                        first_full = {"old_index": i, "first": a, "second": b}
                        break
            full = {"signature_sha256": hashes, "split": hashes[0] != hashes[1], "first_difference": first_full}
        results.append({
            "descriptor_sha256": descriptor,
            "root_sha256": hs,
            "critical_signature_sha256": [digest(r) for r in rows],
            "critical_controls_split": first is not None,
            "first_critical_discriminator": first,
            "full_old_scan": full,
        })
    source = json.load(open(SOURCE_RECEIPT))
    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "source_first_pair_payload_sha256": source["payload_sha256"],
        "source_prefix_payload_sha256": prefix["payload_sha256"],
        "inadequate_doubleton_count": len(pairs),
        "critical_controls_split_count": len(pairs) - survivor_count,
        "critical_survivor_count": survivor_count,
        "first_critical_discriminator_distribution": dict(sorted(first_distribution.items())),
        "survivors_full_old_scan_count": survivor_count,
        "survivors_split_by_full_old_scan": full_scan_split,
        "unresolved_after_full_old_scan": survivor_count - full_scan_split,
        "pair_results": results,
        "cap_unchanged": 256, "closure_extended": False,
        "verdict": "ten critical old contexts split every inadequate doubleton" if survivor_count == 0 else "some doubletons require the conditional all-old scan",
        "fir_scale_all_pairs_scan_needed": survivor_count > 0,
        "scope": "All 16 inadequate doubletons in the frozen 256-root prefix, using the same ten old controls; all-old scans only for survivors. No closure extension, raised cap, lattice, OML, state, sigma, ODBC, or Phi claim.",
        "evidence_class": "Executable verified — sampled finite scope",
        "command": "PYTHONHASHSEED=0 python3 notes/open_questions/verification/adjacent_ar_reb_001_all_doubleton_old_context.py --verify",
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest(); out["payload_sha256"] = digest(out); return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--emit", action="store_true"); ap.add_argument("--verify", action="store_true"); a = ap.parse_args()
    out = payload(); path = os.path.join(HERE, "adjacent_ar_reb_001_all_doubleton_old_context.json")
    if a.emit:
        with open(path, "w") as f: json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    else: assert json.load(open(path)) == out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],"critical_split":out["critical_controls_split_count"],"survivors":out["critical_survivor_count"]}, sort_keys=True))
