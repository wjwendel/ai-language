# Scores directuse/answers.json: regex auto-score, then manual overrides in directuse/qa_overrides.json ({tag: {qnum: [0|1, note]}}).
import json,re,os
Q=json.load(open('directuse/questions.json'));A=json.load(open('directuse/answers.json'))
O=json.load(open('directuse/qa_overrides.json')) if os.path.exists('directuse/qa_overrides.json') else {}
def split(t,n):
    parts=re.split(r'(?m)^\s*(\d{1,2})[\.\)]\s*',t);d={}
    for i in range(1,len(parts)-1,2): d.setdefault(int(parts[i]),parts[i+1].strip())
    return [d.get(i,'') for i in range(1,n+1)]
R={};rows=[]
for tag,t in A.items():
    m,p,l=tag.split('|');qs=Q[p];ans=split(t,len(qs))
    for i,(q,a) in enumerate(zip(qs,ans),1):
        ok=int(any(re.search(r,a,re.I) for r in q['accept']));ov=O.get(tag,{}).get(str(i))
        fin=ov[0] if ov else ok
        rows.append({'tag':tag,'q':i,'type':q.get('type','F'),'auto':ok,'final':fin,'answer':a,'gold':q['gold'],'override':ov[1] if ov else None})
        r=R.setdefault(m,{'all':[0,0],'S':[0,0],'F':[0,0],'en':[0,0],'es':[0,0]})
        for k in ['all',q.get('type','F'),l]: r[k][0]+=fin;r[k][1]+=1
json.dump({'rows':rows,'summary':R},open('directuse/qa_scores.json','w'),indent=1,ensure_ascii=False)
for m,r in R.items(): print(f"{m:14s}"+' '.join(f"{k} {a}/{b} ({100*a/b:.0f}%)" for k,(a,b) in r.items() if b))
