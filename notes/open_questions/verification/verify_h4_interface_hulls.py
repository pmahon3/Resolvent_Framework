#!/usr/bin/env python3
"""Deterministic certificate for the fixed-interface outsider-elimination lemma.

This imports the independently banked cell constructor.  It checks all 46
private single-cell events, all normal forms on two retained coordinates, and
the q/q' repair rules used in the arbitrary-index direct-limit proof.
"""
import hashlib
import json
import sys
from pathlib import Path

import sharedq_kcell_completion_audit as base

SCHEMA = "h4-interface-hull-table-v1"
HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "h4_interface_hull_receipt.json"


def payload():
    states = base.cell_states()
    points = base.build_carrier(3, states)
    atoms = base.build_atom_masks(3, states, points)
    named, _, full = base.block_event_masks(3, atoms)

    def support(name):
        return {int(t.split("@")[1]) for t in name.split("+") if "@" in t}

    retained_map = {m: n for m, n in named.items() if support(n) <= {1, 2}}
    for i, j in ((1, 2), (2, 1)):
        for x in ("e11", "e10"):
            for y in ("e01", "e00"):
                m = atoms[f"{x}@{i}"] | atoms[f"{y}@{j}"]
                retained_map[m] = f"{x}@{i}+{y}@{j}"
    retained = sorted(retained_map.items(), key=lambda p: p[1])
    q = atoms["e11@1"] | atoms["e10@1"]
    interface = {0: "0", full: "1", q: "q", full ^ q: "q'"}
    for a in ("a1", "a2", "a3"):
        interface[atoms[a]] = a
        interface[full ^ atoms[a]] = a + "'"

    private3 = [(m, n) for m, n in named.items() if support(n) == {3}]
    hull_rows = []
    for w, name in sorted(private3, key=lambda p: p[1]):
        upper = [c for c in interface if w | c == c]
        minimal = [c for c in upper
                   if not any(d != c and d | c == c for d in upper)]
        assert len(minimal) == 1, name
        h = minimal[0]
        tested = 0
        for z, _ in retained:
            if w | z == z:
                tested += 1
                assert h | z == z, name
        hull_rows.append({"event": name.replace("@3", "@j"),
                          "least_interface_ceiling": interface[h],
                          "containing_retained_forms_tested": tested})

    # One outsider: x_1 + y_3 is replaced by x_1 + q'.  Check against every
    # raw or repair normal form supported on retained coordinates {1,2}.
    qprime = full ^ q
    one_rows = []
    for x in ("e11", "e10"):
        for y in ("e01", "e00"):
            w = atoms[x + "@1"] | atoms[y + "@3"]
            bar = atoms[x + "@1"] | qprime
            containing = 0
            for z, _ in retained:
                if w | z == z:
                    containing += 1
                    assert bar | z == z, (x, y)
            one_rows.append({"form": "%s@i+%s@j" % (x, y),
                             "replacement": "%s@i+q'" % x,
                             "containing_retained_forms_tested": containing})

    # The dual orientation follows by swapping q and q'.
    for y in ("e01", "e00"):
        for x in ("e11", "e10"):
            w = atoms[x + "@3"] | atoms[y + "@1"]
            bar = q | atoms[y + "@1"]
            for z, _ in retained:
                if w | z == z:
                    assert bar | z == z, (x, y, "dual")

    # If both repair coordinates are outsiders, compute its existential shared
    # signature support.  (One activated off-diagonal signature can be absent.)
    # Exhaust the universal signature supports of every retained one-/two-cell
    # normal form and verify that only 1 contains the outsider repair.
    by_sig = {}
    for s in states:
        by_sig.setdefault(base.signature(s), []).append(s)
    positions_by_sig = {
        sig: [p for p, (psig, _) in enumerate(points) if psig == sig]
        for sig in by_sig
    }
    retained_universal = {}
    for z, name in retained:
        retained_universal[name] = {
            sig for sig, positions in positions_by_sig.items()
            if all((z >> p) & 1 for p in positions)
        }
    saturation = []
    for x in ("e11", "e10"):
        for y in ("e01", "e00"):
            attainable = []
            for sig, fibre in sorted(by_sig.items()):
                if sig[3] == 1:
                    ok = any(x in s for s in fibre)
                else:
                    ok = any(y in s for s in fibre)
                if ok:
                    attainable.append(sig)
            containers = []
            for z, name in retained:
                if set(attainable) <= retained_universal[name]:
                    containers.append(name)
                    assert z == full, (x, y, name)
            saturation.append({"form": "%s@j+%s@l" % (x, y),
                               "attainable_shared_signatures":
                                   len(attainable),
                               "independent_containers": containers})

    return {
        "schema": SCHEMA,
        "private_event_count": len(private3),
        "retained_normal_forms_checked": len(retained),
        "interface_hulls": hull_rows,
        "one_outsider_repairs": one_rows,
        "dual_one_outsider_repairs_checked": 4,
        "two_outsider_repairs": saturation,
        "all_checks_pass": True,
    }


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def main():
    p = payload()
    if "--emit" in sys.argv:
        r = {"schema": SCHEMA,
             "payload_sha256": hashlib.sha256(canonical(p)).hexdigest(),
             "payload": p}
        RECEIPT.write_text(json.dumps(r, indent=1, sort_keys=True) + "\n")
        print("WROTE", RECEIPT)
        return
    receipt = json.loads(RECEIPT.read_text())
    assert receipt["schema"] == SCHEMA
    assert receipt["payload"] == p
    assert receipt["payload_sha256"] == hashlib.sha256(canonical(p)).hexdigest()
    print("PASS", SCHEMA, receipt["payload_sha256"])


if __name__ == "__main__":
    main()
