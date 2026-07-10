# Reading list — σ-essential problem

The object: a concrete σ-complete non-Boolean irreducible OML carrying a finite 2-valued
state on a ⊥-closed subposet that extends to no global σ-additive 2-valued state. Localized
to σ-point-selection failure (`sigma_essential_reduction_writeup.md`); frontier is
non-Polish / non-standard-Borel / irreducibly non-central.

Sources in dependency order, each with the question to read it for.

## Descriptive set theory

**Kechris, *Classical Descriptive Set Theory* (GTM 156).** Borel / analytic / co-analytic
hierarchy → Borel equivalence relations → the Glimm–Effros dichotomy; then uniformization.
- State Glimm–Effros precisely (non-smooth ⟺ E₀ embeds ⟺ no Borel 2-valued transversal).
  Which word does not transport to clause (ii)? (§3j: "Borel.")
- Co-analytic uniformization-failure: why is its obstruction real-valued / over a
  standard-Borel base, hence DW-killed? (§3h)

**Gao, *Invariant Descriptive Set Theory*** (after Kechris). E₀/E∞/hyperfinite/turbulence.
- Define hyperfinite; state Adams–Kechris. Why is E∞ non-hyperfiniteness orthogonal to
  clause (ii)? (§3j)

## Large cardinals and forcing

**Jech, *Set Theory* (3rd millennium ed.).**
- Filters, ideals, ultrafilters: why is `ℱ_s = {A : s(A)=1}` not a filter on a non-Boolean
  concrete OML, even for a Dirac state? (§3a — MO₂: `a∩b≠∅` as sets yet `a∧b=0`.)
- Measurable cardinals, Ulam matrices: re-derive the matrix by hand (§3b); locate the line
  needing non-orthogonal unions / comprehension.
- Forcing: why does set-forcing preserve measurability (Lévy–Solovay)? (`forcing_programme_status.md`)

**Kanamori, *The Higher Infinite*** (after Jech, if the strength path calls). Measurable →
ultrapower → elementary embedding `j: V→M`.
- The UB route transports `U` along `j`, but `U` lives on Boolean P(κ); why is transport to
  orthogonal-only a costume? (§3b)

## Primary sources (read for technique)

**Navara–Pták 1983** (`navara_ptak_1983_byhand_read.md`). Re-derive their ZFC non-Dirac
σ-state. What makes `L_{f,g}` support it, and why is it not a witness? (`rem:np-builds-rescuer`)

**Derr–Williamson 2023 + Maharam 1972 §8** (`sigma_essential_prior_art_verdict.md`). Where
is inner-regularity load-bearing in Thm D.6 / Maharam §8.2?

**Blecher–Weaver 2017** (bounds §3, §3a). Identify the ultrafilter-from-masa step (Prop 2.3);
state the masa-free question it leaves open for the concrete 2-valued case.

## Notes

- Start: Kechris (Borel equivalence relations → Glimm–Effros).
- Definability-vs-existence first: read bounds §3f and §3j, plus the Lean polarity gate
  (`SigmaEssentialConjectures.lean`, `builds_state_implies_not_witness`).
- Operator algebra (masas, von Neumann algebras) is not on the critical path: the masa route
  is dead (§3a), so light functional analysis suffices for Blecher–Weaver.
- Chapter numbers are convenience pointers; navigate by topic.

*Companion: [[oml_lead_philosophical_reading]]; `sigma_essential_taxonomy.json`;
`sigma_essential_large_cardinal_bounds.md`.*
