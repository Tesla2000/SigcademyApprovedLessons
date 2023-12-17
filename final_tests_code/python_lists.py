def generate_questions() -> list[str]:
    return [
        "1. Create a list named 'fruits' containing the following fruits: 'apple', 'banana', 'cherry'.",
        "2. Append 'grape' to the 'fruits' list.",
        "3. Remove 'banana' from the 'fruits' list.",
        "4. Find index of 'cherry' in the 'fruits' list and store it in variable 'index'.",
        "5. Create a new list named 'numbers' with integers from 1 to 5 (inclusive).",
        "6. Find the length of the 'numbers' list and store it in a variable 'num_length'.",
        "7. Sort the 'numbers' list in ascending order.",
        "8. Reverse the 'numbers' list.",
        "9. Slice the 'fruits' list to get only the first two elements and store them in a new list named 'first_two_fruits'.",
    ]


def generate_answers(question: str, _, file: bytes) -> bool | str:
    try:
        if question.startswith("1"):
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if "fruits" not in locals() or type(locals()["fruits"]) is not list:
                return 'The list "fruits" is not defined or not a list.'
        elif question.startswith("2"):
            locals()["fruits"] = []
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if "grape" not in locals()["fruits"]:
                return 'The "grape" is not appended to the "fruits" list.'
        elif question.startswith("3"):
            locals()["fruits"] = ["banana", "limon"]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if "banana" in locals()["fruits"]:
                return 'The "banana" is not removed from the "fruits" list.'
            elif locals()["fruits"] != ["limon"]:
                return "There were other modifications to the list not included in the task."
        elif question.startswith("4"):
            locals()["fruits"] = ["apple", "banana", "cherry"]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["index"] != 2:
                return 'The "cherry" is not found in the "fruits" list.'
        elif question.startswith("5"):
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["numbers"] != list(range(1, 6)):
                return f'The "numbers" list does not contain the correct elements {locals()["numbers"]}.'
        elif question.startswith("6"):
            locals()["numbers"] = [1, 2, 3, 4, 5]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["num_length"] != 5:
                return 'The "num_length" variable does not have the correct value.'
        elif question.startswith("7"):
            locals()["numbers"] = [5, 2, 1, 4, 3]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["numbers"] != [1, 2, 3, 4, 5]:
                return 'The "numbers" list is not sorted in ascending order.'
        elif question.startswith("8"):
            locals()["numbers"] = [5, 2, 1, 4, 3]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["numbers"] != [5, 2, 1, 4, 3][::-1]:
                return 'The "numbers" list is not reversed correctly.'
        elif question.startswith("9"):
            locals()["fruits"] = ["apple", "banana", "cherry"]
            exec(compile(file, "<string>", "exec"), globals(), locals())
            if locals()["first_two_fruits"] != ["apple", "banana"]:
                return 'The "first_two_fruits" list is not sliced correctly.'
        return True
    except Exception as e:
        return str(e)
