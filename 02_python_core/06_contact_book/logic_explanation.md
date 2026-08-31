# 📇 Terminal Contact Book: Logic Explanation

This document explains the logic structure and flow of the completed Terminal Contact Book.

---

## 1. Overview & Setup
* **Storage File:** Contacts are persistently stored in a text file named `contacts.txt` inside the project folder.
* **Storage Format:** Each contact is stored on a new line with comma-separated fields: `Name,Phone,Email` (e.g., `Alice,123456789,alice@example.com`).

---

## 2. Core Functions Walkthrough

### A. `add_contact()`
* Prompts the user for `Name`, `Phone`, and `Email`.
* Validates that `Name` is not empty. If empty, raises a `ValueError` and exits early.
* Opens the contacts file in append mode (`'a'`) and writes the fields comma-separated, followed by a newline `\n`.
* Safely handles exceptions with a `try-except` block to prevent the app from crashing on disk access issues.

```python
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
```

### B. `view_contacts()`
* Checks if `contacts.txt` exists. If not, alerts the user and exits early.
* Opens the file in read mode (`'r'`) and reads it line-by-line.
* Splits each line using `.split(",")` to extract `name`, `phone`, and `email`, formatting the printed output nicely.
* Skips empty lines to avoid `ValueError` during splitting.

```python
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
```

### C. `search_contact()`
* Asks the user for a search query (name).
* Checks if `contacts.txt` exists.
* Iterates through the file line-by-line, splitting fields, and checking if the query matches the name (case-insensitive search using `.lower()`).

```python
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
```

### D. `delete_contact()`
* Checks if the contacts file exists. If not, it warns the user and returns.
  ```python
  if not os.path.exists(CONTACTS_FILE):
      print("No contacts found!")
      return 
  ```

* **Step 1: Read and filter the contacts**
  Reads all lines from the file, skipping empty lines. Compares each contact's name with the target name (case-insensitive). If it matches, sets the `deleted` flag to `True` and prints a deletion message. If it does not match, stores the line in a temporary `remaining_contacts` list.
  ```python
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
  ```

* **Step 2: Write the remaining contacts back to the file**
  If a deletion occurred, overwrites the contacts file using write mode (`'w'`) with the contents of `remaining_contacts`. If not found, prints a message.
  ```python
  if deleted:
      with open(CONTACTS_FILE, 'w') as file:
          file.writelines(remaining_contacts)
  else:
      print(f"Contact '{delete_name}' was not found in the database.")
  ```

---

## 3. Interactive Menu (`main()`)
* Runs in an infinite loop (`while True`) showing the option menu and redirecting the user's choice:

  * **Option 1 (Add Contact):**
    ```python
    if choice == '1':
        add_contact()
    ```
  * **Option 2 (View All Contacts):**
    ```python
    elif choice == '2':
        view_contacts()
    ```
  * **Option 3 (Search Contact):**
    ```python
    elif choice == '3':
        search_contact()
    ```
  * **Option 4 (Delete Contact):**
    ```python
    elif choice == '4':
        delete_contact()
    ```
  * **Option 5 (Exit Menu Loop):**
    ```python
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    ```
