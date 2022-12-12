import random
number=int(input("Please enter your first number "))
number2=int(input("Please enter your second number "))
number3=int(input("Please enter your third number "))
number4=int(input("Please enter your fourth number "))
print()
for x in range(1,10):
    s=random.randrange(9)
    print(s)
    if s==number:
        print("Your first number has been cracked")
        break

print()
for x in range(1,10):
    s=random.randrange(9)
    print(s)
    if s==number2:
        print("Your second number has been cracked")
        break

print()
for x in range(1,10):
    s=random.randrange(9)
    print(s)
    if s==number3:
        print("Your third number has been cracked")
        break

print()
for x in range(1,10):
    s=random.randrange(9)
    print(s)
    if s==number4:
        print("Your fourth number has been cracked")
        break
