# Question 15: Student Profile Static (Dictionary Basics)
#
# Problem Statement:
# Create a dictionary to store a student's basic details (name, age, branch).
# Access specific values using keys, update an existing value, and add a new key-value pair.
#
# Tasks to complete:
# 1. Create a dictionary `student` with keys `"name"`, `"age"`, and `"branch"`.
# 2. Print the student's name using dictionary indexing.
# 3. Update the student's age and add a new key `"city"`.
# 4. Print the updated dictionary.
#
# Write your code below this line:

student = {
    "name": "Khan",
    "age": 18,
    "branch": "B.Tech"
}

print(student["name"])

student["age"] = 19
student["city"] = "Delhi"

print(student)