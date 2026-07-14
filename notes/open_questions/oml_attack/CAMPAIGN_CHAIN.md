# Sigma-essential OML campaign chain

- **Grand problem:** decide whether every admissible concrete sigma-complete
  OML satisfies finite-trace sigma-liftability `Phi`.
- **Starting branch:** `oml-descent-sigma-essential-reduction`.
- **Starting commit:** `1547059a1d0b79873d807759a5a2f726b1331c4d`.
- **Starting worktree:** clean; branch matched
  `origin/oml-descent-sigma-essential-reduction`.
- **Active campaign:** Campaign 2 — lattice cut-saturation.
- **Campaigns completed:** Campaign 1 — exact ODBC formalization.
- **Global stopping status:** not reached.

## Theorem ledger

| Result | Evidence | Status |
|---|---|---|
| `X_p(I)` is the inverse limit of common-witness subsystem section spaces | hand proved | proved |
| ODBC = ODBC-S + CODBC implies GSD and `Phi` | hand proved using reviewed GSD | proved |
| abstract section implication `phi_of_odbc_sections` | Lean verified | proved |
| fine atomic and coarse two-level ODBC reformulations | hand proved | proved |
| ODBC-S for every admissible OML | open | open |
| CODBC for every admissible OML | open | open |

## Counterexample ledger

| Architecture | Status |
|---|---|
| Cantor singleton Boolean boundary atlas | abstract fine control; common paste central and not order-separating |
| club-field local lifts | coarse incoherent control; no compatible coarse lift |
| actual admissible OML failure of ODBC | none |

## Unresolved assumptions

- Finite event-face satisfiability has not been upgraded to a section over
  even two whole blocks.
- Neither ODBC-S nor CODBC follows from T4At or cut-saturation at present.
- Eligible sigma-state loci need not be closed or compact.
- Fine block generation does not imply a countable maximal-block atlas.

## Next automatic pivot

Define event-algebraic cut-saturation and test ODBC-S/CODBC first on two
blocks, trees, cycles, and finite interfaces. The first falsifiable test is
whether two-block centrality plus order separation excludes a boundary trace
whose every finite equation fragment sigma-lifts but whose full interface
does not.
