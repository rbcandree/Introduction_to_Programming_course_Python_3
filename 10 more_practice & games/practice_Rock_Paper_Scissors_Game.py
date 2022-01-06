# Rock, Paper, Scissors Game
# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. 

# The program should work as follows:
# 1. When the program begins, a random number in the range of 1 through 3 is generated. 
# If the number is 1, then the computer has chosen rock. 
# If the number is 2, then the computer has chosen paper. 
# If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)
# 2. The user enters his(her) choice of “rock,” “paper,” or “scissors” at the keyboard.
# 3. The computer’s choice is displayed.
# 4. A winner is selected according to the following rules:
# - If one player chooses rock and the other playerchooses scissors, then rock wins. (Rock smashes scissors)
# - If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper)
# - If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock)
# - If both players make the same choice, the game must be played again to determine the winner.

import random
# Define constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3
INVALID = 3

def main():
    result = TIE
    while result == TIE:
        computer = random.randint(1, 3)
        player = int(input('Enter 1 for Rock, 2 for Paper, 3 for Scissors: '))
        print('Computer chose', choiceStr(computer))
        print('Player chose', choiceStr(player))

        result = winner(computer, player)
        if result == TIE:
            print('The result is TIE')
    if (result == COMPUTER_WINS):
        print('Computer wins')
    elif(result == PLAYER_WINS):
        print('You win the game')
    else:
        print('You have entered an invalid choice')

# The winner function receives numbers representing the computer and player's choices.
# It returns 0 - if there is a tie, 1 - if the computer won, 2 - if the player won, or 3 - if the player made an invalid choice.

def winner(compChoice, playerChoice):
    if(compChoice == playerChoice):
        return TIE
    if compChoice == ROCK:
        if playerChoice == PAPER:
            return PLAYER_WINS
        elif playerChoice == SCISSORS:
            return COMPUTER_WINS
        else:
            return INVALID

    elif compChoice == PAPER:
        if playerChoice == ROCK:
            return COMPUTER_WINS
        elif playerChoice == SCISSORS:
            return PLAYER_WINS
        else:
            return INVALID

    else:  # the 3rd option - computer has chosen SCISSORS
        if playerChoice == ROCK:
            return PLAYER_WINS
        elif playerChoice == PAPER:
            return COMPUTER_WINS
        else:
            return INVALID

# The choiceStr function displays a choice in string format:

def choiceStr(choice):
    if choice == ROCK:
        return 'Rock'
    elif choice == PAPER:
        return 'Paper'
    elif choice == SCISSORS:
        return 'Scissors'
    else:
        return 'Invalid choice'
main()