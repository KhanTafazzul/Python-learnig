# 📊 Personal Expense Tracker: Logic Explanation

This document explains the logic structure and flow of the Personal Expense Tracker program by breaking down the code into small, digestible parts.

---

## 1. Overview & Storage Format
Expenses are saved line-by-line in a text file (`expenses.txt`) as comma-separated values (CSV) matching the fields:
`Date,Category,Amount,Description`

*Example file line:*
```text
31-08-2026,Food,15.50,Lunch at cafe
```

---

## 2. Code Breakdown & Snippets

### A. The Input Helper (`get_yes_no_input`)
This helper function ensures that the user only enters valid yes/no responses. It loops continuously until they enter `y`, `n`, or standard variations, returning a boolean.

```python
def get_yes_no_input(prompt):
    while True:
        choice = input(prompt)
        if choice in ["y", "Y", "yes", "Yes", "YES", "YES"]:
            return True
        elif choice in ["n", "N", "No", "NO", "nO", "no"]:
            return False
        else:
            print("please enter a valid response.")
```

---

### B. Adding a New Expense (`add_expense`)

#### 1. Validating Amount
We ask the user for the amount spent, convert it to a floating-point number, and ensure it is positive. If the input is not a number, the `try-except ValueError` catches it.

```python
    amount_input = input("Enter the amount spent: ")
    try:
        amount = float(amount_input)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
```

#### 2. Selecting Category
We display the options from the `CATEGORIES` list. The user selects a index number (1 to 6). We map that number back to the correct category string.

```python
    print("Categories:")
    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")
        
    try:
        cat_choice = int(input("Select a category (1-6): "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("Invalid category selection.")
            return
        category = CATEGORIES[cat_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
```

#### 3. Date Parsing & Validation
If the user presses Enter without typing a date, we assign today's date automatically. Otherwise, we parse it using `datetime.strptime()` to verify it matches the `DD-MM-YYYY` format.

```python
    date_input = input("Enter date (DD-MM-YYYY) or press [Enter] for today: ")
    if date_input == "":
        date = datetime.now().strftime("%d-%m-%Y")
    else:
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            date = date_input
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")
            return
```

#### 4. Appending to File
We open `expenses.txt` in append (`'a'`) mode to write the new expense at the end of the file, separating fields with commas.

```python
    try:
        with open(EXPENSES_FILE, "a") as file:
            file.write(f"{date},{category},{amount},{description}\n")
        print("Expense added successfully!")
    except Exception as error:
        print("Error saving to file:", error)
```

---

### C. Viewing All Expenses (`view_expenses`)

#### 1. Checking File Existence & Size
Before attempting to read the file, we check if it exists and contains data so we do not attempt to read an empty or missing log.

```python
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        print("No expenses logged yet.")
        return
```

#### 2. Reading & Tabular Printing
We read each line, split it by commas, and print it with left-alignment format spacing. We also add each expense amount to a running `total_spent` variable.

```python
    total_spent = 0.0
    print("\n" + "-" * 60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description':<20}")
    print("-" * 60)
    
    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    date, category, amount, description = parts
                    try:
                        amount_val = float(amount)
                        total_spent += amount_val
                    except ValueError:
                        amount_val = 0.0
                    print(f"{date:<12} | {category:<15} | {amount_val:<10.2f} | {description:<20}")
        print("-" * 60)
        print(f"Total Spent: {total_spent:.2f}")
        print("-" * 60)
```

---

### D. Filtering Expenses (`filter_expenses`)
We prompt the user to choose a category to filter by. When reading the file, we only print the line if its category matches the filtered category, keeping a separate subtotal.

```python
    try:
        with open(EXPENSES_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    date, category, amount, description = parts
                    if category == filter_cat:
                         found = True
                         try:
                             amount_val = float(amount)
                             total_filtered += amount_val
                         except ValueError:
                             amount_val = 0.0
                         print(f"{date:<12} | {category:<15} | {amount_val:<10.2f} | {description:<20}")
```

---

### E. Clearing Expenses (`clear_expenses`)
To prevent accidental data loss, we ask for confirmation. If the user confirms, we delete `expenses.txt` from disk.

```python
def clear_expenses():
    if get_yes_no_input("Are you sure you want to clear all expense logs? (y/n): "):
        try:
            if os.path.exists(EXPENSES_FILE):
                os.remove(EXPENSES_FILE)
                print("Expense logs cleared successfully!")
            else:
                print("No expense log file to clear.")
        except Exception as error:
            print("Error deleting file:", error)
```

---

### F. Interactive Menu Loop (`main`)
This handles choice selection. The menu repeats inside a `while True` loop and redirects user actions to the appropriate function.

```python
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            clear_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
```
