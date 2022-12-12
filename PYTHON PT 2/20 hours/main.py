import Player, sys, time, os.path #Imports another file containing a player class and some other libraries for saving, typing, etc

checkpoint_file_exists = os.path.isfile("loadfile.txt") #Checks if loadfile.txt exists and if it does, sets the vairbale to true
name_file_exists = os.path.isfile("name.txt")
race_file_exists = os.path.isfile("race.txt")
health_file_exists = os.path.isfile("health.txt")

def start():
    typingInput = input("Welcome to Fantasy Adventure!\nPlease select an option\n[1] Start New Game\n[2] Continue Current Game\n[3]Settings\nMake Your Choice")
    if typingInput == "1":
        characterCreation()
    elif typingInput == "2":
        load(checkpoint_file_exists, name_file_exists, race_file_exists)



def load(checkpoint_file_exists, name_file_exists, race_file_exists):
    if checkpoint_file_exists:
        checkpoint_file = open("loadfile.txt", "r")
        room = checkpoint_file.read()
        checkpoint_file.close()
        print(room)
    if name_file_exists:
        name_file = open("name.txt", "r")
        name = name_file.read()
        name_file.close()
        print(name)
    if race_file_exists:
        race_file = open("race.txt", "r")
        race = race_file.read()
        race_file.close()
        print(race)
    if health_file_exists:
        health_file = open("health.txt", "r")
        player_health = int(health_file.read())
        health_file.close()
    if race_file_exists and name_file_exists:
        player = Player.Player(name, race)
        player.stats[0] = health_file
        print(player.stats[0])
    else:
        else_choice = input("No save game found! Do you want to start a new game? [Y/N]: ")

        if else_choice.lower() == "y":
            characterCreation()
        elif else_choice.lower() == "n":
            print("Ok. See you soon!")
            quit()


    

    

def save(checkpoint, player_race, player_name, player_health):
    checkpoint_file = open("loadfile.txt", "w")
    race = open("race.txt", "w")
    name = open("name.txt", "w")
    health = open("health.txt", "w")
    race.write(player_race)
    name.write(player_name)
    health.write(player_health)
    checkpoint_file.write(checkpoint)


def typingInput(text, typingSpeed):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(typingSpeed)
    value = input()
    return value

def characterCreation():
    typingSpeedChoice = float(input("How fast do you want the typing speed to be? (0 for off. 0.05 is recommended): "))
    player_name = typingInput("Enter your name: ", typingSpeedChoice)
    player_race = typingInput("Enter your race. You can choose from: Human, Orc or Kahjiit: ", typingSpeedChoice)
    if player_race.lower() != "human" and player_race.lower() != "orc" and player_race.lower() != "Kahjiit":
        print("Not an option")
        characterCreation()
    else:
        player = Player.Player(player_name, player_race)
        player_health = player.stats[0]
        player_health = "50"
        save("test", player_race, player_name, player_health)

    print(player.__str__("health"))




start()






        


