import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the pass statement in Python?', 'Why is the pass statement useful in defining classes and functions?', 'Can the speaker provide an example of using the pass statement in a for loop?', 'What is an example of a lazy evaluation feature in Python?', 'How can the speaker exhaust a generator in Python?', 'What is the purpose of using the pass statement in Python?', "What is the purpose of using the 'pass' statement in Python?", "Can the speaker provide an example where the 'pass' statement is used to skip a specific condition in a loop?", "How can the 'pass' statement be helpful when dealing with breakpoints in a debugger?", "In what scenario do people sometimes use the 'pass' statement unnecessarily in Python code?", 'Is it true that all expressions in Python are valid statements?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the pass statement in Python?', 'Why is the pass statement useful in defining classes and functions?', 'Can the speaker provide an example of using the pass statement in a for loop?', 'What is an example of a lazy evaluation feature in Python?', 'How can the speaker exhaust a generator in Python?', 'What is the purpose of using the pass statement in Python?', "What is the purpose of using the 'pass' statement in Python?", "Can the speaker provide an example where the 'pass' statement is used to skip a specific condition in a loop?", "How can the 'pass' statement be helpful when dealing with breakpoints in a debugger?", "In what scenario do people sometimes use the 'pass' statement unnecessarily in Python code?", 'Is it true that all expressions in Python are valid statements?'], ['The pass statement in Python is a statement that does nothing. It is used as a placeholder when a statement is syntactically required but no action is needed.', 'The pass statement is useful in defining classes and functions when the syntax requires a block statement but no actual implementation is needed. It helps in making the syntax valid without adding any functionality.', "Sure, here's an example: If the speaker have a generator function that yields values and the speaker want to print a message in between each yield, the speaker can use pass to fill the block where the message is printed without adding any additional functionality. This allows the speaker to maintain the structure of the loop without needing to define unnecessary code.", 'Generators are lazy and do not evaluate their contents until looped over or called with next()', 'You can exhaust a generator by looping over it until there are no more values to yield', 'The pass statement is used when a statement is required syntactically but the speaker do not want any command or code to execute', "The 'pass' statement in Python is used as a placeholder when a statement is required syntactically but the speaker do not want any command or code to execute.", "Sure, the speaker can use the 'pass' statement to skip a specific condition in a loop. For example, if the speaker want to skip the number 15 in a loop, the speaker can use an if statement to check for 15 and then use 'pass' to do nothing for that iteration.", "When dealing with breakpoints in a debugger, adding a 'pass' statement at a specific point can help the debugger stop at a more logical place for debugging, especially when breakpoints seem to jump to unexpected locations.", "People sometimes use the 'pass' statement unnecessarily when defining classes, especially when there are no additional methods or code needed in the class definition. The 'pass' statement can be omitted in such cases without affecting the functionality of the code.", 'Mostly true. While an assignment expression may not be considered a valid statement, it can be placed in parentheses to make it valid. Expressions in Python, including string expressions, numbers, floats, and ellipsis, can be used as statements in various contexts.']))
    chat = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    chat_answer = chat.invoke(
        [
            langchain_core.messages.SystemMessage(content="You will be given question, reference answer pair and users answer. "
                                  'You have to decide if the answer is correct. '
                                  'If it is respond with a single work "Correct" otherwise return a hint about the answer. '),
            langchain_core.messages.SystemMessage(content='The question: ' + question + '\n'
                                  'The reference answer: ' + reference_answers[question]),
            langchain_core.messages.HumanMessage(
                content=answer
            )
        ]
    ).content
    if chat_answer.startswith("Correct"):
        return True
    return chat_answer
