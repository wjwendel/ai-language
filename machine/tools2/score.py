# Score reader answers <dir>/answers/<name>_rN.json against questions.json (accept regexes all must match; reject regexes none)
# + overrides <dir>/answers/overrides.json {file_stem:{qid:[0|1,"reason"]}}. usage: python score.py <dir> [-m]
import json,re,glob,os,sys
# 2026-11-19 r26: \b next to a digit fails before CJK units (462元); use digit lookarounds instead
def fx(x): return re.sub(r'(?<=\d)\\b',lambda m:r'(?!\d)',re.sub(r'\\b(?=\d)',lambda m:r'(?<!\d)',x))
ANS=os.environ.get('ANS','answers');d=sys.argv[1];Q=json.load(open(f'{d}/questions.json'))['questions']
O=json.load(open(f'{d}/{ANS}/overrides.json')) if os.path.exists(f'{d}/{ANS}/overrides.json') else {}
res={};rows=[]
for f in sorted(glob.glob(f'{d}/{ANS}/*_r*.json')):
    st=os.path.basename(f)[:-5];t=open(f).read();J=json.loads(t[t.find('{'):t.rfind('}')+1])
    r=res.setdefault(st,{'all':[0,0],'S':[0,0],'F':[0,0],'hop2':[0,0]})
    for q in Q:
        a=str(J.get(q['id'],'')).strip()
        ok=int(bool(a) and a.lower()!='not stated' and all(re.search(fx(x),a,re.I) for x in q['accept']) and not any(re.search(fx(x),a,re.I) for x in q.get('reject',[])))
        ov=O.get(st,{}).get(q['id']);fin=ov[0] if ov else ok
        rows.append(dict(f=st,id=q['id'],type=q['type'],auto=ok,final=fin,answer=a,gold=q['gold']))
        for k in ['all',q['type']]+(['hop2'] if q.get('hop',1)>1 else []): r[k][0]+=fin;r[k][1]+=1
json.dump({'rows':rows,'summary':res},open(f'{d}/{ANS}/scores.json','w'),indent=1,ensure_ascii=False)
for m,r in res.items(): print(f"{m:28s}"+'  '.join(f"{k} {a}/{b} ({100*a/b:.1f}%)" for k,(a,b) in r.items() if b))
if '-m' in sys.argv:
    for x in rows:
        if not x['final']: print('MISS',x['f'],x['id'],x['type'],'|',x['answer'][:140],'|| gold:',x['gold'][:90])
