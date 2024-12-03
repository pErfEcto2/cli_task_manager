from task import Task
import json
from pathlib import Path


class TaskManager:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)
        self.tasks = dict()
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
        print("added")

    def delete(self, name: str) -> None:
        self.modified = True
        print("deleted")
        pass

    def change(self) -> None:
        self.modified = True
        print("changed")
        pass

    def find(self, keywords: list[str]) -> list[str]:
        return ["1 nastohe", "2 athodeu"]

    def done(self, name: str) -> None:
        self.modified = True
        print("mark as done")
        
    def write(self) -> None:
        if self.modified:
            self.modified = False
        print("written")


