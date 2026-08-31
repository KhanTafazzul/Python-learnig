# Question 14: Student Marks Summary with Functions
#
# Problem Statement:
# Calculate total marks, average score, and letter grade for a student using helper functions.
#
# Tasks to complete:
# 1. Define `calculate_total(marks)` returning `sum(marks)`.
# 2. Define `calculate_average(marks)` returning average score.
# 3. Define `get_grade(average)` returning grade letter ('A', 'B', 'C', or 'F').
# 4. Collect marks for 3 subjects, compute summary statistics, and display grade.
#
# Write your code below this line:

def  calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)

def get_grade(calculated_average):
    if calculated_average >= 90:
        return "A"
    
    elif calculated_average >= 75 and calculated_average < 90:
        return "B"
    
    elif calculated_average >= 40 and calculated_average < 75:
        return "C"

    else:
        return "F"

marks = []

for i in range(1 , 4):
    print(f"Enter marks for subject {i}")
    marks.append(float(input()))
total = calculate_total(marks)
average = calculate_average(marks)
grade = get_grade(average)

print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average}")

if grade == "F":
    print(f"Grade: Fail")

else:
    print(f"Grade: {grade}")
