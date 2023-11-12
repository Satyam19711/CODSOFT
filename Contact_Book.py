contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact {name} added successfully.")

def view_contact_list():
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"{name}: {details['Phone']}")

def search_contact(query):
    results = []
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['Phone']:
            results.append((name, details))
    return results

def update_contact(name, new_phone, new_email, new_address):
    if name in contacts:
        contacts[name]['Phone'] = new_phone
        contacts[name]['Email'] = new_email
        contacts[name]['Address'] = new_address
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# User Interface
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif choice == '2':
        view_contact_list()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("\nSearch Results:")
            for name, details in results:
                print(f"{name}: {details['Phone']}")
        else:
            print("No matching contacts found.")

    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email address: ")
        new_address = input("Enter new address: ")
        update_contact(name, new_phone, new_email, new_address)

    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)

    elif choice == '6':
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

#THANKYOU