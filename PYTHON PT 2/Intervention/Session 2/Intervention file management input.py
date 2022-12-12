file=open("Names.txt", "w")
for x in range(4):
    name=input("Enter your name ")
    file.write(name+"\n")
file.close()
