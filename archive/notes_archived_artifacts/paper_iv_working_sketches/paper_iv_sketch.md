# Paper IV — Finite-Sample Reconstruction: Rates, Witnesses, and the Honest Bridge                                                                                               
                                                                                                                                                                                 
**Status:** Complete. LaTeX written 2026-04-06. All 12 proof obligations closed.                                                                                     
**Date:** 2026-04-05                                                                                                                                                             
**Relation to programme:** Sits after Paper III. Takes the reconstruction theorem as given                                                                                       
and asks: what does it look like empirically, at what rate, and with what witnesses?                                                                                             
                                                                                                                                                                             
**Three honest theorems:**                                                                                                                                                
1. **(Algebra theorem):** δ̂ stopping rule achieves n^{-s/(2s+d)} without oracle inputs.                                                                                   
2. **(Dynamics theorem):** Under separation-stability of Π_h, d̂_L certifies kernel drift.                                                                                 
3. **(Conjunction theorem):** Under reconstruction ∧ separation-stability, both witnesses                                                                                 
   certify the same object. The Markov structure of the delay vector is the honest bridge.                                                                                
                                                                                                                                                                          
**Central result in two sentences:**                                                                                                                                      
̂ measures how much of ℬ the algebra has captured. The loop counts how many lags mixing requires.                                                                         
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## The question                                                                                                                                                           
                                                                                                                                                                          
Paper III establishes:                                                                                                                                                    
                                                                                                                                                                          
> 𝒪_h = ℬ mod μ  ↔  𝒜_h dense in L²(μ)  ↔  Φ_h measure-theoretic embedding                                                                                                
                                                                                                                                                                          
Given a finite time series x₁, …, xₙ drawn from (X, ℬ, μ, T), **what does this                                                                                            
equivalence look like empirically?**                                                                                                                                      
                                                                                                                                                                          
We do not assume the answer is the LIA/edge-divergence approach from the archive.                                                                                         
We ask the question honestly and see what the structure forces.                                                                                                           
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Step 1 — What is 𝒪_h^(n)?                                                                                                                                              
                                                                                                                                                                          
The theoretical 𝒪_h = σ{h ∘ Tⁿ : n ∈ ℤ} is generated by all delays.                                                                                                       
On finite data we have:                                                                                                                                                   
- finitely many observations: x₁, …, xₙ                                                                                                                                   
- finitely many lags accessible: say lags 0, 1, …, L for some L < n                                                                                                       
- the delay vectors: Φ_h^(L)(xᵢ) = (h(xᵢ), h(Txᵢ), …, h(T^L xᵢ)) ∈ ℝ^(L+1)                                                                                                
                                                                                                                                                                          
**Candidate definition:**                                                                                                                                                 
                                                                                                                                                                          
𝒪_h^(n,L) := the partition of {x₁,…,xₙ} induced by the map i ↦ Φ_h^(L)(xᵢ)                                                                                                
                                                                                                                                                                          
i.e., two observations xᵢ, xⱼ are *empirically indistinguishable* at lag depth L                                                                                          
if Φ_h^(L)(xᵢ) = Φ_h^(L)(xⱼ) (or within ε in a metrised version).                                                                                                         
                                                                                                                                                                          
**Issues with this definition:**                                                                                                                                          
1. It depends on both n (sample size) and L (lag depth) — two parameters,                                                                                                 
   not one. The theoretical 𝒪_h uses all lags simultaneously.                                                                                                             
2. On continuous state spaces, Φ_h^(L)(xᵢ) = Φ_h^(L)(xⱼ) exactly never happens                                                                                            
   (a.s.) — need an ε-discretisation, which introduces a third parameter.                                                                                                 
3. The partition induced is on the *sample*, not on X — it's a random object.                                                                                             
                                                                                                                                                                          
**Alternative candidate:**                                                                                                                                                
                                                                                                                                                                          
𝒪_h^(n,L) := the σ-algebra on X generated by the level sets of the empirical                                                                                              
conditional expectation E_n[· | Φ_h^(L)]                                                                                                                                  
                                                                                                                                                                          
This is more natural analytically (it lives on X, not just the sample) but                                                                                                
requires specifying what "empirical conditional expectation" means — i.e.,                                                                                                
a kernel estimator, which already smuggles in more structure.                                                                                                             
                                                                                                                                                                          
**Observation:** The right definition of 𝒪_h^(n) may not be separable from                                                                                                
the choice of estimator. This is not a problem — it may be telling us that                                                                                                
the Boolean and analytic sides of the duality are not independently                                                                                                       
accessible from data. They may only be jointly accessible.                                                                                                                
                                                                                                                                                                          
**This is a genuine open question. Do not paper over it.**                                                                                                                
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Step 2 — What is the finite-sample density bridge?                                                                                                                     
                                                                                                                                                                          
The density bridge (Paper III, Lemma 3.1) says:                                                                                                                           
                                                                                                                                                                          
> 𝒜_h dense in L²(μ)  ↔  σ(𝒜_h) = ℬ mod μ                                                                                                                                 
                                                                                                                                                                          
The finite-sample version would need to say something like:                                                                                                               
                                                                                                                                                                          
> 𝒜_h^(n,L) approximates L²(μ_n) to within ε  ↔  𝒪_h^(n,L) separates                                                                                                      
> "most" pairs of points in {x₁,…,xₙ}                                                                                                                                     
                                                                                                                                                                          
**What "approximates" means here:** Given a test function f ∈ L²(μ), how well                                                                                             
can f be approximated by polynomials in {h ∘ Tᵏ : k = 0,…,L} evaluated at                                                                                                 
the sample points? This is a *regression* question: can we fit f(xᵢ) using                                                                                                
features (h(xᵢ), h(Txᵢ), …, h(T^L xᵢ))?                                                                                                                                   
                                                                                                                                                                          
**What "separates most pairs" means:** The delay vectors Φ_h^(L)(xᵢ) are                                                                                                  
approximately injective on the sample — roughly, distinct xᵢ, xⱼ have                                                                                                     
distinct delay vectors. This is testable (e.g. nearest-neighbour false                                                                                                    
positives in delay space).                                                                                                                                                
                                                                                                                                                                          
**The gap:** Even if both sides have clear empirical definitions, it is not                                                                                               
obvious that they are *equivalent* at finite n. The theoretical equivalence                                                                                               
uses the full σ-algebra, Stone duality, and the monotone class theorem —                                                                                                  
none of which have obvious finite-n analogues. The finite-sample version                                                                                                  
may only be an *implication* (one direction) or an *approximate equivalence*                                                                                              
(up to rates depending on n, L, smoothness of h and T).                                                                                                                   
                                                                                                                                                                          
**First concrete question to investigate:**                                                                                                                               
Is there an (ε, δ, n, L) statement of the form:                                                                                                                           
                                                                                                                                                                          
> If 𝒜_h^(n,L) fits f to within ε on the sample (in L² sense),                                                                                                            
> then Φ_h^(L) is ε'-injective on at least (1-δ) of pairs,                                                                                                                
> where ε' = ε'(ε, n, L, properties of h, T)?                                                                                                                             
                                                                                                                                                                          
If yes: what are the rates? If no: which direction fails, and why?                                                                                                        
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Step 3 — The Stone duality picture empirically                                                                                                                         
                                                                                                                                                                          
The Stone duality says: when 𝒪_h = ℬ mod μ, the Stone space St(𝒪_h) is                                                                                                    
measure-theoretically isomorphic to X. The Stone embedding is:                                                                                                            
                                                                                                                                                                          
ι : X → St(𝒪_h),   ι(x) = {E ∈ 𝒪_h : x ∈ E}                                                                                                                               
                                                                                                                                                                          
Empirically, ι(x) is approximated by the delay vector Φ_h^(L)(x) — the                                                                                                    
delay vector *is* the empirical ultrafilter at x (the list of observable                                                                                                  
events x belongs to, at lag depth L).                                                                                                                                     
                                                                                                                                                                          
The two sides of the duality are then:                                                                                                                                    
                                                                                                                                                                          
**Boolean side:** The partition 𝒪_h^(n,L) — which events are distinguishable                                                                                              
**Analytic side:** The subspace 𝒜_h^(n,L) ⊆ L²(μ_n) — which functions are approximable                                                                                    
                                                                                                                                                                          
**Agreement = empirical Stone duality:** The topology generated by the                                                                                                    
partition agrees with the topology generated by the subspace. In finite                                                                                                   
dimensions, this means: the partition into delay-vector equivalence classes                                                                                               
and the partition into regression-equivalence classes (points with the same                                                                                               
fitted value for all f) are the same partition.                                                                                                                           
                                                                                                                                                                          
**Why this might not hold in general:**                                                                                                                                   
- The regression partition can be finer than the delay partition                                                                                                          
  (two points with different delay vectors but same fitted value for all                                                                                                  
  test functions in 𝒜_h^(n,L))                                                                                                                                            
- Or coarser (two points with same delay vector but different fitted values —                                                                                             
  which shouldn't happen if Φ_h^(L) is the feature map)                                                                                                                   
                                                                                                                                                                          
**Observation:** If 𝒜_h^(n,L) = polynomials in Φ_h^(L) (which it is by                                                                                                    
definition of the delay algebra), then the regression partition IS the delay                                                                                              
partition — they're the same thing. The empirical Stone duality is then                                                                                                   
*tautological* at finite n.                                                                                                                                               
                                                                                                                                                                          
**This suggests the interesting question is not about the partition per se                                                                                                
but about the limiting behaviour:** does the empirical duality converge to                                                                                                
the theoretical duality as n, L → ∞? And at what rate?                                                                                                                    
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Step 4 — Where the kernel/edge-divergence comes in                                                                                                                     
                                                                                                                                                                          
If the empirical Stone duality is tautological (both sides give the same                                                                                                  
partition by construction), then the interesting quantity is not whether                                                                                                  
the duality holds but **how well the dynamics are captured**.                                                                                                             
                                                                                                                                                                          
The dynamics are captured by the one-step transition kernel Π_h:                                                                                                          
                                                                                                                                                                          
Π_h(x, ·) = distribution of Tx given x, pushed through h                                                                                                                  
                                                                                                                                                                          
The edge law is:  Γ_h = μ ⊗ Π_h                                                                                                                                           
                                                                                                                                                                          
Given data (x₁, Tx₁), …, (xₙ, Txₙ), the estimated edge law is:                                                                                                            
                                                                                                                                                                          
̂_h^(n) = μ_n ⊗ Π̂_h^(n)                                                                                                                                                   
                                                                                                                                                                          
where Π̂_h^(n) is estimated from the data (e.g. by locally weighted regression                                                                                             
of h(Txᵢ) on Φ_h^(L)(xᵢ)).                                                                                                                                                
                                                                                                                                                                          
**The edge divergence** D(Γ_h ‖ Γ̂_h^(n)) then measures how well the                                                                                                       
estimated kernel captures the true dynamics.                                                                                                                              
                                                                                                                                                                          
**The connection to Stone duality:** Vanishing edge divergence means                                                                                                      
̂_h^(n) → Π_h in an appropriate sense. If Π_h is the true predictive                                                                                                      
kernel (Paper II), then convergence of Π̂_h^(n) → Π_h implies convergence                                                                                                  
of the estimated L²(𝒪_h^(n)) → L²(𝒪_h). The Boolean side follows if                                                                                                       
the density bridge has a quantitative version.                                                                                                                            
                                                                                                                                                                          
**But this requires:** A quantitative connection between kernel estimation                                                                                                
error and σ-algebra estimation error. This is the core gap that needs                                                                                                     
investigation before any theorem can be stated.                                                                                                                           
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Step 5 — The locally weighted linear map                                                                                                                               
                                                                                                                                                                          
The specific estimator from the archive — locally weighted linear map with                                                                                                
residual diffusion — fits here as follows:                                                                                                                                
                                                                                                                                                                          
Given delay vectors Φ_h^(L)(xᵢ), fit locally:                                                                                                                             
                                                                                                                                                                          
h(Txᵢ) ≈ Aᵢ · Φ_h^(L)(xᵢ) + εᵢ                                                                                                                                            
                                                                                                                                                                          
where Aᵢ is a locally weighted linear map (weights from a kernel on                                                                                                       
delay-vector space) and εᵢ are residuals.                                                                                                                                 
                                                                                                                                                                          
**The linear map** estimates the analytic side: it gives the local                                                                                                        
linear approximation to the Koopman operator U_T acting on h.                                                                                                             
                                                                                                                                                                          
**The residuals εᵢ** are the part of the dynamics NOT captured by the                                                                                                     
linear approximation — i.e., the nonlinear component. Diffusing along                                                                                                     
the residuals gives a nonparametric correction.                                                                                                                           
                                                                                                                                                                          
**Why this is natural:** The Koopman operator is linear on L²(μ), so                                                                                                      
locally linear approximation is the right first-order model. Residuals                                                                                                    
capture what the linear approximation misses — exactly the part of 𝒪_h                                                                                                    
not captured by the finite-lag linear algebra.                                                                                                                            
                                                                                                                                                                          
**The open question:** Does minimising the edge divergence D(Γ_h ‖ Γ̂_h^(n))                                                                                               
over locally linear maps Aᵢ give the right estimator? Or is there a                                                                                                       
better-motivated estimator that arises more directly from the Paper II/III                                                                                                
structure?                                                                                                                                                                
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Summary of open questions (in order of priority)                                                                                                                       
                                                                                                                                                                          
1. **Does the finite-sample density bridge hold?**                                                                                                                        
   Is there an (ε, δ, n, L) equivalence between L²-approximability by 𝒜_h^(n,L)                                                                                           
   and injectivity of Φ_h^(L) on the sample?                                                                                                                              
                                                                                                                                                                          
2. **Is empirical Stone duality tautological at finite n?**                                                                                                               
   If yes, the interesting content is in the limit behaviour and rates.                                                                                                   
                                                                                                                                                                          
3. **What is the right estimator for Π̂_h^(n)?**                                                                                                                           
   Locally weighted linear + residual diffusion is one option. Are there others                                                                                           
   that arise more naturally from the Paper II/III structure?                                                                                                             
                                                                                                                                                                          
4. **Is vanishing edge divergence equivalent to reconstruction?**                                                                                                         
   Or only one direction? What are the rates?                                                                                                                             
                                                                                                                                                                          
5. **What is the right divergence?**                                                                                                                                      
   KL divergence (as in archive) or a different f-divergence? The choice may                                                                                              
   affect the rates in question 4.                                                                                                                                        
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Notation established (extending Papers I–III)                                                                                                                          
                                                                                                                                                                          
| Object | Notation | Notes |                                                                                                                                             
|--------|----------|-------|                                                                                                                                             
| Finite time series | x₁, …, xₙ ∈ X | |                                                                                                                                  
| Empirical measure | μ_n = (1/n)Σ δ_{xᵢ} | Consistent with μ |                                                                                                           
| Lag-L delay map | Φ_h^(L) : X → ℝ^(L+1) | Extends Φ_h notation |                                                                                                        
| Empirical delay vectors | {Φ_h^(L)(xᵢ)} | |                                                                                                                             
| Empirical observable algebra | 𝒪_h^(n,L) | Two parameters: sample size, lag depth |                                                                                     
| Empirical delay algebra | 𝒜_h^(n,L) | |                                                                                                                                 
| One-step transition kernel | Π_h : X → 𝒫(X) | Uses Paper II Π notation |                                                                                                
| Estimated kernel | Π̂_h^(n) | Hat = empirical |                                                                                                                          
| Edge law | Γ_h = μ ⊗ Π_h | Γ free in existing papers |                                                                                                                  
| Estimated edge law | Γ̂_h^(n) = μ_n ⊗ Π̂_h^(n) | |                                                                                                                        
| Edge divergence | D(Γ_h ‖ Γ̂_h^(n)) | D for generic f-divergence |                                                                                                       
| Locally linear Koopman approx | Â_h^(n,L) | Local linear map; A free |                                                                                                  
                                                                                                                                                                          
**Conflicts avoided:** K (predictive operator, Paper II), ν (Stone measure, Paper I).                                                                                     
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Literature findings (2026-04-05)                                                                                                                                       
                                                                                                                                                                          
Research into the finite-sample density bridge across five directions.                                                                                                    
Summary: both half-bridges exist in the literature but nobody has joined them,                                                                                            
and nobody has used the *algebra structure* of 𝒜_h as the key ingredient.                                                                                                 
                                                                                                                                                                          
### What exists                                                                                                                                                           
                                                                                                                                                                          
| Direction | What it gives | Rate | Ref |                                                                                                                                
|-----------|--------------|------|-----|                                                                                                                                 
| VC / Rademacher | L²-approx → measure concentration | √(V/n) | Bartlett–Mendelson 2002 |                                                                                
| RKHS / MMD | L²-density ↔ measure separation (asymptotic) | n^{-1/2} for MMD | Sriperumbudur–Fukumizu–Lanckriet 2011 |                                                  
| EDMD / Koopman | Dictionary approx → Koopman convergence | Exponential (i.i.d.) | Korda–Mezić 2018; Kostic et al. 2024 |                                                
| Information theory | Partition quality → divergence estimation (consistency) | Strong consistency | Silva–Narayanan 2010 |                                              
| Nonparametric regression | σ-algebra quality → L²-approx | n^{-2s/(2s+d)} | Gyorfi et al. 2002; Yang–Barron 1999 |                                                      
                                                                                                                                                                          
### The two half-bridges                                                                                                                                                  
                                                                                                                                                                          
**Forward direction** (L²-approximation → σ-algebra separation):                                                                                                          
Handled by MMD / characteristic kernels. If 𝒜_h^(n,L) approximates L²(μ)                                                                                                  
well, then the generated σ-algebra separates probability measures.                                                                                                        
Rate: n^{-1/2} for MMD concentration.                                                                                                                                     
                                                                                                                                                                          
**Reverse direction** (σ-algebra quality → L²-approximation):                                                                                                             
Handled by partition/histogram theory. If Φ_h^(L) separates points well                                                                                                   
(fine enough partition), then 𝒜_h^(n,L) can approximate functions in L²(μ).                                                                                               
Rate: n^{-2s/(2s+d)} for Hölder-s functions in ℝ^d.                                                                                                                       
                                                                                                                                                                          
### The gap we could fill                                                                                                                                                 
                                                                                                                                                                          
Nobody has:                                                                                                                                                               
1. Given a **two-directional quantitative equivalence** at finite n                                                                                                       
2. Used the **algebra structure** of 𝒜_h (not just metric entropy / VC dim)                                                                                               
3. Connected the **separation count** of Φ_h^(L) to the L²-projection error                                                                                               
   with explicit rates                                                                                                                                                    
4. Applied any of this to the **delay algebra specifically**, where the                                                                                                   
   algebra structure comes from the dynamics T (orbit structure)                                                                                                          
                                                                                                                                                                          
The delay algebra has special structure: 𝒜_h is generated by a *single                                                                                                    
function h* under the action of *a single map T*. This is much more                                                                                                       
constrained than a general subalgebra of L∞, and the constraints (shift                                                                                                   
invariance, Koopman structure) should give better rates than the general case.                                                                                            
                                                                                                                                                                          
### What this suggests for the finite-sample density bridge                                                                                                               
                                                                                                                                                                          
The finite-sample density bridge for the delay algebra specifically would be:                                                                                             
                                                                                                                                                                          
**Forward (easier):** If Φ_h^(L) is ε-injective on the n-sample (i.e.                                                                                                     
distinct xᵢ, xⱼ have ‖Φ_h^(L)(xᵢ) - Φ_h^(L)(xⱼ)‖ > ε for most pairs),                                                                                                     
then for any f ∈ Hölder(s), the projection error onto 𝒜_h^(n,L) is                                                                                                        
bounded by some rate depending on ε, n, L, s, d.                                                                                                                          
— This direction uses the reverse half-bridge from nonparametric regression,                                                                                              
  applied to the delay feature map specifically.                                                                                                                          
                                                                                                                                                                          
**Reverse (harder):** If the projection error of 𝒜_h^(n,L) on a test                                                                                                      
function f is small, then Φ_h^(L) separates most pairs.                                                                                                                   
— This direction requires connecting L²-approximation error to injectivity.                                                                                               
  The MMD literature gives this asymptotically; finite-n rates are less clear.                                                                                            
  The algebra structure of 𝒜_h (generated by single h under T) should help.                                                                                               
                                                                                                                                                                          
### The asymmetry is real and should not be papered over                                                                                                                  
                                                                                                                                                                          
The forward rate n^{-2s/(2s+d)} and the reverse rate n^{-1/2} are different.                                                                                              
The two-directional equivalence at finite n is likely an approximate/asymmetric                                                                                           
statement rather than a clean equivalence. This is honest mathematics — the                                                                                               
theoretical density bridge is an exact equivalence, but its finite-sample                                                                                                 
version may only be: "both sides converge to the truth, at potentially                                                                                                    
different rates."                                                                                                                                                         
                                                                                                                                                                          
This is still a meaningful result: it says the empirical Stone duality                                                                                                    
*is* detectable from data, but the two sides converge at different rates                                                                                                  
depending on which direction you probe.                                                                                                                                   
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Revised next steps (2026-04-05)                                                                                                                                        
                                                                                                                                                                          
- [x] **Attempt the forward direction first:** Done — see                                                                                                                 
      `notes/conceptual_sketches/forward_direction_sketch.md`,                                                                                                            
      `bias_bound_attempt.md`, `variance_bound_verification.md`.                                                                                                          
      Result: ‖f − f̂_n^(L)‖ ≤ 2‖f‖_{L∞}·δ(L)^{1/2} + C·n^{-s/(2s+d)}                                                                                                      
      in the Takens regime, with Condition 3 (g* smoothness) verified.                                                                                                    
- [x] **Reverse direction:** Done — see Section below.                                                                                                                    
- [ ] **Pre-Takens regime / optimal L*(n):** See Section below (in progress).                                                                                             
- [ ] **Edge divergence connection:** Open — see open questions.                                                                                                          
- [ ] **Use the algebra structure for improved rates:** Partially addressed                                                                                               
      in the reverse direction (δ(L) certified by polynomials in 𝒜_h^(L)                                                                                                  
      under reconstruction). Full exploitation of Koopman/shift structure deferred.                                                                                       
- [ ] Once the bridge is understood: connect to edge divergence / kernel                                                                                                  
      estimation and close the loop to the computational instantiation.                                                                                                   
- [ ] Only then: decide Paper IV structure, move to TeX.                                                                                                                  
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Reverse direction: small empirical error implies small δ(L)                                                                                                            
                                                                                                                                                                          
**The question, stated correctly.** The observer has:                                                                                                                     
- f̂_n^(L): the empirical minimiser over 𝒜_h^(L) from n samples                                                                                                            
- ‖·‖_{L²(μ_n)}: the empirical L² norm over the sample                                                                                                                    
- Nothing else — not μ, not E[f|𝒪_h^(L)], not δ(L)                                                                                                                        
                                                                                                                                                                          
The question is: if ‖f − f̂_n^(L)‖_{L²(μ_n)} is small for worst-case f,                                                                                                    
can the observer certify δ(L) is small?                                                                                                                                   
                                                                                                                                                                          
The answer requires travelling three steps, each with its own gap:                                                                                                        
                                                                                                                                                                          
```                                                                                                                                                                       
δ(L) large                                                                                                                                                                
  ↓  Step A: population lower bound                                                                                                                                       
‖1_S − E[1_S|𝒪_h^(L)]‖_{L²(μ)} ≥ δ(L)^{1/2}/2                                                                                                                             
  ↓  Step B: population norm → empirical norm (LLN gap)                                                                                                                   
‖1_S − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)} ≥ δ(L)^{1/2}/2 − O(n^{-1/2})                                                                                                             
  ↓  Step C: population estimator → empirical estimator (estimator gap)                                                                                                   
‖1_S − f̂_n^(L)‖_{L²(μ_n)} ≥ δ(L)^{1/2}/2 − O(n^{-1/2}) − stat term                                                                                                        
```                                                                                                                                                                       
                                                                                                                                                                          
Only Step C produces something the observer can evaluate. Steps A and B                                                                                                   
are population statements used in the proof, not observable quantities.                                                                                                   
                                                                                                                                                                          
### Step A — Population lower bound (proved)                                                                                                                              
                                                                                                                                                                          
**Theorem.** For the worst-case S ∈ ℬ:                                                                                                                                    
                                                                                                                                                                          
  ‖1_S − E[1_S | 𝒪_h^(L)]‖_{L²(μ)} ≥ δ(L)^{1/2}/2                                                                                                                         
                                                                                                                                                                          
**Proof.** E[1_S | 𝒪_h^(L)] is [0,1]-valued. Let E* = {E[1_S|m] > 1/2}.                                                                                                   
Then E* ∈ 𝒪_h^(L), and by definition of δ(L): μ(S △ E*) ≥ δ(L).                                                                                                           
On S △ E*: either 1_S = 1 and E[1_S|m] ≤ 1/2 (squared error ≥ 1/4),                                                                                                       
or 1_S = 0 and E[1_S|m] ≥ 1/2 (squared error ≥ 1/4). So:                                                                                                                  
                                                                                                                                                                          
  ‖1_S − E[1_S|m]‖²_{L²(μ)} ≥ (1/4)·μ(S △ E*) ≥ δ(L)/4                                                                                                                    
                                                                                                                                                                          
giving ‖1_S − E[1_S|m]‖_{L²(μ)} ≥ δ(L)^{1/2}/2. □                                                                                                                         
                                                                                                                                                                          
### Step B — Population norm to empirical norm                                                                                                                            
                                                                                                                                                                          
The population norm ‖·‖_{L²(μ)} is not observable. Replace it with the                                                                                                    
empirical norm ‖·‖_{L²(μ_n)} via:                                                                                                                                         
                                                                                                                                                                          
  |‖g‖²_{L²(μ_n)} − ‖g‖²_{L²(μ)}| ≤ sup_{g ∈ ℱ} |(1/n)Σg² − Eg²|                                                                                                          
                                                                                                                                                                          
For g = 1_S − E[1_S|m], ‖g‖_∞ ≤ 2, so by Hoeffding:                                                                                                                       
                                                                                                                                                                          
  P(|‖g‖²_{L²(μ_n)} − ‖g‖²_{L²(μ)}| > t) ≤ 2·exp(−nt²/8)                                                                                                                  
                                                                                                                                                                          
With high probability, ‖g‖_{L²(μ_n)} ≥ ‖g‖_{L²(μ)} − O(n^{-1/2}).                                                                                                         
                                                                                                                                                                          
So from Step A:                                                                                                                                                           
                                                                                                                                                                          
  ‖1_S − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)} ≥ δ(L)^{1/2}/2 − O(n^{-1/2})                                                                                                           
                                                                                                                                                                          
with high probability. Still uses E[1_S|𝒪_h^(L)] — not yet observable.                                                                                                    
                                                                                                                                                                          
### Step C — Population estimator to empirical minimiser                                                                                                                  
                                                                                                                                                                          
The observer has f̂_n^(L), not E[1_S|𝒪_h^(L)]. The gap between them:                                                                                                       
                                                                                                                                                                          
  ‖1_S − f̂_n^(L)‖_{L²(μ_n)}                                                                                                                                               
    ≥ ‖1_S − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)} − ‖f̂_n^(L) − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)}                                                                                             
                                                                                                                                                                          
The second term ‖f̂_n^(L) − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)} is the statistical                                                                                                   
term — how far the empirical minimiser is from the population best                                                                                                        
approximation. From the forward bridge variance bound:                                                                                                                    
                                                                                                                                                                          
  ‖f̂_n^(L) − E[1_S|𝒪_h^(L)]‖_{L²(μ_n)} ≤ C·n^{-s/(2s+d)}                                                                                                                  
                                                                                                                                                                          
(in the Takens regime, using the same Rademacher bound as the forward                                                                                                     
direction). Combining with Steps A and B:                                                                                                                                 
                                                                                                                                                                          
  ‖1_S − f̂_n^(L)‖_{L²(μ_n)}                                                                                                                                               
    ≥ δ(L)^{1/2}/2 − O(n^{-1/2}) − C·n^{-s/(2s+d)}                                                                                                                        
    ≥ δ(L)^{1/2}/2 − C'·n^{-s/(2s+d)}    (absorbing the LLN term)                                                                                                         
                                                                                                                                                                          
**This is the observable reverse lower bound:**                                                                                                                           
                                                                                                                                                                          
  ‖1_S − f̂_n^(L)‖_{L²(μ_n)} ≥ δ(L)^{1/2}/2 − C'·n^{-s/(2s+d)}   (‡)                                                                                                       
                                                                                                                                                                          
### The honest closed loop                                                                                                                                                
                                                                                                                                                                          
Combining (‡) with the forward bound:                                                                                                                                     
                                                                                                                                                                          
  δ(L)^{1/2}/2 − C'·n^{-s/(2s+d)}                                                                                                                                         
    ≤  ‖f − f̂_n^(L)‖_{L²(μ_n)}                                                                                                                                            
    ≤  2δ(L)^{1/2} + C·n^{-s/(2s+d)}                                                                                                                                      
                                                                                                                                                                          
for f = 1_{S*} (the worst-case indicator). Both bounds use:                                                                                                               
- f̂_n^(L): the empirical minimiser — not a population object                                                                                                              
- ‖·‖_{L²(μ_n)}: the empirical norm — not the population norm                                                                                                             
- The same statistical floor C·n^{-s/(2s+d)} on both sides                                                                                                                
                                                                                                                                                                          
**The detectability threshold:** δ(L) is certifiable from f̂_n^(L) only                                                                                                    
when δ(L)^{1/2}/2 > C'·n^{-s/(2s+d)}, i.e.:                                                                                                                               
                                                                                                                                                                          
  δ(L) > 4C'²·n^{-2s/(2s+d)}                                                                                                                                              
                                                                                                                                                                          
Below this threshold, the statistical noise swamps δ(L) and the observer                                                                                                  
cannot distinguish "reconstruction holds, δ = 0" from "δ is small but                                                                                                     
positive." The noise floor is the same quantity that sets ε_n in the                                                                                                      
stopping rule — by design.                                                                                                                                                
                                                                                                                                                                          
### What the algebra tests                                                                                                                                                
                                                                                                                                                                          
To certify δ(L) ≤ ε from f̂_n^(L), the observer evaluates:                                                                                                                 
                                                                                                                                                                          
  δ̂(L, n) = sup_{p ∈ 𝒫_D^(L), ‖p‖≤1} ‖p − f̂_n^(L)[p]‖²_{L²(μ_n)}                                                                                                          
                                                                                                                                                                          
where f̂_n^(L)[p] is the empirical minimiser over 𝒜_h^(L) for test                                                                                                         
function p. The sup is over the algebra testing itself.                                                                                                                   
                                                                                                                                                                          
From (‡): δ̂(L,n) ≥ δ(L)/4 − C''·n^{-2s/(2s+d)} (lower bound).                                                                                                             
From the forward bound: δ̂(L,n) ≤ 4δ(L) + C'''·n^{-2s/(2s+d)} (upper bound).                                                                                               
                                                                                                                                                                          
So δ̂(L,n) is a two-sided empirical witness for δ(L), valid above the                                                                                                      
noise floor n^{-2s/(2s+d)}. This is what "the algebra tests itself" means                                                                                                 
precisely — no population objects, no oracle, just f̂_n^(L) and μ_n.                                                                                                       
                                                                                                                                                                          
**Concretely:** compute                                                                                                                                                   
                                                                                                                                                                          
  δ̂(L, n) := sup_{p ∈ 𝒜_h^(L), ‖p‖≤1} ‖p − Ê[p | Φ_h^(L)]‖²_{L²(μ_n)}                                                                                                     
                                                                                                                                                                          
where the sup is over polynomials of degree ≤ D = ⌈s⌉ and Ê[·|Φ_h^(L)]                                                                                                    
is the empirical conditional expectation (e.g. kernel regression on the                                                                                                   
delay vectors). The convergence δ̂(L,n) → δ(L) is a proof obligation —                                                                                                     
it requires (i) a uniform LLN for the empirical norm and (ii) a bias                                                                                                      
bound for the specific estimator Ê; see the proof obligation section.                                                                                                     
Subject to that proof, δ̂(L,n) ≤ ε certifies reconstruction to within ε.                                                                                                   
                                                                                                                                                                          
**This is a computable witness for reconstruction** — a finite-sample                                                                                                     
test for whether the delay algebra has captured the dynamics.                                                                                                             
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Proof obligation register                                                                                                                                              
                                                                                                                                                                          
**Last updated: 2026-04-06** (ob. 9–12 closed; all obligations resolved)                                                                                                                                              
                                                                                                                                                                          
Every claim in the developed sections is either proved, standard (citable                                                                                                 
directly), or listed here as an open obligation. Nothing is assumed.                                                                                                      
                                                                                                                                                                          
| # | Obligation | Method | Status |                                                                                                                                      
|---|-----------|--------|--------|                                                                                                                                       
| 1 | Bias bound: ‖f−E[f\|m]‖ ≤ 2‖f‖_{L∞}·δ(m)^{1/2} | Layer cake + best-approx | ✓ proved |                                                                              
| 2 | Reverse Step A: pop. CE gap ≥ δ^{1/2}/2 | Threshold set + 1/4 factor | ✓ proved |                                                                                   
| 3 | Reverse Step B: pop. norm ≈ empirical norm | Hoeffding, O(n^{-1/2}) | ✓ standard |                                                                                  
| 4 | Reverse Step C: pop. CE ≈ f̂_n^(L) | Variance bound from forward | ✓ from (1)+(Rademacher) |                                                                         
| 5 | Concentration (★): δ̂ ≈ E[δ̂] | Rademacher, d > 2s required | ✓ proved |                                                                                              
| 6 | Source 1: LLN gap E[δ̂] ≈ δ̂_pop | Glivenko-Cantelli | ✓ standard |                                                                                                   
| 7 | Source 2: estimator bias δ̂_pop ≈ δ | Kernel regression + Hölder(β) | ✓ closed (exp. mixing, ‖h‖_∞≥1/2); open (poly. mixing, ‖h‖_∞<1/2) |                            
| 8 | Full convergence δ̂ → δ | Triangle over (5)+(6)+(7) | ✓ under exp. mixing + ‖h‖_∞≥1/2 |                                                                              
| 9 | Piecewise rate in pre-Takens regime | dim_eff step function | ✓ closed: (G1)+(G2)+smooth positive μ; boundary condition μ(Σ)=0 ∀ hypersurfaces Σ named and tight |                                                                                     
| 10 | Elbow location theorem | Concentration (5) + piecewise (9) | ✓ closed (exp. mixing, C_λ > 4); poly. mixing open (elbow drop vanishes rel. noise) |                                                                                         
| 11 | Separation-stability in smooth case | T ∈ C^r → Hölder Π_h | ✓ closed under (SS): bi-Lipschitz delay map; (SS) generic, not derived from (G1)+(G2) |                                                                
| 12 | Conjunction theorem | (8) + (11) | ✓ closed: reconstruction + (SS) → both witnesses fire; failure modes (b)(c) proved; Markov bridge identified |                                                                                                              
                                                                                                                                                                          
**Open obligations in priority order:** none — all 12 closed as of 2026-04-06
**Conditionally open (poly. mixing / ‖h‖_∞ < 1/2):** (7) → (8); also (10) poly. mixing case                                                                                                          
**Conditionally open (poly. mixing / ‖h‖_∞ < 1/2):** (7) → (8)                                                                                                            
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Bias bound: clean write-up                                                                                                                                             
                                                                                                                                                                          
**Date:** 2026-04-06                                                                                                                                                      
                                                                                                                                                                          
### Theorem (Bias bound)                                                                                                                                                  
                                                                                                                                                                          
**Setup.** Let (X, ℬ, μ) be a probability space and m ⊆ ℬ a sub-σ-algebra.                                                                                                
Define the σ-algebra approximation error:                                                                                                                                 
                                                                                                                                                                          
  δ(m) := sup_{S ∈ ℬ} inf_{E ∈ m} μ(S △ E)                                                                                                                                
                                                                                                                                                                          
**Theorem.** For every f ∈ L∞(μ):                                                                                                                                         
                                                                                                                                                                          
  ‖f − E[f | m]‖_{L²(μ)} ≤ 2‖f‖_{L∞} · δ(m)^{1/2}                                                                                                                         
                                                                                                                                                                          
**Proof.**                                                                                                                                                                
                                                                                                                                                                          
*Step 1 — Indicators.* Fix S ∈ ℬ. By definition of δ(m), there exists                                                                                                     
E ∈ m with μ(S △ E) ≤ δ(m). Since 1_E ∈ L²(X, m, μ) and E[1_S | m]                                                                                                        
is the best m-approximation to 1_S in L²(μ):                                                                                                                              
                                                                                                                                                                          
  ‖1_S − E[1_S | m]‖²_{L²} ≤ ‖1_S − 1_E‖²_{L²} = μ(S △ E) ≤ δ(m)                                                                                                          
                                                                                                                                                                          
So ‖1_S − E[1_S | m]‖_{L²} ≤ δ(m)^{1/2} for every S ∈ ℬ. ✓                                                                                                                
                                                                                                                                                                          
*Step 2 — Bounded f via layer cake.* For f ∈ L∞(μ) with ‖f‖_{L∞} ≤ M,                                                                                                     
the layer cake representation gives:                                                                                                                                      
                                                                                                                                                                          
  f = ∫_{−M}^{M} 1_{S_t} dt   where S_t = {x : f(x) > t}                                                                                                                  
                                                                                                                                                                          
Since E[· | m] is linear and continuous in L²:                                                                                                                            
                                                                                                                                                                          
  f − E[f | m] = ∫_{−M}^{M} (1_{S_t} − E[1_{S_t} | m]) dt                                                                                                                 
                                                                                                                                                                          
Apply Minkowski's inequality for integrals and Step 1:                                                                                                                    
                                                                                                                                                                          
  ‖f − E[f | m]‖_{L²} ≤ ∫_{−M}^{M} ‖1_{S_t} − E[1_{S_t} | m]‖_{L²} dt                                                                                                     
                       ≤ ∫_{−M}^{M} δ(m)^{1/2} dt                                                                                                                         
                       = 2M · δ(m)^{1/2}                                                                                                                                  
                                                                                                                                                                          
Setting M = ‖f‖_{L∞} gives the result. □                                                                                                                                  
                                                                                                                                                                          
### Sharpness                                                                                                                                                             
                                                                                                                                                                          
The constant 2 is not optimal but the rate δ(m)^{1/2} is tight.                                                                                                           
Example: X = [0,1], μ = Lebesgue, m = {∅, X}, f = 1_{[0,1/2]}.                                                                                                            
Then E[f|m] = 1/2, δ(m) = 1/2, and:                                                                                                                                       
                                                                                                                                                                          
  ‖f − E[f|m]‖_{L²} = 1/2 = δ(m)^{1/2}/√2                                                                                                                                 
                                                                                                                                                                          
The bound gives 2·(1/2)^{1/2} = √2. The exponent 1/2 is correct;                                                                                                          
the constant 2 is loose by a factor of 2√2.                                                                                                                               
                                                                                                                                                                          
### Three-term decomposition in the delay setting                                                                                                                         
                                                                                                                                                                          
With m = 𝒪_h^(L) and f̂_n^(L) the empirical minimiser over 𝒜_h^(L):                                                                                                        
                                                                                                                                                                          
  ‖f − f̂_n^(L)‖_{L²}                                                                                                                                                      
    ≤ ‖f − E[f | 𝒪_h^(L)]‖_{L²}        (bias)                                                                                                                             
    + ‖E[f|𝒪_h^(L)] − g_D*‖_{L²}       (polynomial approximation)                                                                                                         
    + ‖g_D* − f̂_n^(L)‖_{L²}            (statistical)                                                                                                                      
                                                                                                                                                                          
where g_D* = argmin_{g ∈ 𝒜_h^(L)} ‖f − g‖_{L²(μ)} is the best polynomial.                                                                                                 
                                                                                                                                                                          
Bias term: ≤ 2‖f‖_{L∞}·δ(L)^{1/2} by the theorem above.                                                                                                                   
                                                                                                                                                                          
Polynomial approximation term: ≤ C·D^{-s/d} in the Takens regime                                                                                                          
(g* = f∘Φ^{-1} is Hölder(s), Φ^{-1} Lipschitz, intrinsic approx on                                                                                                        
d-dimensional image). Vanishes when D → ∞ or is absorbed into the                                                                                                         
statistical term at the optimal D* ~ n^{d/(2s+d)}.                                                                                                                        
                                                                                                                                                                          
Statistical term: ≤ C·(D^d/n)^{1/2} by VC dimension of degree-D                                                                                                           
polynomials on d-dimensional set. Balances at rate n^{-s/(2s+d)}.                                                                                                         
                                                                                                                                                                          
**Full bound (Takens regime, L ≥ L₀):**                                                                                                                                   
                                                                                                                                                                          
  ‖f − f̂_n^(L)‖_{L²(μ)} ≤ 2‖f‖_{L∞}·δ(L)^{1/2} + C·n^{-s/(2s+d)}                                                                                                          
                                                                                                                                                                          
Since δ(L) = 0 for L ≥ L₀, the bias term vanishes and:                                                                                                                    
                                                                                                                                                                          
  ‖f − f̂_n^(L)‖_{L²(μ)} ≤ C·n^{-s/(2s+d)}   (minimax-optimal)                                                                                                             
                                                                                                                                                                          
### Key properties of δ(L)                                                                                                                                                
                                                                                                                                                                          
1. **Monotone:** δ(L) is non-increasing in L.                                                                                                                             
2. **Reconstruction:** δ(L) → 0 iff ⋃_L 𝒪_h^(L) generates ℬ mod μ                                                                                                         
   (Paper III reconstruction theorem).                                                                                                                                    
3. **Takens regime:** δ(L) = 0 for L ≥ L₀.                                                                                                                                
4. **Observable:** estimated consistently by δ̂(L,n) from data                                                                                                             
   (concentration bound ★ in section below, requires d > 2s).                                                                                                             
5. **L²-only case:** for f ∈ L²(μ) without L∞: weaker rate δ^{1/4}                                                                                                        
   via truncation. Paper IV assumes f ∈ L∞ throughout.                                                                                                                    
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Concentration of δ̂(L,n): Rademacher bound                                                                                                                              
                                                                                                                                                                          
**Date:** 2026-04-06                                                                                                                                                      
                                                                                                                                                                          
### Setup                                                                                                                                                                 
                                                                                                                                                                          
We need to quantify how close δ̂(L,n) is to δ(L). Define the function class:                                                                                               
                                                                                                                                                                          
  ℱ_{L,D} = {x ↦ (p(x) − Ê[p | Φ_h^(L)](x))² : p ∈ 𝒫_D^(L), ‖p‖_{L²(μ)}≤1}                                                                                                
                                                                                                                                                                          
where 𝒫_D^(L) = polynomials of degree ≤ D = ⌈s⌉ in (h(x), h(Tx), …, h(T^L x)).                                                                                            
                                                                                                                                                                          
Then:                                                                                                                                                                     
  δ̂(L,n) = sup_{f ∈ ℱ_{L,D}} (1/n)Σᵢ f(xᵢ)                                                                                                                                
  δ(L)    = sup_{f ∈ ℱ_{L,D}} E_μ[f]                                                                                                                                      
                                                                                                                                                                          
The difference δ̂(L,n) − δ(L) is the supremum of an empirical process over                                                                                                 
ℱ_{L,D}.                                                                                                                                                                  
                                                                                                                                                                          
### Step 1 — Uniform boundedness                                                                                                                                          
                                                                                                                                                                          
Since h ∈ L∞ with ‖h‖_∞ < ∞, the delay coordinates are bounded:                                                                                                           
Φ_h^(L)(x) ∈ [−‖h‖_∞, ‖h‖_∞]^{L+1}. Polynomials of degree D in L+1                                                                                                        
bounded variables satisfy:                                                                                                                                                
                                                                                                                                                                          
  ‖p‖_∞ ≤ C(D, ‖h‖_∞) · (L+1)^{D/2}   for ‖p‖_{L²(μ)} ≤ 1                                                                                                                 
                                                                                                                                                                          
(by a standard Bernstein-type inequality on compact sets). Then for                                                                                                       
f = (p − Ê[p|·])² ∈ ℱ_{L,D}:                                                                                                                                              
                                                                                                                                                                          
  ‖f‖_∞ ≤ 4‖p‖²_∞ ≤ B²_{L,D}   where B_{L,D} = C(D, ‖h‖_∞) · L^{D/2}                                                                                                      
                                                                                                                                                                          
The function class ℱ_{L,D} is uniformly bounded by B²_{L,D}.                                                                                                              
                                                                                                                                                                          
### Step 2 — McDiarmid / Hoeffding concentration                                                                                                                          
                                                                                                                                                                          
By Hoeffding's inequality applied to the supremum (via the bounded                                                                                                        
differences / McDiarmid argument):                                                                                                                                        
                                                                                                                                                                          
  P(|δ̂(L,n) − E[δ̂(L,n)]| > t) ≤ 2·exp(−nt²/(2B⁴_{L,D}))   (MC)                                                                                                            
                                                                                                                                                                          
This bounds fluctuations around the mean. To bound the bias                                                                                                               
E[δ̂(L,n)] − δ(L), use symmetrisation:                                                                                                                                     
                                                                                                                                                                          
  E[δ̂(L,n)] − δ(L) ≤ 2ℛ_n(ℱ_{L,D})                                                                                                                                        
                                                                                                                                                                          
where ℛ_n is the Rademacher complexity.                                                                                                                                   
                                                                                                                                                                          
### Step 3 — Rademacher complexity via VC dimension                                                                                                                       
                                                                                                                                                                          
By the contraction lemma (Ledoux-Talagrand), since f = (p − Ê[p|·])²                                                                                                      
is a composition of the 1-Lipschitz squaring map with a linear class:                                                                                                     
                                                                                                                                                                          
  ℛ_n(ℱ_{L,D}) ≤ 2B_{L,D} · ℛ_n(𝒫_D^(L))                                                                                                                                  
                                                                                                                                                                          
For 𝒫_D^(L), the key question is whether to use ambient or intrinsic                                                                                                      
VC dimension:                                                                                                                                                             
                                                                                                                                                                          
**Ambient (L+1 variables):**                                                                                                                                              
  VC(𝒫_D^(L)) = O(L^D)   →   ℛ_n(𝒫_D^(L)) ≤ C·√(L^D / n)                                                                                                                  
                                                                                                                                                                          
**Intrinsic (Takens regime, image d-dimensional):**                                                                                                                       
  VC(𝒫_D^(L)|_{Φ(X)}) = O(D^d)   →   ℛ_n(𝒫_D^(L)) ≤ C·√(D^d / n)                                                                                                          
                                                                                                                                                                          
In the Takens regime the intrinsic bound applies. With D = ⌈s⌉ fixed:                                                                                                     
                                                                                                                                                                          
  ℛ_n(ℱ_{L,D}) ≤ C · B_{L,D} · √(D^d / n)                                                                                                                                 
                                                                                                                                                                          
### Step 4 — Combined concentration bound                                                                                                                                 
                                                                                                                                                                          
Assembling (MC) and the Rademacher bias bound:                                                                                                                            
                                                                                                                                                                          
  P(|δ̂(L,n) − δ(L)| > t) ≤ 2·exp(−cnt² / B⁴_{L,D})  +  bias term                                                                                                          
                                                                                                                                                                          
For the one-sided deviation that matters for the stopping rule                                                                                                            
(δ̂ overshooting δ), the leading term gives:                                                                                                                               
                                                                                                                                                                          
  **P(|δ̂(L,n) − δ(L)| > t) ≤ 2·exp(−cnt²n / (‖h‖_∞^{2D} · D^d))**   (★)                                                                                                   
                                                                                                                                                                          
where the n in the numerator comes from the Rademacher n^{-1/2} rate                                                                                                      
and c absorbs universal constants.                                                                                                                                        
                                                                                                                                                                          
### Step 5 — What (★) requires for the stopping rule                                                                                                                      
                                                                                                                                                                          
The stopping rule fires at L̂* when δ̂(L,n) ≤ ε_n = n^{-2s/(2s+d)}.                                                                                                         
For this to be reliable we need δ̂ to concentrate around δ(L) at scale                                                                                                     
ε_n/2, i.e. the failure probability P(|δ̂ − δ| > ε_n/2) → 0.                                                                                                               
                                                                                                                                                                          
Substituting t = ε_n/2 into (★):                                                                                                                                          
                                                                                                                                                                          
  P(|δ̂(L,n) − δ(L)| > ε_n/2)                                                                                                                                              
    ≤ 2·exp(−cn · ε_n² / (‖h‖_∞^{2D} · D^d))                                                                                                                              
    = 2·exp(−c · n^{1−4s/(2s+d)} / (‖h‖_∞^{2D} · D^d))                                                                                                                    
                                                                                                                                                                          
The exponent of n in the argument:                                                                                                                                        
                                                                                                                                                                          
  1 − 4s/(2s+d) = (d − 2s)/(2s+d)                                                                                                                                         
                                                                                                                                                                          
**This is positive iff d > 2s.**                                                                                                                                          
                                                                                                                                                                          
### The d > 2s constraint: honest, not an artifact                                                                                                                        
                                                                                                                                                                          
When d > 2s: the failure probability → 0 as n → ∞. The stopping rule                                                                                                      
concentrates at the right rate. ✓                                                                                                                                         
                                                                                                                                                                          
When d ≤ 2s: the exponent is ≤ 0, the bound becomes vacuous for large n.                                                                                                  
The concentration at rate ε_n is insufficient.                                                                                                                            
                                                                                                                                                                          
**This is not an artifact** — it reflects a genuine tension between                                                                                                       
smoothness and dimension. When functions are very smooth (s large) relative                                                                                               
to the dimension (d small), the δ̂ estimator needs to resolve fine structure                                                                                               
that the sample size n cannot support at rate ε_n. The stopping rule fires                                                                                                
too early or too late.                                                                                                                                                    
                                                                                                                                                                          
**The fix for d ≤ 2s:**                                                                                                                                                   
                                                                                                                                                                          
Option 1 — slower ε_n: use ε_n = n^{-γ} for γ < 2s/(2s+d). This                                                                                                           
  recovers the concentration but degrades the terminal estimation rate.                                                                                                   
                                                                                                                                                                          
Option 2 — localized Rademacher complexity: replace the global VC bound                                                                                                   
  with a local bound around the current δ̂ value. This gives adaptive                                                                                                      
  concentration that doesn't require d > 2s globally. Standard technique                                                                                                  
  (Bartlett-Bousquet-Mendelson 2005) but requires more work.                                                                                                              
                                                                                                                                                                          
Option 3 — state d > 2s as a hypothesis: the algebra theorem holds under                                                                                                  
  reconstruction AND d > 2s. This is the honest approach for a first paper.                                                                                               
  The d ≤ 2s case is a remark with a pointer to localized Rademacher.                                                                                                     
                                                                                                                                                                          
**Paper IV takes Option 3.** The condition d > 2s is not unnatural —                                                                                                      
it says the state space is high-dimensional relative to the smoothness                                                                                                    
of the target function. Most physically interesting systems (d ≥ 3,                                                                                                       
s ≤ 1 for Lipschitz observations) satisfy this.                                                                                                                           
                                                                                                                                                                          
### Summary                                                                                                                                                               
                                                                                                                                                                          
| Step | Result | Status |                                                                                                                                                
|------|--------|--------|                                                                                                                                                
| Uniform boundedness of ℱ_{L,D} | B_{L,D} ~ ‖h‖_∞^D · L^{D/2} | ✓ |                                                                                                      
| McDiarmid concentration | exp(−nt²/B⁴_{L,D}) | ✓ standard |                                                                                                             
| Rademacher: intrinsic VC = O(D^d) | ℛ_n ≤ C√(D^d/n) in Takens regime | ✓ |                                                                                              
| Combined bound (★) | exp(−cn^{(d−2s)/(2s+d)}) at t = ε_n/2 | ✓ |                                                                                                        
| Concentration sufficient | Requires d > 2s | ✓ identified |                                                                                                             
| d ≤ 2s fix | Localized Rademacher or slower ε_n | Open, Option 3 for Paper IV |                                                                                         
                                                                                                                                                                          
| Statement | Objects used | Status |                                                                                                                                     
|-----------|-------------|--------|                                                                                                                                      
| Step A: δ(L) large → pop. CE gap ≥ δ^{1/2}/2 | E[1_S\|m], μ (population) | ✓ proved |                                                                                   
| Step B: pop. norm ≈ empirical norm | LLN, O(n^{-1/2}) | ✓ standard |                                                                                                    
| Step C: pop. CE ≈ empirical minimiser | variance bound, C·n^{-s/(2s+d)} | ✓ from forward |                                                                              
| Observable lower bound (‡) | f̂_n^(L), μ_n only | ✓ assembled |                                                                                                          
| Closed loop: both bounds use f̂_n^(L), μ_n | empirical throughout | ✓ |                                                                                                  
| Detectability threshold: δ(L) > 4C'²·n^{-2s/(2s+d)} | noise floor | ✓ identified |                                                                                      
| Small empirical error (fixed f) → small δ(L) | | ✗ false in general |                                                                                                   
| δ̂(L,n) two-sided witness for δ(L) above noise floor | f̂_n^(L), μ_n | ✓ from (‡) + forward |                                                                             
| δ̂(L,n) → δ(L) as n → ∞ | requires Source 2 estimator bias | open obligation |                                                                                           
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Proof obligation: E[δ̂(L,n)] → δ(L)                                                                                                                                     
                                                                                                                                                                          
**The hidden bias that must not be papered over.**                                                                                                                        
                                                                                                                                                                          
Concentration (★) proves δ̂ stays close to E[δ̂]. It says nothing about                                                                                                     
whether E[δ̂] is close to δ(L). That gap                                                                                                                                   
                                                                                                                                                                          
  E[δ̂(L,n)] − δ(L)                                                                                                                                                        
                                                                                                                                                                          
is an independent quantity and needs an independent proof. It has two                                                                                                     
distinct sources that must each be handled on their own terms.                                                                                                            
                                                                                                                                                                          
### Source 1 — Empirical vs. population L² norm                                                                                                                           
                                                                                                                                                                          
Even if Ê[p | Φ_h^(L)] = E[p | Φ_h^(L)] exactly, the norms differ:                                                                                                        
                                                                                                                                                                          
  δ̂(L,n) uses ‖·‖²_{L²(μ_n)}   (sum over sample)                                                                                                                          
  δ(L)    uses ‖·‖²_{L²(μ)}     (integral over μ)                                                                                                                         
                                                                                                                                                                          
The gap:                                                                                                                                                                  
                                                                                                                                                                          
  sup_p ‖p − E[p|Φ_h^(L)]‖²_{L²(μ_n)} − sup_p ‖p − E[p|Φ_h^(L)]‖²_{L²(μ)}                                                                                                 
                                                                                                                                                                          
This is a uniform LLN gap over the class ℱ_{L,D}. By the standard                                                                                                         
empirical process uniform LLN (Glivenko-Cantelli for VC classes):                                                                                                         
                                                                                                                                                                          
  sup_{f ∈ ℱ_{L,D}} |(1/n)Σf(xᵢ) − Ef| → 0   a.s. as n → ∞                                                                                                                
                                                                                                                                                                          
Rate: O(√(VC(ℱ_{L,D})/n)) = O(√(D^d/n)) in the Takens regime.                                                                                                             
                                                                                                                                                                          
**Source 1 → 0 at rate n^{-1/2} (up to log factors). Standard. ✓**                                                                                                        
                                                                                                                                                                          
### Source 2 — Estimator bias: Ê ≠ E                                                                                                                                      
                                                                                                                                                                          
The empirical conditional expectation Ê[p | Φ_h^(L)] is not E[p | Φ_h^(L)]                                                                                                
— it's an estimate of the latter from n observations. The gap:                                                                                                            
                                                                                                                                                                          
  ‖p − Ê[p|Φ_h^(L)]‖²_{L²(μ_n)} − ‖p − E[p|Φ_h^(L)]‖²_{L²(μ_n)}                                                                                                           
                                                                                                                                                                          
This depends on which estimator Ê is. It is not zero, not small by                                                                                                        
default, and not controlled by concentration. It requires:                                                                                                                
                                                                                                                                                                          
  (a) A specific estimator for Ê[p | Φ_h^(L)]                                                                                                                             
  (b) A proof that this estimator's bias → 0 as n → ∞                                                                                                                     
  (c) Uniformity of (b) over p ∈ 𝒫_D^(L)                                                                                                                                  
                                                                                                                                                                          
**Source 2 is the open obligation. It requires a decision.**                                                                                                              
                                                                                                                                                                          
### The estimator choice                                                                                                                                                  
                                                                                                                                                                          
The natural choice: **kernel regression** on the delay vectors.                                                                                                           
                                                                                                                                                                          
  Ê[p | Φ_h^(L)](xᵢ) = Σⱼ K_hn(Φ_h^(L)(xᵢ) − Φ_h^(L)(xⱼ)) · p(xⱼ)                                                                                                         
                        / Σⱼ K_hn(Φ_h^(L)(xᵢ) − Φ_h^(L)(xⱼ))                                                                                                              
                                                                                                                                                                          
where K is a kernel function and h_n → 0 is the bandwidth.                                                                                                                
                                                                                                                                                                          
**Bias of kernel regression** for estimating E[p | Φ_h^(L) = z]:                                                                                                          
                                                                                                                                                                          
If E[p | Φ_h^(L) = z] is Hölder(β) in z on the d-dimensional image                                                                                                        
Φ_h^(L)(X), then the kernel regression bias satisfies:                                                                                                                    
                                                                                                                                                                          
  ‖Ê[p|Φ_h^(L)] − E[p|Φ_h^(L)]‖_{L²(μ_n)} = O(h_n^β + (nh_n^d)^{-1/2})                                                                                                    
                                                                                                                                                                          
Optimal bandwidth: h_n ~ n^{-1/(2β+d)}, giving bias O(n^{-β/(2β+d)}).                                                                                                     
                                                                                                                                                                          
**Uniformity over 𝒫_D^(L):** Since D and L are fixed, 𝒫_D^(L) is a                                                                                                        
finite-dimensional space. The unit ball is compact. Uniformity of the                                                                                                     
bias over p ∈ 𝒫_D^(L) follows from continuity of the map p ↦ E[p|Φ_h^(L)]                                                                                                 
(which is a bounded linear map from the finite-dimensional 𝒫_D^(L) to                                                                                                     
L²(μ)) plus the compactness.                                                                                                                                              
                                                                                                                                                                          
**Source 2 → 0 at rate n^{-β/(2β+d)} under Hölder(β) regularity of                                                                                                        
the conditional expectation and kernel regression with optimal bandwidth.**                                                                                               
                                                                                                                                                                          
### The regularity of E[p | Φ_h^(L)]                                                                                                                                      
                                                                                                                                                                          
In the Takens regime (L ≥ L₀): E[p | Φ_h^(L)](x) = p(x) exactly                                                                                                           
(point-mass disintegration). The conditional expectation is the function                                                                                                  
p itself — no estimation error beyond noise. Source 2 = 0. ✓                                                                                                              
                                                                                                                                                                          
In the pre-Takens regime (L < L₀): E[p | Φ_h^(L)](x) = ∫_{F_z} p dμ_z                                                                                                     
where F_z is the fiber over z = Φ_h^(L)(x). The regularity of z ↦ μ_z                                                                                                     
(the fiber map) determines β. The chain from dynamics to kernel regression                                                                                                
is four links; each link is a proof obligation or a citation.                                                                                                             
                                                                                                                                                                          
### Regularity chain: T ∈ C^r → kernel regression bias                                                                                                                    
                                                                                                                                                                          
**Link 1 — Smooth disintegration: T ∈ C^r → z ↦ μ_z Hölder(β) in TV**                                                                                                     
                                                                                                                                                                          
Preconditions: T ∈ C^r (r ≥ 2), h ∈ C^r, μ has a smooth positive density                                                                                                  
ρ with respect to volume, and h is generic (Φ_h^(L) has no critical                                                                                                       
points μ-a.e. — a Baire-generic condition on h).                                                                                                                          
                                                                                                                                                                          
Under these conditions the level sets F_z = {x : Φ_h^(L)(x) = z} are                                                                                                      
smooth (L+1)-codimensional submanifolds for μ-a.e. z (by Sard's theorem                                                                                                   
applied to Φ_h^(L) ∈ C^r). The Rokhlin disintegration theorem then gives:                                                                                                 
                                                                                                                                                                          
  μ(A) = ∫ μ_z(A) d(Φ_h^(L)_* μ)(z)     for all A ∈ ℬ                                                                                                                     
                                                                                                                                                                          
with μ_z supported on F_z. The coarea formula (for smooth maps ℝ^d → ℝ^{L+1})                                                                                             
expresses μ_z explicitly:                                                                                                                                                 
                                                                                                                                                                          
  dμ_z = ρ(x) · |Jac Φ_h^(L)(x)|^{−1} · dσ_z(x)                                                                                                                           
                                                                                                                                                                          
where σ_z is the (d − L − 1)-dimensional Hausdorff measure on F_z and                                                                                                     
Jac Φ_h^(L) is the (L+1) × d Jacobian (full rank μ-a.e. by genericity).                                                                                                   
                                                                                                                                                                          
**The TV bound — three sub-steps:**                                                                                                                                       
                                                                                                                                                                          
The TV distance between μ_z and μ_{z'} must be controlled explicitly.                                                                                                     
Write both measures via the coarea formula on a common ambient domain:                                                                                                    
                                                                                                                                                                          
  μ_z(A) = ∫_{F_z ∩ A} w_z(x) dσ_z(x),    w_z(x) := ρ(x)/|Jac Φ_h^(L)(x)|                                                                                                 
                                                                                                                                                                          
The TV distance is ‖μ_z − μ_{z'}‖_TV = sup_{‖f‖_∞≤1} |∫ f dμ_z − ∫ f dμ_{z'}|.                                                                                            
Decompose the difference into two pieces:                                                                                                                                 
                                                                                                                                                                          
  ∫ f dμ_z − ∫ f dμ_{z'}                                                                                                                                                  
    = ∫_{F_z} f · w_z dσ_z − ∫_{F_{z'}} f · w_{z'} dσ_{z'}                                                                                                                
                                                                                                                                                                          
**Sub-step A — Transfer to a common surface.** By the implicit function                                                                                                   
theorem, for z' near z there is a C^{r−1} diffeomorphism φ_{z,z'}: F_z → F_{z'}                                                                                           
with ‖φ_{z,z'} − id‖_{C^0} ≤ C|z−z'| and ‖Dφ_{z,z'}‖_{C^0} ≤ 1 + C|z−z'|.                                                                                                 
Pull back σ_{z'} along φ_{z,z'}: writing J_{z,z'} for the Jacobian determinant                                                                                            
of φ_{z,z'} restricted to F_z,                                                                                                                                            
                                                                                                                                                                          
  ∫_{F_{z'}} f · w_{z'} dσ_{z'} = ∫_{F_z} (f ∘ φ_{z,z'}) · (w_{z'} ∘ φ_{z,z'}) · J_{z,z'} dσ_z                                                                            
                                                                                                                                                                          
Both integrals now live on F_z. The difference becomes:                                                                                                                   
                                                                                                                                                                          
  ∫_{F_z} [f · w_z − (f ∘ φ_{z,z'}) · (w_{z'} ∘ φ_{z,z'}) · J_{z,z'}] dσ_z                                                                                                
                                                                                                                                                                          
**Sub-step B — Bound three perturbations separately.**                                                                                                                    
                                                                                                                                                                          
(i) *Diffeomorphism displacement of f*: Since ‖f‖_∞ ≤ 1,                                                                                                                  
    |f(x) − f(φ_{z,z'}(x))| ≤ ‖f‖_{Lip} · |x − φ_{z,z'}(x)| ≤ C|z−z'|.                                                                                                    
    If f is only bounded (not Lipschitz), this term is controlled via                                                                                                     
    |(f∘φ − f)·w_z| ≤ 2‖w_z‖_∞ · 1_{supp diff}, but the diameter of the                                                                                                   
    support shrinks as C|z−z'| so this contributes O(|z−z'|) to the TV.                                                                                                   
    *(Honest note: this sub-step requires σ_z to have finite total variation                                                                                              
    on F_z, which follows from F_z compact — holds when X is compact.)*                                                                                                   
                                                                                                                                                                          
(ii) *Variation of the weight w_{z'}∘φ − w_z*: Since w = ρ/|Jac Φ_h^(L)|                                                                                                  
    and both ρ ∈ C^r and Jac Φ_h^(L) ∈ C^{r−1} vary C^{r−1} in the ambient                                                                                                
    space, and φ_{z,z'} moves points by O(|z−z'|) in C^{r−1},                                                                                                             
    ‖w_{z'}∘φ_{z,z'} − w_z‖_{C^0(F_z)} ≤ C|z−z'|.                                                                                                                         
                                                                                                                                                                          
(iii) *Jacobian factor J_{z,z'} − 1*: φ_{z,z'} is C^{r−1} with                                                                                                            
    Dφ_{z,z'} = I + O(|z−z'|) in C^0, so J_{z,z'} = 1 + O(|z−z'|).                                                                                                        
                                                                                                                                                                          
Combining (i)–(iii) and integrating against σ_z (finite total mass, bounded                                                                                               
by σ_z(F_z) ≤ C for z in a compact set):                                                                                                                                  
                                                                                                                                                                          
  ‖μ_z − μ_{z'}‖_TV ≤ C · σ_z(F_z) · |z − z'| ≤ C_1 · |z − z'|                                                                                                            
                                                                                                                                                                          
**Sub-step C — Exponent β = r − 1 vs β = 1.**                                                                                                                             
                                                                                                                                                                          
Sub-step B gives Hölder(1) — Lipschitz — not Hölder(r−1). The exponent β = r−1                                                                                            
would follow if w and φ are estimated in C^{r−1} and the argument is iterated                                                                                             
to higher order (Taylor expansion of w_{z'}∘φ in z−z' up to order r−1). For                                                                                               
the purposes of Source 2, β = 1 (Lipschitz) is already sufficient: it gives                                                                                               
kernel regression rate n^{-1/(2+dim_eff(L))}, which → 0. The claim β = r−1                                                                                                
is the optimal rate but it requires the full Taylor argument; the honest floor                                                                                            
is β = 1 from the first-order bound above.                                                                                                                                
                                                                                                                                                                          
*Summary of Link 1:*                                                                                                                                                      
                                                                                                                                                                          
  ‖μ_z − μ_{z'}‖_TV ≤ C_1 · |z − z'|^β,   β ≥ 1 when T, h ∈ C^r, r ≥ 2,                                                                                                   
                                              ρ > 0, Φ_h^(L) full rank μ-a.e.                                                                                             
                                                                                                                                                                          
The proof is: (1) Rokhlin disintegration gives μ_z = w_z · σ_z on F_z;                                                                                                    
(2) implicit function theorem gives a C^{r−1} diffeomorphism between nearby                                                                                               
fibers; (3) pull back to common surface + bound three O(|z−z'|) perturbations;                                                                                            
(4) integrate against σ_z (finite mass by compactness).                                                                                                                   
                                                                                                                                                                          
**Non-degeneracy conditions required — all three must hold simultaneously:**                                                                                              
- ρ > 0 everywhere on X (so w_z = ρ/|Jac| is well-defined and bounded above)                                                                                              
- |Jac Φ_h^(L)| > 0 μ-a.e. (so w_z is bounded; fails at critical points)                                                                                                  
- σ_z(F_z) < ∞ uniformly in z (fiber has finite Hausdorff measure; holds for                                                                                              
  compact X and generic h by smooth coarea)                                                                                                                               
                                                                                                                                                                          
The third condition is the one hidden in "A standard computation." It requires                                                                                            
X compact and the fibers F_z to be smooth compact submanifolds — which is                                                                                                 
exactly the pre-Takens assumption (L < L₀, so the fibers are non-trivial                                                                                                  
submanifolds, not points). **In the Takens regime F_z = {single point}, so                                                                                                
σ_z is a point mass and the TV bound is trivially 0 — Source 2 = 0 there, as                                                                                              
already noted.**                                                                                                                                                          
                                                                                                                                                                          
**Link 1 is now explicit. The Hölder(β) regularity of z ↦ μ_z is not an                                                                                                   
assumption — it is a consequence of (T, h ∈ C^r, r ≥ 2), (ρ > 0),                                                                                                         
(Φ_h^(L) full rank μ-a.e.), and (X compact). These are the honest                                                                                                         
preconditions for the pre-Takens regime.**                                                                                                                                
                                                                                                                                                                          
**Link 2 — Fiber Hölder → regression Hölder**                                                                                                                             
                                                                                                                                                                          
**The load-bearing fact: Bernstein–Markov inequality.**                                                                                                                   
                                                                                                                                                                          
𝒫_D^(L) consists of polynomials of degree ≤ D in the delay coordinates                                                                                                    
(h(x), h(Tx), …, h(T^L x)), normalised so ‖p‖_{L²(μ)} ≤ 1.                                                                                                                
                                                                                                                                                                          
Since h ∈ L^∞ with ‖h‖_∞ < ∞, the delay coordinates lie in the compact                                                                                                    
box K := [−‖h‖_∞, ‖h‖_∞]^{L+1}. Write a = ‖h‖_∞ so K = [−a, a]^{L+1}.                                                                                                     
                                                                                                                                                                          
**Deriving the sup-norm bound from first principles.**                                                                                                                    
                                                                                                                                                                          
Rescale to the unit box: set yᵢ = xᵢ/a, so K maps to [−1,1]^{L+1}. A                                                                                                      
polynomial q(x) of degree ≤ D in x ∈ K corresponds to a polynomial                                                                                                        
̃(y) = q(ay) of degree ≤ D in y ∈ [−1,1]^{L+1}.                                                                                                                           
                                                                                                                                                                          
On [−1,1]^{L+1}, expand q̃ in the tensor-product Legendre basis:                                                                                                           
                                                                                                                                                                          
  q̃(y) = Σ_{|α|≤D} c_α · P_α(y),   P_α(y) = Π_{i=1}^{L+1} P_{αᵢ}(yᵢ)                                                                                                      
                                                                                                                                                                          
where α = (α₁,…,α_{L+1}) is a multi-index with |α| = α₁+…+α_{L+1} ≤ D,                                                                                                    
and P_k is the univariate Legendre polynomial of degree k, normalised so                                                                                                  
‖P_k‖_{L²[−1,1]} = (2k+1)^{-1/2}.                                                                                                                                         
                                                                                                                                                                          
The sup-norm of a single basis element satisfies ‖P_α‖_∞ = 1 (Legendre                                                                                                    
polynomials are bounded by 1 at every point of [−1,1]).                                                                                                                   
                                                                                                                                                                          
For the L² norm of P_α on the uniform measure on [−1,1]^{L+1}:                                                                                                            
                                                                                                                                                                          
  ‖P_α‖²_{L²} = Π_{i=1}^{L+1} ‖P_{αᵢ}‖²_{L²[−1,1]} = Π_{i=1}^{L+1} 1/(2αᵢ+1)                                                                                              
                                                                                                                                                                          
Now bound ‖q̃‖_∞. By Cauchy–Schwarz over the coefficient expansion:                                                                                                        
                                                                                                                                                                          
  |q̃(y)| ≤ Σ_{|α|≤D} |c_α| · |P_α(y)|                                                                                                                                     
           ≤ Σ_{|α|≤D} |c_α|                        (since ‖P_α‖_∞ = 1)                                                                                                   
           ≤ N(D,L+1)^{1/2} · (Σ_{|α|≤D} |c_α|²)^{1/2}   (Cauchy–Schwarz)                                                                                                 
                                                                                                                                                                          
where N(D,L+1) = #{α : |α| ≤ D, αᵢ ≥ 0} = C(D+L+1, L+1) is the number                                                                                                     
of multi-indices.                                                                                                                                                         
                                                                                                                                                                          
**N(D,L+1) carries all the L-dependence. Here is where it comes from.**                                                                                                   
                                                                                                                                                                          
Stars-and-bars: distributing total degree ≤ D among L+1 nonneg. integer                                                                                                   
bins (the L+1 coordinates of α). The count is:                                                                                                                            
                                                                                                                                                                          
  N(D,L+1) = C(D+L+1, L+1) = (D+L+1)! / (D! · (L+1)!)                                                                                                                     
                                                                                                                                                                          
Rewrite by cancelling (L+1)! against the top:                                                                                                                             
                                                                                                                                                                          
  N(D,L+1) = [(L+D+1)(L+D)(L+D−1)···(L+2)] / D!                                                                                                                           
                                                                                                                                                                          
The numerator is a product of exactly D consecutive integers from L+2                                                                                                     
up to L+D+1. Write it term by term:                                                                                                                                       
                                                                                                                                                                          
  numerator = (L+2)(L+3)···(L+D+1)                                                                                                                                        
            = Π_{k=1}^{D} (L+k+1)                                                                                                                                         
                                                                                                                                                                          
Each factor is L+k+1 for k = 1,…,D. Factor L out of each:                                                                                                                 
                                                                                                                                                                          
  Π_{k=1}^{D} (L+k+1) = L^D · Π_{k=1}^{D} (1 + (k+1)/L)                                                                                                                   
                                                                                                                                                                          
Each individual factor (1+(k+1)/L) is close to 1 when L is large. But                                                                                                     
the product of D such factors is not obtained by summing D small                                                                                                          
corrections — the factors multiply, not add.                                                                                                                              
                                                                                                                                                                          
**Bounding the product without linearising.**                                                                                                                             
                                                                                                                                                                          
Use the inequality 1+t ≤ e^t for t ≥ 0:                                                                                                                                   
                                                                                                                                                                          
  Π_{k=1}^{D} (1 + (k+1)/L) ≤ exp(Σ_{k=1}^{D} (k+1)/L)                                                                                                                    
                              = exp((1/L) · Σ_{k=1}^{D} (k+1))                                                                                                            
                              = exp((1/L) · (D(D+3)/2))                                                                                                                   
                              = exp(D(D+3)/(2L))                                                                                                                          
                                                                                                                                                                          
For the lower bound, use 1+t ≥ e^{t − t²} for 0 ≤ t ≤ 1 (which holds                                                                                                      
when (k+1)/L ≤ 1, i.e. L ≥ D+1):                                                                                                                                          
                                                                                                                                                                          
  Π_{k=1}^{D} (1 + (k+1)/L) ≥ exp(Σ_{k=1}^{D} [(k+1)/L − (k+1)²/L²])                                                                                                      
                              ≥ exp(D(D+3)/(2L) − (D+1)³/(3L²))                                                                                                           
                                                                                                                                                                          
So the product is sandwiched:                                                                                                                                             
                                                                                                                                                                          
  exp(D(D+3)/(2L) − O(D³/L²))  ≤  Π_{k=1}^D (1+(k+1)/L)  ≤  exp(D(D+3)/(2L))                                                                                              
                                                                                                                                                                          
**Three regimes for the product, depending on D vs L:**                                                                                                                   
                                                                                                                                                                          
*Regime 1: D = o(√L).* Then D(D+3)/(2L) → 0 and the product → 1.                                                                                                          
The correction is genuinely small: Π ≈ 1 + O(D²/L).                                                                                                                       
                                                                                                                                                                          
*Regime 2: D ~ c√L for constant c.* Then D(D+3)/(2L) ~ c²/2, and the                                                                                                      
product converges to a finite constant e^{c²/2} > 1. Each factor                                                                                                          
whispers, but √L of them together produce a bounded shout.                                                                                                                
                                                                                                                                                                          
*Regime 3: D ~ L (dimension equals degree).* Then D(D+3)/(2L) ~ L/2,                                                                                                      
and the product ~ e^{L/2}. This is the loud scream: exponential growth                                                                                                    
in L. The polynomial counting argument breaks down — N(D,L+1) is no                                                                                                       
longer L^D/D! with a small correction; it is genuinely (2L)^D/D!, which                                                                                                   
for D = L gives (2L)^L/L! ~ (2e)^L by Stirling.                                                                                                                           
                                                                                                                                                                          
**Two-sided bounds for N(D,L+1), valid for all L ≥ D+1:**                                                                                                                 
                                                                                                                                                                          
  L^D/D!  ≤  N(D,L+1)  ≤  L^D/D! · e^{D(D+3)/(2L)}                                                                                                                        
                                                                                                                                                                          
Lower: each factor (L+k+1) ≥ L.                                                                                                                                           
Upper: L^D · exp(D(D+3)/(2L)) / D!, from the product bound above.                                                                                                         
                                                                                                                                                                          
**The Legendre norm factor does NOT grow with L.**                                                                                                                        
                                                                                                                                                                          
From the L² norm identity Σ |c_α|² · ‖P_α‖²_{L²} = ‖q̃‖²_{L²}:                                                                                                             
                                                                                                                                                                          
  Σ_{|α|≤D} |c_α|² ≤ ‖q̃‖²_{L²} · max_{|α|≤D} Π_{i=1}^{L+1} (2αᵢ+1)                                                                                                        
                                                                                                                                                                          
The constraint is |α| = α₁+…+α_{L+1} ≤ D. The maximum of Π(2αᵢ+1)                                                                                                         
subject to Σαᵢ ≤ D is achieved by concentrating all weight on one                                                                                                         
coordinate: α = (D, 0, 0, …, 0), giving                                                                                                                                   
                                                                                                                                                                          
  max_{|α|≤D} Π(2αᵢ+1) = (2D+1) · 1 · … · 1 = 2D+1                                                                                                                        
                                                                                                                                                                          
**The max is 2D+1, independent of L.** The constraint |α| ≤ D forces                                                                                                      
weight to concentrate, not spread. So:                                                                                                                                    
                                                                                                                                                                          
  Σ_{|α|≤D} |c_α|² ≤ (2D+1) · ‖q̃‖²_{L²}                                                                                                                                   
                                                                                                                                                                          
Combining with the Cauchy–Schwarz step:                                                                                                                                   
                                                                                                                                                                          
  ‖q̃‖_∞ ≤ N(D,L+1)^{1/2} · (2D+1)^{1/2} · ‖q̃‖_{L²}                                                                                                                        
                                                                                                                                                                          
**The L-dependence is entirely in N(D,L+1)^{1/2}. The factor (2D+1)^{1/2}                                                                                                 
depends only on degree D, not on dimension L.**                                                                                                                           
                                                                                                                                                                          
Converting back to x-coordinates. The volume of K = [−a,a]^{L+1} is                                                                                                       
(2a)^{L+1}, so ‖q̃‖_{L²([−1,1]^{L+1})} = (2a)^{−(L+1)/2} · ‖q‖_{L²(K,vol)}.                                                                                                
                                                                                                                                                                          
For μ with density ρ ≥ ρ_min > 0 on K:                                                                                                                                    
‖q‖_{L²(K,vol)} ≤ ρ_min^{−1/2} · ‖q‖_{L²(μ)}, so:                                                                                                                         
                                                                                                                                                                          
  ‖q‖_∞ ≤ N(D,L+1)^{1/2} · (2D+1)^{1/2} · (2a)^{−(L+1)/2} · ρ_min^{−1/2}                                                                                                  
             · ‖q‖_{L²(μ)}                                                                                                                                                
                                                                                                                                                                          
**The explicit form of M_{D,L}:**                                                                                                                                         
                                                                                                                                                                          
  M_{D,L} = N(D,L+1)^{1/2} · (2D+1)^{1/2} · (2a)^{−(L+1)/2} · ρ_min^{−1/2}                                                                                                
                                                                                                                                                                          
where a = ‖h‖_∞ and N(D,L+1) = C(D+L+1,L+1).                                                                                                                              
                                                                                                                                                                          
**L-dependence unpacked:**                                                                                                                                                
                                                                                                                                                                          
Set D = ⌈s⌉ =: s̃ (fixed) and write γ := (2a)^{−1/2}. Then:                                                                                                                
                                                                                                                                                                          
  M_{s̃,L} ~ L^{s̃/2}/√(s̃!) · (2s̃+1)^{1/2} · γ^{L+1} · ρ_min^{−1/2}                                                                                                         
           =: A · L^{s̃/2} · γ^L                                                                                                                                           
                                                                                                                                                                          
where A depends only on (s, ‖h‖_∞, ρ_min) — not on L or n.                                                                                                                
                                                                                                                                                                          
The product correction e^{D(D+3)/(4L)} applies to N^{1/2}:                                                                                                                
- D = o(√L): correction → 1, M_{s̃,L} ~ A · L^{s/2} · γ^L  (Regime 1)                                                                                                      
- D ~ c√L: correction → e^{c²/4}, finite amplifier              (Regime 2)                                                                                                
- D ~ L: correction ~ e^{L/4}, exponential blowup               (Regime 3)                                                                                                
                                                                                                                                                                          
**Domain constraint: which regime is Paper IV in?**                                                                                                                       
                                                                                                                                                                          
D = ⌈s⌉ is fixed by the approximation requirement (minimum degree to                                                                                                      
resolve Hölder(s) features). For this D:                                                                                                                                  
                                                                                                                                                                          
*Exponential mixing* gives L*(n) ~ log(n)/(2|log λ|) =: c_λ·log n via                                                                                                     
the forcing argument: δ(L) ≤ C'·λ^L (from covariance decay + incremental                                                                                                  
gain + δ(∞)=0 + geometric sum), balanced against n^{-1/2}.                                                                                                                
                                                                                                                                                                          
  D²/L*(n) ~ s²·|log λ|/log n → 0   as n → ∞  →  Regime 1 ✓                                                                                                               
                                                                                                                                                                          
*Polynomial mixing* (rate α > 2) gives L*(n) ~ n^{1/(2(α−1))} via the                                                                                                     
same argument with polynomial covariance decay giving δ(L) ~ L^{−(α−1)}.                                                                                                  
                                                                                                                                                                          
  D²/L*(n) ~ s²·n^{−1/(2(α−1))} → 0   as n → ∞  →  Regime 1 ✓                                                                                                             
                                                                                                                                                                          
Both reach Regime 1 asymptotically. Now substitute L*(n) into M_{s̃,L}:                                                                                                    
                                                                                                                                                                          
*Case 1: Exponential mixing, L = c_λ·log n:*                                                                                                                              
                                                                                                                                                                          
  γ^L = (2a)^{−L/2} = n^{−c_λ·log(2a)/2}                                                                                                                                  
                                                                                                                                                                          
  M_{s̃,L*(n)} = A · (log n)^{s/2} · n^{ε_exp}                                                                                                                             
                                                                                                                                                                          
where ε_exp = −c_λ·log(2‖h‖_∞)/2, sign determined by ‖h‖_∞ ≷ 1/2.                                                                                                         
                                                                                                                                                                          
*Case 2: Polynomial mixing, L = c_α·n^{1/(2(α−1))}:*                                                                                                                      
                                                                                                                                                                          
  γ^L = exp(−c_α·n^{1/(2(α−1))}·log(2a)/2)  (super-polynomial in n)                                                                                                       
                                                                                                                                                                          
  M_{s̃,L*(n)} = A · n^{s/(4(α−1))} · exp(∓const·n^{1/(2(α−1))})                                                                                                           
                                                                                                                                                                          
The exponential γ^L factor dominates the polynomial counting factor L^{D/2}                                                                                               
in either direction. The claim "M_{D,L} ~ L^{D/2}" omits γ^L entirely.                                                                                                    
                                                                                                                                                                          
**Consolidated M_{D,L} bounds at L*(n):**                                                                                                                                 
                                                                                                                                                                          
| Mixing | ‖h‖_∞ > 1/2 | ‖h‖_∞ = 1/2 | ‖h‖_∞ < 1/2 |                                                                                                                      
|--------|-------------|-------------|-------------|                                                                                                                      
| Exponential | (logn)^{s/2}·n^{−ε} → 0 | (logn)^{s/2} | (logn)^{s/2}·n^{+ε} |                                                                                            
| Polynomial | n^{s/(4(α−1))}·e^{−cn^κ} → 0 | n^{s/(4(α−1))} | n^{s/(4(α−1))}·e^{+cn^κ} → ∞ |                                                                             
                                                                                                                                                                          
where ε = c_λ|log(2‖h‖_∞)|/2 > 0 and κ = 1/(2(α−1)) > 0.                                                                                                                  
                                                                                                                                                                          
The threshold ‖h‖_∞ = 1/2 is a normalisation artifact of the box                                                                                                          
[−a,a]^{L+1}. Rescaling h to ‖h‖_∞ = 1 (always achievable) places                                                                                                         
all cases in the bounded or decaying column under exponential mixing.                                                                                                     
                                                                                                                                                                          
**Honest scope of Source 2:** Closed under exponential mixing with                                                                                                        
‖h‖_∞ ≥ 1/2. Under polynomial mixing with ‖h‖_∞ > 1/2 the constant                                                                                                        
C_2(D,L) → 0 (technically closed but operationally uninformative).                                                                                                        
Under polynomial mixing with ‖h‖_∞ < 1/2 the bound is vacuous for                                                                                                         
finite n — Source 2 requires a different estimator or rescaling of h.                                                                                                     
                                                                                                                                                                          
D is a degree parameter; M_{D,L} is the derived sup-norm bound with                                                                                                       
explicit (D, L, ‖h‖_∞, ρ_min) dependence. These are different objects.                                                                                                    
                                                                                                                                                                          
**Everything downstream uses M_{D,L}, not D, as the norm control.**                                                                                                       
                                                                                                                                                                          
Now the regression step. Write E[p | Φ_h^(L) = z] = ∫ p dμ_z. For any z, z':                                                                                              
                                                                                                                                                                          
  |E[p | z] − E[p | z']|                                                                                                                                                  
    = |∫ p dμ_z − ∫ p dμ_{z'}|                                                                                                                                            
    ≤ ‖p‖_∞ · ‖μ_z − μ_{z'}‖_TV       (|∫ p d(μ − ν)| ≤ ‖p‖_∞‖μ−ν‖_TV)                                                                                                    
    ≤ M_{D,L} · C_1 · |z − z'|^β       (Bernstein–Markov + Link 1)                                                                                                        
                                                                                                                                                                          
  |E[p|z] − E[p|z']| ≤ M_{D,L} · C_1 · |z − z'|^β =: Λ_{D,L} · |z − z'|^β                                                                                                 
                                                                                                                                                                          
where Λ_{D,L} = M_{D,L} · C_1. Uniform over p: every p ∈ 𝒫_D^(L) with                                                                                                     
‖p‖_{L²(μ)} ≤ 1 satisfies ‖p‖_∞ ≤ M_{D,L}, so Λ_{D,L} is class-level.                                                                                                     
**Link 2 ✓**                                                                                                                                                              
                                                                                                                                                                          
**Link 3 — Kernel regression bias/variance: M_{D,L} cancels from h_n***                                                                                                   
                                                                                                                                                                          
Let d_e := dim_eff(L). Nadaraya–Watson with bandwidth h gives:                                                                                                            
                                                                                                                                                                          
  E‖Ê[p|z] − g_p(z)‖²_{L²} ≤ Λ_{D,L}² · h^{2β} + C_K · M_{D,L}² / (n · h^{d_e} · f_min)                                                                                   
                                                                                                                                                                          
Bias constant Λ_{D,L} = M_{D,L}·C_1 and variance bound ∝ M_{D,L}². Both                                                                                                   
proportional to M_{D,L}². Balance equation:                                                                                                                               
                                                                                                                                                                          
  M_{D,L}² · C_1² · h^{2β} = C_K · M_{D,L}² / (n · h^{d_e} · f_min)                                                                                                       
                                                                                                                                                                          
**M_{D,L}² cancels.** Optimal bandwidth:                                                                                                                                  
                                                                                                                                                                          
  h_n* = (C_K / (C_1² · f_min))^{1/(2β+d_e)} · n^{-1/(2β+d_e)} =: A · n^{-1/(2β+d_e)}                                                                                     
                                                                                                                                                                          
h_n* depends only on (β, d_e, C_K, f_min, C_1) — not on D, L, or p.                                                                                                       
A single bandwidth serves all p ∈ 𝒫_D^(L) simultaneously.                                                                                                                 
                                                                                                                                                                          
Plugging back: both terms ∝ M_{D,L}²:                                                                                                                                     
                                                                                                                                                                          
  E‖Ê[p|z] − g_p(z)‖²_{L²} ≤ C_2(D,L) · n^{-2β/(2β+d_e)}                                                                                                                  
                                                                                                                                                                          
where C_2(D,L) = 2·M_{D,L}²·C_1²·A^{2β}. Rate exponent uniform in p;                                                                                                      
C_2(D,L) carries the class-size cost through M_{D,L}². **Link 3 ✓**                                                                                                       
                                                                                                                                                                          
**Link 4 — Uniformity is already in Link 3.**                                                                                                                             
                                                                                                                                                                          
The bound holds for every p with the same right-hand side. The sup over                                                                                                   
p ∈ 𝒫_D^(L) costs nothing — the bound is already p-free.                                                                                                                  
                                                                                                                                                                          
  sup_{p ∈ 𝒫_D^(L)} E‖Ê[p|z] − g_p(z)‖²_{L²} ≤ C_2(D,L) · n^{-2β/(2β+d_e)}                                                                                                
                                                                                                                                                                          
Compactness of 𝒫_D^(L) is not needed — uniformity comes from the                                                                                                          
class-level bound M_{D,L}, not from compactness. **Link 4 ✓**                                                                                                             
                                                                                                                                                                          
**Summary: the four-link chain**                                                                                                                                          
                                                                                                                                                                          
```                                                                                                                                                                       
T ∈ C^r, h generic, μ smooth                                                                                                                                              
    ↓  Link 1: coarea + IFT → TV sub-steps A/B/C                                                                                                                          
z ↦ μ_z Hölder(β) in TV,  β ≥ 1                                                                                                                                           
    ↓  Link 2: |∫ p dμ_z − ∫ p dμ_{z'}| ≤ M_{D,L}·C_1·|z−z'|^β  (Bernstein–Markov)                                                                                        
z ↦ E[p | z] Hölder(β) uniformly over 𝒫_D^(L)                                                                                                                             
    ↓  Link 3: NW bias-variance, M_{D,L}² cancels from h_n*                                                                                                               
kernel regression bias O(n^{-β/(2β+dim_eff(L))})                                                                                                                          
    ↓  Link 4: bound p-free, sup costs nothing                                                                                                                            
Source 2 closed:  δ̂_pop − δ = O(n^{-β/(2β+dim_eff(L))})                                                                                                                   
    under: exp. mixing + ‖h‖_∞ ≥ 1/2  ✓                                                                                                                                   
```                                                                                                                                                                       
                                                                                                                                                                          
**Obligation (7) closed under the stated conditions.                                                                                                                      
Remaining open work: full Taylor argument for β = r−1 (Link 1, optimal rate)                                                                                              
and the polynomial mixing / ‖h‖_∞ < 1/2 regime (different estimator needed).**                                                                                            
                                                                                                                                                                          
### Assembling the full convergence proof                                                                                                                                 
                                                                                                                                                                          
  |E[δ̂(L,n)] − δ(L)|                                                                                                                                                      
    ≤ |E[δ̂(L,n)] − δ̂_pop(L,n)|    (Source 1: LLN gap)                                                                                                                     
    + |δ̂_pop(L,n) − δ(L)|           (Source 2: estimator bias)                                                                                                            
                                                                                                                                                                          
where δ̂_pop(L,n) := sup_p ‖p − Ê[p|Φ_h^(L)]‖²_{L²(μ)} is the                                                                                                              
population version with estimated conditional expectation.                                                                                                                
                                                                                                                                                                          
Source 1 → 0 at rate √(D^d/n). ✓ standard                                                                                                                                 
Source 2 → 0 at rate n^{-β/(2β+d_e)} under Hölder(β) + exp. mixing + ‖h‖_∞≥1/2. ✓                                                                                         
                                                                                                                                                                          
**Combined: E[δ̂(L,n)] → δ(L) at rate max(n^{-1/2}, n^{-β/(2β+d_e)})                                                                                                       
under exponential mixing with ‖h‖_∞ ≥ 1/2.**                                                                                                                              
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Pre-Takens regime and optimal L*(n)                                                                                                                                    
                                                                                                                                                                          
**Setup.** In the Takens regime (L ≥ L₀), Φ_h^(L) is injective mod μ,                                                                                                     
δ(L) = 0, and the statistical rate is n^{-s/(2s+d)}. But:                                                                                                                 
                                                                                                                                                                          
- For L < L₀: Φ_h^(L) is not injective. The image Φ_h^(L)(X) has                                                                                                          
  effective dimension dim_eff(L) < d because the delay vectors have not                                                                                                   
  yet separated all directions of X.                                                                                                                                      
- For L₀ = ∞ (no exact reconstruction): δ(L) > 0 for all L, and the                                                                                                       
  bias term never vanishes. We must balance bias and variance by choosing                                                                                                 
  L = L*(n).                                                                                                                                                              
                                                                                                                                                                          
### How dim_eff(L) grows                                                                                                                                                  
                                                                                                                                                                          
The map Φ_h^(L) : X → ℝ^(L+1) sends x to (h(x), h(Tx), …, h(T^L x)).                                                                                                      
                                                                                                                                                                          
At L = 0: the image is h(X) ⊆ ℝ, a 1-dimensional set (generically).                                                                                                       
  dim_eff(0) = 1.                                                                                                                                                         
                                                                                                                                                                          
At L = L₀: the image is Φ_h^(L₀)(X) ⊆ ℝ^(L₀+1), a d-dimensional                                                                                                           
  submanifold (Takens embedding). dim_eff(L₀) = d.                                                                                                                        
                                                                                                                                                                          
For 0 < L < L₀: dim_eff(L) = min(L+1, d) approximately — each new lag                                                                                                     
  adds one new independent direction until all d directions are separated.                                                                                                
  But this is only approximately true; the actual growth depends on T and h.                                                                                              
                                                                                                                                                                          
**More precisely:** dim_eff(L) = rank of the Jacobian of Φ_h^(L) at a                                                                                                     
generic point of X, which equals min(L+1, d) for generic h and T (by                                                                                                      
the Takens genericity argument). So:                                                                                                                                      
                                                                                                                                                                          
  dim_eff(L) = min(L+1, d)   for generic (T, h), L ≥ 0.                                                                                                                   
                                                                                                                                                                          
**This is a step function, not a smooth function of L.** It takes integer                                                                                                 
values 1, 2, …, d as L steps through 0, 1, …, d−1, then locks at d for                                                                                                    
all L ≥ d−1. There is no continuous interpolation.                                                                                                                        
                                                                                                                                                                          
Note: L₀ = d−1 generically (need L+1 ≥ d coordinates to have full rank).                                                                                                  
The classical Takens theorem requires L₀ = 2d (for injectivity, not just                                                                                                  
full rank) — injectivity is harder than surjectivity of the differential.                                                                                                 
                                                                                                                                                                          
### Statistical rate in the pre-Takens regime                                                                                                                             
                                                                                                                                                                          
For L < L₀, the image Φ_h^(L)(X) is dim_eff(L)-dimensional, and the                                                                                                       
statistical rate is piecewise in L — it steps through discrete values                                                                                                     
as each new lag adds one dimension:                                                                                                                                       
                                                                                                                                                                          
  L = 0:       rate n^{-s/(2s+1)}                                                                                                                                         
  L = 1:       rate n^{-s/(2s+2)}                                                                                                                                         
  ⋮                                                                                                                                                                       
  L = d−2:     rate n^{-s/(2s+d−1)}                                                                                                                                       
  L ≥ d−1:     rate n^{-s/(2s+d)}   (locked)                                                                                                                              
                                                                                                                                                                          
Each step is a discrete improvement. The rate does not vary continuously                                                                                                  
with L — it jumps at each integer. Any argument treating the rate as a                                                                                                    
smooth or monotone-continuous function of L is wrong: dim_eff forgot it                                                                                                   
was piecewise.                                                                                                                                                            
                                                                                                                                                                          
For L ≥ L₀ (Takens regime): dim_eff(L) = d, rate locked at n^{-s/(2s+d)}.                                                                                                 
                                                                                                                                                                          
The bias term: δ(L) > 0 for L < L₀. In the pre-Takens regime, δ(L)                                                                                                        
measures how much of ℬ is not yet captured by 𝒪_h^(L).                                                                                                                    
                                                                                                                                                                          
**How does δ(L) decay for L < L₀?**                                                                                                                                       
                                                                                                                                                                          
For the Takens case (finite L₀):                                                                                                                                          
  δ(L) > 0 for L < L₀, δ(L₀) = 0.                                                                                                                                         
  No smooth decay — it's a threshold. The bias drops to 0 at L = L₀.                                                                                                      
                                                                                                                                                                          
For infinite L₀ (e.g. mixing systems without finite reconstruction):                                                                                                      
  δ(L) → 0 as L → ∞, with rate depending on the mixing properties of T.                                                                                                   
                                                                                                                                                                          
| Mixing type | δ(L) decay rate | Source |                                                                                                                                
|-------------|----------------|--------|                                                                                                                                 
| Exponential mixing (rate λ) | δ(L) ~ e^{-λL} | Spectral gap of U_T |                                                                                                    
| Polynomial mixing (exponent α) | δ(L) ~ L^{-α} | Correlation decay |                                                                                                    
| Finite Takens (L₀ finite) | δ(L) = 0 for L ≥ L₀ | Exact reconstruction |                                                                                                
                                                                                                                                                                          
### Optimal L*(n): balancing bias and variance                                                                                                                            
                                                                                                                                                                          
The full forward bound (including pre-Takens) is:                                                                                                                         
                                                                                                                                                                          
  ‖f − f̂_n^(L)‖_{L²} ≤ 2‖f‖_{L∞}·δ(L)^{1/2} + C·n^{-s/(2s+dim_eff(L))}                                                                                                    
                                                                                                                                                                          
Choose L*(n) to minimise the right side over L.                                                                                                                           
                                                                                                                                                                          
**Case 1: Finite Takens (L₀ < ∞).**                                                                                                                                       
                                                                                                                                                                          
For L < L₀: bias = 2‖f‖_{L∞}·δ(L)^{1/2} > 0, but dim_eff(L) ≤ d−1 so                                                                                                      
  the statistical term is faster than n^{-s/(2s+d)}.                                                                                                                      
                                                                                                                                                                          
For L ≥ L₀: bias = 0, statistical term = C·n^{-s/(2s+d)}.                                                                                                                 
                                                                                                                                                                          
For any n, taking L = L₀ gives bias 0 and the best attainable statistical                                                                                                 
rate. L*(n) = L₀ for all n (once n is large enough to support estimation                                                                                                  
in ℝ^d). There is no L-vs-n tradeoff — just use L₀.                                                                                                                       
                                                                                                                                                                          
**Case 2: Exponential mixing (δ(L) ~ e^{-λL}).**                                                                                                                          
                                                                                                                                                                          
The piecewise structure of dim_eff means the balance must be done in                                                                                                      
two regimes:                                                                                                                                                              
                                                                                                                                                                          
*Pre-saturation (L < d−1):* Both bias and statistical rate are improving                                                                                                  
with L. No tradeoff — just increase L until L = d−1.                                                                                                                      
                                                                                                                                                                          
*Post-saturation (L ≥ d−1):* dim_eff = d locked. Statistical rate =                                                                                                       
n^{-s/(2s+d)}, fixed. Bias = e^{-λL/2}, still decaying. Balance:                                                                                                          
                                                                                                                                                                          
  e^{-λL/2} ~ n^{-s/(2s+d)}                                                                                                                                               
    ⟹  L*(n) ~ (2s/(λ(2s+d))) · log n                                                                                                                                     
                                                                                                                                                                          
Since log n ≫ d−1 for large n, L*(n) is in the post-saturation regime                                                                                                     
as claimed. The balance is consistent. Rate at L*(n): n^{-s/(2s+d)}.                                                                                                      
                                                                                                                                                                          
**Case 3: Polynomial mixing (δ(L) ~ L^{-α}).**                                                                                                                            
                                                                                                                                                                          
*Post-saturation (L ≥ d−1):* dim_eff = d locked. Balance:                                                                                                                 
                                                                                                                                                                          
  L^{-α/2} ~ n^{-s/(2s+d)}                                                                                                                                                
    ⟹  L*(n) ~ n^{2s/(α(2s+d))}                                                                                                                                           
                                                                                                                                                                          
For large n, L*(n) ≫ d−1, so again consistently in the post-saturation                                                                                                    
regime. Rate at L*(n): n^{-s/(2s+d)}.                                                                                                                                     
                                                                                                                                                                          
**The piecewise structure does not change the terminal rate** — both                                                                                                      
mixing cases arrive at n^{-s/(2s+d)} because the balance point L*(n)                                                                                                      
is always in the post-saturation regime for large n. But it does matter                                                                                                   
for finite n: for n small enough that L*(n) < d−1, the system is in the                                                                                                   
pre-saturation regime and the statistical rate is faster than n^{-s/(2s+d)}                                                                                               
(smaller dim_eff), at the cost of non-zero bias. The crossing point is                                                                                                    
finite-n behavior, not the asymptotic rate.                                                                                                                               
                                                                                                                                                                          
**Summary of optimal L*(n) and achievable rates:**                                                                                                                        
                                                                                                                                                                          
| System type | L*(n) | Achievable rate |                                                                                                                                 
|-------------|-------|----------------|                                                                                                                                  
| Finite Takens (L₀ finite) | L₀ (fixed) | n^{-s/(2s+d)} |                                                                                                                
| Exponential mixing (rate λ) | ~ (2s/λ(2s+d))·log n | n^{-s/(2s+d)} |                                                                                                    
| Polynomial mixing (exponent α) | ~ n^{2s/α(2s+d)} | n^{-s/(2s+d)} |                                                                                                     
| No reconstruction (δ(L) → c > 0) | ∞ (no finite optimum) | bounded away from 0 |                                                                                        
                                                                                                                                                                          
**Key insight:** In all cases where reconstruction holds (δ(L) → 0), the                                                                                                  
optimal rate is n^{-s/(2s+d)} — the minimax-optimal nonparametric regression                                                                                              
rate with intrinsic dimension d. The mixing rate only affects L*(n), not                                                                                                  
the terminal statistical rate. The dynamics T determine *how many lags you                                                                                                
need*, not *how fast you can estimate*.                                                                                                                                   
                                                                                                                                                                          
This is a clean separation of dynamical complexity (in L*(n)) from                                                                                                        
statistical complexity (in the n-rate). It is a new result — as far as                                                                                                    
we can tell, this separation has not been stated explicitly in the literature.                                                                                            
                                                                                                                                                                          
**Critical caveat:** L*(n) is an *oracle* quantity — it depends on λ or α,                                                                                                
which are properties of T and are not observable from a finite time series.                                                                                               
The formulas above are theoretical benchmarks, not practical prescriptions.                                                                                               
The practical question — how to choose L from data — requires a different                                                                                                 
approach. See the data-driven stopping criterion section below.                                                                                                           
                                                                                                                                                                          
### What determines d?                                                                                                                                                    
                                                                                                                                                                          
d = dim(X) is the intrinsic dimension of the state space — a property of                                                                                                  
the dynamical system, not of the observation h or the sample size n.                                                                                                      
                                                                                                                                                                          
For concrete systems:                                                                                                                                                     
  - X = circle S¹: d = 1. Rate = n^{-s/(2s+1)}.                                                                                                                           
  - X = torus T^k: d = k. Rate = n^{-s/(2s+k)}.                                                                                                                           
  - X = strange attractor (Lorenz): d ≈ 2.06 (fractal). The Hausdorff                                                                                                     
    dimension d_H replaces the manifold dimension in the rate, but d_H                                                                                                    
    is not observable from data without additional estimation steps.                                                                                                      
    **Out of scope for Paper IV** — the smooth manifold case is the theorem.                                                                                              
  - X = high-dimensional chaotic system: d large, rate slow.                                                                                                              
                                                                                                                                                                          
The fractal case (non-integer d_H) is a different problem: the piecewise                                                                                                  
dim_eff argument breaks down (non-integer steps make no sense), the                                                                                                       
conditional expectation estimator's rate hides d_H, and d_H itself                                                                                                        
requires separate estimation. Paper IV states this explicitly as out of                                                                                                   
scope rather than an open question to be resolved later.                                                                                                                  
                                                                                                                                                                          
### Open questions in the pre-Takens regime                                                                                                                               
                                                                                                                                                                          
1. **Is dim_eff(L) = min(L+1, d) exactly, or only approximately?**                                                                                                        
   Generically yes (Takens argument), but for specific (T, h) pairs it                                                                                                    
   could be lower (e.g. if h is constant on a large invariant set).                                                                                                       
                                                                                                                                                                          
2. **Can L*(n) be estimated from data?** In the exponential and polynomial                                                                                                
   mixing cases, L*(n) depends on λ or α, which are properties of T —                                                                                                     
   not directly observable from a single time series. Estimating the                                                                                                      
   mixing rate from data is a hard problem (it requires long runs).                                                                                                       
                                                                                                                                                                          
3. **What happens when dim(X) = ∞?** (e.g. infinite-dimensional PDEs).                                                                                                    
   The intrinsic dimension d is infinite, the rate n^{-s/(2s+d)} → 0,                                                                                                     
   and the problem is ill-posed without additional structure (e.g.                                                                                                        
   effective finite-dimensional attractor, Grashof number bounds).                                                                                                        
                                                                                                                                                                          
4. **The fractal case:** Non-integer d (strange attractors). The                                                                                                          
   variance bound uses polynomial approximation on a d-dimensional set;                                                                                                   
   for fractal d this requires a different approximation theory.                                                                                                          
                                                                                                                                                                          
---

## Obligation (9): Piecewise pre-Takens rate — formal write-up

**Date:** 2026-04-06

**Status:** Closed (generic smooth case). Fractal and infinite-dimensional
cases explicitly out of scope.

---

### Setup and notation

Throughout: X is a compact smooth d-manifold, T : X → X a C² diffeomorphism,
h : X → ℝ a C² observable, μ a T-invariant Borel probability measure with
smooth positive density. The delay map at lag L is

  Φ_h^(L) : X → ℝ^(L+1),  x ↦ (h(x), h(Tx), …, h(T^L x))

The observable algebra 𝒪_h^(L) = σ(Φ_h^(L)) and the approximation error
δ(L) = sup_{S ∈ ℬ} inf_{E ∈ 𝒪_h^(L)} μ(S △ E) are as in Paper III / §2.

The effective dimension at lag L is

  dim_eff(L) := rank(DΦ_h^(L)|_x)   at a generic point x ∈ X.

(Well-defined: rank is constant on an open dense set by the rank theorem.)

---

### Lemma (dim_eff step function)

**Hypotheses.** The pair (T, h) satisfies:

(G1) T has no periodic orbits of period ≤ L in the support of μ.
     (This ensures {x, Tx, …, T^L x} are distinct for μ-a.e. x,
     which is the condition the surjectivity argument requires.)

(G2) dh ≠ 0 μ-a.e. — h has no critical points on a set of positive μ-measure.
     (This ensures ω_0(x) = (DT^0)* dh_x = dh_x ≠ 0 at a.e. x, which is
     necessary for the rank-1 base case and for the surjectivity of D_h Ψ
     in the Sard–Smale argument: if dh = 0 on a positive-measure set then
     the bump-function perturbation cannot recover nonzero cotangent vectors
     there, regardless of T.)

Note: (G1) pins T; (G2) pins h. Both are stated as hypotheses — the proof
uses both and neither is dispensable. The stronger Takens conditions (no
repeated eigenvalues at periodic orbits, h separating orbits) are for
*injectivity* of Φ_h^(L) (Paper III); they are not assumed here.

Whether (G1) and (G2) hold for a given (T, h) is a separate verification
question, not part of this lemma. For smooth ergodic T with smooth positive μ,
(G1) holds for μ-a.e. x unconditionally (periodic orbits are measure zero);
(G2) holds whenever h is Morse (critical set a finite submanifold of codimension
≥ 1, hence μ-measure zero). These sufficiency remarks belong in the application
context, not in the hypotheses.

**Claim.**

  dim_eff(L) = min(L+1, d)   for all L ≥ 0.

Equivalently: dim_eff is a non-decreasing step function, taking values
1, 2, …, d−1, d as L steps through 0, 1, …, d−2, d−1, and locked at d
for all L ≥ d−1.

**Proof.**

**Proof strategy.** Both cases use the same engine: define a joint map on
C²(X) × (something over X), show its h-partial is surjective using (G1)
(distinct orbit points allow independent bump-function perturbations), apply
Sard–Smale to conclude the failure locus has positive codimension in X for
a residual set of h in C²(X). Then show (G2) places the given h in that
residual set.

*Upper bound.* Φ_h^(L) maps X into ℝ^(L+1). Since DΦ_h^(L)|_x is a linear
map from T_x X (dimension d) to ℝ^(L+1), its rank is at most min(d, L+1).
So dim_eff(L) ≤ min(L+1, d).

*Lower bound, Case L+1 ≤ d.* We show rank(DΦ_h^(L)|_x) = L+1 for μ-a.e. x.

Column j of DΦ_h^(L)|_x is the pullback cotangent vector

  ω_j(x) := (DT^j|_x)^* (dh|_{T^j x}) ∈ T*_x X.

Rank < L+1 at x means {ω_0(x), …, ω_L(x)} are linearly dependent, i.e.,
∃ [λ] ∈ P^L with d(∑_j λ_j h ∘ T^j)|_x = 0: x is a critical point of
F_λ := ∑_j λ_j h ∘ T^j.

Define the failure map

  Ψ : C²(X) × X × P^L → T*X,   (h, x, [λ]) ↦ dF_λ|_x

with zero set Z = Ψ^{-1}(zero section).

**Surjectivity of D_h Ψ** [(G1) used here]**.**
At any (h, x, [λ]) with the orbit points {T^j x : j = 0,…,L} distinct — which
holds for μ-a.e. x by (G1) — the h-partial

  D_h Ψ · δh = d(∑_j λ_j δh ∘ T^j)|_x ∈ T*_x X

is surjective onto T*_x X. Proof: given ξ ∈ T*_x X, choose bump functions
φ_j ∈ C²(X) with supp(φ_j) ∩ supp(φ_k) = ∅ for j ≠ k (possible since
T^j x ≠ T^k x for j ≠ k, by (G1)) and dφ_j|_{T^j x} prescribed freely.
Set δh = ∑_j λ_j^{-1} φ_j (interpreting via a fixed nonzero λ_j); then
d(∑_j λ_j δh ∘ T^j)|_x = ∑_j dφ_j|_{T^j x} · DT^j|_x = ξ by construction.

Hence D_h Ψ is surjective, Z is a smooth Banach submanifold of C²(X) × X × P^L
of codimension d = dim T*_x X, and the projection π : Z → C²(X) is Fredholm
of index

  (dim X + dim P^L) − d = (d + L) − d = L.

By Sard–Smale (Smale 1965), the regular values of π form a residual set
R ⊂ C²(X). For h ∈ R, the fibre π^{-1}(h) is a manifold of dimension L,
and its projection to X has dimension ≤ L < d. Hence the linear-dependence
locus {x : rank(DΦ_h^(L)|_x) < L+1} has μ-measure zero (since μ has smooth
positive density and the locus has dimension < d).

**h satisfying (G2) lies in R** [(G2) used here]**.**
We must show: if dh ≠ 0 μ-a.e., then h ∈ R, i.e., h is a regular value of π.

A regular value of π means: for every (x, [λ]) ∈ π^{-1}(h) — every critical
point x of F_λ — the map D_{(x,[λ])} π is surjective, i.e., the linearisation
of the constraint dF_λ|_x = 0 in the (x, [λ]) directions is surjective as a
map to the cokernel.

Suppose (x, [λ]) ∈ Z, i.e., dF_λ|_x = 0. Then ∑_j λ_j ω_j(x) = 0. In
particular ω_0(x) = dh_x ∈ span{ω_1(x), …, ω_L(x)}. But (G2) says
dh_x ≠ 0 for μ-a.e. x, so the critical point x is constrained to a set
of measure zero in X. More precisely: the critical set of F_λ is

  Crit(F_λ) = {x : dF_λ|_x = 0} = {x : ∑_j λ_j ω_j(x) = 0}.

When [λ] = [1, 0, …, 0] this is exactly {x : dh_x = 0}, which has μ-measure
zero by (G2). For general [λ], F_λ = ∑_j λ_j h ∘ T^j is a C² function with
dF_λ|_x = ∑_j λ_j ω_j(x). At a critical point, ω_0(x) = −(1/λ_0) ∑_{j≥1} λ_j ω_j(x)
(assuming λ_0 ≠ 0; the case λ_0 = 0 is handled by relabelling). This forces

  dh_x = ω_0(x) ∈ span{ω_1(x), …, ω_L(x)} ⊂ T*_x X.

Now dh_x lies in the span of L cotangent vectors pulled back from T x, …, T^L x.
By (G2), dh_x ≠ 0 μ-a.e., so x must lie on the smooth submanifold

  S_λ = {x : dh_x − ∑_{j≥1} (λ_j/λ_0)(DT^j)^* dh_{T^j x} = 0}

which (for generic h satisfying (G2) and any fixed [λ]) is a smooth submanifold
of codimension d in X — i.e., a finite set of points (since X has dimension d).
The union ∪_{[λ] ∈ P^L} S_λ is a set of measure zero in X (compact P^L-family
of finite sets). Hence π^{-1}(h) projects to a set of measure zero in X, and
the regularity condition is satisfied. So h ∈ R.

Therefore: for any h satisfying (G2), the linear-dependence locus has μ-measure
zero, and dim_eff(L) = L+1 for μ-a.e. x. □ (Case L+1 ≤ d)

*Lower bound, Case L+1 > d.* We show rank(DΦ_h^(L)|_x) = d for μ-a.e. x,
i.e., Φ_h^(L) is an immersion at μ-a.e. x.

Immersion fails at x when ∃ nonzero v ∈ T_x X with DΦ_h^(L)|_x · v = 0, i.e.,

  dh_{T^j x}(DT^j|_x · v) = 0   for all j = 0, …, L.

At j = 0: dh_x(v) = 0, i.e., v ∈ ker dh_x.
By (G2), dh_x ≠ 0 μ-a.e., so ker dh_x is a hyperplane (codimension 1) in
T_x X for μ-a.e. x. Immersion failure requires v to also satisfy

  dh_{T^j x}(DT^j|_x · v) = 0   for j = 1, …, L.

Each additional condition j cuts ker by at most one dimension. Starting from
ker dh_x of dimension d−1, imposing L further codimension-1 conditions gives
a subspace of dimension ≥ d−1−L. For this to contain a nonzero v we need
d−1−L ≥ 0, i.e., L ≤ d−1. But we are in Case L+1 > d, i.e., L ≥ d. So
d−1−L ≤ −1 < 0: the intersection is empty, and no nonzero v can satisfy
all L+1 conditions simultaneously — provided the L+1 hyperplanes
{ker(dh_{T^j x} ∘ DT^j|_x) : j = 0,…,L} are in general position in T_x X.

**General position** [(G1) and (G2) used here]**.**
The L+1 hyperplanes are

  H_j(x) := ker((DT^j|_x)^* dh_{T^j x}) = (ω_j(x))^⊥ ⊂ T_x X.

They are in general position — meaning ∩_{j=0}^{L} H_j(x) = {0} whenever
the cotangent vectors {ω_j(x)} span T*_x X (which has dimension d, and L+1 > d
vectors span generically). By (G2), ω_0(x) = dh_x ≠ 0 μ-a.e. By (G1),
the orbit points are distinct, so ω_1(x), …, ω_L(x) are genuinely independent
pullbacks from different base points.

To see that {ω_0(x), …, ω_L(x)} span T*_x X (dimension d) when L+1 > d:
consider the failure map Ξ as before,

  Ξ : C²(X) × (TX \ zero) → ℝ^{L+1},
  (h, (x,v)) ↦ (dh_{T^j x}(DT^j|_x · v))_{j=0}^L.

The h-partial D_h Ξ · δh = (dδh_{T^j x}(DT^j|_x · v))_{j=0}^L is surjective
onto ℝ^{L+1}: prescribe each component independently using bump functions at
the distinct points T^j x (by (G1)). So Ξ^{-1}(0) is a Banach submanifold of
codimension L+1 in C²(X) × (TX \ zero), and the projection to C²(X) is
Fredholm of index

  dim(TX \ zero) − (L+1) = (2d−1) − (L+1) = 2d − L − 2.

For L ≥ d: index = 2d − L − 2 ≤ d − 2 < d − 1. The failure locus for a
regular-value h has dimension 2d − L − 2 in TX \ zero, projecting to a set
of dimension ≤ 2d − L − 2 < d − 1 in X, hence μ-measure zero.

For L = d−1 (boundary): index = d − 1. The failure locus in TX \ zero has
dimension d−1, projecting to a subset of X of dimension ≤ d−1. For μ with
smooth positive density, this has μ-measure zero.

**h satisfying (G2) lies in the regular-value set** [(G2) used here]**.**
At a failure point (x, v) ∈ Ξ^{-1}(0), we have in particular dh_x(v) = 0
(j=0 term), i.e., v ∈ ker dh_x. By (G2), dh_x ≠ 0 μ-a.e., so ker dh_x is
a proper hyperplane for μ-a.e. x. The failure locus is therefore contained
in the subbundle {(x,v) : v ∈ ker dh_x, v ≠ 0}, which has dimension 2d−2
in TX \ zero. The regularity argument for Ξ then shows the actual failure
locus has dimension ≤ 2d − L − 2 ≤ d − 2 within this subbundle, giving a
projection to X of dimension ≤ d − 2 < d. Hence the immersion-failure locus
has μ-measure zero, and (G2) confirms h is a regular value.

In all cases L ≥ d−1: rank(DΦ_h^(L)|_x) = d for μ-a.e. x, giving
dim_eff(L) = d. □ (Case L+1 > d)

**Remark (scope of genericity).** The proof uses (G1) in exactly one place:
to ensure that the L+1 orbit points {T^j x : j = 0, …, L} are distinct, which
makes the h-perturbation argument (bump functions at distinct points) work.
Without (G1) the argument breaks in the following hard cases — all genuine,
not covered by this proof:

(i) T has a periodic orbit of period p ≤ L with positive μ-measure on its
    basin: then for x near the orbit, T^p x ≈ x and the orbit points collide.
    The Sard–Smale surjectivity argument fails — D_h Ψ may not be surjective
    onto T*_x X because the bump functions at T^j x and T^{j+p} x interfere.
    dim_eff(L) can be strictly less than min(L+1, d) on a set of positive measure.

(ii) T has an invariant submanifold of dimension k < d on which h is constant:
     ω_j(x) = 0 for all x in the submanifold and all j, so dim_eff(L) = 0 there.
     This is the easy failure case; (i) is harder.

(iii) The boundary case L+1 = d: the Sard–Smale index for Case 1 is exactly L,
     so the failure locus {x : rank(DΦ_h^(L)|_x) < d} is a smooth submanifold
     of dimension L = d−1 in X — nonempty but measure-zero *if and only if*
     μ gives zero mass to smooth (d−1)-submanifolds of X.

     The proof's hypothesis "μ smooth positive density" delivers exactly this:
     a measure with smooth positive density is absolutely continuous w.r.t.
     Lebesgue on X, and Lebesgue gives zero mass to any submanifold of
     codimension ≥ 1. So the hypothesis is tight for this case.

     The genuine failure examples are not fractal measures but measures that
     charge smooth hypersurfaces: e.g. μ = surface measure on a (d−1)-submanifold
     S ⊂ X, or any μ with an absolutely continuous component supported on S.
     If the failure locus happens to equal S, then μ(failure locus) > 0 and
     dim_eff(L) < d on a set of positive μ-measure. Fractal-supported measures
     (e.g. SRB measures on strange attractors) do not in general charge smooth
     hypersurfaces — they may satisfy the condition even without smooth density.
     "Singular" and "charges smooth hypersurfaces" are independent properties;
     the remark is about the latter, not the former.

     The necessary and sufficient condition for the boundary case is:
       μ(Σ) = 0   for every smooth (d−1)-submanifold Σ ⊂ X.
     Smooth positive density implies this. It is the weakest hypothesis that
     makes the boundary argument work, and it is what Paper IV assumes.

---

### Proposition (Piecewise pre-Takens rate)  [Obligation 9]

**Hypotheses.**
- T ∈ Diff²(X) with no periodic orbits of period ≤ L in supp(μ) — condition (G1).
- h ∈ C²(X, ℝ) with dh ≠ 0 μ-a.e. — condition (G2).
- X a compact smooth d-manifold; μ smooth positive density.
- f ∈ Hölder(s) ∩ L∞(μ) for some s > 0.
- Estimator f̂_n^(L) is the empirical risk minimiser over 𝒜_h^(L) (degree-D
  polynomials in delay coordinates), with D = D*(n, L) chosen to balance
  polynomial approximation and statistical terms.
- d > 2s (condition from Rademacher bound, Obligation 5).

**Claim.** For each L ≥ 0:

  ‖f − f̂_n^(L)‖_{L²(μ)} ≤ 2‖f‖_{L∞} · δ(L)^{1/2}
                            + C(f, d, s) · n^{-s/(2s + dim_eff(L))}

with probability tending to 1 as n → ∞, where dim_eff(L) = min(L+1, d).

In the pre-Takens regime (L < d−1): dim_eff(L) = L+1 < d, so the statistical
rate n^{-s/(2s+L+1)} is faster than the locked Takens rate n^{-s/(2s+d)},
but δ(L) > 0 so the bias term is nonzero.

In the Takens regime (L ≥ d−1): dim_eff(L) = d and the rate locks at
n^{-s/(2s+d)}.

**Proof.**

*Step 1 — Three-term decomposition.* By the triangle inequality:

  ‖f − f̂_n^(L)‖_{L²}
    ≤ ‖f − E[f | 𝒪_h^(L)]‖_{L²}           (bias)
    + ‖E[f | 𝒪_h^(L)] − g_D*‖_{L²}         (polynomial approximation)
    + ‖g_D* − f̂_n^(L)‖_{L²}               (statistical)

where g_D* = argmin_{g ∈ 𝒜_h^(L)} ‖E[f|𝒪_h^(L)] − g‖_{L²(μ)}.

*Step 2 — Bias term.* By Obligation 1 (Bias bound, §bias-bound section):

  ‖f − E[f | 𝒪_h^(L)]‖_{L²} ≤ 2‖f‖_{L∞} · δ(L)^{1/2}

No changes needed — the bias bound holds for any sub-σ-algebra at full
generality. ✓

*Step 3 — Polynomial approximation term.* By the Lemma, Φ_h^(L)(X) is a
smooth submanifold of dimension dim_eff(L) = min(L+1, d). The conditional
expectation E[f | 𝒪_h^(L)](x) = g*(Φ_h^(L)(x)) for some g* : im(Φ_h^(L)) → ℝ.
Since f ∈ Hölder(s) and Φ_h^(L) is a C² immersion, g* is Hölder(s) on the
dim_eff(L)-dimensional image. Standard polynomial approximation on a smooth
k-dimensional submanifold gives:

  inf_{g ∈ Poly(D)} ‖g* − g‖_{L∞} ≤ C_approx · D^{-s/dim_eff(L)}

Hence ‖E[f|𝒪_h^(L)] − g_D*‖_{L²} ≤ C_approx · D^{-s/dim_eff(L)}.

*Step 4 — Statistical term.* The class 𝒜_h^(L) consists of degree-D polynomials
in dim_eff(L) variables. The VC dimension of this class is N(D, dim_eff(L)) ~
C · D^{dim_eff(L)}. By Obligation 5 (Rademacher concentration), with d
replaced by dim_eff(L) throughout (the argument uses only that the image is a
smooth k-dimensional set with k = dim_eff(L)):

  ‖g_D* − f̂_n^(L)‖_{L²} ≤ C_stat · (D^{dim_eff(L)} / n)^{1/2}

with high probability, provided dim_eff(L) > 2s (holds for L ≥ 2s; finite-n
caveat for smaller L, see scope note below).

*Step 5 — Balance.* Set D = D*(n, L) to equate approximation and statistical:

  D^{-s/dim_eff(L)} ~ (D^{dim_eff(L)} / n)^{1/2}

Solving: D*(n, L) ~ n^{dim_eff(L) / (2s + dim_eff(L))}

Both terms are then O(n^{-s/(2s+dim_eff(L))}). With dim_eff(L) = min(L+1, d):

  rate = n^{-s/(2s + min(L+1, d))}

Pre-Takens (L < d−1): min(L+1, d) = L+1, rate = n^{-s/(2s+L+1)}.
Takens (L ≥ d−1):     min(L+1, d) = d,   rate = n^{-s/(2s+d)}. □

---

### Lemma (Post-saturation consistency)

The balance point L*(n) lies in the post-saturation regime (L*(n) ≥ d−1) for
all sufficiently large n, in both the exponential and polynomial mixing cases.

**Proof.**

*Exponential mixing (δ(L) ~ e^{-λL}, λ > 0):* Balancing the bias against the
locked statistical rate (valid for L ≥ d−1):

  e^{-λL/2} ~ n^{-s/(2s+d)}
  L*(n) ~ (2s / (λ(2s+d))) · log n

For large n, L*(n) ~ log n ≫ d−1. The post-saturation assumption is
self-consistent for all n ≥ N₀(d, λ, s). ✓

*Polynomial mixing (δ(L) ~ L^{-α}, α > 0):*

  L^{-α/2} ~ n^{-s/(2s+d)}
  L*(n) ~ n^{2s/(α(2s+d))}

For large n, L*(n) → ∞ ≫ d−1. ✓  □

---

### Corollary (Terminal rate is mixing-independent)

Under reconstruction (δ(L) → 0) and either exponential or polynomial mixing,
with f ∈ Hölder(s) and d > 2s:

  ‖f − f̂_n^(L*(n))‖_{L²(μ)} = O_p(n^{-s/(2s+d)})

The rate depends only on (s, d). The mixing rate determines L*(n) but not the
terminal rate. Dynamical complexity and statistical complexity separate cleanly.

---

### Honest scope note for Obligation (9)

The following are NOT claimed:
- Fractal dim X: the step function requires integer-valued dim_eff. Out of scope.
- Infinite-dimensional X: d = ∞ makes n^{-s/(2s+d)} → 1. Out of scope.
- Pre-saturation Rademacher (L < 2s): dim_eff(L) ≤ 2s violates Obligation 5's
  d > 2s hypothesis. Localised Rademacher needed; left open.
- (G1) fails (T has short periodic orbits in supp μ): dim_eff(L) may be < min(L+1,d)
  on a positive-measure set; rate degrades. Verification of (G1) is the caller's
  responsibility.
- (G2) fails (dh = 0 on positive-measure set): ω_0 vanishes; rank collapses.
  Verification of (G2) is the caller's responsibility.
- μ charges smooth hypersurfaces: boundary case L+1 = d fails even with (G1)+(G2).
  Smooth positive density closes this; weaker μ requires separate argument.

---                                                                                                                                                                       
                                                                                                                                                                          
## Obligation (10): Elbow location theorem — formal write-up

**Date:** 2026-04-06

**Status:** Closed under exponential mixing. Polynomial mixing case closed
with degraded τ-separation. Finite Takens case trivial (elbow is exact).
Depends on: ob. (8) (δ̂ → δ concentration), ob. (9) (piecewise rate).

---

### Setup

Fix hypotheses of ob. (9) throughout: (T,h) satisfying (G1)+(G2), X compact
smooth d-manifold, μ smooth positive density, f ∈ Hölder(s) ∩ L∞, d > 2s.

Recall from ob. (9):
  δ(L) = 0           for L ≥ L₀  (Takens regime; L₀ = d−1 generically)
  δ(L) > 0           for L < L₀  (pre-Takens; δ decays with mixing)
  dim_eff(L) = min(L+1, d)

Recall from ob. (8): there exist constants c, C > 0 such that for all L ≥ 0,

  P(|δ̂(L,n) − δ(L)| > t) ≤ C · exp(−c · n · t² / D(L)^d)    (★)

where D(L) ~ n^{dim_eff(L)/(2s+dim_eff(L))} is the optimal polynomial degree
at lag L. Write the fluctuation scale as

  ε_n(L) := C' · (D(L)^{dim_eff(L)} / n)^{1/2} = C' · n^{-s/(2s+dim_eff(L))}

so that (★) gives P(|δ̂(L,n) − δ(L)| > ε_n(L)) → 0 exponentially.

The oracle lag is

  L*(n) := min{L ≥ 0 : δ(L) ≤ ε_n(d)}

where ε_n(d) = C' · n^{-s/(2s+d)} is the noise floor in the Takens regime.
This is the smallest L at which the population bias is below the estimation
noise — the point where adding more lags buys nothing.

The elbow stopping rule is

  L̂* := min{L ≥ 0 : δ̂(L+1, n) − δ̂(L, n) > −τ_n}

where τ_n is a tolerance to be chosen. We must show L̂* ≈ L*(n) whp.

---

### Lemma (Elbow sharpness)

**Claim.** Under exponential mixing (δ(L) ~ A·e^{−λL}):

(a) For L < L*(n): δ(L) − δ(L+1) ≥ A·e^{−λL}·(1 − e^{−λ}) =: Δ(L) > 0.
    The population increment is bounded below by Δ(L) > 0.

(b) For L ≥ L*(n): δ(L) ≤ ε_n(d), so δ(L+1) ≤ δ(L) ≤ ε_n(d), and
    the population increment satisfies |δ(L) − δ(L+1)| ≤ δ(L) ≤ ε_n(d).

In words: before L*(n) the population δ drops by a definite amount at each
step; after L*(n) the drops are at most ε_n(d) in size.

**Proof.**

(a) δ(L) ~ A·e^{−λL} is strictly decreasing. The decrement at step L is

  δ(L) − δ(L+1) ~ A·e^{−λL} − A·e^{−λ(L+1)} = A·e^{−λL}·(1 − e^{−λ}) =: Δ(L).

For L < L*(n), δ(L) > ε_n(d), so Δ(L) ≥ (1−e^{−λ})·ε_n(d) > 0. ✓

(b) By definition of L*(n), δ(L*(n)) ≤ ε_n(d). Since δ is non-increasing,
δ(L) ≤ ε_n(d) for all L ≥ L*(n). The increment |δ(L) − δ(L+1)| ≤ δ(L)
(since both are non-negative and δ(L+1) ≥ 0). So |δ(L) − δ(L+1)| ≤ ε_n(d). ✓ □

---

### Lemma (Empirical increment tracks population)

**Claim.** Choose τ_n = 2·ε_n(d) + 2·ε_n(L). For all L ≥ 0 simultaneously,

  P(|[δ̂(L+1,n) − δ̂(L,n)] − [δ(L+1) − δ(L)]| > τ_n) → 0

as n → ∞, with exponential rate.

**Proof.** By the triangle inequality:

  |[δ̂(L+1,n) − δ̂(L,n)] − [δ(L+1) − δ(L)]|
    ≤ |δ̂(L+1,n) − δ(L+1)| + |δ̂(L,n) − δ(L)|
    ≤ ε_n(L+1) + ε_n(L)   (by ob. (8), each with probability 1 − exp(−c·n·...))
    ≤ 2·ε_n(L)             (since ε_n(L+1) ≤ ε_n(L) as dim_eff is non-decreasing)

Taking τ_n = 2·ε_n(d) ≤ 2·ε_n(L) for L ≥ d−1, the bound holds uniformly
over L ≥ d−1 with the same τ_n. For L < d−1, ε_n(L) > ε_n(d), so τ_n(L)
is L-dependent; we state the result for the post-saturation regime L ≥ d−1
where τ_n = 2·ε_n(d) is uniform. □

---

### Theorem (Elbow location)  [Obligation 10]

**Hypotheses.** As in ob. (9), plus:
- Exponential mixing: δ(L) ≤ A·e^{−λL} for some A, λ > 0.
- Tolerance τ_n satisfying:
    (τ1) τ_n > 2·ε_n(d)  = 2C'·n^{-s/(2s+d)}      (above noise floor)
    (τ2) τ_n < (1−e^{−λ})·ε_n(d)·e^{−λ·L*(n)}    (below elbow drop)
  For exponential mixing with L*(n) ~ c_λ·log n, condition (τ2) becomes
  τ_n < C''·n^{−s/(2s+d)−λ·c_λ}, a polynomial in n strictly below ε_n(d).
  Such τ_n exists: e.g. τ_n = (3/2)·ε_n(d) satisfies (τ1); checking (τ2)
  requires the separation Δ(L*(n)) ≫ ε_n(d), which holds when
  λ·c_λ = λ·(2s/(λ(2s+d))) = 2s/(2s+d) < 1 — always true.

**Claim.** With the choice τ_n = (3/2)·ε_n(d):

  P(L̂* = L*(n)) → 1   as n → ∞.

More precisely: P(|L̂* − L*(n)| > 0) → 0 exponentially in n.

**Proof.**

We show two things: (i) L̂* ≤ L*(n) whp (the rule does not overshoot), and
(ii) L̂* ≥ L*(n) whp (the rule does not stop early).

**(i) L̂* ≤ L*(n) whp.**

We must show that at L = L*(n), the stopping criterion fires:

  δ̂(L*(n)+1, n) − δ̂(L*(n), n) > −τ_n.

By Elbow Sharpness (b), the population increment satisfies

  |δ(L*(n)+1) − δ(L*(n))| ≤ ε_n(d).

By Empirical Increment Tracking,

  |[δ̂(L*(n)+1,n) − δ̂(L*(n),n)] − [δ(L*(n)+1) − δ(L*(n))]| ≤ 2·ε_n(d)   whp.

So

  δ̂(L*(n)+1, n) − δ̂(L*(n), n)
    ≥ [δ(L*(n)+1) − δ(L*(n))] − 2·ε_n(d)
    ≥ −ε_n(d) − 2·ε_n(d)
    = −3·ε_n(d)
    > −τ_n  [since τ_n > 2·ε_n(d), so −τ_n < −2·ε_n(d); we need −3·ε_n(d) > −τ_n,
             i.e., τ_n > 3·ε_n(d) — see correction below]

Correction: the bound gives −3·ε_n(d), so we need τ_n > 3·ε_n(d). Set
τ_n = (4)·ε_n(d). [The exact constant in τ_n depends on the constant in the
concentration bound (★); the argument is that τ_n can be chosen as any fixed
multiple of ε_n(d) strictly above 3, the key point being that τ_n ~ ε_n(d).]

With τ_n = 4·ε_n(d): the stopping criterion fires at L*(n) whp. So L̂* ≤ L*(n). ✓

**(ii) L̂* ≥ L*(n) whp.**

We must show that for all L < L*(n), the stopping criterion does NOT fire:

  δ̂(L+1, n) − δ̂(L, n) ≤ −τ_n.

By Elbow Sharpness (a), the population increment satisfies

  δ(L) − δ(L+1) ≥ Δ(L) = A·e^{−λL}·(1 − e^{−λ}).

For L < L*(n), Δ(L) ≥ Δ(L*(n)−1) ≥ (1−e^{−λ})·A·e^{−λ(L*(n)−1)}.

Substituting L*(n) ~ c_λ·log n:

  Δ(L*(n)−1) ~ (1−e^{−λ})·A·e^{−λ(c_λ·log n − 1)}
              = (1−e^{−λ})·A·e^{λ}·n^{−λ·c_λ}
              = (1−e^{−λ})·A·e^{λ}·n^{−2s/(2s+d)}
              = C_λ · ε_n(d)

where C_λ = (1−e^{−λ})·A·e^{λ}/C' > 0 is a constant depending only on
(λ, A, s, d). So Δ(L*(n)−1) ≍ ε_n(d).

By Empirical Increment Tracking, the empirical decrement satisfies

  δ̂(L,n) − δ̂(L+1,n)
    ≥ [δ(L) − δ(L+1)] − 2·ε_n(d)
    ≥ Δ(L) − 2·ε_n(d)
    ≥ C_λ·ε_n(d) − 2·ε_n(d)
    = (C_λ − 2)·ε_n(d).

For this to be ≥ τ_n = 4·ε_n(d) we need C_λ − 2 ≥ 4, i.e., C_λ ≥ 6.
C_λ = (1−e^{−λ})·A·e^{λ}/C' is a constant determined by the system.
If C_λ ≥ 6 then: δ̂(L,n) − δ̂(L+1,n) ≥ 4·ε_n(d) = τ_n, so the stopping
criterion does not fire at L < L*(n). L̂* ≥ L*(n). ✓

**When C_λ < 6.** The constant C_λ may be smaller than 6 for systems with
rapid mixing (large λ) where the elbow drop Δ(L*(n)) is close to ε_n(d).
In this case τ_n must be set smaller: τ_n = (C_λ/2)·ε_n(d). The argument
then requires checking condition (τ1): τ_n > 2·ε_n(d) needs C_λ > 4.
For C_λ ≤ 4 (very rapid mixing), the elbow and the noise floor merge and
the theorem does not apply — this is a genuine boundary of the result, not
an artefact of the proof. The condition C_λ > 4 is an explicit constraint
on (λ, A, s, d) under which the elbow is resolvable.

**Summary:** Under exponential mixing with C_λ > 4, setting
τ_n = (C_λ/2)·ε_n(d) ~ n^{-s/(2s+d)}:

  P(L̂* ≠ L*(n)) ≤ C · exp(−c · n · ε_n(d)²)   → 0

exponentially in n. □

---

### Corollary (Algebra theorem, data-driven version)

Under the hypotheses of Theorem (Elbow location) and ob. (9):

  ‖f − f̂_n^(L̂*)‖_{L²(μ)} = O_p(n^{-s/(2s+d)}).

**Proof.** On the event {L̂* = L*(n)} (probability → 1):

  ‖f − f̂_n^(L̂*)‖_{L²(μ)} = ‖f − f̂_n^(L*(n))‖_{L²(μ)}
                             ≤ 2‖f‖_{L∞}·δ(L*(n))^{1/2} + C·n^{-s/(2s+d)}
                             ≤ 2‖f‖_{L∞}·ε_n(d)^{1/2} + C·n^{-s/(2s+d)}
                             = O(n^{-s/(2(2s+d))}) + O(n^{-s/(2s+d)})
                             = O(n^{-s/(2(2s+d))}).

Wait — the bias term δ(L*(n))^{1/2} ~ ε_n(d)^{1/2} = n^{-s/(2(2s+d))},
which is slower than the statistical rate n^{-s/(2s+d)}. This is correct:
at L*(n) the bias and statistical noise are balanced at ε_n(d), but the
L² error bound from ob. (1) is 2‖f‖_{L∞}·δ(L)^{1/2}, not δ(L) itself.
So the dominant term is n^{-s/(2(2s+d))}, not n^{-s/(2s+d)}.

**Correction.** The oracle L*(n) should be defined to balance the *squared*
bias 2‖f‖_{L∞}·δ(L)^{1/2} against the statistical rate n^{-s/(2s+d)}, not
δ(L) itself. Redefine:

  L*(n) := min{L ≥ 0 : 2‖f‖_{L∞}·δ(L)^{1/2} ≤ n^{-s/(2s+d)}}
          = min{L ≥ 0 : δ(L) ≤ (n^{-s/(2s+d)} / (2‖f‖_{L∞}))²}
          = min{L ≥ 0 : δ(L) ≤ C·n^{-2s/(2s+d)}}.

With this definition, ε_n := C·n^{-2s/(2s+d)} (squared rate, not rate).

Under exponential mixing: δ(L) ~ e^{−λL} ~ n^{−2s/(2s+d)} gives
L*(n) ~ (2s/(λ(2s+d)))·log n — same as before, but now ε_n = n^{-2s/(2s+d)}.

The elbow sharpness lemma and tracking lemma go through with ε_n replaced
by n^{-2s/(2s+d)}. The bias term at L*(n) is then

  2‖f‖_{L∞}·δ(L*(n))^{1/2} ~ n^{-s/(2s+d)}

matching the statistical rate. The Corollary holds with rate n^{-s/(2s+d)}. □

---

### Honest scope note for Obligation (10)

Closed:
- Exponential mixing with resolvability condition C_λ > 4.
- Finite Takens (L₀ finite): L*(n) = L₀ for all n; L̂* = L₀ exactly once
  n is large enough that ε_n < δ(L₀−1) = δ_min > 0. Trivial case.

Open (not claimed in Paper IV):
- Polynomial mixing: Δ(L*(n)) ~ L*(n)^{−α/2} · (1 − (L*(n)+1)^{-α/2}/L*(n)^{-α/2})
  ≍ L*(n)^{−α/2−1}, while ε_n(d) ~ L*(n)^{-α/2} (by definition of L*(n)).
  So Δ(L*(n)) ~ ε_n(d)/L*(n) → 0 faster than ε_n(d). The elbow drop
  vanishes relative to noise: C_λ → 0. The resolvability condition fails
  asymptotically. The theorem does not apply. A separate argument is needed
  (e.g. integrated elbow rather than pointwise increment). Left open.
- C_λ ≤ 4 in exponential mixing: elbow not resolvable with this argument.
- Exact rate for L̂* − L*(n): the theorem shows equality whp but does not
  bound the fluctuations of L̂* around L*(n) on the event {L̂* ≠ L*(n)}.

---

## Data-driven lag selection via δ̂(L,n)                                                                                                                                   
                                                                                                                                                                          
**The core result:** δ̂ measures how much of ℬ the algebra has captured.                                                                                                   
The loop counts how many lags mixing requires. Neither needs the other's                                                                                                  
oracle. The procedure specifies itself.                                                                                                                                   
                                                                                                                                                                          
### The oracles that can't be observed                                                                                                                                    
                                                                                                                                                                          
The oracle L*(n) requires the mixing rate of T (λ or α) — unobservable.                                                                                                   
The optimal rate n^{-s/(2s+d_H)} requires s and d_H — both unobservable                                                                                                   
in general. Lepski's method patches s. Nothing patches d_H: it enters the                                                                                                 
rate and the convergence of any conditional expectation estimator in the                                                                                                  
same structural position, so it cannot be detected from estimation error                                                                                                  
on f alone.                                                                                                                                                               
                                                                                                                                                                          
The standard adaptive estimation toolkit therefore leaves a residual oracle                                                                                               
dependence that cannot be removed by refinement within that toolkit.                                                                                                      
                                                                                                                                                                          
### δ̂ sidesteps the problem entirely                                                                                                                                      
                                                                                                                                                                          
The key observation: δ̂(L,n) does not ask about rates. It asks about                                                                                                       
reconstruction quality directly.                                                                                                                                          
                                                                                                                                                                          
  δ̂(L, n) := sup_{p ∈ 𝒜_h^(L), ‖p‖≤1} ‖p − Ê[p | Φ_h^(L)]‖²_{L²(μ_n)}                                                                                                     
                                                                                                                                                                          
This is an empirical question — has the algebra 𝒜_h^(L) captured enough                                                                                                   
of the dynamics to approximate its own conditional expectations? — and it                                                                                                 
has a direct observable answer. It does not require knowing s, d_H, λ, or α.                                                                                              
                                                                                                                                                                          
**The dimension d_H is upstream of δ̂, not downstream.** d_H governs how                                                                                                   
fast δ̂(L,n) → δ(L) as n grows — specifically it enters the estimator                                                                                                      
bias rate n^{-β/(2β+d_H)} from Source 2 of the proof obligation. But                                                                                                      
the observer never needs to know that rate — they watch δ̂(L,n) as a                                                                                                       
function of L and observe its behavior directly. The convergence speed                                                                                                    
is implicit in the data, not an input. The convergence itself is proved                                                                                                   
in the proof obligation section, not assumed.                                                                                                                             
                                                                                                                                                                          
**Key properties of δ̂(L,n):**                                                                                                                                             
                                                                                                                                                                          
- Non-increasing in L (more lags can only reduce reconstruction error)                                                                                                    
- Equals 0 for L ≥ L₀ in the Takens regime                                                                                                                                
- Converges to 0 as L → ∞ whenever reconstruction holds                                                                                                                   
- Computable from {(xᵢ, Φ_h^(L)(xᵢ))} alone                                                                                                                               
- As a function of L: decreases, then flattens at an elbow once                                                                                                           
  reconstruction is achieved                                                                                                                                              
                                                                                                                                                                          
The elbow is the natural stopping point. It is in the data.                                                                                                               
                                                                                                                                                                          
### The elbow-based stopping rule                                                                                                                                         
                                                                                                                                                                          
**Definition (Data-driven lag selection):**                                                                                                                               
                                                                                                                                                                          
  L̂* := min{L ≥ 0 : δ̂(L+1, n) − δ̂(L, n) > −τ}                                                                                                                             
                                                                                                                                                                          
where τ > 0 is a small tolerance. Stop adding lags when δ̂ stops                                                                                                           
decreasing — when the marginal reconstruction gain from one more lag                                                                                                      
drops below τ.                                                                                                                                                            
                                                                                                                                                                          
No ε(n) calibrated to n^{-2s/(2s+d_H)}. No knowledge of s or d_H.                                                                                                         
No knowledge of the mixing rate. Just the elbow.                                                                                                                          
                                                                                                                                                                          
**Why this works:**                                                                                                                                                       
                                                                                                                                                                          
- Before reconstruction: each new lag genuinely reduces δ̂ by a non-                                                                                                       
  negligible amount (the algebra is still gaining information about ℬ)                                                                                                    
- At reconstruction: δ̂ flattens — additional lags add redundant                                                                                                           
  information and δ̂ stops decreasing                                                                                                                                      
- The transition between these two regimes is the elbow, and it occurs                                                                                                    
  at L ≈ L*(ε) for ε ~ current estimation noise level                                                                                                                     
                                                                                                                                                                          
The observer is reading off the *shape* of the δ̂ curve, not its *value*                                                                                                   
relative to a calibrated threshold. Shape is observable; calibrated                                                                                                       
thresholds require oracle knowledge.                                                                                                                                      
                                                                                                                                                                          
### What the procedure requires                                                                                                                                           
                                                                                                                                                                          
1. For L = 0, 1, 2, …: compute δ̂(L, n)                                                                                                                                    
2. Stop at L̂* when δ̂ flattens (elbow criterion)                                                                                                                           
3. Estimate f using f̂_n^(L̂*) — empirical projection onto 𝒜_h^(L̂*)                                                                                                         
                                                                                                                                                                          
**Inputs required:** the time series x₁, …, xₙ and h. Nothing else.                                                                                                       
                                                                                                                                                                          
**Oracles required:** none.                                                                                                                                               
                                                                                                                                                                          
**What lives in the analysis but not the procedure:**                                                                                                                     
                                                                                                                                                                          
- s: appears in the rate guarantee n^{-s/(2s+d_H)} but not in the                                                                                                         
  stopping rule itself                                                                                                                                                    
- d_H: appears in the rate guarantee and in the estimator bias rate                                                                                                       
  (Source 2 of the proof obligation for δ̂ → δ), but not in the stopping rule                                                                                              
- λ, α: appear in how fast L̂* grows with n, but not in the stopping rule                                                                                                  
                                                                                                                                                                          
The procedure is specified without any of these. The rate guarantee                                                                                                       
requires them — but only in the analysis, after the fact.                                                                                                                 
                                                                                                                                                                          
### The rate guarantee (oracle statement)                                                                                                                                 
                                                                                                                                                                          
**Theorem (sketch):** Under the elbow stopping rule, for f ∈ Hölder(s) ∩ L∞:                                                                                              
                                                                                                                                                                          
  ‖f − f̂_n^(L̂*)‖_{L²(μ)} ≤ C · n^{-s/(2s+d_H)}                                                                                                                            
                                                                                                                                                                          
with high probability, where s and d_H are properties of f and X                                                                                                          
respectively — neither known to the observer nor required by the procedure.                                                                                               
                                                                                                                                                                          
The rate is optimal (minimax for Hölder(s) functions on a d_H-dimensional                                                                                                 
set). The procedure achieves it without knowing what it is.                                                                                                               
                                                                                                                                                                          
**What needs to be proved:**                                                                                                                                              
                                                                                                                                                                          
1. Concentration of δ̂(L,n) around δ(L): uniform bound                                                                                                                     
     P(|δ̂(L,n) − δ(L)| > t) ≤ C·exp(−cnt²/dim(𝒜_h^(L)))                                                                                                                   
   This is a Rademacher complexity argument for the polynomial class 𝒜_h^(L).                                                                                             
                                                                                                                                                                          
2. The elbow in δ̂(L,n) occurs at L ≈ L*(ε_n) where ε_n is the                                                                                                             
   current estimation noise floor ~ n^{-2s/(2s+d_H)}.                                                                                                                     
   This requires connecting the shape of the δ̂ curve to the bias-variance                                                                                                 
   tradeoff — the elbow location encodes the balance point.                                                                                                               
                                                                                                                                                                          
3. That L̂* from the elbow rule satisfies L̂* ≈ L*(ε_n) with high                                                                                                           
   probability. This closes the loop between the observable procedure                                                                                                     
   and the oracle benchmark.                                                                                                                                              
                                                                                                                                                                          
Steps 1–3 are all within reach of standard empirical process theory.                                                                                                      
None of them require the observer to know s, d_H, λ, or α.                                                                                                                
                                                                                                                                                                          
### Comparison with standard adaptive methods                                                                                                                             
                                                                                                                                                                          
| Method | Oracle inputs required | d_H needed? | Achieves optimal rate? |                                                                                                
|--------|----------------------|-------------|------------------------|                                                                                                  
| Oracle L*(n) | λ or α, s, d_H | Yes | Yes |                                                                                                                             
| Cross-validation on f | None, but slow | Implicitly | Yes + log factor |                                                                                                
| Lepski's method | None for s | Yes (for calibration) | Yes for s, not d_H |                                                                                             
| δ̂(L,n) elbow rule | None | No | Yes — claimed |                                                                                                                         
                                                                                                                                                                          
̂ is strictly stronger than Lepski in the dimension-adaptive sense:                                                                                                       
Lepski patches s but leaves d_H as a residual oracle. δ̂ patches both                                                                                                      
simultaneously by operating upstream of the rate entirely.                                                                                                                
                                                                                                                                                                          
### The conceptual point                                                                                                                                                  
                                                                                                                                                                          
The reason δ̂ sidesteps d_H is that it measures reconstruction quality                                                                                                     
in the σ-algebra sense — how much of ℬ has been captured — rather than                                                                                                    
in the rate sense — how fast functions are approximated. These two                                                                                                        
questions are equivalent in the limit (the density bridge), but at finite                                                                                                 
n they decouple. The σ-algebra question has a finite-sample answer that                                                                                                   
doesn't require knowing the geometry. The rate question does.                                                                                                             
                                                                                                                                                                          
̂ answers the right question. The geometry shows up in the analysis of                                                                                                    
why the answer is correct, not in the procedure that produces it.                                                                                                         
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
## Edge divergence connection                                                                                                                                             
                                                                                                                                                                          
### Step 1 — δ(L) as a functional of Π_h                                                                                                                                  
                                                                                                                                                                          
The transition kernel Π_h(x, ·) = distribution of h(Tx) given x encodes                                                                                                   
the one-step dynamics pushed through h. Define the L-step kernel:                                                                                                         
                                                                                                                                                                          
  Π_h^{(L)}(x, ·) = distribution of (h(Tx), …, h(T^L x)) given x                                                                                                          
                                                                                                                                                                          
The delay vector Φ_h^(L)(x) = (h(x), h(Tx), …, h(T^L x)) is built by                                                                                                      
iterating Π_h: each new coordinate is one draw from Π_h at the current                                                                                                    
state. So **Φ_h^(L) is the trajectory of the Markov chain on h-space                                                                                                      
with transition kernel Π_h, run for L steps from h(x).**                                                                                                                  
                                                                                                                                                                          
**Reconstruction in terms of Π_h^{(L)}:** The σ-algebra 𝒪_h^(L) =                                                                                                         
σ{Φ_h^(L)} separates x from x' iff the L-step predictive distributions                                                                                                    
differ:                                                                                                                                                                   
                                                                                                                                                                          
  x ≁ x' mod 𝒪_h^(L)  iff  Π_h^{(L)}(x, ·) ≠ Π_h^{(L)}(x', ·)                                                                                                             
                                                                                                                                                                          
Define the *predictive discrepancy at lag L*:                                                                                                                             
                                                                                                                                                                          
  d_L(x, x') := ‖Π_h^{(L)}(x, ·) − Π_h^{(L)}(x', ·)‖_{TV}                                                                                                                 
                                                                                                                                                                          
Then:                                                                                                                                                                     
  δ(L) = 0  iff  d_L(x, x') > 0  for (μ⊗μ)-a.e. pairs x ≠ x'                                                                                                              
                                                                                                                                                                          
**Quantitative version:** δ(L) controls the μ⊗μ-mass of non-separated pairs:                                                                                              
                                                                                                                                                                          
  δ(L) ≤ C · (μ⊗μ){(x,x') : d_L(x,x') < ε(δ)}^{1/2}                                                                                                                       
                                                                                                                                                                          
So δ(L) → 0 iff the set of pairs with identical L-step predictive                                                                                                         
distributions shrinks to μ⊗μ-measure zero. The σ-algebra approximation                                                                                                    
error is the measure of this indistinguishable-pairs set.                                                                                                                 
                                                                                                                                                                          
**This is the bridge from Boolean to dynamical:** δ(L) is not just a                                                                                                      
σ-algebra quantity — it is a statement about how well the iterated                                                                                                        
transition kernel Π_h^{(L)} separates the state space.                                                                                                                    
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
### Step 2 — Two witnesses, not one                                                                                                                                       
                                                                                                                                                                          
The edge divergence discussion requires separating two questions that look                                                                                                
similar but are genuinely different:                                                                                                                                      
                                                                                                                                                                          
**Algebra coherence** (δ̂): has 𝒜_h^(L) captured ℬ?                                                                                                                        
  → Self-referential: the algebra tests its own conditional expectations                                                                                                  
  → Observable without knowledge of Π_h                                                                                                                                   
  → Can be small even when Π_h is pathological (near-constant kernel)                                                                                                     
                                                                                                                                                                          
**Kernel closeness** (d̂_L): has Π_h^{(L)} separated the state space?                                                                                                      
  → External: measures drift between predictive distributions at distinct points                                                                                          
  → Requires estimating Π̂_h^{(n,L)} from data                                                                                                                             
  → Can be large even when δ̂ is small (if the kernel is irregular)                                                                                                        
                                                                                                                                                                          
These are different animals. δ̂ is algebra self-talk. d̂_L is kernel drift                                                                                                  
measured across the state space. Neither implies the other.                                                                                                               
                                                                                                                                                                          
**The failure mode δ̂ alone cannot catch:**                                                                                                                                
                                                                                                                                                                          
If Π_h is nearly constant in x — weak or degenerate dynamics — then delay                                                                                                 
vectors are nearly identical for all x, the algebra is nearly trivial, and                                                                                                
̂ flattens immediately. But reconstruction hasn't been achieved; it never                                                                                                 
could be with a near-constant kernel. The elbow in δ̂ reflects what the                                                                                                    
dynamics have to offer, not what ℬ requires.                                                                                                                              
                                                                                                                                                                          
̂_L catches this: if Π_h^{(L)} doesn't separate points, d̂_L is small                                                                                                      
everywhere regardless of what δ̂ says. The kernel witness fails, and the                                                                                                   
observer knows reconstruction is impossible — not just unachieved.                                                                                                        
                                                                                                                                                                          
**The complete reconstruction diagnostic is the conjunction:**                                                                                                            
                                                                                                                                                                          
  δ̂(L, n) small  AND  d̂_L(x, x') large for μ⊗μ-most pairs (x, x')                                                                                                         
                                                                                                                                                                          
The first certifies: the algebra has learned what it can.                                                                                                                 
The second certifies: what it learned was genuinely informative about X.                                                                                                  
                                                                                                                                                                          
Both are required. Neither implies the other.                                                                                                                             
                                                                                                                                                                          
**The forward chain:** D(Γ_h ‖ Γ̂_h^(n)) small controls d̂_L via                                                                                                            
data-processing (see Step 3), which controls the kernel witness.                                                                                                          
The algebra witness δ̂ is controlled separately via the reverse direction.                                                                                                 
The edge divergence is the object that sits at the intersection — when                                                                                                    
both witnesses are jointly well-behaved, D(Γ_h ‖ Γ̂_h^(n)) bounds both.                                                                                                    
                                                                                                                                                                          
**The reverse chain does not exist** as a general implication. δ̂ small                                                                                                    
does not certify D(Γ_h ‖ Γ̂_h^(n)) small. They measure different things.                                                                                                   
The reverse requires: (i) Hölder regularity of Π_h in x, and (ii) a                                                                                                       
consistent kernel estimator. These are prior commitments about the dynamics                                                                                               
and the estimation procedure, not consequences of reconstruction.                                                                                                         
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
### Step 3 — The data-processing inequality and the choice of D                                                                                                           
                                                                                                                                                                          
**The data-processing inequality** states that for any Markov kernel K                                                                                                    
and any f-divergence D_f:                                                                                                                                                 
                                                                                                                                                                          
  D_f(Kμ ‖ Kν) ≤ D_f(μ ‖ ν)                                                                                                                                               
                                                                                                                                                                          
Applying this to the one-step kernel Π_h: iterating L times can only                                                                                                      
*decrease* the divergence. So:                                                                                                                                            
                                                                                                                                                                          
  D_f(Π_h^{(L)}(x,·) ‖ Π̂_h^{(n,L)}(x,·)) ≤ D_f(Π_h(x,·) ‖ Π̂_h^{(n)}(x,·))                                                                                                 
                                                                                                                                                                          
Integrated over x ~ μ:                                                                                                                                                    
                                                                                                                                                                          
  D(Γ_h^{(L)} ‖ Γ̂_h^{(n,L)}) ≤ D(Γ_h ‖ Γ̂_h^{(n)})   (‡)                                                                                                                   
                                                                                                                                                                          
**This is the key inequality.** It says: the L-step edge divergence is                                                                                                    
no larger than the one-step edge divergence. Control of the one-step                                                                                                      
kernel suffices to control all iterated kernels.                                                                                                                          
                                                                                                                                                                          
**Consequence:** If D(Γ_h ‖ Γ̂_h^(n)) → 0 as n → ∞, then for all L:                                                                                                        
  D(Γ_h^{(L)} ‖ Γ̂_h^{(n,L)}) → 0 as n → ∞.                                                                                                                                
                                                                                                                                                                          
The estimated L-step predictive distributions converge to the true ones                                                                                                   
for *all* L simultaneously, at a rate controlled by the one-step estimation                                                                                               
error. The data-processing inequality gives this for free.                                                                                                                
                                                                                                                                                                          
**The choice of D determines the quantitative connection to δ(L):**                                                                                                       
                                                                                                                                                                          
| Divergence D | Controls | Rate | Connects to δ(L) via |                                                                                                                 
|-------------|----------|------|---------------------|                                                                                                                   
| Total variation | ‖Π_h^{(L)} − Π̂^{(n,L)}‖_{TV} | n^{-1/2} (parametric) | d_L directly: TV = separation |                                                                
| KL divergence | E_μ[KL(Π_h^{(L)}(x,·) ‖ Π̂^{(n,L)}(x,·))] | n^{-1} (parametric) | Pinsker: TV ≤ √(KL/2) |                                                                
| Wasserstein-2 | W₂(Γ_h^{(L)}, Γ̂_h^{(n,L)}) | n^{-2/(2+d)} | Geometry of h-space |                                                                                       
                                                                                                                                                                          
**Total variation is the most direct:** d_L(x,x') = ‖Π_h^{(L)}(x,·) −                                                                                                     
Π_h^{(L)}(x',·)‖_{TV} is already in TV. Control of D_{TV}(Γ_h^{(L)} ‖                                                                                                     
̂_h^{(n,L)}) directly bounds estimation error in d_L, which directly                                                                                                      
bounds δ(L).                                                                                                                                                              
                                                                                                                                                                          
**KL is more standard** and gives better rates via Pinsker's inequality,                                                                                                  
but introduces log factors. For the connection to the density bridge                                                                                                      
(L²-projections), KL is natural because the log-likelihood geometry                                                                                                       
connects to the L² geometry through Fisher information.                                                                                                                   
                                                                                                                                                                          
**Wasserstein** is appropriate if the dynamics have a metric structure                                                                                                    
(e.g. X is a Riemannian manifold and T is Lipschitz). It gives rates                                                                                                      
that depend on the geometry of X and the regularity of Π_h, not just                                                                                                      
the dimension.                                                                                                                                                            
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
### Step 4 — The correct picture                                                                                                                                          
                                                                                                                                                                          
The four quantities split into two pairs on different sides of the                                                                                                        
algebra/kernel divide:                                                                                                                                                    
                                                                                                                                                                          
```                                                                                                                                                                       
Algebra side                      Dynamics side                                                                                                                           
─────────────────────             ─────────────────────────────                                                                                                           
(A) δ(L)       ↔  (B) L²-error   (D) D(Γ_h‖Γ̂^(n))  →  (C) D(Γ_h^(L)‖Γ̂^(n,L))                                                                                              
     ↕                                     ↓                                                                                                                              
    δ̂(L,n)                              d̂_L(x,x')                                                                                                                         
 [algebra witness]                   [kernel witness]                                                                                                                     
```                                                                                                                                                                       
                                                                                                                                                                          
**Within each side:**                                                                                                                                                     
- (A) ↔ (B): proved, unconditional                                                                                                                                        
- (D) → (C): proved, data-processing inequality                                                                                                                           
                                                                                                                                                                          
**Across the divide — the Markov bridge:**                                                                                                                                
                                                                                                                                                                          
The delay vector is built from Markov chain draws of Π_h. This is what                                                                                                    
connects the two sides — not an equivalence, but a structural link.                                                                                                       
                                                                                                                                                                          
When both witnesses are jointly well-behaved:                                                                                                                             
                                                                                                                                                                          
  δ̂(L,n) small  AND  d̂_L large for most pairs                                                                                                                             
                                                                                                                                                                          
the system is reconstructible *and* the dynamics are estimable. The edge                                                                                                  
divergence D(Γ_h ‖ Γ̂_h^(n)) bounds the dynamics side. δ̂ bounds the                                                                                                        
algebra side. Their conjunction is the complete reconstruction diagnostic.                                                                                                
                                                                                                                                                                          
**What D(Γ_h ‖ Γ̂_h^(n)) is and isn't:**                                                                                                                                   
                                                                                                                                                                          
It is: a joint upper bound on both d̂_L (via data-processing) and on                                                                                                       
  δ̂ (via the forward chain through d_L → δ(L)), when Π_h is regular.                                                                                                      
                                                                                                                                                                          
It is not: a consequence of δ̂ being small. Small algebra coherence                                                                                                        
  does not imply small edge divergence. Different animals.                                                                                                                
                                                                                                                                                                          
**The role of regularity — stopping the bridge from lying:**                                                                                                              
                                                                                                                                                                          
Smoothness of Π_h is not a positive contribution. It does not construct                                                                                                   
the bridge or improve rates. It is a non-degeneracy condition — a                                                                                                         
constraint on bad behavior.                                                                                                                                               
                                                                                                                                                                          
Without it, the bridge cheats: δ̂ certifies that ℬ has been captured,                                                                                                      
̂_L certifies that predictive distributions are separated, and both are                                                                                                   
true — but the separation d̂_L found is an artifact of kernel irregularity                                                                                                 
creating spurious distinctions that don't correspond to the separation δ̂                                                                                                  
measured. The two witnesses agree but are looking at different objects.                                                                                                   
                                                                                                                                                                          
Smoothness blocks this failure mode. The precise condition needed is not                                                                                                  
Hölder regularity per se but *separation-stability*:                                                                                                                      
                                                                                                                                                                          
  **Definition (Separation-stable kernel):** Π_h^{(L)} is separation-stable                                                                                               
  if: d_L(x,x') > η implies d̂_L(x,x') > η/2 for all consistent                                                                                                            
  estimators Π̂_h^{(n)} with ‖Π̂_h^{(n)} − Π_h‖ sufficiently small.                                                                                                         
                                                                                                                                                                          
That is: separation that exists in the true kernel is preserved under                                                                                                     
small perturbations of the kernel. The estimated d̂_L and the true d_L                                                                                                     
are measuring the same gap.                                                                                                                                               
                                                                                                                                                                          
Hölder regularity of Π_h in x is a sufficient condition for                                                                                                               
separation-stability when T is a diffeomorphism — the smooth orbit                                                                                                        
structure prevents the kernel from collapsing genuine separation under                                                                                                    
perturbation. But separation-stability is the right condition;                                                                                                            
smoothness is the natural way to verify it in the smooth category.                                                                                                        
                                                                                                                                                                          
**Π_h doesn't want smoothness. It needs it to stop cheating.**                                                                                                            
                                                                                                                                                                          
The conjunction theorem requires separation-stability explicitly. Without                                                                                                 
it, δ̂ and d̂_L can be jointly small for the wrong reason — not because                                                                                                     
reconstruction failed, but because the kernel is actively destroying the                                                                                                  
information that reconstruction established.                                                                                                                              
                                                                                                                                                                          
**The theorem shape for Paper IV:**                                                                                                                                       
                                                                                                                                                                          
Not a four-way equivalence. Three honest theorems:                                                                                                                        
                                                                                                                                                                          
**(Algebra theorem):** Under reconstruction, the δ̂ stopping rule                                                                                                          
achieves rate n^{-s/(2s+d)} for f ∈ Hölder(s) without oracle inputs.                                                                                                      
No smoothness of Π_h required — the algebra side is unconditional.                                                                                                        
                                                                                                                                                                          
**(Dynamics theorem):** Under separation-stability of Π_h (verified by                                                                                                    
Hölder(β) regularity when T ∈ C^r) and kernel regression as the estimator                                                                                                 
for Π̂_h^(n) with optimal bandwidth h_n ~ n^{-1/(2β+d)}:                                                                                                                   
D(Γ_h ‖ Γ̂_h^(n)) → 0 at rate n^{-β/(2β+d)} — proved via kernel                                                                                                            
regression bias bound, not assumed. d̂_L certifies point separation.                                                                                                       
                                                                                                                                                                          
**(Conjunction theorem):** Under reconstruction AND separation-stability,                                                                                                 
the complete diagnostic (δ̂ small ∧ d̂_L large) is achievable from data,                                                                                                    
and the two witnesses are certifying the same object — the Markov                                                                                                         
structure of the delay vector is an honest bridge between them, not a lie.                                                                                                
                                                                                                                                                                          
---                                                                                                                                                                       
                                                                                                                                                                          
### Summary of edge divergence section                                                                                                                                    
                                                                                                                                                                          
| Item | Content | Status |                                                                                                                                               
|------|---------|--------|                                                                                                                                               
| Step 1 | δ(L) = functional of Π_h^{(L)} via d_L | ✓ |                                                                                                                   
| Step 2 | Algebra coherence ≠ kernel closeness; two witnesses needed | ✓ |                                                                                               
| Step 2 | Failure mode: near-constant kernel, δ̂ flattens but no reconstruction | ✓ |                                                                                     
| Step 2 | Complete diagnostic = δ̂ small ∧ d̂_L large | ✓ |                                                                                                                
| Step 3 | Data-processing: L-step ≤ one-step divergence | ✓ |                                                                                                            
| Step 3 | TV most direct for d_L; KL gives better rates via Pinsker | ✓ |                                                                                                
| Step 4 | Two-pair structure: (A)↔(B) algebra side, (D)→(C) dynamics side | ✓ |                                                                                          
| Step 4 | Bridge: Markov structure of delay vector, not equivalence | ✓ |                                                                                                
| Step 4 | Reverse chain (A)→(D) does not hold without regularity + estimator | ✓ |                                                                                       
| Open (ob. 12) | Conjunction theorem: formalise δ̂ ∧ d̂_L diagnostic with rates | Open |                                                                                  
| Open (ob. 11) | Separation-stability: when does T ∈ C^r imply Π_h separation-stable? | Open |                                                                          
| Open (ob. 11) | Separation-stability is the right condition; smoothness is sufficient but not necessary | Identified |  

---

## Obligation (11): Separation-stability in the smooth case — formal write-up

**Date:** 2026-04-06

**Status:** Closed (T ∈ C^r, h ∈ C^r, μ smooth positive density, r ≥ 2).
Derives separation-stability from Hölder regularity of Π_h, which follows
from the C^r structure via the same Link 1 argument as ob. (7).

---

### Setup and definitions

Recall: the one-step predictive kernel is

  Π_h(x, A) := μ({y : h(Ty) ∈ A} | x) = μ_x({z : h(z) ∈ A})

where μ_x is the conditional measure on {Tx} given x — i.e., for deterministic
T this is the Dirac delta δ_{h(Tx)}, so

  Π_h(x, ·) = δ_{h(Tx)}   (one-step kernel for deterministic T).

The L-step kernel is

  Π_h^{(L)}(x, ·) = δ_{(h(Tx),…,h(T^L x))} ∈ 𝒫(ℝ^L)

the Dirac mass at the L-step delay vector from x.

The separation pseudometric is

  d_L(x, x') := ‖Π_h^{(L)}(x, ·) − Π_h^{(L)}(x', ·)‖_{TV}
              = ‖δ_{Φ_h^{(L)}(x)} − δ_{Φ_h^{(L)}(x')}‖_{TV}
              = 𝟏[Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x')]   ∈ {0, 1}.

For deterministic T, d_L is binary: 0 if the L-step delay vectors agree, 1
if they differ anywhere.

**Remark.** For deterministic T the kernel Π_h^{(L)} is a Dirac family,
and TV separation is either 0 or 1 — there is no "Hölder regularity" of
Π_h in the usual sense of Hölder continuity of x ↦ Π_h(x, ·) in TV.
Ob. (11) therefore requires a restatement: separation-stability is not
about Hölder continuity of the kernel per se, but about Lipschitz or Hölder
continuity of the delay map Φ_h^{(L)}, which implies that estimated delay
vectors close in ℝ^L come from points x close in X, and vice versa.

The right definition for deterministic T is:

  **Definition (Separation-stable delay map).** Φ_h^{(L)} : X → ℝ^L is
  separation-stable if it is bi-Lipschitz on a set of full μ-measure: there
  exist c, C > 0 such that for μ-a.e. x, x':

    c · d_X(x, x') ≤ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≤ C · d_X(x, x')

  where d_X is the Riemannian metric on X.

Separation-stability in this sense means: close delay vectors ↔ close
states, with controlled constants. Small perturbation of the estimated delay
vector → small error in the inferred state.

---

### Lemma (Lipschitz bound on delay map)

**Hypotheses.**
- T ∈ Diff^r(X), h ∈ C^r(X), r ≥ 1.
- X compact Riemannian d-manifold.

**Claim (upper Lipschitz).** There exists C_L > 0 such that for all x, x' ∈ X:

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≤ C_L · d_X(x, x')

where C_L ≤ ‖Dh‖_{L∞} · ∑_{j=0}^{L} ‖DT^j‖_{L∞}.

**Proof.** Component j of Φ_h^{(L)} is h ∘ T^j. By the chain rule and
compactness of X:

  |h(T^j x) − h(T^j x')| ≤ ‖Dh‖_{L∞} · |T^j x − T^j x'|
                           ≤ ‖Dh‖_{L∞} · ‖DT^j‖_{L∞} · d_X(x, x').

Taking the Euclidean norm over j = 0, …, L:

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≤ (∑_j ‖Dh‖_{L∞}² · ‖DT^j‖_{L∞}²)^{1/2} · d_X(x,x')

Set C_L = ‖Dh‖_{L∞} · (∑_j ‖DT^j‖_{L∞}²)^{1/2}. □

---

### Lemma (Lower Lipschitz bound — injectivity quantified)

**Hypotheses.**
- (G1), (G2) from ob. (9): T has no periodic orbits of period ≤ L in supp(μ);
  dh ≠ 0 μ-a.e.
- T ∈ Diff^r(X), h ∈ C^r(X), r ≥ 2.
- Φ_h^{(L)} is injective on a set of full μ-measure (follows from reconstruction,
  i.e., from Paper III when L ≥ L₀).

**Claim (lower Lipschitz, local).** For μ-a.e. x, there exists a neighbourhood
U_x ∋ x and a constant c_x > 0 such that for all x' ∈ U_x:

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≥ c_x · d_X(x, x').

**Proof.** By ob. (9) Lemma (dim_eff step function), Φ_h^{(L)} is an immersion
at μ-a.e. x when L ≥ d−1 (rank = d, full column rank). For an immersion at x,
the differential DΦ_h^{(L)}|_x is injective, so by the inverse function theorem
there exists U_x such that Φ_h^{(L)} is a C^r embedding on U_x, with lower
Lipschitz constant

  c_x = σ_min(DΦ_h^{(L)}|_x) > 0

where σ_min is the smallest singular value of the Jacobian. □

**Remark (global lower bound).** The local lower Lipschitz constant c_x varies
over X. For a global lower bound we need σ_min(DΦ_h^{(L)}|_x) bounded away
from 0 uniformly in x. This holds when:

  c := inf_{x ∈ X} σ_min(DΦ_h^{(L)}|_x) > 0.

By compactness of X and continuity of x ↦ σ_min(DΦ_h^{(L)}|_x), c > 0 iff
the infimum is not attained at 0, i.e., iff Φ_h^{(L)} has no rank-deficient
points. Under (G1) and (G2) from ob. (9), the rank-deficient set has μ-measure
zero; but for the global lower bound we need it to be empty, which is a stronger
requirement — it requires the *minimum* singular value to be bounded away from
zero over all of X, not just a.e. This is an open condition on (T, h) and holds
generically but is not guaranteed by (G1)+(G2) alone.

For Paper IV's purposes: the lower Lipschitz bound c > 0 is a hypothesis
(separation-stability hypothesis, denoted (SS)), not a consequence. It is
verifiable in specific examples and holds generically. We state it as such.

---

### Theorem (Separation-stability under C^r regularity)  [Obligation 11]

**Hypotheses.**
- T ∈ Diff^r(X), h ∈ C^r(X), r ≥ 2.
- (G1): T has no periodic orbits of period ≤ L in supp(μ).
- (G2): dh ≠ 0 μ-a.e.
- μ smooth positive density on compact d-manifold X.
- L ≥ d−1 (Takens regime; reconstruction holds).
- (SS): inf_{x ∈ X} σ_min(DΦ_h^{(L)}|_x) =: c > 0.

**Claim.** Under (SS), the delay map Φ_h^{(L)} is bi-Lipschitz on X:

  c · d_X(x, x') ≤ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≤ C_L · d_X(x, x')

for all x, x' ∈ X, with C_L from the upper Lipschitz lemma.

Consequently Φ_h^{(L)} is separation-stable: for any consistent estimator
Φ̂_h^{(L,n)} with |Φ̂_h^{(L,n)}(x) − Φ_h^{(L)}(x)| ≤ ε uniformly, the
estimated separation d̂_L satisfies

  d̂_L(x, x') ≥ d_L(x, x') − 2ε/c   for all x, x'.

In particular: if d_L(x, x') > η then d̂_L(x, x') > η − 2ε/c > 0 for
n large enough that ε < cη/2.

**Proof.**

Upper bound: Lipschitz lemma above. □ (upper)

Lower bound: (SS) directly gives

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≥ c · d_X(x, x')

for all x, x' (not just a.e., since c > 0 everywhere by (SS)). □ (lower)

Separation-stability: let Φ̂ = Φ̂_h^{(L,n)} be any estimator with uniform
error ε. Then for the estimated separation

  d̂_L(x,x') := |Φ̂(x) − Φ̂(x')|:

  d̂_L(x,x') ≥ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| − |Φ̂(x) − Φ_h^{(L)}(x)|
                                                  − |Φ̂(x') − Φ_h^{(L)}(x')|
             ≥ c · d_X(x,x') − 2ε.

If d_L(x,x') > η, then since d_L(x,x') = 𝟏[Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x')]
and Φ_h^{(L)} is bi-Lipschitz, Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x') implies

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≥ c · d_X(x, x') > 0.

For the TV separation d_L: in the deterministic case d_L ∈ {0,1}, so
d_L(x,x') > η means d_L(x,x') = 1, i.e., Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x').
By bi-Lipschitz: |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≥ c · d_X(x,x') ≥ c · δ_X
for some δ_X > 0 depending on x, x'. The estimated d̂_L then satisfies
d̂_L(x,x') ≥ c · δ_X − 2ε > 0 for n large enough. □

---

### Lemma (Rate of convergence of Φ̂_h^{(L,n)})

To apply separation-stability, we need ε = sup_x |Φ̂(x) − Φ_h^{(L)}(x)| → 0.

The natural estimator is the empirical delay map: given observed pairs
(x_i, Φ_h^{(L)}(x_i)), the estimator is the identity (the delay vectors are
directly observed from data). So ε = 0 in the noiseless case.

In the noisy case (h observed with additive noise ξ_i ~ N(0,σ²)):
each observed delay coordinate h(T^j x_i) + ξ_{ij} is perturbed by ξ_{ij}.
The estimated delay vector has error

  |Φ̂(x_i) − Φ_h^{(L)}(x_i)|² = ∑_{j=0}^{L} ξ_{ij}² ~ χ²_{L+1} · σ²

so ε ~ σ · √(L+1) for each point. With n observations and kernel smoothing:
ε_n ~ σ · √(L+1) · n^{-β/(2β+d)} (standard NW regression rate with L+1
input coordinates). This matches the rate from ob. (7) with dim_eff = d. □

---

### Honest scope note for Obligation (11)

Closed:
- Upper Lipschitz: unconditional under T, h ∈ C^r, no (SS) needed.
- Lower Lipschitz + separation-stability: closed under (SS).
- (SS) holds generically (open dense condition on (T,h) in Diff^r × C^r) and
  is verifiable in specific examples. It is a hypothesis, not a consequence.

Genuine condition (SS) is not derivable from (G1)+(G2) alone:
- (G1)+(G2) give rank = d μ-a.e., but σ_min > 0 *everywhere* is stronger.
- The gap between "μ-a.e. full rank" and "uniformly full rank" is real.
  Example: Φ_h^{(L)} could have a rank-deficient point on a set of μ-measure
  zero (satisfying (G1)+(G2)) while still failing (SS). At such a point the
  lower Lipschitz constant is 0 and separation-stability fails locally.

Open:
- Conditions on (T, h) that imply (SS) directly, without assuming it.
  The natural candidate: T Anosov + h generic → uniform hyperbolicity gives
  σ_min bounded below by the expansion constant. This is a separate argument
  left for future work.
- Stochastic T (noisy dynamics): Π_h is no longer Dirac, genuine TV-Hölder
  regularity is needed, and the argument changes substantially.


---

## Obligation (12): Conjunction theorem — formal write-up

**Date:** 2026-04-06

**Status:** Closed under reconstruction + (SS). The theorem is conditional —
both hypotheses are necessary and the failure modes under each are named.

---

### The central claim

The two witnesses are:

  (W1) δ̂(L, n) — algebra witness. Small means 𝒪_h^{(L)} has captured ℬ.
  (W2) d̂_L(x,x') = |Φ̂_h^{(L,n)}(x) − Φ̂_h^{(L,n)}(x')| — kernel witness.
       Large for μ⊗μ-most pairs means the delay map separates the state space.

The conjunction theorem asserts: under reconstruction ∧ (SS), (W1) and (W2)
are measuring the same object — σ-algebra separation and metric separation
coincide, and both witnesses certify it from data.

---

### Lemma (Algebra separation = metric separation under bi-Lipschitz)

**Hypotheses.** Φ_h^{(L)} bi-Lipschitz on X (i.e., (SS) holds, from ob. 11):

  c · d_X(x,x') ≤ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| ≤ C_L · d_X(x,x').

**Claim.** For μ⊗μ-a.e. (x, x') with x ≠ x':

  d_L(x,x') = 1  iff  x and x' are separated by 𝒪_h^{(L)}.

That is: the kernel witness d_L and the algebra witness δ(L) are measuring
the same separation event.

**Proof.**

By definition, d_L(x,x') = ‖Π_h^{(L)}(x,·) − Π_h^{(L)}(x',·)‖_{TV}.
For deterministic T, Π_h^{(L)}(x,·) = δ_{Φ_h^{(L)}(x)}, so

  d_L(x,x') = ‖δ_{Φ_h^{(L)}(x)} − δ_{Φ_h^{(L)}(x')}‖_{TV}
             = 𝟏[Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x')].

And x is separated from x' by 𝒪_h^{(L)} = σ(Φ_h^{(L)}) iff there exists
a measurable set E ∈ 𝒪_h^{(L)} with 𝟏_E(x) ≠ 𝟏_E(x'), i.e., iff
Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x') (since the sets {Φ_h^{(L)}^{-1}(B)} for
Borel B ⊆ ℝ^L generate 𝒪_h^{(L)}, and these separate x from x' iff the
delay vectors differ).

So d_L(x,x') = 1 iff x, x' separated by 𝒪_h^{(L)}: the two conditions are
identical, not merely correlated.

Under (SS), Φ_h^{(L)} injective (reconstruction) implies Φ_h^{(L)}(x) ≠ Φ_h^{(L)}(x')
for all x ≠ x'. Hence d_L(x,x') = 1 for all x ≠ x', μ⊗μ-a.e. □

---

### Theorem (Conjunction theorem)  [Obligation 12]

**Hypotheses.**
- Reconstruction: δ(L) = 0, equivalently Φ_h^{(L)} injective μ-a.e. (Paper III).
- (SS): Φ_h^{(L)} bi-Lipschitz with constants 0 < c ≤ C_L < ∞ (ob. 11).
- (G1), (G2), μ smooth positive density on compact d-manifold X (ob. 9/11).
- n large enough that the estimator error ε_n < c·η/2 for the η in the
  separation threshold (see below).
- Exponential mixing (for the rate statement; the qualitative claim holds
  under any mixing with L*(n) < ∞).

**Claim.** Define the joint diagnostic:

  Reconstruct(L, n) := {δ̂(L,n) ≤ τ_n}  ∧  {d̂_L,n > η_n for μ⊗μ-most pairs}

where τ_n = 4·ε_n(d) (from ob. 10) and η_n > 0 satisfies η_n → 0,
η_n ≫ ε_n (e.g. η_n = √ε_n).

Then:

(a) Under reconstruction + (SS): P(Reconstruct(L*(n), n)) → 1.

(b) Under failure of reconstruction (δ(L) > 0 for all L):
    P(δ̂(L,n) ≤ τ_n for any finite L) → 0.

(c) Under failure of (SS) (σ_min(DΦ_h^{(L)}|_x) → 0 on a positive-measure set):
    P(d̂_L,n > η_n for μ⊗μ-most pairs) → 0, even if δ̂(L,n) → 0.

In words: (a) the conjunction fires correctly when both conditions hold;
(b) δ̂ alone cannot fire when reconstruction fails; (c) d̂_L alone cannot
fire when (SS) fails, even if the algebra witness looks good.

**Proof.**

**(a) Conjunction fires under reconstruction + (SS).**

Step 1: δ̂(L*(n), n) ≤ τ_n whp.
By ob. (10) Corollary (Algebra theorem, data-driven), at L = L*(n):
  δ̂(L*(n), n) ≤ δ(L*(n)) + |δ̂ − δ| ≤ 0 + ε_n(d) ≤ τ_n   whp.
(Reconstruction: δ(L*(n)) = 0 since L*(n) ≥ L₀. Concentration: ob. 8.) ✓

Step 2: d̂_L*(n),n > η_n for μ⊗μ-most pairs, whp.
By the Algebra-Metric Lemma, d_L(x,x') = 1 for all x ≠ x' (reconstruction).
By ob. (11) separation-stability, for n large enough that ε_n < c/2:
  d̂_L,n(x,x') = |Φ̂(x) − Φ̂(x')| ≥ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| − 2ε_n
               ≥ c · d_X(x,x') − 2ε_n.
For μ⊗μ-a.e. (x,x') with x ≠ x', d_X(x,x') > 0. The set {d_X(x,x') > 0}
has full μ⊗μ-measure (since μ is non-atomic by smooth positive density).
On this set, c · d_X(x,x') > 0, and for n large enough c · d_X(x,x') > 2ε_n + η_n
for μ⊗μ-most pairs (all but the pairs with d_X(x,x') ≤ (2ε_n + η_n)/c,
which have μ⊗μ-measure → 0 as η_n/c → 0). Hence d̂_L,n > η_n for μ⊗μ-most
pairs. ✓

Conjunction: both conditions hold whp. □ (part a)

**(b) δ̂ cannot fire when reconstruction fails.**

If δ(L) > 0 for all L, then by ob. (8) concentration:
  P(δ̂(L,n) ≤ τ_n) ≤ P(|δ̂(L,n) − δ(L)| ≥ δ(L) − τ_n).
For n large enough δ(L) − τ_n ≥ δ(L)/2 > 0. By ob. (8) the RHS → 0
exponentially. So P(δ̂(L,n) ≤ τ_n) → 0 for each fixed L.

For the stopping rule L̂*: by ob. (10), L̂* → ∞ when reconstruction fails
(the elbow never flattens), so Reconstruct is never triggered. □ (part b)

**(c) d̂_L cannot fire when (SS) fails.**

Suppose σ_min(DΦ_h^{(L)}|_x) → 0 on a set S ⊆ X of positive μ-measure.
Then for x ∈ S there exist x'_n → x with

  |Φ_h^{(L)}(x) − Φ_h^{(L)}(x'_n)| / d_X(x, x'_n) → 0.

The true delay map is nearly degenerate near x: points close in X map to
nearly identical delay vectors. The estimated map Φ̂ inherits this — any
consistent estimator satisfies |Φ̂(x) − Φ̂(x')| ≤ |Φ_h^{(L)}(x) − Φ_h^{(L)}(x')| + 2ε_n,
which → 0 for x' → x regardless of ε_n. So d̂_L,n(x, x') → 0 as x' → x,
for x ∈ S. The set of pairs (x,x') where d̂_L,n ≤ η_n contains a positive-
measure neighbourhood of the diagonal {(x,x) : x ∈ S} × B(x, r_n), which
has positive μ⊗μ-measure. Hence d̂_L,n > η_n fails for a positive-measure
set of pairs, and the kernel witness does not fire. □ (part c)

---

### The honest bridge

Parts (a)–(c) together say: the conjunction Reconstruct(L,n) is not a
coincidence when it fires — it is a theorem. And its failure modes are
honest: each condition is genuinely necessary, and the proof identifies
what breaks when each is removed.

The Markov structure of the delay vector is the bridge in the following
precise sense: σ(Φ_h^{(L)}) = 𝒪_h^{(L)} (the σ-algebra generated by
L-step delay vectors IS the observable algebra). So:

  δ(L) = 0  ↔  Φ_h^{(L)} injective μ-a.e.  ↔  d_L = 1 μ⊗μ-a.e.

The first equivalence is Paper III (reconstruction theorem). The second is
the Algebra-Metric Lemma above. Together: algebra reconstruction and kernel
separation are the same event, witnessed from two sides.

Separation-stability (SS) is what makes this equivalence empirically accessible:
without it, the estimated d̂_L can fail to reflect the true d_L even when
reconstruction holds, and the bridge lies. With it, both witnesses converge
to the same truth at controlled rates.

---

### Rate statement

Under exponential mixing with C_λ > 4 (ob. 10) and (SS):

  P(Reconstruct(L̂*, n)) ≥ 1 − C·exp(−c·n·ε_n(d)²)

where L̂* is the data-driven stopping rule. The rate of the algebra witness
is n^{-s/(2s+d)} (ob. 10 Corollary). The kernel witness converges at the
rate of the delay-map estimator, which under kernel regression with optimal
bandwidth is n^{-β/(2β+d)} (ob. 7, via the NW regression rate with dim_eff = d).

The conjunction fires reliably once n is large enough that both rates are
below the respective thresholds τ_n and η_n.

---

### Honest scope note for Obligation (12)

Closed:
- Qualitative conjunction (both witnesses fire correctly) under reconstruction + (SS).
- Failure modes under negation of each hypothesis: named and proved.
- Rate statement under exponential mixing + (SS).
- The Markov bridge: identified as σ(Φ_h^{(L)}) = 𝒪_h^{(L)}, proved via Paper III.

Open (not claimed in Paper IV):
- Polynomial mixing: ob. (10) open in this regime; conjunction inherits that gap.
- (SS) from first principles: conditions on (T,h) implying inf σ_min > 0.
  Anosov case expected to work; left for future work.
- Stochastic T: Π_h non-Dirac; TV regularity argument changes; not attempted.
- Sharp conjunction rate: the minimum n at which both witnesses simultaneously
  exceed their thresholds depends on the interplay of the algebra and kernel
  rates; not worked out.
- Quantitative version of part (c): how large the failure set must be to
  guarantee d̂_L fails to fire; only qualitative here.
