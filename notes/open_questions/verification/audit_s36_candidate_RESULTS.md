# Independent s36 candidate audit

Both period-one width-four ports pass the independently reconstructed static
and incidence checks, but neither is a genuine bounded candidate.  Each fails
principal-master order separation already inside rooted cell 0.

The self-contained oracle `audit_s36_candidate_oracle.py` enumerates the 29
two-valued states directly from the seven blocks, constructs compatibility
edges directly from the four identifications, and computes infinite
exactly-one-target paths by graph fixed points.  It does not import either the
production relay core or downstream checker.

For target `a1`:

* `((0,11),(3,5),(6,9),(13,3))` has 19 possible cell-0 restrictions of
  principal-master paths.  They never witness the genuine non-order
  `a0 !<= a4` (among 10 total missed cell-0 non-orders).
* `((1,7),(5,9),(11,11),(12,3))` has 15 possible cell-0 restrictions.  They
  never witness `a0 !<= a10` (among 22 total missed cell-0 non-orders).

Both ports have all three face states on infinite all-zero paths and no face
state on an exactly-one-target path at the root.  Both have Berge girth five
in every tested window of 2, 3, 4, 6, 12, 24 and 48 cells.  Their adjacent
target block distances are both four.  Target distances were also recomputed
for gaps 1 through 30.  Thus the kill is specifically downstream global order
separation, not local face/liveness, girth, or master geometry.

The JSON artifact additionally checks cross-cell pairs from rooted cell 0 at
gaps 1 through 12; both ports miss further genuine non-orders at every tested
gap.  The cell-0 witnesses suffice for the rigorous kill.
