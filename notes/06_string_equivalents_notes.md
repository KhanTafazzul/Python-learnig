# 🔤 Python vs. JavaScript String Equivalents Notes

This notes document provides a comprehensive lookup of Python string methods and their JavaScript equivalents. Each comparison includes the method definition, return datatype, and code snippets showing execution and output.

---

## 1. Case Conversions

### A. Convert to Lowercase
*   **Python:** `.lower()`
    *   *Definition:* Converts all uppercase characters in a string to lowercase.
    *   *Return Datatype:* `str`
    ```python
    text = "Hello WORLD"
    result = text.lower()
    print(result)
    # Output: hello world
    ```
*   **JavaScript:** `.toLowerCase()`
    *   *Definition:* Returns the calling string value converted to lowercase.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "Hello WORLD";
    let result = text.toLowerCase();
    console.log(result);
    // Output: hello world
    ```

---

### B. Convert to Uppercase
*   **Python:** `.upper()`
    *   *Definition:* Converts all lowercase characters in a string to uppercase.
    *   *Return Datatype:* `str`
    ```python
    text = "hello world"
    result = text.upper()
    print(result)
    # Output: HELLO WORLD
    ```
*   **JavaScript:** `.toUpperCase()`
    *   *Definition:* Returns the calling string value converted to uppercase.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "hello world";
    let result = text.toUpperCase();
    console.log(result);
    // Output: HELLO WORLD
    ```

---

### C. Capitalize first letter
*   **Python:** `.capitalize()`
    *   *Definition:* Converts the first character to uppercase and all remaining characters to lowercase.
    *   *Return Datatype:* `str`
    ```python
    text = "hello WORLD"
    result = text.capitalize()
    print(result)
    # Output: Hello world
    ```
*   **JavaScript:** Manual slicing & concatenation
    *   *Definition:* Capitalizes the first index and lowers the rest using slicing.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "hello WORLD";
    let result = text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    console.log(result);
    // Output: Hello world
    ```

---

## 2. Whitespace Trimming

### A. Trim Both Ends
*   **Python:** `.strip()`
    *   *Definition:* Removes all leading and trailing whitespace characters.
    *   *Return Datatype:* `str`
    ```python
    text = "  hello  "
    result = text.strip()
    print(f"'{result}'")
    # Output: 'hello'
    ```
*   **JavaScript:** `.trim()`
    *   *Definition:* Removes whitespace from both ends of the string.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "  hello  ";
    let result = text.trim();
    console.log(`'${result}'`);
    // Output: 'hello'
    ```

---

### B. Trim Left Side Only
*   **Python:** `.lstrip()`
    *   *Definition:* Removes leading whitespace characters (from the left side).
    *   *Return Datatype:* `str`
    ```python
    text = "  hello  "
    result = text.lstrip()
    print(f"'{result}'")
    # Output: 'hello  '
    ```
*   **JavaScript:** `.trimStart()`
    *   *Definition:* Removes whitespace from the beginning of the string.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "  hello  ";
    let result = text.trimStart();
    console.log(`'${result}'`);
    // Output: 'hello  '
    ```

---

### C. Trim Right Side Only
*   **Python:** `.rstrip()`
    *   *Definition:* Removes trailing whitespace characters (from the right side).
    *   *Return Datatype:* `str`
    ```python
    text = "  hello  "
    result = text.rstrip()
    print(f"'{result}'")
    # Output: '  hello'
    ```
*   **JavaScript:** `.trimEnd()`
    *   *Definition:* Removes whitespace from the end of the string.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "  hello  ";
    let result = text.trimEnd();
    console.log(`'${result}'`);
    // Output: '  hello'
    ```

---

## 3. Substrings & Searching

### A. String Length
*   **Python:** `len()`
    *   *Definition:* Returns the total number of characters in the string.
    *   *Return Datatype:* `int`
    ```python
    text = "Python"
    result = len(text)
    print(result)
    # Output: 6
    ```
*   **JavaScript:** `.length` property
    *   *Definition:* Returns the length of the string.
    *   *Return Datatype:* `number`
    ```javascript
    let text = "Python";
    let result = text.length;
    console.log(result);
    // Output: 6
    ```

---

### B. Check Prefix (Starts With)
*   **Python:** `.startswith()`
    *   *Definition:* Returns `True` if the string starts with the specified prefix.
    *   *Return Datatype:* `bool`
    ```python
    text = "JavaScript"
    result = text.startswith("Java")
    print(result)
    # Output: True
    ```
*   **JavaScript:** `.startsWith()`
    *   *Definition:* Returns `true` if the string starts with the specified substring.
    *   *Return Datatype:* `boolean`
    ```javascript
    let text = "JavaScript";
    let result = text.startsWith("Java");
    console.log(result);
    // Output: true
    ```

---

### C. Check Suffix (Ends With)
*   **Python:** `.endswith()`
    *   *Definition:* Returns `True` if the string ends with the specified suffix.
    *   *Return Datatype:* `bool`
    ```python
    text = "programming"
    result = text.endswith("ming")
    print(result)
    # Output: True
    ```
*   **JavaScript:** `.endsWith()`
    *   *Definition:* Returns `true` if the string ends with the specified substring.
    *   *Return Datatype:* `boolean`
    ```javascript
    let text = "programming";
    let result = text.endsWith("ming");
    console.log(result);
    // Output: true
    ```

---

### D. Find Substring Index
*   **Python:** `.find()`
    *   *Definition:* Returns the lowest index where the substring is found, or `-1` if missing.
    *   *Return Datatype:* `int`
    ```python
    text = "hello world"
    result = text.find("world")
    print(result)
    # Output: 6
    ```
*   **JavaScript:** `.indexOf()`
    *   *Definition:* Returns the index of the first occurrence of the substring, or `-1` if missing.
    *   *Return Datatype:* `number`
    ```javascript
    let text = "hello world";
    let result = text.indexOf("world");
    console.log(result);
    // Output: 6
    ```

---

### E. Check Containment (Membership)
*   **Python:** `in` operator
    *   *Definition:* Checks whether a substring is present within another string.
    *   *Return Datatype:* `bool`
    ```python
    text = "learning python is fun"
    result = "python" in text
    print(result)
    # Output: True
    ```
*   **JavaScript:** `.includes()`
    *   *Definition:* Checks whether one string is contained within another.
    *   *Return Datatype:* `boolean`
    ```javascript
    let text = "learning javascript is fun";
    let result = text.includes("javascript");
    console.log(result);
    // Output: true
    ```

---

### F. Extract Substring (Slicing)
*   **Python:** Slice Syntax `[start:end]`
    *   *Definition:* Extracts characters between two indices (end index is exclusive).
    *   *Return Datatype:* `str`
    ```python
    text = "development"
    result = text[0:5]
    print(result)
    # Output: devel
    ```
*   **JavaScript:** `.slice()`
    *   *Definition:* Extracts a section of a string and returns it as a new string.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "development";
    let result = text.slice(0, 5);
    console.log(result);
    // Output: devel
    ```

---

## 4. Splitting, Joining & Replacing

### A. Split String
*   **Python:** `.split()`
    *   *Definition:* Splits a string into a list of strings based on a separator.
    *   *Return Datatype:* `list` of `str`
    ```python
    text = "A-B-C"
    result = text.split("-")
    print(result)
    # Output: ['A', 'B', 'C']
    ```
*   **JavaScript:** `.split()`
    *   *Definition:* Splits a string into an array of strings based on a separator.
    *   *Return Datatype:* `Array` of `string`
    ```javascript
    let text = "A-B-C";
    let result = text.split("-");
    console.log(result);
    // Output: [ 'A', 'B', 'C' ]
    ```

---

### B. Join List/Array into String
*   **Python:** `.join()`
    *   *Definition:* Joins items in an iterable (e.g. list) into a single string with the separator.
    *   *Return Datatype:* `str`
    ```python
    items = ["A", "B", "C"]
    result = "-".join(items)
    print(result)
    # Output: A-B-C
    ```
*   **JavaScript:** `.join()`
    *   *Definition:* Joins elements of an array into a single string with the separator.
    *   *Return Datatype:* `string`
    ```javascript
    let items = ["A", "B", "C"];
    let result = items.join("-");
    console.log(result);
    // Output: A-B-C
    ```

---

### C. Replace Substrings
*   **Python:** `.replace()`
    *   *Definition:* Replaces all occurrences of a specified substring with a new substring.
    *   *Return Datatype:* `str`
    ```python
    text = "banana"
    result = text.replace("a", "o")
    print(result)
    # Output: bonono
    ```
*   **JavaScript:** `.replaceAll()`
    *   *Definition:* Replaces all occurrences of a specified substring with a new substring.
    *   *Return Datatype:* `string`
    ```javascript
    let text = "banana";
    let result = text.replaceAll("a", "o");
    console.log(result);
    // Output: bonono
    ```

---

## 5. String Validation

### A. Check if Digits Only
*   **Python:** `.isdigit()`
    *   *Definition:* Returns `True` if all characters in the string are digits.
    *   *Return Datatype:* `bool`
    ```python
    num = "42"
    result = num.isdigit()
    print(result)
    # Output: True
    ```
*   **JavaScript:** Regex validation `/^\d+$/`
    *   *Definition:* Validates that the entire string matches digit characters.
    *   *Return Datatype:* `boolean`
    ```javascript
    let num = "42";
    let result = /^\d+$/.test(num);
    console.log(result);
    // Output: true
    ```
