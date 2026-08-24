#!/usr/bin/env python3
"""Complete one-point-inflation / one-crossing-event census.

All 512 subsets K of the 9-point inflated carrier are enumerated.  The old
12-event control is pulled back along 1a,1b -> 1, then K and K^c are adjoined
and exact complement/disjoint-union closure is taken.  Closed families are
deduplicated before exhaustive lattice, OM, join, split-atom, centre and point
state audits.  This is one deterministic implementation, not an independent
verification and not an actual adjacent-assembly realization.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "split_truth_atom_one_point_inflation_census.json"
FULL = (1 << 9) - 1
C = (1 << 1) | (1 << 2)  # inflated pullback of old singleton {1}
OLD_BASE_8 = {0x00, 0x02, 0x0D, 0x31, 0x0F, 0x33,
              0xCC, 0xF0, 0xCE, 0xF2, 0xFD, 0xFF}


def pull(mask8):
    out = mask8 & 1  # old point 0
    if mask8 & (1 << 1):
        out |= C
    for old_point in range(2, 8):
        if mask8 & (1 << old_point):
            out |= 1 << (old_point + 1)
    return out


BASE = {pull(mask) for mask in OLD_BASE_8}
A, B, H = pull(0xF0), pull(0xCC), pull(0xFD)
LITERAL = A | B
P00 = (1 << 0) | C


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def close_family(seeds):
    family = set(seeds)
    rounds = []
    while True:
        before = len(family)
        family.update(FULL ^ event for event in tuple(family))
        snapshot = tuple(family)
        for i, left in enumerate(snapshot):
            for right in snapshot[i + 1:]:
                if left & right == 0:
                    family.add(left | right)
        added = len(family) - before
        rounds.append(added)
        if added == 0:
            return family, tuple(rounds)


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
    first_failure = None
    for left in sorted(family):
        for right in sorted(family):
            lubs = extrema(family, left, right, True)
            glbs = extrema(family, left, right, False)
            if len(lubs) != 1 or len(glbs) != 1:
                first_failure = {
                    "left_hex": hex(left), "right_hex": hex(right),
                    "minimal_uppers_hex": [hex(x) for x in sorted(lubs)],
                    "maximal_lowers_hex": [hex(x) for x in sorted(glbs)],
                }
                return {"is_lattice": False, "first_failure": first_failure}
            joins[left, right] = lubs[0]
            meets[left, right] = glbs[0]

    om_failure = None
    for left in sorted(family):
        for right in sorted(family):
            if left & ~right == 0:
                rhs = joins[left, meets[right, FULL ^ left]]
                if rhs != right:
                    om_failure = {"left_hex": hex(left), "right_hex": hex(right)}
                    break
        if om_failure:
            break

    centre = [event for event in family if all(
        joins[meets[event, other], meets[event, FULL ^ other]] == event
        for other in family)]
    point_additivity_failure = None
    for point in range(9):
        bit = 1 << point
        for left in family:
            for right in family:
                if left & (FULL ^ right) == left:
                    if bool(joins[left, right] & bit) != (
                        bool(left & bit) or bool(right & bit)
                    ):
                        point_additivity_failure = {
                            "point": point, "left_hex": hex(left),
                            "right_hex": hex(right),
                        }
                        break
            if point_additivity_failure:
                break
        if point_additivity_failure:
            break

    return {
        "is_lattice": True,
        "first_failure": None,
        "orthomodular": om_failure is None,
        "first_om_failure": om_failure,
        "centre_masks_hex": [hex(x) for x in sorted(centre)],
        "centre_free": set(centre) == {0, FULL},
        "a_join_b_hex": hex(joins[A, B]),
        "a_join_b_equals_h": joins[A, B] == H,
        "literal_union_absent": LITERAL not in family,
        "h_splits_inflated_p00": bool(H & P00) and (H & P00) != P00,
        "point_state_additivity": point_additivity_failure is None,
        "first_point_additivity_failure": point_additivity_failure,
        "point_states_order_separate": True,
    }


def survivor_audit(family):
    """Maximal-block and exhaustive abstract-state census for a survivor."""
    events = sorted(family)
    index = {event: i for i, event in enumerate(events)}
    joins, meets = {}, {}
    for left in events:
        for right in events:
            joins[left, right] = extrema(family, left, right, True)[0]
            meets[left, right] = extrema(family, left, right, False)[0]

    def commutes(left, right):
        forward = joins[meets[left, right], meets[left, FULL ^ right]] == left
        reverse = joins[meets[right, left], meets[right, FULL ^ left]] == right
        assert forward == reverse
        return forward

    proper = [event for event in events if event not in (0, FULL)]
    compatible_subsets = []
    for bits in range(1 << len(proper)):
        subset = [proper[i] for i in range(len(proper)) if bits & (1 << i)]
        if all(commutes(left, right) for left, right in itertools.combinations(subset, 2)):
            compatible_subsets.append(frozenset(subset))
    maximal = [subset for subset in compatible_subsets if not any(
        subset < other for other in compatible_subsets)]
    blocks = [tuple(sorted(set(subset) | {0, FULL})) for subset in maximal]

    representatives = []
    seen = set()
    for event in proper:
        if event in seen:
            continue
        representatives.append(event)
        seen.update({event, FULL ^ event})
    states = []
    for bits in range(1 << len(representatives)):
        value = {0: 0, FULL: 1}
        for i, event in enumerate(representatives):
            value[event] = 1 if bits & (1 << i) else 0
            value[FULL ^ event] = 1 - value[event]
        good = True
        for left in events:
            for right in events:
                if left & (FULL ^ right) == left:
                    if value[joins[left, right]] != value[left] + value[right]:
                        good = False
                        break
            if not good:
                break
        if good:
            states.append(tuple(value[event] for event in events))
    point_states = {
        tuple(int(bool(event & (1 << point))) for event in events)
        for point in range(9)
    }
    return {
        "maximal_block_count": len(blocks),
        "maximal_block_size_histogram": {
            str(size): sum(len(block) == size for block in blocks)
            for size in sorted({len(block) for block in blocks})
        },
        "maximal_blocks_masks_hex": [
            [hex(event) for event in block] for block in sorted(blocks)
        ],
        "abstract_two_valued_state_count": len(states),
        "distinct_point_state_count": len(point_states),
        "all_abstract_states_are_point_states": set(states) <= point_states,
        "all_point_states_are_abstract_states": point_states <= set(states),
        "state_table_sha256": digest(states),
    }


def payload():
    closure_map = {}
    candidate_rows = []
    for k in range(1 << 9):
        family, rounds = close_family(BASE | {k, FULL ^ k})
        key = tuple(sorted(family))
        crossing = (k & C).bit_count() == 1 and 0 < (k & (FULL ^ C)) < (FULL ^ C)
        closure_map.setdefault(key, {"representative": k, "seeds": [], "rounds": rounds})
        closure_map[key]["seeds"].append(k)
        candidate_rows.append((k, crossing, digest([hex(x) for x in key])))

    family_rows = []
    survivors = []
    for key, meta in sorted(closure_map.items(), key=lambda item: (len(item[0]), item[1]["representative"])):
        family = set(key)
        result = audit(family)
        crossing_seeds = [k for k in meta["seeds"]
                          if (k & C).bit_count() == 1
                          and 0 < (k & (FULL ^ C)) < (FULL ^ C)]
        row = {
            "family_sha256": digest([hex(x) for x in key]),
            "representative_seed_hex": hex(meta["representative"]),
            "seed_count": len(meta["seeds"]),
            "crossing_seed_count": len(crossing_seeds),
            "first_crossing_seed_hex": None if not crossing_seeds else hex(min(crossing_seeds)),
            "event_count": len(family),
            "closure_round_addition_counts": list(meta["rounds"]),
            **result,
        }
        family_rows.append(row)
        if (crossing_seeds and result["is_lattice"] and result["orthomodular"]
                and result["centre_free"] and result["a_join_b_equals_h"]
                and result["literal_union_absent"]
                and result["h_splits_inflated_p00"]
                and result["point_state_additivity"]):
            row.update(survivor_audit(family))
            survivors.append(row)

    crossing_count = sum(crossing for _, crossing, _ in candidate_rows)
    result = {
        "schema": "split-truth-atom-one-point-inflation-census-v1",
        "schema_version": "1.0",
        "scope": (
            "Complete enumeration of all 512 one-event seeds K on the fixed "
            "9-point one-point-inflated carrier, with one deterministic "
            "implementation. Exact complement/disjoint-union closures are "
            "deduplicated and audited. Generic control only; no actual assembly "
            "or larger-fibre/multiple-transverse-event claim."
        ),
        "candidate_seed_count": 1 << 9,
        "crossing_seed_count": crossing_count,
        "distinct_closed_family_count": len(closure_map),
        "distinct_family_rows": family_rows,
        "survivor_count": len(survivors),
        "survivors": survivors,
        "producer_independence": "single implementation; deterministic cross-seed replay only",
        "evidence_class": "Executable verified exhaustive finite evidence",
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "split_truth_atom_one_point_inflation_census.py --verify"
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    assert crossing_count == 252
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
    print(json.dumps({
        "status": "PASS", "payload_sha256": result["payload_sha256"],
        "families": result["distinct_closed_family_count"],
        "survivors": result["survivor_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
