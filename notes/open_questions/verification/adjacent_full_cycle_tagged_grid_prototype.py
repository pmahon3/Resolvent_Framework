#!/usr/bin/env python3
"""Bounded tagged atom-grid prototype using exact existential/universal types."""
import argparse,hashlib,json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import adjacent_full_cycle_boolean_envelope_shadow as shadow
SCHEMA='adjacent-full-cycle-tagged-grid-prototype-v1'

def capture():
 src=open(shadow.__file__).read();needle=" out={'schema':SCHEMA";assert src.count(needle)==1
 src=src.replace(needle," global _CAPTURE;_CAPTURE=locals().copy()\n out={'schema':SCHEMA")
 ns={'__file__':shadow.__file__,'__name__':'_tagged_shadow_capture'};exec(compile(src,shadow.__file__,'exec'),ns)
 out=ns['payload']();return out,ns['_CAPTURE']

def payload():
 base,b=capture();L,R=b['L'],b['R'];ALL=b['ALL']
 counts={'shared_saturated_shape':0,'left_cylinder_shaped_only':0,'right_cylinder_shaped_only':0,'both_cylinder_shaped_not_saturated':0,'genuinely_mixed_shape':0}
 typecounts={k:0 for k in counts};pairs=0;types=0;firstmixed=None
 for A,nA in sorted(L.items()):
  EA,UA=A;PA=EA&~UA
  for B,nB in sorted(R.items()):
   EB,UB=B
   if EA&EB:continue
   PB=EB&~UB;types+=1;w=nA*nB;pairs+=w
   left=not(PB&~UA);right=not(PA&~UB)
   saturated=not((EA|EB)&~(UA|UB))
   if saturated:k='shared_saturated_shape'
   elif left and right:k='both_cylinder_shaped_not_saturated'
   elif left:k='left_cylinder_shaped_only'
   elif right:k='right_cylinder_shaped_only'
   else:k='genuinely_mixed_shape'
   counts[k]+=w;typecounts[k]+=1
   if k=='genuinely_mixed_shape' and firstmixed is None:
    h=lambda x:hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
    firstmixed={'left_E_sha256':h(EA),'left_U_sha256':h(UA),'right_E_sha256':h(EB),'right_U_sha256':h(UB),
      'left_type_multiplicity':nA,'right_type_multiplicity':nB,'partial_left_states':PA.bit_count(),'partial_right_states':PB.bit_count()}
 out={'schema':SCHEMA,'schema_version':'1.0','base_shadow_payload_sha256':base['payload_sha256'],
 'disjoint_event_pairs':pairs,'disjoint_shadow_type_pairs':types,'event_pair_locality_counts':counts,'shadow_type_pair_locality_counts':typecounts,
 'first_genuinely_mixed_shadow_descriptor':firstmixed,
 'classification_exact_at_shadow_level':True,
 'hostile_scope_correction':'Cylinder-shaped means independence from the opposite atom-grid coordinate. It does not assert membership in either old 18,676-event family. Shared-saturated shape likewise does not assert that the 224-state trace is one of the 56 shared-cell events.',
 'classification_proof':'Disjointness is EA intersect EB empty. The union is independent of the right atom iff no shared state has B partial while A is nonuniversal; dually for left. It is shared-saturated iff every nonempty state fibre is universal.',
 'tagged_descriptor':'A first-round union is tagged by its exact left event and right event; on shared state s its atom grid is (A_s x all q_s) union (all p_s x B_s). No grid cells are materialized.',
 'complement_operation':'Complement of a row/column union is the rectangle (A_s^c x B_s^c). Therefore union tags are not complement-closed; the exact next grammar must include both OR-tags and AND-rectangle tags.',
 'pairwise_disjoint_union_operation':'Two tagged grid subsets can be tested by distributivity into four symbolic intersections of their local restricted MDD roots. This prototype does not serialize those per-state roots, so second-round exact closure is not claimed.',
 'exact_deduplication_status':'open: existential/universal shadows classify locality but do not identify partial atom subsets. Exact deduplication requires a canonical per-event vector of 224 restricted local-MDD root hashes.',
 'first_obstruction':'The first-round OR-tag class is not closed under complement; complements introduce genuine product rectangles. Shadow equality is too coarse to deduplicate those rectangles.',
 'smallest_next_test':'Serialize canonical restricted-root vectors for the 18,676 events at positions 11 and 00; intern OR and AND tags modulo per-state MDD equality, then close only the distinct tags under complement and disjoint union.',
 'scope':'Exact census of event-pair disjointness and cylinder shape from exact shadows; old-local membership, shared-cell membership, exact event deduplication, and mixed closure are not tested.',
 'evidence_class':'executable verified symbolic shadow-type census',
 'command':'python3 notes/open_questions/verification/adjacent_full_cycle_tagged_grid_prototype.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out=payload();path=os.path.join(HERE,'adjacent_full_cycle_tagged_grid_prototype.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
