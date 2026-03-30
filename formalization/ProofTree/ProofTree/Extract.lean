import Lean
import Lean.Elab.InfoTree
import Lean.Server.InfoUtils

/-!
# ProofTree.Extract

Extracts a tactic proof structure from the elaboration `InfoTree` of a
theorem declaration, producing a `ProofTreeNode` tree that can be rendered
as a LaTeX natural deduction proof tree.

## Architecture

We use `InfoTree.foldInfoM` (from `Lean.Server.InfoUtils`) rather than walking
raw `Expr` terms. This handles the `PartialContextInfo → ContextInfo` merging
automatically and visits every `TacticInfo` node with its resolved `ContextInfo`.

Each `TacticInfo` node records:
- `goalsBefore / goalsAfter` : goal `MVarId`s before and after the tactic
- `mctxBefore / mctxAfter`   : metavar contexts for recovering goal types
- `stx`                      : the original tactic syntax (for labels)

Goal formulas and hypotheses are recovered by running `ppExpr` in a `MetaM`
context built from the `ContextInfo` and the goal's `LocalContext`.
-/

open Lean Elab Meta Server

namespace ProofTree

/-- A single node in the extracted proof tree. -/
structure ProofTreeNode where
  /-- Tactic label (e.g. "intro", "exact", "simp"). -/
  tactic     : String
  /-- Hypotheses in scope: (name, type-string) pairs. -/
  hyps       : List (String × String)
  /-- The main goal formula before this tactic. -/
  goalBefore : String
  /-- Goal formulas produced after this tactic (may split). -/
  goalsAfter : List String
  /-- Sub-trees for sub-goals discharged by this tactic. -/
  children   : List ProofTreeNode
  deriving Repr, Inhabited

-- ─── Expression → String ────────────────────────────────────────────────────

/--
Pretty-print an `Expr` to a string using the given `ContextInfo` and
`LocalContext`. Runs in `IO` via `ContextInfo.runMetaM`.
-/
def ppExprIO (ctx : ContextInfo) (lctx : LocalContext) (mctx : MetavarContext)
    (e : Expr) : IO String := do
  let fmt ← ctx.runMetaM lctx do
    -- Substitute the right mctx so metavars resolve correctly
    let s ← get
    set { s with mctx := mctx }
    let e' ← instantiateMVars e
    ppExpr e'
  return fmt.pretty 80

/-- Extract the tactic label from `Syntax`. Returns the last component of the
    elaborator kind, falling back to the raw pretty-print. -/
def tacticLabel (stx : Syntax) : String :=
  let raw := stx.prettyPrint.pretty 60
  let firstLine := (raw.splitOn "\n").headD raw
  let s := firstLine.replace "  " " "
  -- Manual truncation to avoid Slice API issues
  if s.length > 40 then
    (s.toList.take 40 |> String.ofList) ++ "…"
  else s

-- ─── Node construction ───────────────────────────────────────────────────────

/-- Build a `ProofTreeNode` (without children) from a `ContextInfo` + `TacticInfo`. -/
def buildNode (ctx : ContextInfo) (ti : TacticInfo) : IO ProofTreeNode := do
  -- Goal before
  let goalBefore ← match ti.goalsBefore.head? with
    | none => pure "⊢ ?"
    | some mvarId =>
      match ti.mctxBefore.findDecl? mvarId with
      | none     => pure "⊢ ?"
      | some decl =>
        let s ← ppExprIO ctx decl.lctx ti.mctxBefore decl.type
        pure s!"⊢ {s}"

  -- Hypotheses from the first goal's local context
  let hyps ← match ti.goalsBefore.head? with
    | none => pure []
    | some mvarId =>
      match ti.mctxBefore.findDecl? mvarId with
      | none => pure []
      | some decl =>
        let mut result : List (String × String) := []
        for ldecl in decl.lctx do
          if ldecl.isAuxDecl then continue
          let typeStr ← ppExprIO ctx decl.lctx ti.mctxBefore ldecl.type
          result := result ++ [(ldecl.userName.toString, typeStr)]
        pure result

  -- Goals after
  let goalsAfter ← ti.goalsAfter.mapM fun mvarId =>
    match ti.mctxAfter.findDecl? mvarId with
    | none     => pure "⊢ ?"
    | some decl => do
      let s ← ppExprIO ctx decl.lctx ti.mctxAfter decl.type
      pure s!"⊢ {s}"

  return {
    tactic     := tacticLabel ti.stx
    hyps       := hyps
    goalBefore := goalBefore
    goalsAfter := goalsAfter
    children   := []
  }

-- ─── InfoTree traversal ──────────────────────────────────────────────────────

/--
Collect all `(ContextInfo, TacticInfo)` pairs from an `InfoTree`, in
document order, using `foldInfoM` which handles context merging correctly.
-/
def collectTacticPairs (tree : InfoTree) : IO (List (ContextInfo × TacticInfo)) :=
  tree.foldInfoM (fun ctx info acc => do
    match info with
    | .ofTacticInfo ti =>
      -- Skip no-op nodes (where goals didn't change and tactic is trivial)
      return acc ++ [(ctx, ti)]
    | _ => return acc) []

/--
Build a flat list of `ProofTreeNode`s from an `InfoTree`.
Children are not yet nested — call `nestNodes` afterwards.
-/
def buildFlatNodes (tree : InfoTree) : IO (List ProofTreeNode) := do
  let pairs ← collectTacticPairs tree
  pairs.mapM fun (ctx, ti) => buildNode ctx ti

-- ─── Tree nesting (v1: flat, no nesting) ────────────────────────────────────

/--
In v1, we return the flat list as-is — each tactic step is a top-level node.
Proper nesting (consuming sub-goal subtrees) requires either bounded recursion
with a global fuel parameter or a stack-based algorithm; deferred to v2.

The flat list is still useful: the LaTeX renderer uses it as a linear
derivation chain (each step's conclusion feeds the next).
-/
def nestNodes (nodes : List ProofTreeNode) : List ProofTreeNode := nodes

end ProofTree
