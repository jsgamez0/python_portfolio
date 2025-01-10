# Jazmin Gamez
# 10/15/24
# Name Generator

# initialize
play = "yes" # variable that starts the generator once the code is run

# functions
def name_generator():
    global play
    # introduction:
    print("Welcome to Snack Name Generator!")
    print("Answer the questions to find out your snack food name!")

    # loop that will restart the generator if the user inputs "yes" after being asked to play again
    while play == "yes":
        # first question:
        ans = input("Do you prefer sweeter foods or more savory ones? (sweet / savory): ")

        # for when "sweet" is entered:
        if ans == "sweet":
            ans = input("Do you prefer chocolate or vanilla sweets? (chocolate / vanilla): ")

            # for when "chocolate is entered":
            if ans == "chocolate":
                ans = input("Do you prefer cold or hot snacks? (cold / hot): ")
                if ans == "cold":
                    # result 1 (Chocolate Icecream):
                    print("Your snack food name is Chocolate Icecream!")
                    play = input("Would you like to play again? (yes / no): ")

                # for when "hot" is entered:
                else:
                    # result 2 (Hot Chocolate):
                    print("Your snack food name is Hot Chocolate!")
                    play = input("Would you like to play again? (yes / no): ")

            # for when "vanilla" is entered:
            else:
                ans = input("Do you like cinnamon or pumpkin flavors more? (cinnamon / pumpkin): ")
                # for when "cinnamon" is entered:
                if ans == "cinnamon":
                    # result 3 (Cinnamon Bun):
                    print("Your snack food name is Cinnamon Bun!")
                    play = input("Would you like to play again? (yes / no): ")

                # for when "pumpkin" is entered:
                else:
                    # result 4 (Pumpkin Pie):
                    print("Your snack food name is Pumpkin Pie!")
                    play = input("Would you like to play again? (yes / no): ")

        # for when "savory" is entered:
        else:
            ans = input("Do you prefer cheesy or salty foods more? (cheese / salty): ")
            # for when "cheesy" is entered:
            if ans == "cheese":
                ans = input("What type of snack do you like more, chips or puffs? (chips / puffs): ")
                # for when "chips" is entered:
                if ans == "chips":
                    # result 5 (Cheesy Nachos):
                    print("Your snack food name is Cheesy Nachos!")
                    play = input("Would you like to play again? (yes / no): ")

                # for when "puffs" is entered:
                else:
                    # result 6 (Cheese Puffs):
                    print("Your snack food name is Cheese Puffs!")
                    play = input("Would you like to play again? (yes / no): ")

            # for when "salty" is entered:
            else:
                ans = input("Do you like bread or nuts more? (bread / nuts): ")
                # for when "bread" is entered:
                if ans == "bread":
                    # result 7 (Pretzel):
                    print("Your snack food name is Pretzel!")
                    play = input("Would you like to play again? (yes / no): ")

                # for when "nuts" is entered:
                else:
                    # result 8 (Trail Mix):
                    print("Your snack food name is Trail Mix!")
                    play = input("Would you like to play again? (yes / no): ")

    # after the user inputs "no" to playing again
    else:
        print("Thank you for playing!")

# main
name_generator()
