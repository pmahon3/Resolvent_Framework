# Audit correction to disintegration_diagnostic.md

**Date:** 2026-05-27
**Source:** Cross-reference from the MITACS applied-side programme
**Affects:** `disintegration_diagnostic.md` (PARKED 2026-05-26), Phase-2 audit table
**Status:** One audit-table row falsified; one survivable-novelty branch dead

---

## The correction

The Phase-2 audit table in `disintegration_diagnostic.md` lists:

| Component | Status | Reference |
|-----------|--------|-----------|
| ... | ... | ... |
| Patra–Sen conditional diagnostic | Not published | Genuinely absent |

and the closing section "What survives: applied guidance from the
literature" elevates this to "**the novel applied contribution
that survives the audit**":

> Nobody has applied the Patra–Sen (2016) two-component mixture
> estimator to *conditional* distributions as a σ-algebra adequacy
> diagnostic.

**This claim is false.** A second-pass MITACS-side literature scout
(2026-05-26) found:

**Deb, Saha, Guntuboyina, Sen (2022).** "Two-Component Mixture
Model in the Presence of Covariates." *Journal of the American
Statistical Association* **117**(540). arXiv:1810.07897 (2018).
R package `NPMLEmix` (CRAN, currently archived).

Decisive details:

1. **Same author chain.** Bodhisattva Sen co-authored both
   Patra–Sen (2016) AND Deb et al. (2022). The canonical
   covariate-dependent generalization is in JASA by the original
   estimator's author.

2. **Section 6 verbatim** addresses the σ-algebra adequacy
   question in the disintegration note's exact framing:
   *"A basic and important question that we have not yet
   addressed is: 'Do the covariates provide any information at
   all on the distribution of Y'? Put another way, we must first
   check that [the unconditional two-groups] model is inadequate.
   Only then does it make sense to model the dependence between
   Y and X."*

3. **Operational coverage.** Deb et al. provide the strictly
   more general joint NPMLE of π*(x), tuning-parameter-free, plus
   a formal adequacy test via distance covariance (Székely et al.
   2007). The "stratified Patra–Sen" the disintegration note
   proposed (per-stratum unconditional estimation of α̂_L(s) and
   visual inspection of variation) is a coarsened version of
   what Deb et al. already have.

4. **Earlier predecessor for chronology.** Scott et al. (2015
   JASA, FDRreg, arXiv:1307.3495) used the same idea with a
   parametric logistic link.

Full scout report (verbatim search, citations, verdict-with-
confidence):
`~/Research/Dynamics/MITACS/notes/literature/2026-05-26_stratified-patra-sen-scout.md`
(commit `8f0f3f3` on the MITACS-side `operator` branch).

## What's still novel (and what isn't)

- **Identifiability obstruction theorem** (Bergna et al. 2026
  Prop 1; Heckman–Singer 1984; Allahverdyan 2020;
  Andrews–Mallows 1974): unchanged. The disintegration note's
  core theoretical content remains correct and parked.
- **σ-algebra-adequacy vocabulary** as a unifying lens across
  Heckman–Singer / Bergna / Allahverdyan / Manski: unchanged,
  framing-only contribution noted as such in the original note.
- **Patra–Sen conditional diagnostic as the "one novel applied
  contribution surviving the audit"**: FALSIFIED. Deb et al.
  (2022) is the canonical method; further MITACS applied work
  in this direction would cite them, not invent.

## What this changes downstream

- The disintegration note's "park" verdict is unaffected
  (theorem contributions still known; framing still useful).
  The note doesn't need to be revived.
- The audit-table row should be updated to "Published (Deb,
  Saha, Guntuboyina, Sen 2022 JASA); supersedes 'genuinely
  absent' verdict."
- The "What survives" §(a) subsection ("Patra–Sen conditional
  extension (genuinely absent from lit)") should be revised or
  removed; the methods novelty it identified does not exist.
- MITACS-side: the new thread spawned after the
  distributional-class-thread closure (S9+S10 evidence for the
  obstruction) will use NPMLEmix (Deb et al. 2022) as
  established methodology, not invent. Sequence: NPMLEmix
  diagnostic → exogenous-Z testing informed by the diagnostic.

## Workflow lesson

The disintegration note's Phase-2 audit checked the obstruction
theorem against four traditions and found it published in all
four. The audit missed that the canonical author of the
proposed novelty contribution had already published the
covariate-dependent generalization six years prior, in the same
top venue (JASA). Single-author chain audit (forward citations
from Patra–Sen 2016 by Sen himself) would have caught it.
Worth adding to the literature-scout's standard checklist:
"check forward citations of the primary citation by every
listed co-author of the original."

---

Cross-references:
- MITACS Q1: `mitacs-q1-student-t-vs-gaussian` (S8)
- MITACS Q2A: `mitacs-q2a-richer-family` (S9, kernel-refinement lever bounded)
- MITACS Q2B: `mitacs-q2b-non-distributional` (S10, naive same-Q
  manipulations bounded; together with S9, applied evidence for
  the obstruction theorem identified by this disintegration note)
- MITACS scout: `2026-05-26_stratified-patra-sen-scout.md` (the
  full DONE BEFORE verdict)
