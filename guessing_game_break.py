# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a guessing game

import random

pyguess = random.randint(1, 10)


def main():
    # this function uses a break for guessing game

    # input
    guessing = input("Guess the right number between 1-10: ")
    print("")

    # process
    try:
        guessing = int(guessing)
        while True:
            if guessing == pyguess:
                print("You got it right 😃, the number was {}".format(pyguess))
                break
            elif guessing < pyguess:
                print("You got it wrong 😞, the number is higher")
                break
            elif guessing > pyguess:
                print("You got it wrong 😞, the number is lower")
                break
            else:
                print("invalid input")
                break
    except Exception:
        print("sorry, that was not an integer")


if __name__ == "__main__":
    main()
