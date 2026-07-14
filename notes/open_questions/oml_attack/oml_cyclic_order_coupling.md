# Cyclic order-coupling of coarse coordinates: no-Fubini freeness and a closure trichotomy

*Opened 2026-07-13 (campaign iteration 2). Status: ⟦HAND⟧ throughout;
no finite instantiation exists (every claim concerns uncountable
structure), so no oracle accompanies this note. Awaits fresh-context
adversarial review. Nothing here proves Ψ_OML or Φ; the yield is one
reusable freeness lemma, one closed architecture class, one explicit
non-lattice exemplar, and a named residue.*

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
𝒜 agree with ν_ℬ (E ∈ 𝒜 contains B∩S iff it contains a member of ℬ:
one direction is monotone after intersecting the dichotomy witnesses;
for the other, if E ⊇ B∩S and E avoided some B′ we would get
∅ = E∩(B∩B′∩S)... wait B∩B′∩S ⊆ E∩B′ = ∅ contradicts persistent
splitting of B″ ⊆ B∩B′). ν⁻ is symmetric with base {B∖S}. ∎

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
σ-consistent over ν_box**; iterating Lemma A (each further order event
still splits every base member: {x<y<z}∩box ≠ ∅ etc., and the
complementary cells likewise), even all-three-values-1 is σ-consistent
over the box marginal on σ(P₃ ∪ 𝒞*) — despite S₁₂∩S₂₃∩S₃₁ = ∅. The
value-1 base {B∩S₁₂∩S₂₃ : B box} consists of nonempty sets ({x<y<z}
meets every box) and is countably closed, and S₃₁... does **not** split
it — S₃₁∩(B∩S₁₂∩S₂₃) = ∅. So on the **Boolean** σ-field
σ(P₃ ∪ 𝒞*) the three events cannot all be charged (an ultrafilter is
finitely multiplicative). The freeness is exactly pairwise: any TWO of
the cyclic events can be jointly σ-charged over the box marginal, never
all three inside one σ-field.

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
σ-class on Ω = κ³ containing F₁, F₂, F₃ pairwise compatibly (so, by
Bruns–Harding as banked in §9c/A2 of the attack note, P₃ lies inside one
maximal block of L) and containing the three order events. Suppose L is a
lattice (hence an OML: σ-class + lattice gives the orthomodular law by
disjoint-difference). Then at least one of:

1. **(invisibility)** some cyclic pair fails transverse visibility:
   S₂₃ is incompatible with R_α for some α (or cyclically); the coupling
   is then not fully realized by event overlaps at that fibre; **or**
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
visibility (S₂₃ compatible with some but not all transverse fibre
rectangles): that residue is named in §5. (ii) It uses only banked
theorem-lets (T1 second form, L0, 2BR/A2); the new content is the
identification of transverse visibility as a pointwise-resolution
supplier and the resulting closure of the class. (iii) Nothing requires
κ = ω₁ or the order to be a well-order: any relation whose cyclic triple
intersection is empty while {(x,y): x<y}-type fibres are
transversely-visible behaves identically.

## 4. The non-lattice horn is genuinely inhabited: the piecewise closure

Horn (3) is not vacuous bookkeeping; the natural completion that makes
everything visible really does destroy the meet, with exactly the
ω₁-chain anatomy of the product-Ulam witness (mechanism 1 of §3 of the
attack note).

**Definition (piecewise closure L_rich).** E ⊆ Ω belongs to L_rich iff
there is a countable P₃-partition {R_k} of Ω and germs E_k with
E ∩ R_k = E_k ∩ R_k, where each E_k belongs to one of the four-element
algebras ⟨S₁₂⟩, ⟨S₂₃⟩, ⟨S₃₁⟩ (= {∅, S, S^c, Ω}; the trivial germs are
shared).

**Claim 1: L_rich is a concrete σ-class containing P₃ ∪ 𝒞*.**
Complements are germwise. For a countable disjoint family, pass to a
common refinement (still a countable P₃-partition); on each piece the
germs of distinct members are disjoint within their families or trivial;
a nontrivial S-germ and a nontrivial S′-germ from different families
cannot be disjoint on a box-containing piece (their intersection meets
every box), and on box-free pieces — which are covered by three countable
strips, since a P₃-set avoiding a box B = A×B′×C is contained in the
union of the complementary countable strips — one refines to single-fibre
pieces, where every order event **degenerates to a P₃ set**
(S₁₂ ∩ ({α}×κ×κ) = {α}×(α,κ)×κ and cyclically), so germ bookkeeping
reduces to P₃ there. Unions of germs on a piece are handled by refining
the piece by the P₃ parts (split R into R∩E and R∖E). P₃ ⊆ L_rich with
trivial germs; each order event is a one-piece member.

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
Z := Y ∪ X_{α*}. Z ∈ L_rich (common refinement; on the α*-fibre pieces
the union of Y's fibre-degenerate P₃ germs with the S₂₃ germ is
expressible after splitting the piece by the P₃ part). Z is a lower
bound. Z ⊋ Y: a point (α*, y, z) with α* < y < z, y ∉ B̃, z ∉ C̃ lies in
X_{α*}∖Y (such y, z exist: the constraints exclude countably many
values). So no lower bound is maximal, while nonzero lower bounds exist
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
| Lemma A, Corollary A1 | hand proved (self-contained) |
| Theorem B | hand proved over banked T1/L0/2BR/A2 |
| L_rich Claims 1–2 | hand proved (piecewise normal form) |
| "residue open" | open, not a claim |

No executable receipts (uncountable content; finite models trivialize:
on finite carriers St_fa = St_σ). Adversarial review owed and scheduled
as the next campaign checkpoint.
