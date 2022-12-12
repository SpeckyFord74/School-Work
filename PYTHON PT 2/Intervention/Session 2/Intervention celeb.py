file=open("celebrities.txt","w")
for i in range(5):
    celeb1=input("Name your favourite celebrities")
    file.write(celeb1+"\n")
file.close()

