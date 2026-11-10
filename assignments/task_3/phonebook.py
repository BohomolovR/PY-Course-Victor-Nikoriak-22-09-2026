# Task 3

# AI log: not used

from phonebooks_function import load_contacts, add_contacts, input_required, validation_phone, search_by_full_name, \
    display_contact, search_by_phone, search_by_first_name, search_by_last_name, search_by_location, delete_contact, \
    update_contact, save_contacts

import sys


def main():
    path = sys.argv[1]
    contacts = load_contacts(path)
    print("Welcome to the phonebook!")
    while True:
        print(
            "Choose an option:\n"
            "1. Add a contact\n"
            "2. Search by full name\n"
            "3. Search by first name\n"
            "4. Search by last name\n"
            "5. Search by phone number\n"
            "6. Search by city or state\n"
            "7. Delete a contact by phone number\n"
            "8. Update a contact by phone number\n"
            "9. Save and exit")
        try:
            option = int(input("Choose an option (1-9): "))
            if not (1 <= option <= 9):
                print("Enter a number from 1 to 9.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        if option == 1:
            new_contact = {
                "first_name": input_required("First name: "),
                "last_name": input_required("Last name: ").strip(),
                "phone": validation_phone(),
                "city": input_required("City: ").strip(),
                "state": input_required("State: ").strip()
            }
            if add_contacts(contacts, new_contact):
                print("Contact is added in phonebook")
            else:
                print("A contact with this phone number already exists.")
        elif option == 2:
            first_name = input_required("First name: ")
            last_name = input_required("Last name:")
            find_contacts = search_by_full_name(contacts, first_name, last_name)
            if find_contacts:
                for contact in find_contacts:
                    display_contact(contact)
            else:
                print("Contact not found")
        elif option == 3:
            first_name = input_required("First name: ")
            find_contact = search_by_first_name(contacts, first_name)
            if find_contact:
                for contact in find_contact:
                    display_contact(contact)
            else:
                print("Contact not found")
        elif option == 4:
            last_name = input_required("Last name: ")
            find_contact = search_by_last_name(contacts, last_name)
            if find_contact:
                for contact in find_contact:
                    display_contact(contact)
            else:
                print("Contact not found")
        elif option == 5:
            phone = validation_phone()
            find_contact = search_by_phone(contacts, phone)
            if find_contact:
                for contact in find_contact:
                    display_contact(contact)
            else:
                print("Contact not found")
        elif option == 6:
            city_state = input_required("Give a city or state: ")
            find_contact = search_by_location(contacts, city_state)
            if find_contact:
                for contact in find_contact:
                    display_contact(contact)
            else:
                print("Contact not found")
        elif option == 7:
            phone = validation_phone()
            find_contacts = search_by_phone(contacts, phone)
            if find_contacts:
                for contact in find_contacts:
                    display_contact(contact)
                confirmation = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    delete_contact(contacts, phone)
                else:
                    print("Deletion cancelled.")
                    continue

            else:
                print("Contact not found")
        elif option == 8:
            phone = validation_phone()
            find_contacts = search_by_phone(contacts, phone)
            if find_contacts:
                for contact in find_contacts:
                    display_contact(contact)
                while True:
                    try:
                        update = int(input("What do you want update?\n"
                                           "1. First name\n"
                                           "2. Last name\n"
                                           "3. Phone\n"
                                           "4. City\n"
                                           "5. State\n"))
                        if 0 < update <= 5:
                            break
                        else:
                            print("Number 1-5: ")
                    except ValueError:
                        print("Only number(1-5")
                        continue
                if update == 1:
                    new_data = {"first_name": input_required("New first name ")}
                elif update == 2:
                    new_data = {"last_name": input_required("New last name ")}
                elif update == 3:
                    new_data = {"phone": validation_phone()}
                    if new_data["phone"] != phone and search_by_phone(contacts, new_data["phone"]):
                        print("This phone number is already used by another contact.")
                        continue
                elif update == 4:
                    new_data = {"city": input_required("New city ")}
                elif update == 5:
                    new_data = {"state": input_required("New state ")}

                update_contact(contacts, phone, new_data)
                print("Contact updated successfully.")
            else:
                print("Contact not found")
        elif option == 9:
            save_contacts(path, contacts)
            break


if __name__ == "__main__":
    main()
