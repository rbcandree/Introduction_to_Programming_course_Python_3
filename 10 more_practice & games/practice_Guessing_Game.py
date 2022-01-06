from random import randint
n = randint(1, 100)

print("Let's play a Guessing Game?")
print("You have to guess a number from 1 to 100.")
print("On yours first turn, if your guess is within 10 of the random number, you will receive a hint 'WARM!'")
print("However, if you guess further than 10 away from the number - 'COLD!'")
print("On all subsequent turns, if a guess is closer to the number than the previous guess, you will see 'Warmer'")
print("Or if a guess is farther from the number than the previous guess - 'Colder'")
print("Good luck :)")

num = int(input("Let's start the game! Enter your number, please: "))
guesses = [0]

while num != n:
    if num < 1 or num > 100:
        print("Oops! Out of bonds. Please try again: ")
        num = int(input("Enter a new number, please: "))
        continue
    elif n == num:
        break
    guesses.append(num)
    
    if guesses[-2]:
        if abs(n - num) < abs(n - guesses[-2]):
            print('Warmer')
            num = int(input("Enter a new number, please: "))
            pass
        elif abs(n - num) > abs(n - guesses[-2]):
            print('Colder')
            num = int(input("Enter a new number, please: "))
            pass
    else:
        if abs(n - num) <= 10:
            print('WARM')
            num = int(input("Enter a new number, please: "))
        else:
            print('COLD')
            num = int(input("Enter a new number, please: "))


print("Congratulations! You have guessed the number!")
print(f"It took you a {len(guesses)} time(s) :)")