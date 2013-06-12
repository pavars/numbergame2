'''
Created on 2013. gada 7. maijs

@author: Pavars
'''
import random

with open("guestaken.txt","w") as myfile:
    
    def guesses(file):
        myfile = open(file,"a+", encoding="utf-8")
        #myfile.write("%s log \n"%myID)
        myfile.write(" Your guess: \t%s\t"%guess)
        #myfile.readline()     
        myfile.write(" Real answer: \t%s\n"%number)
        #for left in range (0,5):
        #guess = str(guess)
        #print("number." + guess)
        #print(str(guess) +"<---")
        #myfile.readline()
        #myfile.write("\t%s\t"%guess)
        
    def name(file):
        myfile = open(file,"a+", encoding="utf-8")
        myfile.write("Name: " + myID +"\n")
        
print("Hello, what is your name?")
myID = input()
playagain = ("yes")
name("guestaken.txt")

        
while playagain == ("yes") or ("y"):

    guessesTaken = 0    
    guess = []
    result = ["","","",""]
    number = [random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20)]
    
    
   
    print("I'm thinking of a number from 1 to 20 (You have 5 guesses)") 
    
    while guessesTaken < 50:
        print("Well, " + myID + ", guess what number i'm thinking of.")
        rguess = [input(), input(), input(), input()]
        
        guess.append(rguess)
        
                               
        if rguess == ["666","666","666","666"]:
            guesses("guestaken.txt") 
            print("##############--",number,"--##############")
            #guess = [input(),input(),input(),input()]
            #guess[0][1][2][3] = int(guess[0][1][2][3])
            
            
        guessesTaken = guessesTaken + 1 
        guess = list(map(int, rguess))   
        if guess[0] > number[0] or guess[1] > number[1] or guess[2] > number[2] or guess[3] > number[3]:
            
            left = 5 - guessesTaken
            if guess[0] > number[0]:
                result[0]=("too high")
            if guess[1] > number[1]:
                result[1]=("too high")
            if guess[2] > number[2]:
                result[2]=("too high")
            if guess[3] > number[3]:
                result[3]=("too high")
            print(result)
                      
            #print("Guesses left: %i"%(left))
            guesses("guestaken.txt")
            
        if guess[0] < number[0] or guess[1] < number[1] or guess[2] < number[2] or guess[3] < number[3]:
            
            left = 5 - guessesTaken          
            #print("Aim higher. (Guesses left: %i)"%(left))
            if guess[0] < number[0]:
                result[0]=("too low")
            if guess[1] < number[1]:
                result[1]=("too low")
            if guess[2] < number[2]:
                result[2]=("too low")
            if guess[3] < number[3]:
                result[3]=("too low")
            print(result)
            guesses("guestaken.txt")
            
        if guess[0] == number[0] or guess[1] == number[1] or guess[2] == number[2] or guess[3] == number[3]:
            
            if guess[0] == number[0]:
                result[0]=("#")
            if guess[1] == number[1]:
                result[1]=("#")
            if guess[2] == number[2]:
                result[2]=("#")
            if guess[3] == number[3]:
                result[3]=("#")
            print(result)
            guesses("guestaken.txt")
            
        
        
        if guess[0] == number[0] and guess[1] == number[1] and guess[2] == number[2] and guess[3] == number[3]:
            
            if guess[0] == number[0]:
                result[0]=("#")
            if guess[1] == number[1]:
                result[1]=("#")
            if guess[2] == number[2]:
                result[2]=("#")
            if guess[3] == number[3]:
                result[3]=("#")
            print(result)
            guesses("guestaken.txt")
            break
        
        
    if guess[0] == number[0] and guess[1] == number[1] and guess[2] == number[2] and guess[3] == number[3]:
        guessesTaken = str(guessesTaken)
        print("Exactly, "+myID+"! I'm thinking of " , number ,", it took you " + guessesTaken +" times to guess!")
        
    #number = int(number)    
  
    if map(int,rguess) != map(int,number):
        #number = str(number)
        print("Pro Tip: The numbers are random. Think. [", number,"]" )
        
    print("Play again? (yes/no)")
    playagain = input()

    if playagain == ("no"):
        print("See you later, "+myID+"!")
        break
    if playagain == ("n"):
        print("See you later, "+myID+"!")
        break
myfile.close()