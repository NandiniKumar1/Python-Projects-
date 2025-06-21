import pickle
import os

FILENAME = 'emails.dat'

# Load the existing dictionary from the file, or create a new one if the file doesn't exist
def load_emails():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

# Save the dictionary to the file using pickle
def save_emails(email_dict):
    with open(FILENAME, 'wb') as file:
        pickle.dump(email_dict, file)

# Display menu options
def display_menu():
    print("\nMenu:")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit")

# Main program
def main():
    email_dict = load_emails()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            print(f"Email: {email_dict.get(name, 'Not found')}")
        elif choice == '2':
            name = input("Enter the name: ")
            if name in email_dict:
                print("That name already exists.")
            else:
                email = input("Enter the email address: ")
                email_dict[name] = email
                print("Entry added.")
        elif choice == '3':
            name = input("Enter the name: ")
            if name in email_dict:
                email = input("Enter the new email address: ")
                email_dict[name] = email
                print("Email address updated.")
            else:
                print("That name was not found.")
        elif choice == '4':
            name = input("Enter the name: ")
            if name in email_dict:
                del email_dict[name]
                print("Entry deleted.")
            else:
                print("That name was not found.")
        elif choice == '5':
            save_emails(email_dict)
            print("Email data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
