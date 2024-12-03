class Task:
    def __init__(self, ID: int, title: str, desc: str, category: str, deadline: str, priority: int, status: bool):
        self.id = ID
        self.title = title
        self.desc = desc
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.status = status # false - not done; true - done
# there is no functions to get and change fields of an instance, because python doesnt have private fields and there wont be any logic when changing these fields


