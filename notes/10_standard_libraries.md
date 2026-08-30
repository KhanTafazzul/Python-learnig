# 🧪 Python Libraries: Random & Datetime

This document covers two essential built-in Python libraries:
1. `random`   - Used for generating pseudo-random values and choices.
2. `datetime` - Used for managing dates, times, and time arithmetic.

---

## 🎲 1. The `random` Library

### Definition
The `random` library is a built-in Python module that generates pseudo-random numbers, shuffles lists, and makes random selections from sequences.

### Basic Syntax
```python
import random
```

### Key Functions & Examples

#### A. `random.random()`
Returns a random float in the range `[0.0, 1.0)` (excluding `1.0`).
```python
value = random.random()
print(value)  # e.g., 0.374829104
```

#### B. `random.uniform(a, b)`
Returns a random float between `a` and `b`.
```python
value = random.uniform(10.5, 20.0)
print(value)  # e.g., 14.829104
```

#### C. `random.randint(a, b)`
Returns a random integer between `a` and `b` (inclusive of both endpoints).
```python
roll = random.randint(1, 6)
print(roll)  # e.g., 5 (ideal for a dice roll)
```

#### D. `random.randrange(start, stop, step)`
Returns a randomly selected element from `range(start, stop, step)`.
```python
# Get a random even number between 0 and 8 (0, 2, 4, 6, 8)
num = random.randrange(0, 10, 2)
print(num)
```

#### E. `random.choice(sequence)`
Returns a random element from a non-empty list, tuple, or string.
```python
choices = ["Rock", "Paper", "Scissors"]
comp_move = random.choice(choices)
print(comp_move)  # e.g., "Paper"
```

#### F. `random.sample(sequence, k)`
Returns a list of `k` unique elements chosen from a sequence (sampling without replacement).
```python
cards = ["Ace", "King", "Queen", "Jack", "10", "9"]
hand = random.sample(cards, 3)
print(hand)  # e.g., ['King', '10', 'Ace']
```

#### G. `random.shuffle(list)`
Shuffles the items of a list in-place (modifies the original list directly).
```python
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # e.g., [4, 1, 5, 2, 3]
```

#### H. `random.seed(a)`
Initializes the random number generator. Using the same seed will produce the exact same sequence of numbers.
```python
random.seed(42)
print(random.randint(1, 10))  # Will always output 2 when rerun!
```

---

## 📅 2. The `datetime` Library

### Definition
The `datetime` module provides classes for manipulating dates and times. It is useful for timestamping logs, tracking transactions, or calculating differences between dates.

### Basic Syntax
```python
from datetime import datetime, date, time, timedelta
```

### Key Classes & Examples

#### A. `date` Class (Year, Month, Day)
Represents calendar dates.
```python
# Get today's date
today = date.today()
print(today)         # e.g., 2026-08-30
print(today.year)    # 2026
print(today.month)   # 8
print(today.day)     # 30

# Create a custom date
custom_date = date(2025, 12, 25)
print(custom_date)   # 2025-12-25
```

#### B. `time` Class (Hour, Minute, Second)
Represents time independent of any date.
```python
# Create a custom time: time(hour, minute, second)
meeting_time = time(14, 30, 0)
print(meeting_time)  # 14:30:00
```

#### C. `datetime` Class (Date + Time)
Represents a single point containing both date and time values.
```python
# Get current date & time
now = datetime.now()
print(now)           # e.g., 2026-08-30 10:32:00.123456

# Create a custom datetime
event = datetime(2026, 12, 31, 23, 59, 59)
print(event)         # 2026-12-31 23:59:59
```

#### D. `timedelta` Class (Duration & Arithmetic)
Represents the difference/duration between two date or datetime objects.
```python
# Add or subtract days/weeks/hours/minutes
today = date.today()
ten_days_later = today + timedelta(days=10)
three_weeks_ago = today - timedelta(weeks=3)

print("10 Days Later:", ten_days_later)
print("3 Weeks Ago:", three_weeks_ago)

# Difference between two datetimes
time_a = datetime(2026, 8, 30, 10, 0, 0)
time_b = datetime(2026, 8, 30, 12, 45, 0)
duration = time_b - time_a
print(duration)            # 2:45:00
print(duration.seconds)    # 9900 (total seconds)
```

---

## 🔤 Formatting & Parsing (Strftime vs Strptime)

### 1. `strftime()` — Datetime ➔ String (Format)
Converts a datetime object into a formatted string.
```python
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # Outputs: "2026-08-30 10:32:00"
```

### 2. `strptime()` — String ➔ Datetime (Parse)
Parses a string containing a date into a datetime object.
```python
date_str = "30-08-2026 10:32"
parsed_date = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(parsed_date)  # Outputs: 2026-08-30 10:32:00
```

### Common Formatting Directives

| Code | Meaning | Example |
| :--- | :--- | :--- |
| **`%Y`** | Year (4-digit) | `2026` |
| **`%y`** | Year (2-digit) | `26` |
| **`%m`** | Month (2-digit) | `08` |
| **`%B`** | Month (Full name) | `August` |
| **`%d`** | Day of month (2-digit) | `30` |
| **`%H`** | Hour (24-hour clock) | `14` |
| **`%I`** | Hour (12-hour clock) | `02` |
| **`%M`** | Minute (2-digit) | `32` |
| **`%S`** | Second (2-digit) | `00` |
| **`%p`** | AM or PM | `PM` |
