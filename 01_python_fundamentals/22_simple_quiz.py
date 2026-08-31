# Question 22: Multiple-Choice Quiz Game (Lists, Dictionaries & Loops)
#
# Problem Statement:
# Create a multiple-choice quiz game that asks the user 3 questions, tracks their score,
# and displays their final score and percentage.
#
# Tasks to complete:
# 1. Store quiz questions in a list of dictionaries. Each dictionary should contain:
#    - "question": string
#    - "options": list of strings (e.g., ["A. Python", "B. Java", "C. C++", "D. HTML"])
#    - "answer": string (the correct option key, e.g., "A")
# 2. Track the user's score starting at 0 (`score = 0`).
# 3. Loop through all questions:
#    - Display the question and print each option on a new line.
#    - Get user input (convert to uppercase using `.upper()` so 'a' or 'A' both work).
#    - If answer is correct: add 1 to `score` and print "Correct! 🎉"
#    - If wrong: print "Wrong! The correct answer was X."
# 4. Print the final score at the end (e.g., "Final Score: 2 / 3 (66.67%)").
#
# Write your code below this line:

user_point = 0
mcqs = {
    "question1" : {
        "question":"What is the capital of India?",
        "options":["A. Mumbai","B.Lucknow","C.New Delhi","D.Kolkata"],
        "answer":"C"
    },
    "question2":{
        "question":"What is the largest planet in solar system?",
        "options":["A. Earth","B.Jupiter","C.Mars","D.Venus"],
        "answer":"B"
    },
    "question3":{
        "question":"What is the chemical symbol of Gold?",
        "options":["A. Ag","B. Au","C. Pt","D. Fe"],
        "answer":"B"
    },
    "question4":{
        "question":"What is the largest mammal on Earth?",
        "options":["A. Elephant","B. Whale","C. Giraffe","D. Lion"],
        "answer":"B"    
    }
     
}
for key, item in mcqs.items():
    # 1. Print the current question
    print("\n" + item["question"])
    
    # 2. Print each option on a new line
    for option in item["options"]:
        print(option)
    
    # 3. Get user input and check answer against item["answer"]
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == item["answer"]:
        print("Correct! ")
        user_point += 1
    else:
        print("Wrong! The correct answer was", item["answer"])

# Dynamic total score calculation (using len(mcqs) instead of hardcoding 4)
score = (user_point / len(mcqs)) * 100
print(f"\nFinal Score: {user_point}/{len(mcqs)} ({score:.1f}%)")

  
    