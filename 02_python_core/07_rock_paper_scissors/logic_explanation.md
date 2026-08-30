# 🪨📄✂️ Rock, Paper, Scissors: Logic Explanation

This document explains the logic structure and flow of the completed Rock, Paper, Scissors terminal game.

---

## 1. Core Functions

### A. `get_computer_choice()`
* Defines a list of options: `["rock", "paper", "scissors"]`.
* Uses Python's built-in `random.choice()` function to select one element from the list randomly and return it.

```python
def get_computer_choice():
    choice =  ["rock", "paper", "scissors"]
    return random.choice(choice)
```

### B. `determine_winner(user_choice, computer_choice)`
* Compares the user's choice with the computer's choice.
* Returns `"tie"` if they chose the same item.
* Returns `"user"` if the user won:
  * Rock beats Scissors.
  * Paper beats Rock.
  * Scissors beat Paper.
* Returns `"computer"` in all other cases.

```python
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"
    elif user_choice == "paper" and computer_choice == "rock":
        return "user"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "computer"
    elif user_choice == "rock" and computer_choice == "paper":
        return "computer"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "computer"
```

---

## 2. Game Menu & Control Flow (`main()`)

The game runs inside a `while True` loop to allow continuous gameplay.

### A. Score Initialization
* Before the loop starts, three variables keep track of the game state:
  `user_score`, `computer_score`, and `ties_score` are initialized to 0.

### B. Normalization & Input Validation
* Takes the user input and applies `.lower().strip()` to handle mixed cases cleanly (e.g., `"Rock "`, `"ROCK"`).
* Checks if input is invalid: if the choice is not in `["rock", "paper", "scissors"]` (and is not a special command), it warns the user and continues to the next round.

### C. Special Commands
* **`exit`**: If user inputs `"exit"`, print a parting message along with the final scores, and use `break` to exit the loop.
* **`clear`**: If user inputs `"clear"`, display the scores accumulated up to that point, reset `user_score`, `computer_score`, and `ties_score` to 0, print a confirmation message, and continue back to the start of the loop.

### D. Playing a Round
* If user chose a valid game item (rock/paper/scissors), call `get_computer_choice()`.
* Print the choices (e.g., "You chose: Rock | Computer chose: Paper").
* Pass both choices to `determine_winner()`.
* Match the result (`"tie"`, `"user"`, or `"computer"`):
  * If `"tie"` ➔ Increment `ties_score` and print "It's a tie!".
  * If `"user"` ➔ Increment `user_score` and print "You win!".
  * If `"computer"` ➔ Increment `computer_score` and print "Computer wins!".
* Print the current scores.

```python
def main():
    # Initialize score counters for user wins, computer wins, and ties
    user_score = 0
    computer_score = 0
    ties_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        choice = input("\nEnter your choice (rock, paper, scissors, exit or clear): ").lower().strip()
        
        if choice == "exit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties_score}")
            break
        elif choice == "clear":
            print(f"Final Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties_score}")
            user_score = 0
            ties_score = 0
            computer_score = 0
            print(f"Your score is reset")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties_score}")
            continue
        elif choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # 1. Get and store the computer's choice
        computer_choice = get_computer_choice()
        
        # 2. Print both choices so the player knows what happened
        print(f"You chose: {choice.capitalize()} | Computer chose: {computer_choice.capitalize()}")

        # 3. Determine the winner and update scores
        result = determine_winner(choice, computer_choice)
        if result == "tie":
            ties_score += 1
            print("It's a tie!")
        elif result == "user":
            user_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("Computer wins!")
            
        # 4. Print current score
        print(f"Score: You - {user_score}, Computer - {computer_score}, Ties - {ties_score}")
```
