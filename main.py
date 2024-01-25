from actions.insert import insert
from actions.finish import finish
from actions.list import list_all
from actions.edit import edit
from actions.favorite import favorite
from actions.favorite_list import favorite_list
from actions.delete import delete

contact_list = [{
    "name": "Fake Contact",
    "phone": "99999999",
    "mail": "fake@email.com",
    "is_favorite": True
}]

actions = [
  {
    "text": "Add a new contact",
    "function": lambda: insert(contact_list)
  },
  {
    "text": "View contact list",
    "function": lambda: list_all(contact_list)
  },
  {
    "text": "Update contact",
    "function": lambda: edit(contact_list)
  },
  {
    "text": "Mark/unmark contact as favorite",
    "function": lambda: favorite(contact_list)
  },
  {
    "text": "View favorite contact list",
    "function": lambda: favorite_list(contact_list)
  },
  {
    "text": "Delete a contact",
    "function": lambda: delete(contact_list)
  },
  {
    "text": "Exit",
    "function": lambda: finish()
  }
]

while True:
    print("\033[0m\nChose an option:")

    for index, action in enumerate(actions):
        print(f"{index}: {action['text']}")

    action = input("\nEnter your choice: ")

    if not action.isdigit():
        print("\033[31mThe chosen option is invalid\033[0m")
        continue

    try:
        index = int(action)
        actions[index]["function"]()
    except IndexError:
        print("\033[31mThe chosen option is invalid\033[0m")
