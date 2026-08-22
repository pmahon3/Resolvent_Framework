import Mathlib.NumberTheory.Real.Irrational

namespace Probe
variable (α : ℝ)

def A : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α}
def B (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ Even n}

-- proofs produced by the model, spliced verbatim
theorem p1 {x : ℝ} (hx : x ∈ B α 0) : x ∈ A α := by
  unfold A B at * ; obtain ⟨n, m, h, _, _⟩ := hx ; tauto

theorem p3 {k : ℕ} {x : ℝ} (hx : x ∈ B α k) : -x ∈ B α k := by
  simp [B, Set.mem_Ioc, neg_sub, neg_neg] at * ; obtain ⟨n, ⟨y, rfl⟩, hn, hn'⟩ := hx ; refine ⟨-n, ⟨-y, ?_⟩, ?_⟩ <;> simp [hn, hn', abs_neg, even_neg] ; ring

theorem p4 : (0 : ℝ) ∈ A α := by
  simp [A, Set.mem_Icc] ; exact ⟨0, 0, by simp [add_zero]⟩

end Probe
