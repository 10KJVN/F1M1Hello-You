import os
import time
play = True

Q = 1

while play:
    while Q == 1:
        print("Jij staat in de schoenen van de 8-jarige Pawrana en haar vader.")
        print("Je woont met je familie in Afghanistan. (Let op gebruik HOOFDLETTERS!)")
        print("")
        print("Je krijgt een dreigbrief van de Taliban.")
        print("'Parwana we moeten nu gaan.' Zegt hij in shock.")
        print("")
        print("A: Je pakt je favoriete knuffel en gaat mee.")
        print("B: Je blijft toch in Afghanistan.")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 3
            os.system('cls')
        elif InputText == "B":
            Q = 2
            os.system('cls')
    
    while Q == 2:
        print("De Taliban heeft je broer al vermoord.")
        print("Het gevaar dat jouw datzelfde lot overkomt is groot.")
        print("Er is geen tijd te verliezen. ")
        print("")
        print("A: Je vlucht dezelfde avond nog.")
        print("B: Je gaat het verzet in.")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 4
            os.system('cls')
        if InputText == "B":
            Q = 6
            os.system('cls')

    while Q == 3:
        print("Je hebt als doel om naar Europa te vluchten.")
        print("Alleen hoe is het probleem. Je moet eerst nog LEVEND, uit Afghanistan komen.")
        print("Wat doe je nu?")
        print("")
        print("A: Reis 's nachts door de bergen naar de grens van Turkije. ")
        print("B: Probeer te vluchten met een vliegtuig.")
        print("")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 5
            os.system('cls')
        if InputText == "B":
            Q = 4
            os.system('cls')

    while Q == 4:
        print("Je komt aan in de hoofdstad Kabul.")
        print("De enigste vlucht beschikbaar is naar Turkije.")
        print("")
        print("Type A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 5
            os.system('cls')

    while Q == 5:
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
            Q = 9
            os.system('cls')
        if InputText == "B":
            Q = 7
            os.system('cls')

    while Q == 6:
        print("Je hebt Parwana achtergelaten bij je familie, om te vechten.")
        print("Er is nu geen weg meer terug. Jij en je broer hebben al eerder in het leger gevochten.")
        print("Vandaar dat je geen training nodig hebt, je wilt gewoon een toekomst voor je gezin.")
        print("")
        print("Een kamp van het verzet niet zo ver van waar jij zit wordt belaagd door de Taliban.")
        print("Wat doe je?")
        print("")
        print("A: Je gaat er naartoe om te vechten!")
        print("B: Je bent bang om dood te gaan, dus je ontvlucht het leger.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 8
            os.system('cls')
        if InputText == "B":
            Q = 10 
            os.system('cls')

    while Q == 7:
        print("Na veel lopen en meeliften met auto's komen jij en Parwana aan in Izmir.")
        print("Er is een kleine markt waar je eten koopt voor jezelf en Parwana.")
        print("")
        print("Je vraagt aan de verkopers hoe je het snelste naar Griekenland kan")
        print("Uitendelijk heb je besloten om een mensensmokkelaar te betalen voor een gevaarlijke boottocht.")
        print("")
        print("Er is maar 1 boot, het risico is groot. Maar er is geen andere optie.")
        print("Type: A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 13
            os.system('cls')
    
    while Q == 8:
        print("Eenmaal in gebied van de Taliban, wordt je belaagd door een verrassings aanval.")
        print("Jij en de rest van de soldaten zijn gevangen genomen.")
        print("Wat doe je nu? Je executie opwachten, of de andere aansporen om te ontsnappen.")
        print("")
        print("A: Wachten op executie.")
        print("B: Medegevangen aansporen te ontsnappen.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 15
            os.system('cls')
        if InputText == "B":
            Q = 14
            os.system('cls')

    while Q == 9:
        print("Je gaat opzoek naar eten voor jouw en Parwana.")
        print("Terwijl je rond vraagt naar een plek om te eten in het Engels maakt het je verdacht.")
        print("Iemand licht de politie in.")
        print("Je herinnert je dat je illegaal in Turkije bent.")
        print("")
        print("Wat doe je, steel eten en sla op de vlucht. Of ga je je verstoppen voor de politie?")
        print("A: Verstoppen.")
        print("B: Stelen en vluchten.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 11
            os.system('cls')
        if InputText == "B":
            Q = 18

    while Q == 10:
        print("Je bent succesvol het leger ontsnapt.")
        print("Het enige nadeel is dat je nu wordt gezocht door zowel de Taliban als het Verzet.")
        print("Er is geen andere optie, je moet zo snel mogelijk weg.")
        print("")
        print("Je boekt op het vliegveld direct een vlucht naar Griekenland..")
        print("Press A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 12
            os.system('cls')

    while Q == 11:
        print("Je ziet een leeg staande stal op de markt en doet je voor als verkoper. Terwijl Parwana er achter schuilt.")
        print("Je verkoopt zelfs een achtergelaten appel aan de politie, ze groeten je vriendelijk.")
        print("")
        print("Aangezien de politie je ervoor heeft betaald, kan je nu in je eentje naar Duitsland.")
        print("Press A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 16
            os.system('cls')

    while Q == 12:
        print("Je hebt alleen een vliegtuig naar Griekenland genomen.")
        print("Je mist je familie, maar moet toch door.")
        print("Je wilt naar Duitsland of Nederland, en je familie daar naartoe halen.")
        print("")
        print("Wat doe je eerst?")
        print("A: Reizen naar Duitsland.")
        print("B: Werken in Griekenland voor geld.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 16
            os.system('cls')
        if InputText == "B":
            Q = 20
            os.system('cls')

    while Q == 13:
        print("Na een lange en gevaarlijke reis, komen jij en Parwana aan in Griekenland.")
        print("Overal om je heen zie je kampen met vluchtelingen..")
        print("")
        print("De toekomst ziet er grimmig uit. Totdat een man in een aparte outfit naar jullie toekomt.")
        print("Het is iemand van Vluchtelingen werk Nederland!")
        print("In het engels bied hij aan jouw en Parwana naar Nederland te brengen.")
        print("")
        print("Je had eigenlijk Duitsland in gedachte, maar dit is een kans uit duizenden!")
        print("Wat doe je?")
        print("")
        print("A: Nederland.")
        print("B. Duitsland")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 21
            os.system('cls')
        if InputText == "B":
            Q = 16
            os.system('cls')
    
    while Q == 14:
        print("Je hebt je medegevangen aangespoord om te ontsnappen.")
        print("Het is jouw en 1 andere man gelukt te ontsnappen")
        print("De rest is helaas gesneuveld, maar na een lange reis komt de man een oude vriend tegen..")
        print("Jullie leggen de situatie uit, en hij biedt aan jullie naar Duitsland te brengen.")
        print("")
        print("Deze kans is te goed om te laten gaan.")
        print("Press A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 19
            os.system('cls')
 
    while Q == 15:
        print("*8 uur later.*")
        print("")
        time.sleep(8)
        print("Je denkt aan je familie.")
        print("Maar, je hebt geen spijt van de keuzes die je hebt gemaakt.")
        print("")
        print("Een lid van de Taliban haalt je uit je cel en doet een zak over je hoofd.")
        print("")
        print("Je bent geëxecuteerd.")
        print("")
        print("GAME OVER")
        print("Wil je herstarten? Y/N")
        InputText = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("Script herstarten...")
            print("")
        if scriptinput == "n" or scriptinput == "N":
            print("Thanks for playing")
            print("")
            os.system('cls')
            exit()

    while Q == 16:
        print("Na veel tussen stops, werken  en meeliften. Kom je na een half jaar aan in Duitsland.")
        print("Je zit ongeveer anderhalf jaar in een Azielzoekers kamp.")
        print("Een aardige man met een smartphone heeft je die laten gebruiken om je familie te bellen.")
        print("")
        print("Je vrouw, dochter en zoon konden alleen maar huilen, maar waren vooral blij dat je nog leefde.")
        print("Ook vertelde je ze dat je momenteel in Duitsland bent.")
        print("")
        print("Je belooft om ze naar Europa te halen..")
        print("Press A to continue...")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 17
            os.system('cls')
    
    while Q == 17:
        print("Momenteel in Duitsland, zijn er inmiddels 2 jaar voorbij.")
        print("Of je nou alleen of met Parwana bent gekomen naar dit Azielszoekerscentrum.")
        print("")
        time.sleep(2)
        print("Je denkt aan de toekomst van jouw en je familie. Je twijfelt of je dat wilt opbouwen in Nederland of Duitsland.")
        print("In duitsland heb je meer kans op succes, maar Nederland heeft betere educatie, heb je je laten vertellen.")
        print("")
        time.sleep(2)
        print("Wat doe je?")
        print("A: Verblijf in Nederland.")
        print("B: Verblijf in Duitsland.")
        InputText = input().capitalize()
        if InputText == "A":
            Q = 21
            os.system('cls')
        if InputText == "B":
            Q = 19
            os.system('cls')
    
    while Q == 18:
        print("Je steelt eten en rent weg met Parwana aan je hand.")
        print("De politie achtervolgt je, ze zitten op je hielen!")
        print("")
        time.sleep(2)
        print("Terwijl je rent, struikelt parwana.")
        print("Natuurlijk bezorgd, probeer je je dochter gerust te stellen.")
        print("Jullie worden opgepakt, en in de gevangenis gestopt voor illegaal verblijf en het stelen van eten.")
        print("Je dochter, Parwana eindigt in een weeshuis.")
        print("")
        time.sleep(2)
        print("GAME OVER")
        print("Wil je herstaten? Y/N")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("Script herstarten...")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("Thanks for playing")
            print("")
            os.system('cls')
            exit()

    while Q == 19:
        print("Gefliciteerd, Na je lange reis ben je eindelijk in Duitsland geaccepteerd.")
        print("Je krijgt een verblijfsvergunning, maar gaat eerst hulp vragen aan het Rode kruis.")
        print("Zodat je gezin ook een toekomst kan opbouwen in Duitsland, zonder gevaar van de Taliban.")
        print("")
        time.sleep(3)
        print("*3 Maanden later*")
        print("")
        print("Je Familie wordt overgevlogen naar Duitsland, waar jullie van de overheid een huis krijgen.")
        print("De Kinderen gaan naar school, Parwana's vader heeft een baan.")
        print("en daar leven jullie nog lang en gelukkig.")
        print("")
        print("GAME END.")
        print("Wil je herstarten? Y/N")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("Script herstarten...")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("Thanks for playing")
            print("")
            os.system('cls')
            exit()
    
    while Q == 20:
        print("Je hebt geld nodig, dus je zoekt naar zwart werk in Griekenland.")
        print("Mensen krijgen vermoedens dat je illegaal in Griekenland bent en schakelen de politie in.")
        print("Je probeert het to ontkennen, maar ze zien door je act heen.")
        print("")
        time.sleep(2)
        print("Je wordt aangehouden en gaat de gevangenis is.")
        print("Na een maand krijg je te horen dat je terug moet naar Afghanistan..")
        print("")
        time.sleep(2)
        print("GAME OVER")
        print("wil je herstarten? Y/N")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("Script herstarten...")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("Thanks for playing")
            print("")
            os.system('cls')
            exit()

    while Q == 21:
        print("Je komt na een paar dagen aan in Nederland.")
        print("Je legt je verhaal uit aan vluchtelingenwerk Nederland.")
        print("Na een paar maanden, in samenwerking met het Rode Kruis lukt het jullie om je familie naar Nederland te halen.")
        print("")
        time.sleep(2)
        print("Na een inburgeringscursus, gaan de kinderen naar school en vindt je een baan.")
        print("Je wordt door je omgeving geaccepteerd in de samenleving and voelt je gelukkig in Nederland.")
        print("Zo leven jij en je gezin gelukkig in Nederland, bouwend aan de toekomst.")
        print("")
        time.sleep(2)
        print("GAME END.")
        print("Wil je herstarten? Y/N")
        scriptinput = input().capitalize()
        if scriptinput == "y" or scriptinput == "Y":
            Q = 1
            print("Script herstarten...")
            print("")
            os.system('cls')
        elif scriptinput == "n" or scriptinput == "N": 
            print("Thanks for playing")
            print("")
            os.system('cls')
            exit()