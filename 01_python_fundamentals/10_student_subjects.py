# Question 10: List Operations & Index Replacement
#
# Problem Statement:
# Practice fundamental list manipulations: indexing, appending new elements,
# updating an item by index, and getting list length using `len()`.
#
# Tasks to complete:
# 1. Create a list `sub` containing subject names.
# 2. Access first and last elements using indexing (`[0]` and `[-1]`).
# 3. Append a new subject entered by user using `.append()`.
# 4. Replace an existing subject at a specified index.
# 5. Display the final list and total subject count using `len()`.
#
# Write your code below this line:

sub = ["Python", "Maths", "English", "Science"]
print(sub)
print(sub[0])       # First item: Python
print(sub[-1])      # Last item: Science
sub.append(input("Enter a new subject: "))  # Adding a new subject to the list
print(f"{sub}, which subject you want to replace?")
sub[int(input("Enter the index of the subject you want to replace: "))] = input("Enter the new subject: ")  # Replacing a subject at a specific index
print(sub)
print(f"Total number of subjects: {len(sub)}")  # Printing the total number of subjects 