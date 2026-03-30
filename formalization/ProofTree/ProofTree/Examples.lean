import ProofTree.Command

/-!
# ProofTree.Examples

Demonstration of `#prooftree` on small self-contained theorems.
These are chosen to exercise different tactic patterns:
- `intro` + `exact` (linear)
- `constructor` (goal splitting)
- `have` chains
- `rcases`

To use: open this file in VS Code with the Lean 4 extension.
Place your cursor after a `#prooftree` command to see the output
in the infoview, and find the generated `.tex` file alongside this file.
-/

namespace ProofTree.Examples

-- ─── Example 1: intro + exact (3 steps) ─────────────────────────────────────

theorem ex_modus_ponens (p q : Prop) (hp : p) (hpq : p → q) : q := by
  apply hpq
  exact hp

#prooftree ex_modus_ponens

-- ─── Example 2: constructor (goal split) ─────────────────────────────────────

theorem ex_and_intro (p q : Prop) (hp : p) (hq : q) : p ∧ q := by
  constructor
  · exact hp
  · exact hq

#prooftree ex_and_intro

-- ─── Example 3: have chain ────────────────────────────────────────────────────

theorem ex_transitivity (a b c : Nat) (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c := by
  have h3 : a ≤ b := h1
  exact Nat.le_trans h3 h2

#prooftree ex_transitivity

-- ─── Example 4: rcases + cases ───────────────────────────────────────────────

theorem ex_or_elim (p q r : Prop) (h : p ∨ q) (hp : p → r) (hq : q → r) : r := by
  rcases h with rfl | rfl
  · exact hp (by assumption)
  · exact hq (by assumption)

-- Note: rcases with rfl may not typecheck for general Props; simpler version:
theorem ex_or_elim' (p q r : Prop) (h : p ∨ q) (hp : p → r) (hq : q → r) : r := by
  cases h with
  | inl hp' => exact hp hp'
  | inr hq' => exact hq hq'

#prooftree ex_or_elim'

-- ─── Example 5: ebproof mode ──────────────────────────────────────────────────

theorem ex_simple_imp (p : Prop) (h : p) : p := by
  exact h

#prooftree ex_simple_imp mode:ebproof

-- ─── Example 6: depth limiting ───────────────────────────────────────────────

theorem ex_longer (p q r : Prop) (hp : p) (hq : q) (hr : r) : p ∧ q ∧ r := by
  constructor
  · exact hp
  · constructor
    · exact hq
    · exact hr

#prooftree ex_longer depth:2

end ProofTree.Examples
