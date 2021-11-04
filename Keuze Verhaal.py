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
    if InputText == "B":
        Q1 = False
        Q2 = True
#Twijfelen tussen Vechten of Vluchten.
while Q2:
    print("De Taliban heeft je broer al vermoord.")
    print("Het gevaar dat jouw datzelfde lot overkomt is groot.")
    print("Er is geen tijd te verliezen. ")
    time.sleep(2)
    print("A: Je vlucht dezelfde avond nog.")
    print("B: Je gaat het verzet in.")
    InputText = input().capitalize()
    if InputText == "A":
        Q2 = False
        Q4 = True
    if InputText == "B":
        Q2 = False
        Q6 = True
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
    if InputText == "B":
        Q3 = False
        Q4 = True
#Laatste kans om te kiezen tussen vluchten of vechten.
while Q4:
    print("Je komt aan in de hoofdstad Kabul.")
    print("De enigste vlucht beschikbaar is naar Turkije.")
    print("Terwijl je in Pakistan misschien meer kans hebt op succes.")
    time.sleep(2)
    print("Wat ben je van plan te doen.")
    print("A: Ga naar Turkije.")
    print("B: Ga naar Pakistan.")
    InputText = input().capitalize()
    if InputText == "A":
        Q4 = False
        Q5 = True
    if InputText == "B":
        Q4 = False
        Q6 = True
#Toch gekozen om te vluchten. Locatie: Turkije.
while Q5:
    print("Na je lange reis kom je aan in Turkije.")
    print("Je paspoort is verlopen dus je bent er eigenlijk illegaal..")
    print("Ook hebben jij en Parwana al 2 dagen niks gegeten.")
    print("Wat doe je?")
    print("A: Ga opzoek naar eten.")
    print("B: Reis verder naar Izmir.")
    InputText = input().capitalize()
    if InputText == "A":
        Q5 = False
        Q9 = True
    if InputText == "B":
        Q5 = False
        Q9 = True
#Je hebt gekozen om te Vechten.
while Q6:
    print("Je hebt Parwana achtergelaten met de familie om te vechten.")
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
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

while Q7:
    print("Je rent naar binnen om je familie te halen.")
    print("Jullie rennen via de achter deur naar buiten en lopen om naar de auto.")
    print("In de auto krijgen jullie 2 opties.")
    print("A: Jullie gaan naar het vliegveld.")
    print("B: Jullie gaan naar de grens.")
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q7 = False
        Q9 = True
    if InputText == "B":
        Q7 = False
        Q11 = True

while Q8:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

while Q9:
    print("Jullie komen aan bij de bij het vliegveld.")
    print("Je gaat naar de balie toe en vraagt of jullie naar Nederland mogen vluchten.")
    print("Jullie hebben toestemming gekregen van Nederland om daar heen te vluchten")
    print("Jullie wachten op het vliegtuig.")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q9 = False
        Q15 = True

while Q10:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

while Q11:
    print("Jullie komen bij de grens aan")
    print("Jullie worden gestopt door de duane")
    print("De duane ondervraagt jou.")
    print("Na een uur van ondervraging worden jullie naar de gevangenis gebracht.")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q11 = False
        Q17 = True

while Q12:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

while Q13:
    print("")
    print("Op het vliegveld kom je je familie tegen.")
    print("Ze zijn met iemand mee gelift om bij het vliegveld te komen.")
    print("Jullie krijgen toestemming om naar Nederland te vliegen")
    print("Jullie hebben 2 keuzes")
    print("A: Jullie pakken het 1e vliegtuig.")
    print("B: Jullie pakken het 2e vliegtuig.")
    InputText = input().capitalize()
    if InputText == "A":
        Q13 = False
        Q15 = True
        print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "B":
        Q13= False
        Q12 = True

while Q14:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

while Q15:
    print("Het vliegtuig is er en jullie gaan aanboord. ")
    print("Eenmaal aanboord zoeken jullie een goede plek uit.")
    print("")
    print("*5 uur later*")
    print("")
    print("Type: A to continue...")
    InputText = input().capitalize()
    if InputText == "A":
        Q15 = False
        Q19 = True

while Q16:
    print("")
    InputText = input().capitalize()
    if InputText == "A":
        Q = False
        Q = True
    if InputText == "B":
        Q = False
        Q = True

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