/-
# Unit 3: contents and Kolmogorov consistency for the AJ marginals

Unit 3 of `notes/open_questions/aj_tower/SCOPE_trace_projective_layer.md`.

Two pieces, both general rather than tower-specific:

* `ofMeasure` -- every measure is an `AddContent` on the measurable sets. The
  repo had no generic conversion (only two bespoke ones), and
  `NormalizedCompatibleContents` wants contents, not measures.
* `marginal` / `marginal_compat` -- the AJ marginals are `P n = diag_* mu n`,
  and Kolmogorov consistency REDUCES to a condition on the base measures:
  `P m = bond_* P n` exactly when `mu m = incl_* mu n`. The proof is the
  commutation `bond h . diag n = diag m . incl h` (`bond_diag`), which needs
  the inclusions to compose coherently -- hence `Tower'`.

The tower supplies the inclusions: `X_antitone` gives `X n subset X m` for
`m <= n`, which is the right direction (checked).

DISCHARGED 2026-08-24: the tower instance of `(mu n).map (incl h) = mu m` is
`ThickTrace.ajTrace_compat`, off `map_incl_traceMeasure` -- both sides send a
trace `E n X` to `lambda E`, and the inclusion pulls a trace back to the trace
definitionally. Unit 3 is complete.

Axiom-free: [propext, Classical.choice, Quot.sound].
-/
import QuerySystem
open MeasureTheory Set Finset
open scoped ENNReal
namespace U3
variable {Ω : Type*} [MeasurableSpace Ω]

/-- **Any measure is an additive content on the measurable sets.** -/
noncomputable def ofMeasure (μ : Measure Ω) :
    AddContent ℝ≥0∞ {s : Set Ω | MeasurableSet s} where
  toFun := fun s => μ s
  empty' := by simp
  sUnion' := by
    intro I hss hdis hmem
    rw [measure_sUnion I.countable_toSet hdis (fun s hs => hss hs), tsum_fintype]
    exact Finset.sum_finset_coe (f := fun s => μ s) I


variable {X : ℕ → Type} [∀ k, MeasurableSpace (X k)]

abbrev Out (X : ℕ → Type) (n : ℕ) := (i : Fin (n+1)) → X i

/-- The diagonal needs a coercion `X n → X i` for `i ≤ n`. In the tower this is
the inclusion `X_n ⊆ X_i` (antitone). Abstractly: a coherent family of maps. -/
structure Tower (X : ℕ → Type) [∀ k, MeasurableSpace (X k)] where
  incl : ∀ {m n : ℕ}, m ≤ n → X n → X m
  meas : ∀ {m n : ℕ} (h : m ≤ n), Measurable (incl h)

/-- The diagonal map into level `n`. -/
def diag (T : Tower X) (n : ℕ) (x : X n) : Out X n :=
  fun i => T.incl (by omega) x

theorem measurable_diag (T : Tower X) (n : ℕ) : Measurable (diag T n) := by
  refine measurable_pi_lambda _ (fun i => ?_)
  exact T.meas _


/-- The bonding map: initial-segment restriction (H1's `bond`). -/
def bond {m n : ℕ} (h : m ≤ n) (x : Out X n) : Out X m := fun i => x ⟨i.1, by omega⟩

/-- **The key commutation.** Restricting a diagonal point is the diagonal of the
restricted point -- PROVIDED the inclusions compose coherently. -/
structure Tower' (X : ℕ → Type) [∀ k, MeasurableSpace (X k)] extends Tower X where
  incl_comp : ∀ {a b c : ℕ} (hab : a ≤ b) (hbc : b ≤ c) (x : X c),
    toTower.incl hab (toTower.incl hbc x) = toTower.incl (hab.trans hbc) x

theorem bond_diag (T : Tower' X) {m n : ℕ} (h : m ≤ n) (x : X n) :
    bond h (diag T.toTower n x) = diag T.toTower m (T.toTower.incl h x) := by
  funext i
  simp only [bond, diag]
  exact (T.incl_comp _ h x).symm

/-- The marginals: `P n = map (diag n) (mu n)`. -/
noncomputable def marginal (T : Tower X) (mu : ∀ k, Measure (X k)) (n : ℕ) :
    Measure (Out X n) :=
  (mu n).map (diag T n)

/-- **Kolmogorov consistency**, reduced to a statement about the base measures:
`P m = bond_* P n` exactly when `mu m = incl_* mu n`. -/
theorem marginal_compat (T : Tower' X) (mu : ∀ k, Measure (X k))
    (hmu : ∀ {m n : ℕ} (h : m ≤ n), (mu n).map (T.toTower.incl h) = mu m)
    {m n : ℕ} (h : m ≤ n) :
    (marginal T.toTower mu n).map (bond h) = marginal T.toTower mu m := by
  unfold marginal
  rw [Measure.map_map (by exact measurable_pi_lambda _ (fun i => measurable_pi_apply _))
        (measurable_diag T.toTower n)]
  have : (bond (X := X) h) ∘ (diag T.toTower n) = (diag T.toTower m) ∘ (T.toTower.incl h) := by
    funext x; exact bond_diag T h x
  rw [this, ← Measure.map_map (measurable_diag T.toTower m) (T.meas h), hmu h]

#print axioms ofMeasure
#print axioms marginal_compat
end U3
