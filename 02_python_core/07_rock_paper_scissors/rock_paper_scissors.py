# ================================================================================
# PRACTICE PROJECT: ROCK, PAPER, SCISSORS (WITH SCORE KEEPER)
# ================================================================================
# Instructions: Complete the tasks below to build the game!
# Run the file with: python rock_paper_scissors.py
# ================================================================================

import random  # Task 1: Import the random module

def get_computer_choice():
    choice =  ["rock", "paper", "scissors"]
    return random.choice(choice)

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

def main():
    # Task 4: Initialize score counters for user wins, computer wins, and ties
    user_score = 0
    computer_score = 0
    ties_score = 0
    
    # Task 5: Start the game loop (while True)
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        choice = input("\nEnter your choice (rock, paper, scissors,exit or clear): ").lower().strip()
        
        if choice == "exit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties_score}")
            break
        elif choice =="clear":
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

if __name__ == "__main__":
    main()
