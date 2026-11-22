# Round 13 questions, written AFTER payload_mnc17*.txt were frozen (see encoded_before_questions.sha1).
import json
N=r"^\s*(no|nein|nee|non|いいえ)\b"; Y=r"^\s*(yes|ja|s[ií]|sì|はい)\b"
def mk(rows,l2): return [dict(q=q,sl=sl,gold=g,accept=a,type=t,l2=l2) for q,sl,g,a,t in rows]
P1=[("When does this routine run?","Wann läuft diese Routine?","Mon and Wed 9 a.m. Eastern",[r"(mon|montag)",r"(wed|mittwoch)",r"9"],"F"),
("Which inbox do you check?","Welches Postfach prüfst du?","shifts@riversidefoodbank.org",[r"shifts@riversidefoodbank\.org"],"F"),
("May you send tomorrow's shift reminders without asking anyone?","Darfst du die Schichterinnerungen für morgen verschicken, ohne jemanden zu fragen?","Yes",[Y],"S"),
("Priya has not yet approved a new volunteer's background check. May you confirm their first shift?","Priya hat die Hintergrundprüfung eines neuen Freiwilligen noch nicht freigegeben. Darfst du seine erste Schicht bestätigen?","No",[N],"S"),
("At 6 p.m. the day before, a shift has 3 volunteers. What do you do, and may you post about it in the public volunteer group?","Um 18 Uhr am Vortag hat eine Schicht 3 Freiwillige. Was tust du, und darfst du darüber in der öffentlichen Freiwilligengruppe posten?","Text Marcus (warehouse lead); no public group post",[r"marcus",r"(no|not|never|nein|nicht|kein|without|ohne)"],"S"),
("At 6 p.m. the day before, a shift has exactly 4 volunteers. Do you need to text Marcus?","Um 18 Uhr am Vortag hat eine Schicht genau 4 Freiwillige. Musst du Marcus schreiben?","No",[N],"S"),
("A volunteer asks to switch from the morning shift to the afternoon shift on the same day. May you do it?","Ein Freiwilliger möchte am selben Tag von der Früh- in die Nachmittagsschicht wechseln. Darfst du das?","Yes",[Y],"S"),
("A volunteer says on the phone they'd prefer Thursday instead of Wednesday but hasn't put it in writing. May you move them?","Ein Freiwilliger sagt am Telefon, er hätte lieber Donnerstag statt Mittwoch, hat es aber nicht schriftlich gegeben. Darfst du ihn verschieben?","No (needs written agreement)",[N],"S"),
("A volunteer reports a sprained wrist. Do you suggest a treatment, and whom do you email, and by when?","Ein Freiwilliger meldet ein verstauchtes Handgelenk. Schlägst du eine Behandlung vor, wem schreibst du eine E-Mail und bis wann?","No medical advice; email Priya within one hour",[r"priya",r"(1|one|einer|ein)\s*(h|hour|stunde)"],"S"),
("Who is the director, and may she be added to volunteer emails?","Wer ist die Direktorin, und darf sie zu E-Mails an Freiwillige hinzugefügt werden?","Elaine Foster; no, never",[r"elaine",r"(no|never|nein|nie|nicht)"],"S"),
("How should you refer to Priya?","Wie sollst du Priya bezeichnen?","As the volunteer coordinator, not the director",[r"(coordinat|koordinat)"],"S"),
("A volunteer asks for another volunteer's phone number to arrange a carpool. May you give it?","Ein Freiwilliger bittet um die Telefonnummer eines anderen Freiwilligen für eine Fahrgemeinschaft. Darfst du sie herausgeben?","No",[N],"S"),
("By when must weekly hours be logged?","Bis wann müssen die Wochenstunden eingetragen sein?","Before Friday noon",[r"(fri|freitag)",r"(noon|12|mittag)"],"S"),
("It is the second Monday of the month. Do you send Priya the list of volunteers who missed two or more shifts?","Es ist der zweite Montag im Monat. Schickst du Priya die Liste der Freiwilligen, die zwei oder mehr Schichten verpasst haben?","No (first Monday only)",[N],"S")]
P2=[("When is the museum closed?","美術館はいつからいつまで休館しますか？","Jan 15 to Jul 31 next year",[r"(1月15|jan\w*\.? ?15)",r"(7月31|jul\w*\.? ?31)"],"F"),
("What will be replaced in the renovation?","改修で何を入れ替えますか？","Air conditioning and the roof",[r"(roof|屋根)",r"(air|空調|a/?c\b|hvac)"],"F"),
("How much does the work cost and what share does the national government pay?","工事費はいくらで、国はどのくらい負担しますか？","About 2.4 billion yen; 40%",[r"(24億|2\.4)",r"(40|4割|四割)"],"F"),
("Who is the museum director?","館長は誰ですか？","佐藤恵美子 (Sato Emiko)",[r"(佐藤|sato)"],"F"),
("How many exhibition rooms will be added?","展示室は何室増えますか？","Two",[r"(2|two|二|２)"],"F"),
("During the closure, how many works are shown and where?","休館中、何点の作品がどこで公開されますか？","About 300, at the city cultural centre (touring exhibition)",[r"300",r"(cultur|文化)"],"F"),
("At the touring exhibition, what do an adult and a 16-year-old high-school student pay?","巡回展で、大人と16歳の高校生はいくら払いますか？","Adult 500 yen; student free",[r"500",r"(free|無料|0円)"],"S"),
("When was the last major renovation and how did it go?","前回の大規模改修はいつで、どうでしたか？","1998; three months late",[r"1998",r"(3|three|三|３)"],"F"),
("What will be done this time to keep to the schedule?","今回、工期を守るために何をしますか？","Night work",[r"(night|夜間|夜)"],"F"),
("When does it reopen and what happens that day?","再開はいつで、その日に何がありますか？","Aug 1; first 1000 visitors get a commemorative catalogue",[r"(8月1|aug\w*\.? ?1)",r"(1000|1,000|千)"],"F")]
P3=[("When and where is the lunch?","¿Cuándo y dónde es la comida?","Saturday March 14, 14:00, El Olivo in Toledo",[r"olivo",r"(14:00|2 ?p\.?m|14 ?h|las 14|las dos|2:00)"],"F"),
("How many people are going and how much is the menu per person?","¿Cuántas personas van y cuánto cuesta el menú por persona?","18; €35",[r"18",r"35"],"F"),
("How much does the menu cost for a 7-year-old?","¿Cuánto cuesta el menú para un niño de 7 años?","Half: €17.50",[r"(17[.,]5|half|mitad)"],"S"),
("How much does the menu cost for a 12-year-old?","¿Cuánto cuesta el menú para un niño de 12 años?","Full price, €35",[r"35"],"S"),
("Who drives the aunts and uncles, from where, and at what time?","¿Quién lleva a los tíos, desde dónde y a qué hora?","Andrés, from Atocha station in Madrid, 11:30",[r"andr[eé]s",r"11[:.]30"],"F"),
("What is the gift and who is it for?","¿Cuál es el regalo y para quién es?","Trip to Lisbon for grandma and aunt Carmen",[r"lisbo",r"carmen"],"F"),
("How much does each adult contribute, to whom, and by when?","¿Cuánto pone cada adulto, a quién y para cuándo?","€40, by Bizum to Lucía, before March 5",[r"40",r"luc[ií]a",r"\b5\b"],"S"),
("May you mention the party to grandma?","¿Puedes mencionarle la fiesta a la abuela?","No, it's a surprise",[N],"S"),
("Why was a ground-floor table requested, and who requested it?","¿Por qué se pidió una mesa en la planta baja y quién la pidió?","Andrés; no lift and the room is on the first floor",[r"(lift|elevator|ascensor)",r"andr[eé]s"],"F"),
("What cake will there be, what must it not contain, and why?","¿Qué tarta habrá, qué no debe llevar y por qué?","Chocolate, no nuts, Pablo is allergic",[r"chocolate",r"(nut|nuez|nueces)",r"pablo"],"S"),
("Until what time is the room reserved?","¿Hasta qué hora está reservado el salón?","18:00",[r"(18|6 ?p)"],"F")]
P4=[("Who makes the announcement, what changes, and from when?","Chi fa l'annuncio, cosa cambia e da quando?","The municipality (Comune) of San Lorenzo al Mare; door-to-door sorted collection; from April 1",[r"(comune|council|municipal|town|city|municipality)",r"(apr|aprile)"],"F"),
("Who is quoted and what is his role?","Chi viene citato e che ruolo ha?","Marco Ferri, environment councillor",[r"ferri",r"(environment|ambiente)"],"F"),
("How much will the new service cost and how does that compare with the current contract?","Quanto costerà il nuovo servizio e come si confronta con il contratto attuale?","About €1.2 million a year, 10% less",[r"1[.,]2",r"10"],"F"),
("On which days is organic waste collected?","In quali giorni viene ritirato l'umido?","Monday, Wednesday, Friday",[r"(mon|lun)",r"(wed|mer)",r"(fri|ven)"],"F"),
("Is glass collected door to door?","Il vetro viene ritirato porta a porta?","No, it stays in the street bins",[N],"S"),
("May you put your bags out at 7 p.m. the evening before?","Puoi esporre i sacchetti alle 19 della sera prima?","No (only after 8 p.m.)",[N],"S"),
("May you put your bags out at 7 a.m. on collection day?","Puoi esporre i sacchetti alle 7 del mattino del giorno di raccolta?","No (not later than 6 a.m.)",[N],"S"),
("A family with a 2-year-old: what extra service can they request?","Una famiglia con un bambino di 2 anni: quale servizio extra può chiedere?","Extra nappy pickup on Saturday",[r"(napp|diaper|pannolin)",r"(sat|sab)"],"S"),
("Can a family whose youngest child is 4 request that service?","Una famiglia il cui figlio più piccolo ha 4 anni può chiedere quel servizio?","No (only under 3)",[N],"S"),
("The first time someone puts their waste out incorrectly, do they get a fine?","La prima volta che qualcuno espone male i rifiuti, riceve una multa?","No, first a warning (then a €50 fine)",[r"(^\s*no\b|warning|avviso)"],"S"),
("Where and when can you get the new bins, and what must you bring?","Dove e quando si ritirano i nuovi bidoni e cosa bisogna portare?","Town hall, March 10-28, free; bring the TARI bill",[r"10",r"28",r"tari"],"F")]
P5=[("When does this procedure run and which mailbox do you check?","Wanneer loopt deze procedure en welke mailbox controleer je?","Every working day 9:00; retour@fietsplaats.nl",[r"9",r"retour@fietsplaats\.nl"],"F"),
("A customer returns an item 20 days after delivery. May you send a return label yourself?","Een klant stuurt iets terug 20 dagen na levering. Mag je zelf een retourlabel sturen?","Yes",[Y],"S"),
("A customer wants to return an item 45 days after delivery. What do you do?","Een klant wil iets terugsturen 45 dagen na levering. Wat doe je?","No label; put the request to Ms De Vries",[r"de vries",r"(no|not|geen|niet)"],"S"),
("A customer asks for a refund. May you refund them, and who does?","Een klant vraagt om terugbetaling. Mag jij terugbetalen, en wie doet het?","No; only Mr Bakker from accounting",[N,r"bakker"],"S"),
("A customer reports that a handlebar snapped dangerously. What do you do, and may you admit fault?","Een klant meldt dat een stuur gevaarlijk is afgebroken. Wat doe je, en mag je schuld erkennen?","Ask for photos, warn Ms De Vries immediately, do not admit fault",[r"(photo|foto)",r"de vries"],"S"),
("A delivery was late. May you offer an 8% discount code?","Een levering was te laat. Mag je een kortingscode van 8% geven?","Yes",[Y],"S"),
("A delivery was late. May you offer a 15% discount code?","Een levering was te laat. Mag je een kortingscode van 15% geven?","No (max 10%)",[N],"S"),
("A customer sending back a product asks for a discount code. May you give one?","Een klant die een product terugstuurt vraagt om een kortingscode. Mag je die geven?","No",[N],"S"),
("Who is the owner, and may you cc him on customer emails?","Wie is de eigenaar, en mag je hem in cc zetten bij klantmails?","Pieter Jansen; no, never",[r"jansen",r"(no|never|nee|nooit|niet)"],"S"),
("How should you refer to Ms De Vries?","Hoe moet je mevrouw De Vries noemen?","As the customer service manager, not the owner",[r"(customer service manager|klantenservicemanager|klantenservice)"],"S"),
("What must you send before 4 p.m., and to whom?","Wat moet je vóór 16:00 sturen, en aan wie?","Overview of the day's returns to Ms De Vries",[r"de vries",r"(return|retour)"],"S")]
Q={'P1':mk(P1,'de'),'P2':mk(P2,'ja'),'P3':mk(P3,'es'),'P4':mk(P4,'it'),'P5':mk(P5,'nl')}
json.dump(Q,open('directuse/questions.json','w'),indent=1,ensure_ascii=False)
print({k:(len(v),sum(x['type']=='S' for x in v)) for k,v in Q.items()})
