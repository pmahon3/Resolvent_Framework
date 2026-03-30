import ProofTree.Extract
import ProofTree.Render
import Lean.Elab.Command
import Lean.Elab.InfoTree

/-!
# ProofTree.Command

Provides the `#prooftree` command.

## Usage

```lean
#prooftree myTheorem
#prooftree myTheorem mode:ebproof
#prooftree myTheorem mode:bussproofs depth:5
```

## Limitation (v1)

`#prooftree` must appear in the **same file** as the theorem.
The InfoTree is only available during elaboration of that file.
-/

open Lean Elab Command ProofTree

namespace ProofTree

-- ─── Syntax ──────────────────────────────────────────────────────────────────

-- Optional arguments use `ident` to avoid registering new keywords.
-- Supported forms: `bussproofs`, `ebproof`, or a numeric depth limit.
syntax prooftreeOpt := ident <|> num

syntax (name := prooftreeCmd) "#prooftree" ident (prooftreeOpt)* : command

-- ─── Argument parsing ────────────────────────────────────────────────────────

private def chooseMode (args : Array Syntax) : Mode :=
  args.foldl (init := .bussproofs) fun acc arg =>
    match arg.isIdOrAtom? with
    | some "ebproof"    => .ebproof
    | some "bussproofs" => .bussproofs
    | _ => acc

private def chooseDepth (args : Array Syntax) : Nat :=
  args.foldl (init := 20) fun acc arg =>
    if arg.isNatLit? != none then
      arg.toNat
    else acc

-- ─── Elaborator ──────────────────────────────────────────────────────────────

@[command_elab prooftreeCmd]
def elabProoftree : CommandElab := fun stx => do
  let thmIdent := stx[1]
  let opts     := stx[2].getArgs

  -- Resolve the theorem name
  let thmName ← liftCoreM <| Lean.Elab.realizeGlobalConstNoOverloadWithInfo thmIdent

  let renderMode  := chooseMode opts
  let renderDepth := chooseDepth opts

  -- Collect InfoTrees built so far in this file
  let trees ← getInfoTrees

  -- Extract flat node list from all trees (IO lifted into CommandElabM)
  let allNodes ← liftM (m := IO) (do
    let nodeLists ← trees.toList.mapM buildFlatNodes
    pure nodeLists.flatten)

  if allNodes.isEmpty then
    logWarning s!"#prooftree: no tactic info found for '{thmName}'. \
      Ensure #prooftree is in the same file as the theorem \
      and that the proof uses tactic mode."
    return

  let roots := nestNodes allNodes
  let cfg   : RenderConfig := { mode := renderMode, depth := renderDepth }
  let doc   := renderDocument roots thmName.toString cfg

  -- Display in infoview
  logInfo doc

  -- Write .tex file next to the source
  let srcFile := (← read).fileName
  -- Drop the ".lean" suffix (5 chars) to get the stem
  let stem : String :=
    if srcFile.endsWith ".lean" then
      srcFile.toList.reverse.drop 5 |>.reverse |> String.ofList
    else srcFile
  let outPath : System.FilePath := stem ++ "_" ++ thmName.toString ++ ".tex"
  liftM (m := IO) (IO.FS.writeFile outPath doc)
  logInfo s!"Written: {outPath}"

end ProofTree
