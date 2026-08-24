# Strategy D step 1 — math RESOLVED, but KILLED AS A CONTRIBUTION (2026-06-18)

> **⛔ AUDIT KILL (KNOWN-OR-FOLKLORE, /audit full hostile-referee, primary-source).**
> The math in this file is TRUE (the witness is correct) but it is **NOT a
> contribution** — clears no type bar. **Gaifman 1964** (PJM 14(1):61–73, Thm 2.2 +
> property (†)) already exhibits, IN ZFC and 19 years prior, an atomless Boolean
> algebra with **no strictly positive FINITELY-additive measure** — strictly
> STRONGER than the "no σ-additive" leg here. The non-σ-complete + atomless legs are
> conceded-trivial; the only hard ingredient (measure-freeness) is Argyros's already-
> published theorem. "Strategy D" was this programme's PRIVATE name, never field-open;
> the "likely ZFC-independent" prior was a LOCAL MISREADING (σ-completeness read off
> the completion/Gleason cover — Comfort–Negrepontis 6.23/6.25 record the *completed*
> forms — not the trivially-non-σ-complete base). L_MO₂-shape kill (true + trivial
> + occupied) — first kill of the Strategy-D (a)-line, NOT a descent-arc death.
> Strategy D RETIRED. Survives: a one-line Gaifman-1964
> citation, no contribution. Full verdict: `strategy_d_AUDIT_VERDICT.md`. The
> proof below is RETAINED FOR THE RECORD (correct math); its "contribution" /
> "ZFC Strategy D example" framing is SUPERSEDED by this banner.

**Clop(Y,𝔗) is NOT σ-complete** (TRUE — but NOT a contribution; see banner).
⟦HAND — verified⟧ (elementary field-of-sets argument; each step a finite
hand-check; independently re-derived twice + advisor-checked).

This SUPERSEDES the "lean toward route-closed / basically disconnected" prior in
`argyros_sigma_completeness_handoff.md` and `..._scratch.md`. The prior was wrong:
it came entirely from analyzing `V_Σ`-*built* families (handoff Props 1, 3 — all
have sups) plus the gapless all-zeros family (Prop 2, union = co-singleton
`Y∖{0̄}`, closure `Y`, open). A one-character change to the all-zeros family
(`1 → 11`, a *gap*) produces a non-open closure and kills σ-completeness.

The obstruction's load-bearing premise — *"the only new closure points come from
`V_Σ`-accumulation, hence interior"* (flagged unproven in handoff §"obstruction",
problemset Task `tighten`) — is **FALSE**. `0̄` is a counterexample: a new closure
point from *ordinary* (usual-topology) accumulation, lying in **no** `V_Σ`,
genuinely **non-interior**. So Task `tighten` is not hard, it is unprovable.

None of the heavy machinery is needed: St(B), β₀Y, GJ 6M/6W, and the
strong-zero-dimensionality sub-lemma (problemset Task `szd`) are all **MOOT**.
This is a direct field-of-sets disproof in `Y` itself.

---

## The witness

Coordinates 1-indexed; `Y = {0,1}^ω`, `𝔗` = Argyros topology (subbase = usual
product-clopens ∪ `{V_Σ : Σ a branch of T}`); `0̄ = (0,0,0,…)`.

> **A_k := [0^{k-1} 1 1]**  = `{x ∈ Y : x_1=⋯=x_{k-1}=0, x_k=x_{k+1}=1}`  (k ≥ 1).

A leading block of `k−1` zeros, then **two** ones (the gap vs. Prop 2's single 1).

### The five claims (each a finite hand-verification)

**(1) Each `A_k` is 𝔗-clopen; pairwise disjoint.**
`A_k` is usual-clopen (a cylinder), and usual-clopen ⟹ 𝔗-clopen (𝔗 ⊇ usual; the
`A_k` were already usual-*open*). Disjoint: `A_k` forces first-1-position `= k`.

**(2) [load-bearing] The 𝔗-neighbourhood base at `0̄` = the usual one.**
A basic 𝔗-nbhd is a finite intersection of **subbasic** sets containing the point.
Argyros's subbase is `{usual-clopens} ∪ {V_Σ}`. **No `V_Σ` contains `0̄`**: every
pair-restriction of `0̄` is the diagonal `(0,0) ∉ K_s`. So every basic 𝔗-nbhd of
`0̄` is a plain usual-clopen, hence `⊇ [0^N]` for some `N`.
*(Caution: the complements `Y∖V_Σ` are 𝔗-open and do contain `0̄`, but they are
NOT subbasic, so they never enter the nbhd-base at `0̄`. The 𝔗-refinement cannot
shrink a neighbourhood of `0̄`. This is exactly why the refinement can't repair the
defect — and it is the whole reason `0̄` survives as a non-interior closure point.)*

**(3) `cl_𝔗(⋃_k A_k) = (⋃_k A_k) ∪ {0̄}`.**
Since `𝔗 ⊇ usual`, `cl_𝔗 ⊆ cl_usual`. Usual closure: for a non-union point `x`
with first 1 at finite position `p`: either `x_{p+1}=1` (then `x ∈ A_p ⊆ union`) or
`x_{p+1}=0` (then `[0^{p-1}10]` is a usual nbhd of `x` meeting the union nowhere —
any `y` there has first-1 at `p` followed by 0). The only leading-all-zeros point is
`0̄`, and `0̄ ∈ cl` because `A_{N+1} ⊆ [0^N]` and (by (2)) every 𝔗-nbhd of `0̄`
contains some `[0^N]`, which meets `A_{N+1} ≠ ∅`. So `cl_usual = union ∪ {0̄}`; `0̄`
survives into `cl_𝔗` by (2); nothing else can. ∎

**(4) The closure is NOT 𝔗-open** (`0̄` is not interior).
The point `0^N 1 0̄` lies in `[0^N]` but not in `union ∪ {0̄}` (first-1 at `N+1`
followed by 0 ⟹ in no `A_k`, and ≠ `0̄`). Every 𝔗-nbhd of `0̄` contains some `[0^N]`
(by (2)), hence contains such a point outside the closure. So no 𝔗-nbhd of `0̄` is
`⊆` closure. ∎

**(5) `{A_k}` has NO supremum in `Clop(Y,𝔗)`.**
Let `D_N := [0^N] ∪ (A_1 ∪ ⋯ ∪ A_N)`. Each `D_N` is usual-clopen (finite union of
cylinders), hence 𝔗-clopen, and is an upper bound: for `k ≤ N`, `A_k ⊆ D_N`; for
`k > N`, `A_k = [0^{k-1}11] ⊆ [0^N]` (as `k−1 ≥ N`). The `D_N` **strictly decrease**:
`0^N 1 0̄ ∈ D_N ∖ D_{N+1}`. And `⋂_N D_N = union ∪ {0̄}` = the closure (not open).

Now: **every** clopen upper bound `D` (however exotic — built from `V_Σ` and
complements) contains `cl_𝔗(union) ∋ 0̄` (clopen ⟹ 𝔗-closed ⊇ the set ⟹ ⊇ its
closure). Being 𝔗-open and containing `0̄`, `D` contains a basic nbhd of `0̄`, i.e.
some `[0^N]` (by (2)); together with `union` this gives `D ⊇ D_N`. So every clopen
upper bound contains some `D_N`. A least upper bound `L` would satisfy `L ⊆ D_N` for
all `N` ⟹ `L ⊆ ⋂_N D_N = closure`, while `L ⊇ union` and `L` clopen ⟹ `L ⊇ {0̄}` ⟹
`L = closure` — but the closure is not open (4). Contradiction. **No sup.** ∎

⟹ `Clop(Y,𝔗)` is not σ-complete.

---

## The three Strategy D conditions, all in ZFC

The Strategy D target (problemset §1): a Boolean algebra that is simultaneously
non-σ-complete, atomless, and measure-free. For `B = Clop(Y,𝔗)`:

- **non-σ-complete** — the witness above. ✓
- **atomless** — `(Y,𝔗)` has no isolated points (Argyros §1.2 / Def 1.2: clopen
  base; every nonzero clopen splits), so `Clop(Y)` has no atoms. ✓
- **measure-free** — Argyros Claim 1.5: `Y` fails property (**); for the compact
  `βY = X_n`, (**) ⟺ strictly positive measure (Kelley, Argyros 0.5–0.6); and
  `Clop(Y) ≅ Clop(βY) = Clop(X_n)` (dossier line 589; clopens extend uniquely to βY
  because each clopen and its complement are completely separated — a BA iso). A
  strictly positive σ-additive probability on `Clop(Y)` would give one on
  `Clop(X_n)`, i.e. a strictly positive Radon measure on the compact `X_n`,
  contradicting Argyros. ✓ *(Note: don't even need the iso for the headline — but it
  is the clean route to measure-freeness, since Argyros states it for `βY`.)*

**⟹ `Clop(Y,𝔗)` is a ZFC Strategy D example.** (Equivalently, via the iso, so is
`Clop(βY) = Clop(X_n)`.) No `◇`/CH fallback needed.

---

## Reconciling with "Strategy D is likely ZFC-independent" — NO contradiction

The problemset and dossier call Strategy D "likely independent of ZFC" with "nearest
known constructions each missing one condition." A clean ZFC example *looks* like it
contradicts that. It does not — three points, all checked against the dossier:

1. **The "σ-complete / extremally disconnected / wrong row" verdict in the dossier
   (lines 287, 296) attaches to the GLEASON COVER `G(X_n)` — the published "Argyros
   example" (Comfort–Negrepontis Thm 6.25) — NOT to the pre-Gleason `βY`.** Argyros
   passes to `G(X_n)` *precisely because* `βY` is not already extremally/basically
   disconnected. So the witness here (βY not basically disconnected) is fully
   consistent with — indeed predicted by — why the Gleason step exists.

2. **The dossier explicitly logged this as the open hinge, not a known fact** (lines
   306–317): "Whether `βY_n` is basically disconnected requires direct analysis …
   **If `βY_n` is NOT basically disconnected, it would satisfy all three Strategy D
   conditions**"; σ-completeness "not explicitly stated in either Argyros paper." The
   present note *answers* that open sub-question (NOT basically disconnected). No
   published result asserts the opposite.

3. **The "ZFC-independent" claim was a CONJECTURE transferred from the σ-complete
   regime, not a theorem about the non-σ-complete target.** It rests on the Maharam-
   algebra results (Fremlin §539, Todorčević PID — dossier lines 244–274), which
   govern *Dedekind-σ-complete* ccc algebras, and on *prior* constructions (Kunen
   carries a s.p. measure; Fedorchuk σ-completeness unresolved). The pre-Gleason
   space was the dossier's explicit ZFC candidate (item 7, lines 583–587) conjectured
   to break exactly that pattern. **It does.** So: retract the "likely independent of
   ZFC" framing *for this target* — the difficulty was overestimated. The only hard
   condition was always measure-freeness (Argyros's genuine theorem, property (**)
   failure, ZFC); non-σ-complete + atomless were never hard, and their conjunction
   with measure-free was never shown to need independence.

**Why σ-completeness was never going to survive.** Non-σ-completeness is essentially
**inherited from the usual Cantor space**: `Clop({0,1}^ω, usual)` is countable, hence
trivially not σ-complete, and this exact gap family `A_k` witnesses it there too. The
`V_Σ`-refinement only **adds** clopens; it cannot add a sup at `0̄` because `0̄` lies
outside every `V_Σ`. The earlier route-closed lean analyzed only `V_Σ`-built families
(handoff Props 1, 3) and missed the trivial usual-topology witness at `0̄`; the GJ /
β₀Y reduction was a correct but over-built detour around a one-line check.

## What was over-built (for the record)

The GJ 1H/6M/6W reduction, the `St(B)=β₀Y` / Stone–Loomis–Sikorski routing, and the
strong-zero-dim sub-lemma were all correct *machinery* but **unnecessary** for the
answer. They reduce "σ-complete?" to "basically disconnected?" — a true equivalence
— but the direct field-of-sets check is shorter and decisive. The sub-lemma
(`dim Y = 0`?) remains an open *topological* curiosity but is moot for Strategy D.

## Sources
- Argyros 1983, PJM 105(2), 257–272 — `notes/literature_review/literature/argyros_1983.pdf`
  (§1.0–1.5 read directly; construction, separation Lemma 1.3, measure-freeness
  Claim 1.5 all verified against the source).
- Handoff (now superseded): `argyros_sigma_completeness_handoff.md`.
- Problemset kit (ARCHIVED 2026-06-19, `notes/archive/strategy_d_killed/problemset_strategy_d.{tex,pdf}`):
  Task `witness` is the slot this fills; Tasks `tighten`/`szd`/`cons` are now moot.
- Dossier: `strategy_d_dossier.md` (line 589, the Clop iso).
