from random import choice
import random
import string

def generate_password(length, include_upper, include_lower, include_digits, include_special):
    char_pools = []
    guaranteed_chars = []
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

    if not char_pools:
        raise ValueError("At least one character type must be selected!")
    all_chars = "".join(char_pools)
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        raise ValueError("the password length is too short to satisfy the constraints.")
    
    for i in range(remaining_length):
        guaranteed_chars.append(random.choice(all_chars))

    random.shuffle(guaranteed_chars)
    return "".join(guaranteed_chars)
    # TODO 1: Create an empty list called 'char_pools' to hold the selected character pools (strings).
    # TODO 2: Create an empty list called 'guaranteed_chars' to hold one guaranteed character from each chosen set.
    
    # TODO 3: Check if 'include_upper' is True. If yes:
    #         - Append string.ascii_uppercase to 'char_pools'
    #         - Use random.choice() to pick one uppercase letter and append it to 'guaranteed_chars'
    
    # TODO 4: Repeat the same check for 'include_lower' (string.ascii_lowercase).
    
    # TODO 5: Repeat the same check for 'include_digits' (string.digits).
    
    # TODO 6: Repeat the same check for 'include_special' (use a custom string of symbols like "!@#$%^&*()").
    
    # TODO 7: If the 'char_pools' list is empty (user said 'no' to everything):
    #         - raise a ValueError with a message: "At least one character type must be selected!"
    
    # TODO 8: Combine all the selected character pools in 'char_pools' into a single string.
    #         Hint: Use "".join(char_pools)
    
    # TODO 9: Calculate how many characters are left to generate:
    #         remaining_length = length - len(guaranteed_chars)
    
    # TODO 10: If remaining_length is less than 0:
    #          - raise a ValueError saying the password length is too short to satisfy the constraints.
    
    # TODO 11: Generate the remaining characters randomly from your combined characters pool.
    #          Hint: You can use a loop or list comprehension with random.choice()
    
    # TODO 12: Combine 'guaranteed_chars' list and the remaining characters list.
    
    # TODO 13: Shuffle the final combined list of characters using random.shuffle()
    
    # TODO 14: Join the list of characters back into a single string and return it.
    pass

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt)
        if choice in ["y","Y","yes","Yes","YES","YES"]:
            return True
        elif choice in ["n", "N","No","NO","nO","no"]:
            return False
        else:
            print("please enter a valid response.")
    # TODO 15: Write a while loop to repeatedly ask the user a prompt.
    #          - Return True if input is 'y' or 'yes'.
    #          - Return False if input is 'n' or 'no'.
    #          - Otherwise, print an error message and continue the loop.
 

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

    include_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    include_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
    include_digits = get_yes_no_input("Include digits? (y/n): ")
    include_special = get_yes_no_input("Include special characters? (y/n): ")

    # TODO 17: Get character choices using get_yes_no_input() for:
    #          - Uppercase, Lowercase, Digits, and Special Characters.
    try:
        password = generate_password(length,include_upper,include_lower,include_digits,include_special)
        print("Generated password:",password)
    except ValueError as error:
        print("Error:", error)
    # TODO 18: Call generate_password() inside a try-except block to catch any ValueError.
    #          - If successful, print the generated password.
    #          - If ValueError is caught, print the error message.
    

if __name__ == "__main__":
    main()
