# Global integration of the ODBC campaign chain

*Campaign 6, 2026-07-13. This note records the strongest honest integration.
Phi remains open.*

## 1. Exact implication graph

For every admissible concrete sigma-complete OML `L`:

`Phi(L) iff GSD(L) iff [ODBC-S(L) and CODBC(L)] iff coarse ODBC(L).`

The first equivalence is boundary-compatible sigma-surgery. The second is
the exact common-witness section factorization. The last uses the canonical
bijection between coherent envelope families and full-block sigma-states.
**Evidence class: hand proved.**

These equivalences are logically useful but do not reduce the conjecture:
ODBC as a whole and coarse ODBC are extensionally Phi.

For countably generated maximal blocks:

- `Phi -> T4At`. **Evidence class: Lean verified.**
- If the maximal-block atlas is countable, `T4At -> Phi`.
  **Evidence class: hand proved.**
- More generally, `T4At + CSR -> Phi`, where CSR says every cover of a
  coherent finite face by full-block bad loci has a countable subcover.
  **Evidence class: hand proved.**

For arbitrary blocks and fixed common `mu`:

`same-mu envelope solvability + CIR at every block -> eligible block lifts.`

This is objectwise and does not supply the common `mu` or globalization.
**Evidence class: hand proved.**

There are no proved arrows from T4At alone, bare cut-saturation, separate
local lifts, failure of CSR, or failure of CIR to ODBC.

## 2. Stable positive regions

Phi is proved under each of:

1. finite generated boundaries;
2. exact two-block atlas with literal trivial centre;
3. countable fine atlas plus T4At;
4. fine T4At plus CSR/local countability;
5. for every coherent finite pattern, relative closed eligibility plus finite
   subsystem sections.

All five listed theorem claims are **evidence class: hand proved**. The
distinct raw finite-overlap sublemma is **evidence class: Lean verified**.

## 3. Closed construction classes

The following do not yield a counterexample at their stated scope:

- common-base and common-boundary pastes;
- one-coordinate and independent-fibre inflations;
- invertible deterministic transported copies;
- repeated-selector quotient edges;
- gauge-trivial whole-interface twists;
- fully visible cyclic order coupling;
- rotating typed-graph sigma-class (fails latticehood);
- raw crossed three-block union (fails closure).

Each closure is recorded with its evidence class in the focused source note;
no class is promoted beyond that scope.

## 4. Why no final decisive theorem yet exists

ODBC itself cannot be nominated as the final residue without qualification:
it is Phi in section language. Fine CSR and coarse CIR are sufficient but
are not proved exhaustive; their failures do not yield counterexamples. The
nondeterministic transported-boundary realization theorem is asymmetric:
successful realization may yield a counterexample after all state gates,
whereas nonrealizability closes only that architecture.

Therefore legitimate stopping condition 3 is not met. **Evidence class:
hand proved** as a logical audit.

## 5. Boundary-obstruction completeness programme

A genuinely decisive bifurcation needs both:

### Normalization (N)

Every admissible failure `(L,p)` of Phi admits a finite-forced,
finite-degree presentation by nonclosed standard-Borel correspondences with
proper coordinate subalgebras, preserving no-GS and exactly one witnessed
obstruction form:

- **N-S:** a specified countable `J` has `X_p(J)=empty`, with every claimed
  smaller-subsystem section stated explicitly; or
- **N-G:** every countable `J` has a section but `X_p(I)=empty`.

### Realization-or-collapse completeness (RC)

Every normalized presentation either:

1. completes faithfully to an admissible concrete sigma-complete OML,
   preserving the fixed finite pattern, global f.a. witness, subsystem
   sigma-sections, no global sigma-section, maximal blocks, centre,
   essential irreducibility, and global sigma-state order separation; or
2. has a specified mixed-cut collapse whose class-level consequence forces a
   section for the obstructing `J` in N-S, or a global section in N-G.

Both clauses are **evidence class: open**. Their conjunction is called
**boundary-obstruction completeness (BOC)**. BOC is a decision programme,
not itself a proof of Phi: the realization branch may produce a
counterexample. An effective exclusive criterion selecting the branch would
be the final decisive theorem requested by stopping condition 3.

## 6. Best next action

Test N and RC simultaneously on the two-coordinate inflation of distinct
non-atomic selector families in the 44-event survivor. Audit in order:
faithfulness; sigma-closure; binary meets/joins; maximal blocks; centre;
exact boundary relation; sigma-completeness; same-witness subsystem
sections; global sigma-state order separation; forbidden finite pattern.

The earliest failed gate must be extracted as a class theorem; a passed
lattice gate suspends generalization and triggers the full Campaign-5 state
audit.

## 7. Lean integration

`ODBCRegimes.lean` proves only conditional packaging. Its
`SectionSystem.ODBC` hypothesis is the abstract conditional globalization
component, not the full mathematical conjunction ODBC-S plus CODBC:
`phi_of_fine_coarse_odbc_sections` and
`phi_of_regime_odbc_sections`. Both require explicit regime coverage,
applicable ODBC, finite/countable compatible subsystem sections, and GSD.
They do not assert that fine/coarse regimes exhaust traces or that either
satisfies ODBC. **Evidence class: Lean verified.**

These Lean theorems fix the input finitely additive state externally. They
do not formalize the note-level `X_p(J)` quantifier in which a common
`mu_J` is chosen existentially and may vary with `J`. **Evidence class:
hand proved** as a declaration-scope audit.
