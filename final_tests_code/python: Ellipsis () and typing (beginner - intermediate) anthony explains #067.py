import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is ellipsis in Python?', 'How is ellipsis represented in Python?', 'What are the uses of ellipsis in typing, particularly in Python 3?', 'What is the use of ellipses in type annotations in mypy?', 'How are ellipses used for placeholder variables in callable typing?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is ellipsis in Python?', 'How is ellipsis represented in Python?', 'What are the uses of ellipsis in typing, particularly in Python 3?', 'What is the use of ellipses in type annotations in mypy?', 'How are ellipses used for placeholder variables in callable typing?'], ["Ellipsis is a built-in singleton in Python that serves as a placeholder value similar to None, True, and False. It can be accessed using the '...' syntax in Python 3.", "Ellipsis is represented by the '...' syntax in Python 3. It can also be accessed using the 'Ellipsis' name or through the '...' syntax in Python 2 in specific cases.", 'In typing, ellipsis is used in tuples to represent either a tuple with multiple variable types or a homogeneous tuple with a variable length. It serves as a way to annotate multiple return values or composite keys in Python type annotations.', 'Ellipses in type annotations in mypy are used to indicate a homogeneous sequence of elements with a variable length. For example, when defining a tuple of integers with variable length, the speaker can use ellipses to specify that the tuple contains integers of any length.', 'In callable typing, ellipses are used as a placeholder for arguments in a function signature. This indicates that any set of arguments can fit in that position. For example, when defining a callable that takes any number of arguments and returns a tuple of any length, the speaker can use ellipses to specify the variable argument signature.']))
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
