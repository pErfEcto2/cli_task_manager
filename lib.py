import re


def sanitized_input(pattern: str, promt: str = "") -> list[str]:
    """
    returns a list of sanitized strings only when input matches regex pattern
    """
    while re.match(pattern, inp := input(promt).strip()) is None:
        print("invalid input")

    return [x.strip() for x in inp.split(" ")]

def print_tasks(tasks: list[dict]) -> None:
    if len(tasks) == 0:
        print("no tasks")
        return

    for task in tasks:
        tmp = task.get("priority")
        if tmp == 1:
            priority = "High"
        elif tmp == 2:
            priority = "Medium"
        else:
            priority = "Low"

        print(f"""{task.get("id")}: {task.get("title")} ({'done' if task.get("is_done") else 'not done'})\nDescription: {task.get("desc")}
Category: {task.get("category")}\nDeadline: {task.get("deadline")}
Priority: {priority}\n""")

