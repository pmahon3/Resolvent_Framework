/-
Probe: can the model arm close CONSTRUCTIVE goals -- ones needing a witness --
as opposed to deductive ones? Every goal below is a membership claim whose proof
is an anonymous constructor. These are exactly the shapes grind scored 0/8 on
with the automation arm; that run never invoked the model.
-/
import Mathlib.NumberTheory.Real.Irrational

namespace Probe
variable (α : ℝ)

def A : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α}
def B (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ Even n}

theorem p1 {x : ℝ} (hx : x ∈ B α 0) : x ∈ A α := by sorry
theorem p2 {x y : ℝ} (hx : x ∈ A α) (hy : y ∈ A α) : x - y ∈ A α := by sorry
theorem p3 {k : ℕ} {x : ℝ} (hx : x ∈ B α k) : -x ∈ B α k := by sorry
theorem p4 : (0 : ℝ) ∈ A α := by sorry
theorem p5 : Antitone (B α) := by sorry

end Probe
