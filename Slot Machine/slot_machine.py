# Jazmin Gamez
# 01/28/25
# Slot Machine

# initialize
import time # for delays
import random
slot_symbols = ["7", "♪", "☆", "♢", "✿", "♪", "♪", "♪", "☆", "☆", "☆", "♢", "♢", "✿", "✿"] # multiple of a symbol for different probabilities
credits = 100

# functions
def slot_machine():
    global slot_symbols
    global credits
    # 1) introduction
    print("Welcome to the Slot Machine!\n")
    print("The symbols of this machine are: " + str(slot_symbols[0:5]) +"\n")
    print("A MATCH gives you 5x credits")
    print("A JACKPOT gives you 100x credits")
    print("2 OF A KIND gives you 2x credits\n")
    time.sleep(1)
    print("To begin... you have " + str(credits) + " credits.")

    while True:
        # 2) ask player if they'd like to spin or quit
        spin_option = input("Would you like to spin(S) or quit(Q)?\n: ")
        if spin_option.upper() == "S": # when the player spins
            while True:
                cost = int(input("How many credits would you like to bet? (5, 20, 100) \n: "))
                if cost == 5: # 5 credits
                    print("You bet 5 credits")
                    break
                elif cost == 20: # 20 credits
                    print("You bet 20 credits")
                    break
                elif cost == 100: # 100 credits
                    print("You bet 100 credits")
                    break
                else: # player doesn't chose one of the options
                    print("Please enter one of the options.")

            if credits >= cost:
                credits = credits - cost
                print("Spinning...")
                time.sleep(1) # delays the slot machine output to make it seem like it is spinning
                # 3) randomly pull three symbols from our list (Variables)
                symbol1 = random.choice(slot_symbols)
                symbol2 = random.choice(slot_symbols)
                symbol3 = random.choice(slot_symbols)
                # 4) display the three symbols
                print("[ " + str(symbol1) + " ][ " + str(symbol2) + " ][ " + str(symbol3) + " ]")
                # 5) determine the outcome (Jackpot, Match, Loss) --> (if, elif, else)

                time.sleep(1) # delays outcome
                if symbol1 == "7" and symbol2 == "7" and symbol3 == "7": # jackpot
                    print("You got a JACKPOT!")
                    credits = credits + (cost * 100) # player gains 100x credits
                elif symbol1 == symbol2 and symbol2 == symbol3: # match
                    print("You got a MATCH!")
                    credits = credits + (cost * 5) # player gains 5x credits
                elif symbol1 == symbol2 or symbol2 == symbol3 or symbol1 == symbol3: # 2 of a kind
                    print("You got a 2 OF A KIND!")
                    credits = credits + (cost * 2) # player gains 2x credits
                else: # loss
                    print("You lost...")

                time.sleep(1) # before asking if the player wants to spin again
                print("You have " + str(credits) + " credits left")

            else: # when the player bets credits out of their range
                if credits < 100 and credits >= 20: # calculates if the player has enough credits to bet 100
                    print("You have " + str(credits) + " credits left")
                    print("You don't have enough credits to bet 100 credits")
                    print("Try betting a different amount.")
                elif credits < 20 and credits >= 5: # calculates if the player can bet 5
                    print("You can only bet 5 credits.")
                else: # no credits left
                    print("You don't have enough credits to keep playing :(")
                    break

        elif spin_option.upper() == "Q": # when the player quits
            print("You Quit.")
            break
        else: # when the player doesn't chose a possible option
            print("Please enter one of the options given.")

# main
slot_machine()
