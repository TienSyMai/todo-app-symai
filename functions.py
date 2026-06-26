# Chào Mai Tiến SỸ tôi là trợ lý của bạn

FilePath = "extraFile/todos.txt"

def get_todos(filepath=FilePath):
    """read the txt file and return the todos list"""

    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath=FilePath):
    """write infot to file todos ok"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)