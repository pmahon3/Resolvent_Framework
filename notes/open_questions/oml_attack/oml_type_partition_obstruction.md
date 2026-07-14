# The type-partition obstruction: disjointness-based σ-kills defeat their own witness

*Opened 2026-07-13 (campaign iteration 4). Status: ⟦HAND⟧; the theorem
and corollary are elementary and self-contained over the σ-class axioms;
the club-field classification uses Ulam's theorem (ZFC; no σ-complete
free ultrafilter on a set of size ℵ₁ — Ulam 1930, via the Ulam matrix).
No finite oracle applies. Adversarial review owed at the next
checkpoint. Provenance: mined from three failed coarse-trap designs
(§4), per the campaign's failure-mining mandate.*

## 1. What this closes

Iteration 1 (Corollary 3 of
[`oml_coarse_inhabitation_and_defect.md`](oml_coarse_inhabitation_and_defect.md))
reduced trapping at countable-type coarse boundaries to (a) one diffuse-
state exclusion plus (b) killing the atom-principal lifts. The natural
kill mechanism — arrange, atom by atom over a localizer, that two of the
pattern's events be disjoint there, so that any localized σ-state
charges two disjoint events — turns out to be **void**: the finite
partition of the localizer by "which pair is killed" is itself
event-measurable in every case where the localization works, and then
the same disjointness kills the finitely additive witness. The trap and
the witness die together.

## 2. The obstruction theorem

**Theorem 1 (type-partition obstruction).** Let L be a concrete σ-class
on Ω (OML not required). Let T_1, …, T_r ∈ L be pairwise disjoint with
K := T_1 ⊍ … ⊍ T_r ∈ L, and let Σ_1, …, Σ_k ∈ L each be compatible with
every T_t (Σ_i ∩ T_t ∈ L). Suppose that for every cell t there is a pair
i(t) ≠ j(t) with

\[
 Σ_{i(t)} ∩ Σ_{j(t)} ∩ T_t = ∅ .
\]

Then no two-valued finitely additive state μ on L has
μ(K) = μ(Σ_1) = ⋯ = μ(Σ_k) = 1.

*Proof.* Monotonicity holds on any concrete σ-class (banked ✎s16 form:
E ⊆ A, μ(E) = 1 forces μ(A) = 1, since E ⊥ A^c and
μ(E ⊍ A^c) = 1 + μ(A^c) ≤ 1). Additivity over the finite disjoint union
K gives Σ_t μ(T_t) = μ(K) = 1, so exactly one cell T_t is charged.
Multiplicativity on compatible pairs is block-free: with
W := Σ_i ∩ T_t ∈ L, also Σ_i ∖ T_t = Σ_i ∖ W ∈ L (difference of
comparable events), and μ(W) + μ(Σ_i ∖ T_t) = μ(Σ_i) = 1; if μ(W) = 0
then μ(Σ_i ∖ T_t) = 1 with Σ_i ∖ T_t ⊆ T_t^c, so monotonicity gives
μ(T_t) = 0 — contradiction. Hence μ(Σ_{i(t)} ∩ T_t) =
μ(Σ_{j(t)} ∩ T_t) = 1. These two events are disjoint members of L, so
orthogonal, their disjoint union is in L, and additivity yields value
2 — absurd. ∎

**Corollary 2 (uniform pairwise-disjointness σ-kills are self-defeating).**
Let B ⊆ L be a Boolean σ-subfield lying in a block, K ∈ B, and let the
trace of B on K be atomic with atom family {A_m}_{m∈M}. Let
Σ_1, …, Σ_k ∈ L each be compatible with every element of B, and suppose
the intended σ-kill holds: for every m ∈ M some pair i ≠ j has
Σ_i ∩ Σ_j ∩ A_m = ∅. If the type cells

\[
 T_{ij} := \bigcup \{ A_m : (i,j)\ \text{is the least killed pair of}\
 A_m \}
\]

all belong to B — which is automatic when **M is countable** (countable
disjoint unions of B-events) or when **B is locally full below K** (B
contains every sub-union of the atom family) — then Theorem 1 applies
with the cells {T_{ij}}, and no two-valued f.a. state charges
{K, Σ_1, …, Σ_k}: **the pattern that was to exhibit ¬Φ is not even
finitely coherent.**

*Proof.* The finitely many T_{ij} are pairwise disjoint B-events with
union K, each compatible with each Σ (compatibility with all of B is
hypothesized), and Σ_i ∩ Σ_j ∩ T_{ij} = ⋃_m (Σ_i ∩ Σ_j ∩ A_m) = ∅ over
the type's atoms. Theorem 1 finishes. ∎

**Reading.** The asymmetry a witness needs — σ-additive states die,
some finitely additive state survives — can never be produced by
set-level disjointness that block multiplicativity can reach through a
finite pattern: disjointness is a *finitely* additive killer. The only
asymmetry sources left standing are (i) genuinely countable
disjoint-union constraints inside blocks (σ-only — the master/relay
engine), and (ii) completeness failure of free ultrafilters (Ulam-type
— σ-only, and *not* reducible to a fixed countable decomposition; see
§3). Any witness architecture must route its atom-principal kills
through (i) or a contextual mechanism, never through per-atom
disjointness over a localizer the pattern can reach.

## 3. The club field: state-coarse, not countable-type — and still fenced

This answers iteration 1's open question (§5(3) there): countable-type
anatomy is **not** universal among state-coarse σ-fields of sets.

**Definition.** 𝒜_club := {E ⊆ ω₁ : E nonstationary, or E contains a
club}. This is a σ-field: the nonstationary sets form a σ-ideal (the
club filter is countably closed), complement-symmetry is built in, and a
countable union is club-containing if any member is, else nonstationary.

**Proposition 3 (classification).** The two-valued σ-additive states on
𝒜_club are exactly the Diracs δ_α and the club state ν_club
(value 1 on exactly the club-containing sets). In particular 𝒜_club is
state-coarse; its atoms are the singletons, and it is not of countable
type over them (an uncountable nonstationary set with uncountable
complement is neither a countable nor a co-countable union of atoms).

*Proof.* ν_club is a state by the dichotomy defining 𝒜_club, and
σ-additive since the club filter is countably closed (value-1 class
closed under countable intersections). Conversely let ν be σ-additive,
two-valued, non-Dirac. If ν charged a countable set, σ-additivity over
its singletons would make ν Dirac; so ν kills countable sets. If ν
charged an uncountable nonstationary E₀: every subset of E₀ is
nonstationary, so P(E₀) ⊆ 𝒜_club, and the trace of ν on P(E₀) is a
σ-complete free ultrafilter on a set of size ℵ₁ — contradicting Ulam's
theorem (ZFC). So ν kills every nonstationary set and equals ν_club. ∎

**Defect anatomy.** The finitely additive two-valued states on 𝒜_club
are the Diracs, ν_club, and the free ultrafilters concentrated on a
nonstationary set (the trace on some P(E₀)); the σ-defect is exactly
that third class. Unlike the countable-type defect, its members can
concentrate on **uncountable** sets, and their σ-failure has no uniform
countable witness — it is Ulam-type: every free ultrafilter on P(E₀)
simply fails countable completeness, a state-dependent failure.

**Fence.** This richer defect does not escape §2: 𝒜_club is **locally
full** below every nonstationary event (P(E₀) ⊆ 𝒜_club), so Corollary 2
applies to any localizer inside a nonstationary set, with the same
self-defeating conclusion for disjointness-based kills. Separately, a
club-type block inside a non-Boolean carrier must be *cylinderized*
(e.g. events E × F₀ over a second coordinate): the plain field contains
all carrier singletons, and banked T1 makes any concrete σ-class OM
lattice containing all singletons Boolean.

**Sharpened B′(ii) geography.** State-coarse σ-fields of sets now split
three ways: countable-type (defect free-on-countable; trap reduces to
the relay problem — iteration 1), locally-full Ulam-type (club fields;
disjointness-kills void by Corollary 2; free lifts already σ-dead for
free, so the *only* remaining kill target is the Dirac/atom-principal
family), and whatever is neither. The open classification question
becomes: does every state-coarse σ-field of sets have its σ-defect
governed by one of these two mechanisms (fixed countable decomposition
vs. Ulam completeness failure)?

## 4. Provenance: the three failed designs (recorded as required)

All three attempted the same trap on Ω = ω₁ × 6-style carriers: a
cylinder base block B over the first coordinate, a forced event K, and
three graph events Σ_i (per-column row sets r_i(x)) with per-column
pairwise disjointness at eligible columns.

1. **Full-power-set base** (B ≅ P(ω₁)-cylinders): Ulam kills free lifts,
   Diracs are killed per column by disjoint rows — but μ|B is a genuine
   ultrafilter and the kill-type sets are B-events: Corollary 2 kills
   the f.a. witness. Dead.
2. **Countable localizer** (K countable, columns ∈ B): σ-localization
   works, but a σ-field containing the countably many column-atoms of K
   contains every sub-union, hence the type cells. Dead by Corollary 2.
3. **ω₁-many coarse chunks** (B of countable type over uncountably many
   chunk-atoms, type cells invisible in B): the diffuse state ν_∞ of the
   chunk field remains an eligible σ-lift — by the splitting-freeness
   Lemma A of
   [`oml_cyclic_order_coupling.md`](oml_cyclic_order_coupling.md) each
   Σ_i is σ-value-free over the co-chunk-countable base — so there is no
   σ-kill at all without a ν_∞-exclusion event, and any such exclusion
   is a countable chunk-union, i.e. design 2 one level up. Dead by
   recursion into Corollary 2.

The recursion in design 3 is general: over hereditarily countable-type
bases a finite pattern can force only finitely many diffuse-state
exclusions, and the last one is a countable localizer whose type cells
are measurable. Kept as a strategic reading (not a theorem): finite
patterns cannot bottom out coarse towers by disjointness.

## 5. Surviving directions (Lane A)

1. **Contextual (relay-style) kills of atom-principal lifts** remain the
   only standing engine at fine and countable-type-coarse boundaries —
   unchanged, with all its banked bounded no-gos.
2. **New: regressive/Fodor rigidity.** Over a *stationary* localizer the
   kill could be contextual with the killed pair varying regressively
   (each atom's kill witnessed below it). Fodor's lemma then forces a
   stationary set with a constant witness — a potential *uncountable*
   rigidity engine with no finite type partition to become measurable,
   i.e. the first candidate mechanism that Theorem 1 does not touch and
   Ulam does not supply. Completely unexplored; this is the sharpened
   coarse-side residue.

## 6. Evidence ledger

| Claim | Class |
|---|---|
| Theorem 1, Corollary 2 | hand proved (self-contained, σ-class axioms + banked monotonicity) |
| Proposition 3 + defect anatomy | hand proved (uses Ulam 1930, ZFC) |
| §4 design deaths | hand, instances of Corollary 2 (design 3 via Lemma A of the cyclic note) |
| §4 "recursion" reading; §5(2) Fodor direction | strategic readings, not theorems |
