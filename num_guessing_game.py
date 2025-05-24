## Number Guessing Game
# The program randomly selects a number, and the user tries to guess it.

import random

random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
# print(random_integer)

print("I have selected a number. Try guessing it!!")
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Enter a valid integer between 1 and 100")

    if guess > random_integer:
        print("Your guess is greater than the chosen integer!")
    elif guess < random_integer:
        print("Your guess is lesser than the chosen integer!")
    elif guess == random_integer:
        print("Yay! You've guessed the number!")
        break