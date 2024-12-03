from task_manager import TaskManager
import lib

t = TaskManager()

user_input : list[str] = [""]

while True:
    user_input = lib.sanitized_input("^[hqwadcosf].*", "command(write h for help): ")

    match user_input[0]:
        case "h":
            print("""h - print this message
q - quit 
w - write changes to file 
a - add a new task 
d ID/name - delete a task 
c ID/name - change a task 
o ID/name - mark a task as done 
s [CATEGORY] - show all tasks or only with given category
f [keyword1 keyword2 ...] - find tasks using keywords""")
        
        case "q":
            if t.modified:
                if lib.sanitized_input("^[yn]$", "save changes before exiting(y/n)?")[0] == "y":
                    t.write()
            print("bye")
            exit()
        
        case "a":
            t.add()
        
        case "d":
            if len(user_input) != 2:
                print("invalid input; write a name or an ID of a task to delete it")
                continue
            t.delete(user_input[1])
        
        case "c":
            if len(user_input) != 2:
                print("invalid input; write a name or an ID of a task to change it")
                continue
            t.change(user_input[1])

        case "o":
            if len(user_input) != 2:
                print("invalid input; write a name or an ID of a task to mark it as done")
                continue
            t.done(user_input[1])

        case "s":
            print(t.show(user_input[1:] if len(user_input) > 1 else None))

        case "f":
            if len(user_input) == 1:
                print("invalid input; write at least one keyword")
                continue
            print(t.find(user_input[1:]))
        
        case _:
            continue



