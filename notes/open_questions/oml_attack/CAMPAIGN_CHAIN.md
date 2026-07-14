# Sigma-essential OML campaign chain

- **Grand problem:** decide whether every admissible concrete sigma-complete
  OML satisfies finite-trace sigma-liftability `Phi`.
- **Starting branch:** `oml-descent-sigma-essential-reduction`.
- **Starting commit:** `1547059a1d0b79873d807759a5a2f726b1331c4d`.
- **Starting worktree:** clean; branch matched
  `origin/oml-descent-sigma-essential-reduction`.
- **Active campaign:** Campaign 3 — minimal ODBC countermodel.
- **Campaigns completed:** Campaign 1 — exact ODBC formalization; Campaign 2
  — cut-saturation and inverse-limit audit.
- **Global stopping status:** not reached.

## Theorem ledger

| Result | Evidence | Status |
|---|---|---|
| `X_p(I)` is the inverse limit of common-witness subsystem section spaces | hand proved | proved |
| ODBC = ODBC-S + CODBC implies GSD and `Phi` | hand proved using reviewed GSD | proved |
| abstract section implication `phi_of_odbc_sections` | Lean verified | proved |
| fine atomic and coarse two-level ODBC reformulations | hand proved | proved |
| finite generated boundaries imply ODBC | hand proved | proved |
| exact two-block trivial-centre atlases satisfy ODBC | hand proved | proved |
| relative closed eligibility plus finite sections implies a global section | hand proved | proved |
| bare abstract profile cut-saturation implies ODBC-S | refuted | refuted |
| OML-coupled cut-saturation implies ODBC-S | open | open |
| ODBC-S for every admissible OML | open | open |
| CODBC for every admissible OML | open | open |

## Counterexample ledger

| Architecture | Status |
|---|---|
| Cantor singleton Boolean boundary atlas | abstract fine control; common paste central and not order-separating |
| club-field local lifts | coarse incoherent control; no compatible coarse lift |
| actual admissible OML failure of ODBC | none |
| abstract two-fibre cut-saturated Helly-2 failure | abstract only; not an OML |

## Unresolved assumptions

- Finite event-face satisfiability has not been upgraded to a section over
  two selected blocks inside an arbitrary larger atlas, or over a full
  two-block atlas without literal trivial centre.
- Neither ODBC-S nor CODBC follows from T4At or cut-saturation at present.
- Eligible sigma-state loci need not be closed or compact.
- Fine block generation does not imply a countable maximal-block atlas.
- Bare event cut-saturation does not imply a Helly property for eligible
  common-state loci.
- Relative closedness of eligibility fails for `P(N)` and is open on the
  attainable traces of centre-free OMLs.

## Next automatic pivot

Test the three-block section hierarchy in order: singleton, pair, then
triple. At the first abstract failure, realize the fibres by Boolean
sigma-fields, transport boundaries noncentrally, and audit mixed lattice
cuts. Preserve `P(N)` as the finite-equation control.
