import random
import time
import sys


def hey_You():
    print("You wake up slowly, confused. Once you come to your senses, you see you are on the back of a wagon. Your hands are tied and you notice 3 other men. 2 of them are sitting opposite you and one is sitting beside you. ""Hey you, you are finally awake!"" a voice says. The man who said it is sitting opposite and the right of you. He is wearing a light brown rag, almost like a bag you would use to store rice or grain in. ""You were caught trying to cross the border, right?")
    nod_head = input("[1] Nod your head\n[2] Shake your head\nMake your choice: ")

          
def start():
    global difficulty
    difficulty = input("[1] Easy\n[2] Medium\n[3] Hard\nChoose your difficulty: ")
    hey_You()
    

def main_Menu():
    print("Welcome To Fantasy Land!")
    
    main_Menu_Selection = input("[1] Start\n[2] Quit\nWhat is your selection?: ")
    if main_Menu_Selection.lower == "start":
        start()
    elif main_Menu_Selection == 1:
        start()
    elif main_Menu_Selection.lower == "quit":
        print("Goodbye, traveller")
        time.sleep(2)
        sys.exit()
    elif main_Menu_Selection == 2:
        print("Goodbye, traveller")
        time.sleep(2)
        sys.exit()
        

main_Menu()


