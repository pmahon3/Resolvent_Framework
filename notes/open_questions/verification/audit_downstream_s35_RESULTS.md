# Independent s35 downstream audit

`audit_downstream_s35.py` is standalone: it imports neither the census nor
`verify_s35_survivor_girth.py`.  It rebuilds finite chain quotients, computes
their bipartite incidence girth by BFS, and computes master target-gap block
distance by a separate block-intersection BFS.

## Exact result

- The two target-1 and two target-13 pairs have finite-window block girths
  `(5,4,4,4)` at 2, 3, 4, and 6 cells.  Thus all four fail at three cells.
- All nine target-2 and nine target-12 pairs have block girth at least five
  in every window from 2 through 12 cells.  Fifteen pairs have girth 5 and
  three pairs have girth 6 throughout those windows.
- Every one of those 18 pairs fails the complete-single-master test already
  at target gap `g=1`.  Fourteen have target-to-next-target block distance 2;
  four have distance 3.  A complete master block adds one block, so these
  close Berge cycles of length 3 or 4, below the required 5.  There are no
  downstream candidates.
- Reflection `a_i -> a_{-i mod 14}` fixes the face `{a0,a3,a11}` as a set,
  exchanges targets 2 and 12, and partitions the 18 labeled pairs into nine
  two-element orbits.  The script prints every orbit explicitly.
- Since all 18 are killed by master geometry, adjacent/cross-cell order
  separation is not reached and was intentionally not tested.

## Scope

Passing windows through 12 cells is bounded evidence, not by itself a proof
of infinite-chain girth.  This caveat does not weaken the no-go: the gap-1
master obstruction is an explicit local cycle certificate for every pair.
The conclusion is for the displayed period-1, width-3 maps and a single
complete master block.  It does not exclude period-varying relays or a
different, non-single-master completion.

Run with:

```sh
python3 notes/open_questions/verification/audit_downstream_s35.py
```
