"""Generate the Lean proof that a tensor-type triangle family's functional is {0,1} on D3
(TriangleCyclic.lean, layer 3). Input: family name, coefficients over the 13 ordered-partition placements,
and a minimal list of boxes (index 6-tuples into e0..e7). Output: Lean text on stdout.
Boxes come from notes/open_questions/verification (minimal-box search); 2026-10-17."""
import sys, itertools, json
def otype(x):
    vals=sorted(set(x)); return tuple(tuple(i for i in range(3) if x[i]==v) for v in vals)
NAME={((0,),(1,),(2,)):'o012',((1,),(2,),(0,)):'o120',((2,),(0,),(1,)):'o201',((0,),(2,),(1,)):'o021',
      ((2,),(1,),(0,)):'o210',((1,),(0,),(2,)):'o102',((0,1),(2,)):'t01_2',((2,),(0,1)):'t2_01',
      ((0,),(1,2)):'t0_12',((1,2),(0,)):'t12_0',((0,2),(1,)):'t02_1',((1,),(0,2)):'t1_02',((0,1,2),):'t012'}
ORDER=['o012','o120','o201','o021','o210','o102','t01_2','t2_01','t0_12','t12_0','t02_1','t1_02','t012']
def gen(fname, coeffs, boxes):
    E=lambda i: f"e{chr(0x2080+i)}"
    out=[]
    terms=" ".join((("+ " if c>0 else "- ")+("" if abs(c)==1 else f"{abs(c)} * ")+f"Wv p {n} E") for n,c in coeffs.items())
    terms=terms[2:] if terms.startswith("+ ") else "-"+terms[1:]
    out.append(f"/-- Functional of the family `{fname}`. -/\nnoncomputable def s_{fname} (p : Ultrafilter ℕ) (E : Set Ω) : ℤ := {terms}\n")
    out.append(f"theorem s_{fname}_mem {{E : Set Ω}} (hE : D₃.Has E) : s_{fname} p E = 0 ∨ s_{fname} p E = 1 := by")
    out.append("  by_contra hne")
    out.append("  obtain ⟨P, hP, "+", ".join("H"+n for n in ORDER)+"⟩ := homog13 hp E")
    out.append("  obtain ⟨e₀, e₁, e₂, e₃, e₄, e₅, e₆, e₇, m₀, m₁, m₂, m₃, m₄, m₅, m₆, m₇, l₀, l₁, l₂, l₃, l₄, l₅, l₆⟩ := eight P hP")
    out.append("  have hB := box_of_mem hE")
    eqs=[]; hyps=[]; corner_seen={}
    for bi,(a,a2,b,b2,c,c2) in enumerate(boxes):
        plus=[(a,b,c),(a2,b2,c),(a2,b,c2),(a,b2,c2)]; minus=[(a2,b,c),(a,b2,c),(a,b,c2),(a2,b2,c2)]
        lit=lambda x: "!["+", ".join(E(i) for i in x)+"]"
        for x in plus+minus:
            if x in corner_seen: continue
            t=otype(x); n=NAME[t]
            vals=sorted(set(x)); args=vals+[6,7][:3-len(vals)]
            k=f"k{len(corner_seen)}"; corner_seen[x]=k
            u,v,w=args
            out.append(f"  have {k} := cnt_wv (x := {lit(x)}) (H{n} {E(u)} m{chr(0x2080+u)} {E(v)} m{chr(0x2080+v)} {E(w)} m{chr(0x2080+w)} (by omega) (by omega))")
        out.append(f"  have b{bi} := hB {E(a)} {E(a2)} {E(b)} {E(b2)} {E(c)} {E(c2)}")
        lhs=" + ".join(f"(cnt E {lit(x)} : ℤ)" for x in plus); rhs=" + ".join(f"(cnt E {lit(x)} : ℤ)" for x in minus)
        out.append(f"  have b{bi}' : {lhs} = {rhs} := by exact_mod_cast b{bi}")
        hyps.append(f"b{bi}'")
    ks=", ".join(corner_seen.values())
    out.append(f"  simp only [{ks}] at {' '.join(hyps)}")
    for n in ORDER: out.append(f"  have w_{n} : 0 ≤ Wv p {n} E ∧ Wv p {n} E ≤ 1 := by\n    rcases wv_cases p {n} E with h | h <;> rw [h] <;> norm_num")
    out.append(f"  simp only [s_{fname}] at hne")
    out.append("  have hpat : (Wv p o012 E = 1 ∧ Wv p o120 E = 1 ∧ Wv p o201 E = 1 ∧ Wv p o021 E = 0 ∧\n      Wv p o210 E = 0 ∧ Wv p o102 E = 0) ∨ (Wv p o012 E = 0 ∧ Wv p o120 E = 0 ∧\n      Wv p o201 E = 0 ∧ Wv p o021 E = 1 ∧ Wv p o210 E = 1 ∧ Wv p o102 E = 1) := by")
    hl=" ".join(hyps+[f"w_{n}" for n in ORDER]+["hne"])
    out.append("    clear "+" ".join(list(corner_seen.values())+[f"b{i}" for i in range(len(boxes))]+["hB"]))
    for i,n in enumerate(ORDER):
        out.append(f"    generalize Wv p {n} E = A{i} at {hl} ⊢")
    out.append("    omega")
    out.append("  exact not_inP_of_mem hE (inP_of_strict hP Ho012 Ho120 Ho201 Ho021 Ho210 Ho102 hpat)\n")
    return "\n".join(out)
if __name__=='__main__':
    spec=json.loads(sys.argv[1])
    print(gen(spec['name'], spec['coeffs'], [tuple(b) for b in spec['boxes']]))
