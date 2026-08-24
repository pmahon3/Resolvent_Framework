#!/usr/bin/env python3
"""Exhaustive same-carrier one-event centre-killing no-go.

The stronger mathematical reason is that the banked control contains the
singleton event {1}; every complement/disjoint-union-closed extension on the
same carrier keeps a represented singleton central.  The census independently
checks all 256 possible single-event adjunctions and their exact closures.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "split_truth_atom_centre_killing_no_go.json"
OMEGA = 0xFF
BASE = {0x00, 0x02, 0x0D, 0x31, 0x0F, 0x33,
        0xCC, 0xF0, 0xCE, 0xF2, 0xFD, 0xFF}
A, B, H = 0xF0, 0xCC, 0xFD


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def close_family(seeds):
    family = set(seeds)
    while True:
        before = len(family)
        family.update(OMEGA ^ event for event in tuple(family))
        snapshot = tuple(family)
        for i, left in enumerate(snapshot):
            for right in snapshot[i + 1:]:
                if left & right == 0:
                    family.add(left | right)
        if len(family) == before:
            return family


def extrema(family, left, right, upper):
    if upper:
        bounds = [event for event in family if (left | right) & ~event == 0]
        return [event for event in bounds if not any(
            other != event and other & ~event == 0 for other in bounds)]
    bounds = [event for event in family
              if event & ~left == 0 and event & ~right == 0]
    return [event for event in bounds if not any(
        other != event and event & ~other == 0 for other in bounds)]


def audit(family):
    joins, meets = {}, {}
    for left in family:
        for right in family:
            lubs = extrema(family, left, right, True)
            glbs = extrema(family, left, right, False)
            if len(lubs) != 1 or len(glbs) != 1:
                return None
            joins[left, right] = lubs[0]
            meets[left, right] = glbs[0]
    for left in family:
        for right in family:
            if left & ~right == 0:
                if joins[left, meets[right, OMEGA ^ left]] != right:
                    return None
    centre = [event for event in family if all(
        joins[meets[event, other], meets[event, OMEGA ^ other]] == event
        for other in family)]
    return joins, centre


def payload():
    closures = {}
    for candidate in range(256):
        family = close_family(BASE | {candidate})
        key = tuple(sorted(family))
        closures.setdefault(key, candidate)

    rows = []
    successes = []
    for family_key, representative in sorted(
        closures.items(), key=lambda item: (len(item[0]), item[1])
    ):
        family = set(family_key)
        result = audit(family)
        assert result is not None
        joins, centre = result
        preserves_join = joins[A, B] == H
        centre_free = set(centre) == {0x00, 0xFF}
        row = {
            "representative_adjoined_mask_hex": hex(representative),
            "event_count": len(family),
            "a_join_b_mask_hex": hex(joins[A, B]),
            "preserves_a_join_b_equals_h": preserves_join,
            "centre_masks_hex": [hex(event) for event in sorted(centre)],
            "centre_free": centre_free,
            "family_sha256": digest([hex(event) for event in family_key]),
        }
        rows.append(row)
        if preserves_join and centre_free:
            successes.append(row)

    assert len(closures) == 43
    assert all(row["preserves_a_join_b_equals_h"] for row in rows[:-1])
    assert not successes
    result = {
        "schema": "split-truth-atom-centre-killing-no-go-v1",
        "schema_version": "1.0",
        "scope": (
            "Exhaustive over all 256 one-subset adjunctions to the fixed "
            "8-point control, followed by exact complement/disjoint-union "
            "closure and all-pair lattice/OM/centre audit. The accompanying "
            "singleton-centrality theorem closes every same-carrier extension, "
            "not only this one-event census. No larger-carrier claim."
        ),
        "candidate_subset_count": 256,
        "distinct_closed_family_count": len(closures),
        "all_distinct_closures_are_omls": True,
        "preserving_centre_free_candidate_count": len(successes),
        "singleton_central_event_mask_hex": "0x2",
        "rows": rows,
        "hand_theorem": (
            "If {p} is an event in a complement/disjoint-union-closed family "
            "of subsets, then {p} is central in every same-carrier extension "
            "with those closures: for each event x, either p is absent and x "
            "is disjoint from {p}, or p is present and x\\{p} is the complement "
            "of {p} union complement(x)."
        ),
        "evidence_class": (
            "Executable verified exhaustive finite evidence plus Hand proved "
            "same-carrier singleton-centrality no-go"
        ),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "split_truth_atom_centre_killing_no_go.py --verify"
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    result["payload_sha256"] = digest(result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = payload()
    if args.emit:
        RECEIPT.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    if args.verify or not args.emit:
        assert json.loads(RECEIPT.read_text()) == result
    print(json.dumps({"status": "PASS", "payload_sha256": result["payload_sha256"]}))


if __name__ == "__main__":
    main()
