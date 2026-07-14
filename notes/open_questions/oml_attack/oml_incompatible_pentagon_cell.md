# Incompatible pentagon conditional cell

*Campaign 14, 2026-07-14. Exact finite relation-cell gate.*

Let the five Boolean blocks on atoms modulo ten be

\[
 B_i=\{2i,2i+1,2i+2\pmod {10}\},\qquad i<5.
\]

The canonical two-valued-state representation is a concrete 22-event OML on
11 points. Designate

\[
 (a_1,a_2,a_3,q,r)=(1,3,5,7,9).
\]

Its exact projected state table is

```
01110 01000 00010 11111 11100 11001
10011 10000 00111 00100 00001
```

Consequently the activated profiles are exactly `11100` and `11111`:
`111 => q=r`, both diagonal values occur, and both mismatches are excluded.
All four output profiles occur off activation. The activation support is two
carrier points but is not an event. Every pair of designated events is
incompatible.

The executable certificate exhaustively verifies unique binary extrema,
complement and disjoint-union closure, the orthomodular law, complete
two-valued-state enumeration, point-state order separation, trivial centre,
and the truth table. Every nonzero event contains an off-activation point, so
the exact state-separation escape condition holds. The maximal-block audit
gives precisely the five displayed Boolean blocks.

**Evidence class:** executable verified plus exhaustive finite evidence;
hostile independently audited. Certificate:
`../verification/pentagon_incompatible_conditional_cell.py`.

An additional exhaustive scan of atom/coatom designations finds 780 choices
with the truth-table condition and all four aggregate off-activation output
profiles. None has the much stronger property that off-activation states alone
order-determine every ordered pair; the displayed cell does not need that
property, since every nonzero event—not every nonorder—has an off-activation
charging state.

## Scope and remaining gate

This is a finite Phi-tame relation cell, not a counterexample. It proves that
order separation and OML identities do not forbid direct incompatible
conditional equality. It does not prove preservation after two-cell pasting,
canonical mixed-cut completion, an uncountable assembly, or sigma-completion.

The three premises are pairwise incompatible and their joint support is not an
event. They are not claimed to generate a literal horizontal-sum `H4` sub-OML;
that stronger presentation is unnecessary for the semantic cell but remains a
possible assembly constraint.

**Next falsifiable test:** paste two copies around shared output coordinates,
compute canonical orthogonal completion, and audit whether completion creates
an activated mismatch or an event supported inside the activation cylinder.
