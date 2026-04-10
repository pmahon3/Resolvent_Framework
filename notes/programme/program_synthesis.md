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

The last bridge is proved in the companion note (`papers/notes/bridge_note.tex`)
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
| IV | Lack of fibre mixing | The Paper IV analogue of CE |

**Fibre mixing is to Paper IV what CE is to Paper I:** both are the minimal
condition under which a comparison theorem holds. CE makes σ-additivity possible;
fibre mixing makes the algebraic and information-theoretic witnesses comparable.
Both are strictly weaker than their natural sufficient condition (ergodicity implies
fibre mixing; no first-order condition implies CE).

The open question: what is the minimal necessary condition for fibre mixing? Is
it irreducible in the same sense as CE?

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

The programme is complete at the level of four papers. The genuine open
directions, in order of structural depth:

1. **Fibre mixing as a structural condition.** Characterise and possibly prove
   irreducibility of fibre mixing, analogous to the CE irreducibility result in
   Paper I. This is the most direct continuation.

2. **Concentration of the entropy witness.** A finite-$n$ concentration result
   for $\hat{H}_2(\nu_L^{(n)})$ comparable to Proposition 4.1 for $\hat\delta$.
   Requires only McDiarmid bounds on the U-statistic; no new structural theory.
   This is the most immediate technical extension.

3. **Paper 0 direction.** Separation system + coherent charges as a primitive
   foundation: derive the whole programme from observational distinguishability
   alone, without assuming a sample space. CE and fibre mixing would both be
   instances of charge-coherence conditions in this language.
