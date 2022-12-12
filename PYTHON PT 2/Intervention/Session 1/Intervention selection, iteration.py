number=7
while True:
    guess=int(input("Guess the number "))
    if guess== number:
        print("Correct")
        break
    else:
        print("Wrong")
