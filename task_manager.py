import json
from pathlib import Path
import lib


class TaskManager:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)
        self.tasks = list(dict())
        self.modified: bool = False

        if not self.path.is_file():
            if self.path.is_dir():
                raise ValueError("wrong path to file")
            
            self.path.touch()
        else:
            with open(self.path) as f:
                if len(f.read()) != 0:
                    # reading file moves cursor 
                    # seek(0) = set cursor at the beginning
                    f.seek(0)
                    self.tasks = json.load(f)

        if len(self.tasks) != 0:
            self.first_avail_id: int = max([x.get("id") for x in self.tasks]) + 1
        else:
            self.first_avail_id = 1

    def add(self) -> None:
        """
        adds a new task
        """
        self.modified = True
        
        title: str = " ".join(lib.sanitized_input(r"^\w.*$", "title: "))
        desc: str = " ".join(lib.sanitized_input(promt="decsription: "))
        category: str = " ".join(lib.sanitized_input(promt="category: "))
        # it's simplified version to get date from an user 
        # it has flaw: user may input any digits as date
        deadline: str = "".join(lib.sanitized_input(r"\d{2}-\d{2}-\d{4}", 
                                                    "deadline (dd-mm-yyyy): "))
        priority: str = lib.sanitized_input("(high|medium|low)", 
                                            "priority (high, medium or low): ")[0]
        
        self.tasks.append({'id': self.first_avail_id, 'title': title, 
                           'desc': desc, 'category': category, 
                           'deadline': deadline, 'priority': priority, 
                           'is_done': False})
        self.first_avail_id += 1

    def delete(self, id_or_name: str) -> None:
        """
        deletes a task by its id or name
        """
        # deleting by category will delete tasks which isnt done as well
        # so i slightly changed the behavior
        self.modified = True
        try:
            id = int(id_or_name)
            for i, task in enumerate(self.tasks):
                if task.get("id") == id:
                    self.tasks.pop(i)
                    break
            else:
                print("nothing to delete")
        except ValueError:
            name = id_or_name
            for i, task in enumerate(self.tasks):
                if task.get("title") == name:
                    self.tasks.pop(i)
                    break
            else:
                print("nothing to delete")

    def change(self, id_or_name: str) -> None:
        """
        changes task info
        """
        task_index: int = -1
        try:
            id = int(id_or_name)
            for i, task in enumerate(self.tasks):
                if task.get("id") == id:
                    task_index = i
                    break
        except ValueError:
            name = id_or_name
            for i, task in enumerate(self.tasks):
                if task.get("title") == name:
                    task_index = i
                    break
        
        if task_index == -1:
            print("no such task")
            return

        print("changing mode")

        self.modified = True

        while True:
            user_input: list[str] = lib.sanitized_input(r"^(h|b|t|d|c|l|p|s)$", 
                                                        "command (h for help): ")

            match user_input[0]:
                case "h":
                    print("""h - print this message
b - go back
t - change title
d - change description
c - change category
l - change deadline
p - change priority
s - show current task""")
                
                case "b":
                    print("normal mode")
                    return
                
                case "t":
                    self.tasks[task_index]["title"] = " ".join(lib.sanitized_input(r"^\w.*$", 
                                                                                   "title: "))

                case "d":
                    self.tasks[task_index]["desc"] = " ".join(lib.sanitized_input(promt="description: "))

                case "c":
                    self.tasks[task_index]["category"] = " ".join(lib.sanitized_input("category: "))

                case "l":
                    self.tasks[task_index]["deadline"] = " ".join(lib.sanitized_input(r"\d{2}-\d{2}-\d{4}", 
                                                                                      "deadline (dd-mm-yyyy): "))

                case "p":
                    self.tasks[task_index]["priority"] = lib.sanitized_input("(high|medium|low)", 
                                                                             "priority (high, medium or low): ")[0]
    
                case "s":
                    lib.print_tasks([self.tasks[task_index]])

    def find(self, keywords: list[str]) -> list[dict]:
        """
        finds and returns tasks with given keywords
        """
        res : list[dict] = list(dict())
        
        keywords = [x.lower() for x in keywords]

        # i could used nltk library to remove endings of words, 
        # but for the sake of simplicity i didnt
        for task in self.tasks:
            for keyword in keywords:
                if keyword in task.get("title").lower() or \
                   keyword in task.get("desc").lower() or \
                   keyword in task.get("category").lower():
                       res.append(task)

        return res

    def show(self, category: str | None) -> list[dict]:
        """
        returns all tasks or with given category
        """
        res: list[dict] = list(dict())
        if category is None:
            res = self.tasks
        else:
            for task in self.tasks:
                if category.lower() in task.get("category").lower():
                    res.append(task)
        return res

    def done(self, id_or_name: str) -> None:
        """
        marks a task as done
        """
        self.modified = True
        try:
            id = int(id_or_name)
            for i, task in enumerate(self.tasks):
                if task.get("id") == id:
                    self.tasks[i]["is_done"] = True
                    break
        except ValueError:
            name = id_or_name
            for i, task in enumerate(self.tasks):
                if task.get("title") == name:
                    self.tasks[i]["is_done"] = True
                    break
        
    def write(self) -> None:
        """
        writes tasks to a file
        """
        if not self.modified:
            print("already up to date")
            return

        self.modified = False
        with open(self.path, "w") as f:
            json.dump(self.tasks, f)

        print("written to file")


