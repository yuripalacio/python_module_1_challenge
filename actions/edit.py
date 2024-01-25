from .list import list_all

def edit(contact_list):
    list_all(contact_list)

    print("\033[34m\nContact Update:")
    contact_index = input("Enter the ID contact you want to update: ")

    if not contact_index.isdigit():
        print("\033[31mThe provided ID does not exist\033[0m")
        return
    
    index = int(contact_index)

    if index < 0 or index >= len(contact_list):
        print("\033[31mThe provided ID does not exist\033[0m")
        return

    print("Update the data (If no value is passed, the current value will be retained).")
    name = input("Enter the new name: ")
    phone = input("Enter the new phone: ")
    mail = input("Enter the new e-mail: ")

    if name:
        contact_list[index]["name"] = name
    if phone:
        contact_list[index]["phone"] = phone
    if mail:
        contact_list[index]["mail"] = mail

    print("\nContact update succesfully!")

    return


