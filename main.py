# here wont be many comments because the projech isnt that hard nor complex

from task_manager import TaskManager
import lib


t = TaskManager()

while True:
    user_input: list[str] = lib.sanitized_input(r"^(h|q|w|a|d\s.+|c\s.+|o\s.+|s(\s.+)?|f\s.+)$", 
                                                "command (h for help): ")

    match user_input[0]:
        case "h":
            print("""h - print this message
q - quit 
w - write changes to file 
a - add a new task 
d ID/name - delete a task 
c ID/name - change a task 
o ID/name - mark a task as done 
s [CATEGORY] - show all tasks or only with given category (if several categories given only first is used)
f [keyword1 keyword2 ...] - find tasks using keywords""")
        
        case "q":
            if t.modified:
                if lib.sanitized_input("^[yn]$", 
                                       "save changes before exiting(y/n)?")[0] == "y":
                    t.write()
            print("bye")
            exit()
        
        case "a":
            t.add()
        
        case "d":
            t.delete(" ".join(user_input[1:]))
        
        case "c":
            t.change(user_input[1])

        case "o":
            t.done(user_input[1])

        case "s":
            lib.print_tasks(t.show(user_input[1] if len(user_input) > 1 else None))

        case "f":
            lib.print_tasks(t.find(user_input[1:]))
        
        case "w":
            t.write()

        case _:
            continue


