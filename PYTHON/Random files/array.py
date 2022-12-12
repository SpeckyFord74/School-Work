import random
names=[]
for x in range(5):
    choice=input("Enter some names ")
    names.append(choice)


print(random.choice(names))
