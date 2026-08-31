# Question 21: Number Guessing Game (Loops, Conditions & Random Module)
#
# Problem Statement:
# Create an interactive game where the computer picks a random secret number between 1 and 100, 
# and the user has to guess it. After each guess, the program should tell the user 
# if their guess was "Too High!", "Too Low!", or "Correct!".
#
# Tasks to complete:
# 1. Import the `random` module and generate a secret number between 1 and 100 using `random.randint(1, 100)`.
# 2. Keep track of the number of attempts (attempts counter starting at 0).
# 3. Use a `while` loop to repeatedly ask the user to guess the number.
# 4. For each guess:
#    - Increment attempts by 1.
#    - If guess > secret number, print "Too High! Try again."
#    - If guess < secret number, print "Too Low! Try again."
#    - If guess == secret number, print "Congratulations! You guessed it in X attempts!" and exit the loop.
#
# Write your code below this line:

import random

ran_no = random.randint(1 , 100)
attempt = 0
user_no = 0

while (ran_no != user_no):
    
    user_no = int(input("Enter the number you want to guess: "))
    attempt += 1

    if user_no == ran_no:
        print(f"Congratulations! You guessed it in {attempt } attempts!")
        break

    elif user_no < ran_no:
        print("Too Low! Try again.")

    elif user_no > ran_no:
        print("Too High! Try again.")
    




