# Baseline: LLMLingua-2 (xlm-roberta-large-meetingbank, multilingual), CPU. usage: /workspace/llm/ll/bin/python lingua.py <dir> 0.66 0.5
import re,sys,os
from llmlingua import PromptCompressor
d=sys.argv[1];pc=PromptCompressor(model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",use_llmlingua2=True,device_map="cpu")
orig=[p.strip() for p in re.split(r'(?m)^§\d+\n',open(f'{d}/originals.txt').read()) if p.strip()];os.makedirs(f'{d}/baselines',exist_ok=True)
for rate in [float(x) for x in sys.argv[2:]]:
    out=[f'§{i+1}\n'+pc.compress_prompt(p,rate=rate,force_tokens=['\n'])['compressed_prompt'].strip() for i,p in enumerate(orig)]
    open(f'{d}/baselines/c_llmlingua2_r{rate}.txt','w').write('\n\n'.join(out)+'\n');print('done',rate,flush=True)
