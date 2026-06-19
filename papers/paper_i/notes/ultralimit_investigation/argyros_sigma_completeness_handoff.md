# Strategy D step 1 — reduced state of "is Clop(βYₙ) σ-complete?"

> **⚠ SUPERSEDED 2026-06-18 — RESOLVED WITH WITNESS.** `Clop(Y,𝔗)` is **NOT**
> σ-complete (elementary field-of-sets witness at `0̄`: the gap family
> `A_k = [0^{k-1}11]`). The Argyros pre-Gleason algebra is a **ZFC Strategy D
> example**. The "lean toward route-closed / basically disconnected" prior below was
> WRONG — it analyzed only `V_Σ`-built families and missed the trivial
> usual-topology witness at `0̄ ∉` any `V_Σ`. The obstruction premise ("only
> `V_Σ`-accumulation makes new closure points") is FALSE. The GJ/β₀Y/strong-zero-dim
> machinery is correct but MOOT. See **`argyros_sigma_completeness_RESOLVED.md`**.
> The text below is retained as the (now-closed) reduction trail.

*Reduction note, 2026-06-11. Companion to `argyros_sigma_completeness_scratch.md`
(the in-progress working file, reviewed and found sound). This note records the
SHARP reduced question, the lever to attack it, and the evidence that the easy
attacks fail — NOT a verdict. The verdict (is βYₙ basically disconnected?) is
expert-level set-theoretic topology, not Lean-checkable, with low prior of a clean
positive; it is deliberately NOT hand-derived here (per CLAUDE.md: proof/architecture
is the human's, LLM proofs unverified are not trusted). This is a reduction +
handoff, not a solution.*

## The question (unchanged, now precisely grounded)

Is **`Clop(Yₙ)` σ-complete**? Equivalently (Loomis–Sikorski / Stone): is
`St(Clop Yₙ) = β₀Yₙ` (the Banaschewski / universal zero-dimensional
compactification) **basically disconnected** (closure of every cozero set open)?
The dossier (line 572) confirms `Clop(βYₙ) ≅ Clop(Yₙ)`, so "βYₙ" and "Yₙ" name the
same Boolean question — the scratch note's reframe to `Clop(Y)` is the right object,
**and Y's own non-compactness is irrelevant** once the question is read
Boolean-algebraically.

If NOT σ-complete → `Clop(Yₙ)` is non-σ-complete, non-atomic (no isolated points),
measure-free (Argyros Thm 1.9) → **a ZFC Strategy D example**. If σ-complete →
route closed, fall back to a consistency construction (attack mode C, ◇/CH).

## The construction, verified against Argyros 1983 (PJM 105:2), §1.0–1.3

- `Y = {0,1}^ω` as a set; topology `𝔗` has **subbasis**: (a) all usual product-clopens
  of `{0,1}^ω`; (b) `{V_Σ : Σ a branch of the tree T}`.
- Tree `T = ⋃_n T_n ⊂ [ω]²`: choose pairwise-disjoint triples `S_{n,j} ∈ [ω]³`
  (`1≤j≤3ⁿ`); `T_n = ⋃_j [S_{n,j}]²` (the 2-subsets), `|T_n| = 3^{n+1}`. Successor
  rule (§1.1) links `s∈T_n` to `t∈T_{n+1}` when `s,t ∈ [S_{n+1,j}]²`.
- For `s={k,l} ∈ [ω]²`: `K_s` = **anti-diagonal** of `{0,1}^s` = `{(k↦1,l↦0),(k↦0,l↦1)}`
  (the two points where coords `k,l` **differ**).
- `V_Σ = ∏_{s∈Σ} K_s × {0,1}^{ω∖∪Σ}` — constrains each pair on the branch to its
  anti-diagonal. `V_Σ` is usual-**closed**, hence `𝔗`-**clopen**.
- Basic `𝔗`-clopen (§1.2): `V = U ∩ ⋂_{j=1}^k V_{Σ_j}`, `U` usual-clopen, `Σ_j`
  branches. The **§1.3 Lemma** (FIP criterion) governs when such intersections are
  nonempty — it is Argyros's measure-free engine, aimed at property (*), and almost
  certainly says **nothing** about σ-completeness directly. Do not expect the source
  to hand the answer over.

## Evidence the easy attacks fail — THREE families killed by one mechanism (2026-06-12)

Three natural candidate non-σ-completeness families all turn out to **have** sups,
and the third reveals *why* — a structural obstruction, not bad luck:

1. **Single-branch complement** (scratch note). For one branch `Σ`,
   `V_Σ = ⋂_n U^n` (decreasing usual-clopens), so `Aₙ = Y∖U^n` increases to
   `Y∖V_Σ`, which is **clopen** (since `V_Σ` is) — set-union in the algebra = sup. ✗
2. **Coordinate / all-zeros family.** `Cₙ = [0ⁿ1]`. The point `0̄=(0,0,…)` lies in
   **no** `V_Σ` (every pair-restriction of `0̄` is the diagonal `(0,0)`, not the
   anti-diagonal `K_s`), so `𝔗` = usual topology locally at `0̄`. Then `⋃ₙ Cₙ = Y∖{0̄}`,
   `𝔗`-closure `= Y` (`0̄` a limit), every clopen upper bound `= Y`, `sup = Y`. ✗
3. **`V_Σ`-accumulation to a limit branch** (this session). Take branches
   `Σ_1, Σ_2, …` sharing longer initial segments, converging to a limit branch `Σ*`;
   set `A_k = V_{Σ_k}`. One *can* show `V_{Σ*} ⊆ cl_𝔗(⋃_k V_{Σ_k})` (an overshoot —
   post-divergence pairs of `Σ*` and `Σ_k` live on **disjoint** triples, so the
   anti-diagonal constraints are jointly satisfiable, so every `𝔗`-nbhd of an
   `x∈V_{Σ*}` meets some `V_{Σ_k}`). **But this does NOT give a witness**, and the
   reason is the obstruction: `V_{Σ*}` is itself a *subbasic `𝔗`-open* set, so every
   overshoot point is **interior** to the closure. The closure is then
   `(open union) ∪ (interior overshoot) = OPEN`, so the sup exists. ✗

**The obstruction (the real finding).** A non-σ-completeness witness needs a
countable clopen family whose union has **non-open** `𝔗`-closure — i.e. a closure
point that is **not interior** to the closure. But the new closure points produced
by `V_Σ`-accumulation always land *inside* an open `V_Σ`, hence interior. So
**`V_Σ`-built families cannot witness non-σ-completeness** — the same mechanism kills
all three. (This is a strong structural argument, not yet a fully formalized
theorem: the step "the only new closure points come from `V_Σ`-accumulation" wants
tightening. Treat as a near-certain obstruction / the pattern to beat, not a proof.)

**The precise residue (what a genuine witness would require).** A closure point `x`
of `⋃A_k` such that *no* `𝔗`-open set (no usual-clopen, no `V_Σ`) containing `x` is
`⊆ closure` — a true boundary point. Since `𝔗` is generated by usual-clopens + the
`V_Σ`, and the `V_Σ` are "too plentiful" (every constraint-consistent direction is
open), producing such a point is exactly the difficulty. **This shifts the prior
toward "`Yₙ` basically disconnected / `Clop(Yₙ)` σ-complete / route closed,"**
consistent with the dossier's low prior for a clean ZFC example — though a *proof*
of route-closed is the hard universal (every countable clopen union has open
closure), where the strong-zero-dim sub-lemma re-enters. **Per the Phase-4 line:
this records the obstruction and the residue; it does NOT adjudicate the verdict.**

## The reduction (GJ now in hand) — and the one named sub-lemma

GJ pages obtained 2026-06-12 (scans in
`notes/literature_review/literature/gillman_jerison_pages/`). The relevant facts:

- **GJ 1H (definition):** `X` is *basically disconnected* ⟺ every **cozero-set**
  of `X` has **open closure**.
- **GJ 6M.1:** *`βX` is basically disconnected ⟺ `X` is basically disconnected.*
  (Clean iff, no side condition.)
- **GJ 6W** (the witness template): in `βN−N`, *the closure of the union of a
  **strictly increasing sequence of clopen sets** is never open* — hence not
  basically disconnected. This is the shape any non-σ-completeness witness must
  take.

**The clean reduction — route AROUND `βYₙ`, stay in the Boolean algebra (this
avoids a real gap).** The Strategy-D object is `B = Clop(Yₙ)`. Unconditionally
(Stone / Loomis–Sikorski):
> `B` is σ-complete ⟺ `St(B) = β₀Yₙ` (the Banaschewski compactification = Stone
> space of `B`) is basically disconnected.
This needs **no** Stone–Čech machinery and **no** zero-dimensionality hypothesis —
`St(B)` is a Stone space by construction, and its cozero sets are exactly countable
unions of basic clopens, i.e. countable subsets of `B`. So:
> `B` σ-complete ⟺ every countable subset of `B` has a sup in `B` ⟺ (GJ 1H form)
> every countable union of clopens of `St(B)` has open closure.

**⚠ Named sub-lemma — do NOT use the GJ 6M `βYₙ` form without it.** It is tempting
to apply GJ 6M.1 to push the question to "`Yₙ` basically disconnected ⟺ cozero-in-`Yₙ`."
That requires `St(Clop Yₙ) = βYₙ`, i.e. **`Yₙ` strongly zero-dimensional**
(`dim Yₙ = 0`, equivalently `βYₙ` zero-dimensional) — which is NOT free from `Yₙ`
having a clopen base (`ind = 0 ≠ dim = 0`). Argyros (§1.2) only gives a clopen base
(`ind = 0`) and that `𝔗` is finer than the product topology (which can destroy the
Lindelöf condition that would upgrade `ind=0` to `dim=0`). So:
- **SUB-LEMMA (open, needs proof or a citation): is `(Yₙ,𝔗)` strongly
  zero-dimensional?** If YES → `β₀Yₙ = βYₙ` and the question becomes the cleaner
  "every cozero-set of `Yₙ` has `𝔗`-open closure," directly in `Yₙ`. If unknown →
  work intrinsically in `B = Clop(Yₙ)` (the route above), which needs nothing extra.

## The intrinsic witness question (unconditional — this is the live target)

The **positive (Strategy-D-YES) direction needs none of the above** — it is purely
Boolean-algebraic and checkable in `Yₙ`:

> **Find `𝔗`-clopens `G₁ ⊆ G₂ ⊆ ⋯` in `Yₙ` (strictly increasing) such that the
> family `{Gₖ}` has NO least clopen upper bound in `Clop(Yₙ)`** — equivalently,
> `cl_𝔗(⋃ₖ Gₖ)` is not `𝔗`-open (so no clopen sits between `⋃Gₖ` and its closure).

Exists → `Clop(Yₙ)` non-σ-complete → **ZFC Strategy D example**. (This is exactly
the GJ 6W shape, transported into `Yₙ`.) The prior work shows where to look: the
family must exploit the **limit-branch structure** of the tree `T` — single-branch
and coordinate/all-zeros families provably have sups (see below).

The **negative (route-closed) direction** is the genuinely hard quantification:
prove every countable clopen family has a sup. Here the strong-zero-dim sub-lemma
helps (it lets you argue over cozero sets of `Yₙ` rather than in `β₀Yₙ`).

## Realistic endpoints (honest)

Per the dossier's prior (40+ yrs expert work nearby; clean overlooked ZFC example
unlikely):
- **Witness found** (increasing clopens, no least upper bound, via a limit branch) →
  ZFC Strategy D example. The reduction is now sharp enough that this is a concrete
  hand-construction attempt in `Yₙ`, not a literature hunt.
- **Provably basically disconnected** → route closed → consistency construction
  (attack mode C, ◇/CH).
- **Stuck** → the sub-lemma (strong zero-dim of `Yₙ`) and the limit-branch witness
  are the two precise sub-questions to hand a set theorist.

The reduction itself (GJ 1H + 6M/6W + Stone/Sikorski, routed through `B`) is
rigorous and citeable; the witness construction / impossibility proof is the human
Phase-4 step (not Lean-checkable, deliberately not hand-derived here).

## Sources
- Argyros 1983, PJM 105(2), 257–261 — `notes/literature_review/literature/argyros_1983.pdf`
  (§1.0–1.3 read directly; construction above is verified against it).
- Dossier: `strategy_d_dossier.md` (Strategy D forms, the βYₙ question = step 1,
  line 572 `Clop(βYₙ)≅Clop(Yₙ)`).
- Working file: `argyros_sigma_completeness_scratch.md` (reviewed sound: V_Σ-kill
  correct, β₀Y reframe correct; FACT B "Y non-compact" under-argued but harmless).
- **Gillman–Jerison, *Rings of Continuous Functions*** — scans of the relevant
  pages in `notes/literature_review/literature/gillman_jerison_pages/`: §1H (p.22–23,
  basically/extremally disconnected + cozero-closure def), §6M (p.96, `βX` b.d. ⟺
  `X` b.d.), §6W (p.100, the strictly-increasing-clopen non-b.d. witness).
- Comfort–Negrepontis 1982 (`literature/comfort_negrepontis_1982`) and Fremlin Vol 5
  (`literature/fremlin_2003`) — for the Gleason-space distinction and measure-free
  background; the famous "extremally disconnected Argyros example" is `G(Xₙ)` (the
  Gleason cover, σ-complete, WRONG row), NOT `βYₙ`.
