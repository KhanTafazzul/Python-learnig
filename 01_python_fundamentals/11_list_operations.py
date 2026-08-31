# Question 11: List Operations (.append(), .pop(), .sort(), `in` check)
#
# Problem Statement:
# Build a Student Marks & Guest List Manager that uses common list methods.
#
# Tasks to complete:
# 1. Create an empty list called `guests`.
# 2. Ask the user in a loop (3 times) to input a guest name, and add each name to the `guests` list using `.append()`.
# 3. Ask the user for a name to search. Check if the name is in the list using `if name in guests:`.
#    - If present, print "Guest is invited!".
#    - If not present, print "Guest not found on the list."
# 4. Sort the list alphabetically using `.sort()` and print the sorted guest list.
# 5. Remove the last added guest using `.pop()` and print the updated list along with the removed guest name.
#
# Write your code below this line:

guests = []
for i in range(1,4):
    name = input(f"Enter guest{i} name: ")
    guests.append(name)

guest_search = input("Enter the name of the guest to search: ")

if guest_search in guests:
    print(f"{guest_search} is invited")

else:
    print(f"{guest_search} not found")
    
guests.sort()
print(f"Sorted list of guests:{guests}")

removed_guest = guests.pop()
print(f"Removed guest:{removed_guest}")
print(f"Updated list of guests: {guests}")
