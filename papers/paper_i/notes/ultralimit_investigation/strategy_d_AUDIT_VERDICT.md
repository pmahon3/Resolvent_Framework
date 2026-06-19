# Strategy D resolution — HOSTILE-REFEREE AUDIT VERDICT (2026-06-18)

**Target audited:** the claim in `argyros_sigma_completeness_RESOLVED.md` that
`Clop(Y,𝔗)` (Argyros 1983 pre-Gleason algebra) is a *novel* ZFC example of a
non-σ-complete + atomless + measure-free Boolean algebra ("Strategy D").

## One-line verdict: KNOWN-OR-FOLKLORE-KILL.

The combination is folklore; the only hard ingredient is Argyros's published
theorem; and a strictly stronger ZFC witness predates it by **19 years
(Gaifman 1964)**. Clears no contribution-type bar.

## Per-type

- **Type 1 (new theorem): FAIL.** Content = [Argyros 1983 measure-freeness,
  published & hard] + [non-σ-complete + atomless, conceded trivial]. A
  hard-published-theorem plus a trivium is folklore. Moreover the *combination*
  itself is already realized in ZFC by Gaifman 1964 (below) — strictly stronger.
- **Type 2 (new proof): FAIL by the author's own admission.** The gap-family-at-`0̄`
  argument is conceded "essentially inherited from the usual Cantor space" and "the
  difficulty was overestimated." No new technique, no simplification of anything hard.
- **Type 5 (impossibility/sharpening): FAIL.** "Strategy D" is this programme's
  *private* name. The dossier's own lit review found nobody states the combination
  as an open problem (Plebanek 2024 survey doesn't discuss it; etc.). The
  "likely ZFC-independent" belief was a *local mis-estimate*, traceable to a
  systematic reading error in the near-miss table (σ-completeness read off the
  **completion / Gleason cover**, not the base algebra). Correcting one's own
  misreading is not closing a field-recognized open problem.
- **Type 6 (exposition): FAIL.** Pieces are published; the assembly is
  conceded-trivial; named audience + inaccessible-literature bar not met. Per the
  programme's "park honestly / don't rescue with framing" rule, no exposition rescue.

## Single most damaging finding (the unifying diagnosis)

**Gaifman 1964, PJM 14(1):61–73, Theorem 2.2 + property (†)** already exhibits, in
ZFC, an atomless Boolean algebra `𝔄` admitting **no strictly positive
finitely-additive measure** — strictly stronger than Strategy D's "no σ-additive"
leg. Verified from the primary source (pages read directly):

- **Atomless:** property (†) says *every* nonzero relativization `𝔄|ₐ` has no
  strictly positive measure. If `a` were an atom, `𝔄|ₐ ≅ {0,1}` carries the point
  mass `m(a)=1` — contradicting (†). So **(†) ⟹ atomless**. (p. 67, Thm 2.2.)
- **Measure-free (stronger sense):** Gaifman's "measure" = *finitely additive*
  (Introduction, p. 61). No strictly positive f.a. measure ⟹ a fortiori no
  strictly positive σ-additive measure. This out-strengthens the Argyros route,
  whose hard theorem only delivers no σ-additive (Radon) measure.
- **Non-σ-complete (trivial leg):** Gaifman's Thm 2.1/2.2 algebra is a quotient of
  the *free* BA on continuum generators; it is **not complete** — Gaifman himself
  takes its *completion by cuts* in §3 (p. 68) precisely because the base is not
  complete. As the author concedes for the Argyros base, this leg is the trivial
  one. (NB: "not complete" is what the source states verbatim; "not σ-complete"
  for the Gaifman base is the same conceded-trivial finitary fact, not a theorem to
  lean on.)

**Why the combination "looked" unexplored — the mirage explained.** The literature
systematically records these algebras in their **completed** form (extremally /
basically disconnected = the complete, measure-theoretically interesting object):
Comfort–Negrepontis 6.23 presents *Gaifman's* example as extremally disconnected;
C–N 6.25 does the same for *Argyros*. The non-σ-complete **base** is trivially
non-σ-complete, so nobody bothers to write it down. Its absence from the literature
is a non-result, not a gap. The dossier's near-miss table inherited exactly this
artifact — marking both Gaifman and Argyros "σ-complete" by reading the
completion/Gleason presentation — which manufactured the illusion that the
non-σ-complete row was empty.

## Citations found (primary-source verified)

- **Gaifman 1964**, "Concerning measures on Boolean algebras," PJM 14(1):61–73.
  Thm 2.1 (free-BA quotient `B/ℑ`, satisfies (∗), no strictly positive f.a.
  measure); Thm 2.2 + property (†) (atomless version); §3 p. 68 (completion by
  cuts → complete BA, no strictly positive σ-additive measure). **The clean ZFC
  witness of the full combination, 19 years prior.**
- **Argyros 1983**, PJM 105(2):257–272. The genuinely hard ingredient
  (measure-freeness via property (**) failure). Unchallenged; only confirms that
  the sole non-trivial content is borrowed.
- **Comfort–Negrepontis 1982**, *Chain Conditions in Topology*, Ch. 6: Thm 6.23
  (Gaifman, extremally disconnected = completion), Thm 6.25 (Argyros, Gleason
  cover). These are the *completed* objects — the source of the near-miss-table
  misreading.

## What survives

At most a one-line citation note, NOT a contribution: Gaifman 1964 Thm 2.2 + (†)
is the ZFC atomless / no-strictly-positive-(finitely-additive)-measure object that
already inhabits the "Strategy D" cell, predating and out-strengthening the Argyros
route on the measure leg. Strategy D should be retired as a research target: it was
never field-open, and it is inhabited in ZFC by a 1964 construction.

## Correctness notes (not load-bearing for the verdict)

- The gap-family proof in `..._RESOLVED.md` may well be correct; correctness does
  not rescue novelty (author concedes triviality). Not re-verified in depth.
- Do NOT assert "quotients of free BAs are not σ-complete" as a theorem — it isn't
  one. The Gaifman base's non-σ-completeness is the same conceded-trivial finitary
  fact as the Argyros base's, not an independent structural result.
