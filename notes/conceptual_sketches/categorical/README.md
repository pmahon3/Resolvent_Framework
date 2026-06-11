# Categorical reading of the programme — salvaged sketches

*Salvaged 2026-06-11 from the (now-deleted) `categorical-foundations` branch,
which forked 2026-03-18 and was never merged. This material PREDATES the OML
pivot — it frames the Boolean/distributive era of the programme (Paper I and the
Observable Dynamics Program) in category-theoretic language. It is not wrong or
superseded, but it is not on the current critical path. Kept as a conceptual
reference / route-finding sketch, not as live work.*

## Contents

- **`categorical_classical.tex`** — the classical construction of probability in
  categorical language (Meas, the Giry monad 𝒫, its Kleisli category of Markov
  kernels, projective limits, Kolmogorov extension). Sets up *where* the classical
  picture freely chooses a measure (Step 3).
- **`categorical_program.tex`** — the Observable Dynamics Program as the
  *diagram-first* inversion of the above: the measure is derived from the
  coherence of a system of marginals rather than freely chosen. Query systems as
  diagrams in Kl(𝒫).
- **`categorical_adjunction.tex`** — the cleanest result here: the Observational
  Extension Theorem of Paper I read as an **adjunction** `Ext ⊣ Forget : PSys ⇄
  QSys`. The categorical statement of Paper I. This is the piece most likely to
  matter if the categorical framing is ever revived.
- **`categorical_foundations.md`** — the original prose sketch, trimmed to its
  unique residue: the **phenomenological reading** of the inversion (Merleau-Ponty
  correspondence table) plus the open-problems-as-categorical-questions list. The
  formal Meas/Giry/Kleisli/extension development it once duplicated now lives in
  the `.tex` files; the `.md` carries a pointer map to them.
- **`mathlib_gaps.md`** — the **single source** for the Mathlib has/lacks audit
  (Giry monad ✓, Kleisli ✓, Markov kernels ✓; projective limits in Meas and
  Kolmogorov extension absent — formalization gaps, not mathematical ones). The
  `.tex` files' former Mathlib sections now point here.

*Condensed 2026-06-11 (section-level dedup, no content lost): Mathlib material
consolidated into `mathlib_gaps.md`; the duplicated adjunction proof in
`categorical_program.tex` replaced by a pointer to `categorical_adjunction.tex`
(its unique predictive-query / delay / Rose section kept); `categorical_foundations.md`
slimmed to its phenomenological residue. PDFs rebuilt to match.*

## Status / how to use

- **Dormant reference.** No claimed contribution type; not headed for a draft.
  Treat like an open-question note: re-engage only on new input (e.g. if the
  programme returns to the Boolean/distributive line, or if the Ext ⊣ Forget
  adjunction becomes relevant to a Paper I revision).
- The relevant live trunk question is the (a)/(b) fork (see
  `notes/programme/genealogy.md`). This directory is squarely (a)-side material
  (Boolean, no incompatibility) — if anything it is continuous with Strategy D /
  Paper I, not the descent axis.
