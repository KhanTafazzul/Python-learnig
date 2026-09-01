# 📂 Python Core: File Handling

File handling allows you to store data permanently on a disk. Unlike variables which disappear when a program terminates, files persist across sessions.

---

## 1. Opening a File & The Context Manager (`with`)
Always use the Context Manager (`with` statement) to open files in Python.

### Syntax
```python
# Best Practice:
with open("filename.txt", "mode") as file:
    # Perform read/write actions
# File is automatically closed here!
```
* **Why use `with`?** It automatically closes the file safely even if your code crashes, preventing data loss, lockouts, or memory leaks.

---

## 2. File Modes
The mode specifies what you want to do with the file:

| Mode | Name | Description |
| :--- | :--- | :--- |
| **`'r'`** | Read Mode | Opens file for reading. Crashes (`FileNotFoundError`) if file doesn't exist. |
| **`'w'`** | Write Mode | Opens file for writing. Overwrites existing content. Creates file if missing. |
| **`'a'`** | Append Mode | Opens file for adding text at the end. Preserves old content. Creates file if missing. |

---

## 3. Writing Methods

### A. `file.write(string)`
Writes a single string to the file. It does not add newlines automatically, so you must include `\n`.
```python
with open("sample.txt", "w") as file:
    file.write("First line.\n")
```

### B. `file.writelines(list_of_strings)`
Writes a list of strings to the file.
```python
with open("sample.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n"])
```

---

## 4. Reading Methods

### A. `file.read()`
Reads the ENTIRE file into a single string. (Avoid on large files to save memory).
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

### B. `file.readline()`
Reads just one line at a time.
```python
with open("sample.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
```

### C. `file.readlines()`
Reads all lines into a **list of strings** (each item contains its trailing `\n`).
```python
with open("sample.txt", "r") as file:
    lines = file.readlines()  # e.g., ['Line 1\n', 'Line 2\n']
```

### D. Iterating Line-by-Line (Best Practice)
Iterates through the file efficiently. Always use `.strip()` to clean the newline characters.
```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes "\n"
```

---

## 🛠️ System Helpers (The `os` Module)
Use Python's built-in `os` module to safely manage directories and check files.

```python
import os

# 1. Check if file exists before reading (prevents crash)
if os.path.exists("sample.txt"):
    with open("sample.txt", "r") as file:
        print(file.read())
else:
    print("Warning: File does not exist!")

# 2. Create folders safely
os.makedirs("my_folder", exist_ok=True)  # exist_ok=True prevents crash if folder exists
```

---

## 💡 Key Tips & Revision Concepts

### A. Tracking Line Numbers with `enumerate(file, start)`
*   **Description:** Iterates line-by-line while keeping a counter of the current line number.
*   **Syntax:** `enumerate(file_iterator, start_value)`
```python
with open("sample.txt", "r") as file:
    # Starts counting from 1 instead of default 0
    for line_no, line in enumerate(file, 1):
        print(f"Line {line_no}: {line.strip()}")
```

### B. List Appending vs Index Assignment
*   **Description:** When reading file contents into lists dynamically, use `.append()` instead of index assignments like `lst[i]`.
*   **Why?** An empty list `lst = []` has length 0. Attempting to assign to a non-existent index (e.g. `lst[0] = "goal"`) raises an `IndexError`. `.append()` dynamically grows the list as data is read.

### C. Direct Execution Gate: `if __name__ == "__main__":`
*   **Description:** Standard Python pattern that checks if the script is running directly (not imported as a module in another file) before executing main functions.
*   **Syntax:**
```python
def main():
    print("Program started!")

if __name__ == "__main__":
    main()
```
