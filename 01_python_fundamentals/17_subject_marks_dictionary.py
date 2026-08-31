# Question 17: Subject Marks Dictionary & Iteration
#
# Problem Statement:
# Store subject names and marks in a dictionary using a loop, iterate through items,
# and compute total and average marks.
#
# Tasks to complete:
# 1. Prompt user for 3 subject names and marks, storing them in a dictionary.
# 2. Iterate using `marks.items()` to display each subject and mark.
# 3. Compute `total` using `sum(marks.values())` and calculate average.
# 4. Print total, formatted average (`:.2f`), and full dictionary.
#
# Write your code below this line:

marks = {}
for i in range(1, 4):
    subject = input(f"Enter subject {i} name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

for subject, mark in marks.items():
    print(f"{subject}: {mark}")

total = sum(marks.values())
average = total / len(marks)

print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")

print(f"All Subject and Marks: {marks}")

