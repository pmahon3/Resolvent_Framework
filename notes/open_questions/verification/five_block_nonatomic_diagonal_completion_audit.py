#!/usr/bin/env python3
"""Audit diagonal overlap transport for the first non-atomic proxy pair."""

import argparse
import json
from pathlib import Path

from five_block_nonatomic_pair_completion_audit import audit
from five_block_nonatomic_pair_inflation_audit import audit as raw_audit

SCHEMA = "five-block-nonatomic-diagonal-orthogonal-completion-v1"


def diagonal_audit():
    result = audit(
        overlap_relation={(0, 0), (1, 1)},
        schema=SCHEMA,
        expected_maximal_blocks=9,
        expected_coordinate_relation=((0, 0), (0, 1), (1, 0), (1, 1)),
        expected_joint_charged_relation=((0, 0), (1, 1)),
    )
    raw = raw_audit(overlap_relation={(0, 0), (1, 1)})
    result["raw_structural_audit"] = {
        "checks": raw["checks"],
        "first_disjoint_union_failure": raw["first_disjoint_union_failure"],
        "first_extrema_failure": raw["first_extrema_failure"],
        "event_sha256": raw["event_sha256"],
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = diagonal_audit()
    assert all(result["checks"].values())
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
