# Query Systems as Sites: A Sheaf-Theoretic Reformulation of CE

**Branch:** `directedness-interpolation`
**Status:** Exploratory — working through the five definition checks

---

## Setup recap

A **query system** (Paper −1 language) is a tuple `(ι, {Q_i}, {π_{ij}}, {ℓ_i})`
where:
- `ι` is a preordered index set
- `Q_i` is a Boolean algebra (the outcome space / discriminability structure at level `i`)
- `π_{ij} : Q_j → Q_i` for `i ≤ j` are surjective Boolean algebra homomorphisms
  (refinement maps — finer queries map to coarser ones)
- `ℓ_i : Q_i → [0,1]` are normalized finitely-additive charges, compatible:
  `ℓ_i(A) = ℓ_j(π_{ij}^{-1}(A))` for all `A ∈ Q_i`, `i ≤ j`

The structural layer is `(ι, {Q_i}, {π_{ij}})`. The valuation layer is `{ℓ_i}`.

**Collective exhaustion (CE)**: for every level `i` and every decreasing sequence
`A_1 ⊇ A_2 ⊇ ···` in `Q_i` with `⋂_n π_{ij}^{-1}(A_n) = ∅` for some `j ≥ i`,
we have `ℓ_i(A_n) → 0`.

---

## Step 1: The query system as a category

**Definition.** The **category of a query system** `C(ι)` has:
- **Objects**: the Boolean algebras `Q_i` for `i ∈ ι`
- **Morphisms**: `Hom(Q_j, Q_i) = {π_{ij}}` when `i ≤ j` (one morphism per
  comparable pair), and `∅` otherwise
- **Composition**: `π_{ij} ∘ π_{jk} = π_{ik}` for `i ≤ j ≤ k` (transitivity
  of preorder + compatibility of refinement maps)
- **Identity**: `id_{Q_i} = π_{ii}`

**Verification this is a category:**
- Composition is associative: `(π_{ij} ∘ π_{jk}) ∘ π_{kl} = π_{ik} ∘ π_{kl} = π_{il}
  = π_{ij} ∘ (π_{jk} ∘ π_{kl})`. ✓
- Identities work: `π_{ij} ∘ id_{Q_j} = π_{ij} ∘ π_{jj} = π_{ij}` and
  `id_{Q_i} ∘ π_{ij} = π_{ii} ∘ π_{ij} = π_{ij}`. ✓

**Note on direction.** Morphisms go from *finer* to *coarser* (`j → i` when `i ≤ j`).
This is the correct convention: in a projective system, the "maps" go downward
(coarse is the target), so the natural presheaf direction is contravariant in `ι`.
We are working in `C(ι)^op` when thinking of presheaves over the poset.

Equivalently: view the preorder `ι` as a category where `i → j` iff `i ≤ j`
(i.e., `j` is finer). Then the refinement maps `π_{ij} : Q_j → Q_i` form a
**contravariant** functor from `ι` to Boolean algebras — a presheaf of Boolean
algebras on `ι`. This is the natural setting.

---

## Step 2: The covering topology J

We want a Grothendieck topology on `C(ι)` (or equivalently on `ι^op`, the poset
category where arrows go from coarser to finer).

Work in `ι` as a category with `i → j` meaning `i ≤ j` (j is finer).

**Definition.** A **sieve** on `i ∈ ι` is a downward-closed set `S` of morphisms
into `i` in `ι^op` — equivalently, an upward-closed subset `S ⊆ {j ∈ ι : j ≥ i}`
in `ι`.

**The measure-determining topology.** Define `J(i)` to be the collection of sieves
`S` on `i` such that:

> For every `A ∈ Q_i` and every `ε > 0`, there exists `j ∈ S` such that
> `ℓ_j(π_{ij}^{-1}(A))` is `ε`-determined — meaning: `A` is resolved to within
> `ε` by a single level in `S`.

This is **not** yet the right definition — it mixes the structural and valuation
layers. The point of the site-theoretic approach is to put the topology on the
*structural* layer only, independently of any particular charge family `{ℓ_i}`.

**Revised definition — the σ-algebra topology.** Define `J(i)` by:

> A sieve `S` on `i` *covers* `i` if for every decreasing sequence
> `A_1 ⊇ A_2 ⊇ ···` in `Q_i` with `⋂_n A_n = ∅` in `σ(Q_i)`, there
> exists `j ∈ S` and `n` such that `π_{ij}^{-1}(A_n) = ∅` in `Q_j`.

In words: the sieve covers `i` if the refinements in `S` can *witness* the
emptiness of every vanishing sequence in `Q_i`. The cover doesn't compute charges
— it witnesses set-level emptiness.

**Grothendieck axioms check:**

1. **Maximality**: The maximal sieve `S = {j : j ≥ i}` covers `i`, since the
   full system is assumed to witness vanishing (this is part of the setup). ✓

2. **Stability**: If `S` covers `i` and `h : k → i` (i.e., `k ≥ i`... wait —
   pullback goes the other way in `ι^op`). Let's be careful.

   In `ι^op`: morphisms are `i → j` when `i ≥ j` (going from finer to coarser).
   A sieve on `j` in `ι^op` is a set of morphisms `{i → j}` closed under
   precomposition — i.e., an upset in `ι` above `j` (in the original order),
   which is what we want. Pullback of a sieve `S` on `j` along `k → j` (i.e.,
   `k ≥ j` in `ι`) is `S \cap \{l ≥ k\}`.

   Stability: if `S` covers `j` (witnesses vanishing at level `j`) and `k ≥ j`,
   then `S ∩ {l ≥ k}` covers `k`. This says: if witnessing is available from
   level `j` upward, it remains available from any finer level `k ≥ j` upward.

   This holds as long as `π_{jk} : Q_k → Q_j` is surjective (given by assumption).
   A vanishing sequence in `Q_k` pushes forward to a vanishing sequence in `Q_j`
   (by surjectivity), which is witnessed by some `l ∈ S` with `l ≥ j`. If `l ≥ k`
   we're done; if `l < k`, we may need to pass to `max(l, k)` — this requires SUD.

   **Observation**: stability of J requires exactly SUD. Without SUD, the pulled-back
   sieve may not cover. This is where SUD enters the picture in the topos language.

3. **Transitivity**: If `S` covers `j` and every element of `S` is covered by `T`,
   then `T` covers `j`. This is the "local-to-global" principle for witnesses —
   if witnessing can be done in stages, it can be done in one step. This is the
   content of the Daniell-Stone theorem in disguise.

**Summary**: J is a Grothendieck topology on `ι^op` if and only if the query
system has SUD (needed for stability). Without SUD, J fails to be a genuine
Grothendieck topology.

---

## Step 3: The subcanonical condition

A Grothendieck topology `J` on a category `C` is **subcanonical** if every
representable presheaf `よ(U) = Hom(-, U)` is a sheaf for `J`.

In our setting:

- The category is `ι^op` (or `C(ι)^op`).
- A presheaf on `ι^op` is a functor `F : ι → Set` — a covariant functor on
  the original preorder.
- The representable presheaf `よ(i)` sends `j ↦ Hom_{ι^op}(j, i) = {π_{ij}}`
  if `j ≥ i`, else `∅`. This is the "set of refinements of `i` available at
  level `j`."

The sheaf condition for `よ(i)` says: if `{f_k : j_k → i}_{k}` is a covering
sieve and we have compatible sections `s_k ∈ よ(i)(j_k)` (i.e., compatible
refinement maps), there is a unique global section.

For representables, this is automatic if the covering sieve is "generated" by
actual maps in the category — the subcanonical condition holds whenever the
topology is generated by actual morphisms (not phantom ones).

**The more interesting presheaves** are the *charge presheaves*:

Define `F_ℓ : ι^op → [0,1]` by `F_ℓ(i) = ℓ_i` (the charge at level `i`),
with restriction maps `F_ℓ(i ≤ j)(A) = ℓ_j(π_{ij}^{-1}(A))`.

The **sheaf condition for `F_ℓ`** at a covering sieve `S` of `i` says:

> If `{ℓ_j}_{j ∈ S}` is a compatible family of charges on the levels in `S`,
> there is a unique `ℓ_i` on `Q_i` that restricts to each `ℓ_j`.

This is exactly the **compatibility + determination** condition for charges.
Compatibility (given) ensures the family is coherent. Determination (uniqueness)
uses the π-system structure — which requires lower-directedness.

**So the sheaf condition for `F_ℓ` is:**
- **Existence** (gluing): some charge `ℓ_i` is compatible with all `ℓ_j` for
  `j ∈ S`. This is guaranteed by SUD + CE.
- **Uniqueness** (separation): the charge `ℓ_i` is unique. This uses LCD.

---

## Step 4: Is subcanonical ⟺ CE?

The claim to check: **`F_ℓ` is a sheaf for `J` if and only if the charge family
`{ℓ_i}` satisfies collective exhaustion.**

**Forward direction (sheaf → CE):**

Suppose `F_ℓ` is a sheaf and suppose for contradiction that CE fails at level `i`:
there is a decreasing sequence `A_1 ⊇ A_2 ⊇ ···` in `Q_i` with
`⋂_n π_{ij}^{-1}(A_n) = ∅` for some `j ≥ i`, but `ℓ_i(A_n) ↛ 0`.

The sieve `S = {k ≥ j}` covers `i` (it contains the witnessing level `j`).
The family `{ℓ_k}_{k ∈ S}` is compatible. By the sheaf property, the gluing
determines `ℓ_i` uniquely. But the witnessing at level `j` forces `ℓ_i(A_n) → 0`,
contradicting the assumption. ✓ (Needs more care to make precise.)

**Backward direction (CE → sheaf):**

Suppose CE holds. Given a covering sieve `S` of `i` and a compatible family
`{ℓ_k}_{k ∈ S}`, we need to glue to a unique `ℓ_i`.

- *Uniqueness*: two compatible extensions agree on `Q_i` by the compatibility
  condition (charges are determined by their values on the π-system of `Q_i`
  images). Requires LCD structure.
- *Existence*: the charge `ℓ_i` can be defined via the Daniell-Stone extension
  applied to the projective limit. CE is exactly the condition that makes this
  extension σ-additive rather than merely finitely additive.

**Tentative conclusion:** `F_ℓ` is a sheaf for `J` if and only if `{ℓ_i}` is
collectively exhaustive *and* the structural layer has sufficient directedness
(SUD for existence, LCD for uniqueness).

CE is **not** equivalent to the subcanonical condition alone — it is equivalent
to the sheaf condition for the charge presheaf, given the topology `J`. The
topology itself encodes SUD (via stability); CE is the additional condition that
the charge presheaf, not just the representable presheaves, is a sheaf.

---

## Step 5: Does the ultraproduct argument fail for J?

This is the key question for the "mutual aid" programme.

The CE irreducibility argument runs: every point mass `δ_n` satisfies CE; their
ultraproduct `ℓ = ∏_U δ_n` does not; no first-order condition separates them.

Now ask: does the ultraproduct `ℓ` satisfy the sheaf condition for `J`?

**The ultraproduct of sites.** Given query systems `(ι_n, Q_n, π_n, δ_n)`, their
ultraproduct over `U` is a query system `(ι_U, Q_U, π_U, ℓ_U)` where the index
set and algebra structure are ultraproducts in the usual sense.

The topology `J` on each `(ι_n)^op` ultraproducts to a topology `J_U` on
`(ι_U)^op` — but **`J_U` is the ultraproduct topology**, not the topology
determined by witnessing in `ι_U`.

**The gap:** The covering condition in `J` says "there exists `j ∈ S` that
witnesses emptiness of a given sequence." This is an *existential* statement.
Existential sentences *are* preserved by ultraproducts (Łoś's theorem applies to
∃ as well as ∀). So: if each `(ι_n, J_n)` has the witnessing property for a
given sequence, the ultraproduct `(ι_U, J_U)` also has it.

**Wait — this seems to say the ultraproduct argument doesn't fail.** Let's be precise.

The issue is the *type* of quantification:

- CE says: for every decreasing sequence `A_1 ⊇ A_2 ⊇ ···` in `Q_i` vanishing
  in `σ(Q_i)`, the charges tend to zero.

- The "vanishing in `σ(Q_i)`" condition quantifies over `σ(Q_i)` — the
  *σ-algebra generated by* `Q_i`. This is a second-order object: it refers to
  countable Boolean operations, not just elements of `Q_i`.

- An ultraproduct does not generally preserve second-order statements. In
  particular, `σ(Q_U)` ≠ `(σ(Q))_U` in general — the σ-algebra of the
  ultraproduct is not the ultraproduct of the σ-algebras.

**This is the gap the site-theoretic approach may exploit.** The topology `J`
is defined using witnessing conditions that refer to `σ(Q_i)` — second-order
structure. The ultraproduct argument fails precisely here: the ultraproduct
`ℓ_U` inherits the first-order witnessing structure of each `δ_n`, but not the
second-order `σ`-witnessing.

---

## Tentative conclusions

1. **The query system is a site**: `C(ι)` with the topology `J` defined by
   σ-algebraic witnessing is a legitimate site, provided SUD holds (needed for
   stability of `J`).

2. **CE ≠ subcanonical**: CE is not the subcanonical condition on `J`. Rather,
   CE is the condition that the charge presheaf `F_ℓ` is a sheaf — a strictly
   stronger condition than subcanonical (which only requires representables to
   be sheaves).

3. **The ultraproduct argument has a genuine gap in the site-theoretic setting**:
   the topology `J` uses second-order (σ-algebraic) witnessing, which is not
   preserved by ultraproducts. This is the precise point where the CE
   irreducibility argument breaks down if we extend the language to include `J`.

4. **What this does not yet show**: it does not show CE is *derivable* from
   structural conditions in the site language. It shows the irreducibility
   argument cannot be directly applied. Whether CE follows from, say,
   "J-subcanonical + SUD + LCD" is a separate question requiring a proof.

5. **The philosophical upshot**: if CE can be derived from the sheaf condition
   for `J`, then CE is reconceived as: *the charge presheaf is a sheaf for the
   natural topology on the query system.* This is not an observer's commitment
   about mass at infinity — it is the statement that the observer's charges
   are *geometrically realisable* in the site-theoretic sense.

---

## Open questions for further development

- [ ] **Q1**: Is the sheaf condition for `F_ℓ` (charge presheaf) equivalent to
      CE + SUD + LCD, or to CE alone (given SUD and LCD hold)?

- [ ] **Q2**: Is there a purely structural site condition (no valuation) that
      *implies* the sheaf condition for every compatible charge presheaf?
      This would make CE structural.

- [ ] **Q3**: Can the topology `J` be defined without reference to `σ(Q_i)`
      (i.e., using only the Boolean algebra structure)? If so, it is first-order
      and the ultraproduct gap closes again.

- [ ] **Q4**: Is the finite-cofinite content `ℓ` (the canonical CE-failing example)
      a sheaf for `J`? If not — if the ultraproduct topology `J_U` differs from
      the witnessing topology `J` — then we have a structural separation between
      `ℓ` and the point masses, without using CE as a valuation-layer axiom.

- [ ] **Q5**: Does this connect to the **Boolean-valued model** approach to
      forcing? The Stone space `S(Q_i)` is the prime spectrum of `Q_i`; Łoś's
      theorem for Boolean-valued models might give a cleaner account of where the
      ultraproduct argument does and does not apply.

---

## Relationship to the trunk program

If Q4 has a positive answer (ℓ is not a sheaf for J), the program gains a
structural separation of CE-failing charges that does not require CE as a
primitive. The main theorems of Paper −1 would be re-expressible as:

> A charge family is collectively exhaustive iff it is a sheaf for the natural
> site topology on the query system.

This is a strengthening of the current SP1 theorem — same content, richer
language, structural rather than valuation-layer formulation.

The trunk program is unaffected either way: CE remains the correct characterisation
at the current level of language. The site-theoretic reformulation is a
*deepening*, not a *correction*.
