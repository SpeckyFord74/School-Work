a = '7'
while True:
    number = input("Guess the number: ")
    if number == a:
        print("Well done! You guessed correctly!")
        break
    else:
        print("Wrong try again")
