#dictonary
contacts = {}

while True:

    print("\n========== PHONE CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. View Contact Names")
    print("7. View Phone Numbers")
    print("8. Total Contacts")
    print("9. Backup Contacts")
    print("10. Clear All Contacts")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    # -----------------------------------
    # Add Contact
    # -----------------------------------
    if choice == "1":

        name = input("Enter contact name: ").title()
        phone = input("Enter phone number: ")

        contacts.update({name: phone})

        print("Contact added successfully.")

    # -----------------------------------
    # View All Contacts
    # -----------------------------------
    elif choice == "2":

        print("\n========== CONTACT LIST ==========")

        if len(contacts) == 0:
            print("No contacts available.")

        else:

            for name, phone in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("-" * 25)

    # -----------------------------------
    # Search Contact
    # -----------------------------------
    elif choice == "3":

        name = input("Enter contact name: ").title()

        phone = contacts.get(name)

        if phone:

            print(f"\nName : {name}")
            print(f"Phone: {phone}")

        else:

            print("Contact not found.")

    # -----------------------------------
    # Update Contact Number
    # -----------------------------------
    elif choice == "4":

        name = input("Enter contact name: ").title()

        if name in contacts:

            new_phone = input("Enter new phone number: ")

            contacts.update({name: new_phone})

            print("Contact updated successfully.")

        else:

            print("Contact not found.")

    # -----------------------------------
    # Delete Contact
    # -----------------------------------
    elif choice == "5":

        name = input("Enter contact name: ").title()

        if name in contacts:

            contacts.pop(name)

            print("Contact deleted successfully.")

        else:

            print("Contact not found.")

    # -----------------------------------
    # View Contact Names
    # -----------------------------------
    elif choice == "6":

        print("\n===== CONTACT NAMES =====")

        if len(contacts) == 0:
            print("No contacts available.")

        else:

            for name in contacts.keys():
                print(name)

    # -----------------------------------
    # View Phone Numbers
    # -----------------------------------
    elif choice == "7":

        print("\n===== PHONE NUMBERS =====")

        if len(contacts) == 0:
            print("No contacts available.")

        else:

            for phone in contacts.values():
                print(phone)

    # -----------------------------------
    # Total Contacts
    # -----------------------------------
    elif choice == "8":

        print(f"\nTotal Contacts: {len(contacts)}")

    # -----------------------------------
    # Backup Contacts
    # -----------------------------------
    elif choice == "9":

        backup = contacts.copy()

        print("\n===== BACKUP CONTACTS =====")

        if len(backup) == 0:

            print("No contacts available.")

        else:

            for name, phone in backup.items():

                print(f"{name} : {phone}")

    # -----------------------------------
    # Clear All Contacts
    # -----------------------------------
    elif choice == "10":

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":

            contacts.clear()

            print("All contacts deleted.")

        else:

            print("Operation cancelled.")

    # -----------------------------------
    # Exit
    # -----------------------------------
    elif choice == "11":

        print("\nThank you for using Phone Contact Book.")
        break

    else:

        print("Invalid choice. Please try again.")

{"key":"value"}
{"joy":"0176********","Sazzad": "0130*****"}