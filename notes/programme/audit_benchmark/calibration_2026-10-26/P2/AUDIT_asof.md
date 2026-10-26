## Audit: seed.md (mode: full) — audited as of 2023-02-09

Rules applied (AS_OF.md): only sources dated on or before 2023-02-09 count; the seed's own work, under any
title (it matches arXiv:2302.05537, which turned up in a search), is the submission and was ignored. One
undated point is flagged under Sources.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The seed declares types but does not state the bars it commits to clearing (framework, Phase 1
requirement). This is a minor readiness defect and does not block the audit.

### Pure Verdict: NOVEL (as of 2023-02-09)

**Stripped statement.** r_3(N) ≤ N·exp(-c(log N)^β) for some absolute β > 0. This is a quasi-polynomial
(Behrend-shape) upper bound for sets with no three-term AP.

**Hostile search. Closest prior statements:**
- Bloom–Sisask, "Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions",
  arXiv:2007.03528, v1 dated 2020-07-07 [abstract read]. Gives r_3(N) ≪ N/(log N)^{1+c}. This is the
  "previous best" bound the seed cites, and the seed's bound beats it by a lot: it is stronger than every
  power of log N.
- Schoen–Sisask, "Roth's theorem for four variables and additive structures in sums of sparse sets",
  arXiv:1408.2568, dated 2014-08-11 [abstract read]. **This is the most damaging prior source.** Its main
  theorem gives density exp(-c(log N)^{1/7}) for the four-variable equation x+y+z=3w, and it notes that
  1/7 cannot exceed 1/2 (Behrend). So the quasi-polynomial shape of the bound and the almost-periodicity
  route to it were known for the four-variable equation. The three-variable case x+z=2y is the one that
  stayed open.
- Behrend (1946) [not retrieved; standard]. The lower bound r_3(N) ≥ N·exp(-C√log N) shows the seed's
  shape is the right one, and it forces β ≤ 1/2.
- Finite-field side: Ellenberg–Gijswijt, arXiv:1605.09223, dated 2016-05-30 [abstract read], following
  Croot–Lev–Pach 2016. They bound 3-AP-free subsets of F_q^n by c^n, which beats Bateman–Katz
  O(3^n/n^{1+ε}). **So a finite-field bound alone would be KNOWN, and stronger.** What could be new in the
  seed's finite-field step is only an *analytic* (density-increment / Fourier-type) method that reaches a
  quasi-polynomial bound. The polynomial method does not transfer to Z, which is why that matters.
- Peluse, Bourbaki survey "Recent progress on bounds for sets with no three terms in arithmetic
  progression", arXiv:2206.10037, v1 dated 2022-06-20 [abstract only; v2 of 2023-09-25 ignored as
  post-date]. It surveys the state of the art up to June 2022 (Bloom–Sisask, CLP, EG). I could not confirm
  from the abstract whether it calls quasi-polynomial bounds open. Its framing is consistent with
  Bloom–Sisask being the frontier.

Searched for a quasi-polynomial bound for 3-APs in Z under the names "Behrend-type upper bound",
"quasipolynomial Roth" and "exp(-c(log N)^β) r_3(N)". I found no source on or before 2023-02-09 that
states one. It is not folklore, and it does not follow trivially: it is the long-standing open endpoint
the Erdős-conjecture literature is aimed at. Nothing in the pre-date literature shows that the
Schoen–Sisask four-variable method gives the three-variable case. Their own paper presents the
four-variable equation as the case the method reaches.

**Caveat.** The verdict assumes the proof is correct. Correctness is not checked here; that is a referee
task, and Phase 4 / Lean would be the check.

### Applied Verdict: not evaluated
No Type 7 claim, and the result is pure mathematics.

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): PASS.**
- The statement is not known and not folklore.
- It is a categorical improvement over Bloom–Sisask 2020: quasi-polynomial against a power of log.
- The proof cannot be routine, since 50+ years of density-increment work stalled at about 1/log N.
- Bar applied: not known, not folklore, not a trivial consequence, non-routine proof.
- Conditional on correctness.

**Type 3 (unifying framework): FAIL.**
- Bar: a conceptual structure that shows previously unrelated results to be one phenomenon, *and* enables
  method transfer.
- The seed does describe a method transfer: analytic techniques developed in F_q^n are then adapted to Z.
- But the "framework" here is the finite-field-model paradigm. That paradigm is owned (Green, "Finite
  field models in additive combinatorics", arXiv:math/0409420, dated 2004-09-22 [abstract read]) and is
  routine in the field (Meshulam → Roth; Bateman–Katz → Bloom–Sisask).
- F_q^n and {1..N} are not "previously unrelated" domains. The seed offers no new unifying structure,
  only an instance of a known pipeline.
- The transferable *technique* is real and valuable, but it belongs under Type 1 (or Type 2(a) if it is
  later reused). Type 3 is the wrong type for it.

**Undeclared type worth noting.** Type 2(a) would apply if the technique proves reusable, for example on
other translation-invariant equations or on corners. Here it is subsumed by Type 1. Not scored.

### Cross-reference
- The theorem itself clears Type 1.
- The Type 3 claim is a costume. The finite-field→integers transfer is the standard Green paradigm. The
  seed's own value is the technique and the bound, not a framework.
- **Most damaging prior source:** Schoen–Sisask 2014, main theorem: exp(-c(log N)^{1/7}) for x+y+z=3w.
  It owns the bound's *shape* and the almost-periodicity approach for four variables. It does not own the
  three-variable statement.
- Ellenberg–Gijswijt 2016 owns the finite-field *bound*: any finite-field result in the seed must be sold
  on its method, not its numbers.

### Recommendation
- **Proceed to Phase 3, scoped to Type 1 only. Drop Type 3.**
- The problem statement should:
  - make the Schoen–Sisask comparison explicit: what fails for three variables, and what the new step is;
  - state the finite-field result as a *method* result relative to CLP/EG;
  - state the explicit β.
- Correctness verification is owed before any claim is made.
- WHY.md line: weak bearing. This is a single-world counting question with no local-to-global gluing; at
  most it is a lens on the "hidden idealisation" question (structure against randomness).

### Sources (all on or before 2023-02-09 unless noted)
- Bloom–Sisask, arXiv:2007.03528, v1 2020-07-07 — abstract read (v2 2021-09-01).
- Schoen–Sisask, arXiv:1408.2568, 2014-08-11 — abstract read.
- Ellenberg–Gijswijt, arXiv:1605.09223, 2016-05-30 — abstract read.
- Green, arXiv:math/0409420, 2004-09-22 — abstract read.
- Peluse, arXiv:2206.10037, v1 2022-06-20 — abstract only. Later v2 (2023-09-25) excluded, and I could not
  tell which of its content was already in v1.
- Behrend 1946; Bateman–Katz (J. AMS 2012); Croot–Lev–Pach (Annals 2017, arXiv 2016) — not retrieved this
  run, cited from standard knowledge. All three clearly predate the audit date.
- Excluded as the submission itself: arXiv:2302.05537. Later improvements (for example, a later exponent
  improvement) were also ignored.
