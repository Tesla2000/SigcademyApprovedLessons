def generate_questions() -> list[str]:
    return [
        "4. Find index of 'cherry' in the 'fruits' list and store it in variable 'index'.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        locals()["fruits"] = ["apple", "banana", "cherry"]
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if locals()["index"] != 2:
            return 'The "cherry" is not found in the "fruits" list.'
        return True
    except Exception as e:
        return str(e)
