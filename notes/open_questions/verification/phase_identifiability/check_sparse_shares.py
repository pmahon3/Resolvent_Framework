# population V for exchangeable Dirichlet shares with small alpha: does V ever exceed 0 as kappa->inf?
import numpy as np, importlib.util, sys
sp=importlib.util.spec_from_file_location("s","share_total_sweep.py")
src=open("share_total_sweep.py").read().split("print(\"closed form")[0]
exec(src)
for n,al in ((10,0.1),(10,0.5),(10,1.0),(5,0.2),(5,0.3)):
    a=n*al; R=pop_levels(np.ones(n)*al,1e8)
    print(n,al,"a(n-2)-n=%.2f"%(a*(n-2)-n),"rho_inf=%.4f"%R[0,1],"1/(n-1)=%.4f"%(1/(n-1)),"V_inf=%.4f"%V(R))
