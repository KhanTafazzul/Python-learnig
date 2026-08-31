# Question 19: Dictionary Iteration (.items(), .keys(), .values())
# 
# Problem Statement:
# You have a store inventory represented as a dictionary where key = product name, value = price.
# Example: inventory = {"Apple": 50, "Banana": 20, "Mango": 100, "Orange": 40}
#
# Tasks to complete:
# 1. Create a dictionary named `inventory` with at least 4 items and their prices (as integers).
# 2. Iterate through the dictionary using a `for` loop with `.items()` and print each product along with its price.
#    Format output like: "Product: Apple | Price: Rs. 50"
# 3. Calculate the total cost of all products in the inventory using a loop and print the total.
# 4. (Bonus) Find and print the product with the highest price.
#
# Write your code below this line:

inventory = {}

for i in range(1, 6):
    item_name = input("Enter item name: ")
    item_price = int(input("Enter item price: "))
    inventory[item_name] = item_price

print(inventory)
highest = 0

total_cost = 0
for key, value in inventory.items():
    print(f"Product: {key} | Price: Rs. {value}")
    total_cost += value
    if value > highest:
        highest = value

print(f"Total amount is :{total_cost}")
print(f"And highest amount product is :{highest} ")

    