# Cyclic order-coupling of coarse coordinates: no-Fubini freeness and a closure trichotomy

*Opened 2026-07-13 (campaign iteration 2). Status: ⟦HAND⟧ throughout;
no finite instantiation exists (every claim concerns uncountable
structure), so no oracle accompanies this note. Fresh-context
adversarial review CLEARED 2026-07-13 (campaign iteration 3): no
load-bearing claim refuted; repairs applied in place, marked
✎ review s-it3 (Lemma A agreement step reconstructed; a
self-contradicted all-three-consistency clause struck from Corollary
A1; Theorem B's visibility hypothesis restated as X_α ∈ L with the
κ = ω₁ scope pinned for the P₃-internal reading; §4's refinement lemma
and corrected fibre-degeneration supplied). Nothing here proves Ψ_OML
or Φ; the yield is one reusable freeness lemma, one closed architecture
class, one explicit non-lattice exemplar, and a named residue.*

## 1. The candidate

The banked tameness mechanisms all defeat couplings that factor through a
single coordinate. The natural next architecture, named in
[`CAMPAIGN_LOG.md`](CAMPAIGN_LOG.md), couples **three** coarse coordinates
cyclically through order events. Fix an uncountable κ (κ = ω₁ suffices),
Ω = κ³, and:

- F₁, F₂, F₃ — the three coordinate countable/co-countable fields
  (Fᵢ = cylinders over ctble/coctble(κ) in coordinate i);
- S₁₂ = {(x,y,z) : x < y}, S₂₃ = {y < z}, S₃₁ = {z < x}.

The intended cluster is 𝒞* = {S₁₂, S₂₃, S₃₁}: pairwise intersections are
uncountable ({x<y<z} etc.), the triple intersection is **empty** (no
x < y < z < x), so no Dirac charges 𝒞*, and the hope is that pairwise
incompatibility lets a finitely additive state charge all three while
σ-additivity — via some Fubini/Sierpiński mechanism on the coarse
coordinates — forbids it. Both hopes are now closed, one by a freeness
lemma, one by a trichotomy.

Throughout, P₃ := σ(F₁ ∪ F₂ ∪ F₃) (the product σ-field; it contains all
rectangles A×B×C with ctble/coctble sides). A **box** is a rectangle with
all three sides co-countable.

## 2. The no-Fubini lemma: coupling values cannot be forced through coarse marginals

The measure-theoretic intuition — on ω₁², {x<y} has full y-sections and
countable x-sections, so cocountable⊗cocountable cannot decide it
consistently — does **not** transfer to two-valued states. Two-valued
σ-additivity has no integration of sections; what replaces Fubini is a
filter-base computation, and it leaves the order events free.

**Lemma A (splitting freeness).** Let 𝒜 be a σ-field of sets on a set X
and ℬ ⊆ 𝒜∖{∅} a **countably closed filter base** (any countable
subfamily has a member of ℬ below its intersection) satisfying the
**ℬ-dichotomy**: every E ∈ 𝒜 contains or avoids some member of ℬ. Then
ν_ℬ(E) := 1 iff E contains a member of ℬ is the unique two-valued
σ-additive state on 𝒜 charging every member of ℬ. If S ⊆ X **splits ℬ
persistently** (B∩S ≠ ∅ ≠ B∖S for every B ∈ ℬ), then on
σ(𝒜 ∪ {S}) = {(E₁∩S) ⊍ (E₂∖S) : Eᵢ ∈ 𝒜} there are two-valued σ-additive
states ν⁺, ν⁻ extending ν_ℬ with ν⁺(S) = 1 and ν⁻(S) = 0. In particular
σ-additivity does not decide S over the ℬ-marginal.

*Proof.* Well-definedness of ν_ℬ: E cannot both contain B and avoid B′,
since B∩B′ ⊇ some B″ ∈ ℬ is nonempty. Ultrafilter property is the
dichotomy; σ-additivity of a two-valued state is equivalent to closure of
the value-1 class under countable intersections, which is countable
closedness of ℬ (∩ₙEₙ ⊇ ∩ₙBₙ ⊇ B* ∈ ℬ, and ∩ₙEₙ ∈ 𝒜 then contains B*).
Uniqueness: any σ-state ν charging ℬ: if E avoids B′ then E ⊆ X∖B′ gives
ν(E) ≤ 1−ν(B′) = 0; if E ⊇ B then ν(E) = 1.

For ν⁺: the displayed form of σ(𝒜 ∪ {S}) is itself a σ-field containing
𝒜 and S (closure under complement and countable unions is coordinatewise
in (E₁,E₂)). Put ν⁺(E) = 1 iff E ⊇ B∩S for some B ∈ ℬ. The family
{B∩S : B ∈ ℬ} is a countably closed filter base of **nonempty** sets
(persistent splitting plus countable closedness of ℬ), so ν⁺ is
σ-additive and consistent by the same computation. Ultrafilter property:
for E = (E₁∩S) ⊍ (E₂∖S), apply the dichotomy to E₁: if E₁ ⊇ B then
E ⊇ B∩S; if E₁∩B′ = ∅ then E^c = (E₁^c∩S) ⊍ (E₂^c∖S) ⊇ B′∩S. Values on
𝒜 agree with ν_ℬ: let E ∈ 𝒜 with E ⊇ B∩S. By the ℬ-dichotomy either
E ⊇ B′ for some B′ ∈ ℬ — then ν_ℬ(E) = 1 — or E∩B′ = ∅ for some
B′ ∈ ℬ; in the latter case pick B″ ∈ ℬ with B″ ⊆ B∩B′, and
B″∩S ⊆ B∩B′∩S ⊆ E∩B′ = ∅ contradicts persistent splitting of B″. So
ν⁺ = 1 on E ∈ 𝒜 implies ν_ℬ(E) = 1; the converse is monotonicity
(E ⊇ B′ ⊇ B′∩S). ν⁻ is symmetric with base {B∖S}. ∎ *(✎ review s-it3:
this step was garbled in the first draft; reconstruction as above,
checked by the fresh-context referee.)*

**Corollary A1 (order events are σ-free over the box filter).** On P₃
the boxes form a countably closed filter base (countable intersections
of co-countable sides are co-countable) with the ℬ-dichotomy: the class
of events containing or avoiding a box is a σ-field containing the
generators — if each Eₙ avoids a box Bₙ, then ∩Bₙ contains a box avoided
by ∪Eₙ; complements swap the two horns. Hence ν_box (charge exactly the
box-containing events) is the unique σ-state on P₃ with all three
marginals co-countable. Each order event Sᵢⱼ splits every box
persistently (a box has cofinal sides: pick x < y or x ≥ y inside it at
will). Therefore **on σ(P₃ ∪ {Sᵢⱼ}) both truth values of Sᵢⱼ are
σ-consistent over ν_box**, and Lemma A iterates once more: any TWO of
the cyclic order events can be jointly σ-charged over the box marginal
(the value-1 base {B∩S₁₂∩S₂₃ : B box} consists of nonempty sets —
{x<y<z} meets every box — and is countably closed). The iteration
provably stops there: S₃₁ does **not** split that base
(S₃₁∩(B∩S₁₂∩S₂₃) = ∅), so Lemma A's hypothesis fails at the third
step, and indeed on the **Boolean** σ-field σ(P₃ ∪ 𝒞*) the three
events cannot all be charged even finitely additively (an ultrafilter
is finitely multiplicative and the triple intersection is empty). The
freeness is exactly pairwise: any two, never all three inside one
σ-field. *(✎ review s-it3: the first draft asserted all-three
σ-consistency here, contradicting its own next sentence; struck.)*

**Reading.** Lemma A kills the Fubini-transfer intuition in general: a
witness cannot force coupling-event values through countable/co-countable
marginals; every box-splitting event stays free. Any trap must instead
work through **disjoint-union geometry** — countable partitions in a
block — which is the relay/atom-killing engine again, or through
**latticehood interacting with the coupling**, which the next section
closes for this class. Corollary A1's last computation also fixes where
the OML structure must sit: the three order events must be pairwise
**incompatible** (in no common block), else the cluster is not even
finitely coherent.

## 3. The trichotomy: full transverse visibility closes the class

Write R_α := {α}×(α,κ)×κ = ({α}) × (α,κ) × κ, a P₃ rectangle (both
{α} and (α,κ) = κ∖[0,α] are ctble/coctble). Its cyclic analogues are
defined mutatis mutandis.

**Theorem B (cyclic order-coupling trichotomy).** Let L be a concrete
σ-class on Ω = κ³ containing F₁, F₂, F₃ pairwise compatibly and the
three order events. Call the pair (S₁₂, S₂₃) **fully transversely
visible** if X_α := S₂₃ ∩ R_α ∈ L for every α < κ (for κ = ω₁ each
R_α ∈ P₃, and pairwise compatibility of the coordinate fields plus
Bruns–Harding/A2 — which applies once L is assumed a lattice, since A2
needs blocks to be σ-fields — places P₃ inside one maximal block, so
visibility then reads: S₂₃ is compatible with each fibre rectangle;
for general κ take X_α ∈ L as the definition). Suppose L is a lattice
(hence an OML: σ-class + lattice gives the orthomodular law by
disjoint-difference). Then at least one of:

1. **(invisibility)** every cyclically labelled pair fails full
   transverse visibility at some fibre; the coupling is then not fully
   realized by event overlaps at that fibre; **or**
2. **(degeneracy)** two of the order events are compatible, and then no
   finitely additive two-valued state charges 𝒞* — the cluster is not a
   candidate pattern at all; **or**
3. L is **not a lattice** — contradiction with the hypothesis; i.e. a
   fully visible lattice realization does not exist.

Consequently there is **no concrete σ-complete OML realization of the
cyclic order triple with full transverse visibility in which 𝒞* is a
finitely coherent pattern**. The architecture class is closed.

*Proof.* Assume full visibility for the pair (S₁₂, S₂₃): S₂₃ compatible
with R_α for every α, i.e. X_α := S₂₃ ∩ R_α ∈ L. Note
X_α = {(α,y,z) : α < y < z} ⊆ S₁₂ ∩ S₂₃ (α < y gives S₁₂), and every
point of S₁₂∩S₂₃ lies in some X_α (take α = its first coordinate; then
x < y < z puts it in X_x). Each X_α is a lower bound of {S₁₂, S₂₃}. If L
is a lattice, the meet W = S₁₂ ∧ S₂₃ exists and W ⊇ X_α for all α, so
W ⊇ ⋃_α X_α = S₁₂∩S₂₃; being a lower bound, W ⊆ S₁₂∩S₂₃. Hence
S₁₂∩S₂₃ = W ∈ L and the pair is compatible (banked L0: an in-L
intersection is the meet and witnesses commuting). This is horn (2), and
it is exactly the banked T1 second form (pointwise resolution of an
overlap forces compatibility on a lattice), instantiated by transverse
visibility.

For horn (2)'s consequence: suppose S₁₂ ↔ S₂₃, and let μ be a finitely
additive two-valued state with μ ≡ 1 on 𝒞*. In a common block of
S₁₂, S₂₃ (a Boolean σ-field), μ(S₁₂∩S₂₃) = 1. The pattern
{S₁₂∩S₂₃, S₃₁} has value-1 part in two blocks and
(S₁₂∩S₂₃) ∩ S₃₁ = ∅; the 2BR argument then forces
(S₁₂∩S₂₃) ⊥ S₃₁, so their disjoint union is in L and receives μ-value
2 — absurd. So no such μ exists. ∎

**Scope notes.** (i) The theorem does not touch couplings with *partial*
visibility (X_α ∈ L for some but not all α): that residue is named in
§5. (ii) It uses only banked theorem-lets (T1 second form, L0, the
E∩F = ∅ branch of the 2BR proof, A2); the new content is the
identification of transverse visibility as a pointwise-resolution
supplier and the resulting closure of the class. (iii) With visibility
stated as X_α ∈ L, nothing requires κ = ω₁ or a well-order: any
relation triple with empty cyclic intersection and L-visible fibre
slices behaves identically. The P₃-internal reading of visibility
(compatibility with fibre rectangles) does need κ = ω₁, since for
α ≥ ω₁ the interval (α,κ) is neither countable nor co-countable and
R_α ∉ P₃. Only one fully visible pair is needed for the proof; the
cyclic labels are otherwise symmetric.

## 4. The non-lattice horn is genuinely inhabited: the piecewise closure

Horn (3) is not vacuous bookkeeping; the natural completion that makes
everything visible really does destroy the meet, with exactly the
ω₁-chain anatomy of the product-Ulam witness (mechanism 1 of §3 of the
attack note). **This whole section is pinned to κ = ω₁** (the fibre
degenerations below must land in P₃).

**Definition (piecewise closure L_rich).** E ⊆ Ω belongs to L_rich iff
there is a countable P₃-partition {R_k} of Ω and germs E_k with
E ∩ R_k = E_k ∩ R_k, where each E_k belongs to one of the four-element
algebras ⟨S₁₂⟩, ⟨S₂₃⟩, ⟨S₃₁⟩ (= {∅, S, S^c, Ω}; the trivial germs are
shared).

**Refinement lemma (✎ review s-it3: previously asserted without proof,
and false for general σ-fields).** Any countable family of P₃ sets
admits a countable P₃-partition refining all of them. *Proof.* Each
member lies in the σ-field generated by countably many coordinate
cylinders; collect all generators. Per coordinate i, let D_i ⊆ κ be the
(countable) union of the countable sides of the generators (taking the
complement's side when a generator's set is co-countable). Every
generator is a union of the coordinate-i atoms {δ} (δ ∈ D_i) and
κ∖D_i, so the generated σ-field on coordinate i has countably many
ctble/coctble atoms, and the product atoms — countably many P₃
rectangles — partition Ω and refine every member (the class of unions
of product atoms is a σ-field containing the generating cylinders). ∎

**Fibre degeneration (✎ review s-it3: corrected — only TWO of the three
order families degenerate per fibre orientation).** On an x-fibre
{α}×κ², S₁₂ degenerates to the P₃ set {α}×(α,κ)×κ and S₃₁ to
{α}×κ×[0,α), but S₂₃ ∩ ({α}×κ²) = {α}×{y<z} is NOT P₃ (its section
neither contains nor avoids a 2-D box). Cyclically for y- and z-fibres.
So on single-fibre pieces germ bookkeeping reduces to P₃ **for two of
the three families**, and one family's germs persist.

**Claim 1: L_rich is a concrete σ-class containing P₃ ∪ 𝒞*.**
Complements are germwise. For a countable disjoint family {Xₙ}, use the
refinement lemma to pass to a common countable P₃-partition of all the
pieces involved. On a box-containing piece, nontrivial germs of distinct
members from different families cannot coexist (disjointness fails:
distinct-family nontrivial germs intersect on every box), so all
nontrivial germs on such a piece lie in one family and their union stays
in that family's four-element algebra (S ⊍ S^c = Ω). Box-free pieces are
covered by three countable strips (a P₃ set avoiding a box A×B′×C is
contained in the union of the complementary countable strips), so refine
them to single-fibre pieces; there, by fibre degeneration, all germs
from two of the families become P₃ sets, and at most the germs of the
one surviving family are non-P₃: the union on such a piece is
(surviving-family germ part) ∪ (a P₃ set P), and splitting the piece by
P (germ Ω on piece∩P; the surviving family's germ off it) exhibits
membership. P₃ ⊆ L_rich with trivial germs; each order event is a
one-piece member.

**Claim 2: in L_rich, S₁₂ ∧ S₂₃ does not exist.** Lower bounds: X_α ∈
L_rich for every α (one rectangle piece with germ S₂₃), and countable
disjoint unions X_A := ⊍_{α∈A}X_α (A countable) are lower bounds. Now
let Y ∈ L_rich be any lower bound. On a box-containing piece R_k of Y's
partition, Y's germ E_k must satisfy E_k∩R_k ⊆ S₁₂∩S₂₃∩R_k; every
nontrivial germ from any family fails this on a box (e.g.
S₁₂∩R_k ⊄ S₂₃: pick x < y with z ≤ y inside the box), so E_k = ∅ there.
Hence Y is supported on the box-free pieces, i.e. inside countably many
countable strips: there are countable Ã, B̃, C̃ with
Y ⊆ (Ã×κ²) ∪ (κ×B̃×κ) ∪ (κ²×C̃). Choose α* ∉ Ã, and consider
Z := Y ∪ X_{α*} (an overlapping union, so σ-class closure does not apply
directly; membership is checked piecewise ✎ review s-it3). Refine Y's
partition by {α*}×κ² and by R_{α*}. Off the α*-fibre, Z = Y. On a piece
inside R_{α*}: if Y's germ there lies in ⟨S₂₃⟩, the union with X's S₂₃
germ stays in ⟨S₂₃⟩ (S₂₃ ∪ S₂₃ = S₂₃, S₂₃^c ∪ S₂₃ = Ω); if it lies in
⟨S₁₂⟩ or ⟨S₃₁⟩, it degenerates on the fibre to a P₃ set P, and
splitting the piece by P gives germs Ω on piece∩P and S₂₃ off it. So
Z ∈ L_rich. Z is a lower bound (both parts lie in S₁₂∩S₂₃). Z ⊋ Y: a
point (α*, y, z) with α* < y < z, y ∉ B̃, z ∉ C̃ lies in X_{α*}∖Y (each
constraint excludes countably many values, and (α*,κ) is co-countable —
κ = ω₁). So no lower bound is maximal, while nonzero lower bounds exist
(X_α ≠ ∅): the meet fails. ∎

L_rich is therefore a concrete σ-class realizing full visibility whose
lattice completion cannot exist within itself; the lower bounds of the
incompatible pair form an increasing κ-chain of countable-support events
with no maximum — **the same trace-rigidity anatomy that makes the OMP
witness a non-lattice**. Cyclic order-coupling of coarse coordinates
reproduces the Ulam meet-destruction, now as a *derived* rather than
assumed phenomenon.

## 5. Exact conclusion, mechanism entry, and residue

**Closed:** the cyclic order-coupled coarse-coordinate architecture with
full transverse visibility (Theorem B), together with the hope of
σ-value forcing through coarse marginals in *any* architecture
(Lemma A): a coupling event that persistently splits the relevant
countably-closed base is σ-free over that base. A witness must therefore
force values by countable disjoint-union geometry inside blocks (the
relay/atom-killing engine) — coarse marginal structure alone cannot do
it.

**Mechanism entry (for the tameness list):** *pointwise-resolved
overlaps* — if the set intersection of an intended incompatible pair is
exhausted by L-events below it (here: supplied by transverse
visibility), T1 forces compatibility-or-non-lattice; the pattern then
dies by 2BR or the carrier leaves OML.

**Residue (open, sharpened):** partially visible couplings — cyclic
order (or other box-splitting) events compatible with *some but not
all* transverse fibre rectangles, so that pointwise resolution fails on
an uncountable set of fibres while enough visibility remains for blocks
to interact. Any such candidate must specify which fibre rectangles are
visible; stationary/non-stationary splits are the natural place to look.
This residue, not the fully visible class, is the surviving Lane A
direction for coupled coarse coordinates.

## 6. Evidence ledger

| Claim | Class |
|---|---|
| Lemma A, Corollary A1 | hand proved (self-contained), adversarially reviewed SOUND |
| Theorem B | hand proved over banked T1/L0/2BR-branch/A2, adversarially reviewed SOUND |
| L_rich Claims 1–2 (κ = ω₁) | hand proved; two review-found gaps patched in place (refinement lemma, fibre degeneration) |
| "residue open" | open, not a claim |

No executable receipts (uncountable content; finite models trivialize:
on finite carriers St_fa = St_σ). Fresh-context adversarial review
cleared 2026-07-13; see status line.
