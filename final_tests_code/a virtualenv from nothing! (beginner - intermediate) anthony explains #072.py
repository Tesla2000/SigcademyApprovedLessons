import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ['What is the pattern discussed in the video?', 'What are the two different ways shown to create a virtual environment?', 'Which module is used to create a virtual environment in Python?', 'Why might the `venv` module not be available on some Linux distributions?', "How can the speaker install the `venv` module on Debian systems if it's not available by default?", 'Which method is faster for creating a virtual environment, `venv` or `virtualenv`?', 'What file do the speaker need to download to create a virtual environment using the `virtualenv` module?', 'What is the command used to download the virtualenv.pi z file?', 'How do the speaker run the virtualenv.pi z file to create a virtual environment?', 'Why would the speaker bootstrap a virtual environment from nothing?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(['What is the pattern discussed in the video?', 'What are the two different ways shown to create a virtual environment?', 'Which module is used to create a virtual environment in Python?', 'Why might the `venv` module not be available on some Linux distributions?', "How can the speaker install the `venv` module on Debian systems if it's not available by default?", 'Which method is faster for creating a virtual environment, `venv` or `virtualenv`?', 'What file do the speaker need to download to create a virtual environment using the `virtualenv` module?', 'What is the command used to download the virtualenv.pi z file?', 'How do the speaker run the virtualenv.pi z file to create a virtual environment?', 'Why would the speaker bootstrap a virtual environment from nothing?'], ['Creating a virtual environment from scratch using Python.', 'Using the `venv` module and the `virtualenv` module.', '`venv` module.', 'Some Linux distributions, like Ubuntu or Debian, may choose to leave out the `venv` module.', 'You can install the `venv` module on Debian systems by using `sudo apt install python3-venv` for the specific Python version the speaker are using.', '`virtualenv` is faster for creating a virtual environment compared to `venv`.', 'You need to download the `virtualenv.pyz` file from `bootstrap.pypa.io`.', 'curl virtualenv.pi z', 'python3 virtualenv.pi z <virtualenv_name>', "In situations like a siege route, a docker container where you're not allowed to install packages, or to manage packages in your home directory without needing a global installation of pip or virtualenv."]))
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
