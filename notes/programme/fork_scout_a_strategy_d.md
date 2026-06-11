# Fork scout — path (a): the anti-smuggler / Strategy D

*Branch `explore/a-strategy-d`, written 2026-06-11. One of two scouting notes
(sibling: path (b), branch `explore/b-pointfree-descent`). This note exists
to make the (a) path legible enough to decide whether it is worth a year, NOT to
do the math. See `programme/genealogy.md` §"THE OPEN QUESTION" for the (a)/(b)
fork this branches.*

## Which curiosity this serves

**Researcher (a) — the anti-smuggler.** What bothers (a) is positing the answer
to reason backward: Takens assumes the manifold, Kolmogorov assumes the sample
space. The 2024–2026 descent was (a) saying *"no — derive what observation alone
forces."* The discriminating sentence (genealogy line 208): *"You don't need to
assume a state space — observation forces the probability."* If that is the one
you lean into, this is your path.

**What's already delivered for (a).** CE / Paper I: a coherent family of
observations forces a unique σ-additive measure, no Ω assumed. The (a) curiosity
*already has its deep result.* So this path is NOT "find the (a) result" — it is
**push the one genuinely open frontier that is continuous with the 2024 origin**,
the most faithful unfinished business of the Boolean/distributive line.

## The live question (sharp, unsolved, ZFC-level)

**Strategy D** (`papers/paper_i/notes/ultralimit_investigation/strategy_d_dossier.md`,
current to 2026-05-21):

> Does there exist a **non-σ-complete, non-atomic, measure-free** Boolean
> algebra? Equivalently (Stone form): a compact, totally disconnected, no
> isolated points, **not** basically disconnected, carrying **no** strictly
> positive Radon probability.

Why it is the faithful (a) continuation: it is the exact boundary where "coherence
forces a measure" can FAIL — the algebra where finite coherence does not extend
σ-additively and no measure exists at all. It is the structural shadow of CE's
non-derivability, made into a concrete existence question. Pure Boolean /
distributive — no quantum, no OML, no incompatibility. That is the point: it is
(a)'s question, not (b)'s.

## State of the attack (from the dossier)

- **σ-complete regime: well-mapped, all near-misses.** Argyros (ZFC), Souslin/◇,
  Gaifman (ZFC), Farah–Veličković (□_κ) all give measure-free non-atomic BAs —
  but all σ-complete (fail condition 2).
- **Non-σ-complete regime: one construction (Todorčević / Džamonja–Plebanek), but
  it has atoms** (fails condition 1).
- **Likely status: ZFC-independent**, specific independence not yet established.
  Even σ-complete-regime measurability is axiom-sensitive (PID vs ◇), which makes
  a clean ZFC resolution unlikely.

## The ONE concrete next move (no literature search — direct math)

> **Is `Clop(βYₙ)` σ-complete?** Equivalently: is `βYₙ` (the pre-Gleason space in
> Argyros's construction) basically disconnected?

This is the dossier's unresolved sub-question and the sharpest entry point. `βYₙ`
already has property (*), ¬(**), is compact, zero-dimensional, ccc, no isolated
points. If its clopen algebra is **NOT** σ-complete, then `βYₙ` is a **Strategy D
example in ZFC** — the whole question resolves positively, in ZFC, today.

- None of the read sources (Argyros 1983/1982, Comfort–Negrepontis Ch. 6, Fremlin
  §531–539, Džamonja–Plebanek 2008, Plebanek 2024) address whether `βYₙ` is
  basically disconnected.
- The Gleason-space step is standard for *ensuring* extremal disconnectedness, but
  whether it is *necessary* for the measure-theoretic properties is open.
- **Prior is low** (40+ years of expert work nearby ⇒ an overlooked ZFC example is
  unlikely) — but the question is precise and settled by direct analysis of `Yₙ`'s
  cozero structure, not by reading more.

## Subsequent moves (dossier §"Next concrete steps")

2. Verify the two foundational equivalences with exact refs (σ-completeness ↔
   basically disconnected; measure-free BA ↔ Radon-measure-free Stone space).
3. If `βYₙ` IS basically disconnected (move 1 fails): attack mode C — consistency
   construction under ◇/CH.
4. Inspect Kunen / Fedorchuk examples against the three Strategy D conditions.
5. Beyond that, progress likely needs a set theorist (collaboration).

## What would KILL this path

- Move 1 resolves **βYₙ IS basically disconnected** AND modes C/D both stall ⇒
  the question retreats fully into "needs a set-theorist collaborator," i.e. not a
  solo-tractable lead. (Not a math death — a tractability death.)
- Someone has already settled it: the lit-map (dossier §Status, finalized
  2026-05-21) says no, but a fresh search on `Plebanek measure-free Boolean
  algebra non-σ-complete` is the cheap re-check before investing.

## Honest read on this path

This is the **sharper of the two fork paths**: one precise, unsolved, solo-checkable
ZFC question (`Clop(βYₙ)` σ-complete?) with a clear win condition (a ZFC Strategy D
example) and a clear fallback (independence via mode C). It is also the path with
*lower upside-novelty* per (a)'s own ledger — CE/Paper I already delivered the
(a) result, so Strategy D is "finish the open boundary," not "open a new frontier."
The genealogy's caveat stands: choosing (a) means accepting that the deep (a) thing
is done and this is faithful continuation, not fresh territory.

→ Sibling path (b) and the asymmetry between them: `fork_scout_b_descent_impossibility.md`
(on branch `explore/b-pointfree-descent`).
