# arXiv Submission Prep

Strategy: post to arXiv first (permanent preprint ID, immediately citable), then
submit to journals simultaneously. arXiv does not claim exclusivity — standard
practice in mathematics.

---

## Honest status as of 2026-04-24

**Companion note** — ready. Standalone logic paper, 3 pages, polished.
Waiting on arXiv math.LO endorsement (email sent to Halpern).

**Paper I** — ready. 12 pages, all routes proved, CE irreducibility established,
prose and structure at submission quality. Blocked only by endorsement.

**Papers II and III** — editorially polished and combined as of 2026-04-24.
Papers II and III are: Paper II = 7-page combined dynamics+reconstruction paper
(`papers/paper_ii/`); Paper III = 16 pages with Lemma 5.10 (Positive-fraction
balance) and citations using `mahon_paper2`. Cross-reference bib entries
(mahon_paper1, mahon_paper2) need updating with arXiv IDs once Paper I is live —
that is the only remaining mechanical task before Papers II and III can be submitted.

---

## Submission phases (revised)

**Phase 0 (current):** Obtain arXiv endorsement for math.LO.
- Email sent to Halpern (FaginHalpernMegiddo1990).
- Fallback: Plebanek, Džamonja, Cardona et al.

**Phase 1 (on endorsement):** Upload companion note → get arXiv ID → update
`MahonCE2026` in `references.bib` → upload Paper I.

**Phase 2:** Update cross-reference bib entries in Papers II and III with arXiv IDs
from Phase 1 (`mahon_paper1` → actual arXiv ID). Then submit Paper II and Paper III
to arXiv in sequence. No other editorial work needed — both are polished.

---

## What is an MSC class?

MSC = Mathematics Subject Classification. A standard two-level taxonomy used by
journals and arXiv to categorise papers (e.g. `60A10` = Probability theory,
foundations). arXiv requires at least one primary MSC class per submission and
uses them to route papers to mailing lists.

---

## Companion note — "Countable Additivity is Not First-Order"

### File
`papers/paper_i/notes/countable_additivity_not_first_order.tex`

### arXiv category
Primary: `math.LO` (Logic)

### MSC 2020
- `03C20` (primary) — Ultraproducts and related constructions
- `28A60` (secondary) — Measures on Boolean rings, measure algebras
- `60A10` (secondary) — Probability theory, foundations

### Keywords
countable additivity, first-order axiomatizability, ultraproduct,
Boolean algebra, finitely additive measure, Łoś's theorem

### Status
- [x] MSC and keywords added
- [x] CE section removed (standalone logic paper, no Paper I dependency)
- [x] Abstract updated
- [x] Stronger question in display block (italic), open case stated inline
- [x] Compiles clean, 3 pages
- [ ] Obtain math.LO endorsement
- [ ] Upload to arXiv

---

## Paper I — "Probability from Observation"

### File
`papers/paper_i/probability_from_observation.tex`

### arXiv category
Primary: `math.PR` (Probability)
Cross-list: `math.LO` (Logic; for the CE irreducibility / Łoś's theorem content)

### MSC 2020
- `60A10` — Probability theory, foundations (primary)
- `28A60` — Measures on Boolean rings, measure algebras
- `06E15` — Stone spaces (= Boolean spaces) and related structures
- `28A05` — Classes of sets, σ-algebras, measurable spaces

### Keywords
observable extension theorem, collective exhaustion, Carathéodory extension,
Stone duality, Boolean algebra, finitely additive measure, σ-additivity,
directed system, query system

### Status
- [x] MSC 2020 classifications and keywords added
- [x] CE non-derivability remark with metatheorem scope added (§4)
- [x] Bridge §6 synthesis paragraph added (coherence/completion/admissibility triad)
- [x] Closing phrase neutralised ("The realised instantiation sits inside...")
- [x] Final compile: clean, 12 pages
- [ ] Update `MahonCE2026` bib entry with companion note arXiv ID (after Phase 1 upload)
- [ ] Upload to arXiv (after companion note upload)

---

## Papers II and III — deferred pending Phase 2

These papers are not tracked at the task level here until Phase 2 begins.
For reference, the proposed arXiv categories and MSC classes are recorded below
but should be treated as provisional.

### Paper II — "Dynamics and Reconstruction from Observation"
File: `papers/paper_ii/dynamics_and_reconstruction.tex` (7 pages)
arXiv: `math.DS` primary; cross-list `math.FA`, `math.PR`
MSC: `37A30` (primary); `47D06`, `60J05`, `37A05`, `28A60`, `06E15`, `46E30`

### Paper III — "Finite-Sample Reconstruction: Rates, Witnesses, and the Honest Bridge"
File: `papers/paper_iii/finite_sample_reconstruction.tex` (16 pages)
arXiv: `math.ST` primary; cross-list `math.DS`, `math.PR`
MSC: `62G08` (primary); `37A05`, `62M10`, `28A60`, `94A17`

---

## Suggested journal targets (post-arXiv, provisional)

| Paper | Primary target | Backup |
|-------|---------------|--------|
| Companion note | *APAL* (Annals of Pure and Applied Logic) | *MLQ*, *NDJFL* |
| I | *Proceedings of the London Mathematical Society* | *Journal of Theoretical Probability* |
| II-III | *Ergodic Theory and Dynamical Systems* | *Journal of Functional Analysis* |
| IV | *Annals of Statistics* | *Bernoulli* |

---

## arXiv upload checklist (Phase 1)

- [ ] Companion note: source `.tex` + `references.bib`, no PDF, no aux
- [ ] Paper I: `probability_from_observation.tex` + `probability_from_observation_body.tex` + `references.bib`
- [ ] Confirm no figures/images to include (none currently)
- [ ] Author name, affiliation, email set correctly in submission form
- [ ] Abstract copied from paper into arXiv abstract field
- [ ] License: CC BY 4.0
- [ ] After upload: check compiled PDF on arXiv before announcing
- [ ] After companion note ID received: update `MahonCE2026` in `references.bib`
- [ ] After Paper I ID received: update `mahon_paper1` in downstream refs (Papers II and III)
