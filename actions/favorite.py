from .list import list_all

def favorite(contact_list):
    list_all(contact_list)

    print("\033[34m\nFavorite/Unfavorite a contact:")
    contact_index = input("Enter the ID contact you want to favorite/unfavorite: ")

    if not contact_index.isdigit():
        print("\033[31mO ID informádo não existe\033[0m")
        return

    index = int(contact_index)

    if index < 0 or index >= len(contact_list):
        print("\033[31mO ID informádo não existe\033[0m")
        return

    contact_list[index]["is_favorite"] = not contact_list[index]["is_favorite"]

    print("\nContato atualizado com sucesso!")

    return
