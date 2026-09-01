import os
from datetime import datetime

EXPENSES_FILE = "02_python_core/11_expense_tracker/expenses.txt"
CATEGORIES = ["Food", "Travel", "Entertainment", "Bills", "Shopping", "Other"]

def get_yes_no_input(prompt):
    # Loop continuously until a valid yes/no response is given
    while True:
        choice = input(prompt)
        if choice in ["y", "Y", "yes", "Yes", "YES", "YES"]:
            return True
        elif choice in ["n", "N", "No", "NO", "nO", "no"]:
            return False
        else:
            print("please enter a valid response.")

def add_expense():
    print("\n--- Add New Expense ---")
    
    # 1. Ask for amount and validate
    amount_input = input("Enter the amount spent: ")
    try:
        amount = float(amount_input)
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
        
    # 2. Display categories
    print("Categories:")
    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")
        
    # 3. Ask user for category choice and validate selection
    try:
        cat_choice = int(input(f"Select a category (1-{len(CATEGORIES)}): "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("Invalid category selection.")
            return
        category = CATEGORIES[cat_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
        
    # 4. Ask for description (optional)
    description = input("Enter a brief description (optional): ")
    if not description:
        description = "N/A"
        
    # 5. Ask for date or default to today
    date_input = input("Enter date (DD-MM-YYYY) or press [Enter] for today: ")
    if date_input == "":
        date = datetime.now().strftime("%d-%m-%Y")
    else:
        try:
            # Validate date matches required format
            datetime.strptime(date_input, "%d-%m-%Y")
            date = date_input
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")
            return
            
    # 6. Append expense details to the text file
    try:
        with open(EXPENSES_FILE, "a") as file:
            file.write(f"{date},{category},{amount},{description}\n")
        print("Expense added successfully!")
    except Exception as error:
        print("Error saving to file:", error)

def view_expenses():
    # Check if file exists and contains data
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        print("No expenses logged yet.")
        return
        
    total_spent = 0.0
    print("\n" + "-" * 60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description':<20}")
    print("-" * 60)
    
    # Read each line and display neatly in a tabular format
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
    except Exception as error:
        print("Error reading file:", error)

def filter_expenses():
    # Check if file exists and contains data
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        print("No expenses logged yet.")
        return
        
    # Ask user for category to filter by
    print("Categories:")
    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")
        
    try:
        cat_choice = int(input(f"Select category to filter by (1-{len(CATEGORIES)}): "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("Invalid category selection.")
            return
        filter_cat = CATEGORIES[cat_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
        
    total_filtered = 0.0
    found = False
    print("\n" + "-" * 60)
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description':<20}")
    print("-" * 60)
    
    # Display only expenses matching selected category
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
        if not found:
             print("No expenses found in this category.")
        print("-" * 60)
        print(f"Subtotal for {filter_cat}: {total_filtered:.2f}")
        print("-" * 60)
    except Exception as error:
        print("Error reading file:", error)

def clear_expenses():
    # Ask for confirmation before deleting data
    if get_yes_no_input("Are you sure you want to clear all expense logs? (y/n): "):
        try:
            if os.path.exists(EXPENSES_FILE):
                os.remove(EXPENSES_FILE)
                print("Expense logs cleared successfully!")
            else:
                print("No expense log file to clear.")
        except Exception as error:
            print("Error deleting file:", error)

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
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
