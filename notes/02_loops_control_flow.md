# 🔄 Python Core: Loops

A loop is a way to repeat a block of code multiple times. Instead of writing the same code 10 times, you write it once and tell Python to repeat it.

## 💡 Why do we use loops?
* **Automate Repetitive Tasks:** Instead of copy-pasting code, let loops do the repeating.
* **Iterate Data:** Traverse through lists, tuples, or strings.
* **Run Continuous Programs:** Keep a game or menu running until the user decides to exit.

---

## 1. For Loops
Used when you know in advance how many times you want to run the code, or when you want to step through a collection of items.

### Syntax
```python
for variable in sequence:
    # code to repeat
```

### Core Functions & Usages

#### A. `range(start, stop, step)`
Generates a sequence of numbers.
* **`start`**: (Optional) Starting number. Defaults to 0.
* **`stop`**: (Required) Stops **before** this number.
* **`step`**: (Optional) How much to increment by. Defaults to 1.

```python
# Loops from 0 to 4
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# Loops from 1 to 5
for i in range(1, 6):
    print(i)  # Prints: 1, 2, 3, 4, 5

# Loops even numbers from 2 to 8
for i in range(2, 9, 2):
    print(i)  # Prints: 2, 4, 6, 8
```

#### B. Iterating through a List
```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
```

#### C. `enumerate(sequence, start=0)`
Returns both the index (counter) and the value at the same time.
```python
names = ["Aman", "Priya", "Rahul"]
for index, name in enumerate(names, 1):
    print(f"User {index}: {name}")
# Output:
# User 1: Aman
# User 2: Priya
# User 3: Rahul
```

---

## 2. While Loops
Used when you don't know exactly how many times the loop will run, and it should keep running as long as a condition remains True.

### Syntax
```python
while condition:
    # code to repeat
```

```python
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1  # Crucial: increments count so the loop doesn't run forever!
```

### Infinite Loops
If the condition never becomes False, the loop runs forever. This is useful for interactive menus when combined with a `break` statement.
```python
while True:
    choice = input("Enter 5 to exit: ")
    if choice == '5':
        break  # Stops the loop immediately
```

---

## 3. Loop Control Statements
Python has three special keywords to control how loops behave:

### A. `break`
Exits the loop immediately, skipping any remaining code or iterations.
```python
for num in range(1, 10):
    if num == 5:
        break  # Stops the loop completely when num is 5
    print(num)  # Prints: 1, 2, 3, 4
```

### B. `continue`
Skips the rest of the current iteration and jumps straight to the next loop step.
```python
for num in range(1, 6):
    if num == 3:
        continue  # Skips printing 3
    print(num)  # Prints: 1, 2, 4, 5
```

### C. `pass`
Does absolutely nothing. Used as a placeholder when code is syntactically required.
```python
for num in range(5):
    pass  # No error thrown
```

---

## ⚠️ Common Gotchas & Tips
* **Infinite Loop Crash:** If you forget to update the loop variable in a `while` loop, your program will hang. Press `Ctrl + C` in the terminal to stop it.
* **Off-by-One Error:** Remember that `range(1, 5)` loops 4 times (1, 2, 3, 4), **not** 5 times. The stop index is always excluded.
