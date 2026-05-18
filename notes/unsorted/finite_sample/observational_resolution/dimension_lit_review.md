# Literature Review: Observational Resolution Dimension

*Seed note - 2026-05-02*

## See also

- `notes/unsorted/finite_sample/observational_resolution/index.md` — front door
 for the working notes this review serves.

## Purpose

This note places the proposed observational resolution dimension programme in
nearby mathematical and statistical literatures. The guiding object is a valued
refinement exponent

$$
D_\Lambda
=\limsup_{k\to\infty}
\frac{H(\mathcal G_k)}{\Lambda(k)},
$$

where $\mathcal G_k$ is a finite observable refinement, $H(\mathcal G_k)$ is a
distinguishability entropy, and $\Lambda(k)$ is the valuation converting
refinement depth into scale, divergence, cost, proof depth, energy, or another
domain-native denominator.

The core message is that the rate denominator in expressions such as

$$
n^{-s/(2s+D)}
$$

should be read as an effective resolution exponent, not as topological
dimension as such. Smooth examples hide this distinction because topological,
metric, Hausdorff, box, and local Fisher dimensions often coincide.

## Executive Positioning

The idea should be positioned as a synthesis of several established patterns:

- metric entropy controls statistical rates;
- fractal dimensions measure scaling of coverings and refinements;
- information dimension measures quantized entropy growth;
- rate-distortion dimension measures information required per distortion scale;
- dynamical dimension formulas compare entropy growth to Lyapunov expansion;
- information geometry turns families of observational laws into local metrics;
- intrinsic-dimension learning uses measure growth rather than ambient
 dimension;
- algorithmic and spectral dimensions replace geometric scale by computational
 or energetic valuation.

The potentially distinctive contribution is not the bare formula
``growth divided by scale'', which is classical in many fields. The distinctive
move is to make the numerator and denominator internal to the observational
framework: finite observable algebras supply the refinements; empirical
collision, entropy, or covering diagnostics supply the numerator; and the
chosen observation horizon supplies the valuation.

For Paper III, the correct insertion is restrained. It should say that the
exponent $d$ appearing in the finite-sample rates is a resolution exponent. In
the smooth regime this exponent agrees with manifold dimension; in a Cantor or
singular regime it would instead be the relevant observable scaling dimension.
The full valued-refinement programme belongs in future notes unless a theorem is
added.

## 1. Metric Entropy and Minimax Rates

This is the closest statistical home for the rate
$n^{-s/(2s+D)}$. The denominator $2s+D$ is the usual
bias-variance or information-theoretic balance: regularity contributes $s$,
while metric entropy contributes $D$.

Classical starting point:

- Kolmogorov and Tikhomirov introduced epsilon entropy and epsilon capacity of
 function classes, making covering numbers a central quantitative measure of
 compactness and approximation complexity.
 Source: https://www.mathnet.ru/eng/rm7289

Statistical minimax form:

- Yang and Barron prove minimax convergence bounds for density estimation from
 metric entropy conditions. Their paper is the cleanest citation for the
 slogan that entropy structure determines rates.
 Source: https://experts.umn.edu/en/publications/information-theoretic-determination-of-minimax-rates-of-convergen/

- The PDF version states the point sharply: minimax risk bounds depend on
 metric entropy and are derived through information-theoretic tools such as
 Fano-type lower bounds.
 Source: https://www.stat.yale.edu/~arb4/publications_files/Information-TheoreticDeterminationOfMinimaxRatesOfConvergenceAnnalsStatistics.pdf

Modern reference scale:

- Gine and Nickl's book is a broad reference for infinite-dimensional
 statistical models, empirical processes, and nonparametric rates.
 Source: https://www.cambridge.org/core/books/mathematical-foundations-of-infinitedimensional-statistical-models/contents/0DD8B5CA428C86C2D28CE2BEFDA67B93

Use for the programme:

- Treat Paper III's rates as living in the metric-entropy tradition.
- Present $D$ as the exponent in $N(\varepsilon)\asymp\varepsilon^{-D}$, where
 the covering is not necessarily geometric in the ambient state space but may
 be induced by observable distinguishability.
- The observational novelty is the construction of the covering/refinement
 family from query algebras and finite-data witnesses.

## 2. Fractal Geometry and Nontopological Form

This is the natural home for the Mandelbrot question. Fractal geometry already
separates topological dimension from scaling dimensions. The middle-thirds
Cantor set is the canonical example: topological dimension $0$, Hausdorff and
box dimension $\log 2/\log 3$.

Core references:

- Falconer's *The Geometry of Fractal Sets* is a standard entry point for
 Hausdorff dimension, box dimension, and self-similar examples.
 Source: https://openlibrary.org/works/OL11373327W

- Mattila's *Geometry of Sets and Measures in Euclidean Spaces* is the deeper
 geometric-measure-theory reference for Hausdorff measures, density, and
 fractal geometry.
 Source: https://researchportal.helsinki.fi/en/publications/geometry-of-sets-and-measures-in-euclidean-spaces-fractals-and-re/

- Intermediate dimensions are useful when neither pure Hausdorff nor pure box
 dimension captures the intended scale restriction.
 Source: https://link.springer.com/article/10.1007/s00209-019-02452-0

Use for the programme:

- Mandelbrot's point should be treated as already vindicated in fractal
 geometry: Hausdorff dimension is not topological dimension.
- Our contribution should be framed as translating that lesson into an
 observational and finite-sample reconstruction setting.
- In Cantor systems, the denominator valuation is concrete:
 $\Lambda(L)=\log 3^{L+1}$, while the refinement entropy is
 $\log 2^{L+1}$.

Important caution:

- Do not imply that fractal dimension is new or that it derives from topology.
 The programme uses fractal dimension as one case of valued refinement.

## 3. Information Dimension and Rate-Distortion Dimension

This is the most direct information-theoretic analogue of
$D_\Lambda$. Renyi information dimension measures the entropy growth of
quantized variables as quantization scale tends to zero:

$$
d(X)
\approx
\lim_{\varepsilon\downarrow0}
\frac{H([X]_\varepsilon)}{\log(1/\varepsilon)}.
$$

That is almost exactly the proposed template with quantization partitions as
$\mathcal G_\varepsilon$ and $\Lambda(\varepsilon)=\log(1/\varepsilon)$.

Key references:

- Wu and Verdu connect Renyi information dimension to almost-lossless analog
 compression. This is a strong source for the idea that dimension can be an
 operational information limit rather than a purely geometric invariant.
 Source: https://collaborate.princeton.edu/en/publications/r%C3%A9nyi-information-dimension-fundamental-limits-of-almost-lossless/

- The same paper's DOI record is:
 https://doi.org/10.1109/TIT.2010.2050803

- Lindenstrauss and Tsukamoto's metric mean dimension / rate-distortion
 programme links dynamical covering growth to information-theoretic
 distortion rates. Later variational work develops this relation further.
 Source: https://cir.nii.ac.jp/crid/1361418520644583936
 Source: https://www.aimsciences.org/article/doi/10.3934/dcds.2021050

Use for the programme:

- This is the strongest existing framework for "dimension as entropy growth per
 observational scale."
- The observational framework should distinguish itself by allowing
 $\mathcal G_k$ to be a general query algebra or empirical reconstruction
 partition, not only Euclidean quantization.
- Paper III's collision entropy fits naturally here as a Renyi-2 analogue:

$$
H_2(\mathcal G)
=-\log\sum_{A\in\operatorname{At}(\mathcal G)}\mu(A)^2.
$$

Open technical direction:

- Define conditions under which observational collision dimension, Shannon
 information dimension, and covering dimension agree.
- Identify when collision entropy is the right empirical proxy and when it
 fails because the relevant map is continuous and atomless.

## 4. Dynamics: Entropy Over Expansion

Dynamical systems provide a mature version of the valuation-zoo idea. Entropy
counts orbit complexity. Lyapunov exponents convert time/refinement depth into
geometric scale. Dimension formulas often divide one by the other.

Key references:

- Manning proves a relation between entropy, positive Lyapunov exponent, and
 Hausdorff dimension for Axiom A surface diffeomorphisms.
 Source: https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/relation-between-lyapunov-exponents-hausdorff-dimension-and-entropy/67A549D96A0005B564EF4B6AFB54EB30

- Young relates the Hausdorff dimension of an ergodic invariant measure for a
 $C^2$ surface diffeomorphism to measure entropy and Lyapunov exponents. In
 the hyperbolic case $\lambda_1>0>\lambda_2$, the formula has the form

$$
\operatorname{HD}(\mu)
=
h_\mu(f)
\left(
\frac{1}{\lambda_1}
+
\frac{1}{|\lambda_2|}
\right),
$$

 where $\operatorname{HD}(\mu)$ is the infimum of Hausdorff dimensions of
 full-$\mu$-measure sets. The paper also discusses capacity and Renyi
 dimensions and proves equivalence in this setting.
 Source: https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dimension-entropy-and-lyapunov-exponents/5B6962A34BACD4A07EA5C7B6AE539051

- Ledrappier and Young give a deeper entropy/exponent/dimension theory for
 diffeomorphisms.
 Source: https://annals.math.princeton.edu/1985/122-3/p03

- Coates and Gelfert study interval/circle Markov maps with several equally
 sticky neutral fixed points and no physical probability measure. For these
 non-statistical systems, generic basins for measures supported on the neutral
 fixed-point simplex can have full Hausdorff dimension, even though the basins
 have zero Lebesgue measure and zero topological entropy.
 Source: https://arxiv.org/pdf/2509.00241

Use for the programme:

- This literature is the best precedent for valuation functions of the form
 $\Lambda(k)\sim ak$ or $\Lambda(t)\sim \lambda t$.
- It supports the slogan that dimension can be entropy growth divided by
 scale-generation.
- Young is the clean benchmark for how this works after measure and smooth
 dynamics are already available. The numerator is measure-theoretic entropy
 $h_\mu(f)$, i.e. typical orbit-distinction growth per unit time. The
 valuation is supplied by Lyapunov exponents: to resolve a metric ball of
 radius $r$, one needs roughly $\log(1/r)/\lambda_1$ forward iterates in the
 unstable direction and $\log(1/r)/|\lambda_2|$ backward iterates in the stable
 direction. Thus the two-sided refinement cost is

$$
\Lambda_\mu(r)
\sim
\left(
\frac{1}{\lambda_1}
+
\frac{1}{|\lambda_2|}
\right)\log(1/r),
$$

 and the local dimension is the corresponding entropy-over-valuation ratio.
- The Coates-Gelfert example is a useful caution: Hausdorff dimension,
 topological entropy, and measure-theoretic prevalence can rank the same basin
 in incompatible ways. A reconstruction or rate theorem must declare which
 size functional its witness is actually measuring.
- The observational version should ask whether the observation process itself
 supplies the expansion valuation, rather than assuming a hidden smooth
 dynamical system.

Connection to future Lyapunov notes:

- The future Lyapunov direction should try to prove an observable version of
 entropy-over-expansion:

$$
D_{\mathrm{obs}}
\sim
\frac{\text{observable refinement entropy}}
{\text{observable separation exponent}}.
$$

- The hard part is deriving the denominator from the observation/factor
 structure rather than importing it from classical smooth dynamics.

## 5. Information Geometry

Information geometry provides a disciplined way to turn a family of observable
laws into a metric or differential structure. If each hidden state or factor
point $x$ determines an observational law $P_x$, then divergences such as KL,
Hellinger, Jensen-Shannon, or Fisher distance can define observable
distinguishability.

Core references:

- Amari's *Information Geometry and Its Applications* is the standard modern
 book reference. It introduces divergence functions and the resulting
 geometric structures on statistical models.
 Source: https://link.springer.com/book/10.1007/978-4-431-55978-8

- Ay, Jost, Le, and Schwachhofer's *Information Geometry* gives a broad
 mathematical treatment of the subject.
 Source: https://link.springer.com/book/10.1007/978-3-319-56478-4

- Nielsen's survey is a useful open-access orientation to the field.
 Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7650632/

Use for the programme:

- The clean form is:

$$
d_{\mathrm{obs}}(x,y)
=
\sqrt{D_{\mathrm{sym}}(P_x,P_y)}
$$

and

$$
D_{\mathrm{obs}}
=
\limsup_{\varepsilon\downarrow0}
\frac{\log N(X,d_{\mathrm{obs}},\varepsilon)}
{\log(1/\varepsilon)}.
$$

- In smooth identifiable models, this recovers Fisher rank/local manifold
 dimension.
- In singular or fractal models, it can recover a scaling dimension of the
 observable law rather than the ambient hidden state.

Risk:

- Information geometry is not automatically the whole story. It is strongest
 when the observations form a parametrized family of laws. The broader
 observational framework also includes finite Boolean algebras, symbolic
 factors, logical fragments, and spectral refinements.

## 6. Intrinsic Dimension in Learning Theory

This literature is directly useful for Paper III because it already shows how
statistical rates can depend on intrinsic or local dimension rather than
ambient dimension.

Key reference:

- Kpotufe proves that $k$-NN regression adapts to local intrinsic dimension,
 with rates depending on how measures of balls grow near the query point.
 Source: https://papers.nips.cc/paper/4455-k-nn-regression-adapts-to-local-intrinsic-dimension

- The NeurIPS abstract explicitly states that the minimax rate depends on
 doubling-measure structure rather than on a particular ambient space.
 Source: https://neurips.cc/virtual/2011/oral/2994

Use for the programme:

- This is an excellent citation when explaining that the effective dimension in
 a rate can be local, measure-sensitive, and independent of ambient Euclidean
 dimension.
- It supports replacing "dimension of the hidden state space" by "dimension of
 the observable law or observable factor."
- It also supports using local versions of $D_\Lambda$, not just global
 limsups.

Possible theorem direction:

- Define a local observational dimension

$$
D_\Lambda(x)
=
\limsup_{\varepsilon\downarrow0}
\frac{\log \mu(B_{\mathrm{obs}}(x,\varepsilon))^{-1}}
{\log(1/\varepsilon)}
$$

and prove local reconstruction/regression rates under observable doubling or
mass-regularity hypotheses.

## 7. Algorithmic, Logical, Spectral, and Categorical Analogues

These analogues should not be imported into Paper III yet, but they are useful
for the broader programme because they show that valued refinement is not
confined to geometry.

### Algorithmic Dimension

Algorithmic dimension replaces geometric scale by description length,
complexity, or resource bounds.

- Lutz develops resource-bounded dimension using gales and shows that the
 unrestricted version recovers classical Hausdorff dimension.
 Source: https://epubs.siam.org/doi/10.1137/S0097539701417723

- Athreya, Hitchcock, Lutz, and Mayordomo develop effective strong dimension.
 Source: https://epubs.siam.org/doi/10.1137/S0097539703446912

Use for the programme:

- This supports the idea that $\Lambda$ may be computational cost or prefix
 length rather than metric scale.
- It also supports a future bridge to proof depth, description length, and
 logical fragments.

### Spectral and Fractal Zeta Directions

Spectral geometry and fractal zeta functions replace geometric scale by
eigenvalue, heat-time, or complex-dimension data.

- Kigami's *Analysis on Fractals* is a standard reference for analysis and
 Laplacians on fractals.
 Source: https://www.cambridge.org/core/books/analysis-on-fractals/contents/9EBF0F8BA597EBF4056457095760921A

- Lapidus, Levy-Vehel, and Rock define multifractal zeta functions and discuss
 how zeta functions can encode geometric/topological information about
 fractal strings.
 Source: https://link.springer.com/article/10.1007/s11005-009-0302-y

- Lapidus and Maier connect inverse spectral problems for fractal strings to
 the Riemann zeta function.
 Source: https://academic.oup.com/jlms/article/52/1/15/855722

Use for the programme:

- The zeta future note should treat spectral/zeta data as a test case for
 whether a purely mathematical object supplies its own natural valuation.
- The natural question is not "does zeta have a dimension?" in isolation. It is
 whether a specified query horizon and naturality class determine a nontrivial
 valuation $\Lambda_{\mathcal G}$ and refinement entropy.

### Lawvere and Enriched Metric Analogues

Lawvere's generalized metric spaces interpret distances categorically, with
composition enforcing triangle-like inequalities.

- Lawvere's *Metric spaces, generalized logic* is the origin point.
 Source: https://cir.nii.ac.jp/crid/1360576137827119744

- The enriched/Yoneda viewpoint is a useful modern categorical background.
 Source: https://ir.cwi.nl/pub/4820

Use for the programme:

- This is a possible formal home for valuation maps: $\Lambda(i,j)$ can be
 treated as a cost-enriched relation between refinement stages.
- It is probably too abstract for Paper III, but relevant for the long-term
 "valuation of refinement" programme.

## 8. What Should Be Built Next

The literature suggests three levels of development.

### Level A: Paper III Remark

Add only a restrained remark:

> The exponent $d$ entering the rates is the exponent governing growth of
> distinguishable observable cells at resolution $\varepsilon$. In the smooth
> regime considered here this agrees with manifold dimension. In singular or
> fractal regimes the same bias-variance calculation would involve the relevant
> observable resolution dimension instead.

This keeps Paper III honest without creating an unproved new theorem burden.

### Level B: Future Technical Theorem

Prove a theorem of the following shape.

Let $(\mathcal G_k)$ be a finite observable refinement sequence and let
$\Lambda(k)\to\infty$. Suppose:

- entropy growth:

$$
H(\mathcal G_k)
=
D\Lambda(k)+o(\Lambda(k));
$$

- approximation regularity:

$$
\operatorname{bias}(k)\lesssim e^{-s\Lambda(k)};
$$

- empirical fluctuation:

$$
\operatorname{fluctuation}(k,n)
\lesssim
\sqrt{e^{H(\mathcal G_k)}/n}.
$$

Then optimizing over $k$ gives

$$
\operatorname{error}_n
\lesssim
n^{-s/(2s+D)}
$$

up to logarithmic or model-specific factors.

The proof would be elementary but valuable because it isolates exactly what the
framework needs from geometry: entropy growth, valuation, regularity, and
concentration.

### Level C: Programme-Level Generalization

Develop a general theory of valued observational refinement:

- objects: directed observable algebras or query fragments;
- numerator: atom entropy, Shannon entropy, Renyi entropy, covering entropy,
 type count, spectral count, or complexity;
- denominator: metric scale, divergence, Lyapunov expansion, proof depth,
 computational cost, energy, or Lawvere cost;
- comparison maps: conditions under which two valuations induce equivalent
 dimensions;
- empirical proxies: collision entropy, coarse collision, occupancy counts,
 covering numbers, and divergence estimates;
- failure modes: exact collisions vanish in continuous atomless settings;
 nonuniform measures make Renyi dimensions order-dependent; topology alone
 cannot determine the exponent.

## Working Bibliography

- Kolmogorov, A. N. and Tikhomirov, V. M. "epsilon-entropy and epsilon-capacity
 of sets in function spaces." Source: https://www.mathnet.ru/eng/rm7289
- Yang, Y. and Barron, A. "Information-theoretic determination of minimax rates
 of convergence." Source:
 https://experts.umn.edu/en/publications/information-theoretic-determination-of-minimax-rates-of-convergen/
- Falconer, K. *The Geometry of Fractal Sets.* Source:
 https://openlibrary.org/works/OL11373327W
- Mattila, P. *Geometry of Sets and Measures in Euclidean Spaces.* Source:
 https://researchportal.helsinki.fi/en/publications/geometry-of-sets-and-measures-in-euclidean-spaces-fractals-and-re/
- Wu, Y. and Verdu, S. "Renyi information dimension: Fundamental limits of
 almost lossless analog compression." Source:
 https://collaborate.princeton.edu/en/publications/r%C3%A9nyi-information-dimension-fundamental-limits-of-almost-lossless/
- Lindenstrauss, E. and Tsukamoto, M. Metric mean dimension and rate distortion
 dimension. Source: https://cir.nii.ac.jp/crid/1361418520644583936
- Manning, A. "A relation between Lyapunov exponents, Hausdorff dimension and
 entropy." Source:
 https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/relation-between-lyapunov-exponents-hausdorff-dimension-and-entropy/67A549D96A0005B564EF4B6AFB54EB30
- Young, L.-S. "Dimension, entropy and Lyapunov exponents." Source:
 https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dimension-entropy-and-lyapunov-exponents/5B6962A34BACD4A07EA5C7B6AE539051
- Ledrappier, F. and Young, L.-S. "The metric entropy of diffeomorphisms. Part
 II." Source: https://annals.math.princeton.edu/1985/122-3/p03
- Coates, D. and Gelfert, K. "Hausdorff Dimension of Sets of Generic Points for
 Non-statistical Dynamical Systems." Source:
 https://arxiv.org/pdf/2509.00241
- Amari, S.-I. *Information Geometry and Its Applications.* Source:
 https://link.springer.com/book/10.1007/978-4-431-55978-8
- Kpotufe, S. "$k$-NN Regression Adapts to Local Intrinsic Dimension." Source:
 https://papers.nips.cc/paper/4455-k-nn-regression-adapts-to-local-intrinsic-dimension
- Lutz, J. H. "Dimension in Complexity Classes." Source:
 https://epubs.siam.org/doi/10.1137/S0097539701417723
- Kigami, J. *Analysis on Fractals.* Source:
 https://www.cambridge.org/core/books/analysis-on-fractals/contents/9EBF0F8BA597EBF4056457095760921A
- Lapidus, M. L., Levy-Vehel, J., and Rock, J. A. "Fractal Strings and
 Multifractal Zeta Functions." Source:
 https://link.springer.com/article/10.1007/s11005-009-0302-y
- Lawvere, F. W. "Metric spaces, generalized logic." Source:
 https://cir.nii.ac.jp/crid/1360576137827119744

## Bottom Line

The programme should not claim to invent dimension-as-growth-over-scale. That
idea is already widespread and technically mature. The credible claim is that
the observational framework gives a unified source for the refinements,
entropies, empirical witnesses, and valuations that determine which dimension
appears in finite-sample reconstruction rates.
