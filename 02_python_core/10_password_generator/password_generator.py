from random import choice
import random
import string

def generate_password(length, include_upper, include_lower, include_digits, include_special):
    # Setup list variables to store allowed characters and guaranteed items
    char_pools = []
    guaranteed_chars = []
    
    # Check preferences and populate character pools with guaranteed selections
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
        guaranteed_chars.append(random.choice("!@#$%^&*()"))

    # Validate that at least one character type is selected
    if not char_pools:
        raise ValueError("At least one character type must be selected!")
        
    # Combine selected pools and calculate how many remaining characters to generate
    all_chars = "".join(char_pools)
    remaining_length = length - len(guaranteed_chars)
    
    # Check that requested length is sufficient for the rules
    if remaining_length < 0:
        raise ValueError("the password length is too short to satisfy the constraints.")
    
    # Fill out the rest of the password length randomly
    for i in range(remaining_length):
        guaranteed_chars.append(random.choice(all_chars))

    # Shuffle the final list to mix up the guaranteed characters
    random.shuffle(guaranteed_chars)
    
    # Join the list into a single string and return
    return "".join(guaranteed_chars)

def get_yes_no_input(prompt):
    # Loop continuously until a valid input is received
    while True:
        choice = input(prompt)
        
        # Check if the input is a valid yes/no choice
        if choice in ["y", "Y", "yes", "Yes", "YES", "YES"]:
            return True
        elif choice in ["n", "N", "No", "NO", "nO", "no"]:
            return False
        else:
            print("please enter a valid response.")

def main():
    print("=" * 45)
    print("      SECURE TERMINAL PASSWORD GENERATOR       ")
    print("=" * 45)
    
    # Safely get and validate password length
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

    # Prompt the user for character options
    include_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
    include_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
    include_digits = get_yes_no_input("Include digits? (y/n): ")
    include_special = get_yes_no_input("Include special characters? (y/n): ")

    # Generate and display password, catching configuration errors
    try:
        password = generate_password(length, include_upper, include_lower, include_digits, include_special)
        print("Generated password:", password)
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
