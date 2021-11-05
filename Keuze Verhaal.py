import os
from typing import Text

Q1 = True
Q2 = False
Q3 = False
Q4 = False
Q5 = False
Q6 = False
Q7 = False
Q8 = False
Q9 = False
Q10 = False
Q11 = False
Q12 = False
Q13 = False
Q14 = False
Q15 = False
Q16 = False
Q17 = False
Q18 = False
Q19 = False
Q20 = False
Q21 = False

import time
#Voor het vertrek.
while Q1:
    print("Jij staat in de schoenen van de 8-jarige Pawrana en haar vader.")
    print("Je woont met je familie in Afghanistan. (Let op gebruik HOOFDLETTERS!)")
    print("")
    time.sleep(2)
    print("Je krijgt een dreigbrief van de Taliban.")
    print("'Parwana we moeten nu gaan.' Zegt hij in shock.")
    time.sleep(1)
    print("A: Je pakt je favoriete knuffel en gaat mee.")
    print("B: Je blijft toch in Afghanistan.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q1 = False
        Q3 = True
        os.system('cls')
    if InputText == "B":
        Q1 = False
        Q2 = True
        os.system('cls')
#Twijfelen tussen Vechten of Vluchten.
while Q2:
    print("De Taliban heeft je broer al vermoord.")
    print("Het gevaar dat jouw datzelfde lot overkomt is groot.")
    print("Er is geen tijd te verliezen. ")
    time.sleep(2)
    print("A: Je vlucht dezelfde avond nog.")
    print("B: Je gaat het verzet in.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q2 = False
        Q4 = True
        os.system('cls')
    if InputText == "B":
        Q2 = False
        Q6 = True
        os.system('cls')
#Veilige Route, Vluchten
while Q3:
    print("Je hebt als doel om naar Europa te vluchten.")
    print("Alleen hoe is het probleem. Je moet eerst nog LEVEND, uit Afghanistan komen.")
    time.sleep(2)
    print("Wat doe je nu?")
    print("A: Reis 's nachts door de bergen naar de grens van Turkije. ")
    print("B: Probeer te vluchten met een vliegtuig.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q3 = False
        Q5 = True
        os.system('cls')
    if InputText == "B":
        Q3 = False
        Q4 = True
        os.system('cls')
#Makkelijkste manier naar Turkije.
while Q4:
    print("Je komt aan in de hoofdstad Kabul.")
    print("De enigste vlucht beschikbaar is naar Turkije.")
    time.sleep(2)
    print("Type A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q4 = False
        Q5 = True
        os.system('cls')
#Toch gekozen om te vluchten. Locatie: Turkije.
while Q5:
    print("Na een lange reis kom je aan in Turkije.")
    print("Je paspoort is verlopen dus je bent er eigenlijk illegaal..")
    print("Ook hebben jij en Parwana al 2 dagen niks gegeten.")
    print("Wat doe je?")
    print("")
    print("A: Ga opzoek naar eten.")
    print("B: Reis verder naar Izmir.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q5 = False
        Q9 = True
        os.system('cls')
    if InputText == "B":
        Q5 = False
        Q7 = True
        os.system('cls')
#Je hebt gekozen om te Vechten.
while Q6:
    print("Je hebt Parwana achtergelaten met je familie, om te vechten.")
    print("Er is nu geen weg meer terug. Jij en je broer hebben al eerder in het leger gevochten.")
    print("Vandaar dat je geen training nodig hebt, je wilt gewoon een toekomst voor je gezin.")
    time.sleep(2)
    print("")
    print("Een kamp van het verzet niet zo ver van waar jij zit wordt belaagd door de Taliban.")
    print("Wat doe je?")
    print("A: Je gaat er naartoe om te vechten!")
    print("B: Je bent bang om dood te gaan, dus je ontvlucht het leger.")
    InputText = input().capitalize()
    if InputText == "A":
        Q6 = False
        Q8 = True
        os.system('cls')
    if InputText == "B":
        Q6 = False
        Q10 = True
        os.system('cls')
#Izmir, opweg naar Griekeland.
while Q7:
    print("Na veel lopen en meeliften met auto's komen jij en Parwana aan in Izmir.")
    print("Er is een kleine markt waar je eten koopt voor jezelf en Parwana.")
    time.sleep(1)
    print("")
    print("Je vraagt aan de verkopers hoe je het snelste naar Griekenland kan")
    print("Uitendelijk heb je besloten om een mensensmokkelaar te betalen voor een gevaarlijke boottocht.")
    time.sleep(2)
    print("Er is maar 1 boot, het risico is groot. Maar er is geen andere optie.")
    print("Type A to continue...")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q7 = False
        Q13 = True
        os.system('cls')
#Verslagen door de Taliban.
while Q8:
    print("Eenmaal in gebied van de Taliban, wordt je belaagd door een verrassings aanval.")
    print("Jij en de rest van de soldaten zijn gevangen genomen.")
    print("Wat doe je nu? Je executie opwachten, of de andere aansporen om te ontsnappen.")
    print("")
    time.sleep(2)
    print("A: Wachten op executie.")
    print("B: Medegevangen aansporen te ontsnappen.")
    InputText = input().capitalize()
    if InputText == "A":
        Q8 = False
        Q15 = True
        os.system('cls')
    if InputText == "B":
        Q8 = False
        Q14 = True
        os.system('cls')
#Ontwijk de politie.
while Q9:
    print("Je gaat opzoek naar eten voor jouw en Parwana.")
    print("Terwijl je rond vraagt naar een plek om te eten in het Engels maakt het je verdacht.")
    print("Iemand licht de politie in.")
    print("Je herinnert je dat je illegaal in Turkije bent.")
    print("")
    time.sleep(2)
    print("Wat doe je, steel eten en sla op de vlucht. Of ga je je verstoppen voor de politie?")
    print("A: Verstoppen.")
    print("B: Stelen en vluchten.")
    InputText = input().capitalize()
    if InputText == "A":
        Q9 = False
        Q11 = True
        os.system('cls')
    if InputText == "B":
        Q9 = False
        Q18 = True
        os.system('cls')
#Leger ontsnapt.
while Q10:
    print("Je bent succesvol het leger ontsnapt.")
    print("Het enige nadeel is dat je nu wordt gezocht door zowel de Taliban als het Verzet.")
    print("Er is geen andere optie, je moet zo snel mogelijk weg.")
    time.sleep(2)
    print("Je boekt op het vliegveld direct een vlucht naar Griekenland..")
    print("")
    print("Press A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q10 = False
        Q12 = True
        os.system('cls')
#Politie afgeschud, genoeg verdient om naar Duitsland te gaan.
while Q11:
    print("Je ziet een leeg staande stal op de markt en doet je voor als verkoper. Terwijl Parwana er achter schuilt.")
    print("Je verkoopt zelfs een achtergelaten appel aan de politie, ze groeten je vriendelijk.")
    time.sleep(2)
    print("Aangezien de politie je ervoor heeft betaald, kan je nu in je eentje naar Duitsland.")
    print("")
    print("Press A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q11 = False
        Q17 = True
#Griekenland aangekomen, nu nog verder in Europa
while Q12:
    print("Je hebt alleen een vliegtuig naar Griekenland genomen.")
    print("Je mist je familie, maar moet toch door.")
    print("Je wilt naar Duitsland of Nederland, en je familie daar naartoe halen.")
    time.sleep(1)
    print("")
    print("Wat doe je eerst?")
    print("A: Reizen naar Duitsland.")
    print("B: Werken in Griekenland voor geld.")
    InputText = input().capitalize()
    if InputText == "A":
        Q12 = False
        Q16 = True
    if InputText == "B":
        Q12 = False
        Q20 = True
#keuze tussen NL of DE.
while Q13:
    print("Na een lange en gevaarlijke reis, komen jij en Parwana aan in Griekenland.")
    print("Overal om je heen zie je kampen met vluchtelingen..")
    time.sleep(2)
    print("")
    print("De toekomst ziet er grimmig uit. Totdat een man in een aparte outfit naar jullie toekomt.")
    time.sleep(2)
    print("Het is iemand van Vluchtelingen werk Nederland!")
    print("In het engels bied hij aan jouw en Parwana naar Nederland te brengen.")
    print("")
    print("Je had eigenlijk Duitsland in gedachte, maar dit is een kans uit duizenden!")
    print("Wat doe je?")
    time.sleep(2)
    print("A: Nederland.")
    print("B. Duitsland")
    InputText = input().capitalize()
    if InputText == "A":
        Q13 = False
        Q15 = True
        print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "B":
        Q13= False
        Q12 = True
#Je gaat naar duitsland
while Q14:
    print("Je hebt je medegevangen aangespoord om te ontsnappen.")
    print("Het is jouw en 1 andere man gelukt te ontsnappen")
    print("De rest is helaas gesneuveld, maar na een lange reis komt de man een oude vriend tegen..")
    print("Jullie leggen de situatie uit, en hij biedt aan jullie naar Duitsland te brengen.")
    print("")
    time.sleep(2)
    print("Deze kans is te goed om te laten gaan.")
    print("Press A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q14 = False
        Q19 = True
#Extra Einde, verkeerde keuzes. Doodlopend.
while Q15:
    print("*8 uur later.*")
    time.sleep(1)
    print("Je denkt aan je familie.")
    print("")
    print("Maar, je hebt geen spijt van de keuzes die je hebt gemaakt.")
    time.sleep(2)
    print("Een lid van de Taliban haalt je uit je cel en doet een zak over je hoofd.")
    time.sleep(3)
    print("Je wordt geëxecuteerd.")
    print("")
    print("GAME OVER.")
    print("Wil je opniew herstarten? Y/N")
    InputText = input().capitalize()
    if InputText == "y" or InputText == "Y":
        Q15 = False
        Q1 = True
        os.system('cls') 
    if InputText == "n" or InputText == "N":
        print("[o]Thanks for running")
        print("")
        os.system('cls')
    elif InputText == () :
        print("Invalid choice.")
        exit()
#Duitsland, azielzoekers kamp.
while Q16:
    print("Na veel tussen stops, werk en meeliften. Kom je na een half jaar aan in Duitsland.")
    print("Je zit ongeveer anderhalf jaar in een Azielzoekers kamp.")
    print("")
    print("Een aardige man met een smartphone heeft je die laten gebruiken om je familie te bellen.")
    print("Je vrouw, dochter en zoon konden alleen maar huilen, maar waren vooral blij dat je nog leefde.")
    print("Ook vertelde je ze dat je momenteel in Duitsland bent.")
    time.sleep(2)
    print("")
    print("Press A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q16 = False
        Q17 = True

while Q17:
    print("Je krijgt levenslang vanwege land verraad.")
    print("Je familie probeert nog te onstnappen")
    print("Je familie wordt gepakt.")
    print("Type: A to continue")
    InputText = input().capitalize()
    if InputText == "A":
        Q17 = False
        Q21 = True
#EINDE 1 Doodlopend einde
while Q18:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True
#EINDE 2 Gelukkig in [D]uitsland.
while Q19:
    print("")
    print("Hij heeft een bomgordel om zich heen")
    print("Iedereen aan boord probeerd hem over te halen om het niet te doen.")
    print("Hij luisterd niet en laat zijn vest exploderen.")
    print("Iedereen aanboord is dood")
    print("")
    print("GAME OVER")
    print("Wil jij dit script herstarten? Y/N")
    print("")
    scriptinput = input().capitalize()
    if scriptinput == "y" or scriptinput == "Y":
        Q19 = False
        Q1 = True
        print("[o]*Het script word gerestart*")
        print("")
    elif scriptinput == "n" or scriptinput == "N": 
        print("[o]Thanks for running")
        exit()
#Einde 3 Einde in gevangenis
while Q20:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True
#EINDE 4 G[e]lukkig in Nederland
while Q21:
    print("Je familie is gepakt en jullie worden allemaal gestraft.")
    print("De overheid heeft besloten jullie te excuteren.")
    print("GAME OVER")
    print("Wil je herstarten? Y/N")
    scriptinput = input().capitalize()
    if scriptinput == "y" or scriptinput == "Y":
        Q21 = False
        Q1 = True
        print("[o]*Het script word gerestart*")
        print("")
    elif scriptinput == "n" or scriptinput == "N": 
        print("[o]Thanks for running")
        exit()