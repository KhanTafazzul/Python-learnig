# 🧮 Python Math Functions: Beginner-Friendly Guide

Welcome! This guide is ordered from the easiest basic math functions to the more advanced ones. All definitions are written in simple words, making them easy to understand for beginners.

---

## 🚀 1. The Absolute Basics (Built-in Functions)
*Note: You do not need to import anything to use these.*

### A. `sum(iterable)`
*   **Simple Definition:** Adds up all the numbers in a list.
*   **Syntax:** `sum(list_of_numbers)`
*   **Return Datatype:** `int` or `float`
```python
numbers = [10, 20, 30]
print(sum(numbers))  # Output: 60
```

### B. `min()` and `max()`
*   **Simple Definition:** `min()` finds the smallest number, and `max()` finds the largest number in a list.
*   **Syntax:** `min(list)` or `min(a, b, c, ...)`
*   **Return Datatype:** Number
```python
numbers = [12, 45, 2, 89]
print("Smallest:", min(numbers))  # Output: 2
print("Largest:", max(5, 10, 15))  # Output: 15
```

### C. `abs(x)`
*   **Simple Definition:** Turns negative numbers into positive numbers. Positive numbers stay positive.
*   **Syntax:** `abs(number)`
*   **Return Datatype:** Number (integer or float)
```python
print(abs(-5))    # Output: 5
print(abs(10.5))  # Output: 10.5
```

### D. `divmod(a, b)`
*   **Simple Definition:** Divides two numbers and gives you both the quotient (how many times it goes in) and the remainder at the same time.
*   **Syntax:** `divmod(number1, number2)`
*   **Return Datatype:** `tuple` -> `(quotient, remainder)`
```python
# 10 divided by 3 is 3 with a remainder of 1
print(divmod(10, 3))  # Output: (3, 1)
```

### E. `pow(base, exp)`
*   **Simple Definition:** Multiplies a number (base) by itself `exp` times.
*   **Syntax:** `pow(base, exponent)`
*   **Return Datatype:** Number
```python
print(pow(2, 3))  # Output: 8  (which is 2 * 2 * 2)
```

---

## 📏 2. Rounding & Precision
*Note: Python has different ways of rounding depending on whether you want to go to the nearest, round up, round down, or just chop off decimals.*

### A. `round(number, decimals)`
*   **Simple Definition:** Rounds a decimal number to the nearest whole number (or to a specific decimal place).
*   **Syntax:** `round(number, number_of_decimals)`
*   **Return Datatype:** `int` (if no decimals specified) or `float`
```python
print(round(5.7))     # Output: 6  (rounds up because .7 is closer to 6)
print(round(5.4))     # Output: 5  (rounds down because .4 is closer to 5)
print(round(5.27, 1)) # Output: 5.3 (rounds to 1 decimal place)
```

### B. `math.ceil(x)`
*   **Simple Definition:** Always rounds a decimal number **UP** to the nearest whole number, no matter how small the decimal is.
*   **Syntax:** `math.ceil(number)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
print(math.ceil(5.1))  # Output: 6  (even though .1 is small, it rounds UP)
```

### C. `math.floor(x)`
*   **Simple Definition:** Always rounds a decimal number **DOWN** to the nearest whole number, ignoring how big the decimal is.
*   **Syntax:** `math.floor(number)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
print(math.floor(5.9))  # Output: 5  (even though .9 is large, it rounds DOWN)
```

### D. `math.trunc(x)`
*   **Simple Definition:** Chops off the decimal part of a number, keeping only the whole number part (rounds towards zero).
*   **Syntax:** `math.trunc(number)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
print(math.trunc(5.99))   # Output: 5
print(math.trunc(-5.99))  # Output: -5
```

### E. `math.fabs(x)`
*   **Simple Definition:** Returns the absolute (positive) value of a number, but always as a float (decimal number).
*   **Syntax:** `math.fabs(number)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.fabs(-10))  # Output: 10.0
```

### F. `math.fsum(iterable)`
*   **Simple Definition:** Adds up all the decimals in a list with absolute precision, avoiding tiny rounding errors standard sum can have.
*   **Syntax:** `math.fsum(list_of_decimals)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
floats = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(floats))        # Output: 0.9999999999999999 (imprecise)
print(math.fsum(floats))   # Output: 1.0 (precise)
```

---

## ⚡ 3. Powers, Roots & Common Calculations
*Note: These help you do math operations like multiplication chains, square roots, and finding common divisors.*

### A. `math.sqrt(x)`
*   **Simple Definition:** Finds the square root of a number (the value that, when multiplied by itself, gives the original number).
*   **Syntax:** `math.sqrt(number)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.sqrt(25))  # Output: 5.0  (because 5.0 * 5.0 is 25)
```

### B. `math.factorial(x)`
*   **Simple Definition:** Multiplies a whole number by every whole number below it down to 1.
*   **Syntax:** `math.factorial(number)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
# 4 factorial is 4 * 3 * 2 * 1
print(math.factorial(4))  # Output: 24
```

### C. `math.gcd(x, y)`
*   **Simple Definition:** Finds the Greatest Common Divisor (the largest number that divides both numbers perfectly without a remainder).
*   **Syntax:** `math.gcd(number1, number2)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
print(math.gcd(12, 18))  # Output: 6  (6 is the largest number that divides both 12 and 18)
```

### D. `math.log(x, base)`
*   **Simple Definition:** Finds how many times you must multiply the `base` to get the number `x`. If you don't provide a base, it uses the natural base $e$.
*   **Syntax:** `math.log(number, base)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.log(100, 10))  # Output: 2.0 (because 10 ** 2 = 100)
```

### E. `math.log2(x)`
*   **Simple Definition:** Finds the base-2 logarithm of a number (how many times you must multiply 2 to get `x`).
*   **Syntax:** `math.log2(number)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.log2(8))  # Output: 3.0 (because 2 ** 3 = 8)
```

### F. `math.exp(x)`
*   **Simple Definition:** Calculates the exponential value of $e$ raised to the power of `x` ($e^x$, where $e$ is approx. 2.718).
*   **Syntax:** `math.exp(number)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.exp(2))  # Output: 7.38905609893065 (e squared)
```

---

## 📐 4. Shapes & Angles (Trigonometry)
*Note: Important when working with circles, triangles, and angles.*

### A. Constants: `math.pi` and `math.e`
*   **Simple Definition:** Mathematical constants. `pi` ($\pi$) is approximately `3.14159` (used for circles), and `e` is approximately `2.71828`.
*   **Syntax:** `math.pi` / `math.e` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
print(math.pi)  # Output: 3.141592653589793
```

### B. Converters: `math.radians(x)` and `math.degrees(x)`
*   **Simple Definition:** Converts angles between **degrees** (0 to 360) and **radians** (which Python's trig functions require).
*   **Syntax:** `math.radians(degrees)` / `math.degrees(radians)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
rad = math.radians(180)
print("180 degrees in radians:", rad)  # Output: 3.141592653589793 (equal to Pi)
```

### C. `math.sin(x)`, `math.cos(x)`, `math.tan(x)`
*   **Simple Definition:** Returns the Sine, Cosine, or Tangent of an angle `x` (angle must be in **radians**).
*   **Syntax:** `math.sin(radians)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
# Sine of 90 degrees (which is Pi/2 radians) is 1
angle = math.radians(90)
print(math.sin(angle))  # Output: 1.0
```

### D. Arc Functions: `math.asin(x)`, `math.acos(x)`, `math.atan(x)`
*   **Simple Definition:** Inverse trigonometry. Calculates the angle (in radians) when you give the sine, cosine, or tangent value.
*   **Syntax:** `math.asin(val)` / `math.acos(val)` / `math.atan(val)` *(Requires: `import math`)*
*   **Return Datatype:** `float` (in radians)
```python
import math
# Finds angle whose sine is 1.0 (should be 90 degrees)
angle_rad = math.asin(1.0)
print(math.degrees(angle_rad))  # Output: 90.0
```

### E. `math.hypot(x, y)`
*   **Simple Definition:** Calculates the hypotenuse (the longest side) of a right-angled triangle if you know the other two sides.
*   **Syntax:** `math.hypot(side_a, side_b)` *(Requires: `import math`)*
*   **Return Datatype:** `float`
```python
import math
# A triangle with sides 3 and 4 has a hypotenuse of 5
print(math.hypot(3, 4))  # Output: 5.0
```

---

## 🧠 5. Precision & Smart Checks
*Note: Advanced utilities for checking numbers, avoiding decimal rounding errors, and combinatorics.*

### A. Approximate Equality: `math.isclose(a, b)`
*   **Simple Definition:** Safely checks if two decimal numbers are roughly equal. This prevents errors caused by computer floating-point limitations (e.g. `0.1 + 0.2` in computers is slightly `0.300000000004`).
*   **Syntax:** `math.isclose(num1, num2)` *(Requires: `import math`)*
*   **Return Datatype:** `bool`
```python
import math
# Normal comparison fails due to computer rounding logic
print((0.1 + 0.2) == 0.3)      # Output: False
# Safe comparison succeeds
print(math.isclose(0.1 + 0.2, 0.3))  # Output: True
```

### B. Float Value Checks: `math.isnan(x)` and `math.isinf(x)`
*   **Simple Definition:** Checks if a value is "Not a Number" (`NaN`) or if a value represents Infinity.
*   **Syntax:** `math.isnan(number)` / `math.isinf(number)` *(Requires: `import math`)*
*   **Return Datatype:** `bool`
```python
import math
print(math.isinf(float('inf')))  # Output: True
print(math.isnan(float('nan')))  # Output: True
```

### C. Combinations: `math.comb(n, k)` and `math.perm(n, k)`
*   **Simple Definition:**
    *   `comb()`: Calculates the number of ways to pick `k` items from `n` items where the choice order does NOT matter.
    *   `perm()`: Calculates the number of ways to pick `k` items from `n` items where choice order DOES matter.
*   **Syntax:** `math.comb(n, k)` / `math.perm(n, k)` *(Requires: `import math`)*
*   **Return Datatype:** `int`
```python
import math
# If you have 5 colors, how many unique pairs of 2 colors can you make?
print(math.comb(5, 2))  # Output: 10
```
