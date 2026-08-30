import os

CONTACTS_FILE = "02_python_core/05_contact_book/contacts.txt"

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    
    try:
        if name == "":
            raise ValueError("Error: Name cannot be empty!")
    except ValueError as e:
        print(e)
        return
        
    try:
        with open(CONTACTS_FILE, 'a') as file:
            file.write(f"{name},{phone},{email}\n")
        print("Contact added successfully!")
    except Exception as e:
        print(f"An error occurred while saving the contact: {e}")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found!")
        return  
        
    try:
        print("\n--- All Contacts ---")
        with open(CONTACTS_FILE, 'r') as file:
            has_contacts = False
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                
                name, phone, email = line.split(",")
                print(f"Name : {name}")
                print(f"Phone : {phone}")
                print(f"Email : {email}")
                print("-" * 20)
                has_contacts = True
                
            if not has_contacts:
                print("No contacts found!")
    except Exception as e:
        print(f"An error occurred while reading contacts: {e}")

def search_contact():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found!")
        return 
        
    print("\n--- Search Contact ---")
    search_name = input("Enter name to search: ").strip()
    found = False
   
    try:
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                    
                name, phone, email = line.split(",")
                if search_name.lower() == name.lower():
                    print(f"Name : {name}")
                    print(f"Phone : {phone}")
                    print(f"Email : {email}")
                    print("-" * 20)
                    found = True
            
            if not found:
                print(f"Contact '{search_name}' was not found.")
    except Exception as e:
        print(f"An error occurred while searching contacts: {e}")

def delete_contact():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found!")
        return 
        
    print("\n--- Delete Contact ---")
    delete_name = input("Enter name to delete: ").strip()
    
    remaining_contacts = []  # List to store the contacts we want to keep
    deleted = False          # Flag to track if we found and deleted the contact
    
    try:
        # Step 1: Read and filter the contacts
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue  # skip empty lines
                    
                name, phone, email = stripped_line.split(",")
                
                # If it matches, we skip it (don't add to remaining_contacts)
                if name.lower() == delete_name.lower():
                    deleted = True
                    print(f"Name: {name} is deleted from your contact book")
                else:
                    # If it doesn't match, we keep the original line
                    remaining_contacts.append(line)
        
        # Step 2: Write the remaining contacts back to the file
        if deleted:
            with open(CONTACTS_FILE, 'w') as file:
                file.writelines(remaining_contacts)
        else:
            print(f"Contact '{delete_name}' was not found in the database.")
               
    except Exception as e:
        print(f"An error occurred while deleting contact: {e}")
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
