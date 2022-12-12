play=input("Rock, Paper, Scissors, Shoot! ")
import random
dice1 = random.randrange(9)
if play=='rock':
    print("You've chosen Rock")
    if dice1==1:
        print("We've both chosen rock! It's a draw!")
    elif dice1==2:
        print("We've both chosen rock! It's a draw!")
    elif dice1==3:
        print("We've both chosen rock! It's a draw!")
    elif dice1==4:
        print("I've chosen paper! You lose")
    elif dice1==5:
        print("I've chosen paper! You lose")
    elif dice1==6:
        print("I've chosen paper! You lose")
    elif dice1==7:
        print("I've chosen scissors! You win!")
    elif dice1==8:
        print("I've chosen scissors! You win!")
    elif dice1==9:
        print("I've chosen scissors! You win!")

if play=='paper':
    print("You've chosen Paper")
    if dice1==1:
        print("I've chosen rock! You win!")
    elif dice1==2:
        print("I've chosen rock! You win!")
    elif dice1==3:
        print("I've chosen rock! You win!")
    elif dice1==4:
        print("We've both chosen paper! It's a draw!")
    elif dice1==5:
        print("We've both chosen paper! It's a draw!")
    elif dice1==6:
        print("We've both chosen paper! It's a draw!")
    elif dice1==7:
        print("I've chosen scissors! You lose")
    elif dice1==8:
        print("I've chosen scissors! You lose")
    elif dice1==9:
        print("I've chosen scissors! You lose")

if play=='scissors':
    print("You've chosen Scissors")
    if dice1==1:
        print("I've chosen rock! You lose")
    elif dice1==2:
        print("I've chosen rock! You lose")
    elif dice1==3:
        print("I've chosen rock! You lose")
    elif dice1==4:
        print("I've chosen paper! You win!")
    elif dice1==5:
        print("I've chosen paper! You win!")
    elif dice1==6:
        print("I've chosen paper! You win!")
    elif dice1==7:
        print("We've both chosen scissors! It's a draw!")
    elif dice1==8:
        print("We've both chosen scissors! It's a draw!")
    elif dice1==9:
        print("We've both chosen scissors! It's a draw!")
        
    
    
