# Jazmin Gamez
# 02/05/25
# Tetris Score Analysis

# initialize

# list of Tetris scores (unsorted) (top 100 score in Tetris history)
scores = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]

# functions
# 1) create a function that finds the largest score
def maxScore():
    global scores
    max = 0
    for number in scores: # goes through all items and finds the max value of all of them
        if number > max:
            max = number
    return max

# 2) create a function that finds the smallest score
def minScore():
    global scores
    min = maxScore() # sets the min to the maxScore() so that it can be used in the loop
    for number in scores:
        if min > number: # checks the previous number with the current number (if the previous number is smaller, that is the new min)
            min = number
    return min

# 3) create a function that calculates the average score
def avgScore():
    global scores
    avg = 0
    for i in range(len(scores)): # goes through all items in scores
        avg = (avg + scores[i]) # adds all 100 items
    avg = avg / len(scores) # divides the sum by 100 to get the average
    return avg

# 4) create a function that allows the user to enter a new score
# ONLY add the score if it is in the top 100
# IF score is the new highest score, congratulate the user
def newScore():
    global scores
    new = int(input("Please enter new score: "))
    if new > minScore():
        print("Your score is in the TOP 100!")
        if new > maxScore():
            print("Congratulations! You got the NEW HIGH SCORE!!!")
        scores.append(new)
        scores.remove(minScore())
    else:
        print("Your score is not in the top 100...")
    # does not return a value because it checks to see if the new score can be added and not directly used in other functions

# function that runs the Tetris Analysis
def tetrisAnalysis():
    print("Welcome to Tetris Score Analysis!!!")
    while True:
        print("What would you like to do?")
        print("""1. View Largest Score
2. View Smallest Score
3. View Average Score
4. Input New Score
5. Quit""")
        choice = int(input(": "))

        if choice == 1: # view largest score
            print("The largest score is...")
            print(maxScore())
        elif choice == 2: # view smallest score
            print("The smallest score is...")
            print(minScore())
        elif choice == 3: # view average of scores
            print("The average score is...")
            print(avgScore())
        elif choice == 4: # input new score
            newScore() # not in print since it does not return a value but instead the entire function
        else: # user quits
            print("Thank you for using Tetris Analysis!")
            break

        print("Would you like to select another option? (yes/no)") # continues to run until user decides to stop analyzing scores
        again = input(": ")
        if again.lower() == "no": # when user quits
            break

# main
tetrisAnalysis()
