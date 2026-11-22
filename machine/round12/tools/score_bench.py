# Score frontier bench answers (round12/bench_frontier/ans_<method>_rN.txt) with bench-v1 pre-registered regexes + manual overrides
# round12/bench_frontier/overrides.json {file_stem: {qid: [0|1, note]}}
import json,re,os,glob,sys
B=json.load(open('bench/bench.json'))['items'];D='round12/bench_frontier'
O=json.load(open(f'{D}/overrides.json')) if os.path.exists(f'{D}/overrides.json') else {}
R={};rows=[]
for f in sorted(glob.glob(f'{D}/ans_*.txt')):
    stem=os.path.basename(f)[4:-4];t=open(f).read();J=json.loads(t[t.find('{'):t.rfind('}')+1])
    r=R.setdefault(stem,{'all':[0,0],'S':[0,0],'F':[0,0],'r3':[0,0],'r4':[0,0],'r5':[0,0],'instrS':[0,0]})
    for it in B:
        qs=it['questions'];bid=it['bid']
        for lang in (['en','es'] if 'es' in qs[0] else ['en']):
            for i,q in enumerate(qs,1):
                qid=f'{bid}.{lang}{i}';a=str(J.get(qid,''))
                ok=int(bool(a) and a.strip().lower()!='not stated' and any(re.search(x,a,re.I) for x in q['accept']))
                ov=O.get(stem,{}).get(qid);fin=ov[0] if ov else ok
                rows.append(dict(f=stem,id=qid,type=q['type'],auto=ok,final=fin,answer=a,gold=q['gold']))
                for k in ['all',q['type'],f"r{it['round']}"]+(['instrS'] if it['instruction'] and q['type']=='S' else []): r[k][0]+=fin;r[k][1]+=1
json.dump({'rows':rows,'summary':R},open(f'{D}/scores.json','w'),indent=1,ensure_ascii=False)
for m,r in R.items(): print(f"{m:16s}"+' '.join(f"{k} {a}/{b} ({100*a/b:.1f}%)" for k,(a,b) in r.items()))
if '-m' in sys.argv:
    for x in rows:
        if not x['final']: print(x['f'],x['id'],x['type'],'|',x['answer'][:110],'|| gold:',x['gold'][:80])
