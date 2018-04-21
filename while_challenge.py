# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: \nEnter 0 (zero) to exit".format(highest))

while True:
    guess = int(input())
    if guess == 0:
        print("Exiting the program.")
        break
    elif guess == answer:
        print("Well done you guessed it.")
        break
    elif guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
print("See you next time")
