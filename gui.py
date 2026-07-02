import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo box", key="todo")
add_button = sg.Button("Add fuck you")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add fuck you":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos_arg=todos)
        case sg.WIN_CLOSED:
            break

window.close()