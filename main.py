# here wont be many comments because the projech isnt that hard nor big


from task_manager import TaskManager
import lib


t = TaskManager()

user_input : list[str] = [""]

while True:
    user_input = lib.sanitized_input("^(h|q|w|a|d\s.+|c\s.+|o\s.+|s(\s.+)?|f\s.+)$", "command (h for help): ")

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
                if lib.sanitized_input("^[yn]$", "save changes before exiting(y/n)?")[0] == "y":
                    t.write()
            print("bye")
            exit()
        
        case "a":
            t.add()
        
        case "d":
            t.delete(user_input[1])
        
        case "c":
            t.change(user_input[1])

        case "o":
            t.done(user_input[1])

        case "s":
            data = t.show(user_input[1] if len(user_input) > 1 else None)
            match len(user_input):
                case 0:
                    print("no tasks yet")
                case 1:
                    print("all tasks:")
                    for task in data:
                        print(f"{task.get("id")} {task.get("title")}")
                case _:
                    print("found taskn:")
                    for task in data:
                        print(task) # add pretty print for tasks

        case "f":
            print(t.find(user_input[1:]))
        
        case "w":
            t.write()

        case _:
            continue



