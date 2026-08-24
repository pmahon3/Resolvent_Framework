#!/usr/bin/env python3
"""Exact 2x2 grid audit for four incompatible-H4 conditional cells.

Rows share (a1,a2,a3,q); columns share r.  The carrier is the full compatible
fibre product of the 224 single-cell two-valued states.  Sets are represented
as Python integer bitsets.  Macro-block generation is exact (not sampled).

This script intentionally reports a first lattice failure if concrete
complement/disjoint-union closure does not produce an OML.  No infinite claim.
"""
import argparse, hashlib, json, os, sys
from itertools import combinations, product

HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as base

SCHEMA="full-grid-2x2-conditional-cell-v1"
CELLS=((0,0),(0,1),(1,0),(1,1))

def ar(st): return tuple(int(a in st) for a in base.SHARED)
def qr(st):
    return (int("e11" in st or "e10" in st),
            int("e11" in st or "e01" in st))

def repeat_pattern(bits,n,inner,outer):
    """Truth bits on n choices, each expanded inner and whole block outer."""
    unit=0
    ones=(1<<inner)-1
    for j,b in enumerate(bits):
        if b: unit |= ones << (j*inner)
    width=n*inner
    out=0
    for t in range(outer): out |= unit << (t*width)
    return out

def build():
    states=base.cell_states()
    groups={}
    for j,s in enumerate(states):
        a=ar(s); q,r=qr(s)
        groups.setdefault((a,q,r),[]).append(j)
    atom_bases=sorted({x for b in base.CELL_BLOCKS for x in b})
    masks={(c,x):0 for c in CELLS for x in atom_bases}
    offset=0; macro=[]
    # tuple order: cell 00,01,10,11; last coordinate fastest.
    for a0,a1,q0,q1,r0,r1 in product(product((0,1),repeat=3),
                                             product((0,1),repeat=3),
                                             (0,1),(0,1),(0,1),(0,1)):
        lists=[groups.get((a0,q0,r0),[]),groups.get((a0,q0,r1),[]),
               groups.get((a1,q1,r0),[]),groups.get((a1,q1,r1),[])]
        ns=[len(x) for x in lists]
        size=ns[0]*ns[1]*ns[2]*ns[3]
        if not size: continue
        macro.append((a0,a1,q0,q1,r0,r1,ns,size))
        for ci,c in enumerate(CELLS):
            inner=1
            for z in ns[ci+1:]: inner*=z
            outer=1
            for z in ns[:ci]: outer*=z
            for atom in atom_bases:
                bits=[int(atom in states[s]) for s in lists[ci]]
                masks[c,atom] |= repeat_pattern(bits,ns[ci],inner,outer)<<offset
        offset += size
    full=(1<<offset)-1
    raw={0,full}; labels={0:"0",full:"1"}; declared=[]
    for c in CELLS:
        for block in base.CELL_BLOCKS:
            declared.append(tuple((c,a) for a in block))
            for z in range(1,1<<len(block)):
                e=0; names=[]
                for j,a in enumerate(block):
                    if z>>j&1: e|=masks[c,a]; names.append(f"{a}@{c[0]}{c[1]}")
                raw.add(e); labels.setdefault(e,"+".join(names))
    # Interface identifications are semantic equality of pulled-back events.
    interfaces={}
    for row in (0,1):
        for a in base.SHARED:
            interfaces[f"row{row}:{a}"]=masks[(row,0),a]==masks[(row,1),a]
        for name,atoms in (("q",("e11","e10")),):
            interfaces[f"row{row}:{name}"]=(masks[(row,0),atoms[0]]|masks[(row,0),atoms[1]])==(masks[(row,1),atoms[0]]|masks[(row,1),atoms[1]])
    for col in (0,1):
        interfaces[f"col{col}:r"]=(masks[(0,col),"e11"]|masks[(0,col),"e01"])==(masks[(1,col),"e11"]|masks[(1,col),"e01"])
    return states,offset,full,masks,raw,labels,interfaces,macro

def closure(raw,full):
    ev=set(raw); rounds=[]
    while True:
        new={full^x for x in ev}-ev; snap=sorted(ev)
        for j,x in enumerate(snap):
            for y in snap[j+1:]:
                if not x&y and x|y not in ev: new.add(x|y)
        rounds.append(len(new))
        if not new:return sorted(ev),rounds
        ev|=new

def order_tables(ev):
    """Bit-indexed principal up/down sets; pays each huge-set comparison once."""
    up=[0]*len(ev); down=[0]*len(ev)
    for i,x in enumerate(ev):
        for j,y in enumerate(ev):
            if x|y==y: up[i]|=1<<j; down[j]|=1<<i
    return up,down

def extrema_indices(up,down,i,j):
    common_up=up[i]&up[j]; common_down=down[i]&down[j]
    mu=[z for z in range(len(up)) if common_up>>z&1 and down[z]&common_up==1<<z]
    ml=[z for z in range(len(up)) if common_down>>z&1 and up[z]&common_down==1<<z]
    return mu,ml

def digest_set(x,n):
    return hashlib.sha256(x.to_bytes((n+7)//8,"little")).hexdigest()

def audit():
    states,n,full,masks,raw,labels,interfaces,macro=build()
    ev,rounds=closure(raw,full); failures=[]; joins={}; meets={}
    up,down=order_tables(ev)
    for i,x in enumerate(ev):
        for j in range(i,len(ev)):
            y=ev[j]; mu_i,ml_i=extrema_indices(up,down,i,j)
            mu=[ev[z] for z in mu_i];ml=[ev[z] for z in ml_i]
            if len(mu)!=1 or len(ml)!=1:
                failures.append((x,y,mu,ml)); break
            joins[x,y]=joins[y,x]=mu[0]; meets[x,y]=meets[y,x]=ml[0]
        if failures: break
    fail=None
    if failures:
        x,y,mu,ml=failures[0]
        fail={"x_label":labels.get(x),"y_label":labels.get(y),
              "x_sha256":digest_set(x,n),"y_sha256":digest_set(y,n),
              "minimal_upper_bounds":[digest_set(z,n) for z in mu],
              "minimal_upper_bound_labels":[labels.get(z) for z in mu],
              "maximal_lower_bounds":[digest_set(z,n) for z in ml],
              "maximal_lower_bound_labels":[labels.get(z) for z in ml],
              "minimal_upper_bound_count":len(mu),"maximal_lower_bound_count":len(ml)}
    lattice=not failures
    oml=lattice and all(joins[meets[y,full^x],x]==y for x in ev for y in ev if x|y==y)
    # Raw cell projections: by carrier definition every compatible local state
    # occurs; compute the exact five-bit relation independently from cell states.
    relation=sorted({ar(s)+(qr(s)[0],qr(s)[1]) for s in states})
    expected=sorted(set(product((0,1),repeat=5))-{(1,1,1,0,1),(1,1,1,1,0)})
    macro_profiles={(a0,a1,q0,q1,r0,r1) for a0,a1,q0,q1,r0,r1,_,_ in macro}
    expected_macro={(a0,a1,q0,q1,r0,r1)
                    for a0,a1 in product(product((0,1),repeat=3),repeat=2)
                    for q0,q1,r0,r1 in product((0,1),repeat=4)
                    if (a0!=(1,1,1) or q0==r0==r1)
                    and (a1!=(1,1,1) or q1==r0==r1)}
    cylinders=[]
    for row in (0,1):
        c=full
        for a in base.SHARED: c &= masks[(row,0),a]
        cylinders.append(c)
    activation_checks={
        "macro_relation_exactly_intended_four_edges":macro_profiles==expected_macro,
        "both_rows_activated_joint_q0_q1_r0_r1":[list(z) for z in sorted({(q0,q1,r0,r1)
            for a0,a1,q0,q1,r0,r1 in macro_profiles
            if a0==(1,1,1) and a1==(1,1,1)})],
        "activation_cylinders_are_not_events":[c not in set(ev) for c in cylinders],
        "every_nonzero_event_has_off_cylinder_point":[
            all(x & (full^c) for x in ev if x) for c in cylinders],
    }
    return {"schema":SCHEMA,"carrier_points":n,"macro_blocks":len(macro),
            "single_cell_states":len(states),"raw_events":len(raw),
            "completed_events":len(ev),"closure_rounds":rounds,
            "interfaces_identified":interfaces,"lattice":lattice,
            "orthomodular":oml,"first_lattice_failure":fail,
            "each_cell_relation_is_exact_30_profile_relation":relation==expected,
            "activation_checks":activation_checks,
            "scope":"one exhaustive finite 2x2 compatible-state fibre; no arbitrary-grid or infinite promotion"}

def canonical(p): return json.dumps(p,sort_keys=True,indent=2)+"\n"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");args=ap.parse_args()
    p=audit(); p["payload_sha256"]=hashlib.sha256(canonical(p).encode()).hexdigest()
    path=os.path.join(HERE,"full_grid_2x2_conditional_cell.json")
    if args.emit: open(path,"w").write(canonical(p))
    elif os.path.exists(path): assert json.load(open(path))==p
    print(canonical(p),end="")
if __name__=="__main__":main()
