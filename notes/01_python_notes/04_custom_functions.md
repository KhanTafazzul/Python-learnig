# 🛠️ Python Custom Functions & Scope: Reference Notes

This notes document covers how to create and use custom functions in Python, passing data via arguments, returning results, using dynamic inputs, and understanding local vs. global variable scopes.

---

## 1. Defining and Calling Functions

### A. Defining a Basic Function (`def`)
*   **Definition:** Creates a reusable block of code that runs only when called.
*   **Syntax:**
    ```python
    def function_name():
        # Code block
    ```
*   **Return Datatype:** `None` (if no return statement is used)
```python
def say_hello():
    print("Hello, welcome to Python!")

# Calling the function
say_hello()
# Output: Hello, welcome to Python!
```

---

## 2. Function Inputs (Parameters & Arguments)

### A. Parameters vs. Arguments
*   **Definition:** 
    *   **Parameters:** The variable names listed inside the function's parentheses in the definition.
    *   **Arguments:** The actual values sent to the function when calling it.
*   **Syntax:**
    ```python
    def function_name(parameter):
        # Code block
    ```
*   **Return Datatype:** `None` (by default)
```python
# 'name' is the parameter
def greet_user(name):
    print(f"Welcome back, {name}!")

# "Aman" is the argument
greet_user("Aman")
# Output: Welcome back, Aman!
```

### B. Positional vs. Keyword Arguments
*   **Definition:**
    *   **Positional Arguments:** Arguments passed to a function based on their order.
    *   **Keyword Arguments:** Arguments passed by explicitly specifying the parameter name, allowing you to pass them in any order.
*   **Syntax:** `function_name(param1=val1, param2=val2)`
*   **Return Datatype:** `None` (by default)
```python
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 1. Positional (Order matters)
print_info("Aman", 20)          # Output: Name: Aman, Age: 20

# 2. Keyword (Order does not matter)
print_info(age=20, name="Aman") # Output: Name: Aman, Age: 20
```

### C. Default Parameter Values
*   **Definition:** Allows a parameter to have a default value if no argument is passed during the function call.
*   **Syntax:** `def function_name(param = default_value):`
*   **Return Datatype:** `None` (by default)
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Aman")  # Output: Hello, Aman!
greet()        # Output: Hello, Guest! (uses default)
```

---

## 3. Returning Data from Functions

### A. The `return` Statement
*   **Definition:** Sends a value back from the function to the caller and terminates the function's execution immediately.
*   **Syntax:** `return value`
*   **Return Datatype:** The datatype of the returned value (e.g., `int`, `str`, `list`, etc.)
```python
def square(number):
    return number * number

result = square(4)
print(result)
# Output: 16 (result is an integer)
```

### B. Returning Multiple Values
*   **Definition:** Python allows returning multiple values from a function, which are returned packaged together in a tuple.
*   **Syntax:** `return val1, val2, ...`
*   **Return Datatype:** `tuple`
```python
def get_min_max(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest  # returns a tuple

low, high = get_min_max([5, 12, 1, 8, 20])
print(f"Low: {low}, High: {high}")
# Output: Low: 1, High: 20
```

---

## 4. Dynamic Inputs (Arbitrary Arguments)

### A. Positional Arbitrary Arguments (`*args`)
*   **Definition:** Used when you do not know beforehand how many positional arguments will be passed to your function. Python groups them into a tuple.
*   **Syntax:** `def function_name(*args):`
*   **Return Datatype:** `None` (by default)
```python
def sum_all(*numbers):
    # 'numbers' is treated as a tuple containing all passed values
    total = sum(numbers)
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(5, 10, 15, 20))  # Output: 50
```

### B. Keyword Arbitrary Arguments (`**kwargs`)
*   **Definition:** Used when you do not know beforehand how many keyword arguments will be passed to your function. Python groups them into a dictionary.
*   **Syntax:** `def function_name(**kwargs):`
*   **Return Datatype:** `None` (by default)
```python
def show_user_profile(**details):
    # 'details' is treated as a dictionary
    for key, value in details.items():
        print(f"{key}: {value}")

show_user_profile(Name="Aman", City="Delhi", Role="Developer")
# Output:
# Name: Aman
# City: Delhi
# Role: Developer
```

---

## 5. Scope: Local vs. Global Variables

### A. Local Scope
*   **Definition:** Variables created inside a function belong to the local scope of that function and can only be accessed inside it.
*   **Syntax:** Declaring a variable inside a function body.
*   **Return Datatype:** N/A
```python
def my_func():
    local_val = 100  # Local variable
    print(local_val)

my_func()  # Output: 100

# Accessing local_val outside the function raises an error
try:
    print(local_val)
except NameError as e:
    print("Error:", e)
# Output: Error: name 'local_val' is not defined
```

### B. Global Scope & `global` Keyword
*   **Definition:** Variables created in the main body of the script are global and can be accessed anywhere. To modify a global variable inside a function, you must use the `global` keyword.
*   **Syntax:** `global variable_name` inside a function body.
*   **Return Datatype:** N/A
```python
count = 10  # Global variable

def increment_count():
    global count  # Tells Python to use the global 'count' variable
    count += 1

increment_count()
print(count)
# Output: 11
```
