#!/usr/bin/env python3

"""
Number guessing Game.
Author: Your Name
Date: 20.05.2025
"""

import random

def main():
    """Main entry point of the program."""
    try:
        print("Starting program!")
        # Output results
        rnd = random.randint(1, 10)
        while True:
            number = input("Please enter a number from 1-10: \n")
            number = int(number)
            if (number > 0 and number < 11):
                if number == rnd:
                    print("You got it right! \n")
                    break
                else:
                    print("You got it wrong!")
                    if rnd < number:
                        print("The number smaller than what you guessed \n")
                    elif rnd > number:
                        print("The number is bigger than what you guessed \n")
                    continue
            else:
                print("You have not entered a number from 1-10")
                continue
                
        
        print("Program completed successfully")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    
if __name__ == "__main__":
    main()
