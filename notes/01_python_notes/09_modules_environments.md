# 🛠️ Python Core: Modules, Packages & Libraries

Modules and Packages help organize code and make it reusable across files.

---

## 1. What is a Module and Package?
* **Module:** A single Python file (`.py`) containing variables, functions, or classes that you can import and reuse.
* **Package:** A directory containing multiple modules grouped together. It traditionally contains a special file named `__init__.py` (which tells Python that this directory should be treated as a package).

---

## 2. Importing Syntax
You can import modules in different ways:

### A. Entire Module
```python
import math
print(math.sqrt(16))  # Must use math prefix
```

### B. Module with Shortcut (Alias)
```python
import random as rd
roll = rd.randint(1, 6)  # Uses rd prefix
```

### C. Specific Functions (No prefix needed)
```python
from math import sqrt, pi
print(sqrt(16))  # No prefix required!
```

---

## 3. Core Standard Libraries

### A. The `random` Module
Used to generate random numbers and make random selections.
* **`random.randint(a, b)`**: Random integer between `a` and `b` (inclusive).
* **`random.choice(sequence)`**: Selects a random element from a list/tuple/string.
* **`random.random()`**: Random float between `0.0` and `1.0` (excluding `1.0`).
* **`random.uniform(a, b)`**: Random float between `a` and `b`.
* **`random.shuffle(list)`**: Shuffles the elements of a list in-place.

```python
import random
choices = ["rock", "paper", "scissors"]
print(random.choice(choices))  # e.g., "paper"
```

### B. The `datetime` Module
Used for date and time calculations.
* **`date.today()`**: Returns today's date object (`YYYY-MM-DD`).
* **`datetime.now()`**: Returns current date and time.
* **`timedelta(days=X, weeks=Y)`**: Represents a duration of time (used for arithmetic).
  ```python
  from datetime import date, timedelta
  tomorrow = date.today() + timedelta(days=1)
  ```
* **`strftime(format)`**: Converts datetime object ➔ formatted **String** (Format).
* **`strptime(string, format)`**: Parses string ➔ datetime **Object** (Parse).

---

## 4. Creating Your Own Module
You can write code in one file and import it into another in the same directory.

### Step 1: Create a file `my_math.py`
```python
def add(x, y):
    return x + y
```

### Step 2: Import in `main.py`
```python
import my_math
print(my_math.add(5, 10))  # Outputs: 15
```

---

## 5. The `if __name__ == "__main__":` Statement
```python
if __name__ == "__main__":
    # Code in this block runs ONLY if you run this file directly.
    # It will NOT run if this file is imported by another script.
```
* **Why use it?** It prevents test code, menus, or sample runs inside your module from executing when someone imports it elsewhere.
