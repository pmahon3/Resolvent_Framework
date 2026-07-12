# s38 period-three width-one exhaustive result

All `196^3 = 7,529,536` ordered triples of labeled width-one interfaces were
screened for the seven-loop face `C={a0,a3,a11}`.  For target representatives
`a1,a2,a4`, the operative counts are respectively `0,0,0`.  Reflection gives
the same result for `a13,a12,a10`.

The sequential failure distribution is:

| target | face-free failure | face-nonlive failure | complement-order failure | operative |
|---|---:|---:|---:|---:|
| `a1` | 1,488,811 | 6,040,350 | 375 | 0 |
| `a2` | 1,496,688 | 6,032,443 | 405 | 0 |
| `a4` | 1,476,353 | 6,052,798 | 385 | 0 |

Each row sums to 7,529,536.  Thus the dominant obstruction is the local
free/nonlive tension: after face freedom, more than 99.99% of the remaining
triples make a face state live; the few exceptions lose complement order
separation.  No case reaches the additional root-cell `E1[0]` gate.

The C++ production engine records the complete run in
`s38_p3_k1_checkpoint.json`.  An independent Python implementation agrees
with `relay7_core` on all fixed-point masks and pass decisions for 1,000
deterministic triples and all six common-zero targets (6,000 comparisons).
