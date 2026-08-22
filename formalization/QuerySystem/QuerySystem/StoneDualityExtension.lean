/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Topology.Compactification.StoneCech
import Mathlib.Topology.Connected.TotallyDisconnected
import Mathlib.MeasureTheory.Measure.Content
import Mathlib.MeasureTheory.Measure.Regular
import Mathlib.MeasureTheory.Measure.AddContent
import Mathlib.MeasureTheory.OuterMeasure.OfAddContent
import Mathlib.MeasureTheory.SetSemiring
import QuerySystem.QuerySystem
import QuerySystem.DiscriminabilityFoundations

/-!
# Stone Duality Route to the Observational Extension Theorem

This file proves the Stone duality route to the observational extension theorem
(Paper I, §5). The Carathéodory route is in `QuerySystem.lean`; this file gives
an independent second proof.

## The argument

Given a query system `S` with a compatible normalized family of finitely additive
charges `P : S.NormalizedCompatibleContents` satisfying Collective Exhaustion,
the Stone route proceeds:

1. **Stone space** (Task 0′-A): `Ultrafilter S.Omega` is compact Hausdorff and
   totally disconnected. Each cylinder event `E ∈ CylGen` gives a clopen
   `{ u | E ∈ u }`. The evaluation map `S.eval i` extends to a continuous map
   `stoneEval i : Ultrafilter S.Omega → Ultrafilter (S.q i).Outcome`.

2. **Charge → Borel measure** (Task 0′-B): A finitely additive normalized charge
   on the clopen algebra of a compact totally-disconnected Hausdorff space extends
   uniquely to a regular Borel measure. **Intentional sorry**: the Mathlib
   `Content` API works on compact sets of a locally compact space; adapting it to
   charges on the clopen algebra of a Stone space requires infrastructure not yet
   in Mathlib (Halmos §53–54, Fremlin Vol. 1).

3. **Inverse system** (Task 0′-C): The bonding maps between Stone outcome spaces
   form a cofiltered inverse system of compact Hausdorff spaces.

4. **Inverse limit measure** (Task 0′-D): The compatible family of charges on the
   Stone outcome spaces extends to a measure on the inverse limit (Choksi's theorem).
   **Intentional sorry**: not yet in Mathlib.

5. **Agreement with Carathéodory** (Task 0′-E): Under shared hypotheses both
   routes produce the same measure. Proved from `observational_determination`.

## Sorry inventory

| Name | Reason |
|------|--------|
| `stone_observational_extension` | Mathlib gap: Yosida–Hewitt decomposition |

All Task 0′-A, 0′-B, 0′-C, and 0′-E results are proved (0 sorry).
`stone_measure_exists` is fully proved via AddContent.measure on stoneClopens.

## Main definitions and results

* `stoneSpace S` — `Ultrafilter S.Omega`
* `stoneEmbedding S` — `pure : S.Omega → Ultrafilter S.Omega`
* `cylGen_clopen` — cylinder events give clopens in `stoneSpace S`
* `stoneEval i` — continuous extension of `S.eval i` to `stoneSpace S`
* `stoneEval_compat` — commutes with refinement maps
* `stoneOutcomeMap hij` — continuous bonding map between Stone outcome spaces
* `stoneOutcomeMap_trans` — transitivity of bonding maps
* `stoneEval_factor` — `stoneOutcomeMap ∘ stoneEval j = stoneEval i`
* `cylGen_charge_wellDef` — presentation independence for charges (proved)
* `stoneAddContent` — AddContent on stoneClopens (proved, 0 sorry)
* `stoneAddContent_isSigmaSubadditive` — σ-subadditivity via compactness (proved)
* `stone_measure_exists` — probability measure on stoneSpace AGREEING with the
  content on every cylinder clopen (proved, 0 sorry)
* `stone_observational_extension` — proved 2026-08-22 under
  `SequentiallyUpperDirected`. It does NOT go through the Stone space: the
  statement was false under plain `UpperDirected` (Andersen–Jessen), and once
  the hypothesis is corrected it follows from `sp1_iff` plus the already-proved
  `QuerySystem.observational_extension`. The Stone construction in this file
  stands on its own as the finitely additive theorem.
* `stone_observational_extension` — (intentional sorry) Stone route main theorem
* `stone_agrees_with_caratheodory` — both routes produce the same measure (proved)

-/

open Set Filter MeasureTheory Topology

-- ---------------------------------------------------------------------------
-- Task 0′-A: Stone space basics
-- ---------------------------------------------------------------------------

section StoneSpaceBasics

variable (S : QuerySystem)

/-- The Stone space of `S` is the space of ultrafilters on `S.Omega`. -/
abbrev stoneSpace (S : QuerySystem) := Ultrafilter S.Omega

/-- The Stone space is compact. -/
instance stoneSpace_compactSpace : CompactSpace (stoneSpace S) :=
  ultrafilter_compact

/-- The Stone space is T2 (Hausdorff). -/
instance stoneSpace_t2Space : T2Space (stoneSpace S) :=
  Ultrafilter.t2Space

/-- The Stone space is totally disconnected. -/
instance stoneSpace_totallyDisconnected : TotallyDisconnectedSpace (stoneSpace S) :=
  inferInstance

/-- `Ultrafilter.map f` is continuous: preimages of basic opens `{u | s ∈ u}`
    are basic opens `{u | f⁻¹'s ∈ u}`. -/
private theorem continuous_ultrafilter_map {α β : Type*} (f : α → β) :
    Continuous (Ultrafilter.map f) := by
  rw [ultrafilterBasis_is_basis.continuous_iff]
  rintro _ ⟨s, rfl⟩
  exact ultrafilter_isOpen_basic (f ⁻¹' s)

/-- The Stone embedding sends each point of `S.Omega` to its principal ultrafilter. -/
def stoneEmbedding : S.Omega → stoneSpace S := pure

/-- The Stone embedding has dense range in the Stone space. -/
theorem stoneEmbedding_denseRange : DenseRange (stoneEmbedding S) :=
  denseRange_pure

/-- Each cylinder event corresponds to a clopen set in the Stone space. -/
theorem cylGen_clopen (E : Set S.Omega) :
    IsClopen { u : stoneSpace S | E ∈ u } :=
  ⟨ultrafilter_isClosed_basic E, ultrafilter_isOpen_basic E⟩

/-- The Stone space has the topology generated by cylinder clopens.
    The topology on `Ultrafilter S.Omega` is generated by the sets `{ u | E ∈ u }`
    for `E : Set S.Omega`, which includes all cylinder sets. -/
theorem stone_topology_generated_by_cylinders :
    (inferInstance : TopologicalSpace (stoneSpace S)) =
    TopologicalSpace.generateFrom (range fun E : Set S.Omega ↦ { u | E ∈ u }) :=
  rfl

/-- Evaluation at level `i`, extended to the Stone space.
    `stoneEval S i u` is the ultrafilter on `(S.q i).Outcome` obtained by pushing
    `u` forward along `S.eval i`. -/
noncomputable def stoneEval (i : S.ι) : stoneSpace S → Ultrafilter (S.q i).Outcome :=
  Ultrafilter.map (S.eval i)

/-- `stoneEval i` is continuous.
    The target `Ultrafilter (S.q i).Outcome` is compact Hausdorff, so
    `Ultrafilter.extend` applies via `continuous_ultrafilter_extend`. -/
theorem stoneEval_continuous (i : S.ι) : Continuous (stoneEval S i) := by
  unfold stoneEval
  exact continuous_ultrafilter_map _

/-- `stoneEval` commutes with refinement: `stoneOutcomeMap hij ∘ stoneEval j = stoneEval i`. -/
theorem stoneEval_compat {i j : S.ι} (hij : S.le i j) :
    Ultrafilter.map (S.π hij).π ∘ stoneEval S j = stoneEval S i := by
  unfold stoneEval
  funext u
  simp only [Function.comp, Ultrafilter.map_map]
  -- Goal: Ultrafilter.map ((S.π hij).π ∘ S.eval j) u = Ultrafilter.map (S.eval i) u
  congr 1
  -- S.eval_comp_refine hij : S.eval i = (S.π hij).π ∘ S.eval j
  exact (S.eval_comp_refine hij).symm

end StoneSpaceBasics

-- ---------------------------------------------------------------------------
-- Task 0′-C: Bonding maps between Stone outcome spaces
-- ---------------------------------------------------------------------------

section StoneBondingMaps

variable (S : QuerySystem)

/-- For `i ≤ j`, the refinement map `(S.π hij).π` induces a continuous map
    between Stone outcome spaces by pushing ultrafilters forward. -/
noncomputable def stoneOutcomeMap {i j : S.ι} (hij : S.le i j) :
    Ultrafilter (S.q j).Outcome → Ultrafilter (S.q i).Outcome :=
  Ultrafilter.map (S.π hij).π

/-- `stoneOutcomeMap hij` is continuous. -/
theorem stoneOutcomeMap_continuous {i j : S.ι} (hij : S.le i j) :
    Continuous (stoneOutcomeMap S hij) := by
  unfold stoneOutcomeMap
  exact continuous_ultrafilter_map _

/-- Transitivity: bonding maps compose correctly.
    `S.π_trans hij hjk : (π (le_trans hij hjk)).π = (π hjk).π ∘ (π hij).π`. -/
theorem stoneOutcomeMap_trans {i j k : S.ι} (hij : S.le i j) (hjk : S.le j k) :
    stoneOutcomeMap S hij ∘ stoneOutcomeMap S hjk =
    stoneOutcomeMap S (S.le_trans hij hjk) := by
  unfold stoneOutcomeMap
  funext u
  simp only [Function.comp, Ultrafilter.map_map]
  -- Goal: Ultrafilter.map ((S.π hij).π ∘ (S.π hjk).π) u = Ultrafilter.map (S.π (S.le_trans hij hjk)).π u
  congr 1
  exact (S.π_trans hij hjk).symm

/-- `stoneEval` factors through the bonding maps. -/
theorem stoneEval_factor {i j : S.ι} (hij : S.le i j) :
    stoneOutcomeMap S hij ∘ stoneEval S j = stoneEval S i :=
  stoneEval_compat S hij

end StoneBondingMaps

-- ---------------------------------------------------------------------------
-- Task 0′-B/D: Charge → measure on Stone space
-- ---------------------------------------------------------------------------
-- INTENTIONAL SORRY
--
-- The standard result (Halmos §53–54; Fremlin, Measure Theory Vol. 1, 311E)
-- says: on a compact totally-disconnected Hausdorff space, every normalized
-- finitely-additive charge on the clopen algebra extends uniquely to a regular
-- Borel measure. The proof goes through the Content API, but Mathlib's
-- `MeasureTheory.Content` is designed for locally compact spaces and operates
-- on compact subsets, not clopen algebras directly. Wrapping the clopen-algebra
-- charge into a `Content` on the Stone space requires showing that in a
-- compact T2D space the clopen algebra and the compact sets generate the same
-- σ-algebra, and that the charge extends monotonically to compacts. This
-- wrapping is not yet in Mathlib.
--
-- Additionally, Step D uses Choksi's theorem (1958): a compatible family of
-- regular Borel probability measures on a cofiltered inverse system of compact
-- Hausdorff spaces with surjective bonding maps has a unique projective limit.
-- This is not in Mathlib.
--
-- ---------------------------------------------------------------------------
-- Stone measure construction via AddContent
-- ---------------------------------------------------------------------------

section StoneMeasureConstruction

open MeasureTheory

variable {α : Type*}

/-- The ultrafilter basis `{u | s ∈ u}` for `s : Set α` forms an `IsSetRing`. -/
theorem isSetRing_ultrafilterBasis :
    IsSetRing (ultrafilterBasis α) where
  empty_mem := ⟨∅, by ext u; simp [Filter.empty_notMem]⟩
  union_mem := by
    rintro _ _ ⟨s, rfl⟩ ⟨t, rfl⟩
    exact ⟨s ∪ t, by ext u; simp [Ultrafilter.union_mem_iff]⟩
  diff_mem := by
    rintro _ _ ⟨s, rfl⟩ ⟨t, rfl⟩
    exact ⟨s \ t, by ext u; simp [Ultrafilter.diff_mem_iff]⟩

/-- An ultrafilter on a finite union of sets must contain one of them. -/
private theorem Ultrafilter.exists_mem_of_sUnion_mem {α : Type*} (u : Ultrafilter α)
    (I : Finset (Set α)) (h : ⋃₀ ↑I ∈ u) : ∃ E ∈ I, E ∈ u := by
  induction I using Finset.induction_on with
  | empty => simp at h
  | @insert E I' hne ih =>
    rw [Finset.coe_insert, Set.sUnion_insert] at h
    have := Ultrafilter.union_mem_iff.mp h
    rcases this with hE | hI'
    · exact ⟨E, Finset.mem_insert_self E I', hE⟩
    · obtain ⟨F, hFI', hFu⟩ := ih hI'
      exact ⟨F, Finset.mem_insert_of_mem hFI', hFu⟩

end StoneMeasureConstruction

/-- The cylinder clopens on the Stone space: the image of the cylinder family
    under the Stone embedding `E ↦ {u | E ∈ u}`. -/
def stoneClopens (S : QuerySystem) : Set (Set (stoneSpace S)) :=
  (fun E => { u : stoneSpace S | E ∈ u }) '' S.CylGen

/-- The map `E ↦ {u | E ∈ u}` is injective on sets: if two sets determine
    the same ultrafilter membership, they are equal. -/
theorem stone_clopen_injective {s t : Set S.Omega} :
    ({u : stoneSpace S | s ∈ u} = {u | t ∈ u}) → s = t := by
  intro h
  ext x
  have : (pure x : Ultrafilter S.Omega) ∈ {u : stoneSpace S | s ∈ u} ↔
         (pure x : Ultrafilter S.Omega) ∈ {u | t ∈ u} := by rw [h]
  simpa using this

/-- The cylinder clopens inherit `IsSetSemiring` from `CylGen`. -/
theorem isSetSemiring_stoneClopens [Nonempty S.ι] (udir : S.UpperDirected) :
    IsSetSemiring (stoneClopens S) where
  empty_mem := by
    refine ⟨∅, (S.isSetSemiring_CylGen udir).empty_mem, ?_⟩
    ext u; simp [Filter.empty_notMem]
  inter_mem := by
    rintro _ ⟨s, hs, rfl⟩ _ ⟨t, ht, rfl⟩
    refine ⟨s ∩ t, (S.isSetSemiring_CylGen udir).inter_mem s hs t ht, ?_⟩
    ext u
    simp only [Set.mem_setOf_eq, Set.mem_inter_iff]
    exact Filter.inter_mem_iff
  diff_eq_sUnion' := by
    rintro _ ⟨s, hs, rfl⟩ _ ⟨t, ht, rfl⟩
    obtain ⟨I, hIC, hIdis, hIeq⟩ :=
      (S.isSetSemiring_CylGen udir).diff_eq_sUnion' s hs t ht
    refine ⟨I.image (fun E => {u : stoneSpace S | E ∈ u}), ?_, ?_, ?_⟩
    · -- I.image φ ⊆ stoneClopens S
      intro V hV
      simp only [Finset.coe_image, Set.mem_image] at hV
      obtain ⟨E, hEI, rfl⟩ := hV
      exact ⟨E, hIC (Finset.mem_coe.mpr hEI), rfl⟩
    · -- pairwise disjoint: φ preserves disjointness
      intro V₁ hV₁ V₂ hV₂ hne
      simp only [Finset.coe_image, Set.mem_image] at hV₁ hV₂
      obtain ⟨E₁, hE₁I, rfl⟩ := hV₁
      obtain ⟨E₂, hE₂I, rfl⟩ := hV₂
      simp only [Function.onFun, id]
      rw [Set.disjoint_left]
      intro u h1 h2
      have hne' : E₁ ≠ E₂ := fun h => hne (by rw [h])
      have hdis : Disjoint E₁ E₂ := by
        have := hIdis (Finset.mem_coe.mpr hE₁I) (Finset.mem_coe.mpr hE₂I) hne'
        simpa [Function.onFun, id] using this
      have hmem := Filter.mem_of_superset (Filter.inter_mem h1 h2) hdis.le_bot
      exact (u : Filter S.Omega).empty_notMem hmem
    · -- sUnion: {u | s ∈ u} \ {u | t ∈ u} = ⋃₀ (I.image φ)
      ext u
      simp only [Set.mem_diff, Set.mem_setOf_eq, Set.mem_sUnion, Finset.coe_image,
        Set.mem_image, Finset.mem_coe]
      rw [show (s ∈ u ∧ t ∉ u) ↔ s \ t ∈ u from (u.diff_mem_iff).symm, hIeq]
      constructor
      · intro h
        obtain ⟨E, hEI, hEu⟩ := Ultrafilter.exists_mem_of_sUnion_mem u I h
        exact ⟨{v | E ∈ v}, ⟨E, hEI, rfl⟩, hEu⟩
      · intro ⟨_, ⟨E, hEI, rfl⟩, hEu⟩
        exact Filter.mem_of_superset hEu (Set.subset_sUnion_of_mem (Finset.mem_coe.mpr hEI))

/-- Presentation independence for charges on `CylGen`: if `E₁ = E₂` as sets and both
    are in `CylGen` (possibly with different presentations `Cyl i A` vs `Cyl j B`),
    then `P.ν i A = P.ν j B`. -/
private theorem cylGen_charge_wellDef (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents)
    {i₁ i₂ : S.ι} {A₁ : Set ((S.q i₁).Outcome)} {A₂ : Set ((S.q i₂).Outcome)}
    (hmeas₁ : MeasurableSet A₁) (hmeas₂ : MeasurableSet A₂)
    (heq : S.Cyl i₁ A₁ = S.Cyl i₂ A₂) :
    P.ν i₁ A₁ = P.ν i₂ A₂ := by
  -- Find common refinement
  obtain ⟨k, hik, hjk⟩ := udir i₁ i₂
  -- At level k: use cyl_refine to lift both presentations
  have hcyl_eq : S.Cyl k ((S.π hik).π ⁻¹' A₁) = S.Cyl k ((S.π hjk).π ⁻¹' A₂) := by
    rw [← S.cyl_refine hik A₁, ← S.cyl_refine hjk A₂, heq]
  -- EvalSurjective → preimage-injective → set equality at level k
  have hpre_eq : (S.π hik).π ⁻¹' A₁ = (S.π hjk).π ⁻¹' A₂ :=
    (Set.preimage_injective.mpr (surj k)) hcyl_eq
  -- CompatibleContents gives the equality
  calc P.ν i₁ A₁
      = P.ν k ((S.π hik).π ⁻¹' A₁) := P.compat hik A₁ hmeas₁
    _ = P.ν k ((S.π hjk).π ⁻¹' A₂) := by rw [hpre_eq]
    _ = P.ν i₂ A₂ := (P.compat hjk A₂ hmeas₂).symm

/-- The charge value for a cylinder event `E ∈ CylGen` with presentation `E = Cyl i A`:
    returns `P.ν i A`. Uses the canonical (Classical.choice) presentation. -/
private noncomputable def cylGenCharge (S : QuerySystem) [Nonempty S.ι]
    (P : S.NormalizedCompatibleContents) (E : Set S.Omega) (hE : E ∈ S.CylGen) :
    ENNReal :=
  P.ν hE.choose hE.choose_spec.choose

/-- The stone charge function on `stoneClopens S` forms a well-defined `AddContent`.
    Finite additivity is transferred from `P.ν` via the Stone embedding.

    Construction uses `sorry` for the finite additivity transfer (`sUnion'`). The
    key mathematical content (well-definedness via `cylGen_charge_wellDef`) is proved;
    the remaining `sorry` is plumbing through `Classical.choice` proofs. -/
private noncomputable def stoneAddContent (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents) :
    AddContent ENNReal (stoneClopens S) where
  toFun V :=
    haveI : Decidable (V ∈ stoneClopens S) := Classical.propDecidable _
    if h : V ∈ stoneClopens S then cylGenCharge S P h.choose h.choose_spec.1
    else 0
  empty' := by
    simp only
    have hempty : (∅ : Set (stoneSpace S)) ∈ stoneClopens S :=
      (isSetSemiring_stoneClopens udir).empty_mem
    simp only [dif_pos hempty]
    -- Goal: cylGenCharge S P hempty.choose hempty.choose_spec.1 = 0
    unfold cylGenCharge
    -- The goal is: P.ν i A = 0 where E = Cyl i A and {u | E ∈ u} = ∅
    -- Use cylGen_charge_wellDef to reduce to any presentation of ∅ ∈ CylGen
    -- Pick the canonical one: ∅ = Cyl i₀ ∅ for any i₀
    obtain ⟨i₀⟩ := ‹Nonempty S.ι›
    have h_empty_cyl : (∅ : Set S.Omega) ∈ S.CylGen :=
      ⟨i₀, ∅, MeasurableSet.empty, by ext ω; simp [QuerySystem.Cyl]⟩
    -- hempty.choose = ∅ (from stone_clopen_injective)
    have hE_eq_empty : hempty.choose = ∅ := by
      apply stone_clopen_injective (S := S)
      convert hempty.choose_spec.2
      ext u; simp [Filter.empty_notMem]
    -- The chose presentation E = Cyl i A has E = ∅, so Cyl i A = ∅
    -- By cylGen_charge_wellDef, P.ν i A = P.ν i₀ ∅
    have hwd := @cylGen_charge_wellDef S _ udir surj P
      hempty.choose_spec.1.choose i₀
      hempty.choose_spec.1.choose_spec.choose (∅ : Set ((S.q i₀).Outcome))
      (hempty.choose_spec.1.choose_spec.choose_spec.1)
      MeasurableSet.empty
      (by rw [← hempty.choose_spec.1.choose_spec.choose_spec.2, hE_eq_empty]
          simp [QuerySystem.Cyl])
    rw [hwd]
    exact addContent_empty
  sUnion' I hI_ss hI_dis hI_mem := by
    classical
    revert hI_ss hI_dis hI_mem
    induction I using Finset.induction_on with
    | empty =>
      intro _ _ hI_mem
      simp only [Finset.coe_empty, Set.sUnion_empty, Finset.sum_empty]
      have hempty : (∅ : Set (stoneSpace S)) ∈ stoneClopens S := by
        convert hI_mem using 1; simp
      simp only [dif_pos hempty]; unfold cylGenCharge
      obtain ⟨i₀⟩ := ‹Nonempty S.ι›
      have hE_eq : hempty.choose = ∅ := by
        apply stone_clopen_injective (S := S)
        convert hempty.choose_spec.2; ext u; simp [Filter.empty_notMem]
      exact (@cylGen_charge_wellDef S _ udir surj P
        hempty.choose_spec.1.choose i₀
        hempty.choose_spec.1.choose_spec.choose (∅ : Set ((S.q i₀).Outcome))
        hempty.choose_spec.1.choose_spec.choose_spec.1 MeasurableSet.empty
        (by rw [← hempty.choose_spec.1.choose_spec.choose_spec.2, hE_eq]
            simp [QuerySystem.Cyl])).trans addContent_empty
    | @insert V I' hnotmem ih =>
      intro hI_ss hI_dis hI_mem
      -- Setup
      have hV_mem : V ∈ stoneClopens S :=
        hI_ss (Finset.mem_coe.mpr (Finset.mem_insert_self V I'))
      have hI'_ss : ↑I' ⊆ stoneClopens S := fun x hx =>
        hI_ss (Finset.mem_coe.mpr (Finset.mem_insert_of_mem (Finset.mem_coe.mp hx)))
      have hI'_dis : PairwiseDisjoint (↑I' : Set (Set (stoneSpace S))) id :=
        hI_dis.subset (Finset.coe_subset.mpr (Finset.subset_insert V I'))
      have hV_disj : Disjoint V (⋃₀ ↑I') := by
        rw [Set.disjoint_sUnion_right]
        intro s hs
        exact hI_dis (Finset.mem_coe.mpr (Finset.mem_insert_self V I'))
          (Finset.mem_coe.mpr (Finset.mem_insert_of_mem (Finset.mem_coe.mp hs)))
          (fun heq => hnotmem (heq ▸ Finset.mem_coe.mp hs))
      -- (a) ⋃₀ ↑I' ∈ stoneClopens S
      have hI'_mem : ⋃₀ ↑I' ∈ stoneClopens S := by
        obtain ⟨K, hK_cyl, hK_eq⟩ := hI_mem
        obtain ⟨E_V, hEV_cyl, hEV_eq⟩ := hV_mem
        have hunion : V ∪ ⋃₀ ↑I' = {u : stoneSpace S | K ∈ u} := by
          have h := hK_eq
          simp only [Finset.coe_insert, Set.sUnion_insert] at h
          exact h.symm
        -- ⋃₀ ↑I' = {u | K \ E_V ∈ u}
        have hrest_eq : ⋃₀ ↑I' = {u : stoneSpace S | K \ E_V ∈ u} := by
          ext u; constructor
          · intro hu
            have hKu : u ∈ {u : stoneSpace S | K ∈ u} := by
              rw [← hunion]; exact Or.inr hu
            have hnotEV : ¬(E_V ∈ u) := by
              intro hEVu
              have hVu : u ∈ V := hEV_eq.symm ▸ hEVu
              exact Set.disjoint_left.mp hV_disj hVu hu
            exact (u : Ultrafilter S.Omega).diff_mem_iff.mpr ⟨hKu, hnotEV⟩
          · intro hu
            have hKu : K ∈ u := ((u : Ultrafilter S.Omega).diff_mem_iff.mp hu).1
            have hnotEV : ¬(E_V ∈ u) := ((u : Ultrafilter S.Omega).diff_mem_iff.mp hu).2
            have hmem_union : u ∈ V ∪ ⋃₀ ↑I' := by
              have : u ∈ {u : stoneSpace S | K ∈ u} := hKu
              rwa [← hunion] at this
            rcases hmem_union with hV | hI'
            · have hEVu : E_V ∈ u := by
                have : u ∈ (fun E => {u : stoneSpace S | E ∈ u}) E_V := hEV_eq ▸ hV
                exact this
              exact absurd hEVu hnotEV
            · exact hI'
        rw [hrest_eq]
        -- K \ E_V ∈ CylGen
        obtain ⟨i_K, A_K, hA_K, hK_pres⟩ := hK_cyl
        obtain ⟨i_V, A_V, hA_V, hEV_pres⟩ := hEV_cyl
        obtain ⟨k, hkK, hkV⟩ := udir i_K i_V
        refine ⟨K \ E_V, ?_, rfl⟩
        have : K \ E_V = S.Cyl k ((S.π hkK).π ⁻¹' A_K \ (S.π hkV).π ⁻¹' A_V) := by
          rw [hK_pres, hEV_pres, S.cyl_refine hkK A_K, S.cyl_refine hkV A_V]
          ext ω; simp [QuerySystem.Cyl]
        rw [this]
        exact ⟨k, _, (hA_K.preimage (S.π hkK).measurable_π).diff
          (hA_V.preimage (S.π hkV).measurable_π), rfl⟩
      -- (b) Apply IH
      have hih := ih hI'_ss hI'_dis hI'_mem
      -- (c) Binary additivity: toFun(V ∪ ⋃₀ I') = toFun(V) + toFun(⋃₀ I')
      rw [Finset.coe_insert, Set.sUnion_insert, Finset.sum_insert hnotmem, ← hih]
      -- Goal: toFun (V ∪ ⋃₀ ↑I') = toFun V + toFun (⋃₀ ↑I')
      -- V ∪ ⋃₀ I' ∈ stoneClopens (= hI_mem after insert rewrite)
      have hU_mem : V ∪ ⋃₀ ↑I' ∈ stoneClopens S := by
        convert hI_mem using 1; rw [Finset.coe_insert, Set.sUnion_insert]
      simp only [dif_pos hU_mem, dif_pos hV_mem, dif_pos hI'_mem]
      unfold cylGenCharge
      -- Goal shape: P.ν i₁ A₁ = P.ν i₂ A₂ + P.ν i₃ A₃
      -- where i₁,A₁ from hU_mem; i₂,A₂ from hV_mem; i₃,A₃ from hI'_mem
      -- Find common level
      obtain ⟨k, hk⟩ := S.upperBound_finset udir
        ({hU_mem.choose_spec.1.choose, hV_mem.choose_spec.1.choose,
          hI'_mem.choose_spec.1.choose} : Finset S.ι)
      -- Use wellDef to express all three at level k
      have hkU := hk _ (Finset.mem_insert_self _ _)
      have hkV := hk _ (Finset.mem_insert_of_mem (Finset.mem_insert_self _ _))
      have hkI := hk _ (Finset.mem_insert_of_mem (Finset.mem_insert_of_mem
        (Finset.mem_singleton_self _)))
      -- The presentations
      have hU_meas := hU_mem.choose_spec.1.choose_spec.choose_spec.1
      have hV_meas := hV_mem.choose_spec.1.choose_spec.choose_spec.1
      have hI_meas := hI'_mem.choose_spec.1.choose_spec.choose_spec.1
      have hU_pres := hU_mem.choose_spec.1.choose_spec.choose_spec.2
      have hV_pres := hV_mem.choose_spec.1.choose_spec.choose_spec.2
      have hI_pres := hI'_mem.choose_spec.1.choose_spec.choose_spec.2
      -- Preimages at level k
      have hmU := hU_meas.preimage (S.π hkU).measurable_π
      have hmV := hV_meas.preimage (S.π hkV).measurable_π
      have hmI := hI_meas.preimage (S.π hkI).measurable_π
      -- Well-definedness: each P.ν i A = P.ν k (π⁻¹' A)
      have hwU := P.compat hkU _ hU_meas
      have hwV := P.compat hkV _ hV_meas
      have hwI := P.compat hkI _ hI_meas
      rw [hwU, hwV, hwI]
      -- Goal: P.ν k (π_U⁻¹' A_U) = P.ν k (π_V⁻¹' A_V) + P.ν k (π_I⁻¹' A_I)
      -- Show π_U⁻¹' A_U = (π_V⁻¹' A_V) ∪ (π_I⁻¹' A_I) and they're disjoint
      have hset_eq : (S.π hkU).π ⁻¹' hU_mem.choose_spec.1.choose_spec.choose =
          ((S.π hkV).π ⁻¹' hV_mem.choose_spec.1.choose_spec.choose) ∪
          ((S.π hkI).π ⁻¹' hI'_mem.choose_spec.1.choose_spec.choose) := by
        apply (Set.preimage_injective.mpr (surj k))
        -- Goal: eval k ⁻¹' (π_U⁻¹' A_U) = eval k ⁻¹' ((π_V⁻¹' A_V) ∪ (π_I⁻¹' A_I))
        -- eval k ⁻¹' (π⁻¹' A) = Cyl (choose) (choose_spec.choose) = choose_underlying
        have lhs : S.eval k ⁻¹' ((S.π hkU).π ⁻¹' hU_mem.choose_spec.1.choose_spec.choose) =
            hU_mem.choose := by
          show S.Cyl k _ = _; rw [← S.cyl_refine hkU, ← hU_pres]
        have rhs_V : S.eval k ⁻¹' ((S.π hkV).π ⁻¹' hV_mem.choose_spec.1.choose_spec.choose) =
            hV_mem.choose := by
          show S.Cyl k _ = _; rw [← S.cyl_refine hkV, ← hV_pres]
        have rhs_I : S.eval k ⁻¹' ((S.π hkI).π ⁻¹' hI'_mem.choose_spec.1.choose_spec.choose) =
            hI'_mem.choose := by
          show S.Cyl k _ = _; rw [← S.cyl_refine hkI, ← hI_pres]
        rw [Set.preimage_union, lhs, rhs_V, rhs_I]
        -- Goal: hU_mem.choose = hV_mem.choose ∪ hI'_mem.choose
        apply stone_clopen_injective (S := S)
        -- Goal: {u | (hU).choose ∈ u} = {u | (hV).choose ∪ (hI').choose ∈ u}
        ext u
        simp only [Set.mem_setOf_eq, Ultrafilter.union_mem_iff]
        -- Goal: hU.choose ∈ u ↔ hV.choose ∈ u ∨ hI'.choose ∈ u
        -- The goal is: hU_mem.choose ∈ u ↔ hV_mem.choose ∈ u ∨ hI'_mem.choose ∈ u
        -- hU_mem.choose_spec.2 says: (fun E => {u|E∈u}) hU_mem.choose = V ∪ ⋃₀ ↑I'
        -- which beta-reduces to: {u | hU_mem.choose ∈ u} = V ∪ ⋃₀ ↑I'
        -- Similarly for hV_mem and hI'_mem.
        -- Use congrFun (extensionality) to get pointwise iff
        have hU_iff : hU_mem.choose ∈ u ↔ u ∈ V ∪ ⋃₀ ↑I' :=
          show u ∈ {u | hU_mem.choose ∈ u} ↔ _ from by
            rw [show ({u : stoneSpace S | hU_mem.choose ∈ u} : Set _) = V ∪ ⋃₀ ↑I' from
              hU_mem.choose_spec.2]
        have hV_iff : hV_mem.choose ∈ u ↔ u ∈ V :=
          show u ∈ {u | hV_mem.choose ∈ u} ↔ _ from by
            rw [show ({u : stoneSpace S | hV_mem.choose ∈ u} : Set _) = V from
              hV_mem.choose_spec.2]
        have hI_iff : hI'_mem.choose ∈ u ↔ u ∈ ⋃₀ ↑I' :=
          show u ∈ {u | hI'_mem.choose ∈ u} ↔ _ from by
            rw [show ({u : stoneSpace S | hI'_mem.choose ∈ u} : Set _) = ⋃₀ ↑I' from
              hI'_mem.choose_spec.2]
        constructor
        · intro hu
          rcases hU_iff.mp hu with hV' | hI''
          · left; exact hV_iff.mpr hV'
          · right; exact hI_iff.mpr hI''
        · intro h
          rcases h with hV' | hI''
          · exact hU_iff.mpr (Or.inl (hV_iff.mp hV'))
          · exact hU_iff.mpr (Or.inr (hI_iff.mp hI''))
      have hdisj : Disjoint ((S.π hkV).π ⁻¹' hV_mem.choose_spec.1.choose_spec.choose)
          ((S.π hkI).π ⁻¹' hI'_mem.choose_spec.1.choose_spec.choose) := by
        rw [Set.disjoint_left]
        intro o hoV hoI
        obtain ⟨ω, hω⟩ := surj k o
        have hωV : (pure ω : stoneSpace S) ∈ V := by
          have h1 : ω ∈ S.eval k ⁻¹' ((S.π hkV).π ⁻¹'
            hV_mem.choose_spec.1.choose_spec.choose) := by
            simp only [Set.mem_preimage]; rw [hω]; exact hoV
          have h2 : ω ∈ hV_mem.choose := by
            have heq : S.Cyl k ((S.π hkV).π ⁻¹'
              hV_mem.choose_spec.1.choose_spec.choose) = hV_mem.choose := by
              rw [← S.cyl_refine hkV, ← hV_pres]
            rw [← heq]; exact h1
          have h3 : (pure ω : stoneSpace S) ∈
            (fun E => {u : stoneSpace S | E ∈ u}) hV_mem.choose := h2
          rw [hV_mem.choose_spec.2] at h3; exact h3
        have hωI : (pure ω : stoneSpace S) ∈ ⋃₀ ↑I' := by
          have h1 : ω ∈ S.eval k ⁻¹' ((S.π hkI).π ⁻¹'
            hI'_mem.choose_spec.1.choose_spec.choose) := by
            simp only [Set.mem_preimage]; rw [hω]; exact hoI
          have h2 : ω ∈ hI'_mem.choose := by
            have heq : S.Cyl k ((S.π hkI).π ⁻¹'
              hI'_mem.choose_spec.1.choose_spec.choose) = hI'_mem.choose := by
              rw [← S.cyl_refine hkI, ← hI_pres]
            rw [← heq]; exact h1
          have h3 : (pure ω : stoneSpace S) ∈
            (fun E => {u : stoneSpace S | E ∈ u}) hI'_mem.choose := h2
          rw [hI'_mem.choose_spec.2] at h3; exact h3
        exact Set.disjoint_left.mp hV_disj hωV hωI
      rw [hset_eq]
      exact addContent_union (QuerySystem.isSetRing_measurableSets _) hmV hmI hdisj

/-- The Stone content is σ-subadditive by compactness: if clopens cover a clopen,
    finitely many suffice, and finite subadditivity gives the bound.

    This is the key step that uses the topology of the Stone space. -/
private theorem stoneAddContent_isSigmaSubadditive (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents) :
    (stoneAddContent S udir surj P).IsSigmaSubadditive := by
  intro f hf hf_Union
  -- Each f n is a clopen {u | E_n ∈ u}, hence open
  have hf_open : ∀ n, IsOpen (f n) := by
    intro n
    obtain ⟨En, _, hEn_eq⟩ := hf n
    rw [← hEn_eq]; exact (cylGen_clopen S En).2
  -- ⋃ n, f n ∈ stoneClopens, so it equals {u | K ∈ u} for some K
  have hf_Union' := hf_Union
  obtain ⟨K, hK_cyl, hK_eq⟩ := hf_Union'
  -- {u | K ∈ u} is compact (closed in compact space)
  have hK_compact : IsCompact {u : stoneSpace S | K ∈ u} :=
    (cylGen_clopen S K).1.isCompact
  -- Finite subcover by compactness
  have hcover : {u : stoneSpace S | K ∈ u} ⊆ ⋃ n, f n :=
    hK_eq ▸ Set.Subset.refl _
  obtain ⟨t, ht⟩ := hK_compact.elim_finite_subcover f hf_open hcover
  -- Step 1: ⋃₀ (t.image f) = ⋃ n, f n (compactness + trivial direction)
  have hsUnion_eq : ⋃₀ ↑(t.image f) = ⋃ n, f n := by
    rw [Finset.coe_image, Set.sUnion_image]
    apply Set.Subset.antisymm
    · exact Set.iUnion₂_subset fun n _ => Set.subset_iUnion f n
    · calc ⋃ n, f n = {u : stoneSpace S | K ∈ u} := hK_eq.symm
        _ ⊆ ⋃ i ∈ t, f i := ht
  -- Step 2: Members of t.image f are in stoneClopens
  have hfin_ss : ↑(t.image f) ⊆ stoneClopens S := by
    intro V hV
    rw [Finset.mem_coe, Finset.mem_image] at hV
    obtain ⟨n, _, rfl⟩ := hV; exact hf n
  -- Step 3: ⋃₀ (t.image f) ∈ stoneClopens (equals ⋃ n, f n which is)
  have hfin_mem : ⋃₀ ↑(t.image f) ∈ stoneClopens S := by
    rw [hsUnion_eq]; exact hf_Union
  have hsemiring := isSetSemiring_stoneClopens udir
  -- Step 4: Chain the inequalities
  calc (stoneAddContent S udir surj P) (⋃ n, f n)
      = (stoneAddContent S udir surj P) (⋃₀ ↑(t.image f)) := by
        congr 1; exact hsUnion_eq.symm
    _ ≤ ∑ u ∈ t.image f, (stoneAddContent S udir surj P) u :=
        addContent_sUnion_le_sum hsemiring _ hfin_ss hfin_mem
    _ ≤ ∑ n ∈ t, (stoneAddContent S udir surj P) (f n) :=
        Finset.sum_image_le_of_nonneg (fun _ _ => zero_le _)
    _ ≤ ∑' n, (stoneAddContent S udir surj P) (f n) :=
        ENNReal.sum_le_tsum (↑t)

/-- Given a normalized compatible family of charges `P` on the outcome spaces of `S`,
    there exists a probability measure `P̂` on `stoneSpace S` (w.r.t. the σ-algebra
    generated by the cylinder clopens).

    **Construction:** Transfer `P.ν` to an `AddContent` on `stoneClopens S` via the
    Stone embedding `E ↦ {u | E ∈ u}`.  Prove σ-subadditivity via compactness of the
    Stone space.  Apply `AddContent.measure` (Carathéodory extension).

    **The agreement clause is load-bearing.** Until 2026-08-22 the conclusion
    was only `∃ Phat, IsProbabilityMeasure Phat`, which never mentions `P`, so
    it was satisfied by a Dirac measure at any ultrafilter with `udir`, `surj`
    and `P` all unused (Lean's own linter said so). The Carathéodory extension
    the proof builds was discarded at the statement boundary and no downstream
    step could use it. `stone_observational_extension` Step 1 needs exactly the
    agreement clause now stated. -/
theorem stone_measure_exists (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents) :
    haveI : MeasurableSpace (stoneSpace S) :=
      MeasurableSpace.generateFrom (stoneClopens S)
    ∃ Phat : MeasureTheory.Measure (stoneSpace S),
      MeasureTheory.IsProbabilityMeasure Phat ∧
      ∀ E ∈ stoneClopens S, Phat E = stoneAddContent S udir surj P E := by
  letI mα : MeasurableSpace (stoneSpace S) :=
    MeasurableSpace.generateFrom (stoneClopens S)
  -- Build the AddContent on stoneClopens
  let m := stoneAddContent S udir surj P
  have hsemiring := isSetSemiring_stoneClopens udir
  have hgen : mα ≤ MeasurableSpace.generateFrom (stoneClopens S) := le_refl _
  have hsigma := stoneAddContent_isSigmaSubadditive S udir surj P
  -- Apply Carathéodory extension
  have hgen_eq : mα = MeasurableSpace.generateFrom (stoneClopens S) := rfl
  refine ⟨m.measure hsemiring hgen hsigma, ?_,
    fun E hE => AddContent.measure_eq m hsemiring hgen_eq hsigma hE⟩
  constructor
  -- Prove μ(univ) = 1
  -- univ = {u | Set.univ ∈ u} since every ultrafilter contains univ
  have huniv_eq : (Set.univ : Set (stoneSpace S)) =
      {u : stoneSpace S | (Set.univ : Set S.Omega) ∈ u} := by
    ext u
    simp only [Set.mem_univ, Set.mem_setOf_eq, true_iff]
    exact Filter.univ_mem
  -- Set.univ ∈ CylGen
  obtain ⟨i₀⟩ := ‹Nonempty S.ι›
  have huniv_cyl : (Set.univ : Set S.Omega) ∈ S.CylGen :=
    ⟨i₀, Set.univ, MeasurableSet.univ, by ext ω; simp [QuerySystem.Cyl]⟩
  -- univ ∈ stoneClopens S
  have huniv_stone : (Set.univ : Set (stoneSpace S)) ∈ stoneClopens S := by
    rw [huniv_eq]; exact ⟨Set.univ, huniv_cyl, rfl⟩
  -- measure_eq gives: μ(univ) = m(univ)
  have hmeas_eq := AddContent.measure_eq m hsemiring hgen_eq hsigma huniv_stone
  rw [huniv_eq] at hmeas_eq ⊢
  rw [hmeas_eq]
  -- Goal: m {u | Set.univ ∈ u} = 1
  -- Unfold AddContent to get cylGenCharge, then use wellDef to reduce to P.ν i₀ univ
  show (stoneAddContent S udir surj P).toFun {u | (Set.univ : Set S.Omega) ∈ u} = 1
  simp only [stoneAddContent]
  have hmem : {u : stoneSpace S | (Set.univ : Set S.Omega) ∈ u} ∈ stoneClopens S :=
    ⟨Set.univ, huniv_cyl, rfl⟩
  simp only [dif_pos hmem]
  -- Goal: cylGenCharge S P hmem.choose hmem.choose_spec.1 = 1
  unfold cylGenCharge
  -- Goal: P.ν (hmem.choose_spec.1.choose) (hmem.choose_spec.1.choose_spec.choose) = 1
  -- By cylGen_charge_wellDef with i₂ = i₀, A₂ = Set.univ:
  -- Cyl i A = hmem.choose = Set.univ = Cyl i₀ Set.univ
  -- so P.ν i A = P.ν i₀ Set.univ = 1
  have hE_is_univ : hmem.choose = Set.univ := by
    apply stone_clopen_injective (S := S)
    exact hmem.choose_spec.2
  have hwd := @cylGen_charge_wellDef S _ udir surj P
    hmem.choose_spec.1.choose i₀
    hmem.choose_spec.1.choose_spec.choose (Set.univ : Set ((S.q i₀).Outcome))
    hmem.choose_spec.1.choose_spec.choose_spec.1
    MeasurableSet.univ
    (by rw [← hmem.choose_spec.1.choose_spec.choose_spec.2, hE_is_univ]
        ext ω; simp [QuerySystem.Cyl])
  rw [hwd]
  exact P.norm i₀

-- ---------------------------------------------------------------------------
-- Task 0′-B/D (continued): Stone observational extension
-- ---------------------------------------------------------------------------
-- HISTORY. This carried an intentional `sorry` from its introduction until
-- 2026-08-22, recorded as blocked on the Yosida-Hewitt decomposition being
-- absent from Mathlib. That diagnosis was wrong twice over.
--
-- 1. The statement was FALSE as stated. It assumed only `UpperDirected`, and
--    `ce_iff_levelwise_continuity` shows CE is exactly per-level σ-additivity.
--    So the hypotheses read "compatible σ-additive marginals + upper-directed
--    + surjective evaluations", and the conclusion is the global extension:
--    Kolmogorov extension with no regularity hypothesis of any kind. The
--    Andersen-Jessen construction (Sparre Andersen-Jessen 1948) refutes it,
--    indexed by ℕ under ≤ -- upper-directed, NOT sequentially so. See the
--    blueprint, `rmk:kolmogorov-refuted`.
-- 2. No Stone space is needed. With `SequentiallyUpperDirected` -- the natural
--    hypothesis when queries are σ-algebras closed under countable joins --
--    `sp1_iff` converts CE into per-level measures and the already-proved
--    `QuerySystem.observational_extension` finishes directly on `S.Omega`.
--
-- The hypothesis is therefore strengthened to `SequentiallyUpperDirected` and
-- the theorem is proved. Yosida-Hewitt is not required, and neither is any
-- charge theory.

/-- **Stone observational extension theorem.**

    Under `SequentiallyUpperDirected`, `EvalSurjective` and collective
    exhaustion, there is a unique probability measure `μ` on `S.Omega`
    recovering the compatible charges: `μ (Cyl i A) = P.ν i A` for every level
    `i` and measurable `A`.

    **Why sequential upper-directedness, and not merely `UpperDirected`.**
    Under `UpperDirected` alone the statement is false; see the block comment
    above and `rmk:kolmogorov-refuted` in the blueprint. Sequential
    upper-directedness is what a countable cover needs in order to be dominated
    by a single level, and it is the natural condition when a query is a
    σ-algebra of resolvable events and the query family is closed under
    countable joins: `⋁ₙ Qₙ` is then itself a query.

    **Proof.** `sp1_iff` turns CE into a genuine measure at each level;
    compatibility transfers because each `μ i` agrees with `P.ν i` on every
    measurable set; `observational_extension` then extends and
    `map_apply_eval_eq_cyl` converts marginal recovery into the cylinder form.
    No Stone space appears. -/
theorem stone_observational_extension (S : QuerySystem) [Nonempty S.ι]
    (sudir : S.SequentiallyUpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents)
    (hce : S.CollectivelyExhaustive P.ν) :
    ∃! μ : MeasureTheory.Measure S.Omega,
      MeasureTheory.IsProbabilityMeasure μ ∧
      ∀ (i : S.ι) (A : Set ((S.q i).Outcome)), MeasurableSet A →
        μ (S.Cyl i A) = P.ν i A := by
  classical
  -- CE gives a genuine measure at each level (`sp1_iff`).
  choose μ hμ using (S.sp1_iff P).mp hce
  haveI : ∀ i, MeasureTheory.IsProbabilityMeasure (μ i) := by
    intro i
    constructor
    rw [hμ i Set.univ MeasurableSet.univ]
    exact P.norm i
  -- Compatibility transfers: `μ i` agrees with `P.ν i` on every measurable set.
  have hcompat : S.CompatibleMarginals μ := by
    intro i j hij
    ext A hA
    rw [MeasureTheory.Measure.map_apply (S.π hij).measurable_π hA,
        hμ j _ ((S.π hij).measurable_π hA), ← P.compat hij A hA, hμ i A hA]
  obtain ⟨Q, ⟨hQprob, hQmarg⟩, hQuniq⟩ := S.observational_extension sudir surj μ hcompat
  refine ⟨Q, ⟨hQprob, ?_⟩, ?_⟩
  · intro i A hA
    rw [← S.map_apply_eval_eq_cyl Q i A hA, hQmarg i, hμ i A hA]
  · rintro ν' ⟨hν'prob, hν'cyl⟩
    refine hQuniq ν' ⟨hν'prob, fun i => ?_⟩
    ext A hA
    rw [S.map_apply_eval_eq_cyl ν' i A hA, hν'cyl i A hA, ← hμ i A hA]

-- ---------------------------------------------------------------------------
-- Task 0′-E: Agreement with the Carathéodory route
-- ---------------------------------------------------------------------------

/-- **Coincidence of routes.**

    If two probability measures on `S.Omega` both recover the same compatible
    family of marginals on all query levels, they are equal. In particular,
    the Stone extension and the Carathéodory extension (`observational_extension`
    in `QuerySystem.lean`) produce the same measure whenever both apply.

    This is an immediate consequence of `observational_determination`: any
    two finite measures with equal pushforwards along all `S.eval i` are equal.

    **No sorry.** -/
theorem stone_agrees_with_caratheodory (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (μ₁ μ₂ : MeasureTheory.Measure S.Omega)
    [MeasureTheory.IsFiniteMeasure μ₁]
    (h : ∀ i : S.ι,
        MeasureTheory.Measure.map (S.eval i) μ₁ =
        MeasureTheory.Measure.map (S.eval i) μ₂) :
    μ₁ = μ₂ :=
  S.observational_determination udir μ₁ μ₂ h
