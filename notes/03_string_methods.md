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

> [!WARNING]
> **Do not pass multiple single separators as a single string!**
> If you write `text.split(",.!?")`, Python looks for the **exact sequence** `",.!?"` as one single separator. It will NOT split on each punctuation mark individually.
> *   **Wrong:** `text.split(",.!?")` ➔ looks for the sequence `",.!?"` all together.
> *   **Correct Way:** Replace each punctuation mark with a space first using a loop, then split:
>     ```python
>     for char in [".", ",", "!", "?"]:
>         text = text.replace(char, " ")
>     result = text.split()  # Splits on spaces automatically
>     ```
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

---

## 6. Python Tokenization (StringTokenizer Equivalents)
These techniques show how to split strings into tokens in Python, organized by built-in core methods and advanced utilities.

### 6.1 Built-in Core Functions (Actual)
These are native string methods that are built directly into Python and do not require importing any libraries.

#### A. Whitespace Tokenization (Default StringTokenizer)
*   **Description:** Splits a string into individual word tokens using whitespace as the default delimiter.
*   **Syntax:** `text.split()`
*   **Return Datatype:** `list` of `str`
```python
text = "this is a test"
tokens = text.split()
print(tokens)
# Output: ['this', 'is', 'a', 'test']
```

#### B. Custom Delimiter Tokenization
*   **Description:** Splits a string into tokens based on a custom character delimiter (such as a comma).
*   **Syntax:** `text.split(delimiter)`
*   **Return Datatype:** `list` of `str`
```python
text = "apple,banana,cherry"
tokens = text.split(",")
print(tokens)
# Output: ['apple', 'banana', 'cherry']
```

#### C. Right-Side Splitting (rsplit)
*   **Description:** Splits a string into tokens starting from the right side of the string.
*   **Syntax:** `text.rsplit(delimiter, maxsplit)`
*   **Return Datatype:** `list` of `str`
```python
text = "apple,banana,cherry"
# Splits from the right only once
tokens = text.rsplit(",", 1)
print(tokens)
# Output: ['apple,banana', 'cherry']
```

#### D. Line-by-Line Tokenization (splitlines)
*   **Description:** Splits a multi-line string into individual line tokens.
*   **Syntax:** `text.splitlines()`
*   **Return Datatype:** `list` of `str`
```python
text = "line1\nline2\nline3"
print(text.splitlines())
# Output: ['line1', 'line2', 'line3']
```

#### E. First-Match Partitioning
*   **Description:** Splits a string into exactly three parts: before the delimiter, the delimiter itself, and after the delimiter (checks from left).
*   **Syntax:** `text.partition(delimiter)`
*   **Return Datatype:** `tuple` -> `(before, delimiter, after)`
```python
email = "aman@example.com"
print(email.partition("@"))
# Output: ('aman', '@', 'example.com')
```

#### F. Last-Match Partitioning (rpartition)
*   **Description:** Splits a string into exactly three parts based on the last occurrence of the delimiter (checks from right).
*   **Syntax:** `text.rpartition(delimiter)`
*   **Return Datatype:** `tuple` -> `(before, delimiter, after)`
```python
path = "folder/subfolder/file.py"
print(path.rpartition("/"))
# Output: ('folder/subfolder', '/', 'file.py')
```

#### G. Counting Total Tokens (Count Tokens)
*   **Description:** Counts the total number of tokens in a string.
*   **Syntax:** `len(text.split())`
*   **Return Datatype:** `int`
```python
text = "learning python is fun"
token_count = len(text.split())
print(token_count)
# Output: 4
```

#### H. Switching Delimiters Dynamically (Next Token by Delimiter)
*   **Description:** Splits the first part of a string by one delimiter and the rest by another delimiter.
*   **Syntax:** `text.split(delimiter, maxsplit)`
*   **Return Datatype:** `list` of `str`
```python
text = "first second,third"
first_token, remaining = text.split(" ", 1)
print("First:", first_token)  # Output: first
print("Remaining:", remaining.split(","))  # Output: ['second', 'third']
```

---

### 6.2 Other & Intermediate Utilities
These techniques require using external standard modules (like `re`, `shlex`, or `csv`) or combining elements into iterators.

#### A. Step-by-Step Iteration (Next Token / Has More Tokens)
*   **Description:** Mimics iterating through tokens one-by-one by converting the list into an iterator and calling `next()`.
*   **Syntax:** `tokens_iter = iter(text.split())` then `next(tokens_iter)`
*   **Return Datatype:** `iterator` / individual `str` values
```python
text = "one two"
tokens_iter = iter(text.split())
print(next(tokens_iter))  # Output: one
print(next(tokens_iter))  # Output: two
```

#### B. Return Delimiters as Tokens
*   **Description:** Splits a string into tokens but also returns the delimiter characters themselves as tokens.
*   **Syntax:** `re.split(r'(delim)', text)` *(Requires: `import re`)*
*   **Return Datatype:** `list` of `str`
```python
import re
text = "apple,banana"
tokens = re.split(r'(,)', text)
print(tokens)
# Output: ['apple', ',', 'banana']
```

#### C. Multiple Delimiters Tokenization
*   **Description:** Splits text into tokens using multiple different characters as delimiters at the same time.
*   **Syntax:** `re.split(r'[delimiters]+', text)` *(Requires: `import re`)*
*   **Return Datatype:** `list` of `str`
```python
import re
text = "apple, banana; cherry"
tokens = re.split(r'[\s,;]+', text)
print(tokens)
# Output: ['apple', 'banana', 'cherry']
```

#### D. Pattern Extraction Tokenization (findall)
*   **Description:** Extracts tokens that match a specific pattern instead of splitting on delimiters (e.g. extracting all digits).
*   **Syntax:** `re.findall(pattern, text)` *(Requires: `import re`)*
*   **Return Datatype:** `list` of `str`
```python
import re
text = "Aman has 5 apples and 10 bananas."
digits = re.findall(r'\d+', text)
print(digits)
# Output: ['5', '10']
```

#### E. Command-Line Quote Parsing
*   **Description:** Splits a command-line string into tokens, keeping text inside quotes as a single token.
*   **Syntax:** `shlex.split(text)` *(Requires: `import shlex`)*
*   **Return Datatype:** `list` of `str`
```python
import shlex
text = 'hello "world of python"'
print(shlex.split(text))
# Output: ['hello', 'world of python']
```

#### F. Tabular/CSV Tokenization
*   **Description:** Tokenizes standard comma-separated or tab-separated records, handling quotes and fields correctly.
*   **Syntax:** `csv.reader([text])` *(Requires: `import csv`)*
*   **Return Datatype:** `_reader` (iterator of lists of `str`)
```python
import csv
text = 'Aman,20,"Delhi, India"'
reader = csv.reader([text])
for row in reader:
    print(row)
# Output: ['Aman', '20', 'Delhi, India']
```

---

## 7. Advanced String Formatting & Alignment (f-strings)

Python's f-strings (`f"..."`) allow you to format values, align text, and pad spaces inside curly braces `{}` using a colon (`:`) followed by a format specifier:

$$\text{\{variable : [alignment] [width] [.precision] [type]\}}$$

### A. Left Alignment (`<`)
*   **Description:** Align the text or value to the left and fill the remaining width with spaces.
*   **Syntax:** `{variable:<width}`
*   **Code Example:**
    ```python
    category = "Food"
    print(f"|{category:<15}|")
    ```
*   **Output:**
    ```text
    |Food           |
    ```

### B. Right Alignment (`>`)
*   **Description:** Align the text or value to the right and pad spaces on the left side.
*   **Syntax:** `{variable:>width}`
*   **Code Example:**
    ```python
    category = "Food"
    print(f"|{category:>15}|")
    ```
*   **Output:**
    ```text
    |           Food|
    ```

### C. Center Alignment (`^`)
*   **Description:** Align the text or value in the center, padding spaces evenly on both left and right sides.
*   **Syntax:** `{variable:^width}`
*   **Code Example:**
    ```python
    category = "Food"
    print(f"|{category:^15}|")
    ```
*   **Output:**
    ```text
    |     Food      |
    ```

### E. Float Precision (`.Nf`)
*   **Description:** Formats a decimal number (float) to have exactly `N` decimal places.
*   **Syntax:** `{variable:.Nf}`
*   **Code Example:**
    ```python
    amount_val = 25.5
    print(f"Amount: {amount_val:.2f}")
    ```
*   **Output:**
    ```text
    Amount: 25.50
    ```

### F. Combining Alignment, Width, and Precision
*   **Description:** Combine alignment (`<`, `>`, `^`), column width, and float precision together.
*   **Syntax:** `{variable:<width.precisionf}`
*   **Code Example:**
    ```python
    amount_val = 25.5
    # Left-align, reserve 10 characters width, format with 2 decimal places
    print(f"|{amount_val:<10.2f}|")
    ```
*   **Output:**
    ```text
    |25.50     |
    ```

### G. Building Tabular Output (Complete Example)
*   **Description:** Putting all formatting components together to create clean, aligned vertical tables (ideal for terminal logs and expense trackers).
*   **Code Example:**
    ```python
    date = "2026-08-31"
    category = "Entertainment"
    amount_val = 1200.0
    description = "Movie tickets"

    # Print formatted headers
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description':<20}")
    print("-" * 67)
    
    # Print formatted data row
    print(f"{date:<12} | {category:<15} | {amount_val:<10.2f} | {description:<20}")
    ```
*   **Output:**
    ```text
    Date         | Category        | Amount     | Description         
    -------------------------------------------------------------------
    2026-08-31   | Entertainment   | 1200.00    | Movie tickets       
    ```

