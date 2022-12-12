import os
import socket
import time
import sys
import getpass

currentWorkingDirectory = os.getcwd()

def Tools(nav):
        if nav == "pwd":
                currentWorkingDirectory = os.getcwd()
                print(currentWorkingDirectory)
                welcomeScreen()
        elif nav == "ls":
                currentWorkingDirectory = os.getcwd()
                print(os.listdir(currentWorkingDirectory))
                welcomeScreen()
        elif nav == "cd":
                cdTo = input("What directory would you like to go to?: ")
                os.chdir(cdTo)
                welcomeScreen()
        elif nav == "ip":
            hostname = socket.getfqdn()
            print("IP Address:",socket.gethostbyname_ex(hostname))
            welcomeScreen()
        elif nav.lower() == "log off":
            print("Logging Off")
            time.sleep(3)
            login()
        elif nav.lower() == "shut down":
            print("Shutting Down...")
            time.sleep(3)
            sys.exit()
        elif
        else:
                print("Not a valid command!!")
                welcomeScreen()

def welcomeScreen():
    navigation = input(f"18cford@PyLinux:~$ ")
    Tools(navigation)

def login():
    Username = "18cford"
    Password = "9721"
    userNameTry = input("Enter your username: ")
    if userNameTry == Username:
        passwordTry = input("Enter your password: ")
        if passwordTry == Password:
            welcomeScreen()
    else:
        print("Username or password incorrect")
        login()
login()




