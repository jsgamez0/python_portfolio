# Jazmin Gamez
# 11/11/24
# Guessing Game

# initialize
import random

# functions
def guessingGame(): # a guessing game that has the player guess a number from 1 to 10
    tries = 3 # gives the player 3 tries to guess the correct number
    playAgain = "yes"
    # greeting + instructions
    print("Welcome to the Number Guessing Game!")
    print("In this game, you must enter a number from 1 to 10.")
    print("You will have 3 tries to get the number right so try to get the most points out of 90 that you can!")

    # allows the player to try and guess the number 3 times and also repeat the game if they want to
    while playAgain == "yes":
        secret = random.randint(1,10) # resets the random number after each game
        points = 90 # resets the point value to 90 after each game

        while tries > 0: # when the player still has tries left
            guess = int(input("Enter a number: "))

            if secret == guess: # when the player guesses correctly
                print("You guessed correctly!")
                tries = 0
                print("Congrats! You got " + str(points) + "/90 points!")
                print("")

            else: # when the player guesses incorrectly
                print("You guessed incorrectly...")
                if guess > secret: # lets the player know if their guess is too high
                    print("That guess is too high.")
                else: # lets the player know if their guess is too low
                    print("That guess is too low.")
                points = points - 30
                tries = tries - 1

                if tries == 0: # when the player runs out of tries
                    print("The correct answer was " + str(secret) + ".")
                    print("You got " + str(points) + "/90 points...")
                    print("")

        else: # when the game ends
            print("The game is over!")

            playAgain = input("Would you like to play again? (yes/no): ") # lets the player play again
            if playAgain == "yes":
                tries = tries + 3
                print("") # To help distinguish different games from each other
    else:
        print("Thanks for playing!")

# main
guessingGame()

