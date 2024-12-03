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
        self.modified = True
        self.tasks.append({'id': self.first_avail_id, 'title': 'Изучить основы FastAPI', 'desc': 'Пройти документацию по FastAPI и создать простой проект', 'category': 'обучение', 'deadline': '2024-11-30', 'priority': 1, 'status': False})
        self.first_avail_id += 1
        print("added")

    def delete(self, id_or_name: str) -> None:
        self.modified = True
        print("deleted")
        pass

    def change(self, id_or_name: str) -> None:
        self.modified = True
        print("changed")
        pass

    def find(self, keywords: list[str]) -> list[str]:
        return ["1 nastohe", "2 athodeu"]

    def show(self, keywords: str | None) -> list[dict]:
        return self.tasks

    def done(self, id_or_name: str) -> None:
        self.modified = True
        print("mark as done")
        
    def write(self) -> None:
        if not self.modified:
            return

        self.modified = False
        with open(self.path, "w") as f:
            json.dump(self.tasks, f)

        print("written to file")


