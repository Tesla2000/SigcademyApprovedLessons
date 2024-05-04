import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of the function in the code example?', 'What surprised the speaker when they first learned about catching exceptions in Python?', 'How did the speaker resolve the type error when type annotating the function?', 'What is an ellipsis in Python?', 'What is a tuple in Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of the function in the code example?', 'What surprised the speaker when they first learned about catching exceptions in Python?', 'How did the speaker resolve the type error when type annotating the function?', 'What is an ellipsis in Python?', 'What is a tuple in Python?'], ['The function is designed to catch specific types of exceptions that are raised within the try block and handle them accordingly.', 'The speaker was surprised that the speaker can parameterize the types of exceptions to catch in Python.', 'The speaker resolved the type error by using a union type annotation that allows for either a tuple of types or an individual type to be accepted as the exception to catch.', 'An ellipsis (...) is a built-in object in Python that represents a placeholder or a marker for unfinished code or data structures.', 'A tuple is an immutable collection of elements in Python, enclosed in parentheses and separated by commas.']))
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
