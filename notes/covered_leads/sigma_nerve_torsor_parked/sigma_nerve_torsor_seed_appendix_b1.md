# Appendix: Layer-0 and B1 hand proofs

> **PROVENANCE BANNER:** frame LLM-originated (design conversation,
> Claude Fable 5, 2026-07-17); see the seed's banner. All proofs below are
> ⟦HAND⟧, written fresh this session at the stated generality. Novelty is
> NOT claimed here; the Task-3 verdict table governs. No Lean until
> novelty is settled.

Setting: L a concrete σ-class on Ω (∅ ∈ L, complement-closed, closed
under countable disjoint unions; order = inclusion). "σ-complete OML"
adds: (L, ⊆) has all binary meets (equivalently joins, by complements).
Cited without proof (banked, Lean-certified where noted): comparable
differences b∖a = (a ⊍ bᶜ)ᶜ ∈ L for a ⊆ b; blocks are σ-fields
(ConcreteOMLBlocks.lean); orthogonal families extend to blocks; two-valued
σ-additivity is blockwise (A1c).

## A. Countable increasing sups (L0.1)

**Lemma A.1.** If a₁ ⊆ a₂ ⊆ … is a countable increasing chain in a
concrete σ-class L, then ⋃ₙaₙ ∈ L and it is the least upper bound.

*Proof.* The differences dₙ = aₙ₊₁∖aₙ are events (comparable
differences), pairwise disjoint, and disjoint from a₁; so
⋃ₙaₙ = a₁ ⊍ ⨆ₙdₙ ∈ L by countable disjoint-union closure. Any upper
bound contains the union as a set, and the union is an event, so it is
the sup. ∎

**Scope warning (load-bearing).** Countability is essential twice: the
dₙ family must be countable to take its disjoint union, and nothing is
claimed for chains of uncountable cofinality — an ω₁-chain's union need
not be an event. Every "sup = union" step below inherits this
restriction.

## B. Countable lattice-completeness of concrete σ-complete OMLs (L0.2)

**Proposition B.1.** Let L be a concrete σ-complete OML and (aₙ) any
countable family. Then ⋁ₙaₙ exists and equals ⋃ₙ(a₁∨…∨aₙ); dually all
countable meets exist. In general ⋁ₙaₙ ⊇ ⋃ₙaₙ, and the containment can
be strict.

*Proof.* bₙ = a₁∨…∨aₙ exists by latticehood and increases; Lemma A.1
gives b = ⋃ₙbₙ ∈ L. Each aₙ ⊆ b; any event above all aₙ is above every
bₙ (join = least upper bound), hence contains ⋃bₙ = b as a set; so b is
the least upper bound of (aₙ). Meets by de Morgan (complement is set
complement). Strictness of the overshoot at the binary stage is banked
finite data: the Campaign residue events ρ = C∖m with join overshoot
nonempty (four-residue squares of gate-avoiding terminals). ∎

**Remark (scope-fenced per Phase-2 audit).** The countable join may
overshoot the set union exactly because the finite joins already
overshoot; the increasing-chain step itself adds nothing (sup of the
chain = union of the chain). So all **countable** overshoot in a
σ-complete concrete OML is finitary in origin. ⚠ This is NOT a σ-scale
B2 mechanism: at uncountable cofinality no joins are asserted to exist
at all, so the statement is vacuous exactly where B2's hard case lives.

**Post-audit status of §C:** C.2/C.3 are KNOWN — Navara, *The integral
on σ-classes is monotonic*, Rep. Math. Phys. 20 (1984), confirmed by the
Phase-2 audit. Only the §D localization remains as candidate residue;
cite Navara for monotone continuity.

## C. Tails, limsup, monotone continuity, Fatou (B1)

Throughout C, L is a concrete σ-complete OML, (aₙ) ⊆ L, and s a
σ-additive state (σ-additivity = blockwise σ-additivity by A1c; for
two-valued states this is the banked statement, for [0,1]-valued states
the same proof applies verbatim since a countable orthogonal family plus
its sup lies in one block).

**Definition C.1 (tails).** bₘ = ⋁_{n≥m} aₙ (exists by B.1);
limsup aₙ = ⋀ₘ bₘ; dually liminf. All exist by B.1.

**Proposition C.2 (monotone continuity).** If aₙ ↑ a (increasing with
join a) then s(aₙ) → s(a); dually for decreasing meets.

*Proof.* By B.1, a = ⋃aₙ = a₁ ⊍ ⨆dₙ with dₙ = aₙ₊₁∖aₙ. The family
{a₁, d₁, d₂, …} is pairwise orthogonal, so it lies in one block with its
sup; blockwise σ-additivity gives s(a) = s(a₁) + Σₙ s(dₙ) =
lim s(aₙ₊₁), using finite additivity of s on each aₙ₊₁ = a₁ ⊍ d₁ ⊍ … ⊍ dₙ.
Decreasing case by complements. ∎

**Proposition C.3 (Fatou).** s(limsup aₙ) ≥ limsup s(aₙ) and
s(liminf aₙ) ≤ liminf s(aₙ).

*Proof.* bₘ ≥ aₙ for n ≥ m gives s(bₘ) ≥ sup_{n≥m} s(aₙ) ≥
limsup s(aₙ). bₘ decreases to limsup aₙ, so C.2 gives
s(limsup aₙ) = lim s(bₘ) ≥ limsup s(aₙ). Dual by complements. ∎

**Non-claims.** C.2/C.3 use nothing beyond: countable disjoint closure,
comparable differences, latticehood (for tails), and blockwise
σ-additivity. They are exactly the classical Boolean proofs transported;
the expected verdict is that the components are classical (see the
seed's P1/P3 threats — Navara's monotonic-integral paper and the PP91
monograph). No novelty is claimed for C.2/C.3 as statements.

## D. The localization (the sharp sentence, worked on the witness)

**Claim D.1.** On the machine-checked product-Ulam OMP witness
(`papers/sigma_essential/witness_candidate/`, the amended-Ψ carrier), the
construction of §C fails at exactly Definition C.1: there exist
Specker-incompatible sequences (aₙ) with no join, hence no tail events
b_m, hence no limsup/liminf and no Fatou machinery — while §A and the
blockwise theory survive unchanged (the witness is a σ-class; orthogonal
families still confine to blocks).

*Proof sketch, worked.* The witness carrier is a concrete σ-class OMP
whose defining feature (banked, machine-checked) is that certain pairwise
families are Specker-incompatible: every common upper bound set is
nonempty (Ω qualifies) but no least one exists in the family — joins of
the relevant finite subfamilies already fail, and a fortiori the
countable joins bₘ do not exist. §A (increasing sups) still holds — it
needs only σ-class axioms. §B's proof breaks at its first step
(bₙ = a₁∨…∨aₙ undefined). §C.2 survives for monotone sequences whose
sups happen to exist (increasing unions), but tails, limsup, and C.3 are
unavailable. ∎

**Localization statement (the candidate banked result, novelty
pending).** For the blockwise σ-state engine on concrete σ-classes,
**latticehood is used exactly at the existence of tail events**: every
other ingredient (increasing sups, block confinement, blockwise
σ-additivity, assembly) is σ-class-general. The lattice/poset dividing
line for the Fatou package is tail-existence, certified against the
machine-checked witness where the package fails at precisely that step.

**Honesty note.** If P1/P3 verification shows the monotone-continuity/
Fatou components stated at σ-OML generality in the literature (expected),
the seed's Type-4 bar rests on the localization sentence alone plus the
witness certification; per the seed's declaration, that bar is then
marked AT RISK, not silently substituted.
