# python_portfolio
A repository containing my python projects for semester 1 (projects 1-5) and 2 of my projects during semester 2 (projects 6 and 7).

## 1) Guessing Game
### Summary:
In this guessing game, players will have 3 chances to guess a random number. Players guess a number from 1 to 10.
### Key Features:
#### _Limited Guesses_
Players are limited to 3 guesses to get the correct number before they lose.
#### _Hints_
Players are given hints after each incorrect try that tells them if their guess was too high or too low.
#### _Score_
Players are presented with a score out of 90 points after their game ends. Each try is worth 30 points.
#### _Endless Mode_
Players can choose to continue playing after their game ends or can choose to quit.

## 2) Madlibs Game
### Summary:
An interactive story where players input words that fall into specific categories and get to read a story made with those words. Categories are animals, names, adjectives, places, and an item.
### Key Features:
#### _User Inputs_
Players can be involved in the creation of the story and get to read it after.
#### _Bold Text_
Player inputs are bolded in the final story to allow them to see where their inputs are being used.

## 3) Multiplication Quiz
### Summary:
A multiplication quiz to help users practice multiplying numbers from 0-12. Users are given the correct answer if they get the question wrong to help them learn.
### Key Features:
#### _Difficulty Levels_
There are 4 difficulty levels players can choose from:
- easy (numbers 0-4)
- medium (numbers 4-8)
- hard (numbers 8-12)
- all (numbers 0-12)
#### _Quiz Length_
Users can choose how many questions they want to do 
#### _Endless Mode_
After the quiz is over, users can choose to continue doing a new set of questions at a new difficulty level or can choose to quit.

## 4) Snack Name Generator
### Summary:
A snack name generator that asks users questions about what kinds of foods they like eating and gives them a snack food name at the end. Name generator results are Chocolate Icecream, Hot Chocolate, Cinnamon Bun, Pumpkin Pie, Cheesy Nachos, Cheese Puffs, Pretzel, and Trail Mix.
### Key Features:
#### _Endless Mode_
Users can continue to use the name generator after they have been given a snack food name.

## 5) Pokemon Evolution Game
### Summary:
A game where players can train, participate in gym battles, rest, and level up their pokemon. Alongside Squirtle, players go on a journey filled with action and can eventually fight the final boss.
### Key Features:
#### _Training_
Players can choose to spend their day training their pokemon which will level them up by 1 level. Sometimes, a pokemon will do so well training that they level up twice in one day and become happy.
#### _Battles_
Randomized pokemon battles that have 2 outcomes, winning or losing. Chances of winning or losing change depending on the pokemon's mood. Winning will cause the pokemon to level up twice.
#### _Resting_
The player can choose to spend the day resting. Resting displays the pokemon's name, picture, and level. 
#### _Moods_
The pokemon's mood can change while training or from the outcomes of battles. Pokemon's mood changes the odds that they will win battles, either increasing, decreasing, or keeping the odds of winning even. 
#####
Pokemon moods are:
- Happy
- Neutral
- Unhappy
#### _Evolution_
After reaching a certain level, a pokemon can evolve. The pokemon starts off as Squirtle, with the ability to evolve into Wartortle and then Blastoise.
#### _Final Stats_
After the game is over, players get their stats about how they spent their days, how many days they played, and how many battles were both won and lost.

## 6) Magic 8 Ball
### Summary:
A program that simulates a Magic 8 Ball. Users can ask yes or no questions and get one of 15 premade responses as an answer.
### Key Features:
#### _Is it a Question?_
After inputing a question, the program checks to ensure that there is a question mark at the end of the user's input. If there is no question mark, the program will request that users retype their question but this time including a ? to make sure people are asking questions and not statements. This loops until there is a question mark at the end of the sentence.
#### _Another Question?_
After the program gives users a response, users can select "y" if they want to ask another question and this continues until users have asked all of their questions and stops the Magic 8 Ball.

## 7) Slot Machine
### Summary:
A simulation of a slot machine where players start off with 100 credits and can bet from 5, 20, or 100 credits each time they spin. Players win credits if the slot machine displays 2 of a kind, a match (three of the same symbols that aren't 7s), or a jackpot of three 7s.
### Key Features:
#### _Less Credits, Less Options_
With the three betting options of 5, 20, and 100, a player can only bet those amounts if they have them. If the user doesn't have 100 credits but bets 100, the program will inform them that they cannot do that and advises they bet a different amount. This continues until they either run out of credits or win enough to chose the option they want to.
#### _Random Symbols_
There are a list of possible symbols which include repeating symbols which changes the probabilities of certain symbols appearing in the slot machine. This list is used when the slot machine runs and gives players three random symbols from that list.
#### _Winning Symbols_
For two of a kind, the program checks to see if any two symbols match and if they do, players are rewarded 2x credits. For a match, the program checks to see if each of the symbols matches the other symbols displayed (this doesn't apply to all symbols being 7s) and if it is a match, the player is awarded 5x credits. For a jackpot (all 7s), the program checks to see if all symbols match with the symbol 7 and if they do, players are rewarded with 100x credits.
