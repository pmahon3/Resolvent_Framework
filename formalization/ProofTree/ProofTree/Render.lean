import ProofTree.Extract

/-!
# ProofTree.Render

Renders a `ProofTreeNode` tree as LaTeX, in either `bussproofs` or `ebproof` format.

## Unicode → LaTeX substitution

`ppExpr` outputs Unicode. We apply a post-processing pass converting common
mathematical Unicode to LaTeX macros so the output compiles cleanly.

## bussproofs format

Rules: `\AxiomC`, `\UnaryInfC`, `\BinaryInfC`, `\TrinaryInfC`, `\RightLabel`.
Premises are emitted before their conclusion (bottom-up tree order).

## ebproof format

Rules: `\hypo`, `\infer0`, `\infer1`, `\infer2`, etc., with optional label.
Wrapped in `\begin{prooftree} ... \end{prooftree}`.
-/

namespace ProofTree

/-- Render mode. -/
inductive Mode where
  | bussproofs
  | ebproof
  deriving Repr, Inhabited

-- ─── Unicode → LaTeX ─────────────────────────────────────────────────────────

/-- Convert Unicode characters from `ppExpr` to LaTeX math commands. -/
def unicodeToLatex (s : String) : String :=
  s
  |>.replace "∀" "\\forall "
  |>.replace "∃" "\\exists "
  |>.replace "→" "\\to "
  |>.replace "↔" "\\leftrightarrow "
  |>.replace "∧" "\\land "
  |>.replace "∨" "\\lor "
  |>.replace "¬" "\\lnot "
  |>.replace "⊢" "\\vdash "
  |>.replace "≤" "\\leq "
  |>.replace "≥" "\\geq "
  |>.replace "≠" "\\neq "
  |>.replace "∈" "\\in "
  |>.replace "∉" "\\notin "
  |>.replace "⊆" "\\subseteq "
  |>.replace "⊂" "\\subset "
  |>.replace "∩" "\\cap "
  |>.replace "∪" "\\cup "
  |>.replace "∅" "\\emptyset "
  |>.replace "σ" "\\sigma "
  |>.replace "μ" "\\mu "
  |>.replace "ν" "\\nu "
  |>.replace "α" "\\alpha "
  |>.replace "β" "\\beta "
  |>.replace "ω" "\\omega "
  |>.replace "Ω" "\\Omega "
  |>.replace "ℕ" "\\mathbb{N}"
  |>.replace "ℤ" "\\mathbb{Z}"
  |>.replace "ℚ" "\\mathbb{Q}"
  |>.replace "ℝ" "\\mathbb{R}"
  |>.replace "ℂ" "\\mathbb{C}"
  |>.replace "↦" "\\mapsto "
  |>.replace "λ" "\\lambda "
  |>.replace "⟨" "\\langle "
  |>.replace "⟩" "\\rangle "

/-- Escape special LaTeX characters in plain text (for tactic labels). -/
def latexEscape (s : String) : String :=
  s
  |>.replace "_" "\\_"
  |>.replace "%" "\\%"
  |>.replace "&" "\\&"
  |>.replace "#" "\\#"

/-- Format a sequent: `hyp₁ : T₁, …  ⊢ goal`. -/
def formatSequent (hyps : List (String × String)) (goal : String) : String :=
  let hypStr :=
    if hyps.isEmpty then ""
    else
      let items := hyps.map fun (n, t) =>
        unicodeToLatex n ++ " : " ++ unicodeToLatex t
      (", ".intercalate items) ++ " "
  hypStr ++ unicodeToLatex goal

-- ─── LaTeX string helpers ────────────────────────────────────────────────────
-- We use ++ concatenation to avoid s-string parsing issues with $ and {}.

private def mathMode (s : String) : String := "$" ++ s ++ "$"
private def cmdArg (s : String) : String := "{" ++ s ++ "}"
private def optArg (s : String) : String := "[" ++ s ++ "]"
private def ttCmd (s : String) : String := "\\texttt" ++ cmdArg s
private def rightLabel (s : String) : String := "\\RightLabel" ++ cmdArg (ttCmd s)

-- ─── bussproofs renderer ─────────────────────────────────────────────────────

/-- Render one node in bussproofs format. Children are rendered first (premises). -/
partial def renderBuss (node : ProofTreeNode) (depth : Nat) : String :=
  if depth = 0 then
    let seq := formatSequent node.hyps node.goalBefore
    "\\AxiomC" ++ cmdArg (mathMode "\\vdots") ++ "\n" ++
    "\\UnaryInfC" ++ cmdArg (mathMode seq) ++ "\n"
  else
    let childStrs := node.children.map (renderBuss · (depth - 1))
    let premises := childStrs.foldl (· ++ ·) ""
    let conc := formatSequent node.hyps node.goalBefore
    let lbl := latexEscape node.tactic
    let n := node.children.length
    if n = 0 then
      "\\AxiomC" ++ cmdArg (mathMode conc) ++ "\n"
    else if n = 1 then
      premises ++
      rightLabel lbl ++ "\n" ++
      "\\UnaryInfC" ++ cmdArg (mathMode conc) ++ "\n"
    else if n = 2 then
      premises ++
      rightLabel lbl ++ "\n" ++
      "\\BinaryInfC" ++ cmdArg (mathMode conc) ++ "\n"
    else if n = 3 then
      premises ++
      rightLabel lbl ++ "\n" ++
      "\\TrinaryInfC" ++ cmdArg (mathMode conc) ++ "\n"
    else
      premises ++
      rightLabel (lbl ++ " (" ++ toString n ++ " goals)") ++ "\n" ++
      "\\UnaryInfC" ++ cmdArg (mathMode conc) ++ "\n"

/-- Wrap bussproofs body in `\begin{prooftree}...\end{prooftree}`. -/
def wrapBuss (inner : String) : String :=
  "\\begin{prooftree}\n" ++ inner ++ "\\end{prooftree}"

-- ─── ebproof renderer ────────────────────────────────────────────────────────

/-- Render one node in ebproof format. -/
partial def renderEbproof (node : ProofTreeNode) (depth : Nat) : String :=
  if depth = 0 then
    let seq := formatSequent node.hyps node.goalBefore
    "\\hypo" ++ cmdArg (mathMode seq) ++ "\n"
  else
    let childStrs := node.children.map (renderEbproof · (depth - 1))
    let premises := childStrs.foldl (· ++ ·) ""
    let conc := formatSequent node.hyps node.goalBefore
    let lbl := latexEscape node.tactic
    let n := node.children.length
    if n = 0 then
      "\\hypo" ++ cmdArg (mathMode conc) ++ "\n" ++
      "\\infer0" ++ optArg (ttCmd lbl) ++ cmdArg (mathMode conc) ++ "\n"
    else
      premises ++
      "\\infer" ++ toString n ++ optArg (ttCmd lbl) ++
      cmdArg (mathMode conc) ++ "\n"

/-- Wrap ebproof body in `\begin{prooftree}...\end{prooftree}`. -/
def wrapEbproof (inner : String) : String :=
  "\\begin{prooftree}\n" ++ inner ++ "\\end{prooftree}"

-- ─── Top-level ───────────────────────────────────────────────────────────────

/-- Configuration for rendering. -/
structure RenderConfig where
  mode  : Mode := .bussproofs
  depth : Nat  := 20
  deriving Repr, Inhabited

/-- Render a list of root nodes to a LaTeX proof tree. -/
def render (roots : List ProofTreeNode) (cfg : RenderConfig := {}) : String :=
  match cfg.mode with
  | .bussproofs =>
    let inner := roots.map (renderBuss · cfg.depth) |>.foldl (· ++ ·) ""
    wrapBuss inner
  | .ebproof =>
    let inner := roots.map (renderEbproof · cfg.depth) |>.foldl (· ++ ·) ""
    wrapEbproof inner

/-- Produce a complete standalone LaTeX document. -/
def renderDocument (roots : List ProofTreeNode) (thmName : String)
    (cfg : RenderConfig := {}) : String :=
  let pkg := match cfg.mode with
    | .bussproofs => "bussproofs"
    | .ebproof    => "ebproof"
  let tree := render roots cfg
  "\\documentclass{article}\n" ++
  "\\usepackage{amsmath,amssymb}\n" ++
  "\\usepackage{" ++ pkg ++ "}\n" ++
  "\\begin{document}\n\n" ++
  "\\noindent\\textbf{Theorem:} \\texttt{" ++ latexEscape thmName ++ "}\n\n" ++
  "\\bigskip\n\n" ++
  tree ++ "\n\n" ++
  "\\end{document}\n"

end ProofTree
