# Question 16: Student Profile Builder (Dictionary Basics)
#
# Problem Statement:
# Build a dynamic student profile dictionary using user input and practice updating dictionary entries.
#
# Tasks to complete:
# 1. Create an empty dictionary `student = {}`.
# 2. Take user inputs for `"name"`, `"age"`, `"course"`, and `"city"`.
# 3. Display the formatted profile string.
# 4. Update the `"city"` entry with a new input and display the updated profile.
#
# Write your code below this line:

student = {}

student["name"] = input("Enter student's name: ")
student["age"] = int(input("Enter student's age: "))
student["course"] = input("Enter student's course: ")
student["city"] = input("Enter student's city: ")

print(f"Student Profile: {student['name']}, is {student['age']} years old and is enrolled in the {student['course']} course, and lives in {student['city']}.")

student["city"] = input("Enter student's city: ")

print(f"Updated Student Profile: {student['name']}, is {student['age']} years old and is enrolled in the {student['course']} course, and lives in {student['city']}.")