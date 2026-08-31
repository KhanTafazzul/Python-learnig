# Question 18: Contact Search System (`.get()` Method)
#
# Problem Statement:
# Store contact names and phone numbers in a dictionary and search for a contact safely using `.get()`.
#
# Tasks to complete:
# 1. Populate a dictionary `contacts` with 3 name-phone number pairs via user input.
# 2. Prompt user for a `search_name`.
# 3. Use `contacts.get(search_name)` to retrieve the phone number safely.
# 4. If key is missing (`None`), print a "not found" message; otherwise display the phone number.
#
# Write your code below this line:

contacts = {}

for i in range(1 , 4):
    name = input(f"Enter contact {i} name: ")
    phone_number = input(f"Enter contact {name}'s phone number: ")
    contacts[name] = phone_number

search_name = input("Enter the name of the contact you want to search for: ")
phone_number = contacts.get(search_name)

if phone_number is None:
    print(f"{search_name} not found in contacts.")

else:
    print(f"{search_name}'s phone number is: {phone_number}")

print(f"All contacts: {contacts}")

