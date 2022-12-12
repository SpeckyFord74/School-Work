import time
import random
startTime = time.time()
print("Welcome to mastermind!")

seq1=int(input("Please enter your first number between 1 and 7: "))
seq2=int(input("Please enter your second number between 1 and 7: "))
seq3=int(input("Please enter your third number between 1 and 7: "))
seq4=int(input("Please enter your third number between 1 and 7: "))
print(seq1, seq2, seq3, seq4)

ai_guess1=random.randrange(7)
if ai_guess1==(seq1):
    print("Your first number has been cracked")
    ai_guess2=random.randrange(7)
    if ai_guess2==(seq2):
        print("Your second number had been cracked")
        ai_guess3=random.randrange(7)
        if ai_guess3==(seq3):
            print("Your third number has been cracked")
            ai_guess4=random.randrange(7)
            if ai_guess4==(seq4):
                print("Your fourth number has been cracked")
            else:
                print("Your fourth number was not cracked")
        else:
            print("Your third number has not been cracked")        
    else:
        print("Your second number was not cracked")
else:
    print("Your first number was not cracked")


ai_guess2=random.randrange(7)
if ai_guess2==(seq2):
    print("Your second number has been cracked")
    ai_guess3=random.randrange(7)
    if ai_guess3==(seq3):
        print("Your third number has been cracked")
        ai_guess4=random.randrange(7)
        if ai_guess4==(seq4):
            print("Your fourth number has been cracked")
        else:
            print("Your fourth number was not cracked")
    else:
        print("Your third number was not cracked")
else:
    print("Your second number was not cracked")


ai_guess3=random.randrange(7)
if ai_guess3==(seq3):
    print("Your third number has been cracked")
    ai_guess4=random.randrange(7)
    if ai_guess4==(seq4):
        print("Your fourth number has been cracked")
    else:
        print("Your fourth number was not cracked")
else:
    print("Your third number was not cracked")


ai_guess4=random.randrange(7)
if ai_guess4==(seq4):
    print("Your fourth number has been cracked")
else:
    print("Your fourth number was not cracked")

result=input("Has the ai cracked all of your code?")
if result=="no" or "No":
    print("AWW damn")

endTime = time.time()
totalTime = endTime - startTime
print(totalTime)
    
    
