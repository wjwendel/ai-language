# Fresh, stateless call to the local decoder (Qwen2.5-7B-Instruct Q4_K_M via llama.cpp, temp 0). Each call = new conversation, no memory.
import json,urllib.request,sys,time
def chat(user,system=None,max_tokens=1500):
    msgs=([{'role':'system','content':system}] if system else [])+[{'role':'user','content':user}]
    req=urllib.request.Request('http://127.0.0.1:8091/v1/chat/completions',data=json.dumps({'messages':msgs,'temperature':0,'max_tokens':max_tokens,'cache_prompt':False}).encode(),headers={'Content-Type':'application/json'})
    t=time.time();r=json.load(urllib.request.urlopen(req,timeout=3600))
    return r['choices'][0]['message']['content'],round(time.time()-t,1),r.get('usage',{})
