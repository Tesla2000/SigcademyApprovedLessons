import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of customizing the Python interactive prompt?', "How can the speaker modify the behavior of the 'exit' command in the Python interpreter?", 'What is a Python startup file and how can it be used to customize the Python interpreter?', 'What issue does the code snippet address regarding tab completion in Python 2?', 'What is the purpose of importing rl completer in the startup file?', 'How can the speaker enable tab completion in Python 2 by modifying the startup file?', 'What is an example of adding a shortcut for a commonly used function in the startup file?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of customizing the Python interactive prompt?', "How can the speaker modify the behavior of the 'exit' command in the Python interpreter?", 'What is a Python startup file and how can it be used to customize the Python interpreter?', 'What issue does the code snippet address regarding tab completion in Python 2?', 'What is the purpose of importing rl completer in the startup file?', 'How can the speaker enable tab completion in Python 2 by modifying the startup file?', 'What is an example of adding a shortcut for a commonly used function in the startup file?'], ['The purpose of customizing the Python interactive prompt is to enhance the user experience and make the interpreter more user-friendly by modifying its behavior and appearance.', "You can modify the behavior of the 'exit' command in the Python interpreter by changing the wrapper function of the 'exit' object to have a side effect that causes the interpreter to exit when 'exit' is typed.", "A Python startup file is a script that is executed when the Python interpreter starts. It can be used to customize the Python interpreter by setting environment variables like 'python startup' to point to the startup file, which contains code to modify the interpreter's behavior.", 'The code snippet addresses the issue in Python 2 where tab completion did not work as expected, and typing a tab would result in literal tab characters instead of showing attributes of modules. The code modifies readline to enable tab completion in Python 2.', 'The import of rl completer in the startup file sets up tab completion in Python 2.', 'By setting the Python startup file to startup.pi and importing os, tab completion can be enabled in Python 2.', "An example is adding a shortcut for the 'pprint' function by importing pprint and defining a shortcut like 'pp' in the startup file."]))
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
