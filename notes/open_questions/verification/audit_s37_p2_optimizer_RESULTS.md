# Session 37 period-two optimizer audit

`audit_s37_p2_optimizer.py` independently reimplements the period-two
monotone bitset fixed points and compares every semantic mask with
`relay7_core.analyze`.

## Results

- Exhaustive period-two width-one comparison: 230,496 ordered
  map/target cases (`196^2 * 6`).
- Period-two width-two comparison: 1,000 deterministic ordered pairs from
  the 9,408 individually valid ports, for all six common-zero targets
  (6,000 cases).
- Compared masks: `E0`, `E1`, rooted `reach`, any-position `live`, and
  rooted all-zero `free`.
- Mask mismatches: **zero**.
- Independently reconstructed operative-screen mismatches: **zero**.
- In the width-two sample, `E1[0] != live[0]` in 47 of 6,000 cases.
  Consequently an any-position phase-live test cannot replace the mandatory
  root-cell `E1[0]` order-separation gate.

An additional exhaustive signature count found that the 9,408 valid
width-two ports have 9,408 distinct complete ordered successor-row tuples.
Thus bucketing by the complete transition relation is exact but provides no
compression.  A coarser derived signature is safe only if its sufficiency
for every bulk gate is proved, or if all retained pairs are reconstructed
and rechecked against the exact relation.  Phase swapping is not a safe
quotient because phase zero is the distinguished root.

The production C++ engine was also compiled independently and exercised on
three disjoint 100-row slices (first-port indices `0..99`, `4700..4799`, and
`9308..9407`, totalling 2,822,400 ordered pairs).  It reported zero operative
pairs for target representatives `a1`, `a2`, and `a4` on each slice, consistent
with the independent Python sample.  This is a translation smoke test, not a
replacement for the production engine's complete run.

## Reproduction

```sh
python3 notes/open_questions/verification/audit_s37_p2_optimizer.py
```

Observed output:

```text
p2_k1_map_target_comparisons=230496
p2_k2_individually_valid_ports=9408
p2_k2_sample_pairs=1000
p2_k2_map_target_comparisons=6000
screen_pass_mismatches=0
sample_E1root_vs_live0_differences=47
SAFE: bucketing is exact only when the complete ordered successor row tuple (or a proved sufficient derived signature) is retained
UNSAFE: phase swap under rooted phase-zero semantics
MANDATORY: audit E1[0] separately from any-position live[0]
```
