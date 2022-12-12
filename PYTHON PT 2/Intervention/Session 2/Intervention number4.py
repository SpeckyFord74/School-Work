file=open("numbers.txt","w")
for i in range(4):
    num=int(input("Please enter a number "))
    if num>100:
        file.write(str(num)+"\n")
    else:
        print("Number is not big enough ")
file.close()
