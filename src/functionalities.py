from utils import verify_email_address, verify_phone_number, checkcontacts


def add_contact(contacts):
    first_name = input("First Name:").strip()
    last_name = input("Last Name:").strip()
    mobile_number = input("Mobile Phone Number(XXX-XXX-XXXX):")
    home_number = input("Home Phone Number(XXX-XXX-XXXX):")
    email_address = input("Email Address:")
    address = input("Address:")

    if first_name == "":
        print("Contact can't be added due to no first name")
    if last_name == "":
        print("Contact can't be added due to no last name")
    if first_name != "" and last_name != "":
        check = checkcontacts(contacts, first_name, last_name)
        if check:
            print("Can't be added, as contact already exists!")
        else:
            checkm = verify_phone_number(mobile_number)
            if checkm or mobile_number == "":
                checkh = verify_phone_number(home_number)
                if checkh or home_number == "":
                    checkemail = verify_email_address(email_address)
                    if checkemail or email_address == "":
                        new_contact = {'first_name': first_name, 'last_name': last_name, 'mobile_number': mobile_number,
                                       'home_number': home_number, 'email_address': email_address, 'address': address}
                        contacts.append(new_contact)
                        contacts.sort(key = lambda contact: (contact['first_name'], contact['last_name']))

                        print("Congratulations, contact added!")
                    else:
                        print("!!Check email!!")
                else:
                    print("Chech home number")
            else:
                print("Check mobile phone number")


def search_for_contact(contacts):
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    contacts_found = []
    for contact in contacts:
        if first_name.lower() in contact['first_name'].lower() and last_name.lower() in contact['last_name'].lower():
            contacts_found.append(contact)
    print(f"Found {len(contacts_found)} matching contacts.")
    list_contacts(contacts_found)

 
def delete_contact(contacts):
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    flag = False
    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            flag = True
            confirmation = input("Are you sure you would like to delete this contact (y/n)? ")
            if confirmation == 'y':
                contacts.remove(contact)
                print("Contact deleted!")
            else:
                print("Contact not deleted!")
    if not flag:
        print("Contact not found!")


def list_contacts(contacts):
    i = 1
    for contact in contacts:
        print(f"{i}. {contact['first_name']} {contact['last_name']}")
        for key in contact:
            if key == 'first_name' or key == 'last_name':
                pass
            else:
                if contact[key] != "":
                    print(f"\t{key}: {contact[key]}")
        i += 1


def edit_contact(contacts):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    for contact in contacts:
        if first_name in contact['first_name'] and last_name in contact['last_name']:
            tobeedited = input("What do you want to edit?(first_name, last_name, mobile_number, home_number, email_address, address): ")
            new_value = input(f"What do you want to assign in {tobeedited}: ")
            contact[tobeedited] = new_value
            print("Contact edited!")
