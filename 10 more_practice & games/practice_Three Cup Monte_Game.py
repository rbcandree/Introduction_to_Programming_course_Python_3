# Three Cup Monte Game

from random import shuffle
cups = ['empty', 'Ball', 'empty']

def shuffle_game(cups):
    shuffle(cups)
    return cups
result = shuffle_game(cups)
choice = int(input("Guess, in which cup is a ball? 1st is '0', 2nd is '1', 3rd is '2'. Enter a number: "))
while choice != 0 and choice != 1 and choice != 2:
    choice = int(input("Guess, in which cup is a ball? 1st is '0', 2nd is '1', 3rd is '2'. Enter a number: "))
def player_guess(choice):
    if result[choice] == 'Ball':
        print(f"{result[choice]}! You won!")
    else:
        print(f"Look: {result[choice]}. You loose.")
player_guess(choice)