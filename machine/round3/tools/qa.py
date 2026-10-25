# Direct use (no decode): fresh stateless call; model sees ONLY the method's text for one passage (+ key for MNC) and the questions.
import json,re,sys;sys.path.insert(0,'tools');from llm import chat
Q=json.load(open('directuse/questions.json'))
def secs(path):
    t=open(path).read();return {int(m.group(1)):m.group(0).rstrip('\n') for m in re.finditer(r'(?ms)^§(\d).*?(?=^§|\Z)',t)}
orig={i+1:p.strip() for i,(h,p) in enumerate(re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S))}
M={'original':(None,orig),'mnc3':('key.md',secs('payload.txt')),'mnc3x':('key.md',secs('experiments/payload_v3x_aggressive.txt')),
   'mnc3_nokey':(None,secs('payload.txt')),'a_terse':(None,secs('baselines/a_terse.txt')),'b_summarize':(None,secs('baselines/b_summarize.txt')),
   'c_llmlingua2':(None,secs('baselines/c_llmlingua2_r0.66.txt'))}
res=json.load(open('directuse/answers.json')) if len(sys.argv)>1 and sys.argv[1]=='resume' else {}
for m,(k,S) in M.items():
    for p in range(1,6):
        for lang in ['en','es']:
            qs=Q[f'P{p}']
            if lang=='es' and 'es' not in qs[0]: continue
            tag=f'{m}|P{p}|{lang}'
            if tag in res: continue
            ql='\n'.join(f"{i+1}. {q['q'] if lang=='en' else q['es']}" for i,q in enumerate(qs))
            ctx=(f"KEY (how to read the code):\n{open(k).read()}\n\nTEXT (in that code):\n{S[p]}" if k else f"TEXT:\n{S[p]}")
            ins=("Answer the questions using only the text. Number each answer; one short line each; start with Yes or No when the question is yes/no." if lang=='en'
                 else "Responde a las preguntas usando solo el texto. Numera cada respuesta; una línea corta cada una; empieza con Sí o No si la pregunta es de sí/no.")
            t,dt,u=chat(f"{ctx}\n\n{ins}\n\n{ql}",max_tokens=600)
            res[tag]=t;json.dump(res,open('directuse/answers.json','w'),indent=1,ensure_ascii=False);print(tag,dt,flush=True)
