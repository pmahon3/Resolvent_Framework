# Reading list — reconstruction / commensurability

The object: an observation protocol (windows on a symbolic dynamical system) is
*commensurable* when pairwise-coherent window-statistics (EA) force realisability by
a declared class (PR(𝓡)); geometrically iff the coherence polytope C equals the
realisability polytope R. The paper is a **bridge across four fields**; the open
capstone (universal impossibility) reduces to one lemma L-B living in the
Perron–Frobenius + signed-graph corner. Paper skeleton:
`papers/reconstruction/reconstruction_skeleton.tex`; proved body archived at
`papers/reconstruction/notes/reconstruction_body_PROVED_ARCHIVE.tex`; the L-B
detail + oracles in `notes/unsorted/joint2_wielandt_finding.md`,
`notes/unsorted/parity_only_*.py`.

**Diagnostic first (do this before reading anything).** Skim two intros in one
sitting: Abramsky–Brandenburger §§1–4 (field 1) and Wainwright–Jordan §3–4 (field
2). Whichever frame feels *alien* is your primary gap. Most readers missing "a whole
field" here are missing polyhedral combinatorics (field 2) or Perron–Frobenius
(field 4) — the contextuality and dynamics sides are more widely discussed. The two
fields you own already, skip; go straight to the one that felt foreign.

Sources in dependency order, each with the question to read it for.

## Field 1 — Contextuality / the sheaf picture (the FRAMING)

Supplies "coherent windows that come from no global process." Your C=R *is* their
marginal polytope; EA = compatible marginals / no-signalling; PR(𝓡) = a global
section in class 𝓡; contextual = obstruction to a global section.

**Abramsky–Brandenburger 2011, *The Sheaf-Theoretic Structure of Non-Locality and
Contextuality*** (NJP 13; arXiv:1102.0264). THE anchor. Read §§1–4.
- State "contextual = no global section of the presheaf of local sections." Match it
  term-for-term to the paper's `C∖R ≠ ∅`. Which of their objects is the paper's
  *context*, which is its *protocol*? (skeleton §2, def:core)
- Where does *no-signalling / compatible marginals* enter? Confirm it is exactly EA
  (pairwise agreement on shared events). (skeleton def:core)

**Fine 1982, *Hidden variables, joint probability, and the Bell inequalities***
(PRL 48). The classical fact under everything.
- State "compatible marginals ⟺ a global joint exists" for the cyclic case. This is
  the C=R proposition specialised; read it as the sanity floor. (skeleton prop:cr)

**Abramsky 2013, *Relational databases and Bell's theorem*** (LNCS). The bridge that
ties field 1 to fields 2–3; unusually readable.
- Why is "acyclic reporting ⟹ commensurable" LITERALLY the database
  running-intersection / Vorob'ev theorem? Identify the junction-tree glue. This is
  the paper's trichotomy (acyclic arm). (skeleton thm:trichotomy; archive thm:acyclic)

## Field 2 — Polyhedral combinatorics / marginal polytopes (the MACHINERY)

Makes "coherence forces a process" COMPUTABLE. If STAB/FSTAB, total unimodularity,
fractional vertex, marginal polytope feel foreign, THIS is your gap.

**Wainwright–Jordan 2008, *Graphical Models, Exponential Families, and Variational
Inference*, §3–4.** The single best entry point. Their *marginal polytope* = the
paper's C.
- Define the marginal polytope as the convex hull of realisable margins. Map it to
  R = conv{cell-incidence vectors of global configs}. Which inequalities cut out C?
  (skeleton prop:cr)

**Schrijver, *Combinatorial Optimization* (2003)** (or *Theory of Linear and Integer
Programming*). TU, König, integral polytopes. Read the TU + stable-set chapters.
- State the sufficient condition: a {0,±1} matrix with each column signable so every
  row's two nonzeros are opposite-sign is TU. This IS taming (3), signability. Where
  does the frame's bipartition supply the signing? (archive thm:taming7)
- Integral-polytope ⟺ TU-with-integral-RHS: confirm this is the whole content of
  "C=R via integrality." (archive thm:taming7 proof)

**Nemhauser–Trotter 1974 + Chvátal 1975, the STABLE-SET polytope.** STAB vs its
fractional relaxation FSTAB, and when they coincide.
- State: FSTAB(G)=STAB(G) ⟺ G bipartite (König). This is EXACTLY the parity theorem's
  even-case engine. Why does the odd cycle give a unique half-integral vertex u≡½?
  (archive thm:parity, cor:prbox — the PR-box is that vertex)

**(context, not required) De Loera–Onn 2004 + Průša–Werner 2015, universality.** Why
every rational polytope is a coherence polytope ⟹ no finite model-level taxonomy ⟹
the classification must be posed at the PROTOCOL level. (skeleton thm:trichotomy,
variety arm; archive thm:universal)

## Field 3 — Symbolic dynamics (the OBJECTS observed)

The language ρ, the shift of finite type, the transfer digraph, recurrence around a
ring. If "golden-mean shift" / "SFT" is unfamiliar, this is the other likely gap.

**Lind–Marcus 1995, *An Introduction to Symbolic Dynamics and Coding*.** THE textbook;
you need only three chapters.
- Ch. 2 (shifts of finite type): define ρ = legal adjacent pairs; the golden-mean
  shift = "no 11." The paper's *language* is an edge-SFT. (skeleton §2)
- Ch. 4 (the transfer/adjacency matrix): the digraph on states with arc a→b iff
  (a,b)∈ρ. The paper's *transfer digraph*; the *layered ring* is this SFT observed
  cyclically over Z_L. (skeleton §4)
- The Perron–Frobenius chapter: primitivity/irreducibility of the transfer matrix —
  hands you straight into field 4.

## Field 4 — Perron–Frobenius + signed graphs (the ENGINE of the open lemma L-B)

Where the FORCING LEMMA actually lives. "Primitive," "period/imprimitivity,"
"Wielandt index," "cyclic classes" are all Perron–Frobenius; "balanced signed
graph" is Zaslavsky. L-B's two exclusions are PF statements about the DERIVED
pair-graph. **This + the last source are the narrow path to L-B — not the whole stack.**

**Brualdi–Ryser 1991, *Combinatorial Matrix Theory*, Ch. 3.** Primitivity, the
Wielandt bound, imprimitivity/period, cyclic structure. The exact toolkit L-B needs.
- State: a primitive n×n 0-1 matrix has M^k>0 for all k≥(n−1)²+1 (Wielandt). This is
  the length-availability half of "primitive ⟹ cofinitely unsafe." (finding: "Finding
  2" in joint2_wielandt_finding.md)
- State the period/imprimitivity dictionary: strongly-connected digraph has period d
  ⟺ vertices d-partition into cyclic classes arcs advance through ⟺ fibered over Z_d.
  This is taming (8)=grading. Primitive = period 1 = NO grading. (finding: "Finding 1")
- **The two L-B exclusions, in PF language:** (i) primitive ⟹ the *pair-graph* bar-D
  is APERIODIC (has an odd-length closed walk); (ii) primitive+s.c. ⟹ bar-D carries a
  CROSSED cycle (its σ-cover is connected). Read Ch. 3 asking: what forces
  aperiodicity/connectivity of a DERIVED graph from primitivity of the base? That is
  the open content. (joint2_wielandt_finding.md, "THE CLEAN REDUCTION")

**Horn–Johnson, *Matrix Analysis*, Ch. 8** (alternative register). Cleaner analytic
Perron–Frobenius if you prefer it to the combinatorial treatment.
- Same targets as Brualdi–Ryser Ch. 3; pick one, not both.

**Zaslavsky 1982, *Signed graphs* (Discrete Appl. Math. 4)** + his *matrices in the
theory of signed graphs* survey. Balance theory.
- State: a signed graph is BALANCED ⟺ 2-colourable ⟺ no negative (odd-sign) cycle
  ⟺ the sign is a coboundary. The paper's "monodromy+1 balanced" IS this. Confirm
  L-A: safe-on-evens ⟺ the pair-graph signed by (monodromy+1) is balanced. (L-A proof
  in joint2_wielandt_finding.md — the cycle-space Z₂×Z₂ argument is Zaslavsky's balance
  read through two invariants at once.)

## Notes

- **Start (if you know contextuality + dynamics already):** Wainwright–Jordan §3–4
  (marginal polytope = C) → Nemhauser–Trotter/Chvátal (STAB/FSTAB, König = the parity
  engine) → Brualdi–Ryser Ch. 3 + Zaslavsky (L-B's home). That trio is the paper's
  spine and the open lemma; the rest is framing you can pick up from Abramsky–
  Brandenburger §§1–4 on demand.
- **Start (if the whole thing is foreign):** Abramsky 2013 (relational databases /
  Bell) first — it ties contextuality to combinatorics in the most readable single
  paper here — then diagnose which of fields 2/4 you're missing and go there.
- **The narrow path to the one open lemma:** Brualdi–Ryser Ch. 3 (primitivity/
  Wielandt/imprimitivity) + Zaslavsky (signed-graph balance). L-B is written entirely
  in those two vocabularies; you do NOT need the other three fields to attack it.
- Asymmetry vs the σ-essential thread: there the DST + set-theory were the gaps and
  the OML cluster was owned. Here the likely gaps are polyhedral combinatorics and/or
  Perron–Frobenius; contextuality/dynamics are more often already-held.
