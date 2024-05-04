import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is a Python decorator?', 'How is a decorator applied to a function in Python?', 'What is the purpose of using a decorator in Python?', 'What is the purpose of the decorator in the provided code snippet?', 'What issue is identified with the initial decorator implementation?', 'How can the issue of losing the original function attributes be addressed using the functools module?', 'What is a decorator Factory in Python?', "What is the purpose of the 'deck2' decorator function?", "What are the variables used in the 'deck2' decorator function?", "How is the 'deck2' decorator function called and used in the code snippet?", 'What are two common decorators in Python?', 'What does the property decorator do?', 'What does the classmethod decorator do?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is a Python decorator?', 'How is a decorator applied to a function in Python?', 'What is the purpose of using a decorator in Python?', 'What is the purpose of the decorator in the provided code snippet?', 'What issue is identified with the initial decorator implementation?', 'How can the issue of losing the original function attributes be addressed using the functools module?', 'What is a decorator Factory in Python?', "What is the purpose of the 'deck2' decorator function?", "What are the variables used in the 'deck2' decorator function?", "How is the 'deck2' decorator function called and used in the code snippet?", 'What are two common decorators in Python?', 'What does the property decorator do?', 'What does the classmethod decorator do?'], ['A Python decorator is a design pattern that allows the speaker to add new functionality to an existing function or method without changing its structure. It is denoted by the @ symbol followed by the decorator function name.', 'A decorator is applied to a function in Python by placing the @ symbol followed by the decorator function name on the line directly above the function definition. This syntax sugar passes the function to the decorator function for modification or enhancement.', 'The purpose of using a decorator in Python is to extend or modify the behavior of functions or methods without altering their original code. Decorators provide a way to add reusable functionality to multiple functions or methods in a concise and clean manner.', 'The purpose of the decorator in the code snippet is to add behavior before and after a function is called, such as printing messages.', 'The initial decorator implementation replaces the original function with a new function, causing the original function name, docstring, and annotations to be lost.', "The issue of losing the original function attributes can be addressed by using the functools module's wraps decorator, which preserves attributes like the function name, docstring, annotations, and module.", 'A decorator Factory is a function that returns a decorator. It allows for customization of decorators by accepting arguments to configure the behavior of the decorator.', "The purpose of the 'deck2' decorator function is to print a greeting message before calling the original function and then print a farewell message after the function execution.", "The variables used in the 'deck2' decorator function are 'greeting' and 'farewell', which are passed as arguments to the decorator.", "The 'deck2' decorator function is called using the '@' symbol before the function definition, and it is used to decorate the original function by adding the greeting and farewell messages around the function execution.", 'The two common decorators in Python are property and classmethod.', 'The property decorator turns a zero-argument method into what looks like an attribute, allowing the speaker to have a computed function that looks like an attribute.', "The classmethod decorator allows a function to be called from the class itself or an instance of the class, with the first argument conventionally named 'cls' pointing to the class that the method is called from."]))
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
