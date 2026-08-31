# Question 13: Calculator Using Modular Functions
#
# Problem Statement:
# Build a modular calculator with functions for addition, subtraction, multiplication, and division.
# Include error handling for division by zero.
#
# Tasks to complete:
# 1. Define separate functions: `add`, `subtract`, `multiply`, `divide`.
# 2. Implement zero division safety inside `divide(a, b)`.
# 3. Prompt user for two numbers and an operator (`+`, `-`, `*`, `/`).
# 4. Execute the matching function and print the result.
#
# Write your code below this line:

def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

num = float(input("Enter first number: \n"))
operator = input("Enter operator (+, -, *, /):\n ")
num2 = float(input("Enter second number: \n"))

if operator == "+":
    print(f"{num} + {num2} = {add(num , num2)}")

elif operator == "-":
    print(f"{num} - {num2} = {subtract(num , num2)}")

elif operator == "*":
    print(f"{num} * {num2} = {multiply(num , num2)}")

elif operator == "/":
    print(f"{num} / {num2} = {divide(num , num2)}")

else:
    print("Invalid operator. Please use +, -, *, or /.")

