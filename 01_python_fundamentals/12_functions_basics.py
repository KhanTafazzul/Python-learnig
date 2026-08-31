# Question 12: Introduction to Functions (`def`, parameters & `return`)
#
# Problem Statement:
# Learn basic function creation by defining a greeting function and a boolean function to check even numbers.
#
# Tasks to complete:
# 1. Define `greet(name)` to print a personalized welcome message.
# 2. Define `is_even(number)` that returns `True` if even, `False` if odd.
# 3. Call `greet()` with user input.
# 4. Call `is_even()` and print whether the entered number is even or odd.
#
# Write your code below this line:

def greet(name):
    print(f"Hello, {name}! Welcome to Python functions.")

def is_even(number):

    if number % 2 == 0:
        return True
    
    else:
        return False
    
greet(input("Enter your name: "))

number = int(input("Enter a number to check if it is even or odd: "))
boolean = is_even(number)

if boolean == True:

    print(f"{number} is even.")
else:

    print(f"{number} is odd.")