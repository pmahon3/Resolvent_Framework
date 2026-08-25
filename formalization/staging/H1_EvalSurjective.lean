import QuerySystem
open Set Function MeasureTheory
namespace QuerySystem
/-
Now against the REAL definitions. Build the AJ-shaped system abstractly:
iota = N with <=, Outcome n = (i : Fin (n+1)) -> X i, pi = initial-segment
restriction. Then prove EvalSurjective from nonemptiness of each X k.
This is H1's claim, stated against `QuerySystem.Omega` / `eval` themselves.
-/
variable (X : ℕ → Type) [∀ k, MeasurableSpace (X k)]

abbrev Out (n : ℕ) := (i : Fin (n+1)) → X i
instance : ∀ n, MeasurableSpace (Out X n) := fun _ => inferInstance

def bond {m n : ℕ} (h : m ≤ n) (x : Out X n) : Out X m := fun i => x ⟨i.1, by omega⟩

lemma measurable_bond {m n : ℕ} (h : m ≤ n) : Measurable (bond X h) := by
  refine measurable_pi_lambda _ (fun i => ?_)
  exact measurable_pi_apply _

/-- the AJ-shaped query system -/
def AJsys : QuerySystem where
  ι := ℕ
  q := fun n => ⟨Out X n, inferInstance⟩
  le := (· ≤ ·)
  π := fun {m n} h => ⟨bond X h, measurable_bond X h⟩
  le_refl := fun _ => Nat.le_refl _
  le_trans := fun h h' => Nat.le_trans h h'
  π_refl := fun i => by funext x; funext j; rfl
  π_trans := fun hij hjk => by funext x; funext j; rfl

/-- **H1.** Every `eval n` is surjective, given each `X k` nonempty. -/
theorem AJ_evalSurjective (hne : ∀ k, Nonempty (X k)) :
    (AJsys X).EvalSurjective := by
  classical
  intro n a
  let g : ∀ k, X k := fun k => if h : k ≤ n then a ⟨k, by omega⟩ else (hne k).some
  refine ⟨⟨fun m => fun i => g i.1, ?_⟩, ?_⟩
  · intro m n' h; rfl
  · funext i
    show g i.1 = a i
    simp only [g]
    rw [dif_pos (by omega : i.1 ≤ n)]

-- receipts + non-vacuity
#print axioms QuerySystem.AJ_evalSurjective
-- the system is real: Omega is inhabited when each X k is
example (hne : ∀ k, Nonempty (X k)) : Nonempty (AJsys X).Omega := by
  classical
  exact ⟨⟨fun m => fun i => (hne i.1).some, fun h => rfl⟩⟩
-- and eval is genuinely the coordinate map (not a junk def)
example (n : ℕ) (w : (AJsys X).Omega) : (AJsys X).eval n w = w.1 n := rfl

end QuerySystem
