#!/usr/bin/env python3
"""One-leaf opposite-witness provenance discriminator.

Enumerate every exact opposite event in the same universal-mask class for the
six sampled leaves of the actual-event shadow audit.  Retain all events whose
existential mask is inclusion-minimal among admissible witnesses, stratify by
(E, physical-root hash, event index), and choose the leaf with the largest
number of exact-root strata.  Replace only that leaf's canonical witness by
the lexicographically last distinct stratum, rerun the exact actual-event
quotient, and compare universal-shadow and old-kernel outcome digests.
"""
import argparse,collections,hashlib,json,os,sys,time
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter
SCHEMA='adjacent-full-cycle-opposite-witness-diversity-v1'
BASE_SCRIPT=os.path.join(HERE,'adjacent_full_cycle_actual_event_shadow.py')
BASE_RECEIPT=os.path.join(HERE,'adjacent_full_cycle_actual_event_shadow.json')
OLD="B,EB=wits[A][U]"
NEW="B=OVERRIDE.get((name,A,U),wits[A][U][0]);EB=opclasses[B][0]"
def payload():
 start=time.perf_counter();baseline=json.load(open(BASE_RECEIPT))
 assert baseline['producer_sha256']==hashlib.sha256(open(BASE_SCRIPT,'rb').read()).hexdigest()
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};N=len(states)
 occ=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occ[pos][s].append((m,i))
 cache={}
 def status(m,r,pos,i):
  k=(m,r,pos,i)
  if k in cache:return cache[k]
  if r<=1:z=r
  else:
   v,ch=engines[m].nodes[r]
   if v==pos:z=status(m,ch[i],pos,i)
   else:q={status(m,x,pos,i) for x in ch};z=q.pop() if len(q)==1 else 2
  cache[k]=z;return z
 def classify(pos):
  out=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,os in enumerate(occ[pos]):
    vals=[status(m,rr[m],pos,i) for m,i in os]
    if any(vals):E|=1<<s
    if all(x==1 for x in vals):U|=1<<s
   out.append((E,U))
  return out
 left=classify(3);right=classify(0)
 def rhash(rr):
  import struct
  return hashlib.sha256(b''.join(struct.pack('<I',x) for x in rr)).hexdigest()
 leaves=[]
 for rec in baseline['orientation_records']:
  name=rec['orientation'];ret=left if name.startswith('left') else right
  opp=right if name.startswith('left') else left
  for lr in rec['exact_leaf_witness_records']:
   A=lr['retained_event_index'];U=int(lr['witness_U_hex'],16);canonical=lr['opposite_event_index'];EA=ret[A][0]
   candidates=[i for i,(E,V) in enumerate(opp) if V==U and not EA&E]
   minimal_E=sorted({opp[i][0] for i in candidates
    if not any(opp[j][0]!=opp[i][0] and not opp[j][0]&~opp[i][0] for j in candidates)})
   mins=[i for i in candidates if opp[i][0] in minimal_E]
   reps={}
   for i in mins:
    key=(opp[i][0],rhash(roots[events[i]]));reps[key]=min(i,reps.get(key,i))
   strata=sorted((E.bit_count(),E,h,i) for (E,h),i in reps.items())
   assert any(i==canonical for *_,i in strata)
   leaves.append({'orientation':name,'retained_event_index':A,'U':U,'canonical':canonical,
    'candidate_count':len(candidates),'minimal_E_count':len(minimal_E),
    'minimal_exact_root_strata_count':len(strata),'strata':strata})
 # Exact simultaneous six-bit opposite pattern vectors.  Equality under a
 # one-slot substitution proves invariance of every Boolean term in the fixed
 # six-generator quotient, so a full semantic rerun is needed only on the
 # first vector divergence.
 pcache={}
 def patterns(m,rs,pos,i):
  key=(m,rs,pos,i)
  if key in pcache:return pcache[key]
  if all(r<=1 for r in rs):ans=frozenset((sum((r&1)<<k for k,r in enumerate(rs)),))
  else:
   v=min(engines[m].nodes[r][0] for r in rs if r>1)
   if v==pos:
    nxt=tuple(engines[m].nodes[r][1][i] if r>1 and engines[m].nodes[r][0]==v else r for r in rs)
    ans=patterns(m,nxt,pos,i)
   else:
    ans=set()
    for q in range(len(engines[m].domains[v])):
     nxt=tuple(engines[m].nodes[r][1][q] if r>1 and engines[m].nodes[r][0]==v else r for r in rs)
     ans.update(patterns(m,nxt,pos,i))
    ans=frozenset(ans)
  pcache[key]=ans;return ans
 def pattern_vector(indices,pos):
  out=[]
  for s in range(N):
   vals=set()
   for m,i in occ[pos][s]:vals.update(patterns(m,tuple(roots[events[e]][m] for e in indices),pos,i))
   out.append(tuple(sorted(vals)))
  return tuple(out)
 def vhash(v):return hashlib.sha256(repr(v).encode()).hexdigest()
 pattern_tests=[];first_pattern=None
 for name in ('left_retained_position11','right_retained_position00'):
  slots=[x for x in leaves if x['orientation']==name];canon=[x['canonical'] for x in slots]
  pos=0 if name.startswith('left') else 3;basevec=pattern_vector(canon,pos);basehash=vhash(basevec)
  for slot,x in enumerate(slots):
   for *_,alternate in x['strata']:
    if alternate==x['canonical']:continue
    variant=list(canon);variant[slot]=alternate;vh=vhash(pattern_vector(variant,pos))
    rec={'orientation':name,'leaf_slot':slot,'retained_event_index':x['retained_event_index'],
     'U_hex':hex(x['U']),'canonical_opposite_event_index':x['canonical'],
     'alternate_opposite_event_index':alternate,'baseline_pattern_vector_sha256':basehash,
     'variant_pattern_vector_sha256':vh,'joint_pattern_divergence':vh!=basehash}
    pattern_tests.append(rec)
    if rec['joint_pattern_divergence'] and first_pattern is None:first_pattern=rec
 src=open(BASE_SCRIPT).read();assert src.count(OLD)==1;transformed=src.replace(OLD,NEW)
 def outcomes(d,name):
  r=next(x for x in d['orientation_records'] if x['orientation']==name)
  return {'actual_shadow_table_chained_digest_sha256':r['actual_shadow_table_chained_digest_sha256'],
   'full_mismatch_chained_digest_sha256':r['full_mismatch_chained_digest_sha256'],
   'provenance_chained_digest_sha256':r['provenance_chained_digest_sha256'],
   'actual_kernel_bad_terms':r['actual_kernel_bad_terms'],
   'coordinate_kernel_bad_terms':r['coordinate_kernel_bad_terms'],
   'universal_shadow_mismatches':r['universal_shadow_mismatches']}
 inner_seconds=0;semantic=None
 if first_pattern:
  override={(first_pattern['orientation'],first_pattern['retained_event_index'],int(first_pattern['U_hex'],16)):
   first_pattern['alternate_opposite_event_index']}
  ns={'__file__':BASE_SCRIPT,'__name__':'embedded_witness_variant','OVERRIDE':override}
  exec(compile(transformed,BASE_SCRIPT,'exec'),ns);variant,inner_seconds=ns['payload']()
  bo=outcomes(baseline,first_pattern['orientation']);vo=outcomes(variant,first_pattern['orientation'])
  shadow_div=bo['actual_shadow_table_chained_digest_sha256']!=vo['actual_shadow_table_chained_digest_sha256']
  outcome_digest_div=bo['full_mismatch_chained_digest_sha256']!=vo['full_mismatch_chained_digest_sha256']
  bad_count_div=bo['actual_kernel_bad_terms']!=vo['actual_kernel_bad_terms']
  semantic={'baseline_outcomes':bo,'variant_outcomes':vo,'universal_shadow_divergence':shadow_div,
   'audited_term_outcome_digest_divergence':outcome_digest_div,
   'actual_kernel_bad_count_divergence':bad_count_div,
   'variant_has_bad_actual_kernel':vo['actual_kernel_bad_terms']>0}
 shadow_div=bool(semantic and semantic['universal_shadow_divergence'])
 outcome_digest_div=bool(semantic and semantic['audited_term_outcome_digest_divergence'])
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'baseline_actual_event_payload_sha256':baseline['payload_sha256'],
  'baseline_actual_event_source_sha256':baseline['producer_sha256'],
  'transformed_source_sha256':hashlib.sha256(transformed.encode()).hexdigest(),
  'all_leaf_witness_class_summaries':[{
   'orientation':x['orientation'],'retained_event_index':x['retained_event_index'],'U_hex':hex(x['U']),
   'canonical_event_index':x['canonical'],'candidate_count':x['candidate_count'],
   'minimal_E_count':x['minimal_E_count'],'minimal_exact_root_strata_count':x['minimal_exact_root_strata_count'],
   'strata_digest_sha256':hashlib.sha256(repr(x['strata']).encode()).hexdigest()} for x in leaves],
  'simultaneous_six_bit_pattern_tests':pattern_tests,
  'simultaneous_pattern_test_count':len(pattern_tests),
  'simultaneous_pattern_divergence_count':sum(x['joint_pattern_divergence'] for x in pattern_tests),
  'simultaneous_pattern_cache_entries':len(pcache),
  'first_joint_pattern_divergence':first_pattern,
  'semantic_rerun':semantic,
  'universal_shadow_divergence':shadow_div,
  'audited_term_outcome_digest_divergence':outcome_digest_div,
  'actual_kernel_bad_count_divergence':bool(semantic and semantic['actual_kernel_bad_count_divergence']),
  'variant_has_bad_actual_kernel':bool(semantic and semantic['variant_has_bad_actual_kernel']),
  'stop_reason':('bad actual kernel' if semantic and semantic['variant_has_bad_actual_kernel'] else
   'same-(E,U) universal-shadow/audited-term divergence' if shadow_div or outcome_digest_div else
   'joint pattern divergence without tested-term outcome divergence' if first_pattern else
   'all single-slot minimal exact-root substitutions preserve the full six-bit pattern vector'),
  'scope':'Every single-slot substitution by a structurally distinct inclusion-minimal exact-root witness across all 12 sampled leaf slots. Equality proves invariance for every Boolean term in each fixed six-generator quotient, but not simultaneous multi-slot substitutions, other leaves, or full mixed closure.',
  'verification_independence':'Single wrapper; enumeration independently reconstructs exact E/U classes, while variant semantics reuse a source-transformed audited actual-event producer.',
  'evidence_classes':['Executable verified bounded evidence'],
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_witness_diversity.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start,inner_seconds
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out,seconds,inner=payload();path=os.path.join(HERE,'adjacent_full_cycle_witness_diversity.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'stop_reason':out['stop_reason'],
  'universal_shadow_divergence':out['universal_shadow_divergence'],'bad_actual_kernel':out['variant_has_bad_actual_kernel'],
  'runtime_seconds':round(seconds,3),'inner_runtime_seconds':round(inner,3)},sort_keys=True))
