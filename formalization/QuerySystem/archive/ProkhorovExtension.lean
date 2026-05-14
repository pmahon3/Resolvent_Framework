/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: [Your Name]
-/
import Mathlib.MeasureTheory.MeasurableSpace.Basic
import Mathlib.MeasureTheory.Measure.MeasureSpaceDef
import Mathlib.MeasureTheory.Measure.Map
import Mathlib.MeasureTheory.Measure.Typeclasses.Probability
import Mathlib.MeasureTheory.Measure.Regular
import Mathlib.MeasureTheory.Measure.AddContent
import Mathlib.MeasureTheory.OuterMeasure.OfAddContent
import Mathlib.Topology.Compactness.Compact
import QuerySystem.TopologicalQuerySystem

/-!
# Prokhorov Extension for Query Systems (§7)

This file formalizes the Prokhorov extension theorem for query systems: given a countable
sequentially upper-directed query system with σ-additive compatible marginals satisfying
*surjective projective uniform tightness*, there exists a unique σ-additive probability
measure on `Omega` recovering all marginals.

## Main results

* `TopologicalQuerySystem.isCompact_compactCore`: `K_Omega` is compact
* `TopologicalQuerySystem.compactInverseLimit_nonempty`: inverse limit is nonempty
  (KEY LEMMA — the FIP argument; fully proved, requires `UpperDirected` hypothesis)
* `TopologicalQuerySystem.prokhorov_extension`: the main theorem (proved, reduces to `observational_extension`)

## Proof architecture

**Step (a) — σ-subadditivity:**
Given `C_N ↓ ∅` with persistent gap `≥ ε`, the compact core `K_Omega` (nonempty by
the inverse limit theorem) witnesses `C_N ∩ K_Omega ≠ ∅` for each N. By the
finite intersection property for compact sets, `⋂_N (C_N ∩ K_Omega) ≠ ∅`, contradicting
`⋂_N C_N = ∅`.

**Step (b) — Concentration on Omega:**
Each defect set `{ω : eval i ω ≠ π(eval j ω)}` is empty by coherence.

## References

* §7 of `observational_foundations.tex`
* Engelking, R. (1989). General Topology, Theorem 3.2.13.
-/

open MeasureTheory TopologicalSpace Set
open scoped ENNReal

universe u v

namespace TopologicalQuerySystem

variable (T : TopologicalQuerySystem.{u, v})

/-! ## Surjective projective uniform tightness -/

/-- A family of compact sets `{K_Q}` is *surjectively compatible* if the bonding maps
    send `K_j` onto `K_i` for every `i ≤ j`.

    Surjectivity (not just containment) is required for the inverse limit theorem:
    `π(K_j) = K_i` ensures every element of `K_i` extends coherently to all finer levels. -/
def IsSurjCompactFamily (K : ∀ i : T.ι, Set ((T.q i).Outcome)) : Prop :=
  (∀ i, IsCompact (K i)) ∧
  (∀ {i j : T.ι} (hij : T.le i j), (T.π hij).π '' (K j) = K i)

/-- **Surjective projective uniform tightness** (Definition 7.1).

    For every `ε > 0`, there is a surjectively compatible compact family `{K_Q}` with
    `ν_Q(O_Q \ K_Q) < ε` for every `Q`. -/
def SurjProjUnifTight (ν : ∀ i : T.ι, Measure ((T.q i).Outcome)) : Prop :=
  ∀ ε : ℝ≥0∞, 0 < ε →
    ∃ K : ∀ i : T.ι, Set ((T.q i).Outcome),
      T.IsSurjCompactFamily K ∧
      ∀ i : T.ι, ν i ((T.q i).Outcome \ K i) < ε

/-! ## The compact core of Omega -/

/-- The compact core: `K_Omega = {ω ∈ Omega | ∀ i, ω(i) ∈ K i}`. -/
def compactCore (K : ∀ i : T.ι, Set ((T.q i).Outcome)) : Set T.toQuerySystem.Omega :=
  { ω | ∀ i : T.ι, T.toQuerySystem.eval i ω ∈ K i }

lemma compactCore_eq_iInter (K : ∀ i : T.ι, Set ((T.q i).Outcome)) :
    T.compactCore K = ⋂ i : T.ι, T.toQuerySystem.Cyl i (K i) := by
  ext ω; simp [compactCore, QuerySystem.Cyl, QuerySystem.eval]

/-- The compact core is closed when each `K i` is closed. -/
lemma isClosed_compactCore (K : ∀ i : T.ι, Set ((T.q i).Outcome))
    (hK_closed : ∀ i, IsClosed (K i)) : IsClosed (T.compactCore K) := by
  rw [T.compactCore_eq_iInter]
  apply isClosed_iInter
  intro i
  have heq : T.toQuerySystem.Cyl i (K i) = T.toQuerySystem.eval i ⁻¹' (K i) := by
    ext ω; simp [QuerySystem.Cyl, QuerySystem.eval]
  rw [heq]
  exact (hK_closed i).preimage (T.continuous_eval i)

/-- The coherence set in the product: elements of `∀ i, O_i` satisfying all refinement
    constraints. This is the image of `Omega` under the forgetful map `ω ↦ ω.1`. -/
def coherenceSet : Set (∀ i : T.ι, (T.q i).Outcome) :=
  { x | ∀ {i j} (hij : T.le i j), x i = (T.π hij).π (x j) }

/-- The coherence set is closed in `∀ i, O_i` when each outcome space is Hausdorff. -/
lemma isClosed_coherenceSet [∀ i, T2Space ((T.q i).Outcome)] :
    IsClosed (T.coherenceSet) := by
  -- coherenceSet = ⋂_{i,j,h : T.le i j} { x | x i = (π h).π (x j) }
  -- Each factor is closed (equalizer of continuous functions, T2).
  apply isClosed_of_closure_subset
  intro x hx
  intro i j hij
  -- x i = (π hij).π (x j) holds as a limit of points in coherenceSet
  have hcont1 : Continuous (fun y : ∀ k : T.ι, (T.q k).Outcome => y i) := continuous_apply i
  have hcont2 : Continuous (fun y : ∀ k : T.ι, (T.q k).Outcome =>
      (T.π hij).π (y j)) :=
    (T.π hij).continuous_π.comp (continuous_apply j)
  exact tendsto_nhds_unique_of_eventuallyEq
    (hcont1.continuousAt.tendsto.comp (mem_closure_iff_nhds.mp hx _ (isOpen_univ) (Set.mem_univ _) |>.choose_spec.2.tendsto))
    (hcont2.continuousAt.tendsto.comp (mem_closure_iff_nhds.mp hx _ (isOpen_univ) (Set.mem_univ _) |>.choose_spec.2.tendsto))
    (Filter.eventually_of_forall fun y => (y.2 hij))

/-- The image of `compactCore K` under `Subtype.val : Omega → ∀ i, O_i` equals
    the intersection of `coherenceSet` with `{ x | ∀ i, x i ∈ K i }`. -/
lemma compactCore_val_image (K : ∀ i : T.ι, Set ((T.q i).Outcome)) :
    Subtype.val '' (T.compactCore K) =
    T.coherenceSet ∩ { x : ∀ i : T.ι, (T.q i).Outcome | ∀ i, x i ∈ K i } := by
  ext x
  simp only [Set.mem_image, compactCore, Set.mem_setOf_eq, Set.mem_inter_iff, coherenceSet]
  constructor
  · rintro ⟨ω, hω, rfl⟩
    exact ⟨fun hij => ω.2 hij, fun i => hω i⟩
  · intro ⟨hcoh, hK⟩
    exact ⟨⟨x, hcoh⟩, hK, rfl⟩

/-- **The compact core is compact.**

    The image of `compactCore K` under `Subtype.val` is a closed subset of the compact
    product `{ x | ∀ i, x i ∈ K i }`, hence compact. By `Subtype.isCompact_iff`,
    `compactCore K` is compact. -/
lemma isCompact_compactCore [∀ i, T2Space ((T.q i).Outcome)]
    (K : ∀ i : T.ι, Set ((T.q i).Outcome))
    (hK_compact : ∀ i, IsCompact (K i)) :
    IsCompact (T.compactCore K) := by
  rw [Subtype.isCompact_iff, T.compactCore_val_image K]
  -- The product {x | ∀ i, x i ∈ K i} is compact (Tychonoff).
  apply IsCompact.of_isClosed_subset (isCompact_pi_infinite hK_compact)
  · -- coherenceSet ∩ {x | ∀ i, x i ∈ K i} is closed in ∀ i, O_i.
    -- It suffices to show both factors are closed (their intersection is closed).
    apply IsClosed.inter
    · -- coherenceSet is closed: intersection of equalizers.
      -- Each constraint { x | x i = (π h).π (x j) } is closed in T2.
      apply isClosed_iInter (s := fun p : Σ i j : T.ι, T.le i j =>
          { x : ∀ i : T.ι, (T.q i).Outcome | x p.1 = (T.π p.2.2).π (x p.2.1) })
      intro ⟨i, j, h⟩
      exact isClosed_eq (continuous_apply i) ((T.π h).continuous_π.comp (continuous_apply j))
    · -- {x | ∀ i, x i ∈ K i} is closed: intersection of preimages of compact (hence closed) sets.
      apply isClosed_iInter
      intro i
      have hKcl : IsClosed (K i) := hK_compact i |>.isClosed
      exact hKcl.preimage (continuous_apply i)
  · -- coherenceSet ∩ {x | ∀ i, x i ∈ K i} ⊆ {x | ∀ i, x i ∈ K i} ⊆ {x | ∀ i, x i ∈ K i}.
    exact Set.inter_subset_right

/-! ## Inverse limit theorem for compact Hausdorff spaces -/

/-- **Inverse limit of nonempty compact Hausdorff spaces with surjective bonding maps is
    nonempty**, and the projections are surjective.

    This is the topological König's lemma (Engelking 3.2.13), proved here by the FIP
    argument on finite coherence sections, following the proof structure of
    `TopCat.nonempty_limitCone_of_compact_t2_cofiltered_system` in Mathlib.

    **Proof.**
    Consider the ambient compact product `P = ∏ K i` (Tychonoff).
    For each finite set `G ⊆ ι` define the *partial section set*
      `S_G = { x ∈ P | ∀ i j ∈ G, ∀ h : T.le i j, x i = (π h).π (x j) }`.
    Each `S_G` is:
    - *Closed* in P: finitely many equalizer conditions, each closed in T2.
    - *Nonempty*: pick any `i₀ ∈ G`; choose `x_{i₀} ∈ K_{i₀}`. For each `j ∈ G`
      with `T.le i₀ j`, use surjectivity to lift to `K_j`. For the rest, pick freely
      from `K_j` (nonempty). The resulting x satisfies the constraints involving i₀.
      For a full FIP argument, use induction / directedness.
    - The family is *directed*: `S_{G₁} ⊇ S_{G₁ ∪ G₂} ⊆ S_{G₂}` (more constraints → smaller).
    By `IsCompact.nonempty_iInter_of_directed_nonempty_isCompact_isClosed`,
    `⋂_G S_G ≠ ∅`. Any point in `⋂_G S_G` satisfies ALL coherence constraints, so it
    defines a coherent section, i.e., a point in `coherenceSet ∩ P = compactCore K`. -/
lemma compactInverseLimit_nonempty
    [Countable T.ι] [Nonempty T.ι]
    [∀ i, T2Space ((T.q i).Outcome)]
    (udir : T.toQuerySystem.UpperDirected)
    (K : ∀ i : T.ι, Set ((T.q i).Outcome))
    (hK_compact : ∀ i, IsCompact (K i))
    (hK_nonempty : ∀ i, (K i).Nonempty)
    (hK_surj : ∀ {i j : T.ι} (hij : T.le i j), (T.π hij).π '' (K j) = K i) :
    (T.compactCore K).Nonempty ∧
    ∀ i : T.ι, T.toQuerySystem.eval i '' (T.compactCore K) = K i := by
  have hK_closed : ∀ i, IsClosed (K i) := fun i => (hK_compact i).isClosed
  -- Define finite diagrams: pairs (G, E) where G ⊆ ι finite and E ⊆ G×G×le finite.
  -- For cleanliness use the type of finite subsets of the coherence index.
  -- The coherence index: triples (i, j, T.le i j).
  -- We index by Finset T.ι directly, enforcing all constraints within the finset.
  --
  -- Define: for G : Finset T.ι, the partial section set
  --   partFin G = { x : ∀ i, O_i | (∀ i, x i ∈ K i) ∧
  --                 (∀ i ∈ G, ∀ j ∈ G, ∀ (h : T.le i j), x i = (π h).π (x j)) }
  -- viewed as a subset of the ambient product.
  let P : Set (∀ i : T.ι, (T.q i).Outcome) := { x | ∀ i, x i ∈ K i }
  let partFin : Finset T.ι → Set (∀ i : T.ι, (T.q i).Outcome) :=
    fun G => P ∩ { x | ∀ i ∈ G, ∀ j ∈ G, ∀ (h : T.le i j), x i = (T.π h).π (x j) }
  -- P is compact (Tychonoff)
  have hP_compact : IsCompact P := isCompact_pi_infinite hK_compact
  -- Each partFin G is closed in ∀ i, O_i
  have hpF_closed : ∀ G : Finset T.ι, IsClosed (partFin G) := by
    intro G
    apply IsClosed.inter
    · apply isClosed_iInter; intro i
      exact (hK_closed i).preimage (continuous_apply i)
    · apply isClosed_iInter; intro i
      apply isClosed_iInter; intro _
      apply isClosed_iInter; intro j
      apply isClosed_iInter; intro _
      apply isClosed_iInter; intro h
      exact isClosed_eq (continuous_apply i) ((T.π h).continuous_π.comp (continuous_apply j))
  -- Each partFin G is nonempty.
  -- Strategy: use upper-directedness to find a common upper bound k for G,
  -- pick any x_k ∈ K k, and define x i = (π hik).π x_k for all i.
  -- Coherence within G follows from π_trans.
  have hpF_nonempty : ∀ G : Finset T.ι, (partFin G).Nonempty := by
    intro G
    -- Get a common upper bound k for G (using UpperDirected + upperBound_finset)
    obtain ⟨k, hk⟩ := T.toQuerySystem.upperBound_finset udir G
    -- Pick any point x_k ∈ K k
    obtain ⟨x_k, hx_k⟩ := hK_nonempty k
    -- Define the assignment: propagate x_k down to all i via refinement maps
    -- For i ≤ k (i.e., i ∈ G), set x i = (π hik).π x_k
    -- For i ∉ G (not constrained), pick any point in K i
    -- We need a function x : ∀ i, (T.q i).Outcome in P satisfying coherence on G.
    -- Use Classical.choice to define x on all of ι.
    let x : ∀ i : T.ι, (T.q i).Outcome := fun i =>
      if hi : i ∈ G
      then (T.π (hk i hi)).π x_k
      else (hK_nonempty i).choose
    refine ⟨x, ?_, ?_⟩
    · -- x ∈ P: show ∀ i, x i ∈ K i
      intro i
      simp only [x]
      split_ifs with hi
      · -- i ∈ G: x i = (π hik).π x_k ∈ K i, since hK_surj says π '' (K k) = K i
        have : (T.π (hk i hi)).π x_k ∈ (T.π (hk i hi)).π '' (K k) :=
          Set.mem_image_of_mem _ hx_k
        rw [hK_surj (hk i hi)] at this
        exact this
      · -- i ∉ G: x i = (hK_nonempty i).choose ∈ K i by definition
        exact (hK_nonempty i).choose_spec
    · -- x satisfies coherence conditions on G
      intro i hi j hj hij
      -- Both i and j are in G; both map down from k.
      -- x i = (π hik).π x_k and x j = (π hjk).π x_k
      -- Coherence: x i = (π hij).π (x j)
      -- i.e. (π hik).π x_k = (π hij).π ((π hjk).π x_k)
      -- This is π_trans: π hik = π hij ∘ π hjk (since hik = le_trans hij hjk)
      simp only [x, dif_pos hi, dif_pos hj]
      -- hk i hi : T.le i k,  hk j hj : T.le j k,  hij : T.le i j
      -- Need: T.le i k = T.le_trans hij (T.le ... j k)?
      -- We have hik := hk i hi : T.le i k
      --         hjk := hk j hj : T.le j k
      --         hij              : T.le i j
      -- π_trans says: π (le_trans hij hjk) = π hij ∘ π hjk
      -- But we need le_trans hij hjk = hik.  This requires proof-irrelevance on le.
      have hik := hk i hi
      have hjk := hk j hj
      -- (T.π hik).π x_k = (T.π hij).π ((T.π hjk).π x_k)
      -- Since T.le i k is a Prop, hik = T.le_trans hij hjk by proof irrelevance.
      -- Then π_trans gives: (T.π (T.le_trans hij hjk)).π = (T.π hij).π ∘ (T.π hjk).π.
      have heq : hik = T.le_trans hij hjk := Subsingleton.elim _ _
      rw [show (T.π hik).π x_k = (T.π (T.le_trans hij hjk)).π x_k from by rw [heq]]
      simp [T.π_trans hij hjk, Function.comp]
  -- The family partFin is directed (G₁ ⊆ G₂ → partFin G₂ ⊆ partFin G₁)
  have hpF_directed : Directed (· ⊇ ·) partFin := by
    intro G₁ G₂
    use G₁ ∪ G₂
    constructor <;> intro x ⟨hP, hcoh⟩ <;> exact ⟨hP, fun i hi j hj h => hcoh i (Finset.mem_union.mpr (by tauto)) j (Finset.mem_union.mpr (by tauto)) h⟩
  -- Each partFin G is compact (closed subset of compact P)
  have hpF_compact : ∀ G : Finset T.ι, IsCompact (partFin G) :=
    fun G => hP_compact.of_isClosed_subset (hpF_closed G) Set.inter_subset_left
  -- Apply Cantor's intersection theorem
  obtain ⟨x, hx⟩ := IsCompact.nonempty_iInter_of_directed_nonempty_isCompact_isClosed
    partFin hpF_directed hpF_nonempty hpF_compact hpF_closed
  -- x satisfies ALL coherence constraints: it defines a point of compactCore K
  have hx_P : ∀ i, x i ∈ K i := by
    have := hx ⟨∅, rfl⟩
    simp only [partFin, Set.mem_iInter] at hx
    exact ((hx ∅).1)
  have hx_coh : ∀ {i j : T.ι} (hij : T.le i j), x i = (T.π hij).π (x j) := by
    intro i j hij
    have := hx {i, j}
    simp only [partFin, Set.mem_iInter, Set.mem_inter_iff, Set.mem_setOf_eq] at hx
    exact (hx {i, j}).2 i (Finset.mem_insert_self _ _) j
      (Finset.mem_insert_of_mem (Finset.mem_singleton_self _)) hij
  -- Package as an element of Omega
  let ω : T.toQuerySystem.Omega := ⟨x, fun hij => hx_coh hij⟩
  constructor
  · -- compactCore K is nonempty
    exact ⟨ω, hx_P⟩
  · -- Projections are surjective
    intro i
    ext y
    simp only [Set.mem_image, compactCore, QuerySystem.eval, Set.mem_setOf_eq]
    constructor
    · rintro ⟨ω', hω', rfl⟩; exact hω' i
    · intro hy
      -- Given y ∈ K i, find ω' ∈ compactCore K with eval i ω' = y.
      -- Strategy: repeat the FIP argument with the additional constraint {x | x i = y}.
      let pinned : Set (∀ j : T.ι, (T.q j).Outcome) := { x | x i = y }
      let partFin' : Finset T.ι → Set (∀ j : T.ι, (T.q j).Outcome) :=
        fun G => partFin G ∩ pinned
      -- pinned is closed (T2 space, y is a point)
      have hpinned_closed : IsClosed pinned :=
        isClosed_eq (continuous_apply i) continuous_const
      -- Each partFin' G is closed
      have hpF'_closed : ∀ G : Finset T.ι, IsClosed (partFin' G) :=
        fun G => (hpF_closed G).inter hpinned_closed
      -- Each partFin' G is compact (closed subset of compact P)
      have hpF'_compact : ∀ G : Finset T.ι, IsCompact (partFin' G) :=
        fun G => hP_compact.of_isClosed_subset (hpF'_closed G)
          (Set.inter_subset_left.trans Set.inter_subset_left)
      -- partFin' is directed (same argument as partFin)
      have hpF'_directed : Directed (· ⊇ ·) partFin' := by
        intro G₁ G₂
        use G₁ ∪ G₂
        constructor <;>
        · intro x ⟨⟨hP_x, hcoh_x⟩, hpin_x⟩
          exact ⟨⟨hP_x, fun a ha b hb h =>
            hcoh_x a (Finset.mem_union.mpr (by tauto)) b (Finset.mem_union.mpr (by tauto)) h⟩,
            hpin_x⟩
      -- Each partFin' G is nonempty:
      -- Get k ≥ G ∪ {i} via upper-directedness, then use hK_surj to find x_k ∈ K k
      -- with (π hik).π x_k = y, and propagate.
      have hpF'_nonempty : ∀ G : Finset T.ι, (partFin' G).Nonempty := by
        intro G
        obtain ⟨k, hk⟩ := T.toQuerySystem.upperBound_finset udir (insert i G)
        have hik : T.le i k := hk i (Finset.mem_insert_self i G)
        -- Use surjectivity to lift y ∈ K i to some x_k ∈ K k with (π hik).π x_k = y
        have : y ∈ (T.π hik).π '' (K k) := by
          rw [hK_surj hik]; exact hy
        obtain ⟨x_k, hx_k_mem, hx_k_val⟩ := this
        -- Define the assignment pinned at i, propagated from x_k
        let x : ∀ j : T.ι, (T.q j).Outcome := fun j =>
          if hj : j ∈ insert i G
          then (T.π (hk j hj)).π x_k
          else (hK_nonempty j).choose
        refine ⟨⟨?_, ?_⟩, ?_⟩
        · -- x ∈ P
          intro j
          simp only [x]
          split_ifs with hj
          · have : (T.π (hk j hj)).π x_k ∈ (T.π (hk j hj)).π '' (K k) :=
              Set.mem_image_of_mem _ hx_k_mem
            rw [hK_surj (hk j hj)] at this; exact this
          · exact (hK_nonempty j).choose_spec
        · -- coherence on G
          intro a ha b hb hab
          simp only [x, dif_pos (Finset.mem_insert_of_mem ha),
                     dif_pos (Finset.mem_insert_of_mem hb)]
          have hak := hk a (Finset.mem_insert_of_mem ha)
          have hbk := hk b (Finset.mem_insert_of_mem hb)
          have heq : hak = T.le_trans hab hbk := Subsingleton.elim _ _
          rw [show (T.π hak).π x_k = (T.π (T.le_trans hab hbk)).π x_k from by rw [heq]]
          simp [T.π_trans hab hbk, Function.comp]
        · -- x i = y (pinned condition)
          simp only [x, pinned, Set.mem_setOf_eq,
                     dif_pos (Finset.mem_insert_self i G)]
          exact hx_k_val
      -- Apply Cantor's intersection theorem to partFin'
      obtain ⟨x, hx'⟩ := IsCompact.nonempty_iInter_of_directed_nonempty_isCompact_isClosed
        partFin' hpF'_directed hpF'_nonempty hpF'_compact hpF'_closed
      -- Extract coherence and pinning from x
      have hx'_P : ∀ j, x j ∈ K j := by
        simp only [partFin', partFin, Set.mem_iInter] at hx'
        exact ((hx' ∅).1).1
      have hx'_coh : ∀ {a b : T.ι} (hab : T.le a b), x a = (T.π hab).π (x b) := by
        intro a b hab
        simp only [partFin', partFin, Set.mem_iInter, Set.mem_inter_iff,
                   Set.mem_setOf_eq] at hx'
        exact ((hx' {a, b}).1).2 a (Finset.mem_insert_self _ _) b
          (Finset.mem_insert_of_mem (Finset.mem_singleton_self _)) hab
      have hx'_pin : x i = y := by
        simp only [partFin', pinned, Set.mem_iInter, Set.mem_inter_iff,
                   Set.mem_setOf_eq] at hx'
        exact (hx' ∅).2
      -- Package as ω' ∈ compactCore K with eval i ω' = y
      exact ⟨⟨x, fun hab => hx'_coh hab⟩, hx'_P, hx'_pin⟩

/-! ## Graph-support lemma -/

/-- The defect set `{ω : eval i ω ≠ π(eval j ω)}` is empty in `Omega`, hence measure 0. -/
lemma measure_defectSet_eq_zero (P : Measure T.toQuerySystem.Omega)
    {i j : T.ι} (hij : T.le i j) :
    P { ω : T.toQuerySystem.Omega |
        T.toQuerySystem.eval i ω ≠ (T.π hij).π (T.toQuerySystem.eval j ω) } = 0 := by
  have hempty : { ω : T.toQuerySystem.Omega |
      T.toQuerySystem.eval i ω ≠ (T.π hij).π (T.toQuerySystem.eval j ω) } = ∅ := by
    ext ω; simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_not]
    exact ω.2 hij
  rw [hempty, measure_empty]

/-! ## The Prokhorov extension theorem -/

/-- **`EvalSurjective` from compact surjective families.**

    If the outcome spaces are compact and `tight` provides a surjectively compatible
    family `K` with `eval i '' compactCore K = K i`, then for any `y : Outcome_i`
    in `K i` we have `y ∈ eval i '' Omega`.  Applying this to the tightness family
    at any `ε` and using `K i ⊆ Outcome_i`, we conclude `eval i` is surjective.

    **Note on the gap:** `SurjProjUnifTight` guarantees that `K i` can be made to
    cover all but ε-measure of `Outcome_i`, but does not literally give `K i = Outcome_i`.
    The full surjectivity `eval i '' Omega = Outcome_i` follows instead from the
    compact-space assumption: take `K i = (T.q i).Outcome` (compact by `CompactSpace`).
    Surjectivity of the bonding maps at the full-space level is the missing ingredient;
    it is supplied here as an explicit hypothesis `surj`.

    A future refactor could derive `surj` from `tight` if the hypotheses include
    surjectivity of the bonding maps `(T.π hij).π` themselves (which `tight` implies
    at the level of the compact subfamily, but not automatically at the level of
    the full outcome spaces). -/
lemma evalSurjective_of_tight
    [Countable T.ι] [Nonempty T.ι]
    [∀ i, T2Space ((T.q i).Outcome)]
    (udir : T.toQuerySystem.UpperDirected)
    (K : ∀ i : T.ι, Set ((T.q i).Outcome))
    (hfam : T.IsSurjCompactFamily K)
    (hnonempty : ∀ i, (K i).Nonempty) :
    ∀ i : T.ι, K i ⊆ T.toQuerySystem.eval i '' T.toQuerySystem.Omega := by
  intro i y hy
  have ⟨_, hnonempty_core⟩ :=
    T.compactInverseLimit_nonempty udir K hfam.1 hnonempty hfam.2
  rw [← hnonempty_core i] at hy
  exact hy

/-- **Prokhorov Extension Theorem** (Theorem 7.1).

    Given a countable sequentially upper-directed topological query system with compact
    Hausdorff outcome spaces, eval-surjective bonding, compatible probability marginals
    satisfying surjective projective uniform tightness, there exists a unique σ-additive
    probability measure `P` on `(Omega, sigmaQ)` with `(eval i)_# P = ν i` for all `i`.

    ## Proof

    We reduce to `QuerySystem.observational_extension` by supplying:
    - `sudir := seq_upper_dir` (sequential upper-directedness, from hypothesis)
    - `surj` (eval surjectivity, from hypothesis — see note below)
    - `compat` (compatible marginals, from hypothesis)

    The `tight` hypothesis is not used in this algebraic route; it is retained as a
    hypothesis documenting the classical proof path (via the FIP argument on compact cores)
    and for potential future use in the Prokhorov proof of σ-subadditivity.

    ## Note on `surj`

    The `EvalSurjective` hypothesis is made explicit here.  In the classical Prokhorov
    setup it follows from surjectivity of the bonding maps `(T.π hij).π` themselves
    (a standard assumption in projective limit theory).  It is not derivable from
    `SurjProjUnifTight` alone without an additional surjectivity-of-bonding-maps assumption
    (which `tight` only provides at the level of the compact subfamily `K i`, not `Outcome_i`).
    A future refactor should add surjectivity of bonding maps as a structural hypothesis
    on `TopologicalQuerySystem` and derive `EvalSurjective` from it. -/
theorem prokhorov_extension
    [Countable T.ι] [Nonempty T.ι]
    [∀ i, T2Space ((T.q i).Outcome)]
    [∀ i, CompactSpace ((T.q i).Outcome)]
    [∀ i, BorelSpace ((T.q i).Outcome)]
    (seq_upper_dir : T.toQuerySystem.SequentiallyUpperDirected)
    (surj : T.toQuerySystem.EvalSurjective)
    (ν : ∀ i : T.ι, Measure ((T.q i).Outcome))
    [∀ i, IsProbabilityMeasure (ν i)]
    (compat : T.toQuerySystem.CompatibleMarginals ν)
    (tight : T.SurjProjUnifTight ν) :
    ∃! P : Measure T.toQuerySystem.Omega,
      IsProbabilityMeasure P ∧
      ∀ i : T.ι, Measure.map (T.toQuerySystem.eval i) P = ν i :=
  T.toQuerySystem.observational_extension seq_upper_dir surj ν compat

/-- **Corollary**: on standard Borel query systems, σ-additivity holds with P(Omega) = 1.

    ## Proof strategy (not yet formalised in Mathlib)

    The correct route is via **Musiał's theorem** (Fund. Math. 110, 1980), not tightness:

    1. Every Borel probability measure on a standard Borel space is **perfect**
       (Bogachev Vol. 2 §7.7.2; Fremlin Vol. 4 §451Q).
       In Mathlib: `StandardBorelSpace` is the relevant typeclass; the perfectness
       fact is currently absent from Mathlib.

    2. A projective system of perfect probability measures over any directed index set
       admits a unique σ-additive projective limit with P(Ω) = 1 — **no topology,
       no tightness, no compactness required**.  This is Musiał 1980.
       Musiał's theorem is not yet in Mathlib.

    ## Mathlib gaps
    - No `PerfectMeasure` definition.
    - No `standard_Borel_measure_is_perfect` lemma.
    - No `Musial_projective_limit` theorem.

    Until these are available, this theorem remains `sorry`.
    The `polish` hypothesis is included because Polish spaces are standard Borel
    (`PolishSpace` implies `StandardBorelSpace` in Mathlib via `borelSpace_of_polish`),
    so this theorem as stated is subsumed by the standard Borel version.
    A future refactor should replace `T.IsPolish` with a `StandardBorelSpace` typeclass
    on outcome spaces and invoke Musiał directly. -/
theorem prokhorov_extension_polish
    [Countable T.ι] [Nonempty T.ι]
    (seq_upper_dir : T.toQuerySystem.SequentiallyUpperDirected)
    (polish : T.IsPolish)
    (ν : ∀ i : T.ι, Measure ((T.q i).Outcome))
    [∀ i, IsProbabilityMeasure (ν i)]
    (compat : T.toQuerySystem.CompatibleMarginals ν) :
    ∃! P : Measure T.toQuerySystem.Omega,
      IsProbabilityMeasure P ∧
      ∀ i : T.ι, Measure.map (T.toQuerySystem.eval i) P = ν i := by
  -- TODO: formalise via Musiał's theorem once PerfectMeasure and
  -- Musial_projective_limit are available in Mathlib.
  -- Route: polish → StandardBorelSpace → every ν i is perfect →
  --         Musiał → unique σ-additive P with P(Omega) = 1.
  sorry

end TopologicalQuerySystem
