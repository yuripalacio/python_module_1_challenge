def list_all(contact_list):
    print("\033[34m\nContact List:")

    print("ID | [F] Name | Phone | E-mail")
    for indice, contact in enumerate(contact_list):
        is_favorite = "[F] " if contact['is_favorite'] else ""
        print(f"{indice} | {is_favorite}{contact['name']} | {contact['phone']} | {contact['mail']}")

    return
