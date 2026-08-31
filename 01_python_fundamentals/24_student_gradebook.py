# Question 24: Class Gradebook & Topper Finder (Functions & Nested Data)
#
# Problem Statement:
# Create a gradebook program to store records for multiple students.
# Each student has a name and a dictionary of marks for 3 subjects (Maths, Science, English).
# Calculate each student's average mark, assign a Pass/Fail status, and find the class topper!
#
# Tasks to complete:
# 1. Take input for 3 students. Store them in a list of dictionaries `gradebook`.
#    Example structure for each student:
#    {
#        "name": "Aman",
#        "marks": {"Maths": 85, "Science": 90, "English": 80}
#    }
# 2. Write a helper function `get_student_average(student_dict)` that returns the average mark of a student.
# 3. Iterate through `gradebook` and print each student's name, total marks, average score, and status:
#    - Status = "PASSED" if average >= 40, else "FAILED".
# 4. Identify and display the **Class Topper** (the student with the highest average mark).
#
# Write your code below this line:
gradebook = [
    {
        "name": "Aman",
        "marks": {"Maths":00,"Science": 0, "English":0}
    },          
    {
        "name": "Aman",
        "marks": {"Maths": 00, "Science": 0, "English": 0}
    },
    {
        "name": "Aman",
        "marks": {"Maths": 00, "Science": 0, "English": 0}
    }
]

def get_student_average(student_dict):
    sum = 0
    for value in student_dict.values():
        sum += value

    return sum/len(student_dict)

def get_student_total_marks(student_dict):
    return sum(student_dict.values())



for i in range(3):
    gradebook[i]["name"] = input("Enter student name: ")
    gradebook[i]["marks"]["Maths"] = int(input("Enter marks in Maths: "))
    gradebook[i]["marks"]["Science"] = int(input("Enter marks in Science: "))
    gradebook[i]["marks"]["English"] = int(input("Enter marks in English: "))
    
hishest_average = 0
topper_name = ""
total_marks = 0
average = 0
grade = ""

highest_average = 0
topper_name = ""

# Loop through the list of student dictionaries
for student in gradebook:
    average = get_student_average(student['marks'])
    total_marks = get_student_total_marks(student['marks'])
    
    if highest_average < average:
        highest_average = average
        topper_name = student['name']

    if average >= 40:
        grade = "PASSED"

    else:
        grade = "FAILED"
        
    print(f"Student: {student['name']} | Total Marks: {total_marks} | Average Score: {average:.2f} | Status: {grade}")

print(f"\nTopper is {topper_name} with highest average score of {highest_average:.2f}")


