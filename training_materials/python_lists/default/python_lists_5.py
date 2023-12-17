def generate_questions() -> list[str]:
    return [
        "5. Create a new list named 'numbers' with integers from 1 to 5 (inclusive).",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if locals()["numbers"] != list(range(1, 6)):
            return f'The "numbers" list does not contain the correct elements {locals()["numbers"]}.'
        return True
    except Exception as e:
        return str(e)
