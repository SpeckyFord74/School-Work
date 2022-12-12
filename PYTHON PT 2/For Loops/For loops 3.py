while True:
    number=int(input('Please input a number you wish to see the times tables of '))
    for i in range(1,101):
        print(number, "X", i, "=", number*i)
