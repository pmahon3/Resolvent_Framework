/-
# Unit 2: the projective system over the Andersen-Jessen tower

Unit 2 of `notes/open_questions/aj_tower/SCOPE_trace_projective_layer.md`.

**Finding: unit 2 already existed.** The scope doc proposed encoding
`Outcome n` as `X_0 x ... x X_n`. The right shape was already built and
machine-checked in `staging/H1_EvalSurjective.lean` for the H1 surjectivity
check: `Out X n := (i : Fin (n+1)) -> X i` with the bonding maps as
initial-segment restrictions. That IS the projective system, and it is
instantiated here at the tower levels. `pi_refl` and `pi_trans` discharge by
`rfl`, exactly as they did in H1.

`AJ_evalSurjective` (H1) already proves `EvalSurjective` for this shape given
each level nonempty -- so that hypothesis of the extension theorem is available
here for free.

Levels are confined to `[0,1]`: see `ThickTrace.ajThickIn` for why (thickness
in all of `R` is incompatible with confinement, and the contents need mass 1).

Axiom-free: [propext, Classical.choice, Quot.sound].
-/
import QuerySystem.AndersenJessen
import QuerySystem
open MeasureTheory Set QuerySystem
namespace U2
variable (α : ℝ)

/-- The tower's levels, confined to [0,1], as types. -/
abbrev Lev (α : ℝ) (k : ℕ) : Type := ↥(AndersenJessen.X α k ∩ Set.Icc 0 1)

-- do they carry MeasurableSpace?
example (k : ℕ) : MeasurableSpace (Lev α k) := inferInstance

-- H1's Out / bond / AJsys, instantiated here
abbrev Out (n : ℕ) := (i : Fin (n+1)) → Lev α i
def bond {m n : ℕ} (h : m ≤ n) (x : Out α n) : Out α m := fun i => x ⟨i.1, by omega⟩

lemma measurable_bond {m n : ℕ} (h : m ≤ n) : Measurable (bond α h) := by
  refine measurable_pi_lambda _ (fun i => ?_)
  exact measurable_pi_apply _

/-- **Unit 2: the projective system.** Exactly H1's `AJsys` shape. -/
def AJtowerSys : QuerySystem where
  ι := ℕ
  q := fun n => ⟨Out α n, inferInstance⟩
  le := (· ≤ ·)
  π := fun {m n} h => ⟨bond α h, measurable_bond α h⟩
  le_refl := fun _ => Nat.le_refl _
  le_trans := fun h h' => Nat.le_trans h h'
  π_refl := fun i => by funext x; funext j; rfl
  π_trans := fun hij hjk => by funext x; funext j; rfl



#print axioms AJtowerSys
end U2
