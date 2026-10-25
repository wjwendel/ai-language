# Baseline c: LLMLingua-2 (microsoft/llmlingua-2-xlm-roberta-large-meetingbank, multilingual), CPU. rate = kept-token fraction.
import re,sys
from llmlingua import PromptCompressor
pc=PromptCompressor(model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",use_llmlingua2=True,device_map="cpu")
orig=[p.strip() for h,p in re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S)]
for rate in [float(x) for x in sys.argv[1:]]:
    out=[]
    for i,p in enumerate(orig):
        r=pc.compress_prompt(p,rate=rate,force_tokens=['\n'])
        out.append(f'§{i+1}\n'+r['compressed_prompt'].strip())
    open(f'baselines/c_llmlingua2_r{rate}.txt','w').write('\n'.join(out)+'\n');print('done',rate,flush=True)
