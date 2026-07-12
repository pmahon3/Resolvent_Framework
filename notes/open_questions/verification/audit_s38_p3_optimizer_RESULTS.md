# s38 period-three optimizer audit

- deterministic period-three width-one triples: 1,000;
- common-zero targets per triple: 6;
- map/target comparisons: 6,000;
- fixed-point or screen mismatches: 0;
- sampled `E1[0] != live[0]` cases: 0.

The last observation is sample-specific and does not weaken the mandatory
root-cell rule established in s36/s37.  The audit compares `E0`, `E1`, rooted
reachability, `live`, and `free` against an independent monotone-bitset
implementation.
