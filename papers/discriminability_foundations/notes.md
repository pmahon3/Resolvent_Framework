# Discriminability Foundations (Paper −1) — Working Notes

**Status:** Complete draft (2026-03-21). Resting before SP1 resolution.
**Branch:** `paper-minus-one`

---

## Paper status

The paper has been through a full narrative flip: it no longer frames
itself as a preliminary to Papers 0–4 but stands alone as the
foundation from which the program's shape is explained.

Major elements in place:
- §1: Introduction — primitive question, not program gap
- §2: Observable distinctions and the query framework
- §3: The negative result — finitary coherence alone cannot force σ-additivity
- §4: The open question — witnessing conjecture (SP1b)
- §5: The positive result — witnessing from above (proof sketch / conjecture)
- §6: Relation to existing literature (Daniell-Stone, de Finetti, constitutive outside)
- Two `aside` environments (mdframed, clearly labelled as provisional scaffold):
  - Constitutive outside (Derrida/Laclau framing)
  - Tetralemma / Nāgārjuna mapping onto the paper's four-cornered argument

---

## The core stopping point (SP1 / witnessing conjecture)

**Witnessing conjecture (Theorem B in old notes):** Under sequential
upper-directedness, the refinement structure witnesses emptiness from
above, and compatibility propagates that witnessing back down to force
continuity at ∅ at every finite level.

This is the main open mathematical question. The paper currently states
it as a conjecture with a proof sketch. Resolving it is the primary task
before Paper −1 can be submitted.

---

## Philosophical scaffold (to be deposited separately)

The two `aside` environments are explicitly marked as provisional.
Once the witnessing conjecture is proved, the mathematical argument
should stand alone. The scaffold is preserved here for a future
philosophy paper.

Key references for that paper:
- Derrida (1967) *Of Grammatology* — constitutive outside
- Laclau (1990) *New Reflections on the Revolution of Our Time*
- Nāgārjuna / Garfield (1995) *Fundamental Wisdom of the Middle Way*
- Priest (2010) "The Logic of the Catuskoti"

---

## Relation to existing literature (settled)

- **Daniell-Stone theorem:** Our "continuity at ∅" is the standard
  σ-continuity condition. Paper −1 is in this tradition.
- **de Finetti:** Our observable law is a finitely-additive probability
  space in de Finetti's sense. We derive σ-additivity structurally
  (via witnessing) rather than assuming it.
- **Seidenfeld-Schervish (1983):** Precedent for structural forcing of
  σ-additivity from coherence constraints.

---

## Open questions (for the return to SP1)

1. Make "nontrivial refinement" precise for Theorem A (necessity of
   incompleteness). Minimal condition on the query system that forces
   $\mathcal{E}_Q \subsetneq \sigma(\mathcal{E}_Q)$.

2. Precise statement of the witnessing conjecture. Is sequential
   upper-directedness exactly the right colimit condition?

3. Relationship to Boolean algebra / Stone space theory. The Stone space
   of $\sigma(\mathcal{E})$ as closure of the Stone space of $\mathcal{E}$
   may be the right lens.

4. Is sequential upper-directedness *equivalent* to the witnessing
   condition, making SP1 a theorem of the existing framework?
