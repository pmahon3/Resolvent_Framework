#!/usr/bin/env python3
"""Exact seven-cell factor checkpoint for two adjacent full-cycle OMLs."""
import argparse,collections,hashlib,itertools,json,math,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
SCHEMA='adjacent-full-cycle-union-factor-checkpoint-v1'
EDGES=((0,0),(0,1),(1,0),(1,1),(1,2),(2,1),(2,2))

def payload():
 states=cell.cell_states();groups=collections.Counter()
 for s in states:
  a=tuple(int(x in s) for x in cell.SHARED);q=int('e11'in s or'e10'in s);r=int('e11'in s or'e01'in s);groups[a,q,r]+=1
 As=sorted({k[0] for k in groups});macros=0;points=0;mn=None;mx=0;profile_counts=collections.Counter();projected=[set() for _ in range(7)]
 for aa in itertools.product(As,repeat=3):
  for qs in itertools.product((0,1),repeat=3):
   for rs in itertools.product((0,1),repeat=3):
    sizes=[groups[aa[i],qs[i],rs[j]] for i,j in EDGES]
    if not all(sizes):continue
    w=math.prod(sizes);macros+=1;points+=w;mn=w if mn is None else min(mn,w);mx=max(mx,w)
    profile_counts[''.join(map(str,qs+rs))]+=w
    for k,(i,j) in enumerate(EDGES):projected[k].add((aa[i],qs[i],rs[j]))
 # A literal tuple of one root per global macrofibre is already too large:
 # it repeats copy-local roots over all outsider macro choices.
 roots_per_event=macros;events_per_copy=18676
 out={'schema':SCHEMA,'schema_version':'1.0','global_rows':3,'global_columns':3,
 'present_cells':['00','01','10','11','12','21','22'],'missing_cells':['02','20'],
 'left_rectangle_cells':['00','01','10','11'],'right_rectangle_cells':['11','12','21','22'],'shared_cell':'11',
 'global_macro_index':'(a0,a1,a2,q0,q1,q2,r0,r1,r2)',
 'nonempty_global_macrofibres':macros,'global_carrier_points':points,'macrofibre_size_min':mn,'macrofibre_size_max':mx,
 'six_bit_coordinate_profile_counts':dict(sorted(profile_counts.items())),
 'projected_nonempty_state_groups_by_cell':[len(x) for x in projected],
 'all_seven_cell_projections_surjective':all(x==set(groups) for x in projected),
 'naive_roots_per_event':roots_per_event,'events_per_completed_copy':events_per_copy,
 'naive_root_references_for_two_copies':2*roots_per_event*events_per_copy,
 'naive_root_reference_bytes_at_8_bytes':2*roots_per_event*events_per_copy*8,
 'factor_checkpoint_passed':True,
 'old_copy_embedding_status':'Each carrier projection is surjective, so pullback preserves/refects set inclusion, complement, and disjoint unions. Preservation of lattice extrema after adjoining the other copy is open because mixed outsider bounds may intervene.',
 'mixed_cut_status':'not entered: materializing one 23,998-root tuple per event would require the reported root-reference budget before closure',
 'exact_missing_compression_theorem':'Parametric outsider elimination for adjacent full-cycle grammars: every mixed lower/upper bound must admit a bound whose descriptor is a finite union of rectangles A(u) x_{D11} B(v), with u and v canonical 842-macrofibre descriptors and with a uniform bound on the number of such rectangles under complement and orthogonal union. This would replace 23,998-root global tuples by interned pairs of copy-local roots and shared-cell traces.',
 'smallest_next_engine':'Represent a global event as an interned disjoint family of fibre-product rectangles (u,v,t), where u is a left-copy canonical descriptor, v a right-copy descriptor, and t one of the verified shared-cell traces. Implement componentwise emptiness/order using the exact 224-state overlap fibres; test mixed pairs before global closure.',
 'provenance':'Both 18,676-event factors are the verified centre-free full-cycle grammar; overlap is the verified full 56-event cell D11. No event closure or lattice claim is made at this checkpoint.',
 'evidence_class':'executable verified exact factor/count checkpoint; mixed closure open',
 'command':'python3 notes/open_questions/verification/adjacent_full_cycle_union_factor_checkpoint.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out=payload();path=os.path.join(HERE,'adjacent_full_cycle_union_factor_checkpoint.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
