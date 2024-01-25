def favorite_list(contact_list):
    print("\033[34m\nFavorite Contact List:")

    print("ID | Name | Phone | E-mail")
    for indice, contact in enumerate(contact_list):
        if contact['is_favorite']:
            print(f"{indice} | {contact['name']} | {contact['phone']} | {contact['mail']}")

    return
