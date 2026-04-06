# arXiv Submission Prep

Strategy: post to arXiv first (permanent preprint ID, immediately citable), then
submit to journals simultaneously. arXiv does not claim exclusivity — standard
practice in mathematics.

---

## What is an MSC class?

MSC = Mathematics Subject Classification. A standard two-level taxonomy used by
journals and arXiv to categorise papers (e.g. `60A10` = Probability theory,
foundations). arXiv requires at least one primary MSC class per submission and
uses them to route papers to mailing lists. Pick from
https://mathscinet.ams.org/mathscinet/msc/msc2020.html

---

## Paper I — "Probability from Observation"

### arXiv category
Primary: `math.PR` (Probability)
Cross-list: `math.LO` (Logic; for the CE irreducibility / Łoś's theorem content)

### MSC 2020 (proposed)
- `60A10` — Probability theory, foundations (primary)
- `28A60` — Measures on Boolean rings, measure algebras
- `06E15` — Stone spaces (= Boolean spaces) and related structures
- `28A05` — Classes of sets, σ-algebras, measurable spaces

### Keywords (proposed)
observable extension theorem, collective exhaustion, Carathéodory extension,
Stone duality, Boolean algebra, finitely additive measure, σ-additivity,
directed system, query system

### Outstanding tasks
- [x] Fix stale `mahon_paper0` self-reference — removed from `references.bib` (2026-04-05)
- [x] Fix `cardona2025` bib entry format — changed to `@misc` with `howpublished` (2026-04-05)
- [x] Add MSC 2020 classifications and keywords — added as `\begin{quote}` block after abstract (2026-04-05)
- [x] `\pagecolor{white}` — already absent from `paper_i.tex`
- [x] Final compile check — clean (2026-04-05)
- [ ] Upload source files to arXiv

---

## Paper II — "Dynamics from Probability"

### arXiv category
Primary: `math.DS` (Dynamical Systems)
Cross-list: `math.FA` (Functional Analysis; for Koopman/semigroup content),
            `math.PR` (Probability; for predictive kernel content)

### MSC 2020 (proposed)
- `37A30` — Ergodic theory, spectral theory, ergodic theorems (primary)
- `47D06` — One-parameter semigroups and linear evolution equations
- `60J05` — Markov processes with discrete parameter
- `28A99` — Classical measure theory, other

### Keywords (proposed)
Koopman operator, predictive kernel, minimal predictive state, Markov semigroup,
Koopman–Perron duality, observable dynamical system, measure-preserving system,
Lean formalization

### Outstanding tasks
- [x] Add MSC 2020 classifications and keywords (2026-04-05)
- [x] Remove `\pagecolor{white}` (2026-04-05)
- [x] Add missing citations: Koopman1931, Rokhlin1952, Mathlib, mahon_paper1 (2026-04-05)
- [x] Final compile check — clean (2026-04-05)
- [ ] Update `mahon_paper1` in `references.bib` with arXiv ID once Paper I is posted
- [ ] Upload source files to arXiv

---

## Paper III — "Reconstruction from Observation"

### arXiv category
Primary: `math.DS` (Dynamical Systems)
Cross-list: `math.FA` (Functional Analysis; for density bridge / L² content),
            `math.PR` (Probability; for connection to Paper I measure content)

### MSC 2020
- `37A05` — Dynamical aspects of measure-preserving transformations (primary)
- `28A60` — Measures on Boolean rings, measure algebras
- `06E15` — Stone spaces and related structures
- `37A30` — Ergodic theory, spectral theory
- `46E30` — Spaces of measurable functions

### Keywords
reconstruction theorem, delay embedding, observable algebra, density bridge,
measure-theoretic Takens, Stone duality, Koopman operator, measure-preserving system,
Lean formalization

### Outstanding tasks
- [x] Add MSC 2020 classifications and keywords (2026-04-05)
- [x] Remove `\pagecolor{white}` (2026-04-05)
- [x] Final compile check — clean, 7 pages (2026-04-05)
- [ ] Add Paper III to `references.bib` in Papers I and II once arXiv ID known
- [ ] Upload source files to arXiv

---

## Suggested journal targets (post-arXiv)

| Paper | Primary target | Backup |
|-------|---------------|--------|
| I | *Journal of Theoretical Probability* | *Fundamenta Mathematicae* |
| II | *Ergodic Theory and Dynamical Systems* | *Journal of Functional Analysis* |
| III | *Ergodic Theory and Dynamical Systems* | *Nonlinearity* |

---

## arXiv upload checklist (both papers)

- [ ] Source files: `.tex`, `_body.tex`, `references.bib` (no `.pdf`, no `.aux` etc.)
- [ ] Confirm all figures/images included (none currently)
- [ ] Author name, affiliation, email set correctly in submission form
- [ ] Abstract copied from paper (arXiv has its own abstract field — paste from `.tex`)
- [ ] License: typically `CC BY 4.0` or arXiv default non-exclusive
- [ ] After upload: check compiled PDF on arXiv before announcing
