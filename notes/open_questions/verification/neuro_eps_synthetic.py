# Synthetic gate (pre-registered in notes/open_questions/neuro_critical/SYNTHETIC_GATE.md).
import numpy as np
rng=np.random.default_rng(7)
dt=0.01; N=300_000; sig=1.0
lam=np.linspace(1.0,0.02,N)                       # approach to critical point
def simulate(K):
    x=np.zeros((N,3)); 
    for t in range(1,N):
        x[t]=x[t-1]+(-lam[t]*x[t-1]+K@x[t-1])*dt+sig*np.sqrt(dt)*rng.standard_normal(3)
    return x
def dis(a,b): return np.mean(np.sign(a)!=np.sign(b))
def eps_star(dab,dbc,dca):
    V=max(0,dca-dab-dbc,dab-dbc-dca,dbc-dab-dca,dab+dbc+dca-2); return V/3
def table(a,b):
    sa,sb=a>0,b>0; return np.array([np.mean(sa&sb),np.mean(sa&~sb),np.mean(~sa&sb),np.mean(~sa&~sb)])
W=6000; D=W//2; starts=range(0,N-W-2*D,D)
def analyse(name,K):
    x=simulate(K); rows=[]
    for s in starts:
        w0=slice(s,s+W); w1=slice(s+D,s+D+W); w2=slice(s+2*D,s+2*D+W)
        e=eps_star(dis(x[w0,0],x[w0,1]),dis(x[w1,1],x[w1,2]),dis(x[w2,2],x[w2,0]))
        v=np.var(x[w0,0]); a=np.corrcoef(x[w0,0][:-1],x[w0,0][1:])[0,1]
        drift=0.5*np.abs(table(x[w0,0],x[w0,1])-table(x[w1,0],x[w1,1])).sum()
        # simultaneous-window eps* (control: a joint exists, should be 0)
        e_sim=eps_star(dis(x[w0,0],x[w0,1]),dis(x[w0,1],x[w0,2]),dis(x[w0,2],x[w0,0]))
        rows.append((s*dt,lam[s],e,e_sim,v,a,drift))
    R=np.array(rows)
    e,esim,v,a,dr=R[:,2],R[:,3],R[:,4],R[:,5],R[:,6]
    def onset(series):   # first time series exceeds baseline mean + 3 sd (baseline = first 20%)
        nb=max(5,len(series)//5); m,sd=series[:nb].mean(),series[:nb].std()+1e-12
        idx=np.where(series>m+3*sd)[0]; return R[idx[0],1] if len(idx) else None
    c=np.corrcoef(e,dr)[0,1] if e.std()>0 else float('nan')
    print(f"[{name}] max eps*(staggered)={e.max():.4f}  max eps*(simultaneous)={esim.max():.4f}  "
          f"corr(eps*,drift)={c:.2f}")
    print(f"   alarm at lambda: eps*={onset(e)}  variance={onset(v)}  AC1={onset(a)}  drift={onset(dr)}")
J=0.3
Ka=np.array([[0,J,J],[J,0,J],[J,J,0]])                     # all excitatory
Kb=np.array([[0,J,-J],[J,0,J],[-J,J,0]])                    # frustrated: inhibitory 1-3 link
analyse("a: excitatory",Ka); analyse("b: frustrated",Kb)

# Replication over seeds: alarm lambda (higher = earlier warning) per indicator
import io, contextlib
def alarms(K,seed):
    global rng; rng=np.random.default_rng(seed)
    x=simulate(K); E=[];Vv=[];A=[];Dr=[];L=[]
    for s in starts:
        w0=slice(s,s+W); w1=slice(s+D,s+D+W); w2=slice(s+2*D,s+2*D+W)
        E.append(eps_star(dis(x[w0,0],x[w0,1]),dis(x[w1,1],x[w1,2]),dis(x[w2,2],x[w2,0])))
        Vv.append(np.var(x[w0,0])); A.append(np.corrcoef(x[w0,0][:-1],x[w0,0][1:])[0,1])
        Dr.append(0.5*np.abs(table(x[w0,0],x[w0,1])-table(x[w1,0],x[w1,1])).sum()); L.append(lam[s])
    L=np.array(L)
    def on(sr):
        sr=np.array(sr); nb=max(5,len(sr)//5); m,sd=sr[:nb].mean(),sr[:nb].std()+1e-12
        i=np.where(sr>m+3*sd)[0]; return L[i[0]] if len(i) else 0.0
    return on(E),on(Vv),on(A),on(Dr)
for name,K in (("a: excitatory",Ka),("b: frustrated",Kb)):
    res=np.array([alarms(K,s) for s in range(10)])
    earlier=np.mean(res[:,0]>=np.maximum(res[:,1],res[:,2]))
    print(f"[{name}] mean alarm lambda  eps*={res[:,0].mean():.2f} var={res[:,1].mean():.2f} AC1={res[:,2].mean():.2f} drift={res[:,3].mean():.2f}"
          f"  | eps* earliest in {earlier*100:.0f}% of seeds")
