def generate_questions() -> list[str]:
    return [
        "1. Create a list named 'fruits' containing the following fruits: 'apple', 'banana', 'cherry'.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if "fruits" not in locals() or type(locals()["fruits"]) is not list:
            return 'The list "fruits" is not defined or not a list.'
        return True
    except Exception as e:
        return str(e)
