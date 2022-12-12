negative=int(input('How many negatives did you get '))
if negative==1:
    for i in range(1,11):
        print("Prompt")
elif negative==2:
    for i in range(1,51):
        print("Reminder")
elif negative==3:
    for i in range(1,101):
        print("Warning")
else:
    for i in range(1,501):
        print("Removal")
