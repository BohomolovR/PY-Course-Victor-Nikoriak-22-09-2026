import json


def search_by_first_name(contacts, name):
    all_contacts = []
    for contact in contacts:
        if contact["first_name"] == name:
            all_contacts.append(contact)
    return all_contacts


def search_by_last_name(contacts, last_name):
    all_contacts = []
    for contact in contacts:
        if contact["last_name"] == last_name:
            all_contacts.append(contact)
    return all_contacts


def search_by_phone(contacts, phone):
    all_contacts = []
    for contact in contacts:
        if contact["phone"] == phone:
            all_contacts.append(contact)
    return all_contacts


def search_by_location(contacts, location):
    all_contacts = []
    for contact in contacts:
        if contact["city"] == location or contact["state"] == location:
            all_contacts.append(contact)
    return all_contacts


def delete_contact(contacts, phone):
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            return True

    return False


def update_contact(contacts, phone, new_data):
    for contact in contacts:
        if contact["phone"] == phone:
            for key, item in new_data.items():
                contact[key] = item

            return True

    return False


def search_by_full_name(contacts, first_name, last_name):
    all_contacts = []
    for contact in contacts:
        if contact["first_name"] == first_name and contact["last_name"] == last_name:
            all_contacts.append(contact)

    return all_contacts


def add_contacts(contacts, new_contacts):
    if search_by_phone(contacts, new_contacts["phone"]) == []:
        contacts.append(new_contacts)
        return True

    return False


def save_contacts(path, contacts):
    with open(path, 'w', encoding='utf-8') as json_f:
        json.dump(contacts, json_f, indent=2)


def load_contacts(path):
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            contacts = json.load(json_file)
        return contacts
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found in {path!r}")


def input_required(prompt):
    while True:
        answer = input(prompt)
        if len(answer.strip()) == 0:
            continue
        else:
            return answer.strip()


def validation_phone():
    while True:
        phone = input("Phone number: ").strip()
        if phone.startswith("+380") and len(phone) == 13 and phone[4:].isdigit():
            return phone
        else:
            print("Invalid phone number format. Use +380 followed by 9 digits.")


def display_contact(contact):
    print(
        f"First name: {contact['first_name']}\n"
        f"Last name:  {contact['last_name']}\n"
        f"Phone:  {contact['phone']}\n"
        f"City: {contact['city']}\n"
        f"State: {contact['state']}"
    )
