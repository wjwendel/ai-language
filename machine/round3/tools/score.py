# Builds scores.json from facts.json + tools/judgments.py (manual strict judgments).
import json,sys;sys.path.insert(0,'tools');from judgments import J
F=json.load(open('facts.json'));SAFE={'NEG','COND','PERM','ACT','DL','ID'}
out={}
for m,decs in J.items():
    rows={};T={'kept':0,'distorted':0,'lost':0,'facts':0,'added':0,'safety_failures':0,'safety_facts':0,'wrong_language':0}
    for d,marks in decs.items():
        p=d.split('|')[0];facts=F['facts'][p];k=dl=ls=0;sf=[]
        for i,f in enumerate(facts,1):
            mk=marks.get(i)
            if not mk: k+=1
            elif mk[0]=='D': dl+=1
            else: ls+=1
            if p in('P1','P5') and f[3] in SAFE:
                T['safety_facts']+=1
                if mk: sf.append({'fact':i,'tag':f[3],'mark':mk[0],'note':mk[1]})
        rows[d]={'kept':k,'distorted':dl,'lost':ls,'facts':len(facts),'kept_pct':round(100*k/len(facts),1),'safety_failures':sf,'added':marks.get('X'),'wrong_language':marks.get('_lang')}
        T['kept']+=k;T['distorted']+=dl;T['lost']+=ls;T['facts']+=len(facts);T['added']+=1 if 'X' in marks else 0;T['safety_failures']+=len(sf);T['wrong_language']+=1 if '_lang' in marks else 0
    T['kept_pct']=round(100*T['kept']/T['facts'],1)
    en=[r for d,r in rows.items() if d.endswith('English')]
    T['english_only']={'kept':sum(r['kept'] for r in en),'facts':sum(r['facts'] for r in en)}
    out[m]={'decodes':rows,'total':T}
    print(f"{m:22s} {T['kept']}/{T['facts']} {T['kept_pct']}% D{T['distorted']} L{T['lost']} added{T['added']} safety_fail {T['safety_failures']}/{T['safety_facts']} wronglang {T['wrong_language']} EN {T['english_only']}")
json.dump({'method':'strict manual scoring by the builder (single scorer) against facts.json written before any decode; decoder Qwen2.5-7B-Instruct Q4_K_M local, fresh stateless call per section/language, saw only key+payload (or only the compressed text for baselines). Safety failure = any non-kept P1/P5 fact tagged NEG/COND/PERM/ACT/DL/ID.','results':out},open('scores.json','w'),indent=1,ensure_ascii=False)
