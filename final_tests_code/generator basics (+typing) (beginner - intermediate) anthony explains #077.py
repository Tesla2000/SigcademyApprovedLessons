import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What keyword makes a function a generator in Python?', 'How does a generator function differ from a normal function?', 'What happens when the speaker reach the end of a generator in Python?', 'How can the speaker emulate a for loop using a while loop with a generator in Python?', 'What does the yield from syntax do in Python 3?', 'What is the purpose of implementing a custom range function in Python without using yield from or calling range?', 'How is the custom range function implemented without using yield from or range in Python?', 'How can the speaker type annotate a generator function in Python using the typing module?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What keyword makes a function a generator in Python?', 'How does a generator function differ from a normal function?', 'What happens when the speaker reach the end of a generator in Python?', 'How can the speaker emulate a for loop using a while loop with a generator in Python?', 'What does the yield from syntax do in Python 3?', 'What is the purpose of implementing a custom range function in Python without using yield from or calling range?', 'How is the custom range function implemented without using yield from or range in Python?', 'How can the speaker type annotate a generator function in Python using the typing module?'], ['The yield keyword.', 'A generator function uses the yield keyword to yield values one at a time, allowing iteration over the values.', 'When the speaker reach the end of a generator and try to call next on it, it will raise a StopIteration exception.', 'You can assign the generator to a variable, then use a while loop with next to iterate over the values until a StopIteration exception is raised.', 'The yield from syntax allows a generator to yield values from another iterable, incrementally yielding values from that iterable.', 'The purpose is to replicate the functionality of the built-in range function with just one argument, such that calling the custom range function with an argument like 10 would yield values from 0 to 9.', 'The custom range function is implemented using a while loop where a value is initialized to zero and then incremented in each iteration until it reaches the specified limit. The function yields the value in each iteration to generate the range of values.', "To type annotate a generator function in Python, the speaker can import the generator type from the typing module and specify the type parameters. The most important type parameter is the yield type, while the send type and return type can be set to None for simple generator functions. The typical annotation pattern is 'Generator[some_type, None, None]' for the yield type."]))
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
