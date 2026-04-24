# Programme Synthesis — The Full Architecture

*Written 2026-04-06, after completion of Papers I–IV and bridge note integration.*

---

## The single unifying object

Across all four papers, the programme tracks a single notion:

**observational indistinguishability**

Each paper gives it a different form:

| Paper | Indistinguishability | Object |
|-------|---------------------|--------|
| I | events that never separate across refinements | failure of CE |
| II | identical predictive laws | $\Pi_t(x,\cdot) = \Pi_t(x',\cdot)$ |
| III | same delay orbit | $\Phi_h(x) = \Phi_h(x')$ |
| IV | same delay vector at lag $L$ | $(x,x') \in R_L$ |

These are the same equivalence relation, made precise at increasing levels of
structure. Paper IV makes this explicit: the set of unseparated pairs
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

Layer 5 — Statistics (Paper IV)
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
| Boolean → $L^2$ | III | Density bridge: $\sigma$-algebra generation ↔ $L^2$ density |
| $L^2$ → Geometry | III/IV | Delay map: $\sigma(\Phi_h^{(L)}) = \mathcal{O}_h^{(L)}$ |
| Geometry → Information | IV | Conditional variance identity: $\delta(L) = \frac{1}{2}\int_{R_L}|\mathbf{1}_S - \mathbf{1}_{S'}|^2\,d(\mu\otimes\mu)$ |

The last bridge is proved in the companion note (`papers/paper_iv/notes/bridge_note.tex`)
and integrated into Paper IV as Lemma 3.1 + Corollary 5.12.

This is a closed chain. The Stone space introduced in Paper I as a technical
device for measure extension reappears in Paper III as the object being
reconstructed.

---

## The three obstructions

Each paper identifies a single obstruction to its main result:

| Paper | Obstruction | Status |
|-------|------------|--------|
| I | Lack of CE | Proved irreducible (Łoś's theorem + finite-cofinite counterexample) |
| III | Lack of density ($\mathcal{O}_h \neq \mathcal{B}$) | Characterised by the density bridge |
| IV | Lack of fibre mixing | Analogue of CE; irreducibility **open** |

**Fibre mixing is to Paper IV what CE is to Paper I:** both are the minimal
condition under which a comparison theorem holds. CE makes σ-additivity possible;
fibre mixing makes the algebraic and information-theoretic witnesses comparable.
Both are strictly weaker than their natural sufficient condition (ergodicity implies
fibre mixing; no first-order condition implies CE).

**The open question:** is fibre mixing irreducible in the same sense as CE — i.e.,
not derivable from any structural condition on the query system or the dynamics?
This is the deepest open question in the programme. Resolving it would:
- Close the three-obstruction table symmetrically
- Give Paper IV the same foundational standing as Paper I
- Supply the coherence/consistency schema (see `notes/future/coherence_consistency_direction.md`)
  with a second fully worked example in a genuinely different domain

---

## What Paper IV adds (precisely)

Paper IV is not applied statistics appended to a pure theory. It does two
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

## The true frontier

The mathematics of all four papers is worked out. Papers II–IV are at
first-draft quality only — substantial editorial revision (prose, voice,
structure, introductions) is needed before any of them are ready for
submission. Paper I and the companion note are submission-ready; upload
is blocked only by arXiv math.LO endorsement.

The genuine open mathematical directions, ordered by downstream leverage:

### Dependency structure

```
Fibre mixing irreducibility
        ↓                        ↘
Coherence/consistency schema      Paper IV foundational standing
        ↓              ↓
  Zeta direction   Interaction direction

Strategy D ─────────────────────→ (self-contained; no downstream leverage)
Entropy witness concentration ──→ Interaction direction only
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
   is a distinguished special case. See `notes/future/coherence_consistency_direction.md`.

3. **Concentration of the entropy witness** *(most immediate technical extension).*
   A finite-$n$ concentration result for $\hat{H}_2(\nu_L^{(n)})$ comparable
   to Proposition 4.1 for $\hat\delta$. Requires only McDiarmid bounds on the
   U-statistic; no new structural theory. Downstream leverage: interaction
   direction.

4. **Strategy D** *(self-contained; no downstream leverage).*
   Does a non-σ-complete non-atomic Boolean algebra admitting no σ-additive
   probability exist? Likely ZFC-independent. ZFC Boolean-algebra methods
   exhausted. Next step requires forcing. Leave as a named open problem unless
   set-theoretic methods become available.

5. **Paper 0 / zeta / interaction directions** *(post-arXiv, consume results).*
   All downstream of fibre mixing and the coherence/consistency schema. Do not
   develop until Papers I–IV are posted and fibre mixing is understood.
