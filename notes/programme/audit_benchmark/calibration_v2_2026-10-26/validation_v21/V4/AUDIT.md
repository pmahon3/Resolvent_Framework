## Audit: seed.md (local chromatic number of topologically t-chromatic graphs; circular = ordinary chromatic number for even t) (mode: full)

**Audit date (per AS_OF.md): 2004-07-05.** Only sources dated on or before 2004-07-05 count as prior art. Every hit that is the seed's own work (arXiv math/0407075 and its versions, later talks and surveys of it) was set aside and not used. Every hit dated after 2004-07-05 was ignored as prior art. The web was searched on 2026-10-26.

**Read levels.** Most PDFs fetched in this session were scanned or compressed and **could not be read** (Erdős et al. 1986, Lih–Liu 2002, Matoušek–Ziegler 2002/04). Read levels are therefore abstract, bibliographic or secondary (citing-paper) unless stated otherwise. This matters for the referee-estimate cap below.

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof of known result)

The seed does not state its per-type bars explicitly, as the framework requires. That gap is minor, because the claims are concrete theorems.

### Pure Verdict: NOVEL (main result). The circular sub-result is partly owned and partly concurrent; see below.

**Stripped statement.**
- (A) Let G be a graph whose topological lower bound (coindex/connectivity of a box or neighbourhood complex, Lovász-type) gives χ(G) ≥ t. Then every proper colouring of G has a vertex whose closed neighbourhood sees at least ⌈t/2⌉+1 colours, i.e. ψ(G) ≥ ⌈t/2⌉+1. The bound is tight or nearly tight for some Schrijver, generalized Mycielski and Borsuk graphs.
- (B) If such a G has χ(G) = t with t even, then χ_c(G) = χ(G). Some odd-χ Schrijver graphs have χ_c < χ.
- Mechanism: Ky Fan's alternating-sign strengthening of Tucker/Borsuk–Ulam forces a multicoloured complete bipartite subgraph K_{⌈t/2⌉,⌊t/2⌋} in every proper colouring.

**Owners searched for (all names, weaker and stronger forms):** "local chromatic number" together with Kneser, Schrijver, Mycielski, Borsuk and topological bounds; "colorings with locally few colors"; the circular chromatic number of Kneser and Schrijver graphs; the Johnson–Holroyd–Stahl conjecture; Ky Fan's lemma in colouring proofs.

| Source (date) | What it owns | Read level |
|---|---|---|
| Erdős, Füredi, Hajnal, Komjáth, Rödl, Seress, "Coloring graphs with locally few colors", *Discrete Math.* 59 (1986) 21–34 | Defines ψ(G). Main theorem bounds χ in terms of local r-colourability (about r·2^r·log log m). No topological lower bound on ψ was found in any description of it. | Zentralblatt review + secondary citations; the scan was unreadable (fetched 2026-10-26) |
| Körner, Pilotto, Simonyi, "Local chromatic number and Sperner capacity", *JCTB* 95 (2005) 101–117 | χ_f ≤ ψ ≤ χ, the "lies between" sentence of the seed. **Date uncertain:** published 2005. The seed treats the inequality as background, so it was presumably known by 2004-07-05, but I could not confirm a preprint date before 2004-07-05. | Secondary (abstracts, later slides) |
| Ky Fan, "A generalization of Tucker's combinatorial lemma with topological applications", *Ann. Math.* 56 (1952) 431–437 | The alternating-sign (k₀,−k₁,k₂,…) simplex lemma, the seed's tool. The tool is owned; its application to ψ is not. | Secondary (Wikipedia, Prescott–Su 2005 description, Musin survey) |
| Matoušek–Ziegler, "Topological lower bounds for the chromatic number: a hierarchy", arXiv math/0208072 (9 Aug 2002; v3 24 Nov 2003) | The hierarchy of topological bounds t, i.e. the seed's "t". Nothing found on ψ or χ_c. | arXiv abstract only (PDF unreadable) |
| Johnson, Holroyd, Stahl, *J. Graph Theory* (1997) | Conjecture χ_c(KG(n,k)) = χ for all n ≥ 2k. Proved for k = 2, n = 2k+1 and n = 2k+2. | Secondary |
| Hajiabolhassan, Zhu, *JCTB* (2003) | χ_c(KG(n,k)) = χ(KG(n,k)) for n ≥ 2k²(k−1); also for Schrijver graphs with large n | Secondary (citing papers, talk abstract) |
| Lih, Liu, "Circular chromatic numbers of some reduced Kneser graphs", *JGT* 41 (2002) 62–68 (preprint 17 Aug 2001) | χ_c(SG(m,2)) = m−2 = χ for m ≥ 4, m ≠ 5. SG(5,2) = C₅ has χ_c = 5/2 < 3. | Abstract/catalogue; the PDF was unreadable |
| Meunier, "A topological lower bound for the circular chromatic number of Schrijver graphs", *JGT* 49(4) (2005) 257–261, doi 10.1002/jgt.20079 | χ_c(SG(n,k)) = χ for n even, which is exactly the Schrijver case of (B) for even t. **Could not determine whether it predates 2004-07-05:** no received or online date found, and the Wiley page returned 403. Secondary sources describe it as independent and concurrent. | Catalogue entry only (its abstract appears mislabelled) |

**Verdict on (A):** NOVEL. Searches found no pre-2004-07-05 lower bound on ψ for Kneser, Schrijver, Mycielski or Borsuk graphs, nor for any topologically defined class. Every hit on ψ for these families is the seed's own work or later. The ingredients are owned: ψ is from 1986, t from Lovász / Matoušek–Ziegler, and the alternating lemma is Ky Fan 1952. Their combination into "multicoloured K_{⌈t/2⌉,⌊t/2⌋}, hence ψ ≥ ⌈t/2⌉+1" is not a three-line consequence: it needs the alternating-sign version, not plain Borsuk–Ulam or Tucker.

**Verdict on (B):** novel as a general statement, owned in special cases.
- It strengthens Hajiabolhassan–Zhu (large n), Johnson–Holroyd–Stahl (small cases) and Lih–Liu (k = 2) to every topologically t-chromatic graph with t even. That includes all Kneser graphs with n even, which proves the even-χ half of the Johnson–Holroyd–Stahl conjecture.
- The Schrijver/even-n case coincides with Meunier (JGT 2005), and its priority date is unresolved.
- The odd-case claim is consistent with known data: SG(5,2) = C₅ has χ_c = 5/2. Lih–Liu show equality for SG(m,2) with odd m ≥ 7, so the "odd behaves differently" claim must concern larger k. The seed should state its scope precisely.

**Correctness sanity checks (by hand):**
- For t = 3, the bound gives ψ ≥ 3, which is right: ψ = 2 forces bipartite (Erdős 1984 note), and C₅ has ψ = 3.
- For t = 2 it gives ψ ≥ 2, which is trivial and correct.
- (B) is consistent with a multicoloured K_{t/2,t/2} obstruction, because a circular (t−ε)-colouring cannot contain one.

No correctness problem was found. The proofs themselves were not checked: only the abstract-level seed is available.

### Applied Verdict: not evaluated (Type 7 not claimed; pure mathematics)

The practitioner test does not apply.

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): PASS.**
- (A) was not found in the pre-2004-07-05 literature under any name. It is not folklore, and its proof is non-routine: it needs Ky Fan's alternating strengthening.
- (B) as a class-wide statement is also new. Its Schrijver/even case may be co-owned by Meunier (concurrent; date unverified).
- The bar is met for (A) unconditionally. For (B) it is met with a priority caveat.

**Type 2 (new proof of known result): PASS, narrow.** This applies only to the parts of (B) already known: Kneser graphs with n ≥ 2k²(k−1) (Hajiabolhassan–Zhu 2003), the Johnson–Holroyd–Stahl small cases, and SG(m,2) with even χ (Lih–Liu 2002).
- The new route replaces case-specific combinatorics with one topological argument.
- Bar (a), a technique applicable elsewhere, is met: the same multicoloured-bipartite-subgraph lemma also yields (A) across five graph families.
- Type 2 is subordinate. The seed's value is Type 1, and this paper should not be framed as a re-proof.

**Types 3–6: not claimed, not evaluated.** Type 4 does not apply: ψ and χ_c are existing notions, and nothing is renamed.

### Cross-reference

The components are owned: the tool (Ky Fan 1952), the parameters (ψ from 1986; χ_c) and t (Lovász / Matoušek–Ziegler). The assembly produces a genuinely new theorem (A) and a uniform generalisation (B) of scattered circular-chromatic results. Type 1 carries the seed and Type 2 is a by-product. The open priority item is Meunier (JGT 2005) for the Schrijver/even case of (B). The seed's text as given does not credit Meunier, Hajiabolhassan–Zhu, Lih–Liu or Johnson–Holroyd–Stahl, and a write-up must.

**How it bears on the WHY (one line):** local colour constraints (each vertex sees few colours) cannot be satisfied globally once the topology is highly connected. This is a lens on "local views, one world", stated only as an analogy.

### Recommendation

**Proceed to Phase 3, scoped to Type 1**, with the local-chromatic bound (A) as the headline and (B) as a second theorem. Before claiming (B):
- settle priority against Meunier (JGT 49 (2005), doi 10.1002/jgt.20079) and credit him as independent if his result is concurrent;
- cite Hajiabolhassan–Zhu 2003, Lih–Liu 2002 and Johnson–Holroyd–Stahl 1997, and say explicitly which odd-χ Schrijver graphs (k ≥ 3) have χ_c < χ;
- confirm the pre-2004-07-05 status of Körner–Pilotto–Simonyi for χ_f ≤ ψ.

Needs a deeper read of: Erdős et al. 1986 full text, for any earlier lower bound on ψ for specific families. The scan was unreadable.

### Referee estimate: BORDERLINE
Venue class: research journal
Value carried by: factor 1 (new theorem ψ ≥ ⌈t/2⌉+1 for topologically t-chromatic graphs; uniform χ_c = χ for even t, settling the even half of Johnson–Holroyd–Stahl)
Main risk a referee would raise: the circular result overlaps Meunier's concurrent Schrijver-graph theorem (and Hajiabolhassan–Zhu for large n), so priority and credit must be stated. The estimate is held at BORDERLINE by cap v2.1 (ACCEPT-LIKELY on factor 1 needs the nearest prior work read beyond abstract). That prior work is Erdős et al. 1986, Meunier 2005 and Hajiabolhassan–Zhu 2003, and none could be read past abstract or secondary level in this session. On substance, the result looks like a strong research-journal paper.
