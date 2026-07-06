# Witness candidate — the Product Ulam Carrier (VERIFIED 2026-07-06, gates owed)

**VERIFICATION CLEARED + MACHINE-CHECKED 2026-07-06 — see `VERIFICATION_VERDICT.md`
(the authoritative record; outcome (i), qualified).** No mathematical error found by
two independent adversarial passes + mechanical finite-core enumeration; then the
construction was **formalized end-to-end in Lean the same day**: `psiAmended_ZFC`
(`formalization/QuerySystem/QuerySystem/UlamWitnessMain.lean`), zero sorries, axioms
exactly `[propext, Classical.choice, Quot.sound]`. The Ω₇ amendment-forcing example
is also machine-checked (`Omega7Counterexample.lean`). Remaining before promotion:
the definitional-fidelity read (~15 min, Lean defs vs v2 Defs 1.2–1.4), gate β
(prior-art book check: Pták–Pulmannová 1991, Navara's Handbook survey), and Phase-2
`/audit full`. Keep v1 (`../sigma_essential.tex`) frozen except the Ω₇/Prop 2.1
erratum, which is owed regardless. The v2 body's "Lean formalization in progress"
caveat paragraph can now be updated to cite the completed formalization.

A **candidate ZFC construction** of a σ-essential contextual state, resolving an
**amended** form of the open problem. Produced 2026-07-06 in a working session
(claude.ai/share/059e292f-97f0-4787-808e-c89a88dbced4).

## Files
- `sigma_essential_v2.tex` + `sigma_essential_v2_body.tex` + `references.bib` — the full
  integrated paper (localization + boundary map + the new witness), builds clean
  (`latexmk -pdf sigma_essential_v2.tex`, 0 unresolved refs). This is a proposed
  **replacement** for `../sigma_essential.tex`, not a companion.
- `sigma_essential_witness.md` / `.pdf` — the standalone technical writeup of the witness
  construction only (§0–§9), with the author's own §8 "verification map" ranking the
  load-bearing joints by residual suspicion.

## What is claimed
A concrete σ-complete non-Boolean orthomodular **poset** (NOT lattice) `L` on
`Ω = ω₁ × {1,2,3,4}`, with a finite 2-valued pattern `s₀` (a Specker triple of "core"
events `A,B,C`, `A∩B∩C = ∅`) that:
1. is **finitely coherent** (extends to a global finitely-additive 2-valued state `m`,
   built from an ultrafilter on `P(ω₁)/ctble` via a parity-code "vote"), yet
2. extends to **no** σ-additive 2-valued state (rigidity: an Ulam matrix as generators
   makes every σ-additive 2-valued state Dirac; the empty kernel kills every Dirac).

⟹ Ψ (amended) holds in **ZFC** — no large-cardinal strength. The literal OML/lattice
form stays open (§9), conjectured to FAIL (latticehood forces σ-liftability).

## ⚠ The two things verification must decide (see handoff)
1. **Does the amendment preserve the problem, or dodge the wall?** Three amendments:
   (a) finite coherence read GLOBALLY (Def: `s₀` extends to a finitely-additive state) —
   Rem 1.5/`rem:amendment` argues this is FORCED (the literal reading makes [M Prop 2.1]
   false); (b) carrier is an OMP not a lattice (`A∧B` doesn't exist, Cor 4.4);
   (c) irreducibility mod the countable ideal (Prop 7.2/`rem:irreducibility-amended`
   argues literal irreducibility is unavailable to ANY singleton-containing carrier, so
   forced by the method). Each must be judged: forced, or convenient-weakening?
2. **Is `Dirac-only + K(s₀)=∅` a GENUINE witness or the DEGENERATE case?** This is the
   crux vs. the prior programme. Our Lean `diracOnly_with_clause_i_gives_witness` already
   PROVES this path is a valid witness of the FORMALIZED definition — so by the in-repo
   formalization it is genuine. BUT the prior sessions called Dirac-domination
   "degenerate," and Rem 7.3/`rem:quotient` openly states the quotient has NO σ-additive
   2-valued state at all (the vacuous/bisection shape). Reconcile: is the paper's Ψ the
   same Ψ the programme was chasing, or the degenerate sibling the tree-detector flagged?

## Relation to the prior recorded terminus
This **contradicts** the recorded conclusion ("frontier is human mathematics, not close;
every importable object → Wall A"). Either (a) it's a genuine breakthrough that the
amendment legitimately unlocks, or (b) the amendment relocates the problem past the wall
(the witness lives in the OMP-not-lattice + global-coherence + mod-countable regime the
prior programme's Ψ excluded). Verification decides which. Do NOT update the authoritative
frontier (`program_overview.md`) to "SOLVED" until the checklist clears.
