import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the bug demonstrated in the Python program?', 'How does Python handle joining two string literals together?', 'What is an example of a common scenario where this bug can occur in Python code?', 'Is the behavior of joining string literals inherited from C in Python?', 'What is the problem with implicit joining in code?', 'What are some benefits of using winter plugins to catch foot gun errors?', 'What are your thoughts on the use of implicit joining in code?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the bug demonstrated in the Python program?', 'How does Python handle joining two string literals together?', 'What is an example of a common scenario where this bug can occur in Python code?', 'Is the behavior of joining string literals inherited from C in Python?', 'What is the problem with implicit joining in code?', 'What are some benefits of using winter plugins to catch foot gun errors?', 'What are your thoughts on the use of implicit joining in code?'], ['The bug is that when two string literals are placed next to each other without a comma in between, Python automatically joins them together, causing unexpected behavior.', 'Python joins two string literals together automatically when they are placed next to each other without a comma, creating a single string.', 'A common scenario is in setup.py files where developers may forget to include commas between package names or version numbers, leading to unintended string concatenation.', 'Yes, the behavior of joining string literals without an operator is inherited from C in Python.', 'Implicit joining can lead to errors, such as breaking a list of strings if a comma is forgotten, making it a problem in code.', 'Winter plugins can catch foot gun errors and report them as errors, helping to avoid implicit joining issues and improve code readability.', 'There are arguments for and against the use of implicit joining in code. While it may make code more readable in some cases, it can also lead to problems like breaking lists of strings if a comma is forgotten.']))
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
