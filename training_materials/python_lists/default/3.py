def generate_questions() -> list[str]:
    return [
        "3. Remove 'banana' from the 'fruits' list.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        locals()["fruits"] = ["banana", "limon"]
        exec(compile(file, "<string>", "exec"), globals(), locals())
        if "banana" in locals()["fruits"]:
            return 'The "banana" is not removed from the "fruits" list.'
        elif locals()["fruits"] != ["limon"]:
            return "There were other modifications to the list not included in the task."
        return True
    except Exception as e:
        return str(e)
