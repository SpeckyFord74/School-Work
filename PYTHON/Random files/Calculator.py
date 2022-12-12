while True:
    calc=int(input('Please enter a number: '))
    symbol=input("Please enter either the symbols X, +, - or / ")
    if symbol=='X':
        num2=int(input('Please enter the number you want to times by: '))
        equal= calc * num2
        print("The answer is: ", equal)
    elif symbol=='+':
        num3=int(input('Please enter the number you want to add: '))
        equal2= calc + num3
        print("The answer is: ", equal2)
    elif symbol=='-':
        num4=int(input('Please enter the number you want to subtract by: '))
        equal3= calc - num4
        print("The answer is: ", equal3)
    elif symbol=='/':
        num5=int(input('Please enter a number you want to divide by: '))
        equal4= calc / num5
        print("The answer is: ", equal4)
    else:
        print("Sorry, that's not an option")

    
