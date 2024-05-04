import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['How do the speaker implement the __getitem__ method in a generic sequence-like class to handle slices and integers?', 'What is the purpose of using type annotations in Python?', "What is the 'Union' type in Python and how is it used?", 'How can overloading be simulated in Python for type checking purposes?', 'What are some typing related tools for Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['How do the speaker implement the __getitem__ method in a generic sequence-like class to handle slices and integers?', 'What is the purpose of using type annotations in Python?', "What is the 'Union' type in Python and how is it used?", 'How can overloading be simulated in Python for type checking purposes?', 'What are some typing related tools for Python?'], ['To implement the __getitem__ method in a generic sequence-like class to handle slices and integers, the speaker can use the following approach:\n\n1. Define a class that takes in a sequence as input.\n2. Implement the __getitem__ method in the class.\n3. Check if the input index is a slice using isinstance(idx, slice). If it is a slice, return a new instance of the class with the sliced sequence.\n4. If the input index is not a slice, assume it is an integer and return the individual element at that index.\n5. Use type annotations to make the class generic and handle different types of sequences.\n6. Import the necessary typing modules like TypeVar and Sequence.\n7. Define a TypeVar for the generic type variable.\n8. Use Sequence[T] to specify that the sequence can be a list, tuple, or similar type.\n\nBy following these steps, the speaker can implement the __getitem__ method in a generic sequence-like class to handle both slices and integers.', 'Type annotations in Python help provide type hints to the Python interpreter, allowing for static type checking and improved code readability and maintainability.', "'Union' type in Python is used to define a variable that can hold values of multiple types. It is used to specify that a variable can be of one type or another. For example, Union[int, str] would indicate that the variable can be either an integer or a string.", "Overloading in Python can be simulated for type checking purposes by using the 'overload' decorator from the 'typing' module. By defining multiple overloads of a function with different parameter types and return types, the type checker can determine the appropriate function to call based on the types passed into it.", 'Some typing related tools for Python include MyPy, Pyright, Pyre, PyType, and Pydantic.']))
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
