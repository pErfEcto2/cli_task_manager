import re


def sanitized_input(pattern: str = ".*", promt: str = "") -> list[str]:
    """
    returns a list of stripped strings only when input matches regex pattern
    otherwise asks for in input again
    """
    while re.match(pattern, inp := input(promt).strip()) is None:
        print("invalid input")

    return [x.strip() for x in inp.split(" ")]

def print_tasks(tasks: list[dict]) -> None:
    """
    pretty print for tasks
    """
    if len(tasks) == 0:
        print("no tasks")
        return

    for task in tasks:
        print(f"""{task.get("id")}: {task.get("title")} ({'done' if task.get("is_done") else 'not done'})\ndescription: {task.get("desc")}
category: {task.get("category")}\ndeadline: {task.get("deadline")}
priority: {task.get("priority")}\n""")

