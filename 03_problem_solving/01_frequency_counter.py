# Problem 1: Word Frequency Counter (The Frequency Counter Pattern)
#
# Description:
# Given a sentence, count how many times each word appears. Then, find the word 
# that appears the most.
#
# Rules:
# - Case-insensitive: "Apple" and "apple" are the same word.
# - Strip basic punctuation (like periods '.', commas ',', and question marks '?').
#
# ==============================================================================
# LOGIC EXPLANATION:
# 1. Cleaning & Splitting (`clean_and_split`):
#    - Convert the sentence to lowercase so word matching is case-insensitive.
#    - Loop through punctuation marks (.,!?). Replace each mark with a space (" ") 
#      instead of an empty string ("") so words without spaces (like "hai,how")
#      are separated into two words rather than merging into "haihow".
#    - Split by spaces using .split() which automatically handles double spaces.
#
# 2. Counting Frequencies (`count_word_frequencies`):
#    - Create an empty dictionary 'freq_dic'.
#    - For each word, check if it exists in 'freq_dic'.
#      - If yes, increment its value by 1.
#      - If no, add the word as a key with a value of 1.
#
# 3. Peak Frequency Search (`find_most_frequent`):
#    - Loop through dictionary key-value pairs using .items().
#    - Keep track of the 'max_word' and 'max_count'.
#    - If a word's count exceeds 'max_count', update 'max_word' and 'max_count'.
# ==============================================================================

def clean_and_split(sentence):
    # Convert to lowercase
    words = sentence.lower()
    
    # Replace punctuation characters with spaces to handle lack of spaces (e.g. "hai,how")
    for char in [".", ",", "?", "!"]:
        words = words.replace(char, " ")
        
    # Split by spaces and return list of tokens
    words = words.split()
    return words

def count_word_frequencies(words_list):
    freq_dic = {}
    
    # Populate dictionary with word frequencies
    for word in words_list:
        if word in freq_dic:
            freq_dic[word] += 1
        else:
            freq_dic[word] = 1
            
    return freq_dic

def find_most_frequent(freq_dict):
    # Return None if the frequency dictionary is empty
    if not freq_dict:
        return None
    
    max_word = None
    max_count = -1
    
    # Iterate over items to find the word with the highest count
    for word, count in freq_dict.items():
        if count > max_count:
            max_count = count
            max_word = word
            
    return max_word, max_count

# --- Test Section ---
if __name__ == "__main__":
    test_sentence = "Learning Python is fun, and coding in Python is extremely rewarding! Learning is key."
    print(f"Original Sentence: {test_sentence}\n")
    
    # 1. Clean and split words
    words = clean_and_split(test_sentence)
    print("Words list:", words)
    
    # 2. Count frequencies
    frequencies = count_word_frequencies(words)
    print("Word counts:", frequencies)
    
    # 3. Find peak frequency
    top_word, count = find_most_frequent(frequencies)
    print(f"\nMost frequent word is: '{top_word}' (appears {count} times)")
