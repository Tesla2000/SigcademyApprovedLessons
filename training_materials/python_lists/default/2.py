def generate_questions() -> list[str]:
    return [
        "2. Append 'grape' to the 'fruits' list.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        locals()["fruits"] = []
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if "grape" not in locals()["fruits"]:
            return 'The "grape" is not appended to the "fruits" list.'
        return True
    except Exception as e:
        return str(e)
