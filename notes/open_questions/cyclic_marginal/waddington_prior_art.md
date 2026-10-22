# Waddington landscape: prior-art pass (2026-10-22)

reviewed: false. One scout pass (about 14 web searches, US-only, "standard" mode; four full-text
reads, listed below). Everything not marked "read" is snippet, abstract or standard knowledge.

## 1. The essentials

- E1: a possibility space of states (cell fates).
- E2: only local data: pairwise slopes or transition rates between states, or pairwise couplings between time snapshots.
- E3: a sought global object explaining all local data: a potential (height function) or a joint law over trajectories ("one world").
- E4: obstruction = a loop: slopes not summing to zero round a cycle (curl, flux, broken detailed balance), or pairwise couplings that do not glue.

## 2. Shelf hits found BEFORE searching (obeying the shelf-first rule)

- `SHELF_INDEX.json`, no entry for Waddington, single-cell, snapshots, quasi-potential, Schnakenberg or Kolmogorov criterion. No `*_taxonomy.json` mentions them. Only stray hit: `notes/knowledge_map/knowledge_map_body.tex` l.513 cites Schnakenberg 1976 for entropy production (a different thread).
- Already on the shelf and relevant:
  - `jiang_lim_yao_ye_2011_hodgerank.pdf` (C1; index says abstract-level).
  - `kellerer_1964_mass_theoretic_marginal_problems.pdf`, `fritz_chaves_2013_entropic_inequalities_marginal_problems.pdf` (marginal problem, triangle and cycle hypergraphs).
  - `araujo_quintino_budroni_terracunha_cabello_2013_ncycle.pdf`, `sullivant_2006_compressed_polytopes_disclosure.pdf`, `ohsugi_hibi_2010_non_very_ample_contingency.pdf` (C4 machinery).
  - `abramsky_mansfield_barbosa_2011_cohomology_contextuality.pdf`, `abramsky_et_al_2015_contextuality_cohomology_paradox.pdf`, `caru_2017_cohomology_contextuality.pdf` (C5 language).
  - `ecology_contextuality_sweep_2026-10-20.md`: ecology has no joint-existence test; same gap statement applies here.
- Saved this pass (open access, each with a SHELF_INDEX entry): `lavenant_zhang_kim_schiebinger_2021_trajectory_inference.pdf` (arXiv 2102.09204v2), `weinreb_2018_fundamental_limits_snapshots.pdf` (bioRxiv 170118v3, the preprint, not the PNAS version), `zhou_aliyu_aurell_huang_2012_quasipotential.pdf` (arXiv 1206.2311).

## 3. Verdict table

| Claim | Verdict | Owner and location | Read level |
|---|---|---|---|
| C1 loop sums vanish iff global potential | **OWNED** | Kolmogorov reversibility criterion (rates multiplied round any cycle equal reversed product); Schnakenberg 1976 (cycle affinities from fundamental cycles); Jiang–Lim–Yao–Ye 2011 (HodgeRank: gradient / curl / harmonic; "globally consistent" = gradient of a score function, Def 2.3; curl-free on triangles only gives gradient when the 2-complex has no harmonic part). | HodgeRank: PDF text grep, definitions 2.3 and curl-free passages only. Kolmogorov, Schnakenberg: secondary snippets only (Wikipedia, 2012 review); the 1976 paper not retrieved. |
| C2 non-gradient gene networks = potential + rotational flux | **OWNED** | Wang–Xu–Wang PNAS 105 (2008) 12271 (landscape-flux framework); Wang–Zhang–Xu–Wang PNAS 2011 (Waddington landscape quantified; "gradient and curl force"); Zhou–Aliyu–Aurell–Huang 2012 (quasi-potential, Freidlin–Wentzell equivalent, N>2 attractors); Maehara–Ohkawa 2025 ddHodge (Hodge on scRNA-seq vector fields). | Zhou et al.: abstract read in the saved PDF. Others: search snippets only. Ferrell 2012 and Rand/Sáez/Briscoe 2021–22: not read, not verified. |
| C3 snapshots on a chain cannot detect curl | **OWNED for the continuous-drift form; PARTIAL for the graph-shaped form** | Weinreb et al. (limitation 3): "Static snapshot data cannot distinguish periodic oscillations of cell state" and density is invariant under adding rotational u with div(cu)=0. Lavenant et al. §1.3.1: "if the drift v induces a periodic motion, then the distribution of cells may be constant in time". Both resolve it by assuming a gradient drift (Waddington assumption); Lavenant Thm 1.1: law identifiable from marginals under gradient drift. | READ in primary source (text of the saved PDFs, the passages quoted). Only the passages cited; Lavenant §§ beyond ~100k characters of ar5iv not read. |
| C3' "path-shaped query graph ⇒ no twist; a twist needs a loop in the query graph" | **NOT FOUND as a statement in the biology literature; mathematically it is the classical acyclic-hypergraph gluing result** (Vorob'ev 1962; Kellerer 1964; Villani gluing lemma for couplings along a chain). | Not verified in primary source here beyond the shelf entry for Kellerer. Their setting differs: in Weinreb and Lavenant the snapshots are marginals of ONE true process, so a joint exists by construction; the issue there is non-uniqueness, not non-existence. | Shelf entry only. |
| C4 probabilistic hidden twist on a cycle of snapshots / populations | **NOT FOUND** | Searches on "marginal problem" + cycle + single-cell, multi-marginal OT + cycle, lineage tracing + coupling consistency, contextuality + biology returned nothing that asks whether a joint exists. Nearest: MMOT with pairwise costs on graphs with cycles (cost structure, not existence); a hierarchical MMOT paper that glues couplings along a chain (arXiv 2512.14072 from snippet; chain, not cycle). Stochastic thermodynamics side not searched beyond Schnakenberg. | Snippets only. Coverage: US web search, no Google Scholar, no non-English. Moderate chance of a miss, since the vocabulary differs per field. |
| C5 sheaf / cohomology / contextuality for Waddington or cell fate | **NOT FOUND** | Two searches. Only "quantum-like" evolution modelling (arXiv 1705.09863) which uses contextuality loosely (not the formal marginal-problem sense). Cohomological language does appear for ranking (HodgeRank) and for logic (Abramsky et al.), not cell fate. | Snippets only. |

## 4. Where the seam is NOT (owned framings)

- Gauge twist as curl of a velocity field: owned (C1, C2). Kolmogorov and Schnakenberg own the discrete loop criterion. HodgeRank owns the cohomological decomposition on graphs, including triangle-local versus global ("harmonic") cycles.
- "Snapshot data cannot see rotation, so assume a gradient": owned by Weinreb 2018 and Lavenant 2021/24, in words, with the gradient assumption explicitly named as the Waddington assumption.
- The Waddington landscape for non-gradient networks via flux or quasi-potential: owned (Wang et al.; Zhou et al.; Freidlin–Wentzell).
- Chain of couplings always glues: classical.

## 5. Surviving candidate seam (one paragraph, not a claim)

Everything found treats the snapshot problem on the uniqueness side: a true process exists, its marginals are given, and the question is whether the dynamics can be recovered (answer: only under a gradient or potential assumption). Nothing found asks the existence side: given pairwise couplings among three (or more) populations arranged in a cycle, such as three batches, three modalities, or lineage-barcode linkages that reconnect time points, with supports consistent, does any joint law exist, and can pair-level consistency checks stay silent while the frequencies fail to glue (the repo's hidden relational twist at 3×4×4)? Honest distance: real snapshots are marginals of a single process, so a joint exists by construction; non-existence can only arise for estimated or model-derived couplings, merged datasets from different experiments, or deliberately inconsistent assumptions, so this is a data-merging lens (the shelf's `data_merging` question), not a statement about Waddington's landscape as such. The cycle also has no natural home in time-ordered snapshots (a chain); it appears only if the query graph has a loop, which needs non-temporal links. The absence result is from a thin, snippet-level sweep and should be re-run with a scout in the multi-marginal OT and batch-integration (data-merging) literatures before it is relied upon.

## 6. Not done

- Primary-source reads of Wang–Xu–Wang 2008, Schnakenberg 1976, Ferrell 2012, Rand et al., Freidlin–Wentzell, ddHodge.
- Stochastic-thermodynamics literature on non-existence of consistent local rate data.
- A sweep of batch-integration / multi-modal alignment papers (cycle-consistency losses exist in ML, e.g. cycle-GAN-style alignment, but were not examined).
