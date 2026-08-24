#!/usr/bin/env python3
"""Exact cell-11 trace alphabet on the q=r=1 interface.

This is a local-state census for the missing fourth cell in the node-6
three-cell corner construction.  It does not construct the four-cell carrier
or assert that the restricted alphabet is complete for global closure.
"""
import argparse
import collections
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import sharedq_kcell_completion_audit as cell
import full_grid_terminal_split_one_cell_quotient as one

SCHEMA = "full-grid-cell11-qr11-trace-alphabet-v1"


def sha_json(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def activation(state):
    return tuple(int(name in state) for name in cell.SHARED)


def coordinates(state):
    return (int("e11" in state or "e10" in state),
            int("e11" in state or "e01" in state))


def trace_mask(event, indices):
    return sum(1 << j for j, state_index in enumerate(indices)
               if event >> state_index & 1)


def payload():
    states = cell.cell_states()
    events = one.local_event_predicates(states)
    assert len(states) == 224 and len(events) == 56

    activations = sorted(set(activation(state) for state in states))
    assert activations == list(__import__("itertools").product((0, 1), repeat=3))

    rows = []
    union_indices = []
    for a in activations:
        indices = [i for i, state in enumerate(states)
                   if activation(state) == a and coordinates(state) == (1, 1)]
        assert indices
        union_indices.extend(indices)
        traces = sorted({trace_mask(event, indices) for event in events})
        full = (1 << len(indices)) - 1
        proper = [trace for trace in traces if trace not in (0, full)]
        histogram = collections.Counter(trace.bit_count() for trace in traces)
        complement_closed = all((full ^ trace) in set(traces) for trace in traces)
        assert complement_closed
        rows.append({
            "activation": list(a),
            "state_count": len(indices),
            "state_indices_sha256": sha_json(indices),
            "trace_count": len(traces),
            "proper_nonempty_trace_count": len(proper),
            "trace_size_histogram": [
                {"points": size, "traces": count}
                for size, count in sorted(histogram.items())],
            "trace_family_sha256": sha_json([hex(trace) for trace in traces]),
            "proper_trace_family_sha256": sha_json(
                [hex(trace) for trace in proper]),
            "complement_closed": complement_closed,
        })

    union_indices = sorted(union_indices)
    assert len(union_indices) == 72 and len(set(union_indices)) == 72
    coherent = sorted({trace_mask(event, union_indices) for event in events})
    union_full = (1 << len(union_indices)) - 1
    assert len(coherent) == 38
    assert all((union_full ^ trace) in set(coherent) for trace in coherent)

    activated = next(row for row in rows if row["activation"] == [1, 1, 1])
    assert activated["state_count"] == 1
    assert activated["trace_count"] == 2
    assert activated["proper_nonempty_trace_count"] == 0
    assert activated["trace_size_histogram"] == [
        {"points": 0, "traces": 1}, {"points": 1, "traces": 1}]

    out = {
        "schema": SCHEMA,
        "schema_version": "1.0",
        "single_cell_states": len(states),
        "single_cell_events": len(events),
        "qr11_states": len(union_indices),
        "qr11_state_indices_sha256": sha_json(union_indices),
        "coherent_qr11_trace_count": len(coherent),
        "coherent_qr11_complement_pairs": len(coherent) // 2,
        "coherent_qr11_trace_family_sha256": sha_json(
            [hex(trace) for trace in coherent]),
        "per_activation": rows,
        "activated_111_group_is_singleton": True,
        "activated_111_has_no_proper_nonempty_trace": True,
        "scope": (
            "Exact restrictions of the 56 certified cell events to local "
            "state groups with q=r=1. Direct-residue alphabet only; no "
            "four-cell closure, lattice, gate, or trace-sufficiency claim."),
        "dependency_sha256": {
            os.path.basename(cell.__file__): hashlib.sha256(
                open(cell.__file__, "rb").read()).hexdigest(),
            os.path.basename(one.__file__): hashlib.sha256(
                open(one.__file__, "rb").read()).hexdigest(),
        },
        "command": (
            "python3 notes/open_questions/verification/"
            "full_grid_cell11_qr11_trace_alphabet.py --verify"),
    }
    out["producer_sha256"] = hashlib.sha256(
        open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = sha_json(out)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = payload()
    path = os.path.join(HERE, "full_grid_cell11_qr11_trace_alphabet.json")
    if args.emit:
        with open(path, "w") as handle:
            json.dump(out, handle, sort_keys=True, indent=2)
            handle.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps({
        "status": "PASS",
        "payload_sha256": out["payload_sha256"],
        "qr11_states": out["qr11_states"],
        "coherent_qr11_trace_count": out["coherent_qr11_trace_count"],
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
