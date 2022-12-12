number= int(input("Enter the number you want to see the times tables for? "))
print("The times tables for: ", number, "is")
for count in range(1, 101):
    print(number, 'x',  count, '=', number*count)
