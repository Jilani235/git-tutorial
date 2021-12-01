#! /usr/bin/python3

# The random package is needed to choose a random number
import random

# Define the game in a function
def guess_loop():
    # This is the number the user will have to guess, chosen randomly in between 1 and 100
    number_to_guess = random.randint(1, 100)
    print("J'ai un nombre en tête. Peut-tu le trouver ?"))

    # Replay the question until the user finds the correct number
    while True:
        try:
            # Read the number the user inputs
            guess = int(input())

            # Compare it to the number to guess
            if guess > number_to_guess:
                print("Mon nombre est plus petit")
            elif guess < number_to_guess:
                print("Mon nombre est plus grand")
            else:
                # The user found the number to guess, let's exit
                print("Bravo, tu as trouvé mon nombre. C'était ", guess)
                return
        # A ValueError is raised by the int() function if the user inputs something else than a number
        except ValueError as err:
            print("Mon nombre est un entier, tu as mis autre chose")

# Launch the game
guess_loop()
