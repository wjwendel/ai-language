# MNC round 3 measurements -> tokens.json. tiktoken o200k_base + cl100k_base. zlib = bytes, reference only.
import tiktoken,re,json,zlib,os
o=tiktoken.get_encoding('o200k_base');c=tiktoken.get_encoding('cl100k_base')
n=lambda s:[len(o.encode(s)),len(c.encode(s))]
orig={f'P{i+1}':p.strip() for i,(h,p) in enumerate(re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S))}
def secs(path): return {('P'+m.group(1)):m.group(0).rstrip('\n') for m in re.finditer(r'(?ms)^§(\d).*?(?=^§|\Z)',open(path).read())}
TO=[sum(n(v)[i] for v in orig.values()) for i in (0,1)]
K=n(open('key.md').read());KM=n(open('experiments/key_micro.md').read());K2=n(open('../round2/key.md').read())
meth={'mnc3 (key.md)':('payload.txt',K),'mnc3 micro-key':('payload.txt',KM),'mnc3 no key':('payload.txt',[0,0]),
 'mnc3x aggressive (key.md)':('experiments/payload_v3x_aggressive.txt',K),'mnc3a pre-prune (key.md)':('experiments/payload_v3a_prepune.txt',K),
 'a terse English (model)':('baselines/a_terse.txt',[0,0]),'b summarize (model)':('baselines/b_summarize.txt',[0,0]),
 'c LLMLingua-2 rate0.66':('baselines/c_llmlingua2_r0.66.txt',[0,0]),'c LLMLingua-2 rate0.5':('baselines/c_llmlingua2_r0.5.txt',[0,0])}
out={'tokenizers':['o200k_base','cl100k_base'],'originals':{p:n(v) for p,v in orig.items()},'originals_total':TO,
 'key_tokens':{'key.md':K,'key_micro':KM,'round2_key':K2},'methods':{}}
for m,(f,k) in meth.items():
    S=secs(f);per={p:n(S[p]) for p in orig};T=[sum(per[p][i] for p in orig) for i in (0,1)]
    ratio=[T[i]/TO[i] for i in (0,1)]
    out['methods'][m]={'file':f,'per_passage':per,'payload_sections':T,'payload_file':n(open(f).read()),'key':k,
      'payload_saved_pct':[round(100*(1-r),1) for r in ratio],
      'key_plus_payload':[k[i]+T[i] for i in (0,1)],'key_plus_payload_saved_pct':[round(100*(1-(k[i]+T[i])/TO[i]),1) for i in (0,1)],
      'break_even_orig_tokens':[round(k[i]/(1-ratio[i])) if ratio[i]<1 else None for i in (0,1)],
      'per_passage_saved_pct':{p:[round(100*(1-per[p][i]/n(orig[p])[i]),1) for i in (0,1)] for p in orig}}
ob=sum(len(v.encode()) for v in orig.values());oz=len(zlib.compress('\n'.join(orig.values()).encode(),9))
pz=len(zlib.compress(open('payload.txt').read().encode(),9));pb=len(open('payload.txt').read().encode())
out['zlib_bytes_reference_only']={'originals_utf8':ob,'originals_zlib9':oz,'mnc3_payload_utf8':pb,'mnc3_payload_zlib9':pz,'note':'bytes, not tokens; a model cannot read zlib output'}
json.dump(out,open('tokens.json','w'),indent=1,ensure_ascii=False)
for m,v in out['methods'].items(): print(f"{m:28s} pay {v['payload_sections']} saved {v['payload_saved_pct']} key+pay {v['key_plus_payload']} saved {v['key_plus_payload_saved_pct']} BE {v['break_even_orig_tokens']}")
print('orig',TO,'keys',K,KM,K2,out['zlib_bytes_reference_only'])
