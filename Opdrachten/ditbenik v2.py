print("Hello You!")
print("Wie ben jij?")
inputText = input ()
print("Hello" , inputText)

while True:
    print ("Where do you think im from?")
    print ("A: Zaandam")
    print ("B: Amsterdam")
    print ("C: Rotterdam")

    scriptinput = input()
    if scriptinput == "a" or scriptinput == "A" :
        print ("Thats right, maybe you do know more than i thought.")
        script = True
        pass
    
    elif scriptinput == "b" or scriptinput == "B" :
        print ("In a sense that's right as well since i live here.")
        script = True
        pass

    elif scriptinput == "c" or scriptinput == "C" :
        print (". . .") 
        print ("Nope, thats incorrect. Try Again.")
        script = True
        continue
    
    else:
        print (". . .")
        print ("invalid choice, try again")
        script = True
        continue

    print ("How old do you think i am? take a guess.")
    print ("A: 15")
    print ("B: 16")
    print ("C: 17") 

    scriptinput = input()
    if scriptinput == "a" or scriptinput == "A" :
        print (". . .")
        print ("Back when i made this i was, so it counts.")
        script = True
        pass
    
    elif scriptinput == "b" or scriptinput == "B" :
        print ("Correct answer, you may proceed.")
        script = True
        pass
    
    elif scriptinput == "c" or scriptinput == "C" :
        print (". . .")
        print ("Your off by atleast a year, Try again.")
        script = True
        continue
    
    else:
        print (". . .")
        print ("invalid choice, try again")
        script = True
        continue

    print ("Did you enjoy this quiz?")
    print ("A: Yes, i did indeed")
    print ("B: Meh, it was okay")
    print ("C: No, i hated it")

    scriptinput = input()
    if scriptinput == "a" or scriptinput == "A" :
        print ("")
        print ("What a relief, thats good to hear.")
        print ("(Press enter to continue)")
        script = True
        pass

    elif scriptinput == "b" or scriptinput == "B" :
        print ("")
        print ("I'll just take that as 'it was alright'.")
        print ("(Press enter to continue)")
        script = True
        pass
    
    elif scriptinput == "c" or scriptinput == "C" :
        print (". . .")
        print ("Oh, Thats concerning. Do you want to tell me why?")
        print ("Yes or no?")
    
    else:
        print (". . .")
        print ("invalid choice, proceeding...")
        script = True
        continue

    inputText = input() 
    if inputText == "No" or inputText == "no" :
        print ("Alright, proceeding to next step.")
        script = True
        pass
    
    if inputText == "Yes" or inputText == "yes" :
        print ("What's the problem?")
        print ("Type below")
        inputText = input()
        print ("Thanks for the feedback on '" , inputText , "' I'll look into it.")
        script = True
        pass 
   
    print ("Congrantulations, you've reached the end of my 'this is me' quiz,")
    print ("Do you want to retry.")
    print ("")
    print ("Yes or No?")
    scriptinput = input()
    if scriptinput == "Y" or scriptinput == "yes" or scriptinput == "Yes" :
        continue
    
    elif scriptinput == "N" or scriptinput == "No" or scriptinput == "no" :
        break
