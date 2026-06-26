

import functions

while True:
    user_action = input("Type add [your todo], show, exist [number], edit [number], complete [number], task left: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        #new_todos = [item.strip() for item in todos]

        for index, item in enumerate(todos):
            item = item.strip()
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            
            todos = functions.get_todos()

            if len(todos) >= number + 1:
                todos[number] = input("Enter a new todo: ") + "\n"
                functions.write_todos(todos)
            else:
                print("Erorr: May be you enter the wrong number, now try 'edit' command again")
                continue
        except ValueError:
            print("Erorr: May be you enter the wrong number your number may have letters, now try 'edit' command again")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            
            todos = functions.get_todos()
            
            to_do_to_remove = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todos)
            print(f"Congratulations! You have completed '{to_do_to_remove}'")
        except IndexError:
            print("There is no such number")
            continue
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("task left"):
        print(f"You have {len(functions.get_todos())} tasks left")

    elif user_action.startswith("exist"):
        break
    else:
        print("Your command is not valid")

print("Your todo list have updated: thank for using the app")
