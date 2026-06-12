# Scratch: Is Clop(Y) σ-complete? (Argyros 1983 pre-Gleason)

## Verified construction (Argyros 1983, §1.0–1.2, §2.4, §2.10)

- As a SET, Y = {0,1}^ω.
- 𝔗 = topology with SUBBASE: (a) all usual-product clopens, (b) {V_Σ : Σ ∈ 𝚺},
  𝚺 = all branches of tree T. V_Σ = ∏_{s∈Σ} K_s × {0,1}^{ω∖∪Σ},
  K_s = anti-diagonal ⊂ {0,1}^s (2 points, |s|=2).
- 𝔗 ⊇ usual topology (finer). Each V_Σ is usual-CLOSED ⟹ 𝔗-clopen.
- Basic 𝔗-clopen: V = U ∩ ⋂_{j=1}^k V_{Σ_j}, U usual-clopen, Σ_j branches.
- §2.10(a): each V_Σ (infinite branch) = ⋂_n U^n (countable DECREASING
  intersection of usual-clopens), U^n = ∏_{s∈Σ∩T_n} K_s × {rest}.

## Key topological facts to pin down

FACT A. The usual (product) topology and 𝔗 agree on which sets are
usual-clopen: every usual-clopen is 𝔗-clopen. 𝔗 adds the V_Σ as new
clopens (they were usual-closed, not usual-open).

FACT B (Y not compact). Y with 𝔗 is completely regular Hausdorff but NOT
compact (the V_Σ refine away compactness — e.g. the usual-compact Y is
covered by 𝔗-opens with no finite subcover along a branch). X = βY.

## The candidate non-σ-complete witness

Take an INFINITE branch Σ. Then:
  V_Σ = ⋂_n U^n_Σ,  U^n_Σ usual-clopen, decreasing.
Complement:
  C_Σ := Y ∖ V_Σ = ⋃_n W_n,  W_n := Y ∖ U^n_Σ usual-clopen (increasing).
Each W_n is 𝔗-clopen. {W_n} is an increasing sequence of clopens.
Question: does sup_n W_n exist in Clop(Y), and if so does it equal C_Σ?

C_Σ is 𝔗-clopen (since V_Σ is). So C_Σ ∈ Clop(Y) and C_Σ ⊇ each W_n,
i.e. C_Σ is AN upper bound. Is it the LEAST upper bound?

The set-theoretic union ⋃_n W_n = C_Σ exactly (since ⋂U^n = V_Σ). So
C_Σ is the set-union. In a Boolean algebra of sets, IF the set-union is
in the algebra, it is automatically the supremum. So sup_n W_n = C_Σ
EXISTS in Clop(Y).

⟹ THIS family does NOT witness non-σ-completeness. The sup exists.

## Reframe: where can σ-completeness actually fail?

σ-completeness of Clop(Y) fails iff there is a countable family {A_i} ⊂
Clop(Y) with NO supremum in Clop(Y). For SET algebras, sup of {A_i}
exists and = ⋃A_i whenever ⋃A_i ∈ Clop(Y). When ⋃A_i ∉ Clop(Y), the
sup MAY still exist (as a smaller-than-closure clopen) or may fail.

Standard Stone-space picture: in St(B), sup of countable {a_i} exists
iff cl_{St(B)}(⋃ â_i) is clopen (open), where â_i = clopen in St(B).
Equivalently (Loomis–Sikorski / Sikorski): B σ-complete ⟺ St(B)
basically disconnected ⟺ closure of every (cl)open Fσ (= cozero) is open.

So I must work in St(Clop Y), NOT in Y. The join of clopens A_i is
controlled by closure in the STONE SPACE, which is generally LARGER than
Y (Y embeds as a dense subspace of St(Clop Y) only if Y is compact; here
Y is not compact, St(Clop Y) = the "Banaschewski"/zero-dim compactification
β₀Y of Y).

## The real question

Is β₀Y basically disconnected? I.e., for every cozero set G of β₀Y, is
cl(G) open? Equivalently (Boolean): for every countable {A_i} ⊂ Clop(Y),
the "ideal-sup" exists as a clopen.

Cozero sets of a Stone space St(B) = countable unions of clopens
(= the σ-ideal-generated open sets). cl of a countable union ⋃ Â_i of
clopens is open iff there is a LEAST clopen ⊇ all A_i.

## Candidate FAILURE family (the right one)

I need a countable family {A_i} of 𝔗-clopens of Y such that NO 𝔗-clopen
is the least upper bound. Least-upper-bound in Clop(Y): a clopen D ⊇ all
A_i such that any clopen D' ⊇ all A_i has D ⊆ D'.

Intuition from tree algebras: take clopens "filling up" toward a
branch-limit so that the only clopen upper bounds must OVERSHOOT by a
V_Σ-amount, with no least one. Need to find a countable family whose
upper bounds form a downward-directed set with no minimum.
