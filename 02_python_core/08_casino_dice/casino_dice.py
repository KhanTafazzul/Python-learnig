# ================================================================================
# PRACTICE PROJECT: CASINO DICE BETTING GAME
# ================================================================================
# A terminal-based dice betting game where players bet their balance on whether
# the sum of two rolled dice will be Low (2-6), High (8-12), or exactly Seven (7).
# ================================================================================

import random

def roll_dice():
    """
    Simulates rolling two independent six-sided dice.
    Returns:
        tuple: (die1, die2) containing values from 1 to 6.
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2)


def check_win(guess, dice_sum):
    """
    Checks if the player's guess matches the total sum of the rolled dice.
    Args:
        guess (str): 'l' for Low, 'h' for High, 's' for Seven.
        dice_sum (int): The sum of two dice (2 to 12).
    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    if guess == 'l':
        return dice_sum <= 6
    elif guess == 'h':
        return dice_sum >= 8
    elif guess == 's':
        return dice_sum == 7
    return False


def main():
    # Starting balance for the player
    balance = 100
    
    print("==========================================")
    print("Welcome to the Casino Dice Betting Game!")
    print("==========================================")
    
    # Main game loop
    while True:
        print(f"\nCurrent Balance: ${balance}")
        
        # Check if the player wants to exit or reset the game
        choice = input("Press [Enter] to bet, type 'exit' to quit, or 'clear' to reset balance: ").lower().strip()
        
        if choice == "exit":
            print("\nThanks for playing!")
            print(f"You walked away with: ${balance}")
            break
        elif choice == "clear":
            balance = 100
            print("Balance has been reset to $100.")
            continue
            
        # Check if the player is broke before placing a new bet
        if balance <= 0:
            print("\nYou are out of money! Game Over.")
            break
            
        # Get and validate the bet amount
        try:
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
            continue
            
        if bet <= 0:
            print("Bet amount must be greater than $0.")
            continue
        if bet > balance:
            print(f"You cannot bet more than your current balance (${balance}).")
            continue
            
        # Get and validate the guess
        guess = input("Enter your guess (l for Low (2-6), h for High (8-12), s for Seven (7)): ").lower().strip()
        if guess not in ["l", "h", "s"]:
            print("Invalid guess! Please enter 'l', 'h', or 's'.")
            continue
            
        # Roll the dice and calculate sum
        die1, die2 = roll_dice()
        dice_sum = die1 + die2
        print(f"\nRolling the dice... You rolled: {die1} and {die2} (Total: {dice_sum})")
        
        # Check results and apply payout multipliers
        if check_win(guess, dice_sum) and dice_sum == 7:
            # Seven wins pay 3x
            balance += bet * 3
            print(f"🎉 Amazing! You win 3x payout! You rolled exactly Seven!")
        elif check_win(guess, dice_sum):
            # Low/High wins pay 1x
            balance += bet
            print(f"✅ You win! Your guess was correct.")
        else:
            # Loser loses the bet amount
            balance -= bet
            print(f"❌ You lose! Better luck next time.")


if __name__ == "__main__":
    main()
