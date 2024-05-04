import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["What is the deal with 'blank accept' and why should I use 'accept exception'?", "What is the difference between 'blank accept' and 'accept exception'?", 'What is the example code trying to demonstrate?', 'What issue does the code highlight with catching all exceptions using a broad except clause?', 'How can the speaker forcefully terminate a program that is not responding to Ctrl+C due to a broad except clause?', "What is the recommended practice when using 'except BaseException' in Python?", 'What is the difference between accepting exceptions in Python 2 and Python 3?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["What is the deal with 'blank accept' and why should I use 'accept exception'?", "What is the difference between 'blank accept' and 'accept exception'?", 'What is the example code trying to demonstrate?', 'What issue does the code highlight with catching all exceptions using a broad except clause?', 'How can the speaker forcefully terminate a program that is not responding to Ctrl+C due to a broad except clause?', "What is the recommended practice when using 'except BaseException' in Python?", 'What is the difference between accepting exceptions in Python 2 and Python 3?'], ["The 'blank accept' statement is discouraged because it catches all exceptions, including system-level exceptions like SystemExit and KeyboardInterrupt, which should not be caught unless the speaker plan to re-raise them. Instead, it is recommended to use 'accept exception' which specifically catches exceptions that inherit from the 'Exception' class, ensuring that system-level exceptions are not caught unintentionally.", "The main difference between 'blank accept' and 'accept exception' is that 'blank accept' catches all exceptions, including system-level exceptions, while 'accept exception' specifically catches exceptions that inherit from the 'Exception' class. By using 'accept exception', the speaker can avoid unintentionally catching critical system-level exceptions like SystemExit and KeyboardInterrupt.", 'The example code demonstrates the importance of handling exceptions properly in Python, specifically avoiding catching all exceptions using a broad except clause.', 'Catching all exceptions using a broad except clause can lead to unexpected behavior, such as preventing the program from terminating properly when a KeyboardInterrupt (Ctrl+C) is sent.', 'You can use Ctrl+\\ to send a SIGQUIT signal, which triggers a core dump and can forcibly terminate the program that is not responding to Ctrl+C.', "When using 'except BaseException', it is recommended to either re-raise the exception or raise a different exception to handle the error explicitly and maintain proper program behavior.", 'In Python 2, the speaker could raise exceptions that are just strings, but in Python 3, the speaker raise exception classes as part of the class hierarchy. This change occurred in Python 2.7. In Python 2, the speaker could raise string exceptions, while in Python 3, the speaker raise old-style classes as exceptions. The old-style classes do not participate in the exception hierarchy.']))
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
