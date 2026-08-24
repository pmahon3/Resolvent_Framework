#!/usr/bin/env python3
"""Exact one-old-context extensions of the ARR-CYL 16-event control."""
import argparse, collections, hashlib, json, os, struct, time

HERE=os.path.dirname(os.path.abspath(__file__))
SOURCE=os.path.join(HERE,"arr_cyl_critical_sublattice_pilot.py")
SOURCE_RECEIPT=os.path.join(HERE,"arr_cyl_critical_sublattice_pilot.json")
SCHEMA="arr-cyl-one-context-extensions-v1"
GUARD=100000

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def payload():
 start=time.perf_counter();src=open(SOURCE).read();needle="    source=json.load(open(SOURCE_RECEIPT));ar_source=json.load(open(AR_RECEIPT))";assert src.count(needle)==1
 src=src.replace(needle,"    globals()['_ONE_CTX']={'bank':bank,'arr':arr,'K':K,'patterns':patterns,'occ':occ,'left_shared':left_shared,'right_shared':right_shared}\n"+needle)
 ns={"__file__":SOURCE,"__name__":"_one_context_instrumented"};exec(compile(src,SOURCE,"exec"),ns);ns["payload"]();d=ns["_ONE_CTX"]
 bank,arr,K,patterns,occ=d["bank"],d["arr"],d["K"],d["patterns"],d["occ"]
 events,macros,engines=bank["all_events"],bank["macros"],bank["engines"]
 roots={ev:r for r,ev in bank["root_to_event"].items()};root_index={roots[e]:i for i,e in enumerate(events)}
 def op(k,x,y):return tuple(engines[m].app(k,a,b) for m,(a,b) in enumerate(zip(x,y)))
 def neg(x):return tuple(engines[m].neg(a) for m,a in enumerate(x))
 zero=tuple(0 for _ in macros);comp={i:root_index[neg(roots[e])] for i,e in enumerate(events)}
 def dis(i,j):return op(0,roots[events[i]],roots[events[j]])==zero

 # Three mandated contexts plus minimum nontrivial shared representatives of
 # every available disjointness type against the two maximal lowers.
 mandatory=[10752,18322,18331];chosen=[];seen=set()
 def add(i,label):
  key=min(i,comp[i])
  if key not in seen:seen.add(key);chosen.append((key,label))
 for i in mandatory:
  pair=sorted((i,comp[i]));add(i,"mandatory_pair_"+str(pair[0])+"_"+str(pair[1]))
 shared_by_type={}
 for i in sorted(d["right_shared"].values()):
  if i in (0,18431):continue
  typ=(dis(i,15250),dis(i,16786));shared_by_type.setdefault(typ,i)
 for typ,i in sorted(shared_by_type.items()):add(i,"shared_disjoint_type_"+str(typ))
 chosen=chosen[:8];contexts=tuple(i for i,_ in chosen)

 def vector(indices,pos):
  out=[]
  for s in range(224):
   vals=set()
   for m,q in occ[pos][s]:vals.update(patterns(m,tuple(roots[events[e]][m] for e in indices),pos,q))
   out.append(tuple(sorted(vals)))
  return out
 LI=tuple(arr["retained"])+K+contexts;RI=tuple(arr["opposite"])+K+contexts
 LP=vector(LI,arr["pos"]);RP=vector(RI,arr["oppos"]);nk=len(K);nc=len(contexts)
 words=set()
 for s in range(224):
  for l in LP[s]:
   a=l&63;tail=l>>6;lk=tail&((1<<nk)-1);lc=tail>>nk
   for r in RP[s]:
    b=r&63;tailr=r>>6;rk=tailr&((1<<nk)-1);rc=tailr>>nk;u=(arr["F"]>>(a|(b<<6)))&1
    words.add((lk,lc,rk,rc,u))
 words=tuple(sorted(words));N=len(words);ALL=(1<<N)-1;kpos={e:j for j,e in enumerate(K)}
 def mask(field,bit):return sum(1<<q for q,w in enumerate(words) if w[field]>>bit&1)
 LM=[mask(0,j) for j in range(nk)];RM=[mask(2,j) for j in range(nk)]
 LCM=[mask(1,j) for j in range(nc)];RCM=[mask(3,j) for j in range(nc)];U=sum(1<<q for q,w in enumerate(words) if w[4])
 lo1,lo2=RM[kpos[15250]],RM[kpos[16786]];literal=lo1|lo2
 def close(initial):
  fam=set(initial)|{0,ALL};front=list(fam);rounds=[];guard=False
  while front:
   snap=sorted(fam);add=set()
   for x in sorted(front):
    add.add(ALL^x)
    for y in snap:
     if not x&y:add.add(x|y)
   add-=fam
   if len(fam)+len(add)>GUARD:guard=True;break
   rounds.append(len(add));fam|=add;front=list(add)
  return fam,rounds,guard
 def audit(fam):
  xs=sorted(fam);meet={};join={};lattice=True;first_failed=None
  def mh(x):return hashlib.sha256(x.to_bytes((N+7)//8,"little")).hexdigest()
  for x in xs:
   for y in xs:
    lows=[z for z in xs if not z&~x and not z&~y];gl=[z for z in lows if not any(z!=w and not z&~w for w in lows)]
    ups=[z for z in xs if not x&~z and not y&~z];lu=[z for z in ups if not any(z!=w and not w&~z for w in ups)]
    if len(gl)!=1 or len(lu)!=1:
     lattice=False
     if first_failed is None:first_failed={"left_mask_sha256":mh(x),"right_mask_sha256":mh(y),"maximal_lower_count":len(gl),"maximal_lower_sha256":[mh(z) for z in gl],"minimal_upper_count":len(lu),"minimal_upper_sha256":[mh(z) for z in lu]}
    else:meet[(x,y)]=gl[0];join[(x,y)]=lu[0]
  om=False;centre=[]
  if lattice:
   om=all(join[(x,meet[(y,ALL^x)])]==y for x in xs for y in xs if not x&~y)
   centre=[c for c in xs if all(join[(meet[(x,c)],meet[(x,ALL^c)])]==x for x in xs)]
  ups=[x for x in xs if not (lo1|lo2)&~x];mins=[x for x in ups if not any(y!=x and not y&~x for y in ups)]
  return {"family_size":len(xs),"lattice":lattice,"orthomodular":om,"centre_size":len(centre) if lattice else None,"centre_is_trivial":lattice and set(centre)=={0,ALL},"first_failed_lattice_pair":first_failed,
   "actual_join_count":len(mins),"actual_join_minimal_upper_sha256":[mh(z) for z in mins],"actual_join_equals_target":len(mins)==1 and mins[0]==U,"actual_join_equals_literal_g":len(mins)==1 and mins[0]==literal,"literal_g_generated":literal in fam}
 base=LM+RM+[U];records=[]
 for j,(idx,label) in enumerate(chosen):
  fam,rounds,guard=close(base+[LCM[j],RCM[j]])
  A=audit(fam) if not guard else {"family_size":len(fam),"lattice":None,"orthomodular":None,"centre_size":None,"centre_is_trivial":None,"actual_join_count":None,"actual_join_equals_target":None,"actual_join_equals_literal_g":None,"literal_g_generated":literal in fam}
  category="guard_reached" if guard else "preserves_join_R" if A["actual_join_equals_target"] else "generates_g_as_join" if A["actual_join_equals_literal_g"] else "changes_or_loses_join"
  records.append({"context_index":idx,"context_complement_index":comp[idx],"selection_label":label,"disjoint_from_maxima":[dis(idx,15250),dis(idx,16786)],"closure_rounds":rounds,"guard_reached":guard,"category":category,"audit":A})
 left_cyl=all(len({(arr["F"]>>(a|(b<<6)))&1 for b in arr["BP"][s]})==1 for s in range(224) for a in arr["AP"][s]);right_cyl=all(len({(arr["F"]>>(a|(b<<6)))&1 for a in arr["AP"][s]})==1 for s in range(224) for b in arr["BP"][s])
 source=json.load(open(SOURCE_RECEIPT));out={"schema":SCHEMA,"schema_version":"1.0","source_pilot_payload_sha256":source["payload_sha256"],"selected_context_count":len(records),"master_truth_atom_count":N,"master_refinement_exactness":"Each case generator mask ignores every other context coordinate; complement and disjoint union preserve saturation on those forgotten coordinates, so the master representation is the exact pullback of the case quotient.","target_left_cylindrical":left_cyl,"target_right_cylindrical":right_cyl,"guard":GUARD,"records":records,"category_histogram":dict(sorted(collections.Counter(r["category"] for r in records).items())),"scope":"Exact one-context extensions of the restricted 16-event ARR-CYL control only. The guard is a computational stop, never promoted to closure. No ambient full-old-copy completion, state, sigma, ODBC, or Phi claim.","evidence_class":"Executable verified — sampled finite scope","command":"PYTHONHASHSEED=0 python3 notes/open_questions/verification/arr_cyl_one_context_extensions.py --verify"}
 out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest();out["runtime_seconds"]=round(time.perf_counter()-start,6);out["payload_sha256"]=digest({k:v for k,v in out.items() if k!="runtime_seconds"});return out

if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args();out=payload();path=os.path.join(HERE,"arr_cyl_one_context_extensions.json")
 if a.emit:
  with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
 else:
  stored=json.load(open(path));assert stored["payload_sha256"]==digest({k:v for k,v in stored.items() if k not in ("runtime_seconds","payload_sha256")});runtime=out["runtime_seconds"];ph=out["payload_sha256"];stored.pop("runtime_seconds",None);out.pop("runtime_seconds",None);stored.pop("payload_sha256",None);out.pop("payload_sha256",None);assert stored==out
 if a.emit:runtime=out["runtime_seconds"];ph=out["payload_sha256"]
 print(json.dumps({"status":"PASS","payload_sha256":ph,"categories":out["category_histogram"],"runtime_seconds":runtime},sort_keys=True))
