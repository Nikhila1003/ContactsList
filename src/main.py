from json_crud import read_contacts, write_contacts
from functionalities import *


CONTACT_FILE_PATH = "data/contacts.json"

def main(contacts_path):
    print("Welcome to your contact list!\nThe following is a list of useable commands:")
    print("\"add:\" Adds a contact.")
    print("\"delete:\" Deletes a contact.")
    print("\"edit:\" Edits a contact.")
    print("\"list:\" Lists all contacts.")
    print("\"search:\" Searches for a contact by name.")
    print("\"q:\" Quits the program and saves the contact list.")

    user_cmd = ""
    contacts = read_contacts(contacts_path)

    while user_cmd != "q":
        user_cmd = input("Type a command: ")
        if user_cmd == "add":
            add_contact(contacts)
        elif user_cmd == "edit":
            edit_contact(contacts)
        elif user_cmd == "delete":
            delete_contact(contacts)
        elif user_cmd == "list":
            list_contacts(contacts)
        elif user_cmd == "search":
            search_for_contact(contacts)
        elif user_cmd == "q":
            pass
        else:
            print("Unknown command")

    else:
        write_contacts(contacts_path, contacts)
        print("Contacts were saved successfully.")


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)

