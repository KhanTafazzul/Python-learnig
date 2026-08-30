# 🔢 Python Operators Reference Notes

This notes document provides a comprehensive lookup of all operators in Python. Each category covers the syntax, usage explanation, and sample code with output.

---

## 1. Arithmetic Operators
Used with numeric values to perform common mathematical operations.

| Operator | Name | Syntax | Usage |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `x + y` | Adds two values together. |
| `-` | Subtraction | `x - y` | Subtracts the right value from the left value. |
| `*` | Multiplication | `x * y` | Multiplies two values. |
| `/` | Division | `x / y` | Divides the left value by the right value (always returns a float). |
| `%` | Modulus | `x % y` | Returns the division remainder. |
| `**` | Exponentiation | `x ** y` | Raises the left value to the power of the right value. |
| `//` | Floor Division | `x // y` | Divides and rounds down to the nearest whole number. |

### Sample Code:
```python
x = 15
y = 4

print("Addition:", x + y)         # Output: 19
print("Subtraction:", x - y)      # Output: 11
print("Multiplication:", x * y)   # Output: 60
print("Division:", x / y)         # Output: 3.75
print("Modulus:", x % y)          # Output: 3
print("Exponentiation:", x ** y)  # Output: 50625
print("Floor Division:", x // y)  # Output: 3
```

---

## 2. Comparison (Relational) Operators
Used to compare two values. They return a Boolean value (`True` or `False`).

| Operator | Name | Syntax | Usage |
| :--- | :--- | :--- | :--- |
| `==` | Equal | `x == y` | Returns `True` if the values are equal. |
| `!=` | Not Equal | `x != y` | Returns `True` if the values are not equal. |
| `>` | Greater Than | `x > y` | Returns `True` if left is greater than right. |
| `<` | Less Than | `x < y` | Returns `True` if left is less than right. |
| `>=` | Greater Than or Equal To | `x >= y` | Returns `True` if left is greater than or equal to right. |
| `<=` | Less Than or Equal To | `x <= y` | Returns `True` if left is less than or equal to right. |

### Sample Code:
```python
a = 10
b = 20

print("Equal:", a == b)                    # Output: False
print("Not Equal:", a != b)                # Output: True
print("Greater Than:", a > b)              # Output: False
print("Less Than:", a < b)                 # Output: True
print("Greater Than or Equal:", a >= 10)   # Output: True
print("Less Than or Equal:", b <= 15)      # Output: False
```

---

## 3. Logical Operators
Used to combine conditional statements.

| Operator | Description | Syntax | Usage |
| :--- | :--- | :--- | :--- |
| `and` | Logical AND | `x and y` | Returns `True` if both statements are true. |
| `or` | Logical OR | `x or y` | Returns `True` if at least one of the statements is true. |
| `not` | Logical NOT | `not x` | Reverses the logical state (turns `True` to `False` and vice versa). |

### Sample Code:
```python
x = True
y = False

print("AND result:", x and y)  # Output: False
print("OR result:", x or y)   # Output: True
print("NOT result:", not x)   # Output: False

# Numerical logic check
age = 22
has_license = True
print("Can drive:", age >= 18 and has_license)  # Output: True
```

---

## 4. Assignment Operators
Used to assign values to variables. Many combine arithmetic operations with assignment.

| Operator | Syntax | Equivalent To | Usage |
| :--- | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Assigns right side to left side. |
| `+=` | `x += 3` | `x = x + 3` | Adds and assigns. |
| `-=` | `x -= 3` | `x = x - 3` | Subtracts and assigns. |
| `*=` | `x *= 3` | `x = x * 3` | Multiplies and assigns. |
| `/=` | `x /= 3` | `x = x / 3` | Divides and assigns. |
| `%=` | `x %= 3` | `x = x % 3` | Modulus and assigns. |
| `**=` | `x **= 3` | `x = x ** 3` | Exponent and assigns. |
| `//=` | `x //= 3` | `x = x // 3` | Floor divide and assigns. |

### Sample Code:
```python
x = 10
print("Initial:", x)  # Output: 10

x += 5
print("After +=:", x)  # Output: 15

x *= 2
print("After *=:", x)  # Output: 30

x //= 4
print("After //=:", x) # Output: 7
```

---

## 5. Bitwise Operators
Used to perform bitwise operations on integer binary values.

| Operator | Name | Syntax | Usage |
| :--- | :--- | :--- | :--- |
| `&` | Bitwise AND | `x & y` | Sets each bit to 1 if both bits are 1. |
| `\|` | Bitwise OR | `x \| y` | Sets each bit to 1 if one of two bits is 1. |
| `^` | Bitwise XOR | `x ^ y` | Sets each bit to 1 if only one of two bits is 1. |
| `~` | Bitwise NOT | `~x` | Inverts all the bits (flips 0 to 1 and 1 to 0). |
| `<<` | Zero fill left shift | `x << y` | Shift left by pushing zeros in from the right. |
| `>>` | Signed right shift | `x >> y` | Shift right by pushing copies of the leftmost bit in. |

### Sample Code:
```python
# Binary representation:
# 5 is 0101
# 3 is 0011

x = 5
y = 3

print("Bitwise AND (5 & 3):", x & y)   # Output: 1 (binary: 0001)
print("Bitwise OR (5 | 3):", x | y)    # Output: 7 (binary: 0111)
print("Bitwise XOR (5 ^ 3):", x ^ y)   # Output: 6 (binary: 0110)
print("Bitwise NOT (~5):", ~x)         # Output: -6
print("Left Shift (5 << 1):", x << 1)  # Output: 10 (binary: 1010)
print("Right Shift (5 >> 1):", x >> 1) # Output: 2 (binary: 0010)
```

---

## 6. Membership Operators
Used to test if a sequence (such as a list, string, tuple, or dictionary) is present in an object.

| Operator | Syntax | Usage |
| :--- | :--- | :--- |
| `in` | `x in y` | Returns `True` if a sequence with the specified value is present in the object. |
| `not in` | `x not in y` | Returns `True` if a sequence with the specified value is not present in the object. |

### Sample Code:
```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # Output: True
print("orange" not in fruits)  # Output: True
print("cherry" not in fruits)  # Output: False
```

---

## 7. Identity Operators
Used to compare the memory locations of two objects, checking if they are actually the same object instance.

| Operator | Syntax | Usage |
| :--- | :--- | :--- |
| `is` | `x is y` | Returns `True` if both variables point to the same object in memory. |
| `is not` | `x is not y` | Returns `True` if variables do not point to the same object. |

### Sample Code:
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Content comparison using ==
print("list1 == list2:", list1 == list2)  # Output: True (same content)

# Identity comparison using is
print("list1 is list2:", list1 is list2)  # Output: False (different memory objects)
print("list1 is list3:", list1 is list3)  # Output: True (points to the exact same object)
print("list1 is not list2:", list1 is not list2) # Output: True
```
