> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by `forcing_programme_status.md` (forcing target dissolved upstream into the reduction). Kept for the reasoning trail; not current.

# Forcing scout — Part 1: the pinned sentence

*Session 12 (2026-06-22), forcing-scout step 1. Goal: state the precise set-theoretic
existence sentence whose independence Door 3 would prove, so the literature survey
(step 2) is targeted — "is THIS sentence already decided?" — not an open-ended trawl.
⟦HAND — unverified⟧: user verifies; advisor pass pending (advisor was overloaded this
turn). Anchored to `sigma_duality_targets.md` §8–9a and the construction-log S3
state-level reformulation. NOT a claim, a TARGET to attack.*

---

## The object schema (what `L` ranges over)

A structure `L` is an **admissible carrier** iff:

- **(C1) concrete** — `L` is a sub-orthoposet of `P(Ω)` for some set `Ω`:
  `^⊥` = set-complement, order = `⊆`, orthogonal joins = disjoint unions. (Gudder
  concrete logic; NOT the MB ⊥⊥-closure functor.)
- **(C2) σ-complete** — closed under countable orthogonal joins (taken in `P(Ω)`,
  coordinatewise — the Navara/`rem:concrete` reading).
- **(C3) non-Boolean** — `L ⊊ P(Ω)`; equivalently the disjoint-∪-closure is proper, some
  binding pair `a,b` has `a∨b ⊋ h(a)∪h(b)` (non-distributive overshoot).
- **(C4) off-center / irreducible** — `L` has no non-trivial central decomposition routing
  contextuality to a central `P(κ)`. *(Derived-necessary, not extra: §-construction-log
  THE POLE — σ-essentiality forces off-center, else ∏ₙMO₂ death.)*

*(C4 is entailed by the target, kept explicit so the schema is self-contained. Whether to
quantify over it or derive it inside the sentence is a verification question — flagged.)*

## The "binding global σ-point" (the object whose existence is in question)

Fix an admissible `L`. A **σ-additive 2-valued state** is a map
`s : L → {0,1}` that is a σ-homomorphism (`s(⊥)=0`, `s(a^⊥)=1−s(a)`, and for countable
orthogonal `{aₙ}`, `s(∨aₙ) = sup s(aₙ)` — i.e. `=1 ⟺ some s(aₙ)=1`). Write `S_df^σ(L)`
for the set of these.

**The local hull `S_df(B)` — flag (c) RESOLVED 2026-06-22 to the INTRINSIC-INHERITED
reading** (user's call; most in line with programme philosophy — see the "why" note
below). The local witness ranges over **finite sub-orthoposets `B ⊆ L`** (sub-structures
of the actual concrete object, inheriting `L`'s order and orthogonality — NOT the free
orthoposet on a generating set, NOT restrictions of `L`'s global states). For such a
finite `B`, σ-additivity is vacuous, so `S_df(B)` = **all** 2-valued states of `B`
(equivalently df-states, computed inside `B`). This is what "**witnessed by no finite
sub-OML**" means literally, and it matches the S3 state-level reformulation ("a finite
consistent partial atom-selection" = intrinsic-to-`B` data).

The **binding global σ-point over `(L,B,s₀)`** is a σ-additive 2-valued state
`s ∈ S_df^σ(L)` with `s|_B = s₀`, for a prescribed local df-state `s₀ ∈ S_df(B)`.

> **Why intrinsic-inherited (the philosophy selecting, not just the math).** The other two
> readings each violate a *named, load-bearing* programme commitment:
> - **Ambient** (`S_df(B) = {s|_B : s∈S_df(L)}`) defines the "local" hull by restricting
>   GLOBAL states ⟹ the local object secretly carries global info ⟹ the gap is the §6
>   two-hull content relabeled. **Fails the anti-smuggle / red-flag rule.**
> - **Free `⟨B⟩`** counts states of the ABSTRACT orthoposet on a generating set, ignoring
>   `L`'s actual relations ⟹ can manufacture a spurious gap from freedom the concrete
>   object doesn't have. **Fails "concreteness is the gift."**
> - **Intrinsic-inherited** makes the witness a finite sub-structure of the real concrete
>   object, judged on its own honest terms ⟹ "`B` is non-contextual, the whole is not" =
>   the CE/compactness-failure target, stated without smuggling. **Honors all three.**
>
> ⚠ **OPEN TECHNICAL GATE (philosophy can't wave this away):** ranging over finite
> *sub-orthoposets* `B ⊆ L` directly (NOT closures of a generating set) sidesteps the
> finiteness worry — a finite `B` is finite by fiat, σ vacuous on it, clean. If instead
> one wants `B = ⟨F⟩_L` (closure of finite `F` under `L`'s ops), **finiteness is NOT
> guaranteed** (closing under joins/meets can escape finite) — then σ is not vacuous on
> `B` and the "local = finite, no σ" story needs repair. **RESOLUTION: quantify over
> finite sub-orthoposets `B`, not over generated closures `⟨F⟩_L`.** This keeps the
> witness honestly finite. (Verify this is the intended quantifier when the advisor passes.)

## THE PINNED SENTENCE (existence form — the thing to prove independent)

> **`Φ(L)`** : *for every finite sub-orthoposet `B ⊆ L` and every local df-state
> `s₀ ∈ S_df(B)`, there exists a binding global σ-point `s ∈ S_df^σ(L)` with `s|_B = s₀`.*

`Φ(L)` is **σ-additive lifting** for `L`. Its **negation** is the witness:

> **`¬Φ(L)`** : *some finite sub-orthoposet `B` and local df-state `s₀` admit NO global
> σ-additive extension* — the **restriction-gap** `{s|_B : s ∈ S_df^σ(L)} ⊊ S_df(B)`.

**The target object exists ⟺ `∃` admissible `L` with `¬Φ(L)`.** Call this `Ψ`:

> **`Ψ`** : *there exists an admissible carrier `L` (C1–C4) with `¬Φ(L)`* — i.e. a
> concrete σ-complete non-Boolean off-center OML carrying a finite local df-state that no
> global σ-additive 2-valued state restricts onto.

`Ψ` is the **σ-essential contextual witness** existence sentence. **Door 3 = proving `Ψ`
independent of ZFC** (a model where `Ψ`, a model where `¬Ψ`). Exit A = `ZFC ⊢ Ψ`; Exit B
= `ZFC ⊢ ¬Ψ`.

## The three already-decided checks the survey must run against `Ψ` / `Φ`

1. **Boolean ⟹ `Φ` (settled TRUE).** Booleanness forces a determining set of Dirac states
   ⟹ every local df-state lifts. So any witness for `¬Φ` is non-Boolean (built into C3).
   *Check the survey doesn't surface a theorem that secretly Booleanizes the schema.*
2. **Polish-representable ⟹ `Φ` (settled TRUE, `rem:dw` / Derr–Williamson
   arXiv:2302.03522).** If `L`'s point set `Ω` is Polish with `σ(L)=Borel(Ω)` +
   inner-regular blocks, lifting holds. So any witness is **non-Polish-representable**.
   `Ψ` lives strictly in the non-Polish slice. *This is the upper bound; the survey must
   not re-prove it and mistake it for deciding `Ψ`.*
3. **Countably-generated cut — OPEN (scout §9).** Whether (countably generated ∧ C1–C3)
   ⟹ `Φ` is stated nowhere. If a forcing argument needs uncountable generation, that is
   consistent with the record (witness, if any, uncountably generated). *The survey should
   check whether point-distinguishing-OMP work (Burešová–Pták arXiv:2401.13798) has since
   settled the σ version.*

## What the survey (Part 2) is now aimed at

With `Ψ` pinned, the forcing/large-cardinal question is precise:

> **Q.** What forcing or large-cardinal hypothesis bears on the existence of a separating
> family of **σ-additive 2-valued states** over a non-distributive concrete σ-orthoposet —
> specifically, on `Φ(L)` for non-Polish-representable, possibly uncountably-generated
> admissible `L`?

Named leads (from the record, to confirm/extend, NOT re-derive):
- **RVM (real-valued measurable) cardinals** — the natural place σ-additive-state existence
  becomes axiom-sensitive. Blecher–Weaver arXiv:1607.08505: *no RVM cardinal ⟹ σ-states
  restrict normally to atomic abelian subalgebras* — directly about σ-state restriction,
  the `Φ` mechanism. **First thing to chase.**
- **Boolean-valued models / forcing over the carrier** — does a forcing notion add/kill the
  binding σ-point? (The door1≈door3 "same object" conjecture.)
- **`add(𝒩)`** — FENCED (a fixed-measure invariant; discards choice-of-μ). Do NOT route
  independence through it. Listed only to keep the fence visible.

## Part 2 RESULT (2026-06-23, general-purpose scout, ~69k tok) — WALL, foothold named

> **⚠⚠ CORRECTION 2026-06-23 (Phase-2 audit, B–W proof read VERBATIM — this Part-2 block
> read abstracts/gloss, NOT the §4–5 proof, and got the central mechanism BACKWARDS).
> Read this banner before trusting anything below it.**
> - **"The bite always routes through the abelian diagonal" is FALSE for the
>   pure/2-valued case** (the σ-essential object). Masa-factoring holds only for B–W's
>   *real-valued* dichotomy (Thm 3.1/3.3). The **pure** dichotomy (Thm 2.4(ii),(iv))
>   does NOT factor: B–W §4 say it needs Anderson's conjecture, which "is known to be
>   FALSE" (CH), and they use **Marcus–Spielman–Srivastava paving** precisely because
>   the pure state does not reduce to a masa. **Akemann–Weaver (PNAS 105(14) 2008,
>   p.5313): a pure state on B(H) multiplicative on NO masa** = a direct counterexample
>   to "no instance bites without a Boolean sub-object."
> - **"Q is stated nowhere" → PARTIALLY REFUTED.** B–W *state and solve* the existence
>   question on B(ℓ²(κ))'s projection OML (⟺ Ulam-measurable). The abstract OML-off-B(H)
>   case is what's untouched, not the question wholesale.
> - **"Distributive routing port" meta-principle: RETRACTED + FENCED.** No such principle;
>   the pure/2-valued non-commutative case is genuinely OPEN, not a port to be built.
> - **What SURVIVES:** the wall is still load-bearing FOR THE PARK, but for the
>   σ-LS / RDP residue reason (OMLs lack RDP; no σ-LS for non-distributive OMLs), NOT
>   the Boolean-factoring reason. `rem:dw` UNAFFECTED. Park verdict (S13) STANDS.
> - Full retraction: `sigma_essential_prior_art_verdict.md` 2026-06-23 CORRECTION;
>   `CHARTED_sigma_essential.md` ⚠⚠ + FENCE; parked seed
>   `notes/covered_leads/boolean_factoring_sigma_essential_PARKED.md`.

*⟦The original Part-2 text is kept below for the trail. Its "abelian diagonal / port"
mechanism is SUPERSEDED by the banner; do not cite it as current.⟧*

**Verdict: the wall is LOAD-BEARING.** ~~All existing set-theoretic σ-state machinery lives
on the DISTRIBUTIVE/abelian side; the non-distributive OML case is genuinely untouched in
the literature. Q is stated nowhere.~~ *(banner: mechanism backwards; Q only partially
untouched)* This is the same distributive-engine / port-is-the-open-work shape as every
other frontier here. *(banner: "port" retracted)*

- **Blecher–Weaver arXiv:1607.08505 (VERIFIED verbatim — but see banner: the verbatim
  read was of the abstract, not §4–5)** — σ-additive-state existence IS
  large-cardinal-sensitive: *singular countably-additive pure states on B(ℓ²(κ)) exist
  ⟺ κ Ulam measurable* (and <κ-additive ⟺ κ measurable). ~~BUT the bite always routes
  through the **abelian diagonal subalgebra** ℓ∞(κ).~~ *(banner: FALSE for pure case —
  Akemann–Weaver counterexample.)*
- **WHY it doesn't port (the wall, = the known π–λ/RDP gap):** on a Boolean algebra a
  2-valued σ-additive state IS a {0,1}-measure on P(κ) ⟹ Ulam applies directly. On a
  non-distributive OML, df-states are NOT induced by powerset measures (joins ≠ unions)
  ⟹ Ulam machinery has no direct analogue. *(This RDP/π–λ point survives — it's the real
  residue reason; only the "B–W confirms it" framing was wrong.)*
- **The relevant cardinal is ULAM-MEASURABLE, not RVM** (RVM governs [0,1]-valued
  atomless measures; 2-valued σ-additive = Ulam). Sharpens the target.
- ~~**FOOTHOLD (named, not yet a lever):** route a witness OML's df-state space through an
  abelian/Boolean structure where Ulam bites.~~ *(banner: RETRACTED — this "routing port"
  was the Boolean-factoring thesis, which failed audit. Not a foothold.)*
- **No forcing-over-quantum-logic exists.** Takeuti/Ozawa OML-valued set theory
  (arXiv:0908.0367) is orthogonal (set theory built OVER an OML ≠ controlling the OML's
  state space). Zero results forcing to change a non-distributive OML's state space.

### Two corrections the scout surfaced (RECORD-LEVEL, verify)
- **Blecher–Weaver "abelian-restriction" phrasing** (memory "no RVM ⟹ σ-states restrict
  normally to atomic abelian subalgebras") is **INFERRED, not verbatim** — the verified
  theorem is the Ulam-measurable-iff. Soften wherever the record states it as fact.
- **⚠ Derr–Williamson arXiv:2302.03522** — scout's abstract fetch reads *"...Coherent
  Probabilities on Pre-Dynkin-Systems / Coherent Previsions on Linear Subspaces"*, NOT
  obviously the Polish/inner-regular σ-extendability paper the memory describes (Thm
  4.5/D.6). Possible: theorems are in the body, OR the arXiv number is slightly off. This
  is a `rem:dw`-LOAD-BEARING citation — **USER must verify the number/content** before it
  anchors anything further. (Does not change the WALL verdict either way.)

## Flags for verification (⟦HAND — unverified⟧)

- **(a)** Is `Φ` correctly the *lifting/existence* sentence, not the *uniqueness/§6* one?
  (§9 PROOF-DIRECTION DISCIPLINE: attack existence, not "determined-by-generators." I
  believe `Φ` is clean existence — `s|_F=s₀` with `s` existing, no determinacy claim.)
- **(b)** Should C4 (off-center) be a *quantifier restriction* on `L` or a *derived lemma*
  (σ-essential ⟹ off-center)? Stating it as a restriction is safe but may over-narrow.
- **(c)** RESOLVED 2026-06-22 (user's call) → **INTRINSIC-INHERITED**: `S_df(B)` = all
  2-valued states of a finite *sub-orthoposet* `B ⊆ L` (inherits `L`'s order/orthogonality,
  finite by fiat ⟹ σ vacuous). Selected by programme philosophy — ambient reading fails
  anti-smuggle, free-`⟨B⟩` fails concreteness-is-the-gift (full reasoning + the
  finiteness gate in "The local hull" note above). Quantify over finite sub-orthoposets
  `B`, NOT generated closures `⟨F⟩_L` (those may be infinite). Sentence updated to `B`.
  *(One residual: confirm "finite sub-orthoposet" is the intended unit vs. "finite
  sub-OML" — advisor pass.)*
- **(d)** CITATION — RESOLVED 2026-06-22 (primary source, arXiv abstract): arXiv:2401.13798
  is **Burešová–Pták** (Dominika Burešová & Pavel Pták), "...Point-Distinguishing." The
  construction-log S11 entry was RIGHT (and its parenthetical "NOT Anguelov" was right);
  `sigma_duality_targets.md` §9 + this draft's earlier "Anguelov" were WRONG — now fixed.
  CHARTED/MEMORY were already correct. No further action.
