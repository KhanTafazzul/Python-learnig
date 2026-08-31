# 🎲 Casino Dice Betting Game: Logic Explanation

This document explains the logic structure and flow of the completed Casino Dice Betting Game.

---

## 1. Game Setup & Rules
* **Starting Balance:** The player starts with **$100**.
* **Rolling the Dice:** In each round, the computer rolls two 6-sided dice. The sum ranges from **2 to 12**.
* **Guesses & Payout Multipliers:**
  * **`L` (Low):** Sum is between **2 and 6** (inclusive). Pays out **1x** the bet.
  * **`H` (High):** Sum is between **8 and 12** (inclusive). Pays out **1x** the bet.
  * **`S` (Seven):** Sum is exactly **7**. Pays out **3x** the bet.

---

## 2. Functions & Code Walkthrough

### A. `roll_dice()`
* Simulates rolling two standard dice using `random.randint(1, 6)`.
* Returns them grouped together as a tuple: `(die1, die2)`.

```python
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return (dice1, dice2)
```

### B. `check_win(guess, dice_sum)`
* Compares the user's `guess` (`"l"`, `"h"`, or `"s"`) with the `dice_sum`.
* Returns `True` if correct, `False` otherwise.
* Uses direct boolean returns for clean, professional Python code:
  * For `'l'`: returns `dice_sum <= 6`
  * For `'h'`: returns `dice_sum >= 8`
  * For `'s'`: returns `dice_sum == 7`

```python
def check_win(guess, dice_sum):
    if guess == 'l':
        return dice_sum <= 6
    elif guess == 'h':
        return dice_sum >= 8
    elif guess == 's':
        return dice_sum == 7
    return False
```

### C. `main()`
* Keeps track of the player's `balance` (starts at 100).
* Runs inside a `while True` loop:

  1. **User Action Selection:** Prompts player to press `[Enter]` to bet, or type `'exit'` to quit, or `'clear'` to reset balance to $100.
     ```python
     choice = input("Press [Enter] to bet, type 'exit' to quit, or 'clear' to reset balance: ").lower().strip()
     
     if choice == "exit":
         print("\nThanks for playing!")
         print(f"You walked away with: ${balance}")
         break
     elif choice == "clear":
         balance = 100
         print("Balance has been reset to $100.")
         continue
     ```

  2. **Broke Check:** If the balance is `<= 0`, prints game over and exits the loop.
     ```python
     if balance <= 0:
         print("\nYou are out of money! Game Over.")
         break
     ```

  3. **Bet Amount & Validation:** Uses a `try-except ValueError` block to safely convert input to an integer. Validates that the bet is positive and does not exceed the current balance.
     ```python
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
     ```

  4. **Guess & Validation:** Prompts the user for `'l'`, `'h'`, or `'s'` and validates the input.
     ```python
     guess = input("Enter your guess (l for Low (2-6), h for High (8-12), s for Seven (7)): ").lower().strip()
     if guess not in ["l", "h", "s"]:
         print("Invalid guess! Please enter 'l', 'h', or 's'.")
         continue
     ```

  5. **Roll and Display:** Calls `roll_dice()`, calculates the sum, and prints the individual rolls and total sum.
     ```python
     die1, die2 = roll_dice()
     dice_sum = die1 + die2
     print(f"\nRolling the dice... You rolled: {die1} and {die2} (Total: {dice_sum})")
     ```

  6. **Results & Payout Logic:**
     * If the guess is correct and the sum is exactly 7 ➔ player gets a **3x payout** (`balance += bet * 3`).
     * If the guess is correct and the sum is any other number ➔ player gets a **1x payout** (`balance += bet`).
     * If incorrect ➔ player loses the bet amount (`balance -= bet`).
     ```python
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
     ```
