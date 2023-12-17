def generate_questions() -> list[str]:
    return [
        "6. Find the length of the 'numbers' list and store it in a variable 'num_length'.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        locals()["numbers"] = [1, 2, 3, 4, 5]
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if locals()["num_length"] != 5:
            return 'The "num_length" variable does not have the correct value.'
        return True
    except Exception as e:
        return str(e)
