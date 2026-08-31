/-
# The lattice gap — the proved witness is an OMP, not an OML (the pinned boundary)

The product-Ulam carrier `L₁` (`UlamWitnessMain`, `psi_ZFC`) is a proved
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

open SigmaEssential SigmaEssential.Blocks

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

/-- **`L₁` is not order-isomorphic to any σ-algebra.** Stronger than
`carrier_not_interClosed`, and on a different hypothesis: that says the carrier
as presented is not closed under intersection, which a change of presentation
could in principle repair. This says no presentation can, because σ-algebras are
lattices and `L₁` has no meet at the cores. Non-Booleanness is intrinsic to the
witness carrier, not an artefact of how it is written down. -/
theorem carrier_not_orderIso_measurableSpace {Ω' : Type*} {msp : MeasurableSpace Ω'}
    (e : {S // L₁.Has S} ≃o {T : Set Ω' // @MeasurableSet Ω' msp T}) : False :=
  witness_carrier_not_lattice (meetsExist_of_orderIso e)

/-! ## The open boundary, named (never assumed) -/

/-- **PsiOML — the OML form of the σ-essential question (OPEN).** Does a
σ-essential witness exist on a carrier that IS a lattice (`MeetsExist`)? The
proved witness `psi_ZFC` establishes the OMP form; `PsiOML` is the
surviving open core — a named `Prop`, NEVER assumed. (Paper §9 conjectures it is
FALSE: every concrete σ-complete OML satisfies Φ, so the OMP/OML line is exactly
the boundary of σ-essential contextuality.) -/
def PsiOML : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    MeetsExist d ∧ IsSigmaEssential s₀

/-- **`PsiOML → Ψ` (proved).** An OML witness drops its latticehood conjunct to
give a bare σ-essential witness. (Only this implication is formalized; the
converse `Ψ → PsiOML` is FALSE-or-open and NOT claimed here.)

The pin is NOT this trivial conjunct-drop. It is the pair of facts:
`Ψ` (`psi_ZFC`) is a *theorem* — the OMP witness exists in ZFC — while
`PsiOML` is *open*, and the proved witness `L₁` provably fails the extra
latticehood conjunct (`witness_carrier_not_lattice`). So the proved witness
inhabits the OMP existence sentence but, being non-lattice, contributes nothing
to `PsiOML`: the OMP/OML line is exactly where "proved" turns into "open." -/
theorem psiOML_gives_sigmaEssential (h : PsiOML) :
    ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
      IsSigmaEssential s₀ := by
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

/-! ## §5. The centre, and essential irreducibility (`cor:centre`)

`prop:adm` needs the witness carrier to be *essentially irreducible*: trivial
centre in the quotient by the countable ideal. The paper computes the centre
exactly (`cor:centre`): the central elements are precisely the countable and
co-countable carrier sets.

Formalized here as far as the code analysis reaches. The remaining steps --
reading `[E₁] = [E₂] ∈ {0,1}` off the surviving codes, repeating with `coreB`
and `coreC` for a common constant, and forcing the fourth class by parity --
are mechanical given `central_meet_code` but are not yet written. Nothing below
is assumed: `IsCentral` is a definition and every result is a theorem. -/

/-- **Centre of the concrete carrier.** `E` is central when it lies in the
carrier and is compatible with every carrier element -- concretely (the
`Blocks.Compat` test), every intersection `E ∩ A` is again in the carrier. -/
def IsCentral (U : UlamMatrix M) (E : Set (M × Fin 4)) : Prop :=
  (carrier U).Has E ∧ ∀ A, (carrier U).Has A → (carrier U).Has (E ∩ A)

/-- Meeting with `coreA = M × {0,1}` empties coordinates 2 and 3. -/
theorem trace_inter_coreA_23 (E : Set (M × Fin 4)) {f : Fin 4} (hf : f = 2 ∨ f = 3) :
    trace (E ∩ coreA M) f = ∅ := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_inter_iff, coreA,
    Set.mem_preimage, Set.mem_insert_iff, Set.mem_singleton_iff,
    Set.mem_empty_iff_false, iff_false, not_and]
  intro _
  rcases hf with rfl | rfl <;> decide

/-- A countable trace forces its selected set countable. -/
theorem sel_countable_of_trace_countable
    {E : Set (M × Fin 4)} {ξ : Set M} {b : Bool} {f : Fin 4}
    (hr : CEq (trace E f) (sel ξ b)) (hc : (trace E f).Countable) :
    (sel ξ b).Countable := by
  refine Set.Countable.mono ?_ (hc.union hr)
  intro x hx
  by_cases hxf : x ∈ trace E f
  · left; exact hxf
  · right; simp [CEq, Set.mem_symmDiff, hxf, hx]

/-- **`cor:stripping`, the impossibility half.** Countable coordinates 2 and 3
force `κ 2 = κ 3`: otherwise the two selected sets are `ξ` and `ξᶜ`, both
countable, making `M` countable. This is what kills the weight-2 cosets. -/
theorem codes_eq_of_traces_countable (huncount : ¬ (Set.univ : Set M).Countable)
    {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (hrep : Represents E ξ κ)
    (h2 : (trace E 2).Countable) (h3 : (trace E 3).Countable) :
    κ 2 = κ 3 := by
  by_contra hne
  have c2 := sel_countable_of_trace_countable (hrep 2) h2
  have c3 := sel_countable_of_trace_countable (hrep 3) h3
  apply huncount
  cases e2 : κ 2 <;> cases e3 : κ 3 <;> rw [e2] at c2 <;> rw [e3] at c3
  · exact absurd (e2.trans e3.symm) hne
  · simpa using c3.union c2
  · simpa using c2.union c3
  · exact absurd (e2.trans e3.symm) hne

/-- **The code restriction for central sets.** For central `E`, the carrier set
`E ∩ coreA` has coordinates 2,3 empty, so `cor:stripping` plus normalization
leaves only `zeroCode` and `κA`: the weight-2 cosets `κB`, `κC` are excluded.
This is the step `cor:centre` runs three times (with `coreA`, `coreB`, `coreC`)
to force a common trace class. -/
theorem central_meet_code (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    ∃ ξ κ, NRep (E ∩ coreA M) ξ κ ∧ (κ = zeroCode ∨ κ = κA) := by
  obtain ⟨ξ, κ, hEven, hκ3, hrep⟩ := nrep_exists huncount (hc.2 _ (has_coreA U))
  refine ⟨ξ, κ, ⟨hEven, hκ3, hrep⟩, ?_⟩
  have h2 : (trace (E ∩ coreA M) 2).Countable := by
    rw [trace_inter_coreA_23 E (Or.inl rfl)]; exact Set.countable_empty
  have h3 : (trace (E ∩ coreA M) 3).Countable := by
    rw [trace_inter_coreA_23 E (Or.inr rfl)]; exact Set.countable_empty
  have hk2 : κ 2 = false := by
    rw [codes_eq_of_traces_countable huncount hrep h2 h3, hκ3]
  rcases normalized_code_cases hEven hκ3 with h | h | h | h
  · exact Or.inl h
  · exact Or.inr h
  · exfalso; rw [h] at hk2; simp [κB] at hk2
  · exfalso; rw [h] at hk2; simp [κC] at hk2

#print axioms central_meet_code

/-! ### `cor:centre`: propagating the code across all three cores -/

/-- Generic: meeting with `Prod.snd ⁻¹' S` empties coordinates outside `S`. -/
theorem trace_inter_out (E : Set (M × Fin 4)) (S : Set (Fin 4)) {f : Fin 4} (hf : f ∉ S) :
    trace (E ∩ Prod.snd ⁻¹' S) f = ∅ := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_preimage,
    Set.mem_empty_iff_false, iff_false, not_and]
  intro _ hS; exact hf hS

/-- Generic: meeting with `Prod.snd ⁻¹' S` leaves coordinates inside `S` alone. -/
theorem trace_inter_in (E : Set (M × Fin 4)) (S : Set (Fin 4)) {f : Fin 4} (hf : f ∈ S) :
    trace (E ∩ Prod.snd ⁻¹' S) f = trace E f := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_preimage]
  exact ⟨fun h => h.1, fun h => ⟨h, hf⟩⟩

/-- **Two coordinates inside a core carry countably-equal traces.** If the two
"outside" coordinates of a core are empty, the code is constant on the two
"inside" ones, so their traces agree mod countable. -/
theorem traces_agree_of_core (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E)
    (S : Set (Fin 4)) (hS : (carrier U).Has (Prod.snd ⁻¹' S))
    (i j o p : Fin 4) (hi : i ∈ S) (hj : j ∈ S) (ho : o ∉ S) (hp : p ∉ S)
    (hxor : ∀ k : Fin 4 → Bool, EvenCode k → k o = k p → k i = k j) :
    CEq (trace E i) (trace E j) := by
  obtain ⟨ξ, κ, hEven, hκ3, hrep⟩ := nrep_exists huncount (hc.2 _ hS)
  -- the two outside coordinates are empty, hence countable
  have hco : (trace (E ∩ Prod.snd ⁻¹' S) o).Countable := by
    rw [trace_inter_out E S ho]; exact Set.countable_empty
  have hcp : (trace (E ∩ Prod.snd ⁻¹' S) p).Countable := by
    rw [trace_inter_out E S hp]; exact Set.countable_empty
  -- so κ o = κ p (else ξ and ξᶜ both countable)
  have hkop : κ o = κ p := by
    by_contra hne
    have c1 := sel_countable_of_trace_countable (hrep o) hco
    have c2 := sel_countable_of_trace_countable (hrep p) hcp
    apply huncount
    cases e1 : κ o <;> cases e2 : κ p <;> rw [e1] at c1 <;> rw [e2] at c2
    · exact absurd (e1.trans e2.symm) hne
    · simpa using c2.union c1
    · simpa using c1.union c2
    · exact absurd (e1.trans e2.symm) hne
  -- even weight + κ o = κ p forces κ i = κ j (the other two coordinates)
  have hkij : κ i = κ j := hxor κ hEven hkop
  -- equal codes on i,j: traces both ≈ sel ξ (κ i)
  have ri := hrep i; have rj := hrep j
  rw [trace_inter_in E S hi] at ri
  rw [trace_inter_in E S hj] at rj
  rw [hkij] at ri
  exact cEq_trans ri (cEq_symm rj)


/-- `coreA = M × {0,1}`: traces 0 and 1 agree. -/
theorem central_t01 (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    CEq (trace E 0) (trace E 1) :=
  traces_agree_of_core huncount U hc {0,1} (has_coreA U)
    0 1 2 3 (by decide) (by decide) (by decide) (by decide)
    (by intro k hk h; revert hk h; unfold EvenCode; cases k 0 <;> cases k 1 <;> cases k 2 <;> cases k 3 <;> simp_all)

/-- `coreB = M × {0,2}`: traces 0 and 2 agree. -/
theorem central_t02 (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    CEq (trace E 0) (trace E 2) :=
  traces_agree_of_core huncount U hc {0,2} (has_coreB U)
    0 2 1 3 (by decide) (by decide) (by decide) (by decide)
    (by intro k hk h; revert hk h; unfold EvenCode; cases k 0 <;> cases k 1 <;> cases k 2 <;> cases k 3 <;> simp_all)

/-- `coreC = M × {1,2}`: traces 1 and 2 agree. -/
theorem central_t12 (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    CEq (trace E 1) (trace E 2) :=
  traces_agree_of_core huncount U hc {1,2} (has_coreC U)
    1 2 0 3 (by decide) (by decide) (by decide) (by decide)
    (by intro k hk h; revert hk h; unfold EvenCode; cases k 0 <;> cases k 1 <;> cases k 2 <;> cases k 3 <;> simp_all)


/-- **The fourth coordinate, by parity.** `E` itself is in the carrier, so it
has a normalized representation; with the first three trace classes equal
(`central_t01`, `central_t02`, `central_t12`), the even-weight condition forces
the code to be constant, hence all four traces countably equal. -/
theorem central_all_traces (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    ∃ ξ, ∀ f, CEq (trace E f) ξ := by
  obtain ⟨ξ, κ, hEven, hκ3, hrep⟩ := nrep_exists huncount hc.1
  have t01 := central_t01 huncount U hc
  have t02 := central_t02 huncount U hc
  -- code is constant: coords 0,1,2 carry countably-equal traces, and κ 3 = false
  -- equal traces force equal codes: if κ a ≠ κ b then sel ξ (κ a) = (sel ξ (κ b))ᶜ,
  -- and CEq of a set with its own complement makes M countable.
  have codes_eq : ∀ a b : Fin 4, CEq (trace E a) (trace E b) → κ a = κ b := by
    intro a b hab
    by_contra hne
    have ra := hrep a; have rb := hrep b
    have : CEq (sel ξ (κ a)) (sel ξ (κ b)) :=
      cEq_trans (cEq_symm ra) (cEq_trans hab rb)
    apply not_cEq_self_compl huncount ξ
    cases ea : κ a <;> cases eb : κ b <;> rw [ea] at this <;> rw [eb] at this
    · exact absurd (ea.trans eb.symm) hne
    · simpa using this
    · exact cEq_symm (by simpa using this)
    · exact absurd (ea.trans eb.symm) hne
  have k01 : κ 0 = κ 1 := codes_eq 0 1 t01
  have k02 : κ 0 = κ 2 := codes_eq 0 2 t02
  -- three equal + even weight + κ3 = false forces all four equal to false
  have hconst : ∀ f, κ f = κ 3 := by
    have h0 : κ 0 = false := by
      revert hEven; unfold EvenCode
      cases e0 : κ 0 <;> cases e1 : κ 1 <;> cases e2 : κ 2 <;> cases e3 : κ 3 <;>
        simp_all
    have h1 : κ 1 = false := by rw [← k01]; exact h0
    have h2 : κ 2 = false := by rw [← k02]; exact h0
    intro f
    rw [hκ3]
    fin_cases f <;> simpa using ‹_›
  refine ⟨sel ξ (κ 3), fun f => ?_⟩
  have := hrep f
  rwa [hconst f] at this


/-- A set all of whose four traces are countable is itself countable. -/
theorem countable_of_traces_countable {E : Set (M × Fin 4)}
    (h : ∀ f, (trace E f).Countable) : E.Countable := by
  have : E ⊆ ⋃ f : Fin 4, (fun x => (x, f)) '' (trace E f) := by
    rintro ⟨x, f⟩ hx
    exact Set.mem_iUnion.mpr ⟨f, ⟨x, hx, rfl⟩⟩
  exact Set.Countable.mono this
    (Set.countable_iUnion fun f => ((h f).image _))

/-- **The reduction `cor:centre` now rests on.** A central `E` has all four
traces countably equal to one `ξ`; so `E` is countable exactly when `ξ` is, and
co-countable exactly when `ξᶜ` is. What remains for `cor:centre` is the paper's
`[E] ∈ {0,1}`: that `ξ ≈ ∅` or `ξ ≈ M`. That does NOT follow from the invariant
alone (`def:invariant` permits any `ξ`), so it needs centrality used a second
time, beyond the code analysis. -/
theorem central_countable_iff (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    ∃ ξ, (∀ f, CEq (trace E f) ξ) ∧ (ξ.Countable → E.Countable) := by
  obtain ⟨ξ, hξ⟩ := central_all_traces huncount U hc
  refine ⟨ξ, hξ, fun hcnt => ?_⟩
  refine countable_of_traces_countable (fun f => ?_)
  refine Set.Countable.mono ?_ (hcnt.union (hξ f))
  intro x hx
  by_cases hxξ : x ∈ ξ
  · left; exact hxξ
  · right; simp [CEq, Set.mem_symmDiff, hx, hxξ]

#print axioms central_all_traces
#print axioms central_countable_iff

/-! ### The ξ-triviality step: the cell route, and why it does not close

`cor:centre` needs one more thing than `central_all_traces` gives: that the
common `ξ` is itself trivial (`ξ ≈ ∅` or `ξ ≈ M`), the paper's `[E] ∈ {0,1}`.
That does NOT follow from the invariant -- `def:invariant` permits any `ξ` --
so centrality has to be used a second time.

The natural attempt is to intersect with cells, which are carrier generators.
The two lemmas below are what that yields, and they are reusable. What they do
NOT yield is the constraint: normalizing `E ∩ cell` gives `ξ ∩ C α n ≈ η` for an
EXISTENTIALLY BOUND `η`, which says nothing. A real constraint has to bring in
the Ulam matrix's combinatorics (`row_cover`, `col_disjoint`) together with
countable initial segments -- the hypothesis set `rigidity` carries as
`hseg : ∀ β, (Set.Iio β).Countable`. Note `central_all_traces` does not take
`hseg`, so either these lemmas gain that hypothesis or the argument goes
elsewhere. Recorded so the route is not re-walked. -/

/-- Trace of an intersection with a cell. -/
theorem trace_inter_cell (U : UlamMatrix M) (E : Set (M × Fin 4)) (α : M) (n : ℕ)
    (f : Fin 4) : trace (E ∩ cell U α n) f = trace E f ∩ U.C α n := by
  ext x; simp [trace, cell]

/-- For a set whose traces are all `≈ ξ`, every trace of `E ∩ cell` is
`≈ ξ ∩ C α n`. -/
theorem cell_traces (U : UlamMatrix M)
    {E : Set (M × Fin 4)} {ξ : Set M} (hξ : ∀ f, CEq (trace E f) ξ)
    (α : M) (n : ℕ) (f : Fin 4) :
    CEq (trace (E ∩ cell U α n) f) (ξ ∩ U.C α n) := by
  rw [trace_inter_cell]
  refine Set.Countable.mono ?_ (hξ f)
  intro x hx
  simp only [Set.mem_symmDiff, Set.mem_inter_iff] at hx ⊢
  rcases hx with ⟨⟨h1, h2⟩, h3⟩ | ⟨⟨h1, h2⟩, h3⟩
  · exact Or.inl ⟨h1, fun hxi => h3 ⟨hxi, h2⟩⟩
  · exact Or.inr ⟨h1, fun hxi => h3 ⟨hxi, h2⟩⟩


/-! ### Countable initial segments: the lever the cell route lacked

`ADMISSIBILITY_SCOPE.md` records that the ξ-triviality step -- the half of
`cor:centre` still missing -- needs more than the code analysis, and that the
cell route stalls because `E ∩ cell` yields only an existentially bound `η`.

The missing input is the hypothesis the paper uses freely: it builds the carrier
on `ω₁`, where initial segments are countable ("simultaneous choice by AC", body
l.503). `thm:rigidity` already carries it in Lean, and `UlamWitnessOmega1`
discharges it for `M₁`. With it, each ROW is conull, so the cells of one row
partition a conull set -- which is what a counting argument can bite on. -/

/-- **Each row is conull, given countable initial segments.** Everything above
`α` is covered by `row_cover`; everything below is countable by `hseg`. -/
theorem row_conull (hseg : ∀ β : M, (Set.Iio β).Countable) (U : UlamMatrix M)
    (α : M) : ((⋃ n, U.C α n)ᶜ).Countable := by
  refine Set.Countable.mono ?_ ((hseg α).union (Set.countable_singleton α))
  intro x hx
  by_contra hxn
  simp only [Set.mem_union, Set.mem_Iio, Set.mem_singleton_iff, not_or] at hxn
  obtain ⟨hlt, hne⟩ := hxn
  have : α < x := lt_of_le_of_ne (not_lt.mp hlt) (Ne.symm hne)
  obtain ⟨n, hn⟩ := U.row_cover this
  exact hx (Set.mem_iUnion.mpr ⟨n, hn⟩)

#print axioms row_conull

/-! ### ξ-triviality: the second use of centrality, at a core rather than a cell

`ADMISSIBILITY_SCOPE.md` records the cell route as a dead end: normalizing
`E ∩ cell` yields `ξ ∩ C α n ≈ η` with `η` existentially bound, which says
nothing. The obstruction there is that a cell constrains only *part* of `ξ`.

A core constrains all of it, and for a reason the cell route cannot use: the
normal form is **anchored at coordinate 3** (`κ 3 = false`), and `coreA` makes
coordinate 3 empty. So one application of centrality at `coreA` pins the
representing set outright.

`E ∩ coreA` is in the carrier by centrality; its coordinate-3 trace is `∅`; the
anchor makes its representing set `≈ ∅`, i.e. countable; and its coordinate-0
trace is `trace E 0 ≈ ξ`. Reading the code at coordinate 0 then leaves exactly
two options — `ξ` countable or `ξᶜ` countable. -/

/-- Meeting with `coreA` keeps coordinates `0` and `1` untouched. -/
theorem trace_inter_coreA_01 (E : Set (M × Fin 4)) {f : Fin 4} (hf : f = 0 ∨ f = 1) :
    trace (E ∩ coreA M) f = trace E f := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_inter_iff, coreA,
    Set.mem_preimage, Set.mem_insert_iff, Set.mem_singleton_iff]
  constructor
  · exact fun h => h.1
  · intro h
    refine ⟨h, ?_⟩
    rcases hf with rfl | rfl
    · exact Or.inl rfl
    · exact Or.inr rfl

/-- **ξ-triviality (`[E] ∈ {0,1}`).** The common `ξ` of a central `E` is
countable or co-countable. This is the step `cor:centre` was missing. -/
theorem central_xi_trivial (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E)
    {ξ : Set M} (hξ : ∀ f, CEq (trace E f) ξ) :
    ξ.Countable ∨ ξᶜ.Countable := by
  -- centrality, used at a CORE: `E ∩ coreA` is again a carrier set
  obtain ⟨η, κ, _, hκ3, hrep⟩ := nrep_exists huncount (hc.2 _ (has_coreA U))
  -- the anchor: coordinate 3 is empty and `κ 3 = false`, so `η ≈ ∅`
  have h3 := hrep 3
  rw [trace_inter_coreA_23 E (Or.inr rfl), hκ3, sel_false] at h3
  have hη : η.Countable := by
    have : symmDiff (∅ : Set M) η = η := by simp
    rw [CEq, this] at h3; exact h3
  -- coordinate 0 carries ξ
  have h0 := hrep 0
  rw [trace_inter_coreA_01 E (Or.inl rfl)] at h0
  have hx : CEq ξ (sel η (κ 0)) := cEq_trans (cEq_symm (hξ 0)) h0
  -- read the code at coordinate 0
  cases hk : κ 0
  · -- κ 0 = false: ξ ≈ η, and η is countable
    left
    rw [hk, sel_false] at hx
    refine Set.Countable.mono ?_ (hx.union hη)
    intro x hxx
    by_cases hxe : x ∈ η
    · exact Or.inr hxe
    · exact Or.inl (Set.mem_symmDiff.mpr (Or.inl ⟨hxx, hxe⟩))
  · -- κ 0 = true: ξ ≈ ηᶜ, so ξᶜ ⊆ (ξ △ ηᶜ) ∪ η
    right
    rw [hk, sel_true] at hx
    refine Set.Countable.mono ?_ (hx.union hη)
    intro x hxx
    by_cases hxe : x ∈ η
    · exact Or.inr hxe
    · exact Or.inl (Set.mem_symmDiff.mpr (Or.inr ⟨hxe, hxx⟩))

/-- Dual of `countable_of_traces_countable`: co-countable traces force a
co-countable set. -/
theorem cocountable_of_traces_cocountable {E : Set (M × Fin 4)}
    (h : ∀ f, (trace E f)ᶜ.Countable) : Eᶜ.Countable := by
  have hsub : Eᶜ ⊆ ⋃ f : Fin 4, (fun x => (x, f)) '' (trace E f)ᶜ := by
    rintro ⟨x, f⟩ hx
    exact Set.mem_iUnion.mpr ⟨f, ⟨x, hx, rfl⟩⟩
  exact Set.Countable.mono hsub
    (Set.countable_iUnion fun f => ((h f).image _))

/-- A trace countably equal to a co-countable `ξ` is itself co-countable. -/
theorem trace_cocountable_of_cEq {X ξ : Set M} (h : CEq X ξ) (hξ : ξᶜ.Countable) :
    Xᶜ.Countable := by
  refine Set.Countable.mono ?_ (h.union hξ)
  intro x hx
  by_cases hxξ : x ∈ ξ
  · exact Or.inl (Set.mem_symmDiff.mpr (Or.inr ⟨hxξ, hx⟩))
  · exact Or.inr hxξ

/-- **`cor:centre`.** A central set of the witness carrier is countable or
co-countable — the paper's `[E] ∈ {0,1}`, now in the kernel.

The two halves come from different places. `central_all_traces` reduces the
question to the single representing set `ξ` (all four traces are countably equal
to it), and `central_xi_trivial` makes `ξ` trivial by applying centrality a
second time, at `coreA`. Neither alone suffices: the invariant permits any `ξ`,
and centrality without the code analysis does not tell you the four coordinates
agree. -/
theorem central_countable_or_cocountable (huncount : ¬ (Set.univ : Set M).Countable)
    (U : UlamMatrix M) {E : Set (M × Fin 4)} (hc : IsCentral U E) :
    E.Countable ∨ Eᶜ.Countable := by
  obtain ⟨ξ, hξ⟩ := central_all_traces huncount U hc
  rcases central_xi_trivial huncount U hc hξ with hc0 | hc1
  · -- ξ countable: every trace is countable, hence E is
    left
    refine countable_of_traces_countable (fun f => ?_)
    refine Set.Countable.mono ?_ ((hξ f).union hc0)
    intro x hx
    by_cases hxξ : x ∈ ξ
    · exact Or.inr hxξ
    · exact Or.inl (Set.mem_symmDiff.mpr (Or.inl ⟨hx, hxξ⟩))
  · -- ξ co-countable: every trace is co-countable, hence E is
    right
    exact cocountable_of_traces_cocountable
      (fun f => trace_cocountable_of_cEq (hξ f) hc1)

end SigmaEssential.Ulam
