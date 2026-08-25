/-
# The lattice gap — the proved witness is an OMP, not an OML (the pinned boundary)

The product-Ulam carrier `L₁` (`UlamWitnessMain`, `psiAmended_ZFC`) is a proved
σ-essential witness: a **σ-complete orthomodular POSET** carrying a σ-essential
contextual state in ZFC. This file machine-checks the exact boundary between what
is *proved* and what is *open*:

* **Proved here:** `L₁` is **not a lattice** — `MeetsExist L₁` fails at the core
  pair `(coreA, coreB)`. Hence the proved witness does NOT settle the OML
  (σ-complete-orthomodular-*lattice*) form of the question.
* **Open (named, never assumed):** `PsiOML` — does a σ-essential witness exist on
  a carrier that IS a lattice? This is the surviving open core (the paper's §9
  conjecture: every concrete σ-complete OML satisfies Φ). The OMP/OML distinction
  is conjectured to be *precisely* the boundary of σ-essential contextuality.

## The reduction (the content)

`MeetsExist` at `(coreA, coreB)` asks for a `⊆`-greatest carrier element below
`coreA ∩ coreB = M × {0}` (fiber 0; the paper's `M × {1}`). We prove — from the
singletons alone — that such a greatest element, IF it existed, would have to
equal `M × {0}` itself. So the meet exists **iff** `M × {0} ∈ L₁`. That single
membership is the whole content, and it FAILS:

## The one cited fact

`slab0_not_mem : ¬ L₁.Has (M × {0})` is **Corollary 4.1** of
`papers/sigma_essential/witness_candidate/sigma_essential_witness.md` (the
"missing meet region": `M×{1}` has odd-weight class pattern `1000`, excluded by
the Normal-Form Theorem 3.5, `L ⊆ P̃`). That is a *proved paper result* resting
on the full §3 invariant machinery (representation rigidity, the disjointness
table, family trichotomy, normal form). Per the programme's "don't re-formalize
known results; `axiom` with citation" rule, it is imported as a cited `axiom`,
NOT re-proved. Formalizing §3 in Lean is a separate, larger unit; flagged as the
substantive next step. Everything ELSE here is a real proof.

**The uncountability hypothesis is load-bearing and MUST be present.** Cor 4.1's
proof (via Lemma 3.2: "`ξ ≈ ξ'` is impossible, `M` being uncountable") needs
`M` uncountable. Without it the axiom is FALSE: at `M := ℕ` the slab `ℕ × {0}`
is countable, so `has_of_countable` puts it IN the carrier. So `slab0_not_mem`
carries `¬ (univ : Set M).Countable`, exactly as Cor 4.1 does. The reduction
lemmas stay hypothesis-free (the reduction is general); only the
membership-negation needs uncountability.

`#print axioms witness_carrier_not_lattice` is the receipt: it shows exactly the
one cited fact (`slab0_not_mem`) the pin leans on, and nothing else opaque.
-/
import QuerySystem.UlamWitnessMain
import QuerySystem.ConcreteOMLBlocks

open Set Function MeasurableSpace

namespace SigmaEssential.Ulam

open SigmaEssential SigmaEssential.Blocks SigmaEssential.Amended

variable {M : Type*} [LinearOrder M]

/-- **The missing meet region as a fiber slab.** `coreA ∩ coreB = M × {0}`
(fibers 0 and 1 for `A`, 0 and 2 for `B`; the common fiber is 0). The paper's
`M × {1}` under its 1-indexed fibers. -/
theorem coreA_inter_coreB_eq_slab0 :
    coreA M ∩ coreB M = Prod.snd ⁻¹' ({0} : Set (Fin 4)) := by
  ext p
  simp only [coreA, coreB, mem_inter_iff, mem_preimage, mem_insert_iff,
    mem_singleton_iff]
  constructor
  · rintro ⟨hA, hB⟩
    -- p.2 ∈ {0,1} and p.2 ∈ {0,2} ⟹ p.2 = 0
    rcases hA with h | h <;> rcases hB with h' | h' <;> omega
  · intro h
    exact ⟨Or.inl h, Or.inl h⟩

/-- A carrier lower bound of `{coreA, coreB}` is exactly a carrier subset of the
slab `M × {0}`. -/
theorem lowerBound_iff_subset_slab (U : UlamMatrix M) (C : Set (M × Fin 4)) :
    ((carrier U).Has C ∧ C ⊆ coreA M ∧ C ⊆ coreB M) ↔
      ((carrier U).Has C ∧ C ⊆ Prod.snd ⁻¹' ({0} : Set (Fin 4))) := by
  rw [← coreA_inter_coreB_eq_slab0, subset_inter_iff]

/-- **The reduction (the content).** If a `⊆`-greatest carrier lower bound `m` of
`{coreA, coreB}` exists, then `m = M × {0}` — forced by the singletons. Every
point `(α,0)` of the slab gives a singleton `{(α,0)}` that is a carrier lower
bound, hence `⊆ m`; so `M × {0} ⊆ m`, and `m ⊆ M × {0}` by the greatest
element's own membership. Consequently the meet EXISTS iff `M × {0} ∈ L`. -/
theorem greatest_lowerBound_eq_slab (U : UlamMatrix M) {m : Set (M × Fin 4)}
    (hm : IsGreatest {C | (carrier U).Has C ∧ C ⊆ coreA M ∧ C ⊆ coreB M} m) :
    m = Prod.snd ⁻¹' ({0} : Set (Fin 4)) := by
  obtain ⟨hmem, hub⟩ := hm
  simp only [Set.mem_setOf_eq] at hmem
  obtain ⟨_, hmA, hmB⟩ := hmem
  -- m ⊆ slab (from m ⊆ coreA ∩ coreB) and slab ⊆ m (each singleton (α,0) is a lower bound)
  have hmsub : m ⊆ Prod.snd ⁻¹' ({0} : Set (Fin 4)) := by
    rw [← coreA_inter_coreB_eq_slab0]
    exact subset_inter hmA hmB
  refine subset_antisymm hmsub (fun p hp => ?_)
  -- p ∈ slab means p.2 = 0; the singleton {p} is a carrier lower bound, so {p} ⊆ m
  have hp0 : p.2 = 0 := hp
  have hsing_lb : {p} ∈ {C | (carrier U).Has C ∧ C ⊆ coreA M ∧ C ⊆ coreB M} := by
    refine ⟨has_singleton U p, ?_, ?_⟩
    · rintro x rfl
      simp only [coreA, mem_preimage, mem_insert_iff, mem_singleton_iff, hp0]; tauto
    · rintro x rfl
      simp only [coreB, mem_preimage, mem_insert_iff, mem_singleton_iff, hp0]; tauto
  exact hub hsing_lb rfl

/-- The traces of the slab `M × {0}`: everything at coordinate `0`, nothing
elsewhere. -/
theorem trace_slab (f : Fin 4) :
    trace (Prod.snd ⁻¹' ({0} : Set (Fin 4))) f
      = (if f = 0 then (Set.univ : Set M) else ∅) := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_preimage, Set.mem_singleton_iff]
  split <;> simp_all

/-- In any representation of the slab, coordinate `0`'s code differs from every
other coordinate's: the `f = 0` trace is co-countable and the rest are countable,
so equal codes would make one set both. -/
theorem slab_codes_differ (huncount : ¬ (Set.univ : Set M).Countable)
    (ξ : Set M) (κ : Fin 4 → Bool) {f : Fin 4} (hf : f ≠ 0)
    (h : Represents (Prod.snd ⁻¹' ({0} : Set (Fin 4))) ξ κ) :
    κ 0 ≠ κ f := by
  intro hEq
  have h0 := h 0; have hg := h f
  rw [trace_slab] at h0 hg
  rw [if_pos rfl] at h0
  rw [if_neg hf] at hg
  rw [hEq] at h0
  unfold CEq at h0 hg
  apply huncount
  refine Set.Countable.mono ?_ (h0.union hg)
  intro x _
  by_cases hx : x ∈ sel ξ (κ f)
  · right; simp [Set.mem_symmDiff, hx]
  · left;  simp [Set.mem_symmDiff, hx]

/-- **Corollary 4.1 (proved).** The slab `M × {0}` (the paper's `M × {1}`, the
missing meet region) is NOT a member of the carrier.

Formerly a cited `axiom` -- Cor 4.1 of
`papers/sigma_essential/witness_candidate/sigma_essential_witness.md`, proved
there via the full §3 invariant machinery and not re-proved here. It is proved
here now: §3 IS formalized (`nrep_exists`, Thm 3.5), so the paper's argument
runs in the kernel. Any representation must give coordinate `0` a code differing
from the other three (`slab_codes_differ`), i.e. the odd-weight `1000` or its
complement `0111`, and `EvenCode` excludes both. -/
theorem slab0_not_mem (U : UlamMatrix M)
    (huncount : ¬ (Set.univ : Set M).Countable) :
    ¬ (carrier U).Has (Prod.snd ⁻¹' ({0} : Set (Fin 4))) := by
  intro hmem
  obtain ⟨ξ, κ, hEven, _hκ3, hrep⟩ := nrep_exists huncount hmem
  have d1 := slab_codes_differ huncount ξ κ (by decide : (1:Fin 4) ≠ 0) hrep
  have d2 := slab_codes_differ huncount ξ κ (by decide : (2:Fin 4) ≠ 0) hrep
  have d3 := slab_codes_differ huncount ξ κ (by decide : (3:Fin 4) ≠ 0) hrep
  unfold EvenCode at hEven
  revert hEven
  cases h0 : κ 0 <;> cases h1 : κ 1 <;> cases h2 : κ 2 <;> cases h3 : κ 3 <;>
    simp_all

/-- **The pin (proved, modulo the one cited fact).** The witness carrier is NOT a
lattice: `MeetsExist` fails at `(coreA, coreB)`. A greatest lower bound would
equal `M × {0}` (`greatest_lowerBound_eq_slab`), which is not in the carrier
(`slab0_not_mem`) — contradiction. So the proved σ-essential witness is a
σ-complete orthomodular **poset**, not a lattice. -/
theorem meetsExist_fails_at_cores (U : UlamMatrix M)
    (huncount : ¬ (Set.univ : Set M).Countable) :
    ¬ ∃ m, IsGreatest {C | (carrier U).Has C ∧ C ⊆ coreA M ∧ C ⊆ coreB M} m := by
  rintro ⟨m, hm⟩
  have hmem := hm.1
  rw [greatest_lowerBound_eq_slab U hm] at hmem
  exact slab0_not_mem U huncount hmem.1

/-- **`L₁` is not a lattice (proved, modulo Cor 4.1).** The concrete-latticehood
property `MeetsExist` fails on the ω₁ product-Ulam witness carrier. -/
theorem witness_carrier_not_lattice : ¬ MeetsExist L₁ := by
  intro hMeets
  exact meetsExist_fails_at_cores U₁ M₁_uncountable (hMeets (has_coreA U₁) (has_coreB U₁))

/-! ## The open boundary, named (never assumed) -/

/-- **PsiOML — the OML form of the σ-essential question (OPEN).** Does a
σ-essential witness exist on a carrier that IS a lattice (`MeetsExist`)? The
proved witness `psiAmended_ZFC` establishes the OMP form; `PsiOML` is the
surviving open core — a named `Prop`, NEVER assumed. (Paper §9 conjectures it is
FALSE: every concrete σ-complete OML satisfies Φ, so the OMP/OML line is exactly
the boundary of σ-essential contextuality.) -/
def PsiOML : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    MeetsExist d ∧ IsSigmaEssentialL s₀

/-- **`PsiOML → Ψ` (proved).** An OML witness drops its latticehood conjunct to
give a bare σ-essential witness. (Only this implication is formalized; the
converse `Ψ → PsiOML` is FALSE-or-open and NOT claimed here.)

The pin is NOT this trivial conjunct-drop. It is the pair of facts:
`Ψ` (`psiAmended_ZFC`) is a *theorem* — the OMP witness exists in ZFC — while
`PsiOML` is *open*, and the proved witness `L₁` provably fails the extra
latticehood conjunct (`witness_carrier_not_lattice`). So the proved witness
inhabits the OMP existence sentence but, being non-lattice, contributes nothing
to `PsiOML`: the OMP/OML line is exactly where "proved" turns into "open." -/
theorem psiOML_gives_sigmaEssential (h : PsiOML) :
    ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
      IsSigmaEssentialL s₀ := by
  obtain ⟨Ω, d, B, s₀, _, hw⟩ := h
  exact ⟨Ω, d, B, s₀, hw⟩

/-! ## Axiom receipts (the honesty check)

`witness_carrier_not_lattice` must show exactly the standard ZFC axioms PLUS the
single cited fact `slab0_not_mem` (Cor 4.1) — and nothing else opaque, no
`sorry`. The reduction theorems (`greatest_lowerBound_eq_slab`,
`coreA_inter_coreB_eq_slab0`) must be choice-clean, showing the CONTENT is real
and only the one membership is imported. -/

#print axioms coreA_inter_coreB_eq_slab0
#print axioms greatest_lowerBound_eq_slab
#print axioms witness_carrier_not_lattice
#print axioms psiOML_gives_sigmaEssential

end SigmaEssential.Ulam
