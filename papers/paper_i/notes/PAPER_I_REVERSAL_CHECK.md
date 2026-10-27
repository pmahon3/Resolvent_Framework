# Paper I reversal check: independent verification of `PAPER_I_REAUDIT_v21.md` C1–C3 (2026-10-27)

reviewed: false. Checker: Claude (Opus), fresh-context agent, told to be hostile to both audits.
Everything marked ⟦HAND⟧ is checked by hand, not in Lean. Only this file was written. Nothing was committed.

**Verdict: CONFIRMED, with one correction to the re-audit's story and one important precedent it missed.**
- The counterexample refutes `I:thm:stone-main` exactly as stated, under every reading of Σ.
- The 2026-06-23 diagnosis ("σ-LS realization gap") puts the defect in the wrong step and prescribes a fix
  that does not work. It sits *near* the true defect: unrealized ultrafilters carry the mass, but they are
  not countably complete.
- **Precedent missed by both audits.** The repo's own Lean already recorded on 2026-08-22 that the
  corresponding Lean statement was FALSE and repaired it (§5). So the re-audit's "new finding" C2 is
  new to the audit notes, not to the repo. The paper text was never synced with that repair: this is
  paper-vs-Lean drift.

---

## 1. The exact statements (quoted from `probability_from_observation_body.tex`)

**Thm `I:thm:stone-main`** (body lines 614–624):
> Under Surjective Evaluation, Discriminability, common coarsenings, CE, and the realization hypothesis of
> Proposition B2, a compatible family of normalised charges extends to a unique
> $P \in \mathcal{P}(\Omega, \sigma(\mathcal{C}))$ with $P(\mathrm{Cyl}(i,A)) = \mu_i(\mathrm{Cyl}(i,A))$.

Note what is **absent**: "sequential common refinements", i.e. every countable set of indices has an upper
bound. That hypothesis appears only in the Carathéodory theorem `I:thm:obs-extension`.

**Hypotheses, as defined:**
- *Observational structure* (143–154): poset ι; measurable spaces $(O_i,\mathcal O_i)$; measurable
  surjections $\pi_{ij}: O_j\to O_i$ for $i\le j$; $\pi_{ik}=\pi_{ij}\circ\pi_{jk}$.
- *Instantiation* (177–187): **any** set Ω with $\mathrm{eval}_i:\Omega\to O_i$ such that
  $\pi_{ij}\circ\mathrm{eval}_j=\mathrm{eval}_i$. The projective limit is only "a canonical" choice.
  I read the whole body (717 lines) and the wrapper, and grepped for
  `henceforth|throughout|standing|we assume|varprojlim|canonical instantiation`. **Nothing in the paper
  restricts Ω to the projective limit.** The only hits are lines 172 and 189–190 ("a canonical
  instantiation") and the Stone isomorphism at line 498.
- *Common coarsenings* (196–198): every pair has a **lower** bound.
- *Cylinders* (200–208): $\mathrm{Cyl}(i,A)=\mathrm{eval}_i^{-1}(A)$, $\mathcal C$ = all cylinders,
  $B_i$ = the level-$i$ cylinders.
- *Compatible family* (241–247): $\mu_j(\varphi_{ij}E)=\mu_i(E)$.
- *Surjective Evaluation* (261–264): each $\mathrm{eval}_i$ is onto.
- *CE* (405–414): for every $i$ and every $E_n\downarrow\varnothing$ in $\mathcal E_i$, some $j\ge i$
  has $\ell_j(\pi_{ij}^{-1}E_n)\to0$. Prop `I:thm:sp1` says this is the same as each $\ell_i$ being
  σ-additive.
- *Discriminability* (525–530): $\mathcal C$ separates the points of Ω.
- *Σ and the realization hypothesis* (Prop `I:prop:B2`, 556–567): "Σ = the countably-complete
  ultrafilters of $\mathcal C$ (those closed under countable intersection)". Ω *realizes* $\mathcal C$
  if $\mathrm{pure}(\Omega)\supseteq\Sigma$ up to a $\hat\mu$-null set, **equivalently
  $\hat\mu(\Sigma\setminus\mathrm{pure}(\Omega))=0$**. Here
  $\mathrm{pure}(\omega)=\{E\in\mathcal C:\omega\in E\}$.

## 2. Hypothesis-by-hypothesis check ⟦HAND⟧

**The example.** $S=\{0,1\}$ and $\iota=(\mathbb N,\le)$. Take $O_L=\{0,1\}^L$ with its power set, and
let $\pi_{ML}$ keep the first $M$ coordinates. Ω is the set of eventually-zero 0/1 sequences, and
$\mathrm{eval}_L$ returns the first $L$ coordinates. Each $\ell_L$ is uniform on $\{0,1\}^L$.

| Hypothesis | Holds? | Why |
|---|---|---|
| Observational structure | yes | Truncations are measurable surjections and compose. |
| Instantiation (coherence) | yes | Truncating a truncation gives a truncation. Arbitrary Ω is allowed. |
| Surjective Evaluation | yes | Any word $w\in\{0,1\}^L$ is the prefix of $w000\ldots\in\Omega$. |
| Discriminability | yes | Distinct sequences differ at some coordinate $n$, and a level-$n$ cylinder separates them. |
| Common coarsenings | yes | ℕ is a chain, so $\min(i,j)$ is a lower bound. The direction typo in Lemma `pi-system` is irrelevant on a chain. |
| Compatible normalised charges | yes | The fair-coin marginals are consistent. |
| CE | yes | Each $B_L$ is finite, so a sequence $E_n\downarrow\varnothing$ in it is eventually $\varnothing$. Every $\ell_L$ is σ-additive, under either reading of $\mathcal E_i$ ($O_i$-sets or $B_i$). |
| Realization hypothesis | yes, under **every** reading of Σ (below) | |

**The Stone space.** Ω is dense in $2^{\mathbb N}$, so the map from cylinders to clopens of $2^{\mathbb N}$
is a Boolean isomorphism. Hence $\mathcal C\cong\mathrm{Clop}(2^{\mathbb N})$,
$\mathrm{St}(\mathcal C)=2^{\mathbb N}$, and $\hat\mu$ is the Bernoulli(½) measure. A point
$\omega\in\Omega$ corresponds to the ultrafilter $\mathrm{pure}(\omega)$, and a point
$x\notin\Omega$ corresponds to a non-principal ultrafilter $u_x$.

**Readings of "countably complete / closed under countable intersection"**, applied to an ultrafilter
$u$ of $\mathcal C$:
- **R1 (strict).** The set intersection of countably many members is itself a member, so it must lie
  in $\mathcal C$. The prefix cylinders of any $x$ meet in $\{x\}\cap\Omega$, which is $\{x\}$ or
  $\varnothing$. Neither is a member: $\{x\}\notin\mathcal C$ because nonempty cylinders are infinite,
  and $\varnothing\notin u$. So **Σ = ∅**. (This also falsifies the paper's line "each principal
  ultrafilter is countably complete".)
- **R2 (relative).** If $\bigcap E_n\in\mathcal C$, then $\bigcap E_n\in u$.
  - For $x\notin\Omega$: the prefix cylinders meet in $\varnothing\in\mathcal C$, and
    $\varnothing\notin u_x$, so $u_x\notin\Sigma$.
  - For $\omega\in\Omega$: any intersection of members contains ω, so if it lies in $\mathcal C$ it
    lies in $\mathrm{pure}(\omega)$.
  - So **Σ = pure(Ω)**.
- **R3 (Boolean meets in $\mathcal C$).** The prefix cylinders of any $x$ have Boolean infimum $0$ in
  $\mathrm{Clop}(2^{\mathbb N})$, so **Σ = ∅**.
- **R4 (countable intersection property in Ω).** Countable subfamilies must have nonempty intersection
  in Ω. This fails exactly for $x\notin\Omega$, so **Σ = pure(Ω)**.

In every case Σ ⊆ pure(Ω), so $\hat\mu(\Sigma\setminus\mathrm{pure}\,\Omega)=\hat\mu(\varnothing)=0$.
The realization hypothesis holds vacuously. I found no reading of the paper's words under which Σ
contains a point outside pure(Ω).

**The conclusion fails.**
- For $\omega\in\Omega$, $\{\omega\}=\bigcap_L\mathrm{Cyl}(L,\{\omega|_L\})\in\sigma(\mathcal C)$.
- Any $P$ with the stated cylinder values has $P\{\omega\}\le2^{-L}$ for every $L$, so $P\{\omega\}=0$.
- Ω is countable, so $P(\Omega)=0\ne1$. **No such P exists.** ∎
- Measurability is not an issue: pure(Ω) is a countable set of closed points of $2^{\mathbb N}$, hence
  Baire, with $\hat\mu(\mathrm{pure}\,\Omega)=0$.

**Collateral.** The same example falsifies:
- Prop B2's **first** claim, "CE ⟹ $\hat\mu(\Sigma)=1$". Here $\hat\mu(\Sigma)=0$.
- The intro's "a compatible charge family extends … iff CE (Theorem main)" (body lines 129–131).
- The converse half of `I:cor:stone-support`.
- The remark at lines 586–594: Ω countable with $\sigma(\mathcal C)=2^\Omega$ **is** standard Borel,
  the realization hypothesis does hold, and descent still fails.
- The line "the gap cannot bite on … countable … Ω" (lines 604–605).

## 3. Decision

**The counterexample refutes `I:thm:stone-main` as stated.** No hypothesis fails.
- **Where the proof breaks:** B2's step "CE gives $\mu_p=0$, so μ is σ-additive". CE is per-level
  σ-additivity, but the step needs σ-additivity of the glued charge on $\mathcal C=\bigcup B_i$. In the
  example the glued charge is not σ-additive: Ω is covered by countably many singleton-prefix cylinders
  whose total mass is small (re-audit C2, confirmed).
- **What the theorem would need:** sequential common refinements, which makes the two notions coincide
  (and on a countable index forces a top level). Alternatively, replace CE with glued σ-additivity.
- **Is the corrected criterion folklore?** Re-audit C3 says extension ⟺ glued σ-additivity
  ⟺ $\hat\mu^*_{\mathrm{Baire}}(\mathrm{pure}\,\Omega)=1$.
  - The first ⟺ is Hahn–Kolmogorov on the field $\mathcal C$. Under upward directedness
    $\mathcal C$ is a field; on a chain that is automatic. Standard: confirmed.
  - The outer-measure form and the measurable-cardinal test case are plausible, but I did not verify
    them in depth.

## 4. The 2026-06-23/25 diagnosis versus the re-audit

The prior diagnosis is **wrong in its specifics, though adjacent to the truth.** It is not a re-description
of the same defect.
- **Wrong step.** The prior audit named the missing step $\hat\mu(\Sigma\setminus\mathrm{pure}\,\Omega)=0$
  and had that added as a hypothesis. In the example that quantity is already 0, yet the theorem
  fails. The failing step is the one before it, "CE ⟹ $\hat\mu(\Sigma)=1$".
  - The prior audit's "independent second crack" did doubt this step, but blamed an uncountable index.
    The counterexample has index ℕ.
- **Wrong kind of phantom.** In the example the mass does sit on ultrafilters with no point in Ω, so
  "Ω fails to realize where the mass lives" is loosely true. But those ultrafilters $u_x$, $x\notin\Omega$,
  are **not** countably complete. The σ-complete / Loomis–Sikorski / measurable-cardinal apparatus has
  nothing to do with it. The real phenomenon is elementary: which countable intersections are empty in Ω.
  This is Andersen–Jessen territory.
- **The prescribed fix fails.** The prior verdict said "ι countable + O_i standard Borel makes B2 TRUE".
  The counterexample has ι = ℕ and finite $O_i$. The fix works only if Ω is also forced to be the
  projective limit, where Kolmogorov-type extension applies. Neither the verdict nor the paper imposes
  that.
- **On the circularity dispute (re-audit "Disagreement 2"),** I side with the re-audit. If μ is
  σ-additive on the field $\mathcal C\subseteq2^\Omega$, then computing meets in Ω *is* the definition of
  σ-additivity there. Nothing is presupposed. The 2026-06-25 objection reasoned in $\mathrm{St}(\mathcal C)$
  instead.

**One caution on the re-audit's own framing.** The re-audit presents C1/C2 as "new findings the prior
audit did not record". They are new relative to `PAPER_I_AUDIT_VERDICT.md`. They are **not** new to the
repo (§5).

## 5. Lean

- **`formalization/QuerySystem/QuerySystem/StoneDualityExtension.lean`, `stone_observational_extension`
  (line 770).**
  - Its HISTORY block (from line 729) records that, as of 2026-08-22, the earlier `UpperDirected` form
    was "FALSE as stated", refuted by Andersen–Jessen indexed by $(\mathbb N,\le)$.
  - The repaired theorem assumes `SequentiallyUpperDirected` + `EvalSurjective` + CE and is proved via
    `sp1_iff` + `observational_extension`. It does not use the Stone space or Yosida–Hewitt, and it has
    no realization hypothesis.
- **`AJNoExtension.lean`** kernel-checks, axiom-free, that the Andersen–Jessen system satisfies every
  hypothesis of the old form and has no extension.
- **`DiscriminabilityFoundations.lean:857`, `observational_extension_of_collective_exhaustion`.** This is
  the closest Lean analogue of stone-main: CE ⟹ a unique global P. It also assumes
  `SequentiallyUpperDirected` (with `EvalSurjective` and `NormalizedCompatibleContents`), and Ω is again the
  projective limit. No `sorry` or `axiom` was found by grep in that file.
- **`ExtensionObstruction.lean`, `not_exists_extension_of_escapingTower`.** A general Lean statement of the
  C2 mechanism. A decreasing sequence of cylinders, each carrying all the charge, with empty intersection,
  blocks extension "regardless of its directedness, surjectivity, or collective exhaustion". This is a
  direct Lean receipt that per-level σ-additivity does not glue.
- **No contradiction with the counterexample:**
  1. ℕ is not sequentially upper-directed. The countable set ℕ has no upper bound, so the Lean
     hypothesis fails exactly where the paper's statement omits it.
  2. Lean's `QuerySystem.Omega` is **hard-wired to the projective limit** (`QuerySystem.lean:171`).
     The eventually-zero Ω cannot even be expressed there; in Lean, Ω would be $2^{\mathbb N}$, where the
     coin measure exists. The paper allows an arbitrary instantiation, and that is the gap the countable
     example uses.
- **Nothing in Lean formalizes the paper's realization hypothesis, Σ, or Prop B2.** No Lean theorem
  matches `I:thm:stone-main` as printed.
- **Drift.** The paper's Thm stone-main still omits sequential refinements and still carries the
  realization hypothesis (the 2026-06-25 fix), two months after Lean had shown the omission fatal.
  This is another instance of the paper-vs-Lean drift pattern.

## 6. Records that would need updating (not edited here)

- `PAPER_I_AUDIT_VERDICT.md`: its "fatal B2 = σ-LS realization gap" and the "ι countable + standard Borel"
  fix.
- `notes/unsorted/foundations/ce_nonderivability/ce_taxonomy.json`: the `$meta.status` line and the
  walls entry.
- The MEMORY index line "fatal B2 (σ-LS realization gap)".
- The paper's §3 remark at lines 586–612, which claims the same wall as the OML setting. The OML
  `rem:dw` residue itself is not assessed here.

**Bearing on WHY.md.** These are local views, each correct as far as it goes: every finite window is a
fair coin. They fail to compose into one world for an elementary reason: the chosen Ω idealises away the
points where the mass sits. This is a *hidden idealisation* (question 3), not a loop and not a
large-cardinal ghost.
