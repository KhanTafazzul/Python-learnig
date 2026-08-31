# 🛡️ Python Core: Exception Handling

An Exception is an error that occurs while a program is running, which causes it to crash. Exception handling tells Python what to do instead of crashing.

---

## 1. The `try-except-else-finally` Structure

```python
try:
    # 1. Place code here that MIGHT crash.
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    # 2. Runs if user inputs non-numeric characters.
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    # 3. Runs if user inputs 0.
    print("Error: Cannot divide by zero!")
except Exception as e:
    # 4. Fallback: Catches any other unexpected errors and shows the details.
    print(f"An unexpected error occurred: {e}")
else:
    # 5. Runs ONLY if the try block succeeded without any errors.
    print("Result is:", result)
finally:
    # 6. ALWAYS runs, no matter what (even if the code crashed).
    # Ideal for cleanup tasks.
    print("Calculation cycle complete.")
```

---

## 2. The `raise` Statement (Triggering Custom Errors)

Sometimes, you need to manually force an error to occur because a user input breaks a business rule, even if it is mathematically valid in Python. You do this using the `raise` keyword.

*   **Syntax:** `raise ExceptionType("Custom message")`
*   **Why use it?** To stop execution immediately when invalid data is detected (e.g. negative age, empty password settings).

### Example:
```python
def check_age(age):
    if age < 0:
        # Trigger an error manually
        raise ValueError("Age cannot be negative!")
    print(f"Age is set to {age}.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught an error: {e}")
# Output: Caught an error: Age cannot be negative!
```

---

## 3. Difference Between `raise` and Exception Handling

It is important to distinguish between **triggering** a problem and **solving** a problem:

*   **`raise` is like a Fire Alarm:** It signals that a rule is broken and triggers an error state, halting execution.
*   **Exception Handling (`try-except`) is like Firefighters:** It catches the error state, resolves it (e.g., asks the user to try again), and keeps the program from crashing.

### Comparison Table:

| Component | Keyword / Block | Purpose | Example / Use Case |
| :--- | :--- | :--- | :--- |
| **Triggering** | `raise` | Forces an error to occur immediately. | `raise ValueError("Invalid range!")` |
| **Guarding** | `try` | Wraps risky code that might crash. | `try: number = int(input())` |
| **Handling** | `except` | Catches and handles a specific error. | `except ValueError: print("Enter numbers only!")` |
| **Successful Path**| `else` | Runs only if no errors occurred in `try`. | Printing results or database commit. |
| **Cleanup** | `finally` | Always runs, regardless of success or crash. | Closing open files or database connections. |

---

## 4. Common Built-in Exceptions

* **`ValueError`**: A function receives an argument of the correct type but inappropriate value.
  * *Example:* `int("abc")` (Converting letters to an integer).
* **`ZeroDivisionError`**: Dividing a number by zero.
  * *Example:* `10 / 0`.
* **`FileNotFoundError`**: Trying to open a file that does not exist.
  * *Example:* `open("missing.txt", "r")`.
* **`KeyError`**: Searching for a dictionary key that isn't present.
  * *Example:* `student = {"name": "Aman"}` ➔ `student["age"]`.
* **`IndexError`**: Accessing a list index that is out of range.
  * *Example:* `my_list = [10, 20]` ➔ `my_list[5]`.
* **`TypeError`**: Performing an operation on incompatible data types.
  * *Example:* `"hello" + 5`.

---

## 5. Practice Examples

### Safe Division Function
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Error: Inputs must be numbers!")
        return None
```

### Safe File Reader
```python
def safe_read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"⚠️ Error: File '{filename}' was not found.")
        return ""
```

---

## 💡 Best Practices
* **Avoid Bare `except:` Statements:** Never use a plain `except:` without specifying error types. It will block critical exits (like `Ctrl+C`). Use `except Exception as e:` if you need a catch-all.
* **Catch Specific Errors First:** Put specific exceptions (like `ValueError`) first, and general exceptions (like `Exception`) at the bottom.
