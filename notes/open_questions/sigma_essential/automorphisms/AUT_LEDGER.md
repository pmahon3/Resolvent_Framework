# Aut(L) for the product Ulam carrier -- verdict ledger
Date: 2026-09-16. Carrier: Def 5.2, papers/sigma_essential/sigma_essential_body.tex.
Status: paper proofs, HAND. Nothing formalized in Lean (see LEAN STATUS).
Label->number map verified against sigma_essential.aux.
**Erratum 2026-09-22 (D-lr / error 10):** the repo facts behind D-lr are wrong. It is written `(LR_*)` in
docs/s11_quarantine_generality.md, "three-cell star" also appears in docs/psi_lat_attack_surface_ledger.md, and
oml_attack IS the Psi_lat thread. See ../section5_audit/LEDGER.md (D-lr-fact, D-lr-thread, N-*). No Aut content changed.

## 1. Ledger

| ID | Claim | Verdict | One-line reason | Location |
|----|-------|---------|-----------------|----------|
| A-cat | "Aut(L) = ortholattice automorphisms" | **MALFORMED** | Cor 5.11 proves L is NOT a lattice; no such group. Restated for ORTHOPOSET automorphisms. | TASK_A_PROOF.md |
| A | Aut(L) ~= Stab(L) = {pi in Sym(Omega) : pi(L)=L} | **PROVED** (as restated) | Atoms=singletons; L atomistic; order-iso preserves sups; so phi=pi(-). | TASK_A_PROOF.md Thm A |
| A-gen | A needs only "L contains all singletons" | **PROVED** | Proof uses no Ulam matrix/cores/invariant/rigidity. Generic to concrete orthoposets. | TASK_A_PROOF.md |
| A-r1 | Route 1 (atoms) works | **PROVED** | Steps 1-6; the content is atomisticity for UNCOUNTABLE E. | TASK_A_PROOF.md |
| A-r2 | Route 2 (states) works | **SUPPORTED** | Works, but consumes Thm 5.13 (rigidity) unnecessarily; proves strictly less. | TASK_A_PROOF.md |
| A-r2w | Worry: does phi preserve countable orthogonal joins? | **DISSOLVED** | In a sigma-class a countable orthogonal join IS the sup; order-isos preserve existing sups. | TASK_A_PROOF.md Step 1 |
| A-perp | perp-preservation must be assumed | **REFUTED** | Automatic: pi bijection => pi(Omega\E)=Omega\pi(E). Clause (ii) redundant. | TASK_A_PROOF.md Step 5 |
| B-S3 | Fibre action = S_3 on cores, fixing fibre 4 | **REFUTED** | Full S_4 acts: L is perp-closed, so the invariant family is the SIX weight-2 fibre sets, stabiliser = Sym(4) (order 24). Brute-forced. | TASK_B.md B0(a) |
| B-prod | Aut factors as (sigma,tau) in Sym(M) x Sym(F) | **REFUTED** | Transposition of (a0,1),(a0,2) has support 2, lies in Stab(L) by Lem 5.3(3), mixes coordinates. | TASK_B.md B0(b) |
| B1 | pi must preserve the fibre partition | **REFUTED** (exactly); **UNDETERMINED** (mod ctble) | Same 2-cycle breaks it exactly. Mod countable: whether Stab(L) even permutes the 3 weight-2 cosets is UNDETERMINED (see B1-int). | TASK_B.md B1 |
| B1-int | Intrinsic weight-2 vs diagonal separator exists | **UNDETERMINED** | Forward dir PROVED (Lem 5.6(IV)+5.7). Backward FALSE as stated: E=Omega is diagonal yet satisfies the RHS vacuously. General backward dir reduces to the matrix-dependent Afrak question (B2). | SEPARATOR_CHECK.md |
| B2 | pi must preserve the cell family {D_{a,n}} | **MALFORMED** | Cells are GENERATORS, not invariants. Answerable restatement (diagonal sigma-algebra mod ctble) is UNDETERMINED. | TASK_B.md B2 |
| B3 | Parity code E_4 constrains the fibre action | **REFUTED** | All 24 of Sym(F) preserve E_4 (permutations preserve Hamming weight). The order-6 stabiliser is of N, and N is a non-invariant normalisation choice. | TASK_B.md B3 |
| B-quot | **Fibre subgroup** id_M x Sym(F) acts on the 3 complement pairs through S_4/V_4 ~= S_3 | **PROVED** | Kernel = V_4 = {e,(12)(34),(13)(24),(14)(23)}, image order 6. Brute-forced; needs no separator. Claim is about the fibre subgroup ONLY, not all of Stab(L). | TASK_B.md B1 |
| B-ctble | Sym_ctble(Omega) is a normal subgroup of Stab(L) | **PROVED** | Lem 5.3(3) + supports map to supports under conjugation. | TASK_B.md B0(b) |
| B-full | Full determination of Stab(L) | **UNDETERMINED** | Diagonal side depends on the arbitrary g_beta of Lem 5.1; no choice-free answer. Fence, not a gap to close. | TASK_B.md summary |
| C1 | Projection lattice: dim>=3 => unitary/antiunitary, PU(H) x| Z_2 | **SUPPORTED, 2 corrections** | (i) it is UHLHORN not Wigner (ortholattice = orthogonality-preserving hypothesis); (ii) "PU(H) x| Z_2" needs COMPLEX H -- real H gives PO(H), no Z_2. dim>=3 correct & sharp; separability not needed. | TASK_C.md C1 |
| C2 | Frucht-style: every group is Aut of some OML | **CONFIRMED for FINITE; UNDETERMINED for infinite** | NOT a confabulation. Schrag, PAMS 55 (1976) 243-249, via Sabidussi 1957. Found on the shelf in Kalmbach 1983. Claim overstated "every group": theorem is finite groups, finite OMLs. | TASK_C.md C2 |
| C3 | Aut(MO_2,<=)=24, ortho-Aut=8 | **PROVED** | Brute-forced both. Ortho group = Z_2 wr Z_2 = D_4. Task A's framing survives; MO_2 fails A's hypothesis. | TASK_C.md C3 |
| D | Any of A-C bears on the paper | **REFUTED (nothing)** | A is generic, so says nothing about THIS carrier; (a)-(c) each fail on proof economy or transfer. | TASK_D.md |
| D-lr | "(LR*) three-cell star" is a paper item | **MALFORMED** | "three-cell star" is in notes/programme/frontier_map.md l.94 = oml_attack Campaign 11, NOT this paper; "(LR*)" occurs nowhere in repo. Cross-thread conflation. | TASK_D.md (d) |

### What would refute each (required by the protocol)
- **A**: an orthoposet automorphism of L not of the form E|->pi(E) -- equivalently a
  non-singleton atom of L, or two distinct elements of L with the same set of atoms.
  Both impossible since L subseteq P(Omega) and all singletons are in L.
- **A-gen**: a complement-closed family L subseteq P(Omega) with all singletons whose Aut exceeds
  Stab. Refuted by the proof (which uses neither sigma-closure nor orthomodularity).
- **B-S3**: a tau in Sym(F) with (id x tau)(L) =/= L. None: checked all 24.
- **B-prod**: showing every finite-support permutation fails to preserve L -- contradicted by Lem 5.3(3).
- **B1-int**: REFUTED as stated -- E=Omega is exactly such an element. To REVIVE a separator
  one needs an uncountable diagonal [E] that is a non-atom of L/ctble; by Cor 5.10 the cores
  ARE atoms, and whether cells are reduces to the matrix-dependent Afrak question.
- **B-full**: a proof that Stab(L) is independent of the choice of Ulam matrix -- would
  convert the fence into a theorem. I did not attempt this.
- **C1**: an orthogonality-preserving ray bijection of a complex dim>=3 H not unitarily/antiunitarily induced.
- **C2 (finite)**: a finite group not arising as Aut of a finite OML. **C2 (infinite)**: needs a source either way.
- **C3**: a miscount -- brute force says otherwise.
- **D**: exhibiting a proof in the paper genuinely shortened by the S_4 action. I checked Cor 5.12 and it is not.

## 2. Errors in the claim list (NOT empty)

1. **"ortholattice automorphisms of L"** -- L is provably not a lattice (Cor 5.11),
   a fact stated in the task's own context paragraph two sentences earlier. The
   claim is self-inconsistent. Everything must be read in the orthoposet category.
2. **"S_3 permuting the three cores while fixing fibre 4"** -- wrong group. The
   error is taking the CORES as the invariant family; L is perp-closed, so the
   invariant family is the six weight-2 fibre sets and the group is S_4. Fibre 4
   is not distinguished, because M x {4} (odd weight) is not in L -- L cannot see it.
3. **"the parity code E_4 ... so the fibre action must preserve the code's
   structure. Compute the subgroup of Sym(F) preserving the normalised pattern
   set N"** -- right for the wrong reason, then wrong. E_4 IS preserved, but by
   all 24 elements (it is defined by weight alone), so it constrains nothing.
   N is not an invariant: normalisation picks one representative per complement
   pair, a bookkeeping convention in Def 5.4, not a feature of L.
4. **"Is the product form (sigma,tau) forced"** -- presupposes exact product form
   is on the table; countable-support permutations kill it in two lines. The
   question is only meaningful mod the countable ideal.
5. **"Must pi preserve the cell family?"** -- category error: generators are not
   invariants. (The task half-anticipates this with "only up to countable
   perturbation" but the deeper issue is that the cells are a presentation.)
6. **Route 2's stated worry is a non-issue** -- "does phi preserve countable
   orthogonal joins, not just finite ones?" Orthogonal joins in a sigma-class are
   suprema; order-isomorphisms preserve existing suprema. One line.
7. **"By Theorem 5.13 all such are Dirac, so ... "** -- correct, but the task
   frames Route 2 as a peer of Route 1. It is not: it consumes the paper's hardest
   local ingredient to prove something that needs none of it.
8. **"Aut ~= PU(H) x| Z_2, via Wigner"** -- the ortholattice statement is Uhlhorn's,
   not Wigner's (different hypothesis: orthogonality vs transition probability);
   and the group formula silently assumes COMPLEX H.
9. **"every group arises as the automorphism group of some OML"** -- overstated;
   Schrag's theorem is FINITE groups and FINITE OMLs. (But the claim was right to
   exist -- it was graded "possibly a confabulation" and is not one.)
10. **"the (LR*) three-cell star calculation"** -- not in this paper; belongs to the
    oml_attack campaign thread. "(LR*)" is nowhere in the repo.
11. **Minor**: "Corollary 5.11 says L is not a lattice" -- correct, but 5.11 also
    carries the incompatibility of A_1,A_2; and the missing-meet content the task
    attributes to 5.9 is jointly 5.9+5.10 (the lower-bound computation is Cor 5.10's
    last clause). Numbering otherwise checks out against the .aux.

## 3. Corrected claim list

- **A'** (PROVED). For any set Omega and any family L subseteq P(Omega) containing every
  singleton and closed under complement (sigma-closure and orthomodularity are NOT used): the orthoposet automorphism group of L is isomorphic
  to Stab(L) = {pi in Sym(Omega) : pi(L)=L}, via pi |-> (E |-> pi(E)). Moreover
  perp-preservation is automatic, so this is also the ORDER-automorphism group.
  The product Ulam carrier satisfies the hypothesis.
- **B1'** (PROVED). S_4 = Sym(F) embeds in Stab(L) via tau |-> id_M x tau.
- **B2'** (PROVED). Sym_ctble(Omega) <| Stab(L); hence no exact product decomposition.
- **B3'** (PROVED). The action of the fibre group on the three weight-2 cosets of
  L/ctble is the quotient S_4 -> S_4/V_4 ~= S_3.
- **B4'** (UNDETERMINED). Whether weight-2 vs diagonal classes are order-theoretically
  definable mod countable is OPEN (the natural separator is false; SEPARATOR_CHECK.md).
  So `Stab(L) -> Sym(3)` is NOT known to be well-defined: no argument here excludes a
  pi in Stab(L) carrying a weight-2 class to a diagonal one. What IS proved is the
  fibre-subgroup statement B3'.
- **B5'** (UNDETERMINED, fenced). The kernel of Stab(L) -> Sym(3) modulo Sym_ctble is
  the automorphism group of the diagonal sigma-algebra mod countable. It is
  matrix-dependent (Lem 5.1 fixes arbitrary injections g_beta), so there is no
  choice-free answer, and I do not claim one.
- **C1'** (SUPPORTED). For a COMPLEX Hilbert space of dim >= 3 (separability not
  needed), every ortholattice automorphism of the projection lattice is induced by a
  unitary or antiunitary operator [Uhlhorn 1963; Varadarajan 1985], giving
  1 -> PU(H) -> Aut -> Z_2 -> 1, split, so PU(H) x| Z_2. For REAL H: Aut = PO(H), no Z_2.
  dim >= 3 is sharp (dim 2 fails).
- **C2'** (CONFIRMED / partly UNDETERMINED). Every FINITE group is Aut of some FINITE
  OML [Schrag, PAMS 55 (1976) 243-249, via Sabidussi, Canad. J. Math 9 (1957) 515-525].
  The infinite case is not established here.
- **C3'** (PROVED). |Aut(MO_2,<=)| = 24; |Aut(MO_2,<=,perp)| = 8 ~= Z_2 wr Z_2 ~= D_4.
- **D'** (REFUTED). None of A-C bears on the paper. Do not add this line to it.

## 4. LEAN STATUS

**Formalized: nothing. Attempted: nothing. This is a deliberate stop, per the
task's "if the Lean cost looks high, say so and stop at the paper proof."**

Rationale. The mathematical content of Theorem A is (i) atoms = singletons and
(ii) E = union of its singletons -- both trivial in a set-theoretic model -- plus
the transport of an order-isomorphism along them. To get a Lean receipt one must
first build an orthoposet-automorphism group structure, which does NOT exist
anywhere in formalization/QuerySystem/ (ConcreteOMLBlocks.lean is about blocks
and compatibility, not automorphisms). That is substantial scaffolding --
a bundled Aut structure, its group instance, the Stab subgroup of Equiv.Perm,
and the isomorphism -- for a statement whose hand proof has no step that could
plausibly hide an error. The receipt would certify the scaffolding, not the math.

**What would change this call:** if Task D had found an automorphism-invariance
route that shortened Cor 5.12, the S_4 action would need a receipt. It did not
(D is a clean negative), so there is nothing here worth the Lean cost.

**No `sorry` was introduced anywhere; no Lean file was modified.**
