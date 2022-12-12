while True:
    num=int(input('Please enter a you wish to see the times table of: '))
    for i in range(1,101):
        print(num, 'X', i, '=', num*i)
