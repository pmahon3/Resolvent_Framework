# Paper I audit verdict — "When Does Observational Coherence Determine Probability?" (2026-06-23)

Two-pronged hostile audit (proof-correctness + cross-field prior-art), modeled on
the sweep that retired the companion note. **Overall: REVISE-DOWN / PARK THE
NOVELTY CLAIMS.** One fatal proof error in the headline contribution + the
contribution pieces are folklore. Consistent with the programme's own
self-understanding (CLAUDE.md: Paper I is synthesis/positioning, Paper II is the
novelty zone) — this is not a new collapse, it confirms the existing read.

## Prong 1 — proof correctness

### FATAL: Prop "Support condition" (`I:prop:B2`, line ~550), and everything downstream
The proof shows `pure(Ω) ⊆ Σ` (Σ = σ-complete/countably-closed ultrafilters of the
cylinder algebra C) and `μ̂(Σ)=1`, then concludes `μ̂(pure(Ω))=1`. **The missing
step is `μ̂(Σ \ pure(Ω)) = 0`** — that non-principal σ-complete ultrafilters carry
no mass. The proof contains NO sentence bounding mass on `Σ \ pure(Ω)`. And
`Σ \ pure(Ω) = ∅` is exactly "every σ-complete ultrafilter is realized by a point
of Ω" = the **σ-Loomis–Sikorski realization problem** — the SAME abstract-vs-concrete
gap that killed the companion note, and the recurring σ-LS wall in the OML thread.
Discriminability only separates *existing* points (makes `pure` injective); it does
NOT realize σ-complete ultrafilters. Surjective Evaluation / common coarsenings
don't touch it. Independent second crack: the "vanishes on meagre ⟹ full mass on
Σ" step needs `St(C) \ Σ` measurable/null, which over an uncountable index is an
uncontrolled uncountable union of meagre sets — a countability the proof never
invokes.

**Inherited FATAL:** `I:thm:stone-main` (uses `μ̂(pure(Ω))=1` as load-bearing
input) and the headline **Corollary `I:cor:stone-support`** ("σ-additivity ⟺
`μ̂(pure(Ω))=1`") — the paper's central novel claim — do not stand. The **abstract**
asserts this same unproved step ("Under discriminability, σ-additivity is
equivalent to concentration of this measure on the principal ultrafilters").

### THE VISE (why this is not repairable-as-novel)
The auditor's fix (ι countable + O_i standard Borel) makes B2 TRUE — but under
exactly those hypotheses the Stone route **reproduces Kolmogorov / Bochner–Prokhorov**.
So: general regime → B2 false (realization gap) → broken; realizable regime → B2
true → result is Kolmogorov, novelty gone. **No regime is both correct and novel.**
The headline contribution IS the broken step, broken precisely because that's where
it tried to exceed the folklore. Do NOT "fix the proof while keeping the beyond-Kolmogorov
framing" — that repeats the note's Route-A relabeling error.

### FINE / minor
- `I:thm:sp1` (CE Characterisation): correct but a tautology by the paper's OWN
  remark (compatibility makes CE's ∃-quantifier vacuous ⟹ CE ≡ continuity-at-∅ ≡
  σ-additivity of ℓ_i). No abstract-σ trap here — the E_i are concrete cylinder
  *fields* of sets, so Halmos extension applies cleanly. Over-billed as a Theorem.
- `I:thm:main` (i)–(iii): FINE (intrinsic to charges; Yosida–Hewitt).
- `I:prop:invlim` (Choksi): FIXABLE-GAP — Choksi 1958 Thm 1 hypotheses
  (Radon/regularity/non-emptiness) invoked unverified; result independently true via
  an elementary compact-Stone premeasure argument (clopens compact ⟹ premeasure free
  ⟹ Carathéodory). Replace or state hypotheses. Low severity.

## Prong 2 — cross-field prior-art / novelty

| Piece | Status | Owner |
|---|---|---|
| f.a. charge → σ-add Radon on Stone space | OWNED | Lacy 1974 Ch.5 Thm 3; Bhaskara Rao 1983 (paper's OWN cite); Cardona et al. arXiv:2503.08910; de Finetti-for-undergrads arXiv:2107.00250 |
| σ-add ⟺ concentrates on principal ultrafilters | OWNED | extension thm + Yosida–Hewitt; multiple sources |
| YH purely-f.a. part = mass on free ultrafilters | OWNED | Yosida–Hewitt 1952 + Stone duality, standard |
| compatible marginals → cylinder/Stone measure | OWNED | Kolmogorov 1933, Choksi 1958, Mallory–Sion 1971 |
| σ-additivity as Prokhorov/descent condition | OWNED | Prokhorov, classical |
| CE as new vocabulary | TERM NEW, SUBSTANCE NOT | self-collapses to continuity-at-∅ (Halmos); three-statements test FAILS |
| "geometric commitment" framing for phil audience | packaging novel, thin | no single owner; but de Finetti coherentism already has the negative result |

**`rao1983` is the paper's own citation AND the standard reference for the
dichotomy** — exact analog of FHM-was-its-own-reference in the note. The paper
cites rao1983 Thm 10.5.3 inside the broken B2 proof for the σ-additivity
characterization it's reaching for.

## Contribution-type bars
- **Type 1 (theorem):** FAIL — pieces owned (Lacy/Bhaskara Rao/Choksi/Mallory–Sion);
  the one original theorem (Corollary) is broken.
- **Type 2 (proof):** FAIL — no new technique; the novel step is wrong.
- **Type 4 (vocabulary CE):** FAIL — CE ≡ continuity-at-∅ by the paper's own remark;
  three-statements test fails.
- **Type 6 (exposition):** the only survivor, and THIN — gated on whether the
  "geometric commitment" Stone-reading is genuinely inaccessible to the
  philosophy-of-probability audience (which already knows coherence ≠ σ-additivity,
  de Finetti). rao1983 likely already does most of the unifying work.

## Required actions (non-negotiable, independent of positioning)
1. **Pull or restate the abstract sentence** "Under discriminability, σ-additivity
   is equivalent to concentration … on the principal ultrafilters" — it is a
   false-as-written theorem in the abstract. Make conditional-on-realization or cut.
2. **Pull Corollary `I:cor:stone-support` and the Stone-main descent** as stated, or
   add explicit realization hypotheses (ι countable + standard Borel) AND
   simultaneously downgrade the novelty framing to "recovers Kolmogorov via Stone
   duality," not "beyond Kolmogorov."
3. Demote CE Characterisation to a Proposition/Remark; state its tautological nature.
4. Choksi: verify or replace with the compact-Stone premeasure argument.

## Net
Park the novelty claims. If kept at all, reduce to an honest short **exposition**
(Type 6) of the Stone-duality reading for a named philosophy-of-probability
audience — NOT a theorem paper, and only if a rao1983 read confirms the framing
isn't already there. The σ-LS realization gap is the real wall, same as everywhere
else in the programme.
