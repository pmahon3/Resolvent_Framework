# The lattice gap, machine-pinned: witness is an OMP not an OML (2026-07-20)

**Goal.** Drive a formal boundary right up to the fundamentally-open aspect, so
the surviving open question is unmistakably isolated. This pins THE crux of the
whole programme: the proved σ-essential witness is a σ-complete orthomodular
**poset**, not a **lattice** — so it does NOT settle the OML form of the
question (the paper's §9 conjecture / the grand Φ problem).

**Where.** New file
`formalization/QuerySystem/QuerySystem/UlamWitnessLatticeGap.lean` (imports
`UlamWitnessMain` + `ConcreteOMLBlocks`; touches no certified core file).

## What is PROVED (real content, choice-clean reduction)

- `coreA_inter_coreB_eq_slab0` — `coreA ∩ coreB = M × {0}` (the common fiber;
  the paper's `M × {1}`). Axioms `[propext, Quot.sound]` — **choice-free**.
- `greatest_lowerBound_eq_slab` — **the reduction (the content).** If a
  `⊆`-greatest carrier lower bound of `{coreA, coreB}` existed, the singletons
  `{(α,0)}` (each a carrier lower bound) force it to equal `M × {0}` itself. So
  the lattice meet exists **iff** `M × {0} ∈ L`. Real proof, not plumbing.
- `witness_carrier_not_lattice : ¬ MeetsExist L₁` — **the pin.** `MeetsExist`
  (concrete latticehood, `ConcreteOMLBlocks`) fails at `(coreA, coreB)` on the
  ω₁ product-Ulam witness carrier.

## The ONE cited fact (honestly flagged, not re-proved)

`slab0_not_mem (U) (huncount : ¬ (univ : Set M).Countable) :
¬ (carrier U).Has (Prod.snd ⁻¹' {0})` — the slab `M × {0}` (paper's `M × {1}`,
the "missing meet region") is not in the carrier **when `M` is uncountable**.
**Corollary 4.1 / 4.4** of `papers/sigma_essential/witness_candidate/
sigma_essential_witness.md`: its class pattern is odd-weight `1000`, excluded by
Normal-Form Theorem 3.5 (`L ⊆ P̃`). That rests on the full §3 invariant
machinery (representation rigidity 3.2, disjointness table 3.3, family
trichotomy 3.4). Per the programme's "don't re-formalize known results;
`axiom` with citation" rule, imported as a cited `axiom`. Formalizing §3 in Lean
is the flagged next unit (larger; `≈`-quotients, weight-2 cosets, parity).

**⚠ SOUNDNESS FIX (2026-07-20, caught by advisor before the final commit
stood).** The `huncount` hypothesis is LOAD-BEARING and was initially omitted.
Cor 4.1's proof (Lemma 3.2: "`ξ ≈ ξ'` impossible, `M` uncountable") requires
`M` uncountable; without it the axiom is FALSE — at `M := ℕ` the slab `ℕ × {0}`
is countable, so `has_of_countable` puts it IN the carrier, and one can derive
`False`. The unqualified axiom was inconsistent AND over-cited Cor 4.1 (which
has the hypothesis). Verified: the old `False`-derivation (via `has_of_countable`
at `M := ℕ`) compiled against the unqualified axiom and now FAILS to typecheck
against the fixed one (`slab0_not_mem` demands `huncount`, unprovable for ℕ).
`M₁_uncountable` supplies it at the `witness_carrier_not_lattice` call site.
Lesson: `#print axioms` verifies WHAT a theorem leans on, not whether a cited
`axiom` is itself CONSISTENT — an asserted axiom must be checked for soundness
separately (instantiate at a small type and try to derive `False`).

## Axiom receipt (the honesty check — passes)

    witness_carrier_not_lattice → [propext, Classical.choice, Quot.sound,
                                   slab0_not_mem]
    coreA_inter_coreB_eq_slab0  → [propext, Quot.sound]   (choice-free)
    greatest_lowerBound_eq_slab → [propext, Classical.choice, Quot.sound]
    sorryAx present: False

The pin leans on **exactly one** named cited fact (`slab0_not_mem`) and nothing
else opaque; **no `sorryAx`** (it is an honest cited axiom, not a hidden
`sorry`). The reduction is choice-clean, so the content is genuine.

## The open boundary, named (never assumed)

`PsiOML : Prop` — does a σ-essential witness exist on a carrier that IS a
lattice (`MeetsExist`)? A named `Prop`, NEVER assumed. `psiOML_gives_sigmaEssential`
proves `PsiOML` drops its latticehood conjunct to a bare σ-essential witness —
so `PsiOML` is STRICTLY STRONGER than the proved Ψ: it adds exactly the lattice
requirement `L₁` provably fails. **This is the pinned boundary:** the proved
witness inhabits the OMP existence sentence but, being non-lattice, contributes
nothing to `PsiOML`. Paper §9 conjectures `PsiOML` is FALSE (every concrete
σ-complete OML satisfies Φ) — so the OMP/OML line is conjectured to be exactly
the boundary of σ-essential contextuality.

## What this pins, in one line

> Machine-checked: the σ-essential witness that exists in ZFC is an OMP; whether
> one exists that is an OML is `PsiOML`, open, and the proved witness fails
> latticehood at the single membership `M×{0} ∉ L` (Cor 4.1). The grand Φ
> question is now formally isolated as `PsiOML`, in the amended vocabulary, with
> its one load-bearing imported fact visible in the axiom receipt.

## Follow-up unit (flagged, not started)

Formalize §3 (invariant `P̃` + Normal Form 3.5) to discharge `slab0_not_mem`
from a cited axiom to a proved theorem — converting the last import of this pin
into machine-checked content. Larger effort; the pin stands honestly meanwhile.
