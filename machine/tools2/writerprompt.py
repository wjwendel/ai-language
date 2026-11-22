# Terse-English baseline writer prompt for a SEPARATE no-context helper. usage: python writerprompt.py <dir>
import re,sys,os
d=sys.argv[1];orig=[p.strip() for p in re.split(r'(?m)^§\d+\n',open(f'{d}/originals.txt').read()) if p.strip()]
H=(f'You will produce one baseline compression of {len(orig)} separate passages. Treat each passage independently. For each passage apply exactly this instruction: '
 '"Shorten the following text maximally into terse, telegraphic plain English. Keep every fact. Output only the shortened text." '
 'Format: for passage N, a line "§N" followed by that passage\'s output, passages separated by one blank line. No other commentary.')
os.makedirs(f'{d}/dispatch',exist_ok=True)
open(f'{d}/dispatch/writer_terse.txt','w').write(H+'\n\n'+'\n\n'.join(f'=== PASSAGE {i+1} ===\n{p}' for i,p in enumerate(orig))+'\n');print('ok')
