#!/usr/bin/env python3
"""B1/B2 check for WHY_SIDECAR E1. x_i = s_i*T, s~Dirichlet(alpha), T>0 independent.
V = rho(|R-I|)-1 (Perron root of entrywise |R-I|; the V_G=V_2 of VG_TEST_VALIDATION.md, Run-2 definition).
Population: exact moments. Sample: Monte Carlo (N obs), plain-percentile bootstrap size/power not run (statistic only).
Usage: python3 -I share_total_sweep.py"""
import numpy as np
from scipy.special import polygamma
rng = np.random.default_rng(1)
def V(R): 
    A = np.abs(R-np.eye(len(R))); return float(np.max(np.abs(np.linalg.eigvalsh(A))))-1
def pop_levels(alpha, kappa, mu=1.0):
    a=alpha.sum(); n=len(alpha); ET2=mu**2*(1+kappa)
    Ess=np.outer(alpha,alpha)/(a*(a+1)); np.fill_diagonal(Ess, alpha*(alpha+1)/(a*(a+1)))
    C=ET2*Ess-mu**2*np.outer(alpha,alpha)/a**2; d=np.sqrt(np.diag(C)); return C/np.outer(d,d)
def pop_logs(alpha, v):
    a=alpha.sum(); C=-polygamma(1,a)*np.ones((len(alpha),)*2)+np.diag(polygamma(1,alpha))+v
    d=np.sqrt(np.diag(C)); return C/np.outer(d,d)
def sample(alpha, kappa, N, logs=False):
    s=rng.dirichlet(alpha,N); s2=np.log1p(kappa)  # lognormal T, mean 1, CV^2=kappa
    T=np.exp(rng.normal(-s2/2,np.sqrt(s2),N)); x=s*T[:,None]
    return np.corrcoef((np.log(x) if logs else x).T)
print("closed form check: rho_levels=(k a-1)/(k(a+n)+n-1), exchangeable")
for n in (5,10):
    alpha=np.ones(n)*1.0; a=alpha.sum()
    print(f"\n=== n={n}, alpha=1 each (a={a:.0f}); population sign change at kappa=1/a={1/a:.3f}; V>0 needs rho>1/(n-1)={1/(n-1):.3f}")
    print("kappa   rho_pop  closed   V_pop   | sample N=60: meanV  frac(V>0)  | N=400: meanV frac(V>0)")
    for k in (0,0.02,0.05,0.1,0.2,0.3,0.5,1,2,5,20):
        R=pop_levels(alpha,k); rho=R[0,1]; cf=(k*a-1)/(k*(a+n)+n-1)
        out=[]
        for N in (60,400):
            vs=np.array([V(sample(alpha,k,N)) for _ in range(300)]); out+= [vs.mean(), (vs>0).mean()]
        print(f"{k:5.2f} {rho:8.3f} {cf:8.3f} {V(R):8.3f}  | {out[0]:7.3f} {out[1]:6.2f}  | {out[2]:7.3f} {out[3]:6.2f}")
    print("logs: Var(log T)=v : rho_pop, V_pop (threshold v=psi'(a)=%.3f)"%polygamma(1,a))
    for v in (0,0.1,0.2,0.4,0.8,1.6,3.2):
        R=pop_logs(alpha,v); print(f"  v={v:4.2f} rho={R[0,1]:7.3f} V={V(R):7.3f}")
# heterogeneous alpha, levels: signs of population correlations
alpha=np.array([0.3,0.5,1,2,4.]); print("\nheterogeneous alpha n=5: kappa, #negative pairs of 10, antibalanced?, V")
import itertools
for k in (0,0.05,0.1,0.2,0.5,1,5):
    R=pop_levels(alpha,k); neg=sum(R[i,j]<0 for i,j in itertools.combinations(range(5),2))
    # antibalanced iff every triangle has product of off-diag signs negative
    ab=all(np.sign(R[i,j]*R[j,l]*R[i,l])<0 for i,j,l in itertools.combinations(range(5),3))
    print(f"  k={k:4.2f} neg={neg} antibalanced={ab} V={V(R):.3f}")
