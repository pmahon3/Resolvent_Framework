# Discriminability Foundations (Paper −1) — Working Notes
**Status:** SP1 resolved (2026-03-22). Paper updated. One proof to tighten before submission.
**Branch:** `paper-minus-one`

---

## Paper status

The paper is substantially complete. §§1–4 and §6 are in good shape. §5 has been
rewritten to replace the old witnessing conjecture with the SP1 theorem. The abstract
and introduction have been updated accordingly.

Current section structure:
- §1: Introduction — primitive question, not program gap. Three results stated.
- §2: Observable distinctions and the query framework
- §3: The negative result — finitary coherence alone cannot force σ-additivity
- §4: The necessity of incompleteness (see note below)
- §5: The SP1 resolution — independence prop + collective exhaustion def + SP1 theorem
- §6: Foundational conclusions — σ-algebra as commitment, SUD as faith, completed chain

Two `aside` environments remain (mdframed):
- §1: Constitutive outside (Derrida/Laclau) — still provisional, appropriate for a
  philosophy paper. The tetralemma aside (§4) has been updated: C1 now proved false,
  C4 closed by SP1 theorem.
- §5: Ω as regulative ideal — updated to correctly attribute SUD to SP2, not SP1.

---

## One remaining proof to tighten (§4, Theorem 4.2)

Theorem 4.2 (discriminability requires incompleteness) has an informal proof with a
gap at the key step: "the sequence of such distinctions generates events in σ(E_Q)
that are not in E_Q" is asserted rather than constructed. A rigorous proof requires
constructing a specific event in σ(E_Q) \ E_Q from the nontrivial refinement data.

This is not affected by the SP1 work and predates it. The likeliest route: assume
singleton measurability at each level, then any two points x, y with π(x) = π(y) but
x ≠ y in E_{Q'} give {x} ∈ E_{Q'} with π({x}) ∈ E_Q but {x} itself not separable
by anything in E_Q. The connection to Stone space theory (σ(E_Q) as the σ-closure
of E_Q) is likely the right lens.

Decision needed before executing the fix: whether to add singleton measurability as a
standing assumption in §2, or to reformulate Theorem 4.2 with an explicit hypothesis.

---

## Philosophical scaffold

The asides are explicitly marked as provisional. The mathematics now stands alone.
References for the future philosophy paper:
- Derrida (1967) *Of Grammatology* — constitutive outside
- Laclau (1990) *New Reflections on the Revolution of Our Time*
- Nāgārjuna / Garfield (1995) *Fundamental Wisdom of the Middle Way*
- Priest (2010) "The Logic of the Catuskoti"

---

## Relation to existing literature (settled)

- **Daniell-Stone:** Our "continuity at ∅" is σ-continuity in the Daniell-Stone sense.
- **de Finetti:** SP1 theorem settles de Finetti's question at the system level:
  σ-additivity is equivalent to collective exhaustion, neither derivable from finitary
  conditions nor a raw axiom.
- **Seidenfeld-Schervish (1983):** Precedent for structural forcing of σ-additivity.

---

## Open questions post-SP1

1. **SP2 connection.** Does collective exhaustion + SUD give the global extension to Ω
   without topological assumptions? SUD plays no role in SP1 (per-level) but re-enters
   for SP2 (global). This is the natural next mathematical question.

2. **Incompleteness theorem.** See the §4 proof note above. Tightening this requires
   deciding the standing assumptions (singleton measurability?) and likely connects
   to Stone space theory.

3. **Stone space connection.** σ(E_Q) as σ-closure of E_Q in the Stone space — may be
   the right lens for both Q2 (incompleteness) and SP2.

4. **Formal layer independence.** The SP1 dissolution shows index and valuation layers
   are conceptually independent. A model-theoretic independence result would make this
   precise.
