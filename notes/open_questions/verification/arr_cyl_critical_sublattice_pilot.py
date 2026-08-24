#!/usr/bin/env python3
"""Exact ARR-CYL four-generator quotient for actual Neg-023.

Use cylinders of the two maximal old lowers and their complements on one or
both copies, plus the exact Neg-023 relation.  The 56 shared overlap traces
are audited but not adjoined as generators.  Close under complement and
genuinely disjoint union with no seeded ``g``.
"""
import argparse, collections, hashlib, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "adjacent_full_cycle_actual_event_shadow.py")
SOURCE_RECEIPT = os.path.join(HERE, "adjacent_kernel_observational_congruence.json")
AR_RECEIPT = os.path.join(HERE, "adjacent_ar_reb_001.json")
SCHEMA = "arr-cyl-critical-sublattice-pilot-v1"
CRITICAL = (15250, 16786, 10752, 18322, 18331)
FAMILY_CAP = 20000


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def payload():
    started = time.perf_counter()
    src = open(SOURCE).read()
    needle = "base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']"
    assert src.count(needle) == 1
    src = src.replace(needle, needle + ";globals()['_ARR_BANK']=b")
    needle2 = "mismatches=[];actual_bad=coord_bad=0;mismatch_kinds=collections.Counter()"
    assert src.count(needle2) == 1
    src = src.replace(needle2, needle2 + ";arr_counter=0")
    needle3 = "actual=compose_all(retained,pos,tables)"
    assert src.count(needle3) == 1
    inject = """actual=compose_all(retained,pos,tables)
   if name=='left_retained_position11' and t['kind']=='Neg' and arr_counter==23:
    _arr_right=compose_all(opposite,oppos,RT)
    globals()['_ARR_DATA']={'F':t['F'],'retained':tuple(retained),'opposite':tuple(opposite),'AP':AP,'BP':BP,'allowed':allowed,'pos':pos,'oppos':oppos,'patterns':patterns,'occ':occ,'semantic_signature_sha256':sh,'opposite_universal_shadow_root_sha256':rhash(_arr_right)}
   arr_counter+=1"""
    src = src.replace(needle3, inject)
    ns = {"__file__": SOURCE, "__name__": "_arr_cyl_instrumented"}
    exec(compile(src, SOURCE, "exec"), ns); ns["payload"]()
    bank, arr = ns["_ARR_BANK"], ns["_ARR_DATA"]
    events, macros, engines, states = bank["all_events"], bank["macros"], bank["engines"], bank["states"]
    roots = {ev: root for root, ev in bank["root_to_event"].items()}; principal = bank["principal"]
    upmap = {u:i for i,u in enumerate(principal)}; root_index = {roots[e]:i for i,e in enumerate(events)}
    n = len(events); assert (n,len(states)) == (18676,224)
    def negroot(x): return tuple(engines[m].neg(a) for m,a in enumerate(x))
    comp = {i:root_index[negroot(roots[e])] for i,e in enumerate(events)}
    def join(i,j): return upmap[principal[i]&principal[j]]
    def meet(i,j): return comp[join(comp[i],comp[j])]

    # Exact 56 overlap representatives in each orientation: saturated E=U.
    def status(m,r,pos,i,cache={}):
        key=(m,r,pos,i)
        if key in cache:return cache[key]
        if r<=1:z=r
        else:
            v,ch=engines[m].nodes[r]
            if v==pos:z=status(m,ch[i],pos,i)
            else:
                q={status(m,x,pos,i) for x in ch};z=q.pop() if len(q)==1 else 2
        cache[key]=z;return z
    occ=arr["occ"]
    def saturated_reps(pos):
        reps={}
        for idx,e in enumerate(events):
            rr=roots[e];E=U=0
            for s,os in enumerate(occ[pos]):
                vals=[status(m,rr[m],pos,i) for m,i in os]
                if any(vals):E|=1<<s
                if all(v==1 for v in vals):U|=1<<s
            if E==U:reps.setdefault(E,idx)
        return reps
    left_shared=saturated_reps(arr["pos"]);right_shared=saturated_reps(arr["oppos"])
    assert set(left_shared)==set(right_shared) and len(left_shared)==56

    # Smallest exact family: the two maximal lowers and complements.  Do not
    # insert their old-lattice joins; quotient closure below uses only
    # complement and genuinely disjoint literal union.
    K=tuple(sorted({15250,16786,comp[15250],comp[16786]}));old_sublattice_exact=True

    result={"category":"uninitialized"}
    if old_sublattice_exact:
        patterns=arr["patterns"]
        def vector(indices,pos):
            out=[]
            for s in range(224):
                vals=set()
                for m,i in occ[pos][s]:vals.update(patterns(m,tuple(roots[events[e]][m] for e in indices),pos,i))
                out.append(tuple(sorted(vals)))
            return out
        left_indices=tuple(arr["retained"])+K;right_indices=tuple(arr["opposite"])+K
        LP=vector(left_indices,arr["pos"]);RP=vector(right_indices,arr["oppos"])
        atom_words=set()
        for s in range(224):
            for l in LP[s]:
                a=l&63;lk=l>>6
                for r in RP[s]:
                    b=r&63;rk=r>>6;u=(arr["F"]>>(a|(b<<6)))&1
                    atom_words.add((lk,rk,u))
        atom_words=tuple(sorted(atom_words));na=len(atom_words);ALL=(1<<na)-1
        left_masks=[];right_masks=[]
        for j in range(len(K)):
            left_masks.append(sum(1<<i for i,(l,r,u) in enumerate(atom_words) if l>>j&1))
            right_masks.append(sum(1<<i for i,(l,r,u) in enumerate(atom_words) if r>>j&1))
        u_mask=sum(1<<i for i,(_,_,u) in enumerate(atom_words) if u)
        target_left_cylindrical=all(len({(arr["F"]>>(a|(b<<6)))&1 for b in arr["BP"][s]})==1 for s in range(224) for a in arr["AP"][s])
        target_right_cylindrical=all(len({(arr["F"]>>(a|(b<<6)))&1 for a in arr["AP"][s]})==1 for s in range(224) for b in arr["BP"][s])
        kpos={e:j for j,e in enumerate(K)}
        def close(initial):
            fam=set(initial)|{0,ALL};front=list(fam);rounds=[];capped=False
            while front:
                snap=sorted(fam);add=set()
                for x in sorted(front):
                    add.add(ALL^x)
                    for y in snap:
                        if x&y==0:add.add(x|y)
                    if len(fam|add)>FAMILY_CAP:capped=True;break
                add-=fam
                if capped:break
                rounds.append(len(add));fam|=add;front=list(add)
            return fam,rounds,capped
        right_initial=[right_masks[j] for j in range(len(K))]+[u_mask]
        both_initial=right_initial+[left_masks[j] for j in range(len(K))]
        right_f,rr,rc=close(right_initial);both_f,br,bc=close(both_initial)
        lo1=right_masks[kpos[15250]];lo2=right_masks[kpos[16786]];literal=lo1|lo2
        physical_literal_root=tuple(engines[m].app(1,roots[events[15250]][m],roots[events[16786]][m]) for m in range(len(macros)))
        physical_literal_sha=hashlib.sha256(b"".join(__import__('struct').pack('<I',x) for x in physical_literal_root)).hexdigest()
        def cut_report(fam):
            all_ups=[x for x in fam if not (lo1|lo2)&~x]
            all_mins=[x for x in all_ups if not any(y!=x and not y&~x for y in all_ups)]
            interval_ups=[x for x in all_ups if not x&~u_mask]
            return {"family_size":len(fam),"capped":len(fam)>=FAMILY_CAP,
              "all_family_upper_count":len(all_ups),"actual_join_count":len(all_mins),
              "actual_join_equals_literal_union":len(all_mins)==1 and all_mins[0]==literal,
              "actual_join_equals_target":len(all_mins)==1 and all_mins[0]==u_mask,
              "interval_upper_count":len(interval_ups),
              "least_upper_count":len(all_mins),
              "least_upper_equals_literal_union":len(all_mins)==1 and all_mins[0]==literal,
              "least_upper_equals_target":len(all_mins)==1 and all_mins[0]==u_mask,
              "literal_union_generated":literal in fam,"target_generated":u_mask in fam,
              "least_upper_sha256":None if len(all_mins)!=1 else hashlib.sha256(all_mins[0].to_bytes((na+7)//8,"little")).hexdigest()}
        def structural_audit(fam):
            xs=sorted(fam);meet={};joinq={};lattice=True
            for x in xs:
                for y in xs:
                    lows=[z for z in xs if not z&~x and not z&~y]
                    gl=[z for z in lows if not any(z!=w and not z&~w for w in lows)]
                    ups=[z for z in xs if not x&~z and not y&~z]
                    lu=[z for z in ups if not any(z!=w and not w&~z for w in ups)]
                    if len(gl)!=1 or len(lu)!=1:lattice=False
                    else:meet[(x,y)]=gl[0];joinq[(x,y)]=lu[0]
            om=False;centre=[]
            if lattice:
                om=all(joinq[(x,meet[(y,ALL^x)])]==y for x in xs for y in xs if not x&~y)
                centre=[c for c in xs if all(joinq[(meet[(x,c)],meet[(x,ALL^c)])]==x for x in xs)]
            return {"lattice":lattice,"orthomodular":om,"centre_size":len(centre) if lattice else None,
              "centre_is_trivial":lattice and set(centre)=={0,ALL}}
        R=cut_report(right_f);B=cut_report(both_f)
        cut_fields=("actual_join_count","actual_join_equals_literal_union","actual_join_equals_target","literal_union_generated","least_upper_sha256")
        assert R["actual_join_count"]==B["actual_join_count"]==1
        assert R["actual_join_equals_target"] and B["actual_join_equals_target"]
        result={"category":("both_copy_closure_changes_target_only_cut" if any(R[k]!=B[k] for k in cut_fields) else "both_copy_closure_preserves_target_only_cut"),
          "realized_truth_atom_count":na,"right_only_closure_rounds":rr,"both_copy_closure_rounds":br,
          "right_only":R,"both_copy":B,"right_closure_hit_cap":rc,"both_closure_hit_cap":bc,
          "right_only_structural_audit":structural_audit(right_f),"both_copy_structural_audit":structural_audit(both_f),
          "target_left_cylindrical":target_left_cylindrical,"target_right_cylindrical":target_right_cylindrical,
          "literal_union_mask_sha256":hashlib.sha256(literal.to_bytes((na+7)//8,"little")).hexdigest(),
          "physical_literal_union_root_sha256":physical_literal_sha,
          "physical_literal_union_equals_recorded_g":None,
          "target_mask_sha256":hashlib.sha256(u_mask.to_bytes((na+7)//8,"little")).hexdigest()}
    source=json.load(open(SOURCE_RECEIPT));ar_source=json.load(open(AR_RECEIPT))
    assert arr["semantic_signature_sha256"]=="6b048d77733df8711fd75428ead07e246cb53d6af0de8e08945be3caac147185"
    assert arr["opposite_universal_shadow_root_sha256"]=="d5915700da7c9d748c41b8fb97d6300ab60786c684ad9484c24816c2e072cfa3"
    if "physical_literal_union_root_sha256" in result:
        result["physical_literal_union_equals_recorded_g"]=result["physical_literal_union_root_sha256"]==ar_source["seeded_literal_lower_envelope_root_sha256"]
        assert result["physical_literal_union_equals_recorded_g"]
    out={"schema":SCHEMA,"schema_version":"1.0","source_actual_kernel_payload_sha256":source["payload_sha256"],
      "source_actual_event_payload_sha256":source["source_actual_event_payload_sha256"],
      "source_ar_reb_payload_sha256":ar_source["payload_sha256"],
      "occurrence_link":{"occurrence_id":"left_retained_position11-Neg-023","semantic_signature_sha256":arr["semantic_signature_sha256"],"opposite_universal_shadow_root_sha256":arr["opposite_universal_shadow_root_sha256"]},
      "generator_indices":list(K),"contextual_ar_reb_indices":list(CRITICAL),"shared_overlap_trace_count":56,"old_generator_family_size":len(K),
      "old_generator_family_exact":old_sublattice_exact,"family_cap":FAMILY_CAP,"g_seeded":False,
      "result":result,
      "scope":"Exact finite truth-signature quotient generated only by cylinders of the two maximal lowers 15250/16786 and complements, plus actual Neg-023. Any lattice/OML verdict is restricted-generator control only, not an ambient completion of the full old copy. No 6.2M carrier, full old-copy sublogic, state, sigma, ODBC, or Phi claim.",
      "evidence_class":"Executable verified — sampled finite scope",
      "command":"PYTHONHASHSEED=0 python3 notes/open_questions/verification/arr_cyl_critical_sublattice_pilot.py --verify"}
    out["producer_sha256"]=hashlib.sha256(open(__file__,"rb").read()).hexdigest();out["runtime_seconds"]=round(time.perf_counter()-started,6);out["payload_sha256"]=digest({k:v for k,v in out.items() if k!="runtime_seconds"});return out


if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--emit",action="store_true");ap.add_argument("--verify",action="store_true");a=ap.parse_args();out=payload();path=os.path.join(HERE,"arr_cyl_critical_sublattice_pilot.json")
    if a.emit:
        with open(path,"w") as f:json.dump(out,f,sort_keys=True,indent=2);f.write("\n")
    else:
        runtime=out["runtime_seconds"];payloadhash=out["payload_sha256"]
        stored=json.load(open(path));stored_hash=stored["payload_sha256"];assert stored_hash==digest({k:v for k,v in stored.items() if k not in ("runtime_seconds","payload_sha256")});stored.pop("runtime_seconds",None);out.pop("runtime_seconds",None);stored.pop("payload_sha256",None);out.pop("payload_sha256",None);assert stored==out
    if a.emit:runtime=out["runtime_seconds"];payloadhash=out["payload_sha256"]
    print(json.dumps({"status":"PASS","payload_sha256":payloadhash,"category":out["result"]["category"],"runtime_seconds":runtime},sort_keys=True))
