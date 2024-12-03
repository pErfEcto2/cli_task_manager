import re


def sanitized_input(pattern: str, promt: str = "") -> list[str]:
    """
    returns a list of sanitized strings only when input matches regex pattern
    """
    while re.match(pattern, inp := input(promt).strip()) is None:
        print("invalid input")

    return [x.strip() for x in inp.split(" ")]


