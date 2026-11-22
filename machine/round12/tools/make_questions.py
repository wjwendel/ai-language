# Round 12 questions, written AFTER payload_mnc16.txt / payload_mnc16xx.txt were saved (see encoded_before_questions.sha1).
import json
def Q(q,sl,gold,acc,t,l2): return dict(q=q,sl=sl,gold=gold,accept=acc,type=t,l2=l2)
P1=[("When does this routine run?","¿Cuándo se ejecuta esta rutina?","Every Thursday 2 p.m. Central",[r"(thu|jue).*(2|14)|(2|14).*(thu|jue)"],"F"),
("Which template do you use for draft orders?","¿Qué plantilla usas para los borradores de pedido?","Weekly Order",[r"weekly order"],"F"),
("A draft order is ready and Rosa has not answered yet. Should you send it?","Un borrador está listo y Rosa aún no ha respondido. ¿Debes enviarlo?","No; wait for Rosa's approval",[r"^\s*(no|non)\b|wait|esper"],"S"),
("An order totals $450. Does Daniel need to look at it?","Un pedido suma 450 $. ¿Tiene que revisarlo Daniel?","No (only over $600)",[r"^\s*no\b"],"S"),
("An order totals $750. Who must look at it, and should Daniel be copied on the email to the supplier?","Un pedido suma 750 $. ¿Quién debe revisarlo y hay que poner a Daniel en copia del correo al proveedor?","Daniel (accounting) before Rosa approves, then Rosa; do not copy Daniel on the supplier email",[r"daniel.*(no|not|never|nunca)|(no|not|never|nunca).*cop"],"S"),
("To reach a supplier's minimum, may you raise a quantity by 8%? May you switch to a cheaper brand?","Para llegar al mínimo de un proveedor, ¿puedes subir una cantidad un 8 %? ¿Puedes cambiar a una marca más barata?","Yes to 8%; no to switching brand",[r"^\s*(yes|s[ií])\b.*\b(no|not|never|nunca)\b"],"S"),
("A supplier emails announcing a price increase. What do you do?","Un proveedor anuncia una subida de precio por correo. ¿Qué haces?","Don't accept or reply; forward to Rosa",[r"forward.*rosa|rosa.*forward|reenv.*rosa|rosa"],"S"),
("Who is the owner, and may you email him about an order?","¿Quién es el dueño y puedes escribirle sobre un pedido?","Kevin Brandt; no, never contact him about orders",[r"kevin.*(no|never|nunca)"],"S"),
("How should you refer to Rosa?","¿Cómo debes referirte a Rosa?","As the café manager, not the owner",[r"manager|gerente|encargad"],"S"),
("It is Thursday and the Stock sheet was last updated on Saturday. What do you do?","Es jueves y la hoja de Stock se actualizó por última vez el sábado. ¿Qué haces?","Stop and tell Rosa, don't guess",[r"stop.*rosa|rosa|det[eé]n|par[ao]"],"S"),
("A supplier's email is down. May you place the order by phone?","El correo de un proveedor no funciona. ¿Puedes hacer el pedido por teléfono?","No",[r"^\s*no\b"],"S"),
("By when must drafts be ready, and what extra report is due on the last Thursday of the month?","¿Para cuándo deben estar listos los borradores y qué informe extra toca el último jueves del mes?","Thursday 4 p.m.; month's total order costs to Rosa",[r"(4|16).*(total|month|mes)"],"S")]
P2=[("When does the Line 5 southern extension open for trial operation?","5号线南延段什么时候开通试运营？","December 28",[r"12月28|dec\w*\.? ?28|28"],"F"),
("How long is the new section and how many stations does it have?","新线全长多少，设几座车站？","9.6 km, 6 stations",[r"9\.6.*6|6.*9\.6"],"F"),
("Between which two stations does it run?","新线从哪个站通到哪个站？","Nanhu Park (南湖公园站) to the high-speed rail south station (高铁南站)",[r"南湖|nanhu|south lake",r"高铁南|high.?speed"],"F"),
("Who gave the details and what is his role?","谁介绍的情况？他是什么职务？","王建国, deputy director of the city transport bureau",[r"王建国|wang jianguo"],"F"),
("What is the total investment and who pays a third?","总投资多少？谁承担三分之一？","About 6.8 billion yuan; the province",[r"68|6\.8"],"F"),
("How much shorter will the trip from the city centre to the high-speed south station be?","从市中心到高铁南站的时间会怎样变化？","From 50 to 25 minutes",[r"50.*25"],"F"),
("During trial operation, what are the hours and the peak frequency?","试运营期间运营时间和高峰班次是怎样的？","6 a.m. to 10 p.m.; every 4 minutes at peak",[r"(6|六).*(22|10|十).*(4|四)"],"F"),
("Is the first month free, and do riders still need to tap their card?","头一个月免费吗？还需要刷卡进站吗？","Yes, free for everyone; yes, still tap the card",[r"(yes|是|免费|free).*(yes|需要|tap|刷卡|still)"],"S"),
("Why was the opening delayed, and from when?","为什么推迟开通？原计划什么时候？","Groundwater problems; originally planned for last year's National Day",[r"(groundwater|地下水)"],"F"),
("What happens to bus lines along the route?","沿线公交线路会怎样？","Two lines adjusted next March; plan still under consultation",[r"(two|2|两).*(march|3月|三月)"],"F")]
P3=[("When and where does the group meet to leave?","Quand et où le groupe se retrouve-t-il pour partir ?","Friday January 23, 5 p.m., outside Clara's place",[r"(23|fri|ven).*(17|5).*clara|clara.*(17|5)|(17|5 ?p).*clara"],"F"),
("Where is the chalet and how long is the drive?","Où est le chalet et combien de temps de route ?","Morzine, about three hours",[r"morzine.*(3|three|trois)"],"F"),
("Whose cars are they taking?","Quelles voitures prennent-ils ?","Clara's and Hugo's",[r"clara.*hugo|hugo.*clara"],"F"),
("Why does Hugo need to go to the garage, and when?","Pourquoi Hugo doit-il passer au garage, et quand ?","Snow tyres only on the back; Wednesday",[r"(rear|back|arri[eè]re).*(wed|mercredi)|(wed|mercredi).*(rear|back|arri[eè]re)"],"F"),
("How much does each person pay, how many people are there, and by when?","Combien paie chacun, combien sont-ils, et avant quand ?","€120 each, seven people, before January 15",[r"120.*(7|seven|sept).*15|120.*15.*(7|seven|sept)"],"F"),
("Who buys food for Saturday dinner, and what is the meal?","Qui fait les courses pour samedi soir, et quel est le repas ?","Inès; fondue",[r"in[eè]s.*fondue|fondue.*in[eè]s"],"F"),
("Is anyone vegetarian, and is the meal a problem for them?","Quelqu'un est-il végétarien, et le repas lui pose-t-il problème ?","Malik; no, fondue is fine",[r"malik"],"F"),
("Can Inès bring her dog?","Inès peut-elle amener son chien ?","No; no pets, it stays with her parents",[r"^\s*(no|non)\b"],"S"),
("What happened last year, and what will Hugo do this time?","Que s'est-il passé l'an dernier, et que fera Hugo cette fois ?","They forgot the chains and were stuck two hours; Hugo brings chains",[r"(chain|cha[iî]ne).*(2|two|deux)|(2|two|deux).*(chain|cha[iî]ne)"],"F"),
("When and to whom are the keys returned?","Quand et à qui rend-on les clés ?","Sunday before 11 a.m., to the owner M. Perrin",[r"perrin.*11|11.*perrin"],"F")]
P4=[("Which facility closes, when, and why?","Que instalação fecha, quando e porquê?","Indoor municipal pool, March 2-30, heating system replacement",[r"(pool|piscina).*2.*30.*(heat|aquec)|(heat|aquec)"],"F"),
("Who is the official quoted and what is her role?","Quem é a responsável citada e qual o seu cargo?","Ana Lopes, councillor for sport",[r"ana lopes"],"F"),
("How much does the work cost and what share comes from European funds?","Quanto custa a obra e que parte vem de fundos europeus?","About €410,000; 75%",[r"410.*75"],"F"),
("Where do children's swimming lessons move, and how do the children get there?","Para onde passam as aulas de natação das crianças e como chegam lá?","Ribeirinha pool; free transport Tuesdays and Thursdays after school",[r"ribeirinha.*(free|gr[aá]t|tue|ter)"],"F"),
("Is free transport available on Mondays?","Há transporte gratuito às segundas-feiras?","No (only Tuesdays and Thursdays)",[r"^\s*(no|não|nao)\b"],"S"),
("Will March fees be charged?","As mensalidades de março serão cobradas?","No",[r"^\s*(no|não|nao)\b"],"S"),
("A 70-year-old member wants to use the pavilion gym in March. Is there an extra charge?","Um utente de 70 anos quer usar o ginásio do pavilhão em março. Paga mais?","No, free for over-65s that month",[r"^\s*(no|não|nao)\b|free|grat|sem custo"],"S"),
("A 60-year-old asks the same. Does the free gym offer apply to them?","Um utente de 60 anos pergunta o mesmo. A oferta aplica-se?","No (only over 65)",[r"^\s*(no|não|nao)\b"],"S"),
("How did the last works in 2019 go?","Como correu a última obra, em 2019?","Finished two weeks early",[r"(two|2|duas).*(early|antes|weeks|semanas)"],"F"),
("When does the pool reopen and what is special that day?","Quando reabre a piscina e o que há de especial nesse dia?","March 31, free entry",[r"31.*(free|livre|grat)"],"F")]
P5=[("When does this routine run and which mailbox do you check?","Kiedy działa ta procedura i którą skrzynkę sprawdzasz?","Every working day 8:00; serwis@termo-lux.pl",[r"8.*serwis@termo-lux\.pl|serwis@termo-lux\.pl.*8"],"F"),
("A boiler-failure ticket arrives and there is a free technician slot in two days. May you book it yourself?","Przychodzi zgłoszenie awarii pieca, a wolny termin technika jest za dwa dni. Czy możesz sam go wpisać?","Yes",[r"^\s*(yes|tak)\b"],"S"),
("Same, but the first free slot is in five days. May you book it yourself?","To samo, ale pierwszy wolny termin jest za pięć dni. Czy możesz sam go wpisać?","No (only within three days)",[r"^\s*(no|nie)\b"],"S"),
("A customer reports a smell of gas. What do you do?","Klient zgłasza zapach gazu. Co robisz?","Don't book a visit; tell them to call 992 immediately; notify Mr Nowak",[r"992.*nowak|nowak.*992"],"S"),
("A customer asks how much a repair will cost. Do you answer, and who does?","Klient pyta, ile będzie kosztować naprawa. Czy odpowiadasz i kto to robi?","No; only Ms Wiśniewska from the office",[r"(no|nie).*wi[sś]niewsk|wi[sś]niewsk"],"S"),
("A customer asks to move their visit by one day. May you do it?","Klient prosi o przesunięcie wizyty o jeden dzień. Czy możesz to zrobić?","Yes",[r"^\s*(yes|tak)\b"],"S"),
("A customer asks to cancel their visit. May you cancel it yourself?","Klient prosi o odwołanie wizyty. Czy możesz sam ją odwołać?","No, not without Mr Nowak's consent",[r"^\s*(no|nie)\b"],"S"),
("The calendar shows exactly 12 visits for Friday. Must you write to Mr Nowak right away?","W kalendarzu jest dokładnie 12 wizyt na piątek. Czy musisz od razu pisać do Pana Nowaka?","No (only more than 12)",[r"^\s*(no|nie)\b"],"S"),
("Who is the owner, and may you copy her on emails to customers?","Kto jest właścicielem i czy możesz dodać ją do kopii maili do klientów?","Ms Zielińska; no",[r"zieli[nń]sk.*(no|nie|never|nigdy)"],"S"),
("How should you describe Mr Nowak?","Jak należy określać Pana Nowaka?","As the service manager (kierownik serwisu), not the owner",[r"kierownik|service manager|manager"],"S"),
("What must you send by 3 p.m., and to whom?","Co musisz wysłać do 15:00 i komu?","Next day's visit list to Mr Nowak",[r"nowak"],"S")]
L={1:'es',2:'zh',3:'fr',4:'pt',5:'pl'}
out={f'P{p}':[Q(*x,L[p]) for x in qs] for p,qs in zip(range(1,6),[P1,P2,P3,P4,P5])}
json.dump(out,open('directuse/questions.json','w'),indent=1,ensure_ascii=False)
print({k:len(v) for k,v in out.items()}, sum(len(v) for v in out.values())*2, 'S',sum(1 for v in out.values() for x in v if x['type']=='S')*2)
