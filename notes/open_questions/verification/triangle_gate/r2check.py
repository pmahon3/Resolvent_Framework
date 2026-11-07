exec(open('kform.py').read().split("print('|D|'")[0])
print('R2 closed under complement:', all((m^FULL) in D for m in D))
Q=Uclose(W|Ks); print('Q complements outside Q:', sum((m^FULL) not in Q for m in Q))
