def generate_questions() -> list[str]:
    return [
        "7. Sort the 'numbers' list in ascending order.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        locals()["numbers"] = [5, 2, 1, 4, 3]
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if locals()["numbers"] != [1, 2, 3, 4, 5]:
            return 'The "numbers" list is not sorted in ascending order.'
        return True
    except Exception as e:
        return str(e)
