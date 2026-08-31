import os
from datetime import datetime

EXPENSES_FILE = "02_python_core/11_expense_tracker/expenses.txt"
CATEGORIES = ["Food", "Travel", "Entertainment", "Bills", "Shopping", "Other"]

def add_expense():
    print("\n--- 💵 Add New Expense ---")
    # TODO 1: Ask the user for the amount spent.
    #         - Validate that it is a positive float using try-except.
    
    # TODO 2: Display the CATEGORIES list to the user with index numbers (1 to 6).
    #         - Prompt the user to select one category.
    #         - Validate that the chosen number is between 1 and the length of CATEGORIES.
    
    # TODO 3: Ask the user for a brief description (optional).
    
    # TODO 4: Ask the user for a date (DD-MM-YYYY) or press [Enter] to default to today's date.
    #         - If date is entered, validate it matches the DD-MM-YYYY format using datetime.strptime().
    #         - Otherwise, auto-assign today's date using datetime.now().strftime("%d-%m-%Y").
    
    # TODO 5: Save this expense to the EXPENSES_FILE by opening it in append ('a') mode.
    #         - Save each field separated by commas: date,category,amount,description followed by a newline.
    #         - Wrap this in a try-except block to catch any file access exceptions safely.
    pass

def view_expenses():
    # TODO 6: Check if the EXPENSES_FILE exists and is not empty. If not, alert the user and return.
    
    # TODO 7: Open the EXPENSES_FILE in read ('r') mode.
    #         - Read and print each line formatted neatly in a table structure.
    #         - Split each line using .split(",") to extract date, category, amount, and description.
    #         - Keep a running sum of all amounts.
    #         - Print the total spent at the bottom.
    pass

def filter_expenses():
    # TODO 8: Check if the file exists and is not empty.
    
    # TODO 9: Ask the user which category they want to filter by (display list of options).
    
    # TODO 10: Read the file line-by-line:
    #          - Only print lines where the category matches the user's selected category.
    #          - Keep a subtotal sum of the matched expenses and print it at the bottom.
    pass

def clear_expenses():
    # TODO 11: Ask the user for a final confirmation (yes/no) to clear logs.
    #          - If confirmed, delete the EXPENSES_FILE using os.remove() inside a try-except block.
    pass

def main():
    while True:
        print("\n" + "=" * 45)
        print("           📊 PERSONAL EXPENSE TRACKER          ")
        print("=" * 45)
        print("1. Add Expense")
        print("2. View All Expenses & Total")
        print("3. Filter Expenses by Category")
        print("4. Clear Expense Log")
        print("5. Exit")
        print("=" * 45)
        
        # TODO 12: Get user choice and redirect to the corresponding functions.
        #          - choice '1' -> add_expense()
        #          - choice '2' -> view_expenses()
        #          - choice '3' -> filter_expenses()
        #          - choice '4' -> clear_expenses()
        #          - choice '5' -> print goodbye and break loop
        #          - Any other input -> print error and repeat
        pass

if __name__ == "__main__":
    main()
