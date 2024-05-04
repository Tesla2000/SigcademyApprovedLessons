import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the main topic of the video?', "Why does the speaker prefer using Ray's keyboard interrupt without parentheses?", "What is the main difference in execution when using 'raise' with just a type name in Python?", 'How can avoiding instantiation of exception objects impact performance in Python code?', 'Can the speaker provide an example of how avoiding instantiation of exception objects caused a bug in C code?', "What is the purpose of using 'raise' in Python?", 'How does the signal handler in C Python handle keyboard interrupts?', 'What is the role of the C API in handling exceptions in Python?', 'What was the issue the speaker encountered while trying to reproduce a bug in Python?', 'How did the speaker fix the bug related to exception handling in Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the main topic of the video?', "Why does the speaker prefer using Ray's keyboard interrupt without parentheses?", "What is the main difference in execution when using 'raise' with just a type name in Python?", 'How can avoiding instantiation of exception objects impact performance in Python code?', 'Can the speaker provide an example of how avoiding instantiation of exception objects caused a bug in C code?', "What is the purpose of using 'raise' in Python?", 'How does the signal handler in C Python handle keyboard interrupts?', 'What is the role of the C API in handling exceptions in Python?', 'What was the issue the speaker encountered while trying to reproduce a bug in Python?', 'How did the speaker fix the bug related to exception handling in Python?'], ["The main topic of the video is about the difference between using Ray's keyboard interrupt with parentheses and without parentheses in Python code.", "The speaker prefers using Ray's keyboard interrupt without parentheses because it is slightly faster in execution compared to using it with parentheses. The difference in speed is due to one fewer opcode being run in the code without parentheses.", "The main difference in execution is that when using 'raise' with just a type name, the object is instantiated with zero arguments as needed. This can be beneficial in cases where the exception object does not need to be inspected, leading to better performance.", 'Avoiding instantiation of exception objects can improve performance in cases where exceptions are raised frequently or in performance-critical sections of the code. By only instantiating the exception object when necessary, unnecessary overhead can be avoided.', 'In a C codebase, avoiding instantiation of exception objects can lead to unexpected behavior when catching exceptions. An example of this is a bug in the libsass Python library where not instantiating the exception object properly resulted in a segfault and a C stack trace during exception handling.', "The 'raise' keyword in Python is used to raise an exception. It can be used to signal that an error or exceptional condition has occurred during the execution of a program.", 'The signal handler in C Python is responsible for setting the keyboard interrupt exception and unwinding the stack when a keyboard interrupt (Ctrl+C) occurs. This allows the program to gracefully handle the interrupt and perform any necessary cleanup operations.', 'The C API in Python provides functions and mechanisms for handling exceptions, including setting exception values and traceback information. It allows for low-level manipulation of exceptions in Python code.', 'I encountered an issue where the exception value and traceback were not properly set when raising an exception in Python. This led to difficulties in reproducing the bug and identifying the root cause of the issue.', "I fixed the bug by calling the 'PyErr_NormalizeException' C API function, which ensures that the exception value and traceback are properly set when raising an exception. This resolved the issue and allowed for proper handling of exceptions in the program."]))
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
