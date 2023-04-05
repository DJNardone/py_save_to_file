class PersonalAssistant:
    def __init__(self, todos):
        self.todos = todos

    def get_contact(self, name):
      if name in self.contacts:
        return self.contacts[name]
      else:
        return "Name is not in Contacts"

    def add_todo(self, new_item):
      self.todos.append(new_item)

    def remove_todo(self, todo_item):
      if todo_item in self.todos:
        # Get the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
      else:
        print("Todo is not in list!")

    def get_todos(self):
      return self.todos

    def get_birthday(self, name):
      if name == "Ash":
        return("Birthday is 1/1/80")
      elif name == "Mom":
        return("Birthday is 3/3/44")
      elif name == "Monk":
        return("Birthday is 7/7/99")
      else:
        return("Can't find a birthday for this person.")
  
#assistant = PersonalAssistant()

#assistant.add_todo("Pick up groceries")
#assistant.add_todo("Buy dog food")
#print(assistant.get_todo())
#assistant.remove_todo("Buy dog food")
#print(assistant.get_todo())

#print(assistant.get_contact("Chelsea"))

#print(assistant.get_birthday("Ash"))
