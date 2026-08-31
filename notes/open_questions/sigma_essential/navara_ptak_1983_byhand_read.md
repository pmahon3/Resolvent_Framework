# Navara–Pták 1983 — by-hand read (the closest published ancestor)

*Extracted from the retired `CHARTED_sigma_essential.md` (2026-06-26). Primary-source
read of the paper the deep-research sweep flagged as the one library-pull needed before
calling the σ-essential cell "genuinely open." Companion to [[sigma_essential_taxonomy]]
(entry `strat.navara_ptak`) and the survey example `ex:navara-ptak`.*

**File:** `notes/literature_review/literature/navara_ptak_1983_two_valued_measures_sigma_classes.pdf`
(Navara & Pták, *Two-valued measures on σ-classes*, Čas. Pěst. Mat. 108(3):225–229, 1983;
gitignored per library convention).

---

## Verdict

**BORDERS the cell, does NOT inhabit it — the cell stays GENUINELY OPEN** (confirmed by
reading, not assertion). The paper solves a DIFFERENT question: Gudder's integration
problem (∫(f+g)=∫f+∫g for two-valued measures on a σ-class), not the σ-essential
extension/independence question. Not an instance of Ψ.

## Three things it gives the programme

1. **Setting confirmed + load-bearing fact.** Their "σ-class" = our concrete σ-complete
   logic EXACTLY (Def 1: Q a set, A closed under complement + countable disjoint unions).
   Key fact: *"any two measurable mappings on a σ-class are summable iff the σ-class is a
   σ-algebra"* — so non-σ-algebra concrete σ-classes are exactly where non-Boolean
   behaviour lives. Confirms the non-Boolean constraint sits right.

2. **GIFT — Thm 1 concentration criterion (reusable).** A 2-valued measure `m` on the
   σ-class `⟨f,g⟩` satisfies additivity IFF `m↾A_{f,g}` is CONCENTRATED at a point (≡ a
   Dirac/point-evaluation). This is exactly the gap mechanism (a state that is / isn't a
   restriction of a Dirac). Proof technique: *"two measures agreeing on all generators of
   a σ-class agree on the whole"* — directly relevant to the σ-point-SELECTION problem at
   the heart of Ψ.

3. **TEMPLATE — explicit concrete NON-concentrated 2-valued measure.** Their Example:
   `Q = ℚ² ∩ (0,1)²`, `f,g` = coordinate projections, `A = ⟨A_f ∪ A_g⟩_σ`, and `m(A)=1`
   iff `A ⊇` one of `B=f⁻¹{1/3}`, `C=g⁻¹{1/2}`, `D=(f+g)⁻¹{1/2}`; since `B∩C∩D=∅`, `m`
   is not concentrated. The closest published object to the phenomenon — NOT the witness
   (`m` is globally defined, no EXTENSION failure) but a construction template on the ℚ²
   carrier. Their pure-but-not-2-valued example (even-subsets σ-class on {1..6}) is a
   caution: pure ≠ 2-valued on σ-classes.

## Why the template is not itself a witness (the key point, verified vs Def 3)

**Joint 1 verified against Navara–Pták Definition 3:** their `m` IS a Ψ-sense σ-additive
2-valued state — Def 3 requires `m(⊔Aᵢ)=Σm(Aᵢ)` over mutually-DISJOINT families; on a
concrete σ-class disjoint = orthogonal, and for 2-valued `m` that additivity is the
σ-homomorphism `s(∨aₙ)=sup s(aₙ)`. So `m` is a genuine Ψ-rescuer, not a weaker-notion
artifact. The `B∩C∩D=∅` device defeats DIRACS, but N–P then construct a NON-Dirac
σ-state through the gap extending `s₀ = {B,C,D ↦ 1}`. **The construction builds its own
rescuer.** This is why clause (i) of the localization never suffices alone, and why all
weight falls on clause (ii). (Navara is co-author ⟹ the concrete-σ-class machinery is
exactly the Navara/Pták Prague school, already in the swept names — no hidden prior art.)

---

## Cross-check 2026-08-31 — a prediction of `isDiracOn_of_countable_singletons`

`Blocks.isDiracOn_of_countable_singletons` proves: on a **countable** carrier
containing **every singleton**, every σ-additive two-valued state agrees on the
carrier with a point evaluation. `Blocks.existsUnique_part_of_countable_partition`
is the mechanism, and it is this file's §"GIFT — Thm 1 concentration criterion"
in general form: σ-additivity concentrates the state on exactly one part of any
countable carrier partition.

That yields a falsifiable prediction about the Example recorded above.
N–P's carrier is `Q = ℚ² ∩ (0,1)²` — **countable** — and they construct on it a
**non-Dirac** σ-additive two-valued state. By the theorem, their σ-class
`A = ⟨A_f ∪ A_g⟩_σ` must therefore **fail to contain some singleton**.

It does, and for the reason the whole programme turns on: a singleton
`{(p,q)} = f⁻¹\{p\} ∩ g⁻¹\{q\}` is an *intersection* of two generators, and the
σ-class is not intersection-closed. So the singletons are exactly what
non-Booleanness withholds, and withholding them is what leaves room for the
non-Dirac state.

Consistent, and informative in both directions: the theorem explains why the
published example had to be built on a non-intersection-closed class over a
countable base, and the example shows the singleton hypothesis is not removable.
