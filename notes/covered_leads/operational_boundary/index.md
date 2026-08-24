# The Operational Boundary

*Seed note — 2026-05-20*

## The observation

The finite/countable boundary (FA vs σ-additive) cannot be detected
from finite data.  Every finitary test — first-order sentences,
finite covers, sheaf conditions on finite refinements — is passed
equally by σ-additive measures and PFA charges.  This is not a
technical gap; it is a theorem (Łoś ultraproduct, Espíndola
collapse, Biesel finite-covers-only).

Every attempt to *grade* the boundary (put a continuous parameter on
"how σ-additive") also fails:

- Supremum-over-refinements collapses to {0, ∞} (Halmos dichotomy).
- Rate of tail decay and PFA mass are independent (SSK 2021).
- The proposed single axis (light tails → heavy tails → PFA) does
  not exist.

**But the boundary has operational consequences that are always
detectable.**

## The trade

Replace "can we know the rate?" with "how long will it take to know
the rate?"  The first question is about the boundary itself
(undecidable from finite data).  The second question is about
convergence conditional on being on one side of the boundary, and
has a definite finite answer for every (n, k).

Specifically:

- If the true measure is σ-additive with regularity s relative to
  the observation system, the estimation rate is
  n^{−s/(2s+D_Λ)}.  This is the D_Λ framework.

- If the true charge has a PFA component of mass ε, then at
  resolution G_k the estimation error has a floor at ε that no
  amount of data can reduce.  The PFA mass is invisible to finite
  refinements but manifests as a non-vanishing estimation floor.

- The *difference* between these two regimes — convergence to zero
  vs convergence to a positive floor — is detectable from finite
  data via standard rate-estimation diagnostics.

Under the conditions where the PFA component is small relative to
the observation resolution (i.e., the CE condition holds at a rate
compatible with the observation horizon), the operational
distinction between "is σ-additive" and "looks σ-additive at every
accessible scale" is vacuous.

## What this is NOT

- It is not a way to *detect* σ-additivity.  You cannot determine
  from finite data whether the underlying charge is σ-additive.
  The boundary is epistemically inaccessible.

- It is not a graded parameter interpolating FA and σ-additive.
  The tail-decay seed is dead (SSK 2021).  The boundary does not
  grade.

- It is not a new theorem.  The rate n^{−s/(2s+D)} is classical
  (Stone 1982, nonparametric estimation).  The PFA floor is a
  restatement of the Yosida-Hewitt decomposition.  The
  undetectability is a restatement of Łoś/ultraproduct.

## What it IS

A precise statement of how the finite/countable boundary is
*operationally present* without being *epistemically accessible*:

> You can't touch the boundary.  But you can always feel it,
> relative to your operational perspective.

"Feeling it" means: the convergence rate of your estimator encodes
which side of the boundary you're on.  If σ-additive, the rate is
n^{−s/(2s+D_Λ)} and improves with data.  If PFA, the rate plateaus.
The plateau is detectable.  The cause of the plateau (PFA mass vs
insufficient resolution vs model misspecification) is not
distinguishable from finite data — but the plateau itself is.

This is the programme's observer-dependence earning its keep.  The
refinement-independent question dies.  The refinement-dependent
question survives, because it asks something weaker: not "what is
the measure?" but "what does the measure look like through this
instrument?"

## Connection to existing notes

- `notes/unsorted/finite_sample/observational_resolution/index.md`:
  D_Λ framework — the quantitative apparatus.
- `notes/covered_leads/tail_decay_graded_sigma_additivity.md`:
  dead predecessor — tried to grade the boundary itself.
- `notes/reading_directions/`: the finite/countable boundary
  literature (Howson, Frot, Espíndola, Biesel) documents the
  inaccessibility side.
- `notes/archive/strategy_d_killed/ultralimit_investigation/strategy_d_dossier.md`:
  Strategy D — the question of whether the boundary can be
  structurally absent (no σ-additive measures at all).

## The recursive undermining argument

Any information-theoretic distinguishability criterion for the
boundary falls into one of two cases:

1. **Too weak:** satisfied by PFA charges (they pass all finite
   tests).  Fails to detect the boundary.

2. **Too strong:** equivalent to σ-additivity (quantifies over all
   countable sequences).  Restates the boundary, doesn't explain it.

There is no intermediate logic between first-order (has compactness,
can't see the boundary) and full second-order (lacks compactness,
sees the boundary by brute force) that both has compactness and can
express σ-additivity.  Espíndola's L_{ω₁,ω} completeness theorem
confirms this from the topos side.

The operational trade sidesteps this by not trying to detect the
boundary.  It asks a conditional question: *given that you're on
one side, what can you learn and how fast?*

## What a theorem would look like

A formal version might say:

**Statement (informal).**  Let (G_k, Λ) be a valued refinement
system and μ = μ_c + μ_p the Yosida-Hewitt decomposition of a
bounded charge.  For n i.i.d. samples from μ:

(a) The empirical estimator of μ_c converges at rate
    n^{−s/(2s+D_Λ)} where s is the Hölder regularity and
    D_Λ is the observational resolution dimension.

(b) The PFA component μ_p contributes a bias floor
    ||μ_p|| · f(k) where f(k) depends on the refinement level
    but not on n.

(c) The total estimation error is therefore
    max(n^{−s/(2s+D_Λ)}, ||μ_p|| · f(k)).

(d) The transition between the n-dependent regime and the
    k-dependent regime is detectable from the data (the
    rate-vs-resolution diagnostic).

This would make precise the sense in which the boundary is
"felt" operationally: statement (d) says you can detect *that*
you've hit a floor, even though you can't determine *why*
(PFA mass vs resolution limit vs misspecification).

**Status (2026-05-20):** VERIFIED ROUTINE.  Worked the problem:
the PFA structural constraint (finite-additivity across
resolutions) does NOT improve the minimax contamination floor.

Key argument: Kolmogorov extension theorem guarantees that the
restrictions of any PFA charge to finite subalgebras form a
projective system indistinguishable from σ-additive marginals.
At any finite collection of resolution levels, PFA contamination
looks exactly like contamination from some σ-additive measure.
No multi-resolution estimator can exploit the PFA structure.

This is the *mechanism* behind epistemic inaccessibility:
Kolmogorov extension is why the boundary can't be seen at
finite resolution.  Not just "hard to detect" — provably
indistinguishable at every finite stage.

The rate R*(n) ≍ n^{−2s/(2s+D_Λ)} ∨ ε² is correct, routine.

## Audit verdict (Phase 2): TAXONOMIC — PARK

- Rate formula: Liu-Gao (2019) instantiated on finite alphabets.
- D_Λ substitution: Yang-Barron (1999), Kpotufe (2011).
- Plateau detection: Lepski adaptive methods (1997).
- Epistemic inaccessibility: Łoś (1955), Espíndola (2019).
- Kill mechanism for "PFA structure helps": Kolmogorov extension.

The one new observation is that Kolmogorov extension is the
precise mechanism behind inaccessibility.  This is a remark,
not a theorem.  Added to §2.9 of the literature review.

Full working: `notes/unsorted/finite_sample/operational_boundary_theorem/theorem_spec.md`
