from task import Task
import json
from pathlib import Path


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
        # TODO
        self.modified = True
        self.tasks.append({'id': self.first_avail_id, 'title': 'Изучить основы FastAPI', 'desc': 'Пройти документацию по FastAPI и создать простой проект', 'category': 'обучение', 'deadline': '2024-11-30', 'priority': 1, 'is_done': False})
        self.first_avail_id += 1

    def delete(self, id_or_name: str) -> None:
        self.modified = True
        if id_or_name.isdigit():
            id = int(id_or_name)
            for i, task in enumerate(self.tasks):
                if task.get("id") == id:
                    self.tasks.pop(i)
                    break
            else:
                print("nothing to delete")
        else:
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
        # TODO
        return self.tasks

    def show(self, category: str | None) -> list[dict]:
        # TODO
        return self.tasks

    def done(self, id_or_name: str) -> None:
        # TODO
        self.modified = True
        print("mark as done")
        
    def write(self) -> None:
        if not self.modified:
            print("already wrote")
            return

        self.modified = False
        with open(self.path, "w") as f:
            json.dump(self.tasks, f)

        print("written to file")


