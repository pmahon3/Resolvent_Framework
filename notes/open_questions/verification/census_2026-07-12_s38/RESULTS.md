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

## Near-miss classification and rooted obstruction

The schema-2 checkpoint retains all 1,165 complement-order failures and the
exact absent ordered nonorders in every phase.  Their target counts are
`375,405,385`, as above.  Every case first fails order separation at the
distinguished root phase zero.  More strongly, the single target-independent
witness

\[
 a_3\nleq a_1
\]

is absent from the phase-zero complement-live state set in all 1,165 cases.
Thus the proposed witness-family cover collapses to one witness.  Since
`a3` belongs to the face `C={a0,a3,a11}`, the obstruction is already rooted
at Sasaki depth zero.

`classify_near_misses.py` reproduces the common-witness intersections and
greedy covers in `s38_near_miss_classification.json`.  The independent
finite-lattice audit `sasaki_root_audit.py` reconstructs the 30-element OML,
checks orthocomplementation and the orthomodular identity on every comparable
pair, and enumerates right-Sasaki closure through depth four.  The premises
are already Sasaki-closed; the common rooted hit occurs at depth zero.
