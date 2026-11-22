# Score round-12 frontier answers frontier/ans_<method>_rN.txt with pre-written regexes + manual overrides frontier/overrides.json {stem:{qid:[0|1,note]}}
import json,re,os,glob,sys
Q=json.load(open('directuse/questions.json'));O=json.load(open('frontier/overrides.json')) if os.path.exists('frontier/overrides.json') else {}
R={};rows=[]
for f in sorted(glob.glob('frontier/ans_*.txt')):
    stem=os.path.basename(f)[4:-4];t=open(f).read();J=json.loads(t[t.find('{'):t.rfind('}')+1])
    r=R.setdefault(stem,{'all':[0,0],'S':[0,0],'F':[0,0],'en':[0,0],'L2':[0,0],'P1S':[0,0],'P5S':[0,0]})
    for p in range(1,6):
        qs=Q[f'P{p}']
        for lang in ['en',qs[0]['l2']]:
            for i,q in enumerate(qs,1):
                qid=f'§{p}.{lang}{i}';a=str(J.get(qid,''))
                ok=int(bool(a) and a.strip().lower()!='not stated' and all(re.search(x,a,re.I) for x in q['accept']))
                ov=O.get(stem,{}).get(qid);fin=ov[0] if ov else ok
                rows.append(dict(f=stem,id=qid,type=q['type'],auto=ok,final=fin,answer=a,gold=q['gold']))
                for k in ['all',q['type'],'en' if lang=='en' else 'L2']+([f'P{p}S'] if q['type']=='S' and p in(1,5) else []): r[k][0]+=fin;r[k][1]+=1
json.dump({'rows':rows,'summary':R},open('frontier/scores.json','w'),indent=1,ensure_ascii=False)
for m,r in R.items(): print(f"{m:26s}"+' '.join(f"{k} {a}/{b} ({100*a/b:.1f}%)" for k,(a,b) in r.items() if b))
if '-m' in sys.argv:
    for x in rows:
        if not x['final']: print(x['f'],x['id'],x['type'],'|',x['answer'][:120],'|| gold:',x['gold'][:80])
