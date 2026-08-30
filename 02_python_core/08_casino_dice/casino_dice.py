# ================================================================================
# PRACTICE PROJECT: CASINO DICE BETTING GAME
# ================================================================================
# Instructions: Complete the tasks below to build the game!
# Run the file with: python casino_dice.py
# ================================================================================

import random  # Task 1: Import the random module

def roll_dice():
    # Task 2: Simulate rolling two six-sided dice.
    # Return them as a tuple: (die1, die2)
    # Hint: Use random.randint(1, 6) for each die.
    pass

def check_win(guess, dice_sum):
    # Task 3: Check if the user's guess is correct.
    # guess is a string: "l", "h", or "s"
    # dice_sum is an integer: between 2 and 12
    # Returns True if guess is correct, otherwise False.
    # Rules:
    # - Low ("l"): sum is between 2 and 6 (inclusive)
    # - High ("h"): sum is between 8 and 12 (inclusive)
    # - Seven ("s"): sum is exactly 7
    pass

def main():
    # Task 4: Initialize starting balance ($100)
    balance = 100
    
    print("Welcome to the Casino Dice Betting Game!")
    
    # Task 5: Start the game loop (while True)
    while True:
        # Display current balance
        # Prompt user to enter bet amount (or type "exit" to quit, or "clear" to reset balance to $100)
        # Handle input validation:
        #   - Must be a number
        #   - Must be greater than 0
        #   - Must not be greater than current balance
        
        # Prompt user for their guess ("l" for Low, "h" for High, "s" for Seven)
        # Validate guess input (must be l, h, or s)
        
        # Roll dice using roll_dice() and calculate sum
        
        # Check win using check_win()
        
        # Update balance according to payout rules:
        #   - If won Seven ("s"): add 3 * bet to balance
        #   - If won Low/High ("l"/"h"): add bet to balance
        #   - If lost: subtract bet from balance
        
        # Print round results (what dice rolled, sum, won/lost, new balance)
        
        # Check if player is broke (balance <= 0) and end game if they are
        pass

if __name__ == "__main__":
    main()
