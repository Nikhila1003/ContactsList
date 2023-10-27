def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def verify_phone_number(mobile_number):
    if len(mobile_number) != 12:
        return False
    
    mbl_domain = mobile_number.split("-")
    first_domain = "".join(mbl_domain[0])
    mid_domain = "".join(mbl_domain[1])
    last_domain = "".join(mbl_domain[-1])
    print(first_domain, mid_domain, last_domain)
    if len(first_domain) != 3:
        return False
    if len(mid_domain) != 3:
        return False
    if len(last_domain) != 4:
        return False
    return True


def checkcontacts(contacts, first_name, last_name):
    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            return True
    return False
