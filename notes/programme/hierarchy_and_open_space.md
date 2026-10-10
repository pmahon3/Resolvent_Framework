# Hierarchy of the central question, and where the open space is

*Written 2026-10-09. A navigation note: read it when the thread feels lost.*

## The question

Does coherence, followed to its end, force probability, dynamics and
reconstruction rather than assuming them? And where it does, what exactly does it
force? (`program_overview.md`, The Central Question; reopened as a question
2026-10-09.)

## The hierarchy

```
F. IDENTIFICATION / REALIZATION   what system must generate the data?
          ▲
E. PROCESS                        does coherence at all lengths force a process?
          ▲            ▲
B. PASTING (flagship)   C. REGULARITY on Boolean algebras (classical)
          ▲
A. LOCAL DATA                     finite windows, coherent on overlaps

side branch, off the path to dynamics:
  pasting failure → D. SHARPNESS (two-valued) → C′. PATHWISE σ (σ-essential lane)
```

**The edges:**
- **E rests on B and C.** A process is Kolmogorov extension: B at every finite
  window, then C to pass to the limit.
- **C is free for finite alphabets** (compactness). So for finite alphabets, E is
  exactly the flagship's capstone.
- **C′ is a side branch.** σ-essential patterns are pasting failures by
  construction (empty kernel on a finite block). Two-valued means a single
  trajectory, not deterministic dynamics, and a stationary two-valued state is a
  fixed point. So C′ never feeds E.

## Status by layer (2026-10-09)

| layer | answer so far | status |
|---|---|---|
| C, Boolean regularity | forced iff the finitely additive part vanishes; free for finite alphabets | classical |
| B, pasting | forced on the tame classes; the boundary is decidable per length (winding criterion) | proved |
| E, process | forced for finite alphabets exactly where no catalogued obstruction exists, **if L-B′ holds** | one open lemma |
| F, identification from a given system (Takens root) | injectivity: Takens / SYC. Generation: Rokhlin / KS (killed for invertible T). Conditioning: the stable-embedding literature | **accounted for** |
| F, realization without a given system | — | **unscouted** |
| C′, pathwise σ | not forced: ZFC witness; countable witness on every ring L ≥ 4 (Lean) | real, off the path |

## How the thread got lost (diagnosis)

1. **The root assumed the system.** The pre-repo root question, delay embeddings
   that are injective and well-conditioned, took (X,T) and h as given.
2. **The descent questioned that assumption.** Each step asked "is this forced?",
   and that question only ever points down. It never turns back up by itself.
3. **The descent answered a sharper question:** does the data force a system at
   all? The original question was answered by the literature on its own.
4. **The real drift was the σ lane.** It followed regularity into non-Boolean,
   two-valued territory because it kept producing theorems. Without a map, depth
   looked like progress toward the root.
5. **The way back up is to re-ask the top question without its premise.** That is
   realization ("what system is forced?"), not delay embedding ("how well do
   delays recover a given system?").

## Where the open space has been: classical theorem minus one given

| crowded room | assumption it relies on | open space found by dropping it |
|---|---|---|
| Takens / Rokhlin / stable embedding | a given system | whether coherent data forces any system (the descent) |
| Carathéodory / Kolmogorov extension | Boolean, compact | σ-essential witnesses on non-Boolean carriers |
| Vorob'ev / marginal polytopes | acyclic or fixed model | winding criterion, forcing lemma (protocol families on rings) |
| realization theory (HMM / OOM / PSR) | a declared model class | what coherence forces on *any* generating system (unscouted) |

## The test for open space

1. **Name the crowded theorem nearby**, with its exact hypotheses.
2. **Drop one hypothesis.**
3. **Ask whether the dropped version still feeds a layer above it.**
   - Yes: open ground **on the path**.
   - No: open ground **off the path**. It can be real, but it is a side room
     (e.g. C′).

## The two open spaces on the path

**L-B′ (layer E).** Set-up:
- Watch two tokens move in lockstep through the language's transition graph.
  They may never occupy the same state at the same time.
- A **swap** is a run that ends with the two tokens' positions exchanged.
- Two states are **cocyclic** if they lie on one simple cycle.
- A **component** is a strongly connected component of bar-D, the graph whose
  vertices are pairs of distinct states and whose closed walks are these
  two-token runs.

**L-B′:** in a primitive language, every component that contains a swap also
contains a cocyclic pair.

**Status.**
- With the cycle lemma (proved), L-B′ makes every swap-carrying component
  aperiodic. That is exactly the forcing lemma, and with it the flagship's
  capstone becomes unconditional.
- The evidence: exhaustive to 4 states, and samples to 9.
- Primitivity is essential: there are 8 imprimitive cactus counterexamples.
- Detail: `papers/reconstruction/notes/joint2_wielandt_finding.md` (last three
  sections).

**Realization without a declared class (layer F).** This is the broadest form of
the realization question, with a trap built in.
- **Trap 1: taken literally, it is trivial.** Every process is realized by its own
  shift on path space (the canonical realization).
- So the question has to be about what every realization must have, i.e.
  invariants forced by coherence, or about a *minimal* realization under some
  complexity measure:
  - entropy;
  - Markov order;
  - Hankel / positive-realization rank;
  - minimal number of causal states.
- **Trap 2: occupied ground.** That is crowded. Computational mechanics
  (Crutchfield–Young 1989, ε-machines) is literally "the minimal causal-state
  realization with no declared class". Stochastic realization theory (Heller
  1965; Ito–Amari–Kobayashi 1992; Jaeger's OOMs; PSRs) owns the finite-rank side.
- **Where open space plausibly sits:** at the joint with the flagship. What
  realization invariants does a *protocol family* force when only window
  statistics on rings are observed, contextual data included? That is the
  question of what F forces when B fails.
- **Unscouted.** Prior art comes first.
