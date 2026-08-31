# Question 23: Shopping Cart & Billing System (Lists, Dictionaries & Loops)
#
# Problem Statement:
# Create an interactive shopping cart system for a grocery store.
# The user can view available items with prices, add items to their cart with quantities,
# calculate total cost, apply a 10% discount if total exceeds ₹500, and print a final bill.
#
# Available Store Items (Use this dictionary):
# store_items = {
#     "apple": 60,
#     "milk": 30,
#     "bread": 40,
#     "eggs": 70,
#     "rice": 120
# }
#
# Tasks to complete:
# 1. Display available items and prices from `store_items`.
# 2. Use a `while` loop allowing the user to add items to their cart (`cart` dictionary mapping item -> quantity).
#    - If user enters "done", stop adding items.
#    - If item is not in store, print "Item not available!".
# 3. Calculate total bill amount: `quantity * price` for each item.
# 4. If total > 500, apply a 10% discount (`total * 0.90`) and print discount notification.
# 5. Print a clean, formatted receipt showing each item, quantity, subtotal, and final bill amount.
#
# Write your code below this line:

store_items = {
    "apple": {
        "price":60,
        "quantity": 10
    },
    "milk": {
        "price":30,
        "quantity": 5
    },
    "bread": {
        "price":40,
        "quantity": 8
    },
    "eggs": {
        "price":70,
        "quantity": 12
    },
    "rice": {
        "price":120,
        "quantity": 15
    }
    }

cart = []
user_input = ""
total = 0

# Display available items
print("Welcome to the Shopping Cart!")
print("Available Items:")
for item, price in store_items.items():
    print(f"- {item.capitalize()}: ₹{store_items[item]['price']}")
print("----------------------------")

# Add items to cart

# Add items to cart
while True:
    user_input = input("Enter the item you want to buy, or type 'done' to quit: ").lower()
    
    if user_input == "done":
        break

    # 1. Check if item exists in store
    elif user_input not in store_items:
        print("Item not available in store!")

    # 2. Check if item is in stock
    elif store_items[user_input]["quantity"] > 0:
        cart.append(user_input)   #Store item name string
        store_items[user_input]["quantity"] -= 1
        total += store_items[user_input]["price"]
        print(f"Added {user_input.capitalize()} to cart!")
    else:
        print(f"Sorry, {user_input.capitalize()} is out of stock!")

print("\nReceipt:")
for item in cart:
    print(f"- {item.capitalize()} x 1 = ₹{store_items[item]['price']}")

if total > 500:
    total -= total * 0.10
    print("\nYou got a 10% discount!")

print(f"Your total amount is: ₹{total:.2f}")
print("Thank you for shopping!")
