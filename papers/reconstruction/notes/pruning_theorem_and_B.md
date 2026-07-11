# The pruning theorem (phase-parametrized) + theorem-let B: Safe(ρ) is eventually periodic and effectively computable

**Date:** 2026-07-10 (session 7). **Status:** PROVED ⟦HAND⟧ — full proof written
out below (this note IS the proof, not a sketch); instrument-anchored (see
§Verification). **This is Theorem 1 of the shovel plan** (`notes/programme/
shovel_plan.md` §1): the proved, phase-parametrized statement whose sketch-level
closure was recorded in `pruning_k2_theorem.md` (73,728-check adversarial scan,
0 failures).

**What is new here over `pruning_k2_theorem.md`:** the complete written proof
(strand decomposition, assembly, the generator-conjugation lemma, the
non-generator overcount pinned as a lemma with witness), the theorem stated
WITHOUT strong connectivity (not needed — noted, since the downstream class is
SC), exactness for ALL L (not merely cofinite), and theorem-let B assembled
into an effective certificate with a runnable, raw-DFS-anchored instrument
(`oracles/safe_rho_instrument.py`).

---

**✎s18 (2026-07-11): Theorem P is LEAN-VERIFIED —
`formalization/QuerySystem/QuerySystem/PruningTheorem.lean` (receipts
`[propext, Quot.sound]`, not even choice): Steps 2–4 at general k
(`isTR_one_of_isLISC`, `isLISC_of_isTR_one`, `isTR_rot_iff_isTR_one`,
composite `pruning`), for an ARBITRARY relation on an ARBITRARY alphabet
— kit gaps 5.1 and 5.2 discharged. Lemma NG's orbit decomposition and
Theorem B (gap 5.3) are not formalized (instrument-covered).**

## 1. Setting

Finite alphabet A, n = |A| ≥ 1. A relation ρ ⊆ A × A; D = the digraph (A, ρ).
**No strong-connectivity hypothesis** — everything below holds for arbitrary ρ.

**Layered ring.** For L ≥ 1, R_L(ρ) has vertex set ℤ_L × A and arcs
(i, a) → (i+1 mod L, b) for every (a, b) ∈ ρ.

**Lemma 0 (layer clock).** Every arc advances the layer by exactly 1, so a walk
of length t from a layer-c vertex ends at layer c + t (mod L), and position t
of the walk sits at layer c + t (mod L). *Proof:* the arc shape; induction. ∎

**Simple cycles and winding.** A *simple cycle* is a closed walk all of whose
vertices are distinct. By Lemma 0 a closed walk's length m satisfies L | m; its
*winding* is k = m/L. A simple cycle of winding k visits each layer i at
exactly its k positions t ≡ i − c (mod L); those are k distinct vertices at the
same layer, hence **k distinct states per layer — layer-injectivity is
automatic given simplicity** (the adjective in "LISC" is kept for continuity
with the seed's terminology).

- **LISC_k(L)** ⟺ there exists a simple cycle of winding k in R_L(ρ).

**Tuple digraph (the independent proxy).** For 1 ≤ k ≤ n let T_k(ρ) have vertex
set the *injective* k-tuples u ∈ A^k (entries pairwise distinct;
N_k = n!/(n−k)! vertices) and arcs u → v iff (u_j, v_j) ∈ ρ for every j
(the k-fold tensor power restricted to injective tuples — "diagonal-avoiding"
at every step). For r ∈ ℤ_k let σ_r be the *left rotation*
σ_r(u)_j = u_{j+r mod k}.

- **TR_k^{(r)}(L)** ⟺ there exists a walk of length L in T_k(ρ) from some u
  to σ_r(u).

**Unsafe/Safe.** Unsafe(ρ) = {L ≥ 1 : LISC_k(L) for some k ≥ 2};
Safe(ρ) = ℕ_{≥1} ∖ Unsafe(ρ). (Consumer: the winding characterization — ring
reconstruction C_L = R_L exactly on Safe(ρ); see the seed §P18 and
`joint2_wielandt_finding.md`. Not re-derived here.)

---

## 2. Theorem P (pruning, phase-parametrized)

**Theorem P.** For every ρ ⊆ A × A, every L ≥ 1, every k ≥ 1, and every r with
gcd(r, k) = 1:

  LISC_k(L) ⟺ TR_k^{(r)}(L),

witnessed by explicit maps in both directions. The equivalence is **exact for
every L** — not merely cofinite — and needs no strong connectivity.

**Lemma NG (non-generators overcount).** If gcd(r, k) = d > 1, a TR_k^{(r)}(L)
witness assembles into d pairwise vertex-disjoint simple cycles of winding k/d
each — it certifies LISC_{k/d}(L) (with multiplicity d), NOT LISC_k(L), and
LISC_k(L) can genuinely fail while TR_k^{(r)}(L) holds. Witness: C4dir = the
directed 4-cycle, L = 2: LISC₂ holds, LISC₄ fails, TR₄^{(2)} fires.

### Proof of Theorem P

**Step 1 (phase normalization).** Let W be a simple cycle of winding k, length
kL. Its length is ≥ L, so by Lemma 0 it meets every layer; cyclically reindex
(the same cycle) so that W[0] is at layer 0. Then position t is at layer
t mod L, and the k visits to layer i are exactly W[i], W[L+i], …, W[(k−1)L+i].
In particular the visits to layer 0 are L apart: the cycle splits into k
**strands** P_j = W[jL .. (j+1)L] (j = 0, …, k−1), each a path traversing
layers 0 → 1 → ⋯ → 0, with strand j ending where strand j+1 starts
(indices of W mod kL). *Strands are labelled by traversal order.*

**Step 2 (extraction: LISC_k(L) ⟹ TR_k^{(1)}(L)).** Define, for i = 0, …, L,
the tuple τ_i ∈ A^k by τ_i[j] = state of W[jL + i].

- *Injectivity of every τ_i.* For i < L the entries of τ_i are the states of
  the k distinct vertices of W at layer i — distinct vertices at the SAME layer
  have distinct states. For i = L: τ_L[j] = W[(j+1)L], so
  τ_L = (W[L], W[2L], …, W[(k−1)L], W[0]) = σ_1(τ_0), injective because τ_0 is.
  **Off-diagonality is forced by simplicity, not assumed.**
- *Arcs.* Coordinate j of τ_i → τ_{i+1} is the step W[jL+i] → W[jL+i+1], a
  consecutive pair of W, hence in ρ — including the boundary step i+1 = L,
  where W[jL+L−1] → W[(j+1)L] is still a consecutive pair of W.
- *Endpoint.* τ_L = σ_1(τ_0) as computed.

So (τ_0, …, τ_L) is a length-L walk in T_k from τ_0 to σ_1(τ_0). ∎(⟹, r=1)

**Step 3 (assembly: TR_k^{(1)}(L) ⟹ LISC_k(L)).** Given a T_k-walk
τ_0 → ⋯ → τ_L with τ_L = σ_1(τ_0), define a closed walk W of length kL by
placing position t = jL + i (0 ≤ j < k, 0 ≤ i < L) at vertex (i, τ_i[j]).

- *Within strand j* (i < L−1): τ_i[j] → τ_{i+1}[j] ∈ ρ; layers i → i+1. ✓
- *Strand boundary* t = jL + (L−1) → (j+1)L: the walk supplies
  τ_{L−1}[j] → τ_L[j] ∈ ρ, and τ_L[j] = σ_1(τ_0)[j] = τ_0[j+1], which is the
  state at position (j+1)L; layers L−1 → 0. ✓ For j = k−1 this is the closure:
  τ_L[k−1] = τ_0[0] = state at position 0. ✓
- *Simplicity.* Suppose positions t = jL+i and t′ = j′L+i′ carry the same
  vertex. Same layer forces i = i′ (Lemma 0); then τ_i[j] = τ_i[j′] forces
  j = j′ by injectivity of τ_i. So t = t′.

W is a closed walk of length kL with all vertices distinct = a simple cycle of
winding k. ∎(⟸, r=1)

**Step 4 (generator conjugation: r ↦ 1).** Let gcd(r, k) = 1 and r̄ = r^{−1}
mod k. Define the slot relabelling P(u)[j] = u[j r̄ mod k]. Then P is a
bijection of injective tuples, maps T_k-arcs to T_k-arcs (a fixed coordinate
permutation; arcs are coordinatewise), and conjugates the rotations:

  P(σ_1(u))[j] = σ_1(u)[j r̄] = u[j r̄ + 1] = u[(j + r) r̄] = P(u)[j + r]
  = σ_r(P(u))[j].

So (τ_i) is a TR^{(1)} witness iff (P(τ_i)) is a TR^{(r)} witness:
TR_k^{(1)}(L) ⟺ TR_k^{(r)}(L) for every r with gcd(r, k) = 1. With Steps 2–3
this proves Theorem P. ∎

**Proof of Lemma NG.** If gcd(r, k) = d > 1, the orbits of j ↦ j + r on ℤ_k
have size k/d. Given τ_L = σ_r(τ_0), strand j ends at τ_L[j] = τ_0[j+r] =
start of strand j+r, so the strand-concatenation of Step 3 runs along each
orbit separately: each orbit of size k/d closes into a simple cycle of length
(k/d)·L, winding k/d (simplicity within each: injectivity of τ_i as in Step 3);
distinct orbits give pairwise vertex-disjoint cycles (injectivity of τ_i across
all of ℤ_k). Conversely nothing recovers winding k: for C4dir at L = 2,
LISC₂(2) holds — e.g. (0,0)(1,1)(0,2)(1,3) — while LISC₄(2) fails and
TR₄^{(2)}(2) fires via the two disjoint winding-2 cycles. (Machine-checked;
`pruning_k2_theorem.md` rot-check + instrument.) ∎

**Remark (k = 1).** The theorem holds trivially at k = 1: σ_1 = id on 1-tuples,
TR_1(L) = "some closed walk of length L in D", and every closed walk of length
L is simple in R_L because its L positions occupy L distinct layers (Lemma 0).

**Remark (where the phase lives — the seed's 2.2z gap, resolved in the
statement).** The lockstep-exchange model synchronized the two strands of a
winding-2 cycle at relative phase 0 and provably missed real witnesses (seed
§2.2z: strands weave at a nonzero relative phase). In the statement above the
phase is not a free parameter but is *absorbed by the strand decomposition*:
the tuple τ_i reads the k strands at the SAME layer i, across their different
traversal times jL + i — that is exactly the phase the tuple-reachability proxy
"quietly carries." Quantifying over strand interleavings = quantifying over
which rotation σ_r closes the linking; labelling strands by traversal order
makes it σ_1; a labelling realizing σ_r exists iff σ_r is a k-cycle iff
gcd(r, k) = 1 (Step 4), and non-generators are a strictly different, lower-
winding statement (Lemma NG). That is the phase-parametrized content, and it is
where the one real defect in this lane's history lived ("any rotation"
overcounts LISC_{k/d}).

---

## 3. Theorem-let B (eventual periodicity of Safe(ρ), effective)

**Theorem B.** For every ρ ⊆ A × A:

1. **(k-cap)** LISC_k(L) requires k distinct states at each layer, so k ≤ n and
   Unsafe(ρ) = ⋃_{k=2}^{n} LISC_k = ⋃_{k=2}^{n} TR_k^{(1)}  (Theorem P).

2. **(periodicity, effective)** Fix k and let M_k be the N_k × N_k Boolean
   adjacency matrix of T_k(ρ). Then L ∈ TR_k^{(1)} iff (M_k)^L has a 1 at some
   entry (u, σ_1(u)). The power sequence ((M_k)^L)_{L≥0} lives in the finite
   monoid of Boolean matrices, hence is eventually periodic: there are
   s_k ≥ 0, p_k ≥ 1 with (M_k)^{L+p_k} = (M_k)^L for all L ≥ s_k, and the
   minimal pair is found by iterating powers to the first repeat. Any predicate
   of (M_k)^L — in particular membership in TR_k^{(1)} — is then eventually
   periodic with threshold s_k, period p_k.

3. **(assembly)** Finite unions and complements of eventually periodic sets are
   eventually periodic (threshold = max, period = lcm). Hence **Safe(ρ) is
   eventually periodic**, with threshold S = max_k s_k and period P = lcm_k p_k,
   and the full set is described by the finite **certificate**
   (exact table of Safe on [1, S), residue table of Safe on {S, …, S+P−1}),
   all effectively computed from ρ. Membership "L ∈ Safe(ρ)?" is decidable by
   table lookup; the certificate is independently checkable (each entry is a
   reachability fact in a fixed finite digraph).

*Proof.* (1) is the pigeonhole on a layer plus Theorem P. (2): finiteness of
the Boolean-matrix monoid gives a first repeat (M_k)^{t} = (M_k)^{s} with
t > s; the sequence is generated deterministically by right-multiplication, so
it is periodic with period p = t − s from threshold s onward, and the first
repeat gives the minimal (s, p). (3) is immediate bookkeeping. ∎

**Citations (bridge facts, not re-derived).** Eventual periodicity of Boolean
matrix powers is classical (finite-semigroup argument as above). Sharper
index/period bounds are known and citable but NOT load-bearing here — the
brute repeat-search is already effective and certifying: Wielandt's bound
(index ≤ (N−1)² + 1 for primitive N × N), Schwarz 1970 and Dulmage–Mendelsohn
1964 for the reducible case (period = lcm of the cyclicity indices of the
strongly connected components; cf. Kim, *Boolean Matrix Theory and
Applications*, 1982). T_k(ρ) need not be strongly connected even when D is —
this is precisely gap (1) flagged at registration (seed §2.2x) — and none of
the above needs it.

**Scale.** N_k = n!/(n−k)! ≤ n^k; for the class where the programme lives
(n ≤ 5) the largest T_k has 120 vertices — the instrument is instant. The crude
worst-case bound s + p ≤ 2^{N_k²} is never the operative one in practice; the
instrument computes the true minimal (s_k, p_k) directly.

---

## 4. What this banks, and what it does not

**Banked.**
- **Safe(ρ) is provably eventually periodic and effectively computable** — the
  certificate-backed decision procedure an outsider can run on their own
  examples (shovel plan §1's stated payoff). Instrument:
  `oracles/safe_rho_instrument.py`.
- Joint 1 of universal impossibility now rests on a written proof, not a
  scan-backed sketch. The scan (73,728 checks, 0 fail) remains the standing
  counterexample-guard; raw-DFS LISC remains the only trusted LISC oracle.
- The statement is exact (all L) and hypothesis-light (no strong connectivity);
  eventual periodicity enters only through T_k's finiteness.

**Not touched (do not overclaim).**
- **Joint 2** (why non-symmetry forces primitive ⟹ cofinitely-unsafe) — the
  sole conceptual open core of universal impossibility; see
  `joint2_wielandt_finding.md`. Needs an idea, not a formalization.
- The bar-D aperiodic half of L-B (parked with the vacant lot), and the
  winding-2 → full bridge scope caveat on the census-law consumers.
- Lean durability step for this theorem: teed up in `pruning_k2_theorem.md`
  §LEAN DURABILITY (4 design constraints, esp. pin rotation-by-GENERATOR),
  still optional, still not owed.

**Grade.** Theorem P + Lemma NG + Theorem B: ⟦HAND⟧ — full proof above,
machine-verified at scale (the 73,728-check scan for P; the anchored instrument
below for B's certificate). Bridge facts cited. Not Lean.

---

## 5. Verification (instrument, anchored)

`oracles/safe_rho_instrument.py` computes, for each target ρ: the per-k minimal
(s_k, p_k) by Boolean-power repeat-search, the union certificate
(S, P, exact prefix, residue table), and then **anchors** the prediction
against the raw-DFS LISC oracle (independent code path, the trusted one) at
every L in the anchor window, per-k winding sets compared exactly (not just the
union). Any mismatch = FAIL and no certificate is emitted.

### Verification log

- **2026-07-10: instrument run on 15 targets — per-k EXACT match vs raw DFS on
  every anchor point, EVERY window crossing S+P. ZERO failures.** Zoo:
  NAND/golden, full2, rho13, rho5, tournament3, full3, mixed, C4tgt, C4dir,
  adv1–adv5, rho20 (= 2-cycle ⊔ 3-cycle, NOT strongly connected — exercises
  the hypothesis-light form). Windows: L ≤ 8–21 per target (adv4 needed 21 to
  cross its S+P = 20; extended, not silently capped).
- **External consistency (independent ground truth, not fit):**
  - rho20: certificate gives Safe = {L ≡ 0 mod 6} — reproduces the known
    Safe(ρ₂₀) = 6ℤ (seed, census-law context).
  - rho13: certificate gives Safe = {3} exactly (S=11, no safe residues) —
    reproduces P18 (Safe(ρ₁₃) = {3} across L = 3..9), now with the cofinite
    tail CERTIFIED rather than scanned.
  - NAND/golden: Safe = even L — the parity-residue pattern on record.
  - C4dir: Safe = {L ≡ 0 mod 4}; and the Lemma NG discriminator (LISC₂(2)=T,
    LISC₄(2)=F, TR₄^{(2)}(2) fires) confirmed per-k.
- Sample certificates (S, P): rho13 (11, 3); adv2/adv3 (12, 4); adv4 (16, 4)
  — note the genuinely long pre-periodic prefixes on the adversarial
  imprimitive-ish targets: the threshold is REAL, small scans cannot see past
  it, the certificate can.
- **2026-07-10 (s10): fresh-context adversarial proof-read — VERDICT SOUND,
  no finding above cosmetic (adv2≅adv3 isomorphic twins; k=1 remark inert).**
  Every step verified or independently re-derived; 8 receipt scripts
  committed. Full record: `PROOF_READ_2026-07-10_pruning.md`; scripts:
  `../oracles/proof_read_2026-07-10/`. Clears the s7 proof-read debt.
