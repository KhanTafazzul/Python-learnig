# Question 9: Useful String Methods (.lower(), .upper(), .strip(), .split(), .replace())
#
# Problem Statement:
# Clean up messy user input and analyze text using string methods.
#
# Tasks to complete:
# 1. Ask the user to input a sentence (e.g., "  Python programming is Fun and EASY!  ").
# 2. Clean the sentence by removing extra spaces at the beginning and end using `.strip()`.
# 3. Convert the cleaned sentence into all lowercase letters using `.lower()`.
# 4. Count how many total words are in the sentence using `.split()` and `len()`.
# 5. Replace all spaces in the sentence with underscores (`_`) using `.replace(" ", "_")` to turn it into a slug/filename, and print it.
#
# Example Output:
# Original Input: "  Python is awesome!  "
# Cleaned (lowercase): "python is awesome!"
# Word Count: 3
# Filename version: "python_is_awesome!"
#
# Write your code below this line:

text = input("Enter your text: ")

strip = text.strip()
lower = strip.lower()
no_words = len(strip.split())
replace = strip.replace(" ","_")
print ("Split text ,removed extra spaces:-",strip)
print("Text after it converted to lowercase:",lower)
print("Text after repacing space bar toUnderscore: ",replace)
print("Number of words in text:",no_words)




