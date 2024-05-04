import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the purpose of a virtual environment in Python?', 'Why is it recommended to use virtual environments in Python?', 'What are the drawbacks of installing Python packages globally on your system?', 'What is the first difference between virtualenv and the vm module?', 'How do the speaker activate a virtualenv on POSIX platforms?', 'What environment variable is set when activating a virtualenv?', 'What does activating a virtualenv do to the executable search path?', 'How do the speaker activate a virtualenv on Windows?', 'What is the benefit of installing packages in a virtual environment instead of globally on the machine?', 'What are some advantages of using virtualenv?', 'What is a downside of using virtualenv?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the purpose of a virtual environment in Python?', 'Why is it recommended to use virtual environments in Python?', 'What are the drawbacks of installing Python packages globally on your system?', 'What is the first difference between virtualenv and the vm module?', 'How do the speaker activate a virtualenv on POSIX platforms?', 'What environment variable is set when activating a virtualenv?', 'What does activating a virtualenv do to the executable search path?', 'How do the speaker activate a virtualenv on Windows?', 'What is the benefit of installing packages in a virtual environment instead of globally on the machine?', 'What are some advantages of using virtualenv?', 'What is a downside of using virtualenv?'], ['A virtual environment allows the speaker to install Python packages in an isolated fashion, preventing conflicts with system packages and allowing for better control over package versions.', 'It is recommended to use virtual environments in Python to avoid conflicts with system packages, ensure consistent package versions, and have better control over the Python environment for your projects.', 'Installing Python packages globally on your system can lead to conflicts with system packages, dependency issues, and difficulties in managing package versions. It can also make it challenging to work with different versions of Python for different projects.', 'The first difference is that virtualenv is significantly faster than running the vm module due to the way virtualenv caches packages and avoids reaching out to the internet for installations.', "To activate a virtualenv on POSIX platforms, the speaker use the command 'source /path/to/virtualenv/bin/activate' which sets up the virtual environment and environment variables.", "The environment variable 'virtual_env' is set when activating a virtualenv, which is a path to the virtual environment directory.", "Activating a virtualenv puts the path to the 'bin' directory of the virtual environment at the beginning of the executable search path, ensuring that commands point to the virtual environment's executables.", "On Windows, the speaker activate a virtualenv by running the 'activate' script directly in the 'Scripts' directory. There is no 'source' command like in POSIX platforms.", 'Installing packages in a virtual environment isolates them from the system, preventing pollution of the global environment and ensuring dependencies are contained within the virtual environment.', '1. Ships with Python, making it generally available.\n2. Works with Python 2 if needed.\n3. Allows for creating virtual environments with different Python versions.', 'Cannot create virtual environments with different Python versions.']))
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
