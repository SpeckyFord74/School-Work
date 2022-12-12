def function(space, marks):
    print(""*space+"X" *marks)

def repeat():
    for i in range(number):
        function(space, marks)
space=int(input('How many spaces do you want? '))
marks=int(input('How many X do you want? '))
number=int(input('How many rows do you want? '))

repeat()
