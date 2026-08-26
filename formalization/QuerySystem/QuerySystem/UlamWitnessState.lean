/-
# The Product Ulam Carrier — §6: the finitely additive vote state `m`

Builds the global finitely additive two-valued state `m` from an ultrafilter
extending the co-countable filter on `M`, through the parity vote
(`v(E) = κ Δ (u(ξ)·1111)`, `m(E) = 1 ⟺ v(E) ∈ Ŝ`), and discharges:

* `mState` — `m` is a `FinAddState (carrier U)` (Lem 6.2 well-definedness via
  `nrep_unique`; Thm 6.3 pair additivity via the §3 disjointness table);
* `mState_extends` — `m` extends the Specker pattern `s₀` (Cor 6.4);
* `corePattern_coherent` — clause (0): `FinitelyCoherent s₀`;
* `witnessAt` / `psi_holds` — with the σ-side (`UlamWitnessCore`),
  **Theorem 7.1**: the pattern is a σ-essential contextual state, so
  `Psi` holds — in ZFC once instantiated at `ω₁` (`UlamWitnessMain`).
-/
import QuerySystem.UlamWitnessInvariant
import Mathlib.Order.Filter.Cocardinal
import Mathlib.Order.Filter.Ultrafilter.Basic

open Set Function MeasurableSpace Filter

namespace SigmaEssential.Ulam

open SigmaEssential

variable {M : Type*} [LinearOrder M]

/-! ## §6.0 The ultrafilter -/

/-- On an uncountable `M` the co-countable filter is proper. -/
theorem cocountable_neBot (huncount : ¬ (Set.univ : Set M).Countable) :
    (Filter.cocountable : Filter M).NeBot := by
  rw [Filter.neBot_iff]
  intro h
  have : (∅ : Set M) ∈ (Filter.cocountable : Filter M) :=
    Filter.empty_mem_iff_bot.mpr h
  rw [Filter.mem_cocountable, compl_empty] at this
  exact huncount this

/-- A fixed ultrafilter extending the co-countable filter (Def 6.1). -/
noncomputable def uf (huncount : ¬ (Set.univ : Set M).Countable) : Ultrafilter M :=
  haveI := cocountable_neBot huncount
  Ultrafilter.of Filter.cocountable

variable {huncount : ¬ (Set.univ : Set M).Countable}

/-- Co-countable sets belong to the ultrafilter. -/
theorem uf_cocountable (h : ¬ (Set.univ : Set M).Countable) {S : Set M}
    (hS : Sᶜ.Countable) : S ∈ uf h := by
  haveI := cocountable_neBot h
  have hmem : S ∈ (Filter.cocountable : Filter M) := Filter.mem_cocountable.mpr hS
  exact Ultrafilter.of_le Filter.cocountable hmem

/-- Countable sets do not belong to the ultrafilter. -/
theorem uf_not_countable (h : ¬ (Set.univ : Set M).Countable) {N : Set M}
    (hN : N.Countable) : N ∉ uf h := by
  intro hmem
  have h1 : Nᶜ ∈ uf h := uf_cocountable h (by rwa [compl_compl])
  have h2 : N ∉ uf h := (Ultrafilter.compl_mem_iff_notMem).mp h1
  exact h2 hmem

/-- `u` is constant on `≈`-classes. -/
theorem uf_congr (h : ¬ (Set.univ : Set M).Countable) {ξ η : Set M}
    (hce : CEq ξ η) : (ξ ∈ uf h ↔ η ∈ uf h) := by
  have key : ∀ {X Y : Set M}, CEq X Y → X ∈ uf h → Y ∈ uf h := by
    intro X Y hXY hX
    have hcompl : (symmDiff X Y)ᶜ ∈ uf h :=
      uf_cocountable h (by rw [compl_compl]; exact hXY)
    have hsub : X ∩ (symmDiff X Y)ᶜ ⊆ Y := by
      rintro x ⟨hxX, hxs⟩
      by_contra hxY
      exact hxs (Set.mem_symmDiff.mpr (Or.inl ⟨hxX, hxY⟩))
    exact Filter.mem_of_superset (Filter.inter_mem hX hcompl) hsub
  exact ⟨key hce, key (cEq_symm hce)⟩

/-- The Boolean value of the ultrafilter on a set. -/
noncomputable def uBool (h : ¬ (Set.univ : Set M).Countable) (ξ : Set M) : Bool := by
  classical
  exact if ξ ∈ uf h then true else false

theorem uBool_eq_true_iff (h : ¬ (Set.univ : Set M).Countable) {ξ : Set M} :
    uBool h ξ = true ↔ ξ ∈ uf h := by
  classical
  simp [uBool]

theorem uBool_congr (h : ¬ (Set.univ : Set M).Countable) {ξ η : Set M}
    (hce : CEq ξ η) : uBool h ξ = uBool h η := by
  classical
  by_cases h1 : ξ ∈ uf h
  · simp [uBool, h1, (uf_congr h hce).mp h1]
  · have h2 : η ∉ uf h := fun hh => h1 ((uf_congr h hce).mpr hh)
    simp [uBool, h1, h2]

theorem uBool_compl (h : ¬ (Set.univ : Set M).Countable) (ξ : Set M) :
    uBool h ξᶜ = ! uBool h ξ := by
  classical
  by_cases h1 : ξ ∈ uf h
  · have h2 : ξᶜ ∉ uf h := fun hc => ((uf h).compl_mem_iff_notMem.mp hc) h1
    simp [uBool, h1, h2]
  · have h2 : ξᶜ ∈ uf h := (uf h).compl_mem_iff_notMem.mpr h1
    simp [uBool, h1, h2]

theorem uBool_empty (h : ¬ (Set.univ : Set M).Countable) :
    uBool h (∅ : Set M) = false := by
  classical
  simp only [uBool, if_neg (uf_not_countable h Set.countable_empty)]

theorem uBool_univ (h : ¬ (Set.univ : Set M).Countable) :
    uBool h (Set.univ : Set M) = true := by
  classical
  simp only [uBool,
    if_pos (uf_cocountable h (by rw [compl_univ]; exact Set.countable_empty))]

/-! ## §6.1 The vote and `Ŝ` -/

/-- The vote `v = κ Δ (b·1111)`. -/
def vote (κ : Fin 4 → Bool) (b : Bool) : Fin 4 → Bool := fun f => xor (κ f) b

/-- The transversal `Ŝ = {1111, 1100, 1010, 0110}` (one member of each
complement pair of `E₄`). -/
abbrev InShat (v : Fin 4 → Bool) : Prop :=
  v = (fun _ => true) ∨ v = κA ∨ v = κB ∨ v = κC

/-- `m`'s defining predicate: some (equivalently by `nrep_unique`, any)
normalized representation votes into `Ŝ`. -/
noncomputable def mVal (h : ¬ (Set.univ : Set M).Countable)
    (E : Set (M × Fin 4)) : Prop :=
  ∃ ξ κ, NRep E ξ κ ∧ InShat (vote κ (uBool h ξ))

/-- **Well-definedness (Lem 6.2).** Against a fixed normalized representation,
`mVal` evaluates to the vote of that representation. -/
theorem mVal_of_nrep (h : ¬ (Set.univ : Set M).Countable)
    {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool} (hrep : NRep E ξ κ) :
    mVal h E ↔ InShat (vote κ (uBool h ξ)) := by
  constructor
  · rintro ⟨η, lam, hrep', hvote⟩
    obtain ⟨hκ, hce⟩ := nrep_unique h hrep' hrep
    rw [hκ] at hvote
    rwa [uBool_congr h hce] at hvote
  · intro hvote
    exact ⟨ξ, κ, hrep, hvote⟩

/-! ## §6.2 The finite Ŝ-logic (all closed Bool computations) -/

theorem inShat_vote_zero (b : Bool) : InShat (vote zeroCode b) ↔ b = true := by
  cases b <;> simp [vote, zeroCode, InShat, κA, κB, κC] <;> decide

/-- Self-duality of `Ŝ` along complement votes, for the three nonzero
normalized codes. -/
theorem inShat_vote_not {κ : Fin 4 → Bool} (hκ : EvenCode κ) (h3 : κ 3 = false)
    (b : Bool) : InShat (vote κ (! b)) ↔ ¬ InShat (vote κ b) := by
  rcases normalized_code_cases hκ h3 with rfl | rfl | rfl | rfl <;>
    cases b <;> simp [vote, zeroCode, InShat, κA, κB, κC] <;> decide

/-! ## §6.3 `m` is a finitely additive state (Thm 6.3) -/

variable (U : UlamMatrix M)

/-- **The state `m`** as a `FinAddState` on the carrier. Normalization at `Ω`,
complement flip, and pair additivity via the §3 table. -/
noncomputable def mState (h : ¬ (Set.univ : Set M).Countable) :
    FinAddState (carrier U) where
  Val := mVal h
  decVal := Classical.decPred _
  val_univ := by
    rw [mVal_of_nrep h nrep_univ, uBool_univ h]
    decide
  not_val_empty := by
    rw [mVal_of_nrep h nrep_empty, uBool_empty h]
    rw [inShat_vote_zero]
    simp
  val_compl := by
    intro E hE
    obtain ⟨ξ, κ, hrep⟩ := nrep_exists h hE
    rw [mVal_of_nrep h hrep, mVal_of_nrep h (nrep_compl hrep),
      uBool_compl h ξ]
    exact inShat_vote_not hrep.1 hrep.2.1 _
  val_union := by
    intro E G hE hG hdisj
    obtain ⟨ξ, κ, hrepE⟩ := nrep_exists h hE
    obtain ⟨η, lam, hrepG⟩ := nrep_exists h hG
    have hEG : (carrier U).Has (E ∪ G) :=
      DynkinSystem.has_union_disjoint _ hE hG hdisj
    by_cases hκ0 : κ = zeroCode <;> by_cases hlam0 : lam = zeroCode
    · -- case (I): both diagonal
      subst hκ0; subst hlam0
      obtain ⟨hint, hrepU⟩ := table_I h hrepE hrepG hdisj
      rw [mVal_of_nrep h hrepE, mVal_of_nrep h hrepG, mVal_of_nrep h hrepU,
        inShat_vote_zero, inShat_vote_zero, inShat_vote_zero,
        uBool_eq_true_iff, uBool_eq_true_iff, uBool_eq_true_iff]
      exact Ultrafilter.union_mem_iff
    · -- case (III): E diagonal, G weight-2
      subst hκ0
      obtain ⟨hEc, hrepU⟩ := table_III h hlam0 hrepE hrepG hdisj
      have hEfalse : ¬ mVal h E := by
        obtain ⟨hκz, hξe⟩ := nrep_countable_of h hrepE hEc
        rw [mVal_of_nrep h hrepE, inShat_vote_zero,
          uBool_congr h hξe, uBool_empty h]
        simp
      rw [mVal_of_nrep h hrepU, ← mVal_of_nrep h hrepG]
      constructor
      · exact fun hval => Or.inr hval
      · rintro (hval | hval)
        · exact absurd hval hEfalse
        · exact hval
    · -- case (III) mirrored: E weight-2, G diagonal
      subst hlam0
      have hdisj' : Disjoint G E := hdisj.symm
      obtain ⟨hGc, hrepU⟩ := table_III h hκ0 hrepG hrepE hdisj'
      have hGfalse : ¬ mVal h G := by
        obtain ⟨hlamz, hηe⟩ := nrep_countable_of h hrepG hGc
        rw [mVal_of_nrep h hrepG, inShat_vote_zero,
          uBool_congr h hηe, uBool_empty h]
        simp
      rw [union_comm] at hrepU
      rw [mVal_of_nrep h hrepU, ← mVal_of_nrep h hrepE]
      constructor
      · exact fun hval => Or.inl hval
      · rintro (hval | hval)
        · exact hval
        · exact absurd hval hGfalse
    · -- cases (II)/(IV): both weight-2; (IV) impossible, so same coset
      have hκlam : κ = lam := by
        by_contra hne
        exact table_IV h hκ0 hlam0 hne hrepE hrepG hdisj
      subst hκlam
      obtain ⟨hce, hrepU⟩ := table_II h hκ0 hrepE hrepG hdisj
      have hη : uBool h η = ! uBool h ξ := by
        rw [uBool_congr h hce, uBool_compl h ξ]
      rw [mVal_of_nrep h hrepE, mVal_of_nrep h hrepG, mVal_of_nrep h hrepU,
        inShat_vote_zero, uBool_univ h, hη]
      have hdual := inShat_vote_not hrepE.1 hrepE.2.1 (uBool h ξ)
      constructor
      · intro _
        by_cases hv : InShat (vote κ (uBool h ξ))
        · exact Or.inl hv
        · exact Or.inr (hdual.mpr hv)
      · intro _
        rfl

/-! ## §6.4 `m` extends the pattern (Cor 6.4) — clause (0) discharged -/

/-- `m` is true on each core (vote = the core's own code, in `Ŝ`). -/
theorem mVal_coreA (h : ¬ (Set.univ : Set M).Countable) :
    mVal h (coreA M) := by
  rw [mVal_of_nrep h nrep_coreA, uBool_empty h]
  decide

theorem mVal_coreB (h : ¬ (Set.univ : Set M).Countable) :
    mVal h (coreB M) := by
  rw [mVal_of_nrep h nrep_coreB, uBool_empty h]
  decide

theorem mVal_coreC (h : ¬ (Set.univ : Set M).Countable) :
    mVal h (coreC M) := by
  rw [mVal_of_nrep h nrep_coreC, uBool_empty h]
  decide

/-- The complement values follow from `val_compl`; the pattern's values on the
block agree with `m`'s. -/
theorem mState_extends (h : ¬ (Set.univ : Set M).Countable) (m₀ : M) :
    ExtendsF (mState U h) (corePattern U m₀) := by
  classical
  intro A hA
  have hcompl : ∀ X, (carrier U).Has X → ((mState U h).Val Xᶜ ↔ ¬ (mState U h).Val X) :=
    fun X hX => (mState U h).val_compl hX
  -- the six block members
  simp only [coreBlock, Finset.mem_insert, Finset.mem_singleton] at hA
  have hpatA : (corePattern U m₀).Val (coreA M) := corePattern_val_coreA U m₀
  have hpatB : (corePattern U m₀).Val (coreB M) := corePattern_val_coreB U m₀
  have hpatC : (corePattern U m₀).Val (coreC M) := corePattern_val_coreC U m₀
  have hpatAc : ¬ (corePattern U m₀).Val (coreA M)ᶜ :=
    fun hc => ((corePattern U m₀).val_compl (by simp [coreBlock])).mp hc hpatA
  have hpatBc : ¬ (corePattern U m₀).Val (coreB M)ᶜ :=
    fun hc => ((corePattern U m₀).val_compl (by simp [coreBlock])).mp hc hpatB
  have hpatCc : ¬ (corePattern U m₀).Val (coreC M)ᶜ :=
    fun hc => ((corePattern U m₀).val_compl (by simp [coreBlock])).mp hc hpatC
  rcases hA with rfl | rfl | rfl | rfl | rfl | rfl
  · simpa [mState] using iff_of_true (mVal_coreA h) hpatA
  · simpa [mState] using iff_of_true (mVal_coreB h) hpatB
  · simpa [mState] using iff_of_true (mVal_coreC h) hpatC
  · refine iff_of_false ?_ hpatAc
    rw [hcompl _ (has_coreA U)]
    simpa [mState] using mVal_coreA h
  · refine iff_of_false ?_ hpatBc
    rw [hcompl _ (has_coreB U)]
    simpa [mState] using mVal_coreB h
  · refine iff_of_false ?_ hpatCc
    rw [hcompl _ (has_coreC U)]
    simpa [mState] using mVal_coreC h

/-- **Clause (0): the pattern is finitely coherent** — `m` witnesses it. -/
theorem corePattern_coherent (h : ¬ (Set.univ : Set M).Countable) (m₀ : M) :
    FinitelyCoherent (corePattern U m₀) :=
  ⟨mState U h, mState_extends U h m₀⟩

/-- **Theorem 7.1 (parameterized).** On any uncountable `M` with countable
initial segments, the Specker pattern on the product Ulam carrier is a
σ-essential contextual state. -/
theorem corePattern_witness (h : ¬ (Set.univ : Set M).Countable)
    (hseg : ∀ β : M, (Set.Iio β).Countable) (m₀ : M) :
    IsSigmaEssential (corePattern U m₀) :=
  (witness_iff_coherent h hseg m₀).mpr (corePattern_coherent U h m₀)

end SigmaEssential.Ulam
