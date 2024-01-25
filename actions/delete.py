from .list import list_all

def delete(contact_list):
    list_all(contact_list)

    contact_index = input("Enter the ID contact you want to delete: ")

    if not contact_index.isdigit():
        print("\033[31mThe provided ID does not exist\033[0m")
        return

    index = int(contact_index)

    if index < 0 or index >= len(contact_list):
        print("\033[31mThe provided ID does not exist\033[0m")
        return

    del contact_list[index]

    print("\nContact deleted succesfully!")

    return
