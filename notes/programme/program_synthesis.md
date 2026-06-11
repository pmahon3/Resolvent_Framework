# Programme Synthesis — The Full Architecture

*Written 2026-04-06. Updated 2026-05-03 after notes reorganization and
renumbering cleanup into the current three-paper architecture.*

> **⚠ STALE SNAPSHOT (pre-dates the 2026-05-11 CE collapse).** This document
> describes the architecture as of early May and presents leads — notably
> **fibre-mixing irreducibility** ("the highest-leverage move", §"The true
> frontier") — that have since died or parked. Fibre mixing was **killed**
> (bridge theorem false); Papers II/III were withdrawn; the OML thread that
> succeeded them has itself closed/parked (descent axis, 2026-06-10). Read this
> for the historical architecture only. For current state the authoritative doc
> is `program_overview.md`; for the kill history see `genealogy.md`. Left
> un-rewritten because it is a dated snapshot, not a live state doc.

---

## The single unifying object

Across all three papers, the programme tracks a single notion:

**observational indistinguishability**

Each paper gives it a different form:

| Paper | Indistinguishability | Object |
|-------|---------------------|--------|
| I | events that never separate across refinements | failure of CE |
| II | identical conditional regularity laws | $\kappa_Q(q,\cdot) = \kappa_Q(q',\cdot)$ |
| III | same delay vector at lag $L$ | $(x,x') \in R_L$ |

These are the same equivalence relation, made precise at increasing levels of
structure. Paper III makes this explicit: the set of unseparated pairs
$R_L = \{(x,x') : \Phi_h^{(L)}(x) = \Phi_h^{(L)}(x')\}$ and its measure
$(\mu\otimes\mu)(R_L)$ is the final invariant. Everything reduces to this.

---

## The pipeline

The programme is a single pipeline in five layers:

```
Layer 1 — Logical / algebraic
  query system, Boolean algebras, CE decides existence

Layer 2 — Measure
  probability measure emerges, σ-additivity is earned

Layer 3 — Dynamics
  predictive kernels, semigroup structure

Layer 4 — Geometry
  delay map, embedding

Layer 5 — Statistics (Paper III)
  empirical witnesses, rates, entropy
```

Each layer is derived from the previous. Nothing is globally postulated.

---

## The chain of bridges

The programme connects five mathematical structures by four bridges:

```
Boolean  ←→  Measure  ←→  Function space  ←→  Geometry  ←→  Information
```

| Bridge | Paper | Identity |
|--------|-------|----------|
| Boolean → Measure | I | Carathéodory / Stone: CE makes σ-additivity possible |
| Boolean → $L^2$ | II | Density bridge: $\sigma$-algebra generation ↔ $L^2$ density |
| $L^2$ → Geometry | II/III | Delay map: $\sigma(\Phi_h^{(L)}) = \mathcal{O}_h^{(L)}$ |
| Geometry → Information | III | Conditional variance identity: $\delta(L) = \frac{1}{2}\int_{R_L}|\mathbf{1}_S - \mathbf{1}_{S'}|^2\,d(\mu\otimes\mu)$ |

The last bridge is integrated into Paper III as the conditional variance identity
(Lemma~III:lem:cond-var) and Corollary~III:cor:entropy.

This is a closed chain. The Stone space introduced in Paper I as a technical
device for measure extension reappears in Paper III as the object being
reconstructed.

---

## The three obstructions

Each paper identifies a single obstruction to its main result:

| Paper | Obstruction | Status |
|-------|------------|--------|
| I | Lack of CE | Proved irreducible (Łoś's theorem + finite-cofinite counterexample) |
| II | Lack of density ($\mathcal{O}_h \neq \mathcal{B}$ mod $\mu$) | Characterised by density bridge; faithfulness of Φ_h |
| III | Lack of fibre mixing | Analogue of CE; irreducibility **open** |

**Fibre mixing is to Paper III what CE is to Paper I:** both are the minimal
condition under which a comparison theorem holds. CE makes σ-additivity possible;
fibre mixing makes the algebraic and information-theoretic witnesses comparable.
Both are strictly weaker than their natural sufficient condition (ergodicity implies
fibre mixing; no first-order condition implies CE).

**The open question:** is fibre mixing irreducible in the same sense as CE — i.e.,
not derivable from any structural condition on the query system or the dynamics?
This is the deepest open question in the programme. Resolving it would:
- Close the three-obstruction table symmetrically
- Give Paper III the same foundational standing as Paper I
- Supply the coherence/consistency schema (see `notes/unsorted/foundations/coherence_completion/conceptual_schema.md`)
  with a second fully worked example in a genuinely different domain

---

## What Paper III adds (precisely)

Paper III is not applied statistics appended to a pure theory. It does two
structurally new things:

**(A) Identifies the observable invariant.**
$(\mu\otimes\mu)(R_L)$ is simultaneously:
- the algebraic error (via the conditional variance identity)
- the geometric failure (mass of unseparated pairs)
- the information loss (negative Rényi-2 entropy of $\nu_L$)

**(B) Makes the whole programme computable.**
Three estimable witnesses from data alone:
1. $\hat\delta(L,n)$ — algebraic
2. $\hat{d}_L(x,x')$ — geometric (delay separation)
3. $\hat{H}_2(\nu_L^{(n)})$ — information-theoretic (collision entropy)

All three detect the same transition. (1) and (3) are asymptotically equivalent
under fibre mixing; (2) certifies state-space separation directly.

---

## The deepest statement

> A system is reconstructible exactly when indistinguishability vanishes across
> all observational layers, and this vanishing can be detected equivalently in
> algebraic, geometric, or information-theoretic terms.

---

## Passage Conditions

The mature programme claim is not that observation alone determines every
stronger structure.  The sharper claim is:

> The framework identifies what is forced by observation and exactly what extra
> admissibility or valuation is needed for stronger structures.

This gives the recurring grammar:

| Passage | Not forced by | Added/licensing condition |
|---|---|---|
| finite coherence $\to$ probability | compatibility alone | CE |
| probability + indexed observations $\to$ dynamics | measure alone | temporal coherence / composition structure |
| observation $\to$ reconstruction | finite queries alone | faithfulness / exhaustion of the observable algebra |
| reconstruction $\to$ rates | population structure alone | sampling, regularity, and concentration |
| refinement $\to$ dimension | refinement ordering alone | valuation of refinement $\Lambda$ |
| entropy witness $\leftrightarrow$ algebraic witness | separation alone | fibre mixing |
| zeta curve $\to$ canonical law | function alone | naturality / admissibility / valuation |

The shared form is:

$$
\text{local data}
\quad+\quad
\text{completion or limiting object}
\quad+\quad
\text{admissibility or valuation}
\quad\Rightarrow\quad
\text{genuine structure}.
$$

The failure modes are as important as the positive theorems.  They mark where
local coherence, finite refinement, or formal completion stops short of the
intended object.

---

## The true frontier

All three papers are mathematically complete and editorially polished.
Paper I and the companion note are arXiv-ready; Papers II and III are
editorially polished pending Paper I's arXiv ID for cross-reference updates.
Upload is blocked only by arXiv math.LO endorsement.

The genuine open mathematical directions, ordered by downstream leverage:

### Dependency structure

```
Fibre mixing irreducibility
        ↓                        ↘
Coherence/consistency schema      Paper III foundational standing
        ↓              ↓
  Zeta direction   Interaction direction

Strategy D ─────────────────────→ (self-contained; no downstream leverage)
Entropy witness concentration ──→ Interaction direction only
Observational resolution ───────→ Paper III remark / future theorem
```

The highest-leverage move is fibre mixing irreducibility. It feeds the
coherence/consistency schema with the second worked example that schema needs
to become a genuine classification. Without it, the schema is a one-example
framework. With it, it fans out to all other future directions.

The right sequencing is therefore: fibre mixing first, coherence/consistency
schema second (generalise with two examples in hand), then everything else.

### Open directions

1. **Fibre mixing irreducibility** *(highest leverage — start here).*
   Is fibre mixing derivable from any structural condition on the query system
   or dynamics? The Łoś-type argument from CE irreducibility is the natural
   template; the question is whether the finite-cofinite construction generalises
   or whether a different witness is needed. Either outcome — irreducible or
   derivable — has large downstream consequences.

2. **Coherence/consistency schema** *(second, after fibre mixing).*
   Formalise the three-component schema (local data / global realization /
   failure mode) with CE and fibre mixing as the two primary worked examples.
   The priority theorem target: prove that the contradiction failure mode is the
   unique compact coherence notion, giving a formal sense in which consistency
   is a distinguished special case. See
   `notes/unsorted/foundations/coherence_completion/conceptual_schema.md` and
   `notes/README.md`.

3. **Concentration of the entropy witness** *(most immediate technical extension).*
   A finite-$n$ concentration result for $\hat{H}_2(\nu_L^{(n)})$ comparable
   to Proposition 4.1 for $\hat\delta$. Requires only McDiarmid bounds on the
   U-statistic; no new structural theory. Downstream leverage: interaction
   direction.

4. **Observational resolution dimension** *(Paper III-adjacent future theorem).*
   Treat exponents such as \(n^{-s/(2s+D)}\) as arising from valued
   distinguishability growth.  The current stance is conservative: a Paper III
   remark is acceptable, but real integration waits for a theorem.  See
   `notes/unsorted/finite_sample/observational_resolution/index.md`.

5. **Strategy D** *(self-contained; no downstream leverage).*
   Does a non-σ-complete non-atomic Boolean algebra admitting no σ-additive
   probability exist? Likely ZFC-independent. ZFC Boolean-algebra methods
   exhausted. Next step requires forcing. Leave as a named open problem unless
   set-theoretic methods become available.

6. **Foundational topology / zeta / interaction directions** *(post-arXiv, consume results).*
   All downstream of fibre mixing and the coherence/consistency schema. Do not
   develop until Papers I–III are posted and fibre mixing is understood.
