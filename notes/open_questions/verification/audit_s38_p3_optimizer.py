#!/usr/bin/env python3
"""Independent deterministic audit of the s38 period-three semantics."""
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_s37_p2_optimizer as independent_oracle  # noqa: E402

CORE = HERE / "census_2026-07-12_s35"
sys.path.insert(0, str(CORE))
import relay7_core as rc  # noqa: E402


def main():
    ports = list(rc.two_cell_maps(1))
    rng = random.Random(380301)
    triples = [tuple(ports[i] for i in ix) for ix in
               ((0, 0, 0), (0, 0, 195), (0, 195, 0), (195, 0, 0),
                (195, 195, 195))]
    triples += [tuple(rng.choice(ports) for _ in range(3)) for _ in range(995)]
    mismatches = 0
    root_live_differences = 0
    for maps in triples:
        for target in rc.COMMON_ZERO_TARGETS:
            independent_oracle.compare(maps, target)
            got = independent_oracle.independent(maps, target)
            passes = (all((x & rc.FACE) == rc.FACE for x in got["free"]) and
                      all(not (x & rc.FACE) for x in got["live"]) and
                      all(rc.false_nonorders(x & rc.COMPLEMENT) == 0
                          for x in got["live"]))
            mismatches += passes != rc.screen(maps, target)["passes"]
            root_live_differences += got["E1"][0] != got["live"][0]
    print(f"p3_k1_sample_triples={len(triples)}")
    print(f"map_target_comparisons={len(triples) * len(rc.COMMON_ZERO_TARGETS)}")
    print(f"screen_pass_mismatches={mismatches}")
    print(f"E1root_vs_live0_differences={root_live_differences}")


if __name__ == "__main__":
    main()
