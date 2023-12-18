"""
CS50 - Guessing Game
Author: Roger Nem
About: Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again
       Randomly generates an integer between 1 and n, inclusive, using the random module.
       Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
"""

# Importing the required library
import random

while True:
    try:
        # Prompts the user for a level, n
        level = int(input("Level: "))
        # If the user does not input a positive integer, the program should prompt again
        if level > 0:
            break
    except:
        pass

# Randomly generates an integer between 1 and n
random_int = random.randint(1, level)

while True:
    try:
        # If the guess is not a positive integer, the program should prompt the user again
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_int:
                print("Too small!")
            elif guess > random_int:
                print("Too large!")
            elif guess == random_int:
                print("Just right!")
                break
    except:
        pass