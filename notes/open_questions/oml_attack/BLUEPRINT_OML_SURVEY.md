# What is formalized on the OML/OMP side, and what a blueprint can honestly say

**Written 2026-08-24.** Survey + rendering-mechanics verification. No new math.
Purpose: the blueprint currently covers the *classical* (distributive) runway;
the OML/OMP frontier is almost entirely outside it. This is the map for fixing that.

## Coverage today

18/46 modules appear in the blueprint. The OML/OMP core is in the 28 that do not:
`OrthomodularMO2`, `ConcreteOMLBlocks`, `ConcreteOMLPatterns`, `ODBCRegimes`,
`ODBCSections`, `InnerRegularity`, `MarczewskiTransport`, `SigmaEssentialOpenCore`,
`SigmaEssentialBareForm`, `SigmaEssentialConjectures`, `BandClosure`,
`BoundaryDescent`, `KernelClosureCalculus`, `UlamWitnessReceipts`, and the
reconstruction cluster (`Commensurability`, `WindingDichotomy`, `ReconstructionTheorem`,
`DelayEmbedding`, …).

## Axiom census over the OML/OMP cluster (24 modules)

`#print axioms` over every public theorem in those modules:

- **305 clean** (`[propext, Classical.choice, Quot.sound]` only)
- **11 resting on repo-local axioms**
- **0 unexplained** (8 further names are `private`, hence not blueprint candidates;
  5 initially-unresolved names were namespace-parse artifacts and are all clean)

### The 11, and why they are three DIFFERENT kinds

Rendering these uniformly would make the blueprint lie. They are:

**(A) Cited results — legitimate per CLAUDE.md ("Don't formalize known results.
Use `axiom` with citation"). NOT gaps.**
- `dw_polish_no_witness` — Derr–Williamson 2023, Thm D.6
- `fw_abstract_sigma_free` — Feldman–Wilce, Thm 4.7
- `navara_ptak_kernel_empty` — Navara–Pták

**(B) Open-problem markers / deliberate abstractions.**
- `MeasurableExists` — stand-in for "a measurable cardinal exists" (strength axis)
- `PolishRepresentable`, `AbstractSigmaOrtho` — cited predicates, abstract by design

**(C) Genuine stubs — the honest gaps.**
- `IsConcrete`, `IsSigmaComplete`, `IsIrreducible`, `IsNonSegregated` — the four
  "not-yet-Lean-proved admissibility predicates"
- `slab0_not_mem` — §3 Normal Form, proved on paper, not re-proved in Lean

⚠ **Fidelity consequence that must survive into the blueprint:** `IsIrreducible`
being an unconnected stub is why `Psi` omits essential irreducibility and is
**strictly weaker than the paper's Ψ** (`FIDELITY_REVIEW.md`). A blanket `\leanok`
over this cluster would erase that.

## Rendering convention — VERIFIED, not assumed

Probed on a throwaway node, rendered, then reverted:

`\lean{...}` **with no** `\leanok` renders as `color=green, no fillcolor` — per the
legend, "the statement of this result is formalized" with the proof NOT formalized.
That is semantically exact for an axiom. No theme hacking needed.

Also confirmed: `checkdecls.sh` accepts an axiom name (it `#check`s, and an axiom
is a constant), so category (A)/(B) nodes pass the existing gate unchanged.

**So the taxonomy is expressible today:**
| kind | blueprint rendering |
|---|---|
| proved theorem | `\lean{}` + `\leanok` on statement and proof |
| cited axiom (A) | `\lean{}`, NO `\leanok`, citation in the statement text |
| abstraction (B) | `\lean{}`, NO `\leanok`, marked as a deliberate abstraction |
| stub (C) | `\lean{}`, NO `\leanok`, named as an open obligation |

## The distributive / non-distributive axis IS the spine

The pivot is already formalized and is a single predicate:

`SigmaEssentialLocalization.lean:329` —
`InterClosed d := ∀ {A A'}, d.Has A → d.Has A' → d.Has (A ∩ A')`
with the docstring: "A Dynkin system with this property is exactly a σ-algebra (π–λ)."

So: **σ-class + intersection-closure = Boolean/distributive; drop it = orthomodular.**

And the axis is load-bearing, not decorative. `TwoValuedState.val_inter`'s docstring:

> "This is the only place distributivity (lattice-meet = set-intersection, i.e.
> `InterClosed`) is used — exactly the step that fails on a non-Boolean OML."

The distributive case is *closed*: `boolean_baseline` (Prop 1.6) and
`boolean_no_witness` (Prop 2.1) prove a Boolean carrier admits NO
σ-essential witness. The non-distributive case is where the witness lives
(`UlamWitness*`) and where Φ stays open (`rmk:phi-open`).

That is exactly the runway/frontier contrast: classical distributive material as
preparation, the orthomodular case as the destination.

## Caveat on chapter wiring

The existing blueprint's chapters are near-disconnected (only ch0→ch1 carries real
edges; ch2/3/4 have no incoming mathematical dependencies). Adding OML chapters will
NOT automatically fix that — a cross-chapter edge requires a real Lean dependency,
not a prose reference. Checked: `ConcreteOMLBlocks` imports `SigmaEssentialWitness`
→ `SigmaEssentialLocalization` → Mathlib only. `OrthomodularMO2` imports Mathlib only.
**No OML module imports ch0/ch1.** So the OML chapters will form their own connected
component unless a genuine dependency is written.

## Not settled here (needs the user)

- Whether `PruningTheorem`/`TheoremB` (ch4) and the reconstruction cluster stay in
  this restructure — that is reconstruction material, not OML.
- Which nodes make the spine vs. get left to the coverage ratchet. 313 theorems
  across 24 modules against the current blueprint's 84 nodes: this must be a
  SPINE, not an index.
- Adding modules moves `coverage_baseline.txt` off 28; regenerate deliberately
  (`coverage.py --update`) in the same commit.

---

## AMENDMENT 2026-08-31 — three names in this file no longer exist

This survey is otherwise still a good map. But it lists as available:

* `dw_polish_no_witness` (line ~32) — **deleted.** The Derr–Williamson citation
  was checked against arXiv:2302.03522 and Thm D.6 does not support it: D.6 is an
  iff-criterion for σ-extendability of a *countably additive* probability, with
  σ(D)=F and block inner regularity, about real-valued probabilities. A witness
  pattern is only finitely coherent, so it does not meet the hypothesis. The
  claim is now the open conjecture `OpenCore.DWPolishCut`, carried as an explicit
  hypothesis by `witness_not_polish` and `carrier_not_polish`.
* `IsIrreducible`, `IsNonSegregated` (lines ~41, ~45) — **retired**, not deleted.
  They are definitions with content in `QuerySystem.Admissibility`
  (`EssentiallyIrreducible`, `NonSegregated`), and `L₁_admissible` proves the
  witness carrier satisfies both. `IsConcrete` and `IsSigmaComplete` were
  likewise discharged as proved defs on 2026-08-30.

So the ⚠ fidelity consequence this file flags — that `IsIrreducible` being an
unconnected stub keeps `Psi` weaker than the paper's Ψ — **is closed.**
`targetA_sharp_ZFC` proves the sharp Exit-A target is inhabited in ZFC by the
ω₁ witness.

The OML side is also no longer "almost entirely outside" the blueprint: it now
carries MO₂ concretely, the four-points-necessary minimality result, the
concrete descent witness, the admissibility bundle, and the Polish-cut
reduction.
