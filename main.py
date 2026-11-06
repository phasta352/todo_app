todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                    print(f"{index}.{item}")
        case "edit":
            number = int(input("Enter a todo number to edit: "))
            todos[number - 1] = input("Enter the new item text: ")
        case "exit":
            break
        case _:
            print("Invalid input")

print("Bye!")
