# Candidate: rotating small-piece graph triple over an Ulam base

*Opened 2026-07-13 (campaign iteration 5). Status: DESIGN SPECIFICATION
with staged gates — no gate beyond the per-column kill logic is claimed
passed. ⟦HAND — design-level; the kill and escape arguments below are
proved conditional on the closure normal form (Gate N), which is open.⟧
This is the first architecture in the campaign that survives, by
construction, every banked obstruction currently on the books; it is
therefore the priority construction target. Iteration 6's bounded
column-trace census passes the local six-cell closure check, but does
not address global closure coincidences; adversarial review of the
global design remains owed.*

## 1. Why this candidate exists

Iteration 4's type-partition obstruction (Theorem 1 of
[`oml_type_partition_obstruction.md`](oml_type_partition_obstruction.md))
killed disjointness-based coarse traps; T1 pointwise resolution
(iteration 2) kills fully resolved overlaps; no-Fubini (Lemma A) kills
marginal value-forcing; 2BR kills two-block patterns; the ω₁-chain kills
naive meet structure. What remains for a σ/f.a. asymmetry:

- **σ-localization without f.a. localization:** on B = P(ω₁)-cylinders,
  every σ-state's B-trace is column-principal (Ulam, ZFC), while free
  f.a. ultrafilters are column-free. No type partition is involved.
- **finite column geometry as the kill:** at its column, a localized
  state dies by *finite* additivity on a designed two-point piece — no
  countable decomposition, no disjoint pattern pair.
- **partial overlap resolution:** each pattern pair's set intersection
  is resolved only on a proper column class, blocking T1, while the
  resolved part is collected into a designed meet event, restoring
  latticehood.

## 2. The data

Carrier Ω = ω₁ × ω₁ (columns col_α = {α} × ω₁; fibre = second factor).
Fix a partition ω₁ = T_1 ⊍ T_2 ⊍ T_3 into three uncountable **column
types**. For each α, with k = the type of α and {i,j} = {1,2,3}∖{k}
(i < j), choose a labelled six-cell partition of the fibre

\[
 \{g_k(\alpha)\}\mathbin{\dot\cup}\{h_k(\alpha)\}
 \mathbin{\dot\cup}W(\alpha)\mathbin{\dot\cup}V_i(\alpha)
 \mathbin{\dot\cup}V_j(\alpha)\mathbin{\dot\cup}R(\alpha)=\omega_1,
\]

with every displayed cell nonempty (and the nonsingleton cells chosen
infinite/cofinal if a later gate needs that extra property). Define:

- r_k(α) = {g_k(α), h_k(α)} — the **small piece**, two points;
- r_i(α) = {g_k(α)} ∪ W(α) ∪ V_i(α);
- r_j(α) = {h_k(α)} ∪ W(α) ∪ V_j(α);

where W(α) (the **unresolved pair-witness region**, giving
r_i ∩ r_j = W(α) ≠ ∅), V_i, V_j (private), and the two small points are
pairwise disjoint and infinite/cofinal as needed. By construction, at a
type-k column: r_i ∩ r_k = {g_k(α)}, r_j ∩ r_k = {h_k(α)},
r_i ∩ r_j = W(α) ≠ ∅, and r_1 ∩ r_2 ∩ r_3 = ∅. **Every pair intersects
at every column; the triple is empty everywhere.**

Generators of L (to be closed under complement and countable disjoint
union — Gate N determines the normal form):

1. B := {A × ω₁ : A ⊆ ω₁} (full first-coordinate cylinder field);
2. Σ_m := ⋃_α {α} × r_m(α), m = 1,2,3 (the three graph events);
3. the column pieces P_m^α := {α} × r_m(α) (forced anyway by
   Σ_m ↔ col_α, which the design requires pairwise);
4. the resolution singletons {(α, g_k(α))}, {(α, h_k(α))} for every α
   (k = type of α);
5. the meet collectors
   defined without an orientation ambiguity as follows. At a type-k
   column (with the other indices i<j), put
   `q_ik(α)=g_k(α)`, `q_jk(α)=h_k(α)`, and leave `q_ij(α)` undefined.
   For each unordered pair `{a,b}`, set
   `G_ab := {(α,q_ab(α)) : α∈T_a∪T_b}`. Thus `G_ab` is empty on the
   unresolved third type, lies in `Σ_a∩Σ_b`, and the three collectors
   are pairwise disjoint. They are deliberately **not** declared closed
   under restriction to uncountable cylinders.

Exclusions (design constraints on the closure, part of Gate N): no
nonzero event below any {α} × W(α); no event equal to Σ_m ∩ Σ_n or to
G_mn ∩ Acyl for uncountable co-uncountable A; the Σ's pairwise
incompatible; each Σ_m compatible with each column and with countable
and co-countable cylinders, but NOT with every element of B.

Pattern p: Σ_1 = Σ_2 = Σ_3 = 1 (⊥-closure adds complements).

## 3. The intended asymmetry (proved modulo Gate N)

**σ-kill.** Let ν be a global σ-additive two-valued state with
ν(Σ_m) = 1 for all m. B is pairwise compatible, so lies in maximal
blocks; ν's restriction there is σ-additive, hence its B-trace is a
σ-complete ultrafilter on a copy of P(ω₁): by **Ulam's theorem it is
principal** — ν(col_α) = 1 for some α. Let k = type(α). The pair
(Σ_k, col_α) is compatible, so pairwise multiplicativity (block of the
pair) gives ν(P_k^α) = 1. P_k^α = {(α,g)} ⊍ {(α,h)} is a two-element
disjoint union of events (generators 4), so **finite** additivity
charges one resolution point, say g = g_k(α). Then {(α,g)} ⊆ Σ_j^c
(g ∉ r_j by construction), and monotonicity gives ν(Σ_j) = 0 —
contradiction. No σ-state charges the pattern.

**f.a. escape (the open crux, Gate F).** A witness μ must be
column-free (μ|B a free ultrafilter U on ω₁) — the kill above uses
finite additivity only, so *any* state charging a column dies; the
asymmetry is exactly that f.a. states need not charge columns while
σ-states must (Ulam). The threats threaded by design:

- **type-partition (Theorem 1 of iteration 4):** the type cells
  T_k-cyl ∈ B are a finite partition, so μ charges one; but on every
  cell every pattern pair intersects pointwise at every column — no
  disjoint pair exists anywhere, and Theorem 1 is silent. Moreover
  Σ_m ∩ T_kcyl need not be an event at all (Σ's are not B-compatible),
  so no cell-level multiplicativity is even available.
- **cell splitting:** the death of the constant-row designs recurred
  when Σ_k ∩ T_kcyl split into two L-graphs each avoiding one Σ. Here
  G_ik ∩ T_kcyl ∉ L (G's incompatible with uncountable cylinder
  restrictions), and only countable subgraphs (countable ⊍ of
  singletons) are events — charged 0 by a column-free μ without
  consequence.
- **2BR / cluster normal form:** value-1 part needs ≥ 3 blocks ✓ (the
  Σ's are pairwise incompatible, pairwise intersecting as sets, with
  empty triple intersection — the exact m = 3 normal form; no Dirac
  charges the pattern since the triple intersection is empty, and no
  carrier point lies in all three).

**Latticehood (Gate L).** Σ_i ∧ Σ_j should be G_ij: lower bounds of the
pair are (modulo Gate N) supported on the resolution graph (W-regions
carry no events; T1 is blocked because W-region points are unresolved),
and every countable-⊍-of-singletons lower bound lies below G_ij. All
other meets to be audited in the normal form.

## 4. Staged gates (stop at first indispensable failure; mine it)

- **Gate N (normal form):** exhibit the ⊍/c-closure of the generators
  explicitly; verify the exclusions of §2 survive closure (no forced
  event below W-regions; no forced Σ_m ∩ Σ_n; no forced uncountable
  graph restrictions). THE critical gate; everything above is
  conditional on it. Failure mode to watch: closure coincidences
  manufacturing forbidden events from complements of countable ⊍'s.
  **Bounded subcheck passed (iteration 6):** the exhaustive six-cell
  trace at one fixed type-k column has 24 events, contains no nonzero
  event below W, omits r_i ∩ r_j = W, isolates exactly g and h, and
  splits r_k. Producer, certificate, and independent verifier are in
  `../verification/census_2026-07-13_campaign_it6/`. This is finite
  column-local evidence only; it does not establish Gate N.
- **Gate L (latticehood/OML):** meets exist for every pair in the
  normal form; expected: designed meets G_mn, poor pairs elsewhere,
  orthomodularity automatic (σ-class + lattice).
- **Gate M (maximal blocks):** exhaustive classification; B-based
  blocks, per-column fibre blocks, Σ-blocks, hybrid ⊍-blocks.
- **Gate C (σ-completeness):** by σ-class construction + OML
  disjointization; verify no uncountable-join obligations sneak in.
- **Gate Z (centre + essential irreducibility):** trivial centre
  expected (columns split everything; Σ's incompatible with cylinders);
  quotient mod countable: B survives (P(ω₁)/ctble), graphs survive as
  nonzero classes? — must be computed, NOT assumed (iteration 1's
  fence: the trap structure must survive the quotient; here the
  G-graphs have countable column-sections but uncountable support, and
  the Σ's have uncountable sections — expected to survive; audit).
- **Gate F (f.a. coherence — the crux):** construct μ ∈ St_fa(L) with
  μ(Σ_m) = 1: a coherent blockwise ultrafilter family over the Gate-M
  classification, column-free, charging each Σ in its own blocks.
  Candidate construction: extend {Σ_m-tails} ∪ {co-countable cylinder
  traces of one fixed free U} blockwise; coherence on overlaps = the
  thing to prove. No banked obstruction applies — but nothing
  guarantees success; this is where the candidate most likely dies,
  and any death must be converted into the next obstruction theorem.
- **Gate Φ (the verdict):** if F passes with the σ-kill intact, p is a
  σ-essential pattern and L refutes the conjecture — subject to the
  full admissibility audit (Gate Z) and adversarial review + (per the
  workflow) Lean formalization of the kill and of Gate N's normal form.

## 5. Honest position

Nothing is banked here beyond: (i) the per-column kill logic (elementary,
conditional on generators 3–4 being events and the pairwise
compatibilities listed); (ii) the threat-model analysis that no
currently banked mechanism exclusion applies to this design. History
says Gate N or Gate F will likely produce a new obstruction rather than
a witness; either outcome is progress. This note exists so the next
session can attack Gate N directly against a fixed specification.

## 6. Evidence ledger

| Item | Class |
|---|---|
| σ-kill argument | hand, conditional on Gate N (events + compatibilities as specified) |
| fixed-column six-cell closure | exhaustive executable certificate + independent verifier; column-local only |
| threat-model threading | design analysis over banked theorems, not a proof of viability |
| Gates N, L, M, C, Z, F | open |
| Ulam's theorem usage | cited (ZFC, Ulam 1930) |

## 7. Gate N partial algebra (campaign continuation)

The closure operation here is Dynkin/σ-class closure, not Boolean
σ-algebra generation. In particular, the full cylinder algebra does **not**
by itself restrict an added graph.

**Lemma 7.1 (one persistently splitting graph).** Let
`cyl(A)=A×F` for every `A⊆I`, and let `S⊆I×F` have both `S_α` and
`F\S_α` nonempty for every column `α`. The smallest concrete σ-class
containing all cylinders and `S` is exactly

\[
 \{\operatorname{cyl}(A):A\subseteq I\}\cup\{S,S^c\}.
\]

*Proof.* The displayed family contains the generators and is closed under
complement. Two cylinders have a disjoint union which is a cylinder. No
nonempty cylinder is disjoint from `S` or from `S^c`, by the two fibre
nonemptiness hypotheses. The only remaining nontrivial disjoint pair is
`S,S^c`, whose union is the full cylinder. Thus it is a σ-class (indeed
there are no new countably infinite disjoint families), and minimality is
immediate. ∎

This is a useful negative control: an argument that “all cylinders are
present, therefore every graph restriction is present” is invalid. Any
forced restriction in the rotating candidate must use interactions among
several graph/collector forms, or a form with empty fibres.

For the intended collector incidence, the three `G_ij` are pairwise
disjoint and each is empty precisely on the unresolved third type. Hence
Gate N immediately forces

\[
 R_G=G_{12}\mathbin{\dot\cup}G_{13}\mathbin{\dot\cup}G_{23}
\]

 and, for each `i`, the residual event/form

\[
 H_i=\Sigma_i\setminus(G_{ij}\mathbin{\dot\cup}G_{ik}).
\]

These are genuine σ-class operations: the collector union is disjoint and
is contained in `Σ_i`, so the difference is obtained from complements and
disjoint union of comparable events. Fibrewise, `H_i` is empty on `T_i`,
and `H_i∩H_j` is exactly the unresolved `W`-region on the third column
type, while the triple intersection is empty. Thus the `H_i` themselves,
not only the collectors, admit arbitrary full-cylinder decorations on their
zero-fibre types. The fixed-column 24-event calculation already
shows that this subtraction does not expose that pairwise intersection
locally. Globally, collectors with an empty type also force decorated forms
`G_ij ⊍ cyl(A)` for arbitrary `A` contained in that empty type. Whether
complements and further disjoint unions of these decorated forms splice a
different collector on `A` is the current missing closure lemma.

**Evidence boundary.** Lemma 7.1 and the displayed forced-event derivations
are hand proved. They neither pass nor fail Gate N. A complete theorem must
classify the decorated multi-graph forms; no claim about an uncountable
collector restriction or a `W`-event is made here.

**Hostile review.** A fresh-context review cleared Lemma 7.1 and every
forced-event derivation after requiring the explicit `q_ab` incidence table
in §2 and the zero-fibre clause for `H_i`. It found no short forbidden-event
derivation. It also emphasized that compatibility with cylinders is not
generator data: Gate N classifies event membership, while compatibility and
meet claims belong to Gate L after the event class is known.

## 8. Decorated upper normal form (campaign iterations 8--18)

The arbitrary-base closure analysis is now in
[`oml_typed_graph_closure_calculus.md`](oml_typed_graph_closure_calculus.md).
It proves the local 24-trace invariant, a same-type pair-polarity theorem,
and an 88-profile three-type transversal invariant. Consequently no nonzero
`W` event, no `Σ_i∩Σ_j`, no unintended singleton collector, and no collector
restriction with uncountable variation modulo countable support is generated.
Proper co-countable restrictions are generated by countable deletion and are
not forbidden. The intended `G_ij` is proved to be the greatest lower bound
of its graph pair, but general latticehood remains unopened.

Gate N remains **open** at one exact equality step: finite-core splicing for
countable disjoint unions of countable-column modifications. The upper
invariants exclude the named fatal traces but do not yet decide membership of
every admissible decorated profile.
