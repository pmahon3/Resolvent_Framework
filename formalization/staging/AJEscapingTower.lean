/-
# Unit 4: the escaping tower over the Andersen-Jessen system

Unit 4 of `notes/open_questions/aj_tower/SCOPE_trace_projective_layer.md`.
`EscapingTower` has five fields; three are proved here, against the projective
system of unit 2 instantiated at the tower levels.

  empty  cyl_iInter_empty   -- the hard one. A coherent family lying in every
                               diagonal cylinder pins a single real (coherence
                               plus diagonality force all coordinates to share
                               it), and that real is in every tower level,
                               contradicting X_iInter.
  meas   measurableSet_base -- the diagonal is a finite intersection of
                               coordinate-equality conditions.
  anti   cyl_antitone       -- restriction of a diagonal point is diagonal.

NOT here: `idx` (it is `id`) and `full`, which needs the
`NormalizedCompatibleContents` instance actually built -- i.e. the marginals of
unit 3 packaged through `ofMeasure`, with `nu n (base n) = 1` coming from
mass 1 (`ajThickIn`, `volume_Icc_one`). That packaging is the remaining step,
and until it exists `EscapingTower` cannot be instantiated, so
`not_exists_extension_of_escapingTower` is not yet applied to the tower.

Note the levels here are `X alpha k` (thick in R), not the `[0,1]`-confined
version. `full` will need the confined form; see `ThickTrace.ajThickIn`.

Axiom-free: [propext, Classical.choice, Quot.sound].
-/
import QuerySystem.AndersenJessen
import QuerySystem
open MeasureTheory Set QuerySystem
namespace U4
variable (α : ℝ)

abbrev Lev (α : ℝ) (k : ℕ) : Type := ↥(AndersenJessen.X α k)
abbrev Out (n : ℕ) := (i : Fin (n+1)) → Lev α i
def bond {m n : ℕ} (h : m ≤ n) (x : Out α n) : Out α m := fun i => x ⟨i.1, by omega⟩

lemma measurable_bond {m n : ℕ} (h : m ≤ n) : Measurable (bond α h) :=
  measurable_pi_lambda _ (fun i => measurable_pi_apply _)

def Sys : QuerySystem where
  ι := ℕ
  q := fun n => ⟨Out α n, inferInstance⟩
  le := (· ≤ ·)
  π := fun {m n} h => ⟨bond α h, measurable_bond α h⟩
  le_refl := fun _ => Nat.le_refl _
  le_trans := fun h h' => Nat.le_trans h h'
  π_refl := fun i => by funext x; funext j; rfl
  π_trans := fun hij hjk => by funext x; funext j; rfl

/-- The diagonal in `Out n`: all coordinates carry the same underlying real. -/
def base (n : ℕ) : Set (Out α n) := {x | ∀ i j, (x i).1 = (x j).1}

/-- **`empty`.** A coherent family lying in every diagonal cylinder yields a
real belonging to every tower level -- impossible, since the levels have empty
intersection. -/
theorem cyl_iInter_empty :
    (⋂ n, (Sys α).Cyl n (base α n)) = ∅ := by
  ext ω
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro hall
  -- ω.1 n : Out n; its 0-th coordinate is a point of Lev 0
  set r : ℝ := (ω.1 (0 : ℕ) ⟨0, by omega⟩).1 with hr
  -- claim: r ∈ X α k for every k, contradicting X_iInter
  have hmem : ∀ k, r ∈ AndersenJessen.X α k := by
    intro k
    -- coherence: ω.1 0 = bond (0 ≤ k) (ω.1 k), so the 0-th coord comes from level k
    have hco := ω.2 (show (Sys α).le (0 : ℕ) k from Nat.zero_le k)
    have hdiag := hall k
    -- ω.1 k lies in the diagonal, so all its coordinates share an underlying real
    have : (ω.1 k ⟨0, by omega⟩).1 = (ω.1 k ⟨k, by omega⟩).1 := hdiag _ _
    have h0 : r = (ω.1 k ⟨0, by omega⟩).1 := by
      rw [hr, hco]; rfl
    rw [h0, this]
    exact (ω.1 k ⟨k, by omega⟩).2
  have : r ∈ ⋂ k, AndersenJessen.X α k := Set.mem_iInter.mpr hmem
  rw [AndersenJessen.X_iInter α] at this
  exact this


#print axioms cyl_iInter_empty

/-- **`meas`.** The diagonal is measurable: it is a countable intersection of
coordinate-equality conditions. -/
theorem measurableSet_base (n : ℕ) : MeasurableSet (base α n) := by
  have : base α n = ⋂ (i : Fin (n+1)) (j : Fin (n+1)),
      {x : Out α n | (x i).1 = (x j).1} := by
    ext x; simp [base, Set.mem_iInter]
  rw [this]
  refine MeasurableSet.iInter (fun i => MeasurableSet.iInter (fun j => ?_))
  have hi : Measurable (fun x : Out α n => (x i).1) :=
    (measurable_subtype_coe.comp (measurable_pi_apply i))
  have hj : Measurable (fun x : Out α n => (x j).1) :=
    (measurable_subtype_coe.comp (measurable_pi_apply j))
  exact measurableSet_eq_fun hi hj

/-- **`anti`.** The diagonal cylinders decrease. -/
theorem cyl_antitone : Antitone (fun n : ℕ => (Sys α).Cyl n (base α n)) := by
  intro m n hmn ω hω
  -- ω ∈ Cyl n means eval n ω ∈ base n; need eval m ω ∈ base m
  simp only [QuerySystem.Cyl, QuerySystem.eval, Set.mem_setOf_eq, base] at hω ⊢
  intro i j
  have hco := ω.2 (show (Sys α).le m n from hmn)
  rw [hco]
  exact hω _ _

#print axioms measurableSet_base
#print axioms cyl_antitone
end U4
