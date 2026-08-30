# 🎲 Casino Dice Betting Game: Logic Explanation

This document explains the logic structure and flow of the Casino Dice Betting Game.

---

## 1. Game Setup & Rules
* **Starting Balance:** The player starts with **$100**.
* **Rolling the Dice:** In each round, the computer rolls two 6-sided dice. The sum ranges from **2 to 12**.
* **Guesses & Payout Multipliers:**
  * **`L` (Low):** Sum is between **2 and 6** (inclusive). Pays out **1x** the bet.
  * **`H` (High):** Sum is between **8 and 12** (inclusive). Pays out **1x** the bet.
  * **`S` (Seven):** Sum is exactly **7**. Pays out **3x** the bet.

---

## 2. Functions to Complete
You will write the following functions in `casino_dice.py`:

### A. `roll_dice()`
* Roll two separate dice using `random.randint(1, 6)`.
* Return a tuple containing: `(die1, die2)`.

### B. `check_win(guess, dice_sum)`
* Compare the user's `guess` (`"l"`, `"h"`, or `"s"`) with the `dice_sum`.
* Return `True` if the guess is correct (won).
* Return `False` if the guess is incorrect (lost).

### C. `main()`
* Maintains the player's balance variable (starting at 100).
* Contains the game loop (`while True`) that:
  1. Prompts the user for a bet amount or to type `exit` or `clear` (resets balance to $100).
  2. Validates that the bet is a valid integer between $1 and the player's current balance.
  3. Prompts the user for their guess (`l`, `h`, or `s`) and validates it.
  4. Rolls the dice and calculates the sum.
  5. Determines if the player won or lost.
  6. Updates the balance:
     * If guess was `S` and won ➔ `balance += bet * 3`
     * If guess was `L` or `H` and won ➔ `balance += bet`
     * If lost ➔ `balance -= bet`
  7. Checks if `balance <= 0` ➔ game over!
