/-
# The `full` field: the diagonal carries all the mass

The last unproved input of unit 4's `EscapingTower`.

`full` asks for `nu n (base n) = 1`, where `nu n` is the diagonal pushforward of
the level measure. `Measure.map_apply` reduces this to
`mu n (diag^-1 (base n))`, and the preimage is everything because every
diagonal point trivially satisfies coordinate-equality -- `diag_preimage_base`
closes by `rfl`, since the tower's inclusion preserves the underlying real
DEFINITIONALLY (`incl h y = <y.1, _>`).

Two things this deliberately does NOT do:

* It does not describe the diagonal as `Set.range diag`. That form would need
  `MeasurableSet (range diag)` -- measurability of a range, not generally
  provable and with no lemma to hand -- and would then have to be reconciled
  with `AJEscapingTower.base`, which is the coordinate-equality set. Going
  through `base` directly avoids both problems; `measurableSet_base` is already
  proved there.
* It does not abstract over an arbitrary inclusion. `diag^-1 base = univ`
  needs value-preservation, which is true of the tower's subtype inclusion and
  false for a general `incl`. Specializing keeps the step honest and `rfl`.

Combined with `ThickTraceGeneral.ajTrace_univ` (= 1 over the restricted base),
this is `full`.

Axiom-free: [propext, Classical.choice, Quot.sound].
-/
import QuerySystem.AndersenJessen
import QuerySystem
open MeasureTheory Set QuerySystem
open scoped ENNReal
namespace F2
variable (α : ℝ)

abbrev Lev (α : ℝ) (k : ℕ) : Type := ↥(AndersenJessen.X α k)
abbrev Out (n : ℕ) := (i : Fin (n+1)) → Lev α i

/-- The tower inclusion, value-preserving by construction. -/
def incl {m n : ℕ} (h : m ≤ n) (y : Lev α n) : Lev α m :=
  ⟨y.1, AndersenJessen.X_antitone α h y.2⟩

/-- The diagonal map into level `n`. -/
def diag (n : ℕ) (x : Lev α n) : Out α n := fun i => incl α (by omega) x

/-- The diagonal SET, as coordinate-equality (matching AJEscapingTower.base). -/
def base (n : ℕ) : Set (Out α n) := {x | ∀ i j, (x i).1 = (x j).1}

/-- **The key step, without `range`.** Every diagonal point satisfies
coordinate equality, so the preimage is everything. -/
theorem diag_preimage_base (n : ℕ) : diag α n ⁻¹' base α n = Set.univ := by
  ext x
  simp only [Set.mem_preimage, base, Set.mem_setOf_eq, Set.mem_univ, iff_true]
  intro i j
  rfl

theorem measurable_diag (n : ℕ) : Measurable (diag α n) :=
  measurable_pi_lambda _ (fun i => by
    rintro S ⟨E, hE, rfl⟩
    exact ⟨E, hE, rfl⟩)

/-- **`full`.** The diagonal carries all the mass. -/
theorem map_diag_base (mu : ∀ k, Measure (Lev α k)) (n : ℕ)
    (hbase : MeasurableSet (base α n)) :
    ((mu n).map (diag α n)) (base α n) = mu n Set.univ := by
  rw [Measure.map_apply (measurable_diag α n) hbase, diag_preimage_base]

#print axioms diag_preimage_base
#print axioms map_diag_base
end F2
