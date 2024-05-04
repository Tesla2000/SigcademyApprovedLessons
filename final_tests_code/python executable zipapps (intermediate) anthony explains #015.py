import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the main topic of the video?', 'How can the speaker create a zip file containing a Python script?', 'What is the purpose of zipping up Python files as mentioned in the video?', 'Which Python module makes it easier to build zip apps in Python 3.5?', 'What command can be used to initialize Virtualenv without pip installing Virtualenv?', 'What is the file format of the executable binary data mentioned in the text?', 'How can Python be used to unzip the zip file even though it does not have zip data at the front of it?', 'What is an example of another file in Python that is actually a zip file?', 'How can the speaker import code from a wheel file in Python?', 'What are some limitations of zip apps in Python?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the main topic of the video?', 'How can the speaker create a zip file containing a Python script?', 'What is the purpose of zipping up Python files as mentioned in the video?', 'Which Python module makes it easier to build zip apps in Python 3.5?', 'What command can be used to initialize Virtualenv without pip installing Virtualenv?', 'What is the file format of the executable binary data mentioned in the text?', 'How can Python be used to unzip the zip file even though it does not have zip data at the front of it?', 'What is an example of another file in Python that is actually a zip file?', 'How can the speaker import code from a wheel file in Python?', 'What are some limitations of zip apps in Python?'], ["Explaining Python's zip applications and similar technologies.", "You can create a zip file containing a Python script by adding the Python script file (e.g., main.py) to a zip archive using a command like 'zip -r archive.zip main.py'.", 'The purpose of zipping up Python files is to create executable zip files that can run as Python scripts, similar to how Java jars work.', 'The zipapp module makes it easier to build zip apps in Python 3.5.', "The command 'python3 vmf' can be used to initialize Virtualenv without pip installing Virtualenv.", 'The file format is a zip file with a shebang at the beginning.', 'Python can recognize and unzip the file because it natively supports executing zip files, allowing for distribution of executables without the need to run them with Python explicitly.', "An example is a wheel file, such as the 'asd_pretty-2.0-py2.3-non-any.whl' file, which contains packaging metadata and Python code inside of it.", 'You can set the Python path to the wheel file and then run an interpreter to import and execute the code from the wheel file.', 'One limitation is that the speaker cannot natively include binary modules like C extensions in zip apps. Tools like Pex, Shiv, and XAR can help overcome this limitation.']))
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
