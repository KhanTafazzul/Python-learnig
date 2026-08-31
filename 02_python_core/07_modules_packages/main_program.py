# Main Program: main_program.py
from my_math import add, subtract

# TODO: Import add and subtract from my_math module using 'from ... import ...'


# TODO: Import the entire my_math module with an alias 'mm' using 'import ... as ...'
import my_math as mm

# --- Test Section ---
# 1. Use the imported 'add' function and print the result
# 2. Use the imported 'subtract' function and print the result
# 3. Use the 'mm' alias to call 'multiply' and print the result
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(add(a,b))
print(subtract(a,b))
print(mm.multiply(a,b))