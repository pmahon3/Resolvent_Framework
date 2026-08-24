#!/usr/bin/env python3
"""Old-context discriminator for the first inadequate prefix doubleton."""
import argparse, hashlib, json, os, struct

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_ar_reb_001_prefix_classification.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_ar_reb_001_prefix_classification.json")
SCHEMA = "adjacent-ar-reb-001-doubleton-old-context-v1"
ROOT_HASHES = (
    "4d4062cd", "2572f79e",
)
CRITICAL = (15250, 16786, 10752, 18322, 18331)


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def payload():
    src = open(SOURCE).read()
    needle = "    source_receipt = json.load(open(SOURCE_RECEIPT))"
    pos = src.rfind(needle)
    assert pos >= 0
    replacement = "    globals()['_CTX_INTERNAL']={'family':family,'new_roots':new_roots,'bank':bank}\n" + needle
    src = src[:pos] + src[pos:].replace(needle, replacement, 1)
    ns = {"__file__": SOURCE, "__name__": "_doubleton_context_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns)
    ns["payload"]()
    data = ns["_CTX_INTERNAL"]
    family, new_roots, bank = data["family"], data["new_roots"], data["bank"]
    events, macros, engines = bank["all_events"], bank["macros"], bank["engines"]
    roots = {ev: root for root, ev in bank["root_to_event"].items()}
    principal = bank["principal"]
    upmap = {u: i for i, u in enumerate(principal)}

    def op(k, x, y): return tuple(engines[m].app(k, a, b) for m, (a, b) in enumerate(zip(x, y)))
    def neg(x): return tuple(engines[m].neg(a) for m, a in enumerate(x))
    zero_root = tuple(0 for _ in macros)
    def subset(x, y): return op(0, x, neg(y)) == zero_root
    def rhash(x): return hashlib.sha256(b"".join(struct.pack("<I", a) for a in x)).hexdigest()
    root_index = {roots[e]: i for i, e in enumerate(events)}
    comp = {i: root_index[neg(roots[e])] for i, e in enumerate(events)}
    n = len(events); allold = (1 << n) - 1; zero = upmap[allold]
    def old_join(x, y): return upmap[principal[x] & principal[y]]
    nonatomic = 0
    for d, upper in enumerate(principal):
        if d != zero: nonatomic |= upper & ~(1 << d)
    bits = allold & ~nonatomic & ~(1 << zero); atoms = []
    while bits:
        q = bits & -bits; atoms.append(q.bit_length() - 1); bits -= q
    def cut(x):
        lo = zero
        for a in atoms:
            if subset(roots[events[a]], x): lo = old_join(lo, a)
        lg = subset(roots[events[lo]], x)
        nx = neg(x); cl = zero
        for a in atoms:
            if subset(roots[events[a]], nx): cl = old_join(cl, a)
        ug = subset(roots[events[cl]], nx)
        return {"lower": lo if lg else None, "upper": comp[cl] if ug else None}

    chosen = []
    for prefix in ROOT_HASHES:
        matches = [x for x in new_roots if rhash(x).startswith(prefix)]
        assert len(matches) == 1, (prefix, len(matches))
        chosen.append(matches[0])
    critical = sorted(set(CRITICAL + tuple(comp[i] for i in CRITICAL)))
    def context_row(x, i):
        y = roots[events[i]]; dis = op(0, x, y) == zero_root
        row = {"old_index": i, "x_subset_old": subset(x, y), "old_subset_x": subset(y, x), "disjoint": dis}
        if dis:
            z = op(1, x, y)
            row.update({"union_root_sha256": rhash(z), "union_location": "new" if z in set(new_roots) else "old" if z in root_index else "absent", "union_old_cut": cut(z)})
        return row
    critical_rows = [[context_row(x, i) for i in critical] for x in chosen]
    critical_split = critical_rows[0] != critical_rows[1]
    full_scan = None
    first_full_difference = None
    if not critical_split:
        chains = []
        for x in chosen:
            rows = [context_row(x, i) for i in range(n)]
            chains.append(digest(rows))
        if chains[0] != chains[1]:
            for i in range(n):
                a, b = context_row(chosen[0], i), context_row(chosen[1], i)
                if a != b:
                    first_full_difference = {"old_index": i, "first": a, "second": b}; break
        full_scan = {"old_event_count_per_root": n, "signature_sha256": chains, "signatures_differ": chains[0] != chains[1]}
    source = json.load(open(SOURCE_RECEIPT))
    out = {"schema": SCHEMA, "schema_version": "1.0", "source_prefix_payload_sha256": source["payload_sha256"],
      "doubleton_root_sha256": [rhash(x) for x in chosen], "critical_old_indices": critical,
      "critical_context_rows": critical_rows, "critical_controls_split_doubleton": critical_split,
      "full_old_scan": full_scan, "first_full_scan_difference": first_full_difference,
      "cap_unchanged": 256, "closure_extended": False,
      "scope": "Exact old-context test for one inadequate frozen-prefix doubleton. Critical controls first; all-old scan only if needed. No new closure root, raised cap, lattice, OML, state, sigma, ODBC, or Phi claim.",
      "evidence_class": "Executable verified — sampled finite scope",
      "command": "PYTHONHASHSEED=0 python3 notes/open_questions/verification/adjacent_ar_reb_001_doubleton_old_context.py --verify"}
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest(); out["payload_sha256"] = digest(out); return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--emit", action="store_true"); ap.add_argument("--verify", action="store_true"); a = ap.parse_args()
    out = payload(); path = os.path.join(HERE, "adjacent_ar_reb_001_doubleton_old_context.json")
    if a.emit:
        with open(path, "w") as f: json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    else: assert json.load(open(path)) == out
    print(json.dumps({"status":"PASS","payload_sha256":out["payload_sha256"],"critical_split":out["critical_controls_split_doubleton"],"full_scan":out["full_old_scan"] is not None}, sort_keys=True))
