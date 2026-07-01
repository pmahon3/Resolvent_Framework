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

---

## Combinatorial-catalog scout — the whole catalog is BARREN, one structural reason (2026-07-01, /scout, ⟦HAND/structural⟧)

After the gap/AD kill (above), scouted the FULL set-theory catalog of uncountable
combinatorial objects against the razor: does the object's non-uniformizability block a
SET/function (⟹ a non-Dirac σ-state routes around it = rescuer = fails) or a NON-meet-closed
{0,1}-coherent assignment (= state-shaped = a construction lead)? Six classes assessed.

**VERDICT: UNIFORMLY SET-LEVEL. No object passes the razor. No construction lead.**

| Object | blocks a uniformizing… | verdict |
|---|---|---|
| MAD families (Törnquist; Schrittesser–Törnquist) | SET (no set almost-refines all; "no analytic MAD" = definability of a set-family) | FAILS |
| Ladder + non-uniformizable colorings (Devlin–Shelah, weak ◇) | FUNCTION (no g:ω₁→2 uniformizes) | FAILS |
| Suslin / Aronszajn trees | SET (no branch / no antichain) | FAILS |
| Coherent sequences / walks (Todorcevic, ρ, oscillation) | FUNCTIONS (coherence among fiber maps) | FAILS |
| Gaps beyond Hausdorff/Luzin (analytic, tight, (κ,λ), spectrum) | SET (no interpolating set) — type invariant across the spectrum | FAILS |
| Non-meet-closed maximal filter/tower on P(ω)/fin | — DOES NOT EXIST | VACUOUS |

**THE ONE STRUCTURAL REASON (not six coincidences):** every catalog object lives in a
BOOLEAN AMBIENT (P(ω)/fin, 2^ω₁, tree orders). In a Boolean ambient a maximal coherent
{0,1}-assignment is an ULTRAFILTER = MEET-CLOSED BY DEFINITION. The razor demands the
opposite (non-meet-closed = non-distributivity), which NO Boolean-ambient object exhibits.
Object #6 — the only place a state-obstruction could hide — is a contradiction in terms (a
filter on a Boolean algebra is meet-closed by def). Independent re-derivation of the gap-kill
Check-2 (§3a `ℱ_s` meet-closure failure), generalized from gaps to the whole catalog.

**POSITIVE CONTROL (makes it airtight, not failure-to-find):** Kochen–Specker PASSES the razor
(genuine state-obstruction) — but is exactly what Ψ excludes (non-concrete, on L(H), finite/
Wright-covered). So a real state-obstruction is intrinsically non-distributive and provably
does NOT come from the P(ω)/fin catalog.

**⚠ CALIBRATION (do NOT overstate — scout-flagged):** this is NOT evidence toward ¬Ψ (B–W's
Hilbert analogue exists under a measurable ⟹ ¬Ψ is not a ZFC theorem). Correct statement:
**the witness cannot be IMPORTED from set-theoretic combinatorics — borrowed uncountable
combinatorics is a BARREN skeleton source.**

**⭐ THE SHARPENING of "needs a genuinely new object" (the keeper):** the non-distributivity
must be NATIVE TO THE SKELETON, not added to a borrowed one. You cannot glue a non-distributive
object along a DISTRIBUTIVE (Boolean, meet-closed, hence rescued) skeleton and get the
obstruction. The skeleton and the non-distributivity are INSEPARABLE — which is precisely why
every "glue atomless blocks along [combinatorial object]" attempt died: the object was always
Boolean. `intrinsic_K` tightened: the gluing itself must be non-Boolean.

**Flag:** the transfer claim (each set-obstruction routed-around by a non-Dirac σ-state) rests on
the §3a meet-closure argument, taken as given, not re-proved against a paper; the
Boolean-ambient⟹meet-closed⟹rescued spine is a definitional deduction. Sources: Devlin–Shelah
(arXiv:1806.03867), Schrittesser–Törnquist (arXiv:1810.03016), Todorcevic walks (2410.00607).
⟦HAND/structural — catalog barren, one reason; NOT ¬Ψ evidence; witness needs native-non-distributive skeleton.⟧

---

## Feldman–Wilce / Younce block-closure — the concreteness fork RESOLVED (2026-07-01, primary source re-read + advisor ×3)

Handoff `reading_directions/nondistributive_primitive_handoff.md` §5 angle 2 asked: can a
MANUAL be a concrete σ-OML without its σ-completion going abstract (ultrapower)? Advisor
sharpened this to the discriminating **fork**: is the ultrapower in F–W Thm 4.7 a *general
non-concreteness theorem* (⟹ adjacent to impossibility, outcome b) or an *artifact of F–W's
particular construction* (⟹ the concrete-σ gap is located, outcome c)? Full re-read of
`feldman_wilce_1993.pdf` (text `scratchpad/fw.txt`).

**FORK RESOLVED — the ultrapower is a FREE-CASE ARTIFACT, not a general theorem.** The three
F–W σ-representation results split cleanly:
- **Thm 4.1 / 4.2 / 4.5** (L ALREADY carries a σ-structure δ ⟹ L ≅ Π(P₂), P₂ = countable
  j.o. sets D with δD=1): CANONICAL, NO ultrapower. The manual is built from L's OWN elements
  (the σ-analogue of the tautological self-representation Thm 2.1). If L is concrete, its points
  are perspectivity-classes of subsets of the actual set 𝔄(L), not ultrafilter classes.
- **Thm 4.7** (ARBITRARY OA embeds in a σ-OA, via iterated ultrapower `*X=X^α/u` to ω₁):
  ultrapower is load-bearing — but ONLY because it must FREELY manufacture σ-joins the arbitrary
  input lacks. Freeness ⟹ ultrapower; it is the fingerprint of the free completion, not a proof
  that concrete σ-completions can't exist.

**∴ NOT a reversal of the §3s "concreteness-preservation DECISIVELY NEGATIVE" verdict** (advisor
caught this): §3s answered the NARROW hinge "does F–W's *construction* preserve concreteness?"
(no, ultrapower) — compatible with the OPEN question "can a concrete σ-OA with native incompat.
EXIST?" Two different questions, both answered correctly. §3s never claimed impossibility. Do NOT
relabel this re-derivation as a discovery (sharpen guardrail).

**THE THREE-RUNG LADDER (the located-wall content, outcome c):**
> σ-OA (Def 3.2: incr. seqs have sups)  ⊇  block-closed (Younce, Thm 4.4)  ⊇?  concrete (L⊆P(Ω))
>
> ⚠ CONTAINMENTS, NOT proven-strict (do not read ⊋). block-closed ⊆ σ-OA holds (a chain lives in
> one block ⟹ its sup exists there); rung1/rung2 STRICTNESS = Younce's OPEN problem verbatim ("we
> do not know whether every block in an arbitrary σ-OA is closed"). rung2/rung3: concrete ⊆
> block-closed is not even obviously clean (is a maximal Boolean subalgebra of L⊆P(Ω) closed under
> countable disjoint unions? not free), and the strict gap (a block-closed NON-concrete OML) is
> CONJECTURAL — argued structurally (fiber vs glue), NO witness exhibited. The ladder pins the
> QUESTION, not a chain of strict inclusions.

- **Younce block-closure** (Thm 4.4, F–W leave it OPEN: "we do not know whether every block in
  an arbitrary σ-OA is closed"): (i) each block B has ∨_B D for countable j.o. D⊆B; (ii) blocks
  B,C sharing D agree: ∨_B D = ∨_C D. ⟺ L admits δ under which every block is closed.
- **Block-closure is NECESSARY but strictly WEAKER than concreteness.** Once closed, each block
  IS a Boolean σ-algebra ⟹ σ-LS-representable INDIVIDUALLY (`B≅Σ_B/N_B`) — the "Boolean σ-rep"
  leg of Side A holds FIBER-WISE FOR FREE. Concreteness additionally demands these per-block
  Stone reps GLUE on one common Ω. Block-closure = fiber condition; concreteness = glue condition.

**⚠ RAZOR CHECK — block-closure is on the WRONG SIDE (advisor, decisive):** clause (ii)
constrains D contained in BOTH blocks = the COMPATIBLE overlap B∩C (itself Boolean). It says
NOTHING about incompatible a∈B, b∈C with a∧b=0 yet a∩b≠∅ as sets. The razor's obstruction —
non-meet-closed {0,1}-coherence across INCOMPATIBLE contexts — lives exactly on the pairs (ii)
does not touch. So "block-closure ≠ σ-LS" is TRUE but INERT: distinct because it's a different
(compatible-overlap) axis, NOT a new grip on the glue. The glue side is σ-LS / Wall A, unchanged.

**NET (outcome c, located wall — a WIN, not strained further):** (1) fork resolved — F–W
ultrapower load-bearing ONLY for free completion of an arbitrary OA; canonical & non-ultrapower
when the σ-structure pre-exists. (2) three-rung ladder places block-closure BETWEEN σ-OA and
concrete (containments only — strictness UNEARNED: rung1/rung2 = Younce's open problem, rung2/rung3
conjectural with no witness), and the gap between them = the non-distributive cross-incompatible-
block glue = Wall A. F–W leaving block-closure open ≠ a construction handle (advisor own-corrected
the earlier "gap where a skeleton could live" optimism). Younce's open "every block closed?" bears
only on whether σ-OA⊋block-closed is STRICT; it does NOT flip Ψ — a failing per-fiber condition
still doesn't
cross the razor. Angle 2 (manuals-as-skeleton) bottoms at the SAME Wall A as every other road.
The convergence held again. Sources: Feldman–Wilce, Order 10:383–392 (1993); Younce diss. [7].
⟦HAND/primary — fork resolved from the paper's own theorem split; razor-check advisor-decisive.⟧

---

## Abramsky–Barbosa pBA duality — angle-3 import read, OFF-CELL via ATOMIC (2026-07-01, talk + advisor)

User supplied the A–B talk "Duality for Partial Boolean Algebras" (Topos Institute Colloquium
15/05/2025; filed `literature/abramsky_barbosa_2025_duality_pBA_talk.pdf`) — directly on handoff
angle 3 (large pBAs = closest existing home for "non-distributive at the skeleton"). Read for the
duality's carrier: is the dual object a native-non-distributive skeleton usable for a witness?

**THE DUALITY (frames 27–42):** transitive partial CABA ≅ complete exclusivity graph, via the
**GRAPH OF ATOMS** `At(A)` — vertices = atoms, edge iff `x⊙x' ∧ x∧x'=0` (compatible + orthogonal);
elements of A ≅ ≡-classes of cliques of At(A); functorially `epCABA ≅ XGph^op`. The dual is
genuinely non-Boolean (a graph with primitive irreflexive-symmetric exclusivity `#`) — at first
glance a native-non-distributive skeleton. KS-property ⟺ no global point (hom A→2 = morphism
K₁→At(A)), frames 13/40.

**KILL = ATOMIC (advisor-corrected — NOT "no σ"):** complete ⟹ σ-complete, so σ is subsumed
trivially; the text's zero σ/countable is because complete-atomic swallows it, NOT the reason.
The real block: CABA = complete **ATOMIC** BA (frame 27, explicit); the ENTIRE duality is built on
**atoms as points** ("state descriptions / possible worlds"). Frame 26 is decisive and self-aware:
they ABANDON the point-based **Stone** route — "classical Stone duality builds the Stone space from
points (homs B→2); by Kochen–Specker, for interesting pBAs there are NO such points" — and go to
the atom-based **Tarski** side BY NECESSITY. (Verified all 5 "Stone" hits: one Stone–Čech *analogy*
for LEP-isation, the rest = the frame-26 rejection. NO atomless/Stone-side pBA duality in the talk.)

**∴ STRUCTURALLY EMPTY ON THE Ψ CELL.** The σ-essential open cell `open.atomless_uncountable_AD` is
ATOMLESS (Luzin collapse kills atomic-only). Atomless ⟹ At(A) empty ⟹ the duality DEGENERATES to
nothing. Same shape as RDP⟺MV (strat.impossibility_i_to_iii): the machinery lives on the COMPLEMENT
of the Ψ config — not unreached, structurally absent there. And At(A) for an atomic-orthogonal OML
= the MO_κ / segregated orthogonality graph = the already-DEAD cell (`carrier.mo_kappa`). This is
KS in categorical-dual dress — razor-pass GUARANTEED (KS passes the razor) yet Ψ-excluded, so the
razor tells us nothing here (advisor: skip it, wrong test).

**SURVIVES — do NOT over-kill:** the pBA **grammar** (states = per-block gluing on overlaps, no
global point set — Abramsky–Barbosa CSL 2021) is UNTOUCHED; still the base language for STATING the
target (P1/P2 separation). Only the duality/REPRESENTATION theorem is atom-blocked. This closes the
"import the pBA duality as representation machinery" sub-route of angle 3; it does NOT close angle-3
grammar. Recorded `strat.abramsky_barbosa_pba_duality` (dead, same_as carrier.mo_kappa).

**CONSTRUCTIVE RESIDUE (angle-4 seed, `open.exclusivity_space_atomless`):** an ATOMLESS / pointfree
analogue of the complete-exclusivity-graph — an "exclusivity space" with `#` primitive but NO
atoms-as-vertices — WOULD be a genuine native-non-distributive skeleton. But that is INVENT (angle
4), not import (angle 3): the A–B object is atom-founded by necessity, nothing transfers. ⚠ Do NOT
launder invention into import because the talk gestures nearby; §6 self-deception warnings apply.
⟦HAND/primary — verdict from the paper's own atom-founded duality + frame-26 Stone-rejection;
atomic-kill advisor-decisive.⟧
