#!/usr/bin/env python3

"""
Number guessing Game.
Author: Your Name
Date: 20.05.2025
"""

import random

def main():
    listChoose = ["scissor", "paper", "rock"]

    counterUser = 0
    counterComputer = 0

    try:
        while counterUser < 5 and counterComputer < 5:
            userChoose = input("rock, paper, scissor? \n")
            userChoose = userChoose.lower()
            if userChoose in listChoose:
                computerChoose = random.choice(listChoose)
                print(f"User has {userChoose}, Computer has {computerChoose} ")
                if userChoose == computerChoose:
                    print("Nobody wins")
                else:
                    if userChoose == "scissor":
                        if computerChoose == "rock":
                            print("Computer wins!")
                            counterComputer += 1
                        elif computerChoose == "paper":
                            print("User wins!")
                            counterUser += 1
                    elif userChoose == "rock":
                        if computerChoose == "scissor":
                            print("User wins!")
                            counterUser += 1
                        elif computerChoose == "paper":
                            print("Computer wins!")
                            counterComputer += 1
                    elif userChoose == "paper":
                        if computerChoose == "scissor":
                            print("Computer wins!")
                            counterComputer += 1
                        elif computerChoose == "rock":
                            print("User wins!")
                            counterUser += 1
                print(f"User has {counterUser} points and Computer has {counterComputer} points \n")
            else:
                print(f"{userChoose} is not a valid input! Try again \n")

        print("Game has ended successfully")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

if __name__ == "__main__":
    main()