# Reading directions — skilling up to attempt the σ-essential problem

*Written 2026-06-27. A sequenced, audit-structured study plan for the σ-essential
contextual-state problem, written for the **foundations-first / path-agnostic** choice:
build the common substrate (descriptive set theory + large cardinals + the OML σ-state
corner) until the primary sources read fluently and the tractable edge reveals itself.
Each phase carries **target-questions** tied to a specific file/§ in the investigation —
the study has the same verify-against-a-question structure as the research. The driver is
"learn and try"; the only real constraints are the theorems already proved
(forcing-wrong-engine, masa-free-dead), not background.*

---

## The object, stripped to what a solver must touch

> A concrete σ-complete non-Boolean irreducible OML carrying a finite 2-valued state on
> a ⊥-closed subposet that extends to **no** global σ-additive 2-valued state.

Localized (`sigma_essential_reduction_writeup.md`): this is **σ-point-selection failure**
(wall A) — a locally coherent 2-valued pattern across overlapping incompatible blocks with
no global σ-additive 2-valued state. The frontier is **non-Polish / non-standard-Borel /
irreducibly non-central**, strength **genuinely unknown** (`bounds §3f`), and **no
borrowable principle exists in any surveyed field** (`bounds §3h–3j`). Resolution needs a
genuinely new object — built, not transported.

The skill list is therefore *not* generic "learn set theory." It is targeted at the three
things a witness-construction OR an independence proof would demand, in dependency order.

**The asymmetry (the whole reason for the ordering):** you already own the OML / quantum-logic
cluster (CLAUDE.md). The gaps are descriptive set theory and large cardinals. The plan
front-loads those and treats the OML sources as practitioner-level re-reads.

---

## Phase 0 — the bridge you almost crossed (free, ~1–2 weeks)

Before any new book, nail the **definability-vs-existence** distinction cold. It is the
error *type* that killed the CBER bridge and it will recur at every DST contact.

- **Read:** your own `bounds §3f` (LB-mechanism refutation) and `§3j` (CBER kill) with one
  lens — *"no Borel selector" (a definability fact) vs "no state at all" (an existence
  fact).*
- **Target-question (must answer without notes):** *Why can a ZFC theorem (E₀, E∞
  non-smooth) neither force nor refute clause (ii)?* If the answer ("clause (ii)-failure is
  ≥ measurable strength; a ZFC fact is silent on measurable-strength statements; a
  definability obstruction cannot yield an existence obstruction") is fluent, you have the
  load-bearing intuition. The Lean polarity gate certifies this shape — read it too
  (`SigmaEssentialConjectures.lean`, `builds_state_implies_not_witness`).

---

## Phase 1 — Descriptive set theory (the witness's home regime, ~2–3 months)

The frontier *is* the non-standard-Borel regime; Glimm–Effros is *your* dichotomy one
abstraction level over; the whole DST sweep (`§3h`) lives here.

### Kechris, *Classical Descriptive Set Theory* (GTM 156)
Read by dependency, not linearly:
- **Ch. 11–14** — Borel / analytic / co-analytic hierarchy → **Borel equivalence relations**
  → the **Glimm–Effros dichotomy**.
  - *Target-Q:* state Glimm–Effros precisely ("a CBER is non-smooth ⟺ E₀ embeds ⟺ no Borel
    2-valued transversal"). Then: *which word in it is the one that does NOT transport to
    clause (ii)?* (Answer in `§3j`: "Borel.") This closes the CBER lead with understanding,
    not just on the advisor's say-so.
- **Ch. 16–18** — uniformization, the projective hierarchy.
  - *Target-Q:* co-analytic uniformization-failure was DST-corner #1 (`§3h`). *Why is its
    obstruction real-valued / over a standard-Borel base — i.e. why is it DW-killed?*

### Gao, *Invariant Descriptive Set Theory*
Read **after** Kechris supplies the language. This is the E₀/E∞/hyperfinite/turbulence book
in one place.
- *Target-Q:* define hyperfinite; state Adams–Kechris (uncountably many non-Borel-bireducible
  CBERs). Then the one that matters: *why is E∞ being non-hyperfinite ORTHOGONAL to clause
  (ii)?* (`§3j`: non-hyperfiniteness buys more non-smoothness; non-smoothness is exactly
  what's orthogonal to an existence obstruction.) When this is obvious, the DST corner is
  genuinely closed for you.

---

## Phase 2 — Large cardinals + forcing (the strength axis, ~2–3 months)

Your bare object on the Boolean shadow *is* a measurable cardinal (`rem:not-measurable`);
the open strength question is whether non-distributivity pushes above or below it
(`§3f, §3i`).

### Jech, *Set Theory* (3rd millennium ed.)
- **Ch. 8** — filters, ideals, ultrafilters. The substrate for everything below.
  - *Target-Q:* why is `ℱ_s = {A : s(A)=1}` NOT a filter on a non-Boolean concrete OML, even
    for a Dirac state? (`§3a`, the MO₂ unit test: `a∩b≠∅` as sets yet `a∧b=0` lattice-wise.)
    This is *your* carrier's defect stated in filter language.
- **Ch. 10** — measurable cardinals; **Ulam matrices**.
  - *Target-Q:* re-derive the Ulam matrix argument by hand (you started this in `§3b`).
    Locate the exact line where the construction needs **non-orthogonal unions /
    comprehension** — that line is why the matrix argument doesn't transplant to an
    orthogonal-join-only OML.
- **Ch. 14–15** — forcing, specifically to *feel* **Lévy–Solovay**.
  - *Target-Q:* why does set-forcing preserve measurability (can't create or destroy it
    by small forcing)? This is *why forcing is the wrong engine* for the existence
    direction (`forcing_programme_status.md`) — you need the mechanism, not the citation.

### Kanamori, *The Higher Infinite* (second pass, only if the strength path calls)
Ch. 1–2 (measurable → ultrapower → elementary embedding `j: V→M`, crit pt κ). Only after
Jech. *Target-Q:* the UB route would "transport `U` along `j`" — `§3b` flagged this as
costume #8 (the measurable gives `U` on **Boolean** P(κ); transport to orthogonal-only =
the disjointification wall from the construction side). Understand why that's a costume.

---

## Phase 3 — your own primary sources, read as a practitioner (~1–2 months, interleaved)

By now you read these for **technique**, not verdict.

- **Navara–Pták 1983** (`navara_ptak_1983_byhand_read.md`) — re-derive their ZFC non-Dirac
  σ-state construction. This is your **existence-proof template** and the object that
  refuted the LB mechanism. *Target-Q:* what makes their carrier `L_{f,g}` support a
  non-Dirac global σ-state — and why is it NOT a witness (the two compatible observables /
  "Boolean enough" point, `rem:np-builds-rescuer`)?
- **Derr–Williamson 2023 + Maharam 1972 §8** (`sigma_essential_prior_art_verdict.md`) — the
  Polish upper boundary. *Target-Q:* exactly where is inner-regularity load-bearing in
  Thm D.6 / Maharam §8.2? (This is the boundary a witness must escape.)
- **Blecher–Weaver 2017** (`bounds §3, §3a`) — the Hilbert analogue that does NOT transfer.
  *Target-Q:* identify the ultrafilter-extraction-from-a-masa step (Prop 2.3); state the
  **masa-free question** (§3a) it leaves open for the concrete 2-valued case.

---

## Where to start today

**Kechris Ch. 12–14 (Borel equivalence relations → Glimm–Effros), paired with the Phase-0
re-read.** Rationale: it is the single chapter that makes your own frontier-map legible AND
is the most reusable across all three resolution paths. After ~a month you will feel whether
to lean DST-construction or strength-axis — that is the path-agnostic plan working as
intended.

## Honest constraints (the only real ones)

- **Theorems, not background.** Forcing-wrong-engine (Lévy–Solovay) and masa-free-dead (§3a)
  are *proved* dead ends — respect those. Everything else is learn-and-try; there is no
  ceiling.
- **The convergence is the finding so far.** This plan is for *attempting* the open object,
  not re-litigating the closed literature frontier. If a phase surfaces a borrowable
  principle the sweep missed, that is a real result — but expect to *build*, not find.

*Companion: [[oml_lead_philosophical_reading]] (the question's phenomenological framing);
`sigma_essential_taxonomy.json` (zoom-out attempt index);
`sigma_essential_large_cardinal_bounds.md` (the bounds + every §ref above).*
