# Strategy D step 1 — reduced state of "is Clop(βYₙ) σ-complete?"

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

## Evidence the easy attacks fail (these are verified, elementary)

Two natural candidate non-σ-completeness families both turn out to **have** sups,
so neither witnesses non-σ-completeness:

1. **Single-branch complement** (scratch note). For one branch `Σ`,
   `V_Σ = ⋂_n U^n` (decreasing usual-clopens), so `Aₙ = Y∖U^n` increases to
   `Y∖V_Σ`, which is **clopen** (since `V_Σ` is) — so the set-union is in the
   algebra and is the sup. ✗
2. **Coordinate / all-zeros family.** `Cₙ = [0ⁿ1]` (usual-clopen). The point
   `0̄=(0,0,…)` lies in **no** `V_Σ` (every pair-restriction of `0̄` is the diagonal
   `(0,0)`, not the anti-diagonal `K_s`), so `𝔗` agrees with the usual topology
   locally at `0̄`. Then `⋃ₙ Cₙ = Y∖{0̄}`, whose `𝔗`-closure is all of `Y` (`0̄` is a
   limit), so every clopen upper bound is `Y` and `sup Cₙ = Y` **exists**. ✗

**Consequence (the real signal):** a non-σ-completeness witness cannot be a soft
coordinate or single-branch family — those all have sups. It must exploit the
**branch structure around a limit branch** (the scratch note's instinct, §"Candidate
FAILURE family"): a countable family whose clopen upper bounds are downward-directed
with **no minimum**, the overshoot being a `V_{Σ*}`-amount for a limit branch `Σ*`.
This is exactly where the difficulty lives, and is honest evidence the route is hard,
not quick.

## The lever to use (NOT the §1.3 lemma)

The right tool is a **βX-vs-base-space basic-disconnectedness theorem**, not
Argyros's FIP machinery:

- **Gillman–Jerison, *Rings of Continuous Functions*** has the standard results on
  when a Stone–Čech / zero-dimensional compactification is basically (or extremally)
  disconnected in terms of a cozero property of the base space `(Y,𝔗)`. **GJ is not
  in the repo** — the next step needs its **exact theorem statement** (the
  "`βX` basically disconnected iff `X` is basically disconnected and `X` is ...
  / iff every cozero set of `X` has open closure" family). Get it from the source;
  do not reconstruct from memory.
- That theorem likely reduces the compactification question to a **cozero property
  of `(Y,𝔗)` directly** — far more tractable than computing in `β₀Y`. The concrete
  target then: is there a cozero set `G ⊆ Y` (countable union of `𝔗`-clopens, e.g.
  a limit-branch family) whose `𝔗`-closure is **not** open? That single set, if it
  exists, is the Strategy D witness.

## Realistic endpoints (set expectations honestly)

Per the dossier's own prior (40+ years of expert work in this neighbourhood; a
clean overlooked ZFC example is unlikely):

- **βYₙ IS basically disconnected** → route closed → fall back to the consistency
  construction (attack mode C, ◇/CH).
- **Genuinely open** → needs a set theorist; the deliverable is then the sharp
  reduced cozero question above, ready to pose.

The honest framing of this whole step: *sharp reduced question + the lever + evidence
the easy attacks fail* — **not** "close to a ZFC example."

## Sources
- Argyros 1983, PJM 105(2), 257–261 — `notes/literature_review/literature/argyros_1983.pdf`
  (§1.0–1.3 read directly; construction above is verified against it).
- Dossier: `strategy_d_dossier.md` (Strategy D forms, the βYₙ question = step 1,
  line 572 `Clop(βYₙ)≅Clop(Yₙ)`).
- Working file: `argyros_sigma_completeness_scratch.md` (reviewed sound: V_Σ-kill
  correct, β₀Y reframe correct; FACT B "Y non-compact" under-argued but harmless).
- Needed, not in repo: **Gillman–Jerison**, basic-disconnectedness-of-`βX` theorem.
- Comfort–Negrepontis 1982 (`literature/comfort_negrepontis_1982`) and Fremlin Vol 5
  (`literature/fremlin_2003`) — for the Gleason-space distinction and measure-free
  background; the famous "extremally disconnected Argyros example" is `G(Xₙ)` (the
  Gleason cover, σ-complete, WRONG row), NOT `βYₙ`.
