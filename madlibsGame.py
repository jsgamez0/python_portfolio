# Jazmin Gamez
# 12/10/24
# Madlibs Game

# initialize

# functions
def madlibs_game(): # A madlibs game
    print("Welcome to The Adventure Story!") # introduction
    print("To begin making your own story, enter words for the following:")
    print()
    animal = input("Animal: ") # the main character
    animal = animal.lower()
    animal2 = input("Animal: ") # the antagonist
    animal2 = animal2.lower()
    animal3 = input("Animal: ") # the friend
    animal3 = animal3.lower()

    name = input("Name: ") # the main character
    name = name.capitalize()
    friend_name = input("Name: ") # the friend's name
    friend_name = friend_name.capitalize()

    adjective = input("Adjective: ") # describing the first location
    adjective = adjective.capitalize()
    adjective2 = input("Adjective: ") # describing the antagonist
    adjective2 = adjective2.lower()
    adjective3 = input("Adjective: ") # describing the second location
    adjective3 = adjective3.capitalize()

    place = input("Place: ") # the first location
    place = place.capitalize()
    place2 = input("Place: ") # the second location
    place2 = place2.capitalize()

    item = input("Item: ") # the item found in the story
    item = item.capitalize()

    print() # start of the story with user input in bold text
    print("Once upon a time, a " + '\033[1m' + str(animal) + '\033[0m' + " named " + '\033[1m' + str(name) + '\033[0m' + " decided to go to the " + '\033[1m' + str(adjective) + '\033[0m' + " " + '\033[1m' + str(place) + '\033[0m' + " in search for a rare " + '\033[1m' + str(item) + '\033[0m' + ".")
    print("After a long journey, " + '\033[1m' + str(name) + '\033[0m' + " made it to the " + '\033[1m' + str(adjective) + '\033[0m' + " " + '\033[1m' + str(place) + '\033[0m' + " and found the " + '\033[1m' + str(item) + '\033[0m' + "!")
    print('\033[1m' + str(name) + '\033[0m' + " celebrated finding the " + '\033[1m' + str(item) + '\033[0m' + " but that happiness didn't last long...")
    print()
    print("In an instant, a " + '\033[1m' + str(adjective2) + '\033[0m' + " " + '\033[1m' + str(animal2) + '\033[0m' + " took the " + '\033[1m' + str(item) + '\033[0m' + " from " + '\033[1m' + str(name) + '\033[0m' + " and started to run away, their laughter fading the farther they went.")
    print('\033[1m' + str(name) + '\033[0m' + " was left devestated. " + '\033[1m' + str(name) + '\033[0m' + " stood there crying for a long time, until a " + '\033[1m' + str(animal3) + '\033[0m' + " came along.")
    print()
    print("'What's wrong?' asked the " + '\033[1m' + str(animal3) + '\033[0m' + ".")
    print()
    print("'The " + '\033[1m' + str(adjective2) + '\033[0m' + " " + '\033[1m' + str(animal2) + '\033[0m' + " took my " + '\033[1m' + str(item) + '\033[0m' + "!' cried " + '\033[1m' + str(name) + '\033[0m' + ".")
    print()
    print("'How dare that " + '\033[1m' + str(animal2) + '\033[0m' + "!' the " + '\033[1m' + str(animal3) + '\033[0m' + " exclaimed. 'We need to go find the " + '\033[1m' + str(animal2) + '\033[0m' + " and get your " + '\033[1m' + str(item) + '\033[0m' + " back!'")
    print('\033[1m' + str(name) + '\033[0m' + " decided that the " + '\033[1m' + str(item) + '\033[0m' + " needed to be taken back because it was wrongfully stolen!!!")
    print('\033[1m' + str(name) + '\033[0m' + " and the " + '\033[1m' + str(animal3) + '\033[0m' + " went outside of the " + '\033[1m' + str(adjective) + '\033[0m' + " " + '\033[1m' + str(place) + '\033[0m' + " and into the " + '\033[1m' + str(adjective3) + '\033[0m' + " " + '\033[1m' + str(place2) + '\033[0m' + ".")
    print("There, they found the " + '\033[1m' + str(adjective2) + '\033[0m' + " " + '\033[1m' + str(animal2) + '\033[0m' + ".")
    print()
    print("'Give us back the " + '\033[1m' + str(item) + '\033[0m' + "!' said " + '\033[1m' + str(name) + '\033[0m' + ".")
    print()
    print("The " + '\033[1m' + str(adjective2) + '\033[0m' + " " + '\033[1m' + str(animal2) + '\033[0m' + " was so shocked that they dropped the " + '\033[1m' + str(item) + '\033[0m' + ".")
    print('\033[1m' + str(name) + '\033[0m' + " and the " +  '\033[1m' + str(animal3) + '\033[0m' + " ran off with the " + '\033[1m' + str(item) + '\033[0m' + " with a smile on their faces.")
    print('\033[1m' + str(name) + '\033[0m' + " was so happy that they shared the " + '\033[1m' + str(item) + '\033[0m' + " with their new friend " + '\033[1m' + str(friend_name) + '\033[0m' + ", the " + '\033[1m' + str(animal3) + '\033[0m' + " that helped them get their " + '\033[1m' + str(item) + '\033[0m' + " back.")
    print()
    print('\033[1m' + str(name) + '\033[0m' + " and " + '\033[1m' + str(friend_name) + '\033[0m' + " became best friends forever after the adventure they went on.")
    print()
    print("The end.") # ending

# main
madlibs_game()
