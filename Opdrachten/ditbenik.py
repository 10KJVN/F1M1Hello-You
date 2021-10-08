print("Hello You!, Ik ben Jahva")
print("Wie ben jij?")
inputText = input ()
print("Hello" , inputText)

while True: 
    print("do you want to repeat?")
    inputText = input ()
    print("input:" , inputText)
    if inputText == "no" or "No" : 
        break

while True:
    print ("Where do you think im from bro?")
    print ("A: Zaandam")
    print ("B: Amsterdam")
    print ("C: Rotterdam")

    scriptinput = input()
    if scriptinput == "a" or scriptinput == "A" : 
        print ("Thats kind of right, im originally from Zaandam (HVZ) But i live in Amsterdam.")
        script = True

    elif scriptinput == "c" or scriptinput == "C" :  
        print ("Thats totally wrong, i aint no opp. (Hint: Ajax)")
        script = True
    
    elif scriptinput == "b" or scriptinput == "B" : 
        print ("That sounds more like it since i do live in Amsterdam, im from Zaandam so yeah that's that.")
        script = True
        break

while True:  
    print ("What about you big dawg, where you from homie?")
    inputText = input ()
    print("I aint never heard of that place but," , inputText , "sounds like a nice place") 
    print("Maybe i should come visit u sometime, send the addy and imma slide")
    print("Sike! im just playin with ya.")
    print("Anyways, did you want to know anything else?")
    print("Input: Y/N")
    
    scriptinput = input()
    if scriptinput == "Y" : 
        print ("You want to know about my favorite game?") 
        script = True
        break

    elif scriptinput == "N" : 
        print ("ight then have a nice day.")
        script = True
        break

while True: 
    print("Ight so my favorite game of all time is probably Nier:Automata")
    print("Simply cause its a dope RPG with a intriguing story and characters")
    print("The music and combat stands out as well")
    print("Another unique thing the game has 27 different endings so theres enough to do!")
    print("So... did you like hearing about my fav game OwO? ")
    print("input: Y/N")
    
    scriptinput = input()
    if scriptinput == "Y" or scriptinput == "N" :
        print("Well it doesnt matter wether u did or not")
        print("Im out of questions now so il go, cya!")
        script = True
        break