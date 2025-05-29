# Jazmin Gamez
# 01/25/25
# Magic 8 Ball

# initialize
import time
import random

    # stores 15 predefined responses (five for yes, maybe, and no)
responses = ["You bet!", "Yes!", "100% yes!", "That's a yes from me!", "That's definitely a yes!", "Ask again in the future.", "Maybe...", "You'll get the answer to that soon enough...", "The answer will be revealed in due time...", "It's best if you didn't know the answer to that right now.", "No.", "Definitely not!", "That's a no from me.", "Nope!", "Noooooo!!!"]
     # variables to make sure that the responses given are not the same in a row (after multiple questions are asked)
random_response1 = ""
random_response2 = ""

# functions
def magic8Ball(): # function for a Magic 8 Ball that gives 15 predetermined answers after a user asks a yes or no question
    global responses
    global random_response1
    global random_response2
    print("Welcome to the Magic 8 Ball!") # welcoming message
    print("Ask questions and get answers in an instant!")
    time.sleep(1) # adds a delay
    while True: # keeps looping until the user doesn't want to ask more questions
        while True: # keeps looping until user asks a question with a ? mark
            print("Enter a yes-or-no question.")
            question = input("Question: ")
            if question.endswith("?"):
                time.sleep(1)
                while True: # keeps looping until the previous response given is not the same as the new response
                    random_response1 = random.choice(responses) # sets a random response
                    if random_response1 != random_response2: # makes sure previous response was not the same as the new one
                        print(random_response1)
                        random_response2 = random_response1 # sets this response as the previous one
                        break
                break
            else: # when the user did not end their question with a ? mark
                print("Please enter a question (ending in a ? mark).")
        time.sleep(1)
        print("Would you like to ask another question? (y/n)") # asks user if they want to ask another question
        again = input(": ")
        if again.lower() == "y" or again.lower() == "yes": # when the response is yes
            print()
            time.sleep(1)
        else: # when the response is no
            print("Thank you for asking questions with the Magic 8 Ball!")
            break

# main
magic8Ball()
