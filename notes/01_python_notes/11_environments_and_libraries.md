# 🛠️ Python Core: Virtual Environments & Library Management

This notes document covers how to isolate project dependencies using Virtual Environments (`venv`), manage packages using `pip`, and introduces key built-in and external libraries with practical examples.

---

## 1. Virtual Environments (`venv`)

### A. What is a Virtual Environment?
A virtual environment is an isolated directory on your computer containing its own Python executable and package manager. 

### B. Why do we use them?
*   **Prevent Dependency Conflicts:** Project A might need Django 3.0, but Project B needs Django 5.0. A virtual environment allows you to keep both versions separate on the same computer without conflicts.
*   **Clean System:** It avoids installing clutter globally on your system.
*   **Easy Collaboration:** It makes sharing dependency list (via `requirements.txt`) simple so others can run your code instantly.

### C. Commands Lookup (Windows)

| Action | PowerShell Command | CMD Command |
| :--- | :--- | :--- |
| **1. Navigate to Project** | `cd d:\Aman\pythonbasics` | `cd d:\Aman\pythonbasics` |
| **2. Create Environment** | `python -m venv venv` | `python -m venv venv` |
| **3. Activate Environment** | `venv\Scripts\Activate.ps1` | `venv\Scripts\activate.bat` |
| **4. Install Package** | `pip install <package-name>` | `pip install <package-name>` |
| **5. Save Package List** | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| **6. Install from List** | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| **7. Deactivate** | `deactivate` | `deactivate` |

---

## 2. Third-Party Libraries (Downloaded via `pip`)

These are libraries created by other programmers that you can download and use in your projects.

### A. `colorama`
*   **Definition:** A library that makes it easy to print colored text in the terminal window.
*   **Common Use Case:** Creating clean, readable terminal user interfaces (e.g. green for success, red for errors).
*   **Example:**
    ```python
    from colorama import Fore, Back, Style, init
    
    # Initialize colorama
    init(autoreset=True)
    
    print(Fore.GREEN + "✅ Success: Operation completed!")
    print(Fore.RED + Back.WHITE + "❌ Error: Invalid operation!")
    print(Style.BRIGHT + "Bright text")
    ```

### B. `requests`
*   **Definition:** A library used to send HTTP requests to websites or APIs to fetch or send data.
*   **Common Use Case:** Fetching live weather data, connecting to backend servers, or scraping web page data.
*   **Example:**
    ```python
    import requests
    
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        data = response.json()
        print("GitHub API is online. Current user endpoint:", data["current_user_url"])
    ```

### C. `pygame`
*   **Definition:** A library designed for writing 2D video games in Python.
*   **Common Use Case:** Loading game assets (images, sound effects) and drawing graphical window interfaces.
*   **Example:**
    ```python
    import pygame
    
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("My Pygame Window")
    
    # Simple loop to keep screen open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    ```

---

## 3. Built-In Standard Libraries (Pre-Installed)

These libraries come bundled with Python automatically. You do not need `pip` to install them; you just `import` them.

### A. `os` (Operating System Interface)
*   **Definition:** Provides functions to interact with the computer's directory paths, files, and operating system.
*   **Common Use Case:** Creating folders, deleting files, checking if a path exists.
*   **Example:**
    ```python
    import os
    
    # Check if a folder exists
    if not os.path.exists("test_folder"):
        os.makedirs("test_folder")  # Create folder
        print("Folder created!")
        
    # Check if a file exists
    if os.path.isfile("data.txt"):
        print("File found.")
    ```

### B. `sys` (System-Specific Parameters & Functions)
*   **Definition:** Provides access to system inputs, outputs, and parameters controlled by the Python interpreter.
*   **Common Use Case:** Exiting the program early, fetching command-line arguments.
*   **Example:**
    ```python
    import sys
    
    print("Starting process...")
    # Exits the program immediately, returning status code 0 (success)
    sys.exit(0)
    print("This will never print!")
    ```

### C. `random` (Pseudo-Random Generation)
*   **Definition:** Generates random numbers, shuffles sequences, and makes random choices.
*   **Common Use Case:** Simulating card shuffles, rolling dice, selecting random winners.
*   **Example:**
    ```python
    import random
    
    options = ["Rock", "Paper", "Scissors"]
    print("Random Choice:", random.choice(options))
    
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print("Shuffled List:", numbers)
    ```

### D. `datetime` (Date and Time Management)
*   **Definition:** Manipulates dates, times, and handles durations.
*   **Common Use Case:** Timestamping transaction logs, checking current dates.
*   **Example:**
    ```python
    from datetime import datetime
    
    now = datetime.now()
    print("Full Timestamp:", now)
    print("Formatted Date:", now.strftime("%d-%m-%Y %H:%M"))
    ```

### E. `math` (Mathematical Functions)
*   **Definition:** Provides advanced mathematical constants (like `pi`) and trigonometry/logarithmic operations.
*   **Common Use Case:** Rounding decimals, performing geometric formulas.
*   **Example:**
    ```python
    import math
    
    print("Square Root of 16:", math.sqrt(16))  # 4.0
    print("Round Up 4.2:", math.ceil(4.2))      # 5
    print("Round Down 4.8:", math.floor(4.8))   # 4
    print("Value of Pi:", math.pi)
    ```
