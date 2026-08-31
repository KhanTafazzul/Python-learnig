# 📊 Personal Expense Tracker: Logic Explanation

This document explains the logic structure and flow of the completed Personal Expense Tracker app.

---

## 1. Overview & Setup
*   **Storage File:** Expenses are stored in a text file named `expenses.txt` inside the project folder.
*   **Storage Format:** Records are saved line-by-line as comma-separated values (CSV) matching the fields: `Date,Category,Amount,Description` (e.g., `30-08-2026,Food,15.50,Lunch at cafe`).
*   **Categories:** The app enforces a standard list of categories to prevent typos: `Food`, `Travel`, `Entertainment`, `Bills`, `Shopping`, `Other`.

---

## 2. Core Functions Walkthrough

### A. `add_expense()`
*   **Amount Input:** Prompts for amount and validates that it is a positive float.
*   **Category Input:** Displays the indexed list of categories and prompts the user to select an integer between 1 and 6.
*   **Description:** Obtains optional descriptive text.
*   **Date Input:** Checks if the user provided a date in the `DD-MM-YYYY` format. If empty, it defaults to today's date automatically using:
    ```python
    datetime.now().strftime("%d-%m-%Y")
    ```
*   **Save:** Appends the record line to `expenses.txt`.

### B. `view_expenses()`
*   Checks if the file exists and is not empty.
*   Opens the file in read mode (`'r'`) and reads it line-by-line.
*   Splits fields using `.split(",")`, converts the amount back to float, sums them up, and prints a formatted console table with alignment.

### C. `filter_expenses()`
*   Prompts the user to pick a category they wish to filter by.
*   Scans the file and prints only those lines where the category matches.
*   Calculates a category subtotal and prints it.

### D. `clear_expenses()`
*   Asks the user for a final confirmation to prevent accidental loss of data.
*   If confirmed, deletes the file from disk using `os.remove()`.

---

## 3. Interactive Menu (`main()`)
*   Runs inside a `while True` loop presenting choices 1 to 5.
*   Redirects control to the appropriate functions, and breaks the loop when option 5 is chosen.
