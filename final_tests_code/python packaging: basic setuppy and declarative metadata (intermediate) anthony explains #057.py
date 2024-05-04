import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the name of the Python package being created in the video?', 'What is the version number set for the Python package in the setup.py file?', 'Who is listed as the author of the Python package in the setup.py file?', 'What is the description of the Python package in the setup.py file?', 'What is the URL specified for the Python package in the setup.py file?', 'What does the find_packages helper from setuptools do?', 'Why is using find_packages helpful as your package grows?', 'How can the speaker exclude specific directories when using find_packages?', 'What is the purpose of adding an entry point in packaging metadata?', "What is the purpose of the tool 'setup-pi-upgrade'?", 'What is the benefit of using declarative metadata over code-based setup.py files?', "Can the speaker explain the functionality of the tool 'setup-cfg-format'?"]
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the name of the Python package being created in the video?', 'What is the version number set for the Python package in the setup.py file?', 'Who is listed as the author of the Python package in the setup.py file?', 'What is the description of the Python package in the setup.py file?', 'What is the URL specified for the Python package in the setup.py file?', 'What does the find_packages helper from setuptools do?', 'Why is using find_packages helpful as your package grows?', 'How can the speaker exclude specific directories when using find_packages?', 'What is the purpose of adding an entry point in packaging metadata?', "What is the purpose of the tool 'setup-pi-upgrade'?", 'What is the benefit of using declarative metadata over code-based setup.py files?', "Can the speaker explain the functionality of the tool 'setup-cfg-format'?"], ['hello world', '1', 'Anthony Sottile', 'This package contains some sample hello world code.', 'github.com/acetylene/hello-world', 'The find_packages helper from setuptools iterates over the file system to look for directories that contain __init__.py files and automatically adds them to the packaging metadata.', 'Using find_packages is helpful as your package grows because it automates the process of adding new directories to the packaging metadata, reducing the chances of errors and the need to manually synchronize with the file system.', "You can exclude specific directories when using find_packages by passing the 'exclude' parameter with the directories the speaker want to exclude, such as 'test*' and 'testing*' in a tuple.", 'Adding an entry point in packaging metadata allows the speaker to run the package as a program directly without having to run it as a module. It specifies the executable name and the module path with the attribute to be executed.', "The purpose of the tool 'setup-pi-upgrade' is to automatically upgrade setup.py files to declarative metadata format, which stores metadata as data instead of code, making it easier to modify and rewrite.", 'Declarative metadata is easier to modify and rewrite compared to code-based setup.py files, as it stores metadata as data, making it simpler to work with and manage.', "The tool 'setup-cfg-format' is a code formatter that normalizes the output of setup.cfg files and adds helpful fields. It can also format classifiers and automatically add license information if a license file is present."]))
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
