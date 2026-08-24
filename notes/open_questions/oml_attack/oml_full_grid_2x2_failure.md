# Full conditional-cell 2x2 grid failure

## Construction and scope

Four copies (D_{\alpha i}), \(\alpha,i<2\), of the verified 56-event
literal-`MO3` conditional cell were pasted on the full compatible-state fibre.
Cells in row \(\alpha\) share their activation triple and input (q_\alpha);
cells in column (i) share output (r_i).  No other equality is imposed.  The
raw family is the union of the four pulled-back cell families and the tested
completion is its least complement/disjoint-union-closed concrete family.

The deterministic exhaustive certificate is
`../verification/full_grid_2x2_conditional_cell_audit.py`, with receipt
`../verification/full_grid_2x2_conditional_cell.json`.

## Exact negative result

The compatible carrier has 6,186,568 points in 842 nonempty macro-fibres.  The
raw union has 198 events.  Concrete orthogonal closure adds 32 events in one
substantive round and stabilizes at 230 events, but the result is **not a
lattice**.

Indeed, put

\[
 x=e_{01}^{(0,1)}=\{q_0=0,r_1=1\},\qquad
 y=e_{10}^{(1,0)}=\{q_1=1,r_0=0\}.
\]

They have precisely two minimal upper bounds in the completed family:

\[
 u=(e_{11}^{(0,0)})^\perp=\neg(q_0=1,r_0=1),
 \qquad
 v=(e_{00}^{(1,1)})^\perp=\neg(q_1=0,r_1=0).
\]

Both dominate (x,y): (x\le u) by (q_0=0), (y\le u) by (r_0=0),
while (x\le v) by (r_1=1) and (y\le v) by (q_1=1).  They are
incomparable on the compatible carrier, and the exhaustive order census proves
there is no third event below both and above (x,y).  The maximal lower bound
is uniquely (0).  Thus the conditional gadgets do not select either bound of
the stripped rectangle obstruction.

**Evidence class:** executable verified plus exhaustive finite evidence.  The
displayed domination argument is hand proved; minimality and exhaustion are
machine verified.

## Semantic controls

The failure is structural rather than relational.  All four cell projections
retain exactly the intended 30-profile relation.  The full macro-relation is
exactly the four edge implications, and when both rows activate its
\((q_0,q_1,r_0,r_1)\)-fibre is

\[
 \{(0,0,0,0),(1,1,1,1)\}.
\]

Neither row activation cylinder is an event, and every nonzero event in the
230-event completion has a carrier point off each activation cylinder.

## Consequence

The proposed full-grid arrow fails already at (K_{2,2}) under ordinary
concrete orthogonal closure.  A scalable grouped-output construction requires
a genuine rectangle-cut repair which adds a least upper bound below (u,v),
not merely the pair-local repairs sufficient for a one-hub row.  Because that
repair would be a new event with four-edge support, its effects on conditional
semantics, joint-boundary reconstruction, centre, and higher overlapping
rectangles must be audited before any countable or uncountable promotion.

