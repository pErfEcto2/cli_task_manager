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
                    f.seek(0) # reading file moves cursor; seek(0) = set cursor an the beginning
                    self.tasks = json.load(f)

        if len(self.tasks) != 0:
            self.first_avail_id: int = max([x.get("id") for x in self.tasks]) + 1
        else:
            self.first_avail_id = 1

    def add(self) -> None:
        self.modified = True
        title: str = " ".join(lib.sanitized_input(r"^\w.*$", "title: "))
        desc: str = " ".join(lib.sanitized_input(promt="decsription: "))
        category: str = " ".join(lib.sanitized_input(promt="category: "))
        deadline: str = "".join(lib.sanitized_input(r"\d{2}-\d{2}-\d{4}", "deadline (dd-mm-yyyy): "))
        priority: str = lib.sanitized_input("(high|medium|low)", "priority (high, medium or low): ")[0]
        self.tasks.append({'id': self.first_avail_id, 'title': title, 'desc': desc, 'category': category, 
                           'deadline': deadline, 'priority': priority, 'is_done': False})
        self.first_avail_id += 1

    def delete(self, id_or_name: str) -> None:
        # deleting by category will delete tasks which isnt done, so i slightly changed it
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
        # TODO
        self.modified = True
        print("changed")

    def find(self, keywords: list[str]) -> list[dict]:
        res : list[dict] = list(dict())
        
        keywords = [x.lower() for x in keywords]

        for task in self.tasks:
            for keyword in keywords:
                if keyword in task.get("title").lower() or keyword in task.get("desc").lower() or \
                   keyword in task.get("category").lower():
                       res.append(task)

        return res

    def show(self, category: str | None) -> list[dict]:
        res: list[dict] = list(dict())
        if category is None:
            res = self.tasks
        else:
            for task in self.tasks:
                if category.lower() in task.get("category").lower():
                    res.append(task)
        return res

    def done(self, id_or_name: str) -> None:
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
        if not self.modified:
            print("already up to date")
            return

        self.modified = False
        with open(self.path, "w") as f:
            json.dump(self.tasks, f)

        print("written to file")


