import random
import langchain_openai
import langchain_core
def generate_questions() -> list[str]:
    questions = ["Why don't the speaker install pip or virtualenv globally on your Linux system?", 'What is the reason for not changing the version of eurolib 3 installed globally?', 'How does the user make virtualenv available for the rest of the system?']
    return random.sample(questions, min(len(questions), 5))


def generate_answers(question: str, answer: str, _: str) -> bool | str:
    reference_answers = dict(zip(["Why don't the speaker install pip or virtualenv globally on your Linux system?", 'What is the reason for not changing the version of eurolib 3 installed globally?', 'How does the user make virtualenv available for the rest of the system?'], ["There are three main reasons why I don't install packages globally on my Linux system:\n1. I don't have root access on some machines, so I need to use user space to install packages without requiring root permissions.\n2. Debian modifies the packages of pip and virtualenv, leading to performance issues and unnecessary package installations. I prefer using upstream packages maintained by the original maintainers.\n3. Installing packages to the system can potentially break system packages that depend on specific Python packages, causing compatibility issues.", 'Changing the version of eurolib 3 installed globally can potentially break the operating system and other components, even inside a Docker container.', 'The user makes virtualenv available for the rest of the system by creating a virtualenv inside their home directory, installing packages regularly in that virtualenv, and creating a symbolic link in the bin directory of their home directory to the virtualenv installation location.']))
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
