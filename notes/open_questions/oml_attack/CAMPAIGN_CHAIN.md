# Sigma-essential OML campaign chain

- **Grand problem:** decide whether every admissible concrete sigma-complete
  OML satisfies finite-trace sigma-liftability `Phi`.
- **Starting branch:** `oml-descent-sigma-essential-reduction`.
- **Starting commit:** `1547059a1d0b79873d807759a5a2f726b1331c4d`.
- **Starting worktree:** clean; branch matched
  `origin/oml-descent-sigma-essential-reduction`.
- **Active campaign:** Campaign 10 — non-atomic simultaneous-coordinate test.
- **Campaigns completed:** Campaign 1 — exact ODBC formalization; Campaign 2
  — cut-saturation and inverse-limit audit; Campaign 3 — minimal relational
  countermodel and realization gates; Campaign 4 — fine/coarse
  specializations; Campaign 6 — global integration; Campaign 7 — hostile
  audit; Campaign 8 — BOC normalization and finite two-coordinate test;
  Campaign 9 — arbitrary-base orthogonal-atom reduction.
  Campaign 5 finite audit was entered for the two-coordinate approximants;
  they passed structural gates and were Phi-tame.
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
| standard-Borel relation traces are `R` for sigma states and `closure(R)` for f.a. states | hand proved | proved |
| countably generated separating sigma-boundaries support puncture embeddings | refuted | refuted |
| invertible deterministic transport removes common boundary | refuted | refuted |
| fine T4At plus locally-countable-defect criterion implies Phi | hand proved | proved |
| coarse CIR plus envelope solvability gives a coherent Dirac lift | hand proved | proved |
| coarse ODBC is a weaker independent specialization | refuted | refuted |
| exact implication graph and non-tautology audit | hand proved | proved |
| conditional fine/coarse regime packaging | Lean verified | proved |
| boundary-obstruction completeness | open | open |
| locally countable finite-arity CSS implies GS | hand proved | proved |
| finite-degree N-G normalization | refuted | refuted |
| two-coordinate 44-survivor finite approximants | exhaustive finite evidence | structurally passed, Phi-tame |
| arbitrary two-atom complement closure | hand proved | proved |
| outsider-extremality lemma OE | open | open |
| binary closure implies countable disjoint closure | conditional hand proof | proved conditionally |
| orthogonal two-atom state trichotomy and Phi | conditional hand proof | proved conditionally |
| ODBC-S for every admissible OML | open | open |
| CODBC for every admissible OML | open | open |

## Counterexample ledger

| Architecture | Status |
|---|---|
| Cantor singleton Boolean boundary atlas | abstract fine control; common paste central and not order-separating |
| club-field local lifts | coarse incoherent control; no compatible coarse lift |
| actual admissible OML failure of ODBC | none |
| abstract two-fibre cut-saturated Helly-2 failure | abstract only; not an OML |
| Cantor singleton CSS-without-GS model | complete compact-ambient abstract relational countermodel; eligible spaces noncompact |
| standard-Borel local realization | complete locally; OML transport gates fail |
| two-selector P2xP2/P2xP3/P3xP2 | concrete finite OMLs, exact five blocks, trivial centre, order-separated, Phi-tame |
| orthogonal two-atom arbitrary-base family | complement closed; OML/maximal-block gates open; conditionally Phi-tame |

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
- Genuine transport must use nondeterministic nonclosed correspondences with
  proper coordinate subalgebras.
- Fine defect countable-subcover reflection and coarse same-`mu` envelope
  solvability plus boundary CIR are open as consequences of the admissible
  OML hypotheses.
- Normalization and realization-or-collapse completeness are both open.
- Lean section packaging fixes the witness externally and is not a
  formalization of concrete `X_p(J)`.
- N-G requires an explicit uncountable-incidence hub, infinite-arity
  constraint, or coarse inverse-limit coordinate.
- Arbitrary-base two-selector latticehood/maximal blocks remain open.
- `FC_bin` is incomplete and requires OE against outsider coefficients;
  maximal blocks require the separate at-most-five-form signature theorem.

## Next automatic pivot

Test the first non-atomic proxy pair with all three common-block regions
nonzero. Determine whether mixed closure creates simultaneous nonrectangular
transport or forces a common/central joint algebra. Preserve OE as the exact
unfinished structural theorem for the orthogonal-atom control.
