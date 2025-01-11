# Jazmin Gamez
# 01/08/25
# Multiplication Quiz

# initialize
import random

# functions
def multiplication_game(): # a muliplication game with random multiplication problems
    print("Welcome to the Multiplication Quiz!") # welcome message
    print("In this game, you will answer multiplication questions between 2 random numbers.")
    print()

    while True: # allows player to keep playing if they want to
        score = 0
        print("To begin, what difficulty level would you like to do?") # difficulty level
        print()
        print("""a. easy (numbers 0-4)
b. medium (numbers 4-8)
c. hard (numbers 8-12)
d. all (numbers 0-12)""")
        print()
        difficulty = input("Please select a letter: ")

        print("How many questions would you like to do?") # amount of questions
        questions = int(input("Amount: "))

        for i in range(questions): # creates the amount of questions the player wants in a loop
            if difficulty.lower() == "a": # easy
                num1 = random.randint(0,4)
                num2 = random.randint(0,4)
            elif difficulty.lower() == "b": # medium
                num1 = random.randint(4,8)
                num2 = random.randint(4,8)
            elif difficulty.lower() == "c": # hard
                num1 = random.randint(8,12)
                num2 = random.randint(8,12)
            else: # all
                num1 = random.randint(0,12)
                num2 = random.randint(0,12)
            correct_num = num1 * num2 # the correct answer for the random numbers multiplied

            print("What is " + str(num1) + " x " + str(num2) + "?") # asks the player a question
            answer = int(input("Answer: "))

            if answer == correct_num: # when the player's answer is correct
                print("That answer was correct!")
                score = score + 1 # adds a point to the player's score
            else: # when the player's answer is incorrect
                print("Sorry, that was incorrect...")
                print("The correct answer is " + str(correct_num) + ".") # displays correct answer

        print("Your final score is " + str(score) + "/" + str(questions) + "!") # displays final score for this round
        print("Would you like to keep playing? (y/n)")
        quit = input("Response: ")
        if quit.lower() == "n": # player chooses to quit
            print("Thank you for playing!")
            print()
            break # lets the player quit early
        else: # player wants to continue the game
            print()

# main
multiplication_game()
