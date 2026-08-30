# Full Python + Web Development Course Notes

This file contains detailed notes from the start of the course up to Flask and capstone level. It includes definitions, syntax, explanation of common functions, and what each topic does.

---

## 📚 Quick Notes of Core Learning Modules
Here is a quick summary of the core Python learning modules in the course. For complete definitions, syntaxes, and examples, refer to their dedicated files:

### 1. 🔢 [01: Operators](file:///d:/Aman/pythonbasics/notes/01_operators.md)
*   **What it does:** Performs calculations, checks conditions, and modifies variables.
*   **Summary:** Covers Arithmetic (`+`, `-`, `*`, `/`, `%`, `**`, `//`), Comparison (`==`, `!=`, `>`, `<`), Logical (`and`, `or`, `not`), Assignment (`+=`, `-=`), Membership (`in`), and Identity (`is`).
*   **Quick Syntax:**
    ```python
    x = 10
    x += 5
    is_valid = x > 12 and x is not None
    ```

### 2. 🔁 [02: Loops & Control Flow](file:///d:/Aman/pythonbasics/notes/02_loops_control_flow.md)
*   **What it does:** Decision making and repeating code execution blocks.
*   **Summary:** Covers conditional tests (`if/elif/else`), running fixed-count iterations (`for` loops), running condition-based loops (`while`), and changing loop behaviors (`break` and `continue`).
*   **Quick Syntax:**
    ```python
    for i in range(5):
        if i == 3:
            break
        print(i)
    ```

### 3. 🔤 [03: String Methods](file:///d:/Aman/pythonbasics/notes/03_string_methods.md)
*   **What it does:** Processes, formats, and transforms string text.
*   **Summary:** Covers lowercase (`.lower()`), uppercase (`.upper()`), capitalizations (`.title()`, `.capitalize()`), trimming whitespace (`.strip()`), searching (`.startswith()`, `.find()`), and splitting/joining (`.split()`, `.join()`).
*   **Quick Syntax:**
    ```python
    text = "  python programming  "
    clean_text = text.strip().title()  # Output: "Python Programming"
    ```

### 4. 🛠️ [04: Custom Functions & Scope](file:///d:/Aman/pythonbasics/notes/04_custom_functions.md)
*   **What it does:** Creates reusable code blocks with custom parameters, arguments, dynamic inputs (`*args`/`**kwargs`), and handles variable scope.
*   **Summary:** Covers function definitions (`def`), inputs (positional/keyword args, defaults), return statements, variable scope (local vs global, and the `global` keyword).
*   **Quick Syntax:**
    ```python
    def calc_square(x=2):
        return x * x
    print(calc_square(5))  # Output: 25
    ```

### 5. 🧮 [05: Math Functions](file:///d:/Aman/pythonbasics/notes/05_math_functions.md)
*   **What it does:** Provides built-in and external mathematical methods.
*   **Summary:** Covers built-in arithmetic (`abs()`, `sum()`, `min()`, `max()`, `divmod()`, `round()`), power/roots (`math.sqrt()`, `pow()`), rounding limits (`math.ceil()`, `math.floor()`, `math.trunc()`), geometry/trigonometry, precision comparisons (`math.isclose()`), and combinations (`math.comb()`).
*   **Quick Syntax:**
    ```python
    import math
    print(math.sqrt(25))                 # Output: 5.0
    print(math.isclose(0.1 + 0.2, 0.3))  # Output: True
    ```

### 6. 📦 [06: Data Structures](file:///d:/Aman/pythonbasics/notes/06_data_structures.md)
*   **What it does:** Stores, groups, and maps multiple items.
*   **Summary:** Covers ordered/mutable Lists (`[]`), ordered/immutable Tuples (`()`), key-value Dictionaries (`{}`), and unique-value Sets (`{}`).
*   **Quick Syntax:**
    ```python
    student = {"name": "Aman", "grades": [90, 85]}
    unique_numbers = {1, 2, 2, 3}  # Output set: {1, 2, 3}
    ```

### 7. 📁 [07: File Handling](file:///d:/Aman/pythonbasics/notes/07_file_handling.md)
*   **What it does:** Reads data from or writes data permanently to storage files.
*   **Summary:** Covers open modes (Write `'w'`, Read `'r'`, Append `'a'`), line-by-line reading, and using `with open(...) as file:` to guarantee automatic closing of resources.
*   **Quick Syntax:**
    ```python
    with open("contacts.txt", "a") as file:
        file.write("Aman,12345,aman@test.com\n")
    ```

### 8. 🛡️ [08: Exception Handling](file:///d:/Aman/pythonbasics/notes/08_exception_handling.md)
*   **What it does:** Safely catches runtime errors so programs run continuously without crash.
*   **Summary:** Covers `try` (run risky code), `except` (catch specific errors), `else` (run if no error occurred), and `finally` (always execute at the end).
*   **Quick Syntax:**
    ```python
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Error: Invalid numeric input.")
    ```

### 9. 🛠️ [09: Modules & Environments](file:///d:/Aman/pythonbasics/notes/09_modules_environments.md)
*   **What it does:** Code partitioning (import/export), setting up isolated folders, and package installations.
*   **Summary:** Covers modular imports (`import math`), creating isolated virtual environments (`venv`), installing third-party packages (`pip install`), and exporting package listings (`pip freeze > requirements.txt`).
*   **Quick Syntax:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install colorama
    ```

### 10. 🧪 [10: Standard Libraries](file:///d:/Aman/pythonbasics/notes/10_standard_libraries.md)
*   **What it does:** Provides detailed reference guides for standard modules (`random` and `datetime`).
*   **Summary:** Generating random numbers/items, formatting dates and times, and time calculations.
*   **Quick Syntax:**
    ```python
    import random
    from datetime import datetime
    print(random.randint(1, 10))
    print(datetime.now().strftime("%Y-%m-%d"))
    ```

---

# 1. Python Fundamentals & Primitives

## 1.1 print()
### Definition
`print()` is used to display output on the screen.
### Syntax
```python
print("Hello")
print(10)
print(a)
```
### Explanation
It shows text, numbers, or the value of a variable.
### Example
```python
name = "Aman"
print("My name is", name)
```

## 1.2 Variables
### Definition
Variables are used to store data in memory.
### Syntax
```python
name = "Aman"
age = 20
is_student = True
```
### Explanation
A variable holds a value that can be used later.
### Example
```python
x = 5
y = x + 3
print(y)
```

## 1.3 Input
### Definition
`input()` is used to take input from the user.
### Syntax
```python
name = input("Enter your name: ")
```
### Explanation
It waits for user input and stores the typed value as a string.
### Example
```python
age = input("Enter your age: ")
print("Your age is", age)
```

## 1.4 Numbers
### Definition
Numbers are used for calculations.
### Types
```python
age = 20          # int
price = 12.5      # float
```
### Explanation
Python supports integers and floating-point numbers.
### Example
```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

## 1.5 Functions
### Definition
Functions are reusable blocks of code.
### Syntax
```python
def greet(name):
    print("Hello", name)
```
### Explanation
Functions help organize code and avoid repetition.
### Example
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```
### Common built-in functions
- `print()`
- `input()`
- `len()`
- `type()`
- `sum()`
- `max()`
- `min()`

---

# 2. Step 1: Operators
### Definition
Operators perform operations on values.
### Types
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`
### Example
```python
x = 5
print(x > 3)
print(x == 5 and x < 10)
```

---

# 3. Step 2: Loops & Control Flow

## 3.1 if / elif / else
### Definition
These are used for decision-making.
### Syntax
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```
### Explanation
The program checks conditions in order and runs the matching block.
### Example
```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## 3.2 Loops
### For loop
```python
for i in range(5):
    print(i)
```
### While loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
### Explanation
Loops repeat code multiple times.

---

# 4. Step 3: Strings & String Methods

## 4.1 Strings Basics
### Definition
A string is text enclosed in quotes.
### Syntax
```python
text = "Hello"
text2 = 'Python'
```
### Explanation
Strings store characters and can be manipulated using methods.

## 4.2 String Methods
### Common methods
```python
text = "python"
text.upper()
text.lower()
text.capitalize()
text.split()
text.strip()
```
### Explanation
These methods help process and transform text.
### Examples
```python
len("Hello")         # returns length
"Hello".upper()     # converts to uppercase
"Hello".lower()     # converts to lowercase
"Hello".replace("H", "J")
```

---

# 5. Step 4: Custom Functions & Variable Scope

## 5.1 Defining Custom Functions (`def`)
### Definition
Creates a reusable block of code that runs only when called.
### Syntax
```python
def function_name(param1, param2=default_val):
    # code block
    return result
```
### Explanation
Functions group code, accept inputs (arguments), and return outputs.

## 5.2 Variable Scope (Local vs. Global)
### Definition
Variables created inside a function are **local** to that function. Variables in the main body are **global**. To edit a global variable inside a function, use the `global` keyword.
### Syntax
```python
global_var = 100

def edit_var():
    global global_var
    global_var += 50
```
### Explanation
Helps manage variable access and prevent accidental data overwrites.

---

# 6. Step 5: Math Functions
*(Included in general Functions & Modules. Reference: [05_math_functions.md](file:///d:/Aman/pythonbasics/notes/05_math_functions.md) for full guide).*

---

# 7. Step 6: Data Structures

## 7.1 Lists
### Definition
A list stores multiple items in one variable.
### Syntax
```python
fruits = ["apple", "banana", "mango"]
```
### Common methods
```python
fruits.append("orange")
fruits.remove("banana")
fruits.sort()
len(fruits)
```
### Explanation
Lists are ordered and mutable.

## 7.2 Tuples
### Definition
A tuple is similar to a list but cannot be changed.
### Syntax
```python
point = (10, 20)
```
### Explanation
Tuples are immutable and useful for fixed data.

## 7.3 Dictionaries
### Definition
A dictionary stores data as key-value pairs.
### Syntax
```python
student = {"name": "Aman", "age": 20}
```
### Common methods
```python
student["name"]
student.get("age")
student.keys()
student.values()
```
### Explanation
Dictionaries are useful for organizing related data.

## 7.4 Sets
### Definition
A set stores unique values.
### Syntax
```python
numbers = {1, 2, 2, 3}
```
### Explanation
Sets remove duplicates automatically.

---

# 8. Step 7: File Handling
### Definition
Used to read or write files.
### Syntax
```python
with open("file.txt", "w") as f:
    f.write("Hello")
```
### Reading file
```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```
### Explanation
Files store data permanently on disk.

---

# 9. Step 8: Exception Handling (Exceptions)
### Definition
Exceptions are errors that happen during program execution.
### Syntax
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
```
### Explanation
`try` and `except` help handle errors gracefully.

---

# 10. Step 9: Libraries, Modules & Environments

## 10.1 Modules
### Definition
Modules are Python files containing useful code.
### Syntax
```python
import math
print(math.sqrt(16))
```
### Explanation
Modules help reuse code and add features.

## 10.2 Virtual Environments
### Definition
A virtual environment keeps project packages separate.
### Syntax
```bash
python -m venv venv
```
### Explanation
It prevents conflicts between different projects.

---

# 3. Problem Solving in Python

## 3.1 Breaking a problem into steps

### Explanation
Good programming starts by understanding the problem and dividing it into small steps.

### Example
For a calculator:
1. Take input
2. Choose operation
3. Perform calculation
4. Print result

---

# 4. HTML and CSS

## 4.1 HTML

### Definition
HTML is used to create the structure of a webpage.

### Basic syntax
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Hello</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

### Common tags
- `<h1>` to `<h6>`: headings
- `<p>`: paragraph
- `<a>`: link
- `<img>`: image
- `<form>`: form
- `<table>`: table
- `<div>`: container

### Explanation
HTML defines what content appears on the page.

---

## 4.2 CSS

### Definition
CSS is used to style a webpage.

### Syntax
```css
body {
    background-color: lightblue;
    font-family: Arial;
}
```

### Explanation
CSS controls color, layout, spacing, and design.

### Common properties
- `color`
- `background-color`
- `font-size`
- `margin`
- `padding`
- `border`

---

## 4.3 Box Model

### Definition
Every HTML element is a box with content, padding, border, and margin.

### Explanation
This helps control spacing and layout.

---

## 4.4 Flexbox

### Definition
Flexbox is a layout system for arranging items in rows or columns.

### Syntax
```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

### Explanation
It makes alignment and spacing easier.

---

## 4.5 Grid

### Definition
Grid is used for 2D layouts.

### Explanation
It allows you to place items in rows and columns.

---

## 4.6 Responsive Design

### Definition
Responsive design makes websites work on mobile, tablet, and desktop.

### Explanation
It uses media queries and flexible layouts.

---

# 5. JavaScript

## 5.1 Variables in JavaScript

### Syntax
```javascript
let name = "Aman";
const age = 20;
var city = "Delhi";
```

### Explanation
Used to store data in the browser.

---

## 5.2 Functions in JavaScript

### Syntax
```javascript
function greet(name) {
    return "Hello " + name;
}
```

### Explanation
Functions group reusable code.

---

## 5.3 Arrays

### Syntax
```javascript
let numbers = [1, 2, 3, 4];
```

### Explanation
Arrays store multiple values.

---

## 5.4 Objects

### Syntax
```javascript
let student = { name: "Aman", age: 20 };
```

### Explanation
Objects store data as key-value pairs.

---

## 5.5 DOM Manipulation

### Definition
DOM means Document Object Model. It lets JavaScript change HTML content.

### Syntax
```javascript
document.getElementById("demo").innerText = "Hello";
```

### Explanation
This updates the webpage dynamically.

---

## 5.6 Events

### Definition
Events happen when users interact with the page.

### Example
```javascript
document.getElementById("btn").onclick = function() {
    alert("Clicked");
};
```

### Explanation
Events make webpages interactive.

---

## 5.7 Form Validation

### Definition
Checks user input before submitting a form.

### Explanation
It improves user experience and security.

---

## 5.8 Local Storage

### Definition
Stores data in the browser.

### Syntax
```javascript
localStorage.setItem("name", "Aman");
let name = localStorage.getItem("name");
```

### Explanation
Useful for saving small amounts of data.

---

## 5.9 fetch()

### Definition
`fetch()` is used to request data from an API.

### Syntax
```javascript
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data));
```

### Explanation
It helps connect frontend with backend services.

---

# 6. Flask

## 6.1 What is Flask?

### Definition
Flask is a Python framework used to build web applications.

### Explanation
It helps create routes, handle requests, and return web pages.

---

## 6.2 Installing Flask

### Syntax
```bash
pip install flask
```

### Explanation
Installs the Flask package.

---

## 6.3 Creating a basic Flask app

### Syntax
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()
```

### Explanation
- `Flask(__name__)` creates an app object.
- `@app.route('/')` defines a URL route.
- `home()` runs when the route is visited.
- `app.run()` starts the server.

---

## 6.4 Routes

### Definition
Routes define the URL paths of your website.

### Syntax
```python
@app.route('/about')
def about():
    return "About page"
```

### Explanation
When the browser opens `/about`, the function runs.

---

## 6.5 Return HTML

### Syntax
```python
@app.route('/')
def home():
    return "<h1>Welcome</h1>"
```

### Explanation
You can return plain HTML as a string.

---

## 6.6 Templates (Jinja)

### Definition
Templates are HTML files that can display dynamic data.

### Syntax
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', name=name)
```

### Explanation
Templates separate Python logic from HTML design.

---

## 6.7 Forms

### Definition
Forms let users send data to the server.

### Syntax
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello {name}"
```

### Explanation
The server receives form data using `request`.

---

## 6.8 Static Files

### Definition
Static files are CSS, JavaScript, and images.

### Explanation
Flask serves files from a `static` folder.

---

## 6.9 SQLite Database

### Definition
SQLite is a lightweight database used in small Flask apps.

### Explanation
It stores app data such as notes, users, or tasks.

---

## 6.10 CRUD

### Definition
CRUD stands for Create, Read, Update, Delete.

### Explanation
These are the main actions in most web apps.

### Example actions
- Create new record
- Read existing record
- Update record
- Delete record

---

## 6.11 Environment Variables

### Definition
Environment variables store secret values safely.

### Syntax
```python
import os
secret = os.environ.get("SECRET_KEY")
```

### Explanation
Used for keys, passwords, or sensitive information.

---

# 7. Capstone

## 7.1 What is a capstone?

### Definition
A capstone is a final project that shows all your learning.

### Explanation
It should include:
- Python backend logic
- HTML/CSS frontend
- JavaScript interactions
- Flask routes
- Database storage

---

## 7.2 Good capstone ideas

- Study planner
- Expense tracker
- Student notes app
- Task manager
- College event manager

---

## 7.3 Important capstone features

- Clean design
- CRUD operations
- Readable code
- Good documentation
- Safe handling of secrets

---

# 8. Summary

This course gradually teaches you:
1. Python basics
2. Python core concepts
3. HTML and CSS for layout and design
4. JavaScript for interactivity
5. Flask for backend web development
6. Capstone project for portfolio building

---

# 9. Study Tips

- Practice every day
- Write code yourself
- Build small projects
- Review old topics regularly
- Keep notes of syntax and common errors
