# 🔐 Secure Password Generator: Logic Explanation

This document explains the logic structure and flow of the completed Secure Password Generator.

---

## 1. Project Goal & Setup
*   **Persistent Custom Rules:** The program generates a password of user-defined length (minimum 6).
*   **Guaranteed Selection:** If a user selects a character set (like numbers or uppercase), the program **must** include at least one character from that set, preventing weak/random results.
*   **Cryptographic Randomness:** Leverages Python's `random` module for unpredictable selections and shuffling, and `string` constants for clean letter pools.

---

## 2. Core Functions & Code Walkthrough

### A. `generate_password()`
Creates the password based on selected options and length constraints.

1.  **Pool & Guarantee Initialization:** Setup lists to hold the selected character pools and the guaranteed characters that are pre-selected to enforce strength.
    ```python
    char_pools = []
    guaranteed_chars = []
    ```

2.  **Evaluating Selection Flags:** Checks each input flag. If `True`, adds that character pool string to `char_pools` and uses `random.choice()` to add one guaranteed character of that type to `guaranteed_chars`.
    ```python
    if include_upper:
        char_pools.append(string.ascii_uppercase)
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    
    if include_lower:
        char_pools.append(string.ascii_lowercase)
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if include_digits:
        char_pools.append(string.digits)
        guaranteed_chars.append(random.choice(string.digits))
    if include_special:
        char_pools.append("!@#$%^&*()")
        guaranteed_chars.append(random.choice("!@#$%^&*()"   ))
    ```

3.  **Config Validation:** Checks if the user selected no sets at all. If so, triggers a manual `ValueError` to stop execution.
    ```python
    if not char_pools:
        raise ValueError("At least one character type must be selected!")
    ```

4.  **Combining & Length Constraint Checks:** Joins all selected character sets. Calculates `remaining_length` (requested length minus guaranteed characters already selected). Throws a `ValueError` if the length is too short to fulfill the requested flags.
    ```python
    all_chars = "".join(char_pools)
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        raise ValueError("the password length is too short to satisfy the constraints.")
    ```

5.  **Random Fill:** Uses a loop to select the remaining characters from the combined pool of selected characters.
    ```python
    for i in range(remaining_length):
        guaranteed_chars.append(random.choice(all_chars))
    ```

6.  **Shuffle & Output:** Shuffles the full list of characters in-place using `random.shuffle()` so the guaranteed items are not always at the front, and converts the list back to a string.
    ```python
    random.shuffle(guaranteed_chars)
    return "".join(guaranteed_chars)
    ```

---

### B. `get_yes_no_input(prompt)`
Asks user for a yes/no input, handles validation, and loops until a correct response is received.

*   Runs in a `while True` loop, gets the keyboard input, and returns `True` for yes-related choices or `False` for no-related choices. Prints a warning if invalid.
    ```python
    def get_yes_no_input(prompt):
        while True:
            choice = input(prompt)
            if choice in ["y","Y","yes","Yes","YES","YES"]:
                return True
            elif choice in ["n", "N","No","NO","nO","no"]:
                return False
            else:
                print("please enter a valid response.")
    ```

---

### C. `main()`
Manages the terminal interface, gets the password configuration from the user, and prints the result.

1.  **Welcome Banner & Input Validation:** Shows a title. Prompts for a length. Uses `try-except ValueError` to catch cases where letters are typed instead of a number, exiting early if invalid. Checks if length is less than 6.
    ```python
    def main():
        print("=" * 45)
        print("      SECURE TERMINAL PASSWORD GENERATOR       ")
        print("=" * 45)
        
        try:
            length = int(input("Enter the length of the password must be at least 6: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if length < 6:
           print("Password length must be at least 6 characters.")
           return
        else:
            pass
    ```

2.  **Getting Set Rules:** Calls `get_yes_no_input()` to collect yes/no selections for each character type.
    ```python
    include_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    include_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
    include_digits = get_yes_no_input("Include digits? (y/n): ")
    include_special = get_yes_no_input("Include special characters? (y/n): ")
    ```

3.  **Generating and Printing:** Calls `generate_password()` inside a `try-except` block to capture any constraints error, printing the password if successful.
    ```python
    try:
        password = generate_password(length,include_upper,include_lower,include_digits,include_special)
        print("Generated password:",password)
    except ValueError as error:
        print("Error:", error)
    ```
