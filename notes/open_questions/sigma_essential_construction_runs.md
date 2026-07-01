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

## Gap / uncountable-AD gluing skeleton — KILLED, split by gap-type (2026-07-01, advisor-checked ×2, ⟦HAND⟧)

**Attempted (the untried seed):** use a **Luzin/Hausdorff gap** or an **uncountable
almost-disjoint (AD) family on ω₁** as the gluing skeleton for the non-Polish carrier, so
that finite ⊥-closed patterns extend locally (Wright) but the global σ-additive 2-valued
thread is blocked by the gap's provable non-interpolability / the AD family's lack of a
common refinement. Hope: the obstruction lives in the *uncountable cross-block gluing*,
not a central factor ⟹ non-segregated + a genuine non-existence (not a rescuer).

**RESULT: NOT A WITNESS. The seed splits into two gap-types, each dead at a different
check; neither survives.** The death is visible at the *skeleton + state* level — no full
Ω/L/s₀ construction is needed to kill it.

**HAUSDORFF form → Check 1 (segregation), NEW reason.** A Hausdorff `(ω₁,ω₁)`-gap is two
⊆*-monotone towers ⟨a_α⟩↑, ⟨b_α⟩↓ with `a_α ⊆* b_β` for all α,β. **Every pair of gap
elements is ⊆*-comparable** (a-side is a ⊆*-chain, b-side is a ⊆*-chain, cross-pairs
⊆*-ordered). A comparability structure is the *most distributive* thing possible ⟹ the gap
generates a **Boolean (distributive) sub-object**. So the gap can be, at best, a *central*
Boolean factor (⟹ **segregated**: σ-states concentrate there ⟹ Dirac ⟹ dead) or a single
**block** (⟹ "no interpolant" is a statement inside one Boolean σ-algebra on ω, where every
σ-additive 2-valued state is Dirac since ω is not measurable ⟹ a δ_ω **rescues** ⟹ dead).
**NEW structural finding (worth logging distinct from Wall A): a gap is a
*compatibility/comparability* structure, and non-central non-distributivity requires
*incompatible* generators — so a gap can NEVER *be* the non-central non-distributivity.**
It is always central or single-block. The seed's hope ("gap entangled with the
non-distributive overlaps, not central") is unrealizable *for type reasons*.

**LUZIN form (ATOMIC blocks) → Check 4 (band dichotomy), index-size-independent.** A Luzin
gap is a pairwise almost-disjoint family `{A_α}` = *exactly* the band-family substrate
(archive `sigma_construction_log_archive.md` L24: "{S_α:α<𝔠} an ALMOST-DISJOINT family").
For **atomic (point-separating) blocks** its death is the archived **relCompl forcing
chain**: for any binding pair with `S_α∪S_β ∈ ℐ` (finite-∪-closure), the forbidden finite
cell `(S_α∩S_β)×{j}` is FORCED into `L̄` at the finite pre-σ level ⟹ **Boolean**; else
`cl(a∪b)` escapes ⟹ **not-a-lattice**. The archive **certifies this index-size-independent**
("difference size IRRELEVANT," "Step 1 does not need ℕ — only `S_α∪S_β∈ℐ`"), so moving `κ`
from 𝔠 to ω₁ **re-triggers the identical dichotomy**. This is the "AD-indexed with a
specific closure" entry already on the DEAD list — nothing new to run.

**⚠ SCOPE (advisor-caught over-claim, corrected): Check 4 is ATOMIC-ONLY.** The relCompl
step is set-algebraic and transfers, BUT the *collapse-to-Boolean conclusion* routes through
the **Session-7 equivalence** (archive L57–66): "point-separating generators ⟹ full σ-algebra
`P(Ω)` ⟹ `L̄` Boolean ⟺ `L̄⊊P(Ω)`." That inference **needs point-separation = atomicity** —
precisely what **atomless measure-algebra blocks lack**. And the DEAD list only kills atomless
gluing when it is *countable* (DW/Polish). So the cell **atomless + uncountable-AD** is killed
by NEITHER — Check 4 does not reach it. That cell is the seed's likely actual target (it
proposed "atomless … contexts"). See the mechanism-kill below, which DOES reach it.

**THE GENERAL KILL — Check 2, atomicity-agnostic (reaches even atomless+uncountable-AD).**
The gap's whole hoped-for power is its **non-interpolability / unseparability**: (Luzin) no
`B` with `A_α ⊆* B` on one part, `A_α ∩ B =* ∅` on the other; (Hausdorff) no `c` with
`a_α ⊆* c ⊆* b_β`. This is a **ZFC-absolute** non-existence — so, unlike the CBER/DST kills
(§3j–§3l, definability obstructions), the gap route genuinely tests whether
**definability-vs-existence was the ONLY obstruction.** ANSWER: NO — **the obstruction is the
WRONG TYPE and does not transfer, on ANY carrier (atomic or atomless).** Non-interpolability
blocks a separating/interpolating **SET**; the witness needs "no non-Dirac σ-additive 2-valued
**STATE**." These are different objects: an N–P-style non-Dirac σ-state extends `s₀`
regardless of unseparability and is the **rescuer**, because a σ-state on a σ-*class* need
NOT produce a separating set (the `ℱ_s`-not-a-filter / meet-closure failure, §3a) — the
{0,1}-values of a state do not assemble into a set `B` unless the state's filter is meet-
closed, which fails off Boolean. Transfer would need intersection-closure = disjointification
= Boolean. **This kill never touches atomicity**, so it covers the atomless+uncountable-AD
cell that Check 4 misses: the *gap-interpolation MECHANISM* is shown not to reach a witness on
any carrier. (It does NOT kill the atomless+uncountable-AD *carrier* as such — only this
mechanism for exploiting it; cf. the standing "mechanism fails ≠ carrier dead" calibration,
§3f/§3m.) **This confirms the wall exceeds the definability gap** — the
definability-vs-existence diagnosis (§3j/§3r) was correct but not the *whole* story; the
disjointification wall blocks even an absolute combinatorial obstruction.

**Check 3 note (why ω₁-carrier evasion buys nothing):** a gap on ω lives on standard-Borel
`P(ω)` + countable `Ω` ⟹ DW/band-theorem kill directly. The only Check-3 survivor is a gap
whose *elements* live on an uncountable ω₁-carrier — but Hausdorff-ω₁ still dies Check 1
(segregation) and Luzin-ω₁ still dies Check 4 (band, index-independent). Non-Polishness of
the carrier does not rescue either horn.

**VERDICT (three-layer, honestly scoped):**
- **Check 2 (GENERAL, atomicity-agnostic) is the load-bearing kill:** the gap's
  non-interpolability is an *absolute obstruction of the WRONG TYPE* — it blocks separating
  SETS, not σ-additive 2-valued STATES; no transfer without intersection-closure = Boolean.
  This kills the *gap-interpolation MECHANISM* on any carrier, atomic or atomless.
- **Check 1 (Hausdorff only):** comparable ⟹ Boolean ⟹ central (segregated) or single-block
  (δ_ω rescues). Extra, form-specific.
- **Check 4 (Luzin, ATOMIC blocks only):** mod-finite→exact = band dichotomy,
  index-size-independent; but the Boolean conclusion routes through point-separation, so it
  does NOT reach atomless blocks.

Two NEW findings worth keeping: (i) *a Hausdorff gap is a **comparability** structure ⟹
structurally incapable of being the non-central non-distributivity* (SCOPED TO HAUSDORFF —
Luzin/AD families DO produce incompatibility, the band "binding pair"; Luzin dies not for
lacking incompatibility but because, atomically, the incompatibility is forced closed, and
atomlessly because the interpolation MECHANISM is the wrong type — Check 2). (ii) *the wall is
confirmed to exceed the definability-vs-existence gap — even an ABSOLUTE combinatorial
non-existence (unseparability) fails to transfer, for the disjointification reason.*

**Honest boundary (not over-claimed):** this run kills the **gap/interpolation mechanism** for
building the witness, on every carrier. It does NOT close the **atomless+uncountable-AD
CARRIER** — that cell is killed by neither the DEAD-list (which only kills atomless gluing when
*countable*, DW/Polish) nor Check 4 (atomic-only); only the specific gap-interpolation route
into it is shown not to reach a witness. Not a witness. Stop-condition unchanged: needs a
genuinely new object; a gap's *interpolation-failure* is provably not the tool, and a Hausdorff
gap's *comparability* structurally cannot host non-central non-distributivity. ⟦HAND,
advisor-checked ×2; load-bearing facts verified: Hausdorff pairwise ⊆*-comparability (gap def);
relCompl index-independence + its atomic/point-separation dependence (archive L44–66); Check 2
type-mismatch (§3a `ℱ_s` meet-closure failure).⟧
