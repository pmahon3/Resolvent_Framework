# Sharp-skeleton evasion of route (i): VERDICT

*Literature settling note — June 2026. Feeds `oml_onboarding.{md,tex}` §4.3(i).*

## The question

The candidate tried to evade route (i) ("OML + RDP ⟺ Boolean") by representing
a concrete OML not as the whole effect algebra but as the **sharp skeleton**
`S(E)` (sharp elements `a`: `a ∧ a′ = 0`) of an ambient monotone σ-complete
effect algebra `E` *with* RDP — the ambient has RDP, the OML itself need not.

Decisive sub-question: in a (monotone σ-complete) effect algebra `E` with RDP,
is the set `S(E)` of sharp elements forced to be a **Boolean** σ-algebra, or
can it be a genuinely non-Boolean orthomodular σ-complete lattice?

## VERDICT: CLOSES-AS-ROUTE-(i)

The sharp skeleton of an RDP effect algebra is **forced Boolean**. The evasion
collapses the same way route (i) does. Clean kill by citation.

## The precise statement + citation

**Theorem (Jenča, Cor. 4.3).** Let `a` be an element of an effect algebra `E`
satisfying the Riesz decomposition property. TFAE:
  (a) `a` is sharp (`a ∧ a′ = 0`);  (b) `a` is central (`a ∈ C(E)`);
  (c) `a` is principal.
— G. Jenča, *Blocks of homogeneous effect algebras*, Bull. Austral. Math. Soc.
**64** (2001), 81–98, Corollary 4.3.

**Theorem (Greechie–Foulis–Pulmannová, Prop. 4.1).** For any effect algebra
`E`, the center `C(E)` is a sub-effect algebra of `E` and is a **Boolean
algebra**.
— R. Greechie, D. Foulis, S. Pulmannová, *The center of an effect algebra*,
Order **12** (1995), 91–106. (Quoted as Prop. 4.1 in Jenča 2001.)

**Composite (the load path).** RDP ⟹ `S(E) = C(E)` ⟹ `S(E)` is a **Boolean
algebra**. That alone kills the candidate: a non-Boolean OML cannot be a
Boolean algebra. σ-completeness is irrelevant to the kill — it does not enter
the load path. (Non-essential add-on: in the monotone σ-complete case `C(E)` is
moreover a Boolean *σ*-algebra; for that detail cite Buhagiar–Chetcuti–
Dvurečenskij on σ-complete EA / effect-tribe representation rather than
asserting it. Do not let this clause shoulder the kill — it doesn't need to.)

**Why "RDP", not merely "homogeneous" (the one real trap).** The early
literature throws up an apparent contradiction: "sharp elements of a
*homogeneous* EA form an **orthoalgebra**, need not be Boolean" vs. "= center,
Boolean." Resolution: `S(E)` is an orthoalgebra whose **blocks are the centers
of the blocks of `E`** (Jenča structure theorem). A *multi-block* homogeneous
EA can therefore have non-Boolean `S(E)` (e.g. Ex. 5.7's Wright triangle:
three blocks, `S(E)` a non-lattice OMP). But **RDP forces a single block** (a
block is a maximal sub-EA with RDP; if `E` itself has RDP it is its own unique
maximal such sub-EA), collapsing `S(E)` to the single center `C(E)`. So the
non-Boolean cases are exactly the *non-RDP* (multi-block) ones, and the kill
lives strictly on the RDP side. "homogeneous ⊋ RDP" is doing the work.

**Mechanism (one line).** In an RDP algebra every sharp element is *principal*,
so `[0,a]` is a Riesz ideal and `a` splits `E` as a direct factor — i.e. `a` is
central. Centrality is the same direct-factor/idempotent phenomenon whose
carriers always form a Boolean algebra.

## The contrapositive is in the SAME paper (sanity check)

Jenča's **Example 5.7** builds a homogeneous EA `E` whose `S(E)` is a
*non-lattice-ordered OMP*, and argues: if `E` had RDP then by Cor. 4.3
`S(E) = C(E)` would be Boolean — contradiction, since `S(E)` is not even a
lattice. So a non-Boolean sharp skeleton is *exactly what witnesses failure of
RDP*. Non-Boolean `S(E)` and RDP are mutually exclusive, confirmed from both
directions. (Cf. Jenča's structure theorem: `S(E)` is an orthoalgebra whose
blocks are the centers of the blocks of `E`; an RDP algebra is a *single*
block, so `S(E) = C(E)`.)

## One-line addition for oml_onboarding §4.3(i)

> The "sharp-skeleton" evasion (represent the OML as the sharp elements of an
> ambient RDP effect algebra, so only the ambient carries RDP) also closes: in
> any RDP effect algebra the sharp elements *coincide with the center* and are
> therefore Boolean (Jenča 2001, Cor. 4.3, via Greechie–Foulis–Pulmannová 1995)
> — a non-Boolean sharp skeleton in fact *witnesses* RDP-failure (Jenča 2001,
> Ex. 5.7). So route (i) is closed against this refinement too.

## Sources
- G. Jenča, *Blocks of homogeneous effect algebras*, Bull. Austral. Math. Soc.
  64 (2001), 81–98. (Cor. 4.3; Prop. 4.1; Ex. 5.7; arXiv:1504.00354.)
- R. Greechie, D. Foulis, S. Pulmannová, *The center of an effect algebra*,
  Order 12 (1995), 91–106.
- A. Dvurečenskij, Y. Xie, *Atomic Effect Algebras with the Riesz
  Decomposition Property*, arXiv:1203.0111 (RDP EA = interval `G⁺[0,u]` in an
  interpolation po-group — the structural backbone).
- J. Paseka, *The role of meager elements in homogeneous effect algebras*
  (block = maximal sub-EA with RDP).
