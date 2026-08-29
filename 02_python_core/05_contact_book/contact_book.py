import os

CONTACTS_FILE = "02_python_core/05_contact_book/contacts.txt"

def add_contact():
    print("\n--- Add New Contact ---")
    # TODO: Prompt user for name, phone, and email
    # TODO: Validate that name is not empty
    # TODO: Open contacts.txt in append mode ('a') and save contact as Name,Phone,Email
    pass

def view_contacts():
    print("\n--- All Contacts ---")
    # TODO: Check if file exists. If not, print a message and return.
    # TODO: Open file in read mode ('r'), loop through lines, and print nicely.
    # TODO: Wrap file operations in try-except block for safety.
    pass

def search_contact():
    print("\n--- Search Contact ---")
    # TODO: Prompt user for name to search
    # TODO: Open file, loop through lines, and print matches (case-insensitive)
    pass

def delete_contact():
    print("\n--- Delete Contact ---")
    # TODO: Prompt user for name to delete
    # TODO: Read all lines, filter out matching contact(s), write remaining lines back
    pass

def main():
    while True:
        print("\n=== TERMINAL CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
