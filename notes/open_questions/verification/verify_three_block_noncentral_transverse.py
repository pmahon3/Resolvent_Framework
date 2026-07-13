#!/usr/bin/env python3
"""Check the recorded gates of the finite noncentral transverse triangle."""

import json
from pathlib import Path


receipt = json.loads((Path(__file__).parent / "three_block_noncentral_transverse_schema.json").read_text())
assert receipt["schema"] == "three-block-noncentral-transverse-v1"
assert receipt["carrier"] == {
    "events": 56,
    "maximal_block_count": 7,
    "maximal_block_sizes": [16] * 7,
    "points": 16,
}
assert receipt["selected_triangle"] == ["A01", "C01", "A10"]
assert receipt["transverse_triangle"] == {
    "incident_joint_closure_sizes": [8, 8, 8],
    "incident_joint_closures_proper": True,
    "interfaces_distinct_at_each_endpoint": True,
    "nontrivial_interface_events_noncentral": True,
    "pairwise_interface_sizes": [4, 4, 4],
}
gates = receipt["completion_gates"]
assert gates["centre_size"] == 2
assert gates["full_maximal_boundary_sizes"] == [16] * 7
assert all(value is True for key, value in gates.items()
           if key not in {"centre_size", "full_maximal_boundary_sizes"})
assert receipt["state_gates"] == {
    "every_selected_triangle_state_extends": True,
    "global_coherent_block_states": 16,
    "global_states_equal_point_evaluations": True,
    "phi_tame_by_finiteness": True,
    "point_evaluations_order_separate": True,
    "selected_triangle_coherent_states": 12,
    "selected_triangle_extendable_states": 12,
    "sigma_essential_state": False,
}
print("PASS: finite noncentral transverse triangle receipt has every recorded gate")
