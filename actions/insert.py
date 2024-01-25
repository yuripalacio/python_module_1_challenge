def insert(contact_list):
    print("\033[34m\nFill in the details of the new contact")
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    mail = input("Enter the e-mail: ")
    is_favorite = input("Mark contact as favorite? [Y/N] ").upper()
    contact_list.append({
        "name": name,
        "phone": phone,
        "mail": mail,
        "is_favorite": is_favorite == 'Y'
    })
    print(f"Contact {name} add succesfully!")

    return
