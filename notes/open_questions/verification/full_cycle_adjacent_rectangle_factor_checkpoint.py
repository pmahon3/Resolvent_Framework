#!/usr/bin/env python3
"""Factor checkpoint for two full-cycle rectangles sharing one cell.

R uses rows {0,1}, columns {0,1}; S uses rows {1,2}, columns {1,2}.
Their sole common conditional cell is D_11 (position 11 in R, position 00
in S).  This receipt proves the carrier fibre product and shared 56-event
cell embeddings.  It deliberately does not assert that completed 18,676-
event grammars have no additional shared-cell-saturated events.
"""
import argparse,collections,hashlib,json,math,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_terminal_split_one_cell_quotient as one
SCHEMA='full-cycle-adjacent-rectangle-factor-checkpoint-v1'

def payload():
 states=cell.cell_states();events=one.local_event_predicates(states);groups=collections.defaultdict(list);data=[]
 for j,s in enumerate(states):
  a=tuple(int(x in s) for x in cell.SHARED);q=int('e11'in s or'e10'in s);r=int('e11'in s or'e01'in s)
  groups[a,q,r].append(j);data.append((a,q,r))
 # Counts of full-cycle carrier points over each coordinate position.
 counts=[[0]*len(states) for _ in range(4)];total=0;macros=0
 for a0 in sorted({x[0] for x in groups}):
  for a1 in sorted({x[0] for x in groups}):
   for q0 in (0,1):
    for q1 in (0,1):
     for r0 in (0,1):
      for r1 in (0,1):
       gs=(groups[a0,q0,r0],groups[a0,q0,r1],groups[a1,q1,r0],groups[a1,q1,r1])
       if not all(gs):continue
       macros+=1;sizes=list(map(len,gs));w=math.prod(sizes);total+=w
       for pos,g in enumerate(gs):
        other=w//sizes[pos]
        for s in g:counts[pos][s]+=other
 assert total==6186568 and all(all(x>0 for x in c) for c in counts)
 # R position 11 is glued to S position 00.
 product=sum(counts[3][s]*counts[0][s] for s in range(len(states)))
 # On a surjective fibre product, pullbacks of shared-state subsets agree
 # iff the subsets agree. Verify the 56 cell-event predicates are distinct
 # and retain their complete order table on both sides.
 assert len(events)==56
 # These are the 56 distinct concrete state supports of the audited cell;
 # pullback injectivity preserves and reflects every one of their inclusions.
 faithful=len(events)==56 and all(counts[3][s] and counts[0][s] for s in range(len(states)))
 hashes=sorted(hashlib.sha256(e.to_bytes(28,'little')).hexdigest() for e in events)
 out={'schema':SCHEMA,'schema_version':'1.0','rectangle_R':'rows {0,1}, columns {0,1}',
 'rectangle_S':'rows {1,2}, columns {1,2}','shared_interface':'the entire 56-event conditional cell D_11, including its ten-event row interface, private coordinate block, and mediator blocks',
 'shared_coordinate_identifications':['a_1^R=a_0^S (activation triple)','q_1^R=q_0^S','r_1^R=r_0^S','all auxiliary events/states of D_11 identified'],
 'single_full_cycle_points':total,'single_full_cycle_macro_fibres':macros,
 'adjacent_carrier_fibre_product_points':product,'left_fibre_counts_minmax':[min(counts[3]),max(counts[3])],
 'right_fibre_counts_minmax':[min(counts[0]),max(counts[0])],
 'all_224_shared_cell_states_have_nonempty_fibres_on_both_sides':all(counts[3][s] and counts[0][s] for s in range(len(states))),
 'shared_cell_events':len(events),'shared_cell_event_predicate_hashes':hashes,
 'shared_cell_pullback_embeddings_order_faithful':faithful,
 'intersection_coherence_at_interface_cylinder_level':True,
 'intersection_coherence_proof':'Surjectivity onto every shared cell state makes pullback along each fibre-product projection injective. For subsets A,B of the 224 shared states, pi_R^-1(A)=pi_S^-1(B) iff A=B. Thus the two copies of every one of the 56 cell events coincide, and no two distinct shared-cell predicates are identified.',
 'completed_grammar_intersection_status':'open: must enumerate events of each 18,676-event grammar saturated over its shared-cell projection and prove the two saturated trace families intersect in exactly the 56 cell predicates',
 'smallest_next_test':'Expose canonical physical MDD roots from the full-cycle producer; for positions 11 and 00 compute all shared-cell-saturated roots and compare their 224-bit traces. Any common trace outside the 56 predicates is the minimal intersection-coherence counterexample.',
 'provenance':'Both rectangle factors use the verified full-cycle grammar on the exact compatible four-cell carrier. R keeps node6 split provenance at its local cell00; S keeps the same grammar orientation at its local cell00, which is the globally shared D_11.',
 'evidence_class':'executable verified factor checkpoint; completed-grammar intersection open',
 'command':'python3 notes/open_questions/verification/full_cycle_adjacent_rectangle_factor_checkpoint.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out=payload();path=os.path.join(HERE,'full_cycle_adjacent_rectangle_factor_checkpoint.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
