#!/usr/bin/env python3
"""Exact completed-grammar intersection on the one-cell rectangle overlap."""
import argparse,hashlib,json,os,struct,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_grid_four_cell_mdd_closure as grammar
import full_grid_terminal_split_one_cell_quotient as one
import sharedq_kcell_completion_audit as cell
SCHEMA='full-cycle-adjacent-rectangle-intersection-v1'

def capture_grammar():
 # Instrument a private in-memory copy at one source point; unlike sys.settrace
 # this adds no per-line overhead and does not edit the banked producer.
 src=open(grammar.__file__).read();needle=" out={'schema':SCHEMA"
 assert src.count(needle)==1
 src=src.replace(needle," global _CAPTURE;_CAPTURE=locals().copy()\n out={'schema':SCHEMA")
 ns={'__file__':grammar.__file__,'__name__':'_adjacent_capture_grammar'}
 exec(compile(src,grammar.__file__,'exec'),ns);receipt=ns['payload'](25000,1000000);box=ns['_CAPTURE']
 assert receipt['closure_completed'] and receipt['lattice'],(receipt['closure_completed'],receipt['stop_reason'],receipt['lattice'],receipt['interned_mdd_nodes'])
 return receipt,box

def payload():
 base,b=capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 event_roots={ev:root for root,ev in b['root_to_event'].items()}
 def trace_if_saturated(ev,pos):
  roots=event_roots[ev];truth={}
  for m,(_,ds) in enumerate(macros):
   eng=engines[m];root=roots[m]
   if root>1:
    v,ch=eng.nodes[root]
    if v!=pos or any(z>1 for z in ch):return None
   for i,s in enumerate(ds[pos]):
    z=root if root<=1 else ch[i]
    if s in truth and truth[s]!=z:return None
    truth[s]=z
  if len(truth)!=len(states):return None
  return sum(1<<s for s,v in truth.items() if v)
 def family(pos):
  out={}
  for idx,e in enumerate(events):
   t=trace_if_saturated(e,pos)
   if t is not None:out.setdefault(t,[]).append(idx)
  return out
 left=family(3);right=family(0);common=set(left)&set(right)
 local=one.local_event_predicates(states);extras=sorted(common-local,key=lambda x:(x.bit_count(),x))
 def thash(t):return hashlib.sha256(t.to_bytes(28,'little')).hexdigest()
 def provenance(t,side):
  fam=left if side=='R_position11' else right;ans=[]
  for idx in fam[t][:4]:
   p,f=events[idx];raw=b''.join(struct.pack('<I',z) for z in p)+struct.pack('<I',f)
   ans.append({'event_index':idx,'full17_hex':hex(f),'partial_root_tuple_sha256':hashlib.sha256(raw).hexdigest()})
  return ans
 extra_records=[{'trace_points':x.bit_count(),'trace_sha256':thash(x),'R_provenance':provenance(x,'R_position11'),'S_provenance':provenance(x,'S_position00')} for x in extras[:16]]
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
 'orientation_R':'shared global D11 is local position11; node6 split source remains local D00 and is not shared',
 'orientation_S':'reoriented rectangle rows {1,2}, columns {1,2}; shared global D11 is local position00, so the node6 split source lies in the shared cell; state labels are identified literally with no q/r or activation permutation',
 'completed_events_each':len(events),'R_position11_saturated_trace_count':len(left),'S_position00_saturated_trace_count':len(right),
 'common_saturated_trace_count':len(common),'shared_cell_trace_count':len(local),'common_equals_56_event_shared_cell':common==local,
 'R_contains_all_shared_cell_traces':local<=set(left),'S_contains_all_shared_cell_traces':local<=set(right),
 'extra_common_trace_count':len(extras),'smallest_extra_common_traces':extra_records,
 'intersection_theorem':('The two completed grammar pullbacks intersect exactly in the 56-event shared conditional cell.' if common==local else 'The completed grammar intersection strictly exceeds the 56-event shared cell; the serialized smallest common trace is an explicit coherence obstruction.'),
 'proof_method':'For each closed event and each macrofibre, reduced-MDD restriction to the shared coordinate must leave a terminal root. Truth values are then checked for equality across every occurrence of each of the 224 shared states. Surjective fibre-product pullbacks are equal exactly when these traces are equal.',
 'evidence_class':'executable verified exhaustive over all completed events and macrofibres',
 'command':'python3 notes/open_questions/verification/full_cycle_adjacent_rectangle_intersection.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out=payload();path=os.path.join(HERE,'full_cycle_adjacent_rectangle_intersection.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
