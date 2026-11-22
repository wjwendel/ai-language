# Blind reader prompt: TEXT + questions only. usage: python qaprompt.py <dir> name=file ...  -> <dir>/dispatch/qa_<name>.txt
import json,sys,os
d=sys.argv[1];Q=json.load(open(f'{d}/questions.json'))['questions'];os.makedirs(f'{d}/dispatch',exist_ok=True)
INS=('Answer using only the TEXT. Some questions describe a situation and ask what to do or whether something is allowed; apply every rule in the TEXT that bears on it. '
 'Reply with one JSON object only, mapping each question ID to a short answer string (start yes/no questions with "yes" or "no"). Answer in English. If the TEXT does not say, answer "not stated".')
for a in sys.argv[2:]:
    n,f=a.split('=');t=open(f'{d}/{f}').read().strip()
    ql='\n'.join(f"{q['id']}: {q['q']}" for q in Q)
    open(f'{d}/dispatch/qa_{n}.txt','w').write(f"TEXT:\n{t}\n\nQUESTIONS (each is about the section named in its ID):\n{ql}\n\n{INS}\n");print('wrote',n)
