file=open("data.txt","w")
while True:
    choice=input("Would you like to write to the file ")
    if choice==("Yes"):
        sentence=input("What would you like to write ")
        file.write(sentence+"\n")
    if choice==("yes"):
        sentence=input("What would you like to write ")
        file.write(sentence+"\n")
    elif choice==("No"):
        break
    elif choice==("no"):
        break
    
