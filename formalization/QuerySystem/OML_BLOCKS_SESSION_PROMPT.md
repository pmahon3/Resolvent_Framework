# Session prompt: Lean formalization of the concrete-OML block layer

**Paste-able starter for a fresh session. Written 2026-07-11 end of s16;
audit of existing Lean infrastructure already done — reuse it, do not
re-audit.**

## Goal and why

The user cannot confidently hand-ratify the s11–s16 OML-attack math
(ratification kit: `notes/open_questions/kits/ratification_kit_2026-07-11.pdf`).
Formalize the load-bearing chain so ratification rests on Lean instead
of hand-checking. Priority = ratification leverage:

- **Phase A** discharges kit item 2 gaps 2.2–2.5 (A1, L0-bridge,
  monotonicity, T3 prerequisites) — fully provable, no axioms.
- **Phase B** discharges gap 2.1 (A2, the biggest single gap: blocks
  are σ-fields, ∩-closed — needs Foulis–Holland/commutant closure).
- **Phase C** discharges kit item 4 gaps 4.1/4.5 (P⁼, cluster normal
  form, 2BR, Φ-density; T4 + B′(i) as open `Prop`s — the conjecture
  harness) and the owed pattern re-encoding fix.
- **Phase D** (optional, later): kit item 3 (theorem-lets R and P;
  needs Polish/perfect-set topology — Mathlib has it).

Math source of record: `notes/open_questions/oml_attack/oml_lattice_regularity_attack.md`
§§9, 11 (all statements proof-read SOUND at s12 standard — receipts
`PROOF_READ_2026-07-10_attack_s9.md`, `PROOF_READ_2026-07-11_attack_s11.md`
in the same folder). Definitions for the reduction ladder are also
collected reviewer-grade in
`notes/open_questions/verification/proof_read_2026-07-11_s15/` scripts'
docstrings and the statements file referenced by the s16 receipt.

## Existing infrastructure (audited 2026-07-11 — REUSE)

Project: `formalization/QuerySystem/` (Lean 4 + Mathlib, builds; run
`lake build` from that directory; mathlib is compiled in `.lake`).

- **σ-class carrier** = Mathlib's `MeasurableSpace.DynkinSystem Ω`
  (complement + countable pairwise-disjoint unions). Used everywhere:
  `variable (d : DynkinSystem Ω)`; membership `d.Has A`; API used in
  repo: `d.has_empty`, `d.has_compl`, `d.has_diff` (diff of nested
  sets). `Carrier d := {A | d.Has A}` in `SigmaEssentialLocalization.lean:28`.
- **`TwoValuedState d`** (`SigmaEssentialLocalization.lean:36`):
  two-valued **σ-additive** state — `Val : Set Ω → Prop`, `decVal`,
  `val_univ`, `not_val_empty`, `val_compl` (iff-form), `val_iUnion`
  (union true ↔ some member true, over ℕ-indexed pairwise-disjoint
  families in `d`). `dirac ω` at line 58; `IsDirac` line 67. Derived:
  `val_union`, monotonicity (see the fidelity block starting line 69).
- **`FinAddState d`** (`SigmaEssentialAmended.lean:45`): two-valued
  **finitely additive** state (same fields, pair-additivity
  `val_union` instead of `val_iUnion`). Derived already: `val_mono`
  (line 67), `val_at_most_one` (75), `val_inter` on an
  intersection-closed carrier (85, uses spine predicate `InterClosed d`).
  This is St_fa. St_σ = `TwoValuedState`.
- ⚠ **Name collision:** `Block d` (`SigmaEssentialLocalization.lean:163`)
  is ALREADY TAKEN — it means a finite ⊥-closed pattern (a `Finset` of
  sets, complement-closed), with `Extends s s₀ B`, `kernel`,
  `IsSigmaEssential` built on it. For maximal compatible families use a
  different name (suggest `MaxBlock`).
- ⚠ **Known defect (do not repeat):** `EncodingDefectCheck.lean`
  proved the old witness-predicate encoding FALSE — patterns must be
  encoded as a LOCAL state on `B` (a value assignment on the pattern's
  sets), never as a global state that happens to be restricted. The fix
  is owed (`formalization_status` memory); Phase C's pattern work
  should implement it.
- Style: every file opens with a header stating what is proved vs
  cited vs open; receipts via `#print axioms` at file end; open
  problems as named `Prop`s (never `sorry`); cited-literature facts as
  `axiom` with citation comment (feedback_lean_triangulation).

## Design decisions (already made — follow unless they break)

1. **Compatibility is concrete:** `Compat d A B := d.Has (A ∩ B)`.
   Justification = L0 (attack note §9c): on σ-class OMLs concrete and
   lattice compatibility coincide. Derive immediately:
   `compat_of_disjoint` (∅ ∈ d), symmetry, and the decomposition
   `d.Has A → d.Has B → Compat d A B → d.Has (A \ B)`
   (via `A \ B = (Aᶜ ∪ (A∩B))ᶜ`, a disjoint union).
2. **`MaxBlock d`** := maximal element of
   `{F : Set (Set Ω) | F ⊆ Carrier d ∧ F.Pairwise (Compat d)}`.
   Existence/extension (A1a) via `zorn_subset_nonempty` (chain unions
   of pairwise-compat families are pairwise-compat: any two members
   share a chain link).
3. **Latticehood enters only where needed** (Phase B+): as a
   hypothesis `MeetsExist d` := for all `A B ∈ Carrier d` there is a
   `⊆`-greatest element of `Carrier d` inside `A ∩ B`. Do NOT build an
   abstract OML class; stay concrete.
4. **Phase A theorem list** (attack note §9b/§11, all
   machine-corroborated + proof-read):
   - A1a (extension to a MaxBlock, Zorn);
   - A1b: a MaxBlock contains ∅ and univ, is complement-closed, and is
     closed under countable pairwise-disjoint unions (the ⊍-closure
     argument: `u ∩ b = ⊍ (cₙ ∩ b)`, then maximality);
   - A1c: `s : FinAddState d` satisfies the σ-condition globally iff
     it does on every MaxBlock (⟸ needs: any ℕ-indexed disjoint family
     in `d` together with its union is pairwise-Compat, hence extends
     to a MaxBlock by A1a);
   - monotonicity is ALREADY DONE (`FinAddState.val_mono`) — the s16
     strengthening (no OML needed) is thus already the formal form;
   - C1′ (|V| ≤ 2 Dirac rescue, no lattice): if `μ : FinAddState d`,
     `μ.Val A`, `μ.Val B`, then `(A ∩ B).Nonempty` (else disjoint and
     `val_at_most_one` contradicts), and any `ω ∈ A ∩ B` has
     `dirac ω` agreeing with the pattern on `{A, B}` + complements.
5. **Phase B:** commutant closure: if `C` is Compat with `A` and `B`
   (all in `d`, meets exist), then `C` is Compat with `A ∩ B` —
   this is the Foulis–Holland/Bruns–Harding step. FIRST attempt a
   direct concrete proof (the set identity
   `A ∩ B ∩ C` decompositions using the Compat splittings of A, B
   along C — try `(A∩B)∩C = (A∩C)∩(B∩C)` with d-membership chased
   through the compat decompositions; if A↔C and B↔C then A∩C, B∩C ∈ d
   and their intersection... this is where the real content is). If the
   direct route stalls, take
   `axiom foulis_holland ...` with citation (Kalmbach 1983 Thm 5 p.25 /
   Bruns–Harding 2000 Prop 2.8) and FLAG it in the file header — the
   ratification story must say which. Then: A2 = MaxBlocks are
   ∩-closed σ-fields; T3 (Dirac realization on countably generated
   MaxBlocks — statement in §9c, proof re-derived in the s12 receipt).
6. **Phase C:** re-encode patterns as local states (owed fix);
   theorem-lets 2BR, cluster normal form, P⁼ (§11a–c); Φ-density
   (§11d) — state `Phi d` as a `Prop` over local patterns; `BPrimeI`
   and `T4` as named open `Prop`s; prove the ladder equivalences
   `BPrimeI ↔ cluster-selection form ↔ density form` and
   `BPrimeI → T4`. `#print axioms` receipts for everything.

## Session protocol

- Work in `formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean`
  (new file; add to the lakefile/root import as the project does for
  other modules — check `QuerySystem.lean`).
- Build early, build often (`lake build`); never end the session with
  a broken build; no `sorry` — trim scope instead (Phase A alone is a
  fine session outcome).
- lean-reviewer agent exists (`.claude/agents/`) for Mathlib API hunts
  if invocable; otherwise search `.lake/packages/mathlib` directly
  (e.g. `zorn_subset_nonempty` in `Mathlib/Order/Zorn.lean`).
- On completion: update `formalization_status` memory topic file +
  MEMORY hook (Lean bolster status), taxonomy `lean` certificate
  fields where a banked theorem-let becomes machine-checked, and the
  ratification kit's item-2/item-4 sections (mark gaps discharged by
  Lean, recompile the PDF). Commit with receipts.
- The point is RATIFICATION LEVERAGE: after Phase A+B the user ratifies
  item 2 by reading two `#print axioms` outputs instead of re-deriving
  T3 by hand. Keep that framing in the status updates.
