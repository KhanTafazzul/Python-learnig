# 🐍 Python String Methods Reference Notes

This notes document provides a comprehensive lookup of Python's built-in string methods. Each method includes its description, return datatype, and code snippets showing execution and output.

---

## 1. Case Conversions

### A. `.lower()`
*   **Description:** Converts all uppercase characters in the string to lowercase.
*   **Return Datatype:** `str`
```python
text = "Hello WORLD"
result = text.lower()
print(result)
# Output: hello world
```

### B. `.upper()`
*   **Description:** Converts all lowercase characters in the string to uppercase.
*   **Return Datatype:** `str`
```python
text = "hello world"
result = text.upper()
print(result)
# Output: HELLO WORLD
```

### C. `.capitalize()`
*   **Description:** Converts the first character of the string to uppercase and the rest to lowercase.
*   **Return Datatype:** `str`
```python
text = "hello WORLD"
result = text.capitalize()
print(result)
# Output: Hello world
```

### D. `.title()`
*   **Description:** Converts the first character of each word to uppercase and the remaining characters to lowercase.
*   **Return Datatype:** `str`
```python
text = "learning python is fun"
result = text.title()
print(result)
# Output: Learning Python Is Fun
```

---

## 2. Whitespace Trimming

### A. `.strip()`
*   **Description:** Removes all leading and trailing whitespace characters (spaces, tabs, newlines).
*   **Return Datatype:** `str`
```python
text = "  hello  "
result = text.strip()
print(f"'{result}'")
# Output: 'hello'
```

### B. `.lstrip()`
*   **Description:** Removes leading whitespace characters (from the left side).
*   **Return Datatype:** `str`
```python
text = "  hello  "
result = text.lstrip()
print(f"'{result}'")
# Output: 'hello  '
```

### C. `.rstrip()`
*   **Description:** Removes trailing whitespace characters (from the right side).
*   **Return Datatype:** `str`
```python
text = "  hello  "
result = text.rstrip()
print(f"'{result}'")
# Output: '  hello'
```

---

## 3. Substrings & Searching

### A. `.startswith()`
*   **Description:** Returns `True` if the string starts with the specified prefix; otherwise, `False`.
*   **Return Datatype:** `bool`
```python
text = "Python Programming"
result = text.startswith("Py")
print(result)
# Output: True
```

### B. `.endswith()`
*   **Description:** Returns `True` if the string ends with the specified suffix; otherwise, `False`.
*   **Return Datatype:** `bool`
```python
text = "programming.py"
result = text.endswith(".py")
print(result)
# Output: True
```

### C. `.find()`
*   **Description:** Searches the string for a specified value and returns the lowest index where it is found. Returns `-1` if not found.
*   **Return Datatype:** `int`
```python
text = "hello world"
result = text.find("world")
print(result)
# Output: 6
```

### D. `.index()`
*   **Description:** Searches the string for a specified value and returns the lowest index where it is found. Raises a `ValueError` if the value is not found.
*   **Return Datatype:** `int`
```python
text = "hello world"
try:
    result = text.index("python")
except ValueError:
    result = "Not Found (ValueError raised)"
print(result)
# Output: Not Found (ValueError raised)
```

### E. `.count()`
*   **Description:** Returns the number of times a specified value occurs in the string.
*   **Return Datatype:** `int`
```python
text = "banana"
result = text.count("a")
print(result)
# Output: 3
```

---

## 4. Splitting, Joining & Replacing

### A. `.split()`
*   **Description:** Splits the string at the specified separator and returns a list of substrings. Defaults to whitespace.
*   **Return Datatype:** `list` of `str`
```python
text = "apple,banana,cherry"
result = text.split(",")
print(result)
# Output: ['apple', 'banana', 'cherry']
```

### B. `.join()`
*   **Description:** Joins elements of an iterable (like list or tuple) using the string as the separator.
*   **Return Datatype:** `str`
```python
items = ["apple", "banana", "cherry"]
result = "-".join(items)
print(result)
# Output: apple-banana-cherry
```

### C. `.replace()`
*   **Description:** Returns a copy of the string where all occurrences of a substring are replaced with another.
*   **Return Datatype:** `str`
```python
text = "banana"
result = text.replace("a", "o")
print(result)
# Output: bonono
```

---

## 5. String Validation

### A. `.isdigit()`
*   **Description:** Returns `True` if all characters in the string are digits.
*   **Return Datatype:** `bool`
```python
num = "12345"
print(num.isdigit())
# Output: True

mixed = "123a5"
print(mixed.isdigit())
# Output: False
```

### B. `.isalpha()`
*   **Description:** Returns `True` if all characters in the string are alphabetic (a-z, A-Z).
*   **Return Datatype:** `bool`
```python
text = "Python"
print(text.isalpha())
# Output: True

mixed = "Python3"
print(mixed.isalpha())
# Output: False
```

### C. `.isalnum()`
*   **Description:** Returns `True` if all characters in the string are alphanumeric (alphabetic or digits).
*   **Return Datatype:** `bool`
```python
text = "Python3"
print(text.isalnum())
# Output: True

spaces = "Python 3"
print(spaces.isalnum())
# Output: False
```

### D. `.islower()`
*   **Description:** Returns `True` if all cased characters in the string are lowercase.
*   **Return Datatype:** `bool`
```python
text = "hello"
print(text.islower())
# Output: True
```

### E. `.isupper()`
*   **Description:** Returns `True` if all cased characters in the string are uppercase.
*   **Return Datatype:** `bool`
```python
text = "HELLO"
print(text.isupper())
# Output: True
```
