"""Directly verify: lift the D-closed-walk 0->1->0->2->0 (length 4, revisits 0
twice in D) onto R_4(rho). Is the lifted walk simple (all (layer,state) pairs
distinct)? The k=1 remark claims YES always, because each step also advances
layer, so revisits in D land at DIFFERENT layers and can't collide."""
walk_D = [0,1,0,2,0]  # positions 0..4, closes 0->0 length 4
L = 4
lifted = [(i % L, walk_D[i]) for i in range(4)]  # positions 0,1,2,3 (drop closing dup)
print("Lifted walk (layer,state):", lifted)
print("All distinct?", len(set(lifted)) == len(lifted))

# Now also stress with an even more adverse D-closed-walk: many revisits packed
# into few layers is impossible by Lemma 0 (each step forces layer+1 mod L),
# so within one full traversal (length L) each layer occurs EXACTLY once,
# hence no two of the L positions can coincide regardless of what D does.
# This is just Lemma 0, tautologically. Try L=6 with a long messy D-walk:
walk_D2 = [0,1,0,1,0,1,0]  # length 6 closed walk in a 2-cycle graph, k=1 test at L=6
L2 = 6
lifted2 = [(i % L2, walk_D2[i]) for i in range(6)]
print("Lifted walk 2:", lifted2, "distinct?", len(set(lifted2))==len(lifted2))
