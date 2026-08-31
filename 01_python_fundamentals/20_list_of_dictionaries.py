# Question 20: List of Dictionaries (Managing Multiple Records)
#
# Problem Statement:
# Real-world data (like database records or API responses) is often stored as a list of dictionaries.
# Example:
# students = [
#     {"name": "Aman", "score": 85},
#     {"name": "Priya", "score": 92},
#     {"name": "Rahul", "score": 78}
# ]
#
# Tasks to complete:
# 1. Create a list called `students` containing at least 3 student dictionaries with keys `"name"` and `"score"`.
# 2. Iterate through the `students` list using a `for` loop, and print each student's name and score.
#    Format output like: "Student: Aman | Score: 85"
# 3. Calculate and print the average score of all students.
# 4. Find and print the student with the highest score (print both name and score).
#
# Write your code below this line:

students = [
            {"name":"Aman","score":85},
            {"name":"Priya","score":92},
            {"name":"Rahul","score":78}
            ]
highest_marks = 0
highest_name = ""
total_score = 0

for i in students:
    print(f"Student: {i['name']} | Score: {i['score']}")
    total_score += i['score']
    if i['score'] > highest_marks:
        highest_marks = i['score']
        highest_name = i['name']  

average_score = total_score/len(students)
print("Average score is :",average_score)
print("Student with highest marks is:",highest_name,  "|", highest_marks) 
