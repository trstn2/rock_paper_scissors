# Tristan
# December 11th 2024
# Rock Paper Scissor game.

import random
import sys

def rock_paper_scissors():
    r_p_s = ["Rock", "Paper", "Scissors"]
    prompt = input("Enter your choice (R)ock, (P)aper, or (S)cissors: ")
    bot_choice = random.choice(r_p_s)

    if prompt == "R":
        if bot_choice == "Rock":
            print("Tie!")
        elif bot_choice == "Paper":
            print("You lose!")
        elif bot_choice == "Scissors":
            print("You win!")
        else:
            print("Sorry an error has prompted the program to quit unexpectedly.")

    if prompt == "P":
        if bot_choice == "Rock":
            print("You win!")
        elif bot_choice == "Paper":
            print("Tie!")
        elif bot_choice == "Scissors":
            print("You lose!")
        else:
            print("Sorry an error has prompted the program to quit unexpectedly.")

    if prompt == "S":
        if bot_choice == "Rock":
            print("You lose!")
        elif bot_choice == "Paper":
            print("You win!")
        elif bot_choice == "Scissors":
            print("Tie!")
        else:
            print("Sorry an error has prompted the program to quit unexpectedly.")

    check_user = input("Would you like to play again? (Y/N): ")
    if check_user == "Y":
        rock_paper_scissors()
    elif check_user == "N":
        sys.exit()

rock_paper_scissors()
