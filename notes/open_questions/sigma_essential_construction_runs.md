# σ-essential — the construction/refutation runs (reasoning trails)

*Extracted from the retired `CHARTED_sigma_essential.md` (2026-06-26). The actual
reasoning of the ¬Ψ and Con(Ψ) attempts, the template no-go resolution, and the
selection-first kill — the trails behind the taxonomy's one-line verdicts. Companion to
[[sigma_essential_taxonomy]] and [[sigma_essential_reduction_writeup]] (the clean writeup;
its §5/§7 supersede the in-the-moment framings flagged below). ⟦HAND — advisor-checked
where noted, NOT verdicts.⟧*

---

## ¬Ψ first run (Exit-B, 2026-06-25)

**Attempted:** prove ¬Ψ under "no measurable cardinal" (in L) — every finite-local
2-valued state `s₀` on `B⊆L` extends to a global σ-additive 2-valued state.

**RESULT: the natural lever is σ-LS-BLOCKED — NOT a verdict on ¬Ψ.** The reduce-to-Dirac
argument (no measurable cardinal ⟹ every σ-state is a point mass ⟹ reduces to
point-realization) is a **σ-ALGEBRA** theorem (classical Ulam/Loomis–Sikorski). L is
non-Boolean: σ-completeness is ORTHOGONAL-joins-only, so `U_s = {A∈L : s(A)=1}` is
countably-complete w.r.t. L's orthogonal-join structure, NOT the powerset's — **there is
no σ-algebra to run Ulam on.** Breaks exactly at the missing σ-LS representation (HW
Problem 2, no regular completion, open in literature). ⚠ "Lever blocked" ≠ "¬Ψ fails":
only the obvious reduction is closed.

**Genuine yield — sharpened witness characterization:** a Con(Ψ) witness must carry a
**countably-complete lattice-ultrafilter on the ORTHOGONAL-JOIN structure that is (i) NOT
a Dirac and (ii) NOT extendable to a σ-algebra** — i.e. the non-Boolean orthogonal-join
structure does the work that needs no measurable cardinal.

**⚠ Symmetry (sober, not a verdict):** if ¬Ψ's natural lever needs σ-LS (Boolean rep)
AND Ψ's witness needs the non-distributive orthogonal-join structure, BOTH sides may
bottom out at the SAME σ-LS wall rather than a clean large-cardinal dichotomy ⟹
independence NOT established in either direction.

## Con(Ψ) construction first run (2026-06-25)

**Attempted:** build a witness on the Navara–Pták template (ℚ²-carrier, `B∩C∩D=∅`
device) sharpened by the ¬Ψ yield.

**The dichotomy (two exhaustive horns):** (H1) force global σ-states = Diracs-only ⟹ Ω
must be standard-Borel/Polish ⟹ **Derr–Williamson D.6 KILLS the gap.** (H2) don't force
Diracs-only ⟹ exotic non-Dirac σ-points may exist ⟹ one can extend `s₀` ⟹ no gap —
UNLESS suppressed via a non-Polish carrier = reintroduces σ-LS. The property that defeats
the local pattern (Diracs-only) is the NEGATION of the property that admits a witness
(non-Polish). The only escape is a third regime (non-Polish carrier, σ-states controlled
enough to suppress the rescuer) = precisely the open σ-LS/HW-Problem-2 cell.

## Template no-go (#28) — RESOLVED: collapses into σ-LS

**Supersedes the earlier "scissors" reading.** Joint 1 verified against Navara–Pták Def 3
(see [[navara_ptak_1983_byhand_read]]): their `m` IS a genuine Ψ-sense σ-additive 2-valued
state. So the N–P example is NOT a Ψ-witness — **not because Polish kills it, but because
the construction BUILDS ITS OWN RESCUER.** `s₀` fails to extend iff NO Dirac AND NO
non-Dirac σ-state rescues it; non-Dirac-rescuer-existence = the σ-point-SELECTION problem
= σ-Loomis–Sikorski. So #28 (bounded no-go) and #29 (the reduction) are ONE theorem; the
honest target is the REDUCTION, conditional on an open problem (HW Problem 2).

**⚠ "convergence" correction (hostile audit):** the "three/seven-way convergence" was a
BOTTLENECK, not a convergence. Genuine independent reductions to wall A ≈ 1 (the §2
equivalence); ¬Ψ-lever / Con(Ψ)-construction / template-no-go are ONE argument three
angles; catuṣkoṭi = failed dissolution; Blecher–Weaver = Hilbert sector, no routing port.
Detail: [[sigma_essential_reduction_writeup]] §5 (corrected).

## Selection-first reframe — CHECKED + KILLED (the 6th costume)

**Reframe:** "build the bare coherent σ-additive non-principal SELECTION first, check
lattice-admissibility after" — hoping to sidestep the band-family closure dichotomy.

**KILLED by direct check on the band family's own partition system** (BandClosure.lean,
on disk). "Coherent across overlapping partitions" means partitions share elements IN L
⟹ the coherence condition IS the lattice overlap-data the reframe proposed to defer.
Concretely on Ω=ℕ×ℕ: a coherent σ-additive selection must respect the two-relative-
complement chain (`relCompl`: `Sβ∖Sα` then `Sα∩Sβ` cells), forcing it to VALUE the
forbidden finite singleton cells `{(i,j)}`; then σ-additivity over the countable disjoint
union of singletons (`csUnion`/`forces_boolean`) forces the selection to be DETERMINED BY
POINTS = principal/Dirac. The selection dies the SAME collapse as the lattice — coherence
conditions = closure conditions. NOT a sidestep; the same wall in the other order. So
selection-first = band family relabeled = 6th costume. Construction by hand stays
CHARTED-DEAD; profile unchanged (uncountably-generated, non-compositional, forcing).

## Step-1 scoping: C1–C4 and why B–W is precedent-not-instance (2026-06-25)

B(ℓ²(κ)) projection lattice passes **C2** (σ-complete, vN-algebra complete lattice),
**C3** (non-Boolean), **C4** (off-center, type-I factor trivial center) but **FAILS C1
(concrete)** — L(H) dim≥3 admits NO 2-valued homomorphism (Kochen–Specker). So B–W is a
PRECEDENT, not an INSTANCE of Ψ; the consistency half is NOT in hand. The entire distance
B–W → admissible-Ψ-witness collapses to the single axis C1 (concreteness). The open STEP
1: *can the Ulam-measurable σ-state mechanism be relocated from B(ℓ²(κ)) onto a CONCRETE
σ-complete OML?* Per Akemann–Weaver (no routing port), NOT by factoring through a
Boolean/concrete sub-object — it must be a DIRECT construction. **Guardrail: C1 is
non-negotiable** (dropping it lands back in known L(H)/KS).

**Dzhenzher 2026 line, read directly (primary source):** arXiv:2604.25854 (quantum states
on ℓ²(κ)) and 2605.24923 (quantum channels on vN-algebras) are BOTH confined to the
Hilbert/operator-algebra case — every Ulam-measurable result in the live literature lives
on the C1-failing Hilbert side; not one reaches a concrete OML. The relocation question is
open in the LIVE 2026 literature, not just in-notes — nobody works the concreteness axis.
