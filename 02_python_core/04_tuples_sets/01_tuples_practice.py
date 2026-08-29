# Task 1: Tuple Operations & Immutability

# 1. Create a function get_student_record(name, age, grade, city)
# It should return a tuple of these four values.
def get_student_record(name, age, grade, city):
    std_record = (name, age, grade, city)
    return std_record

# --- Test Section ---
# 2. Call the function with some details (e.g., "Aman", 22, "A", "Delhi")
# Unpack the returned tuple into std_name, std_age, std_grade, std_city
# Print them nicely.
record = get_student_record("Aman", 22, "A", "Delhi")

std_name, std_age, std_grade, std_city = record
print(f"Name: {std_name}")
print(f"Age: {std_age}")
print(f"Grade: {std_grade}")
print(f"City: {std_city}")

# 3. Attempt to modify the grade in the returned record directly (e.g., record[2] = "A+")
# Wrap this in a try-except block to handle TypeError and print a friendly message.
try:
    record[2] = "A+"
except TypeError as e:
    print("\nError: Tuples are immutable and cannot be modified!")
    print(f"Details: {e}")